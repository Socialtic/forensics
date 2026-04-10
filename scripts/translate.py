"""
translate.py

Translate Markdown documentation either via direct CLI parameters or
automatically based on recent git changes.

USAGE (CLI mode):
    translate.py [-h] [-f FILE] [-s SOURCE_LANG] [-t TARGETS ...] [-o OUTPUT_DIR]

OPTIONS:
    -f FILE, --file FILE
        Path to the source file to translate.
    -s SOURCE_LANG, --source-lang SOURCE_LANG
        Source language code (required only when -f is used).
    -t TARGETS [TARGETS ...], --targets TARGETS [TARGETS ...]
        One or more target language codes (required only when -f is used).
    -o OUTPUT_DIR, --output-dir OUTPUT_DIR
        Optional output directory. Defaults to the same directory as the source file.

BEHAVIOR:
1. Translation with parameters (CLI mode)
    - When parameters are provided, the script translates the entire document.
    - If no output directory is specified, the translated file is saved alongside
      the source file.

2. Automatic translation based on git diff (auto mode)
    - If no parameters are provided, the script inspects the latest git commit
      and identifies modified files.
    - For each modified file, the script checks the "auto-translate" flag
      embedded in the file metadata:
        • If auto-translate is true, then the file is automatically translated.
        • If auto-translate is false or not present, then no translation occurs.
    - The source language is inferred from the file path. All other specified languages are used as targets.
    - If the modified file has never been translated before:
        • The full content is translated using the DeepL API.
    - If the file already has a live translation:
        • Only added or modified lines are translated.
        • Translations are inserted in the appropriate locations.
    - The script does not remove or replace lines. 
"""



import os
import subprocess
from pathlib import Path
import deepl
import re
import argparse
from typing import List
import concurrent.futures
import threading, sys



# ==== Configuration parameters ======

# Keys and variables. Remove language if you do not want to automatically translate
DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")
ALL_LANGS = ["es", "pt"]
ROOT_DIR = Path("docs")
MAX_CHARS_PER_RUN = 200_000       # hard safety cap ~40-80 pages to translate per run max
MAX_CHARS_PER_REQUEST = 5_000     # soft cap for tanslation per request
_run_char_count = 0
DEFAULT_TRANSLATION_TIMEOUT = 10  # Stop if a 5000 chunk takes longer than 10s to translate


# DeepL API language codes mapping
LANG_MAP = {
    "en": "EN-US",
    "es": "ES",
    "pt": "PT-BR",
}

# Add here meta-data that should be ignored
METADATA_KEYS = [
    "title:",
    "summary:",
    "keywords:",
    "author:",
    "lang:",
    "tags:",
    "last_updated:",
    "some_url:",
    "icon:",
    "auto-translate:",
    "translation-review-pending:",
    "type =",
    "title =",
    "layout =",
    "weight =",
    "toc = true ="
]

# Check and initialize translator using deepl python packages
if not DEEPL_API_KEY:
    raise ValueError("Missing API key")
translator = deepl.Translator(DEEPL_API_KEY)  

# tolerant front-matter key/value regex
_KEY_RE = re.compile(r"^([a-zA-Z0-9_\-]+)\s*:\s*(.+)$")



# ======= Methods and functions  ===============


# -------------------------
# Helper: Watchdog to kill the process in case it reaches a defined time. This is to preventing haning and consuming quota.   
# -------------------------

def start_watchdog(seconds=300):
    def kill():
        print("ERROR: Translation watchdog triggered — aborting.")
        sys.exit(1)
    t = threading.Timer(seconds, kill)
    t.daemon = True
    t.start()
    return t

# -------------------------
# Helper: get deepl API quota  
# -------------------------
def get_deepl_character_quota(translator):
    usage = translator.get_usage()

    # Text translation quota (what translate_text uses)
    detail = getattr(usage, "_character", None)

    if detail is None:
        raise RuntimeError(
            f"DeepL usage object does not expose character quota: {vars(usage)}"
        )

    used = getattr(detail, "count", None)
    limit = getattr(detail, "limit", None)

    if used is None or limit is None:
        raise RuntimeError(
            f"Unable to read DeepL character quota: {vars(detail)}"
        )

    return used, limit

# -------------------------
# Helper: parser for mardown metadata, returns type, header and body of metadata 
# -------------------------

def split_front_matter(text: str):
    if not text:
        return None, "", text
    s = text.lstrip("\ufeff")
    if s.startswith("---"):
        parts = s.split("---", 2)
        if len(parts) >= 3:
            header = parts[1]
            body = parts[2].lstrip("\r\n")
            return "yaml", header, body
        return None, "", text
    if s.startswith("+++"):
        parts = s.split("+++", 2)
        if len(parts) >= 3:
            header = parts[1]
            body = parts[2].lstrip("\r\n")
            return "toml", header, body
        return None, "", text
    return None, "", text


# -------------------------
# Helper: CLI argument parsing
# -------------------------
def parse_cli_args():
    parser = argparse.ArgumentParser(description="Translate docs (diff mode or single-file CLI).")

    parser.add_argument(
        "-f", "--file",
        type=str,
        help="Source file to translate (CLI mode)."
    )

    parser.add_argument(
        "-s", "--source-lang",
        type=str,
        help="Source language code (required only when -f is used)."
    )

    parser.add_argument(
        "-t", "--targets",
        type=str,
        nargs="+",
        help="Target languages (required only when -f is used)."
    )

    parser.add_argument(
        "-o", "--output-dir",
        type=str,
        help="Optional output directory for CLI mode."
    )
    return parser.parse_args()


# -------------------------
# Helper: build CLI target filename (append -<lang> before extension)
# -------------------------
def build_cli_target_path(src_file: Path, target_lang: str, output_dir: Path | None = None) -> Path:

    suffix = "".join(src_file.suffixes)
    stem = src_file.stem
    new_name = f"{stem}-{target_lang}{suffix}"

    if output_dir:
        return output_dir / new_name
    else:
        return src_file.with_name(new_name)

# -------------------------
# Helper: read markdown meta-data from key->value pair
# -------------------------
def read_front_matter(text: str) -> dict:
    if not text:
        return {}
    s = text.lstrip("\ufeff\r\n\t ")
    if not s.startswith("---"):
        return {}
    parts = s.split("---", 2)
    if len(parts) < 3:
        return {}
    header = parts[1]
    out = {}
    for line in header.splitlines():
        m = _KEY_RE.match(line.strip())
        if m:
            k = m.group(1).strip()
            v = m.group(2).strip()
            # normalize booleans
            if v.lower() in ("true", "yes", "1"):
                out[k] = True
            elif v.lower() in ("false", "no", "0"):
                out[k] = False
            else:
                out[k] = v
    return out

# -------------------------
# Helper: update markdown meta-data
# -------------------------
def update_front_matter(text: str, key: str, value) -> str:
    val_str = "true" if value is True else ("false" if value is False else str(value))
    s = text.lstrip("\ufeff\r\n\t ")
    prefix_ws = ""
    if text and not text.startswith(s):
        # preserve leading whitespace/BOM
        prefix_ws = text[: len(text) - len(s)]
    if s.startswith("---"):
        parts = s.split("---", 2)
        if len(parts) >= 3:
            header = parts[1]
            body = parts[2]
            # build header lines, update key if exists
            lines = [ln for ln in header.splitlines()]
            for i, ln in enumerate(lines):
                if ln.strip().startswith(f"{key}:"):
                    lines[i] = f"{key}: {val_str}"
                    break
            else:
                # append the key before closing
                lines.append(f"{key}: {val_str}")
            new_header = "\n".join(lines) + "\n"
            return prefix_ws + "---" + new_header + "---" + body
    # no front matter -> create a new block
    new_block = f"---\n{key}: {val_str}\n---\n\n"
    return prefix_ws + new_block + text

# -------------------------
# Gets paths of any .md file changed in the last commit
# -------------------------
def get_changed_markdown_files() -> list[Path]:
    result = subprocess.run(
        ["git", "diff", "--name-only", "HEAD~1", "HEAD"],
        capture_output=True,
        text=True,
        check=True,
    )
    changed = [
        Path(f)
        for f in result.stdout.splitlines()
        if f.startswith(f"{ROOT_DIR}/") and f.endswith(".md")
    ]
    return changed

# -------------------------
# Detect the language of the files being changed
# -------------------------
def detect_language(file_path: Path) -> str:
    print(f"DEBUG file: {file_path}")
    parts = file_path.parts
    try:
        lang_index = parts.index("docs") + 1
        lang = parts[lang_index]
        print(f"DEBUG lang: {lang}")
        if lang not in ALL_LANGS:
            raise ValueError(f"Language not defined for automatic translations: {lang}")
        return lang
    except (ValueError, IndexError):
        raise RuntimeError(f"Could not determine language for {file_path}")

# -------------------------
# Return a list (line_number, text added) for each new line based on the git diff
# -------------------------
def get_added_lines_with_context(file_path: Path):
    diff = subprocess.run(
        ["git", "diff", "-U0", "HEAD~1", "HEAD", "--", str(file_path)],
        capture_output=True,
        text=True,
        check=True,
    ).stdout

    added_lines = []
    current_line_number = None

    # Parse the diff to understand what type of change, focus on additions
    for line in diff.splitlines():
        if line.startswith("@@"):
            # Parse hunk header, e.g. "@@ -10,0 +11,3 @@"
            plus_part = line.split("+")[1].split(" ")[0]
            start_line = int(plus_part.split(",")[0])
            current_line_number = start_line
        elif line.startswith("+") and not line.startswith("+++"):
            added_lines.append((current_line_number, line[1:].rstrip()))
            current_line_number += 1
        elif line.startswith("-") and not line.startswith("---"):
            # Ignore deletions entirely
            continue

    return added_lines


# -------------------------
# Helper: split in chunks of a determined size to avoid consuming api quota
# -------------------------
def chunk_text(text: str, size: int):
    for i in range(0, len(text), size):
        yield text[i:i + size]

# -------------------------
# Helper: Count characters in CLI mode
# -------------------------
def estimate_cli_chars(src_text: str) -> int:
    fm_type, _, body = split_front_matter(src_text)
    text = body if fm_type is not None else src_text
    return len(text)


# -------------------------
# Helper: Count characters in git diff mode
# -------------------------
def estimate_diff_chars(added_lines) -> int:
    total = 0
    for _, line in added_lines:
        stripped = line.strip()
        if (
            not stripped
            or stripped.startswith("---")
            or stripped.startswith("+++")
            or stripped.startswith("```")
            or stripped.lower().startswith("<!--")
            or any(stripped.startswith(k) for k in METADATA_KEYS)
        ):
            continue
        total += len(line)
    return total

# -------------------------
# Helper: Translate text of arbitrary size by chunking safely.
# -------------------------
def translate_large_text(text: str, src_lang: str, tgt_lang: str) -> str:
    if len(text) <= MAX_CHARS_PER_REQUEST:
        return translate_text(text, src_lang, tgt_lang)

    translated_chunks = []
    for chunk in chunk_text(text, MAX_CHARS_PER_REQUEST):
        translated_chunks.append(
            translate_text(chunk, src_lang, tgt_lang)
        )

    return "".join(translated_chunks)


# -------------------------
# Use deepl API to make the necessary translations 
# -------------------------
def translate_text(text: str, src_lang: str, target_lang: str) -> str:
    
    global _run_char_count
    char_count = len(text)

    # Hard per-request limit
    if char_count > MAX_CHARS_PER_REQUEST:
        raise RuntimeError(
            f"Single translation chunk too large: {char_count} chars "
            f"(limit: {MAX_CHARS_PER_REQUEST})"
        )

    # Hard per-run limit
    if _run_char_count + char_count > MAX_CHARS_PER_RUN:
        raise RuntimeError(
            f"Translation budget exceeded: "
            f"{_run_char_count + char_count} > {MAX_CHARS_PER_RUN} chars"
        )

    _run_char_count += char_count

    print(
        f"[DeepL] Translating {char_count} chars "
        f"(run total: {_run_char_count}/{MAX_CHARS_PER_RUN}) "
        f"{src_lang} → {target_lang}"
    )


    
    tgt_code = LANG_MAP.get(target_lang, target_lang).upper()
    src_code = src_lang.upper()

    def _call():
        return translator.translate_text(
            text,
            source_lang=src_code,
            target_lang=tgt_code,
            outline_detection=False,
            non_splitting_tags=["code", "pre"],
        ).text

    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as ex:
        future = ex.submit(_call)
        try:
            return future.result(timeout=DEFAULT_TRANSLATION_TIMEOUT)
        except concurrent.futures.TimeoutError:
            raise RuntimeError(
                f"DeepL translation timed out after {timeout}s "
                f"(src={src_lang}, tgt={target_lang}, chars={char_count})"
            )



# -------------------------
# Translate full file if targed does not exist, otherwise append translation in line
# -------------------------
def patch_translation_file(source_path: Path, target_path: Path, added_lines):
    
    src_lang = detect_language(source_path)
    tgt_lang = detect_language(target_path)


    # If the target file doesn’t exist, translate everything but copy front-matter verbatim
    if not target_path.exists():
        print(f" {target_path} missing. Translating full file.")

        src_text = source_path.read_text(encoding="utf-8")
        fm_type, header, body = split_front_matter(src_text)  # returns fm_type: "yaml"/"toml"/None

        # Determine what to translate: prefer body if front-matter exists, otherwise the whole text
        if fm_type is not None:
            text_to_translate = body
        else:
            text_to_translate = src_text

        # Translate only the body text (or the full text if there was no front-matter)
        try:
            translated_body = translate_large_text(text_to_translate, src_lang, tgt_lang)
        except concurrent.futures.TimeoutError:
            print("ERROR: DeepL translation timed out")
            sys.exit(1)

        # Build the resulting front-matter: copy header verbatim, but append translation-review-pending if missing
        if fm_type == "toml":
            # TOML header delimiter + header content is in `header`
            header_lines = [
                ln for ln in header.splitlines()
                if not re.match(r"\s*auto[-_]?translate\s*[:=]", ln, re.IGNORECASE)
            ]
            # check presence (accept key forms: translation-review-pending or translation_review_pending)
            if not any(re.search(r"translation[-_]?review[-_]?pending\s*=", ln, re.IGNORECASE) for ln in header_lines):
                header_lines.append('translation-review-pending = true')
            new_header = "\n".join(header_lines).rstrip() + "\n"
            final_text = f"+++\n{new_header}+++\n\n{translated_body.lstrip()}"
        elif fm_type == "yaml":
            header_lines = [
                ln for ln in (header.splitlines() if header else [])
                if not re.match(r"\s*auto[-_]?translate\s*[:=]", ln, re.IGNORECASE)
            ]
            if not any(re.search(r"translation[-_]?review[-_]?pending\s*:", ln, re.IGNORECASE) for ln in header_lines):
                header_lines.append('translation-review-pending: true')
            new_header = "\n".join(header_lines).rstrip() + "\n"
            final_text = f"---\n{new_header}---\n\n{translated_body.lstrip()}"
        else:
            # No front matter in source — create basic YAML front-matter with review flag
            new_header = "translation-review-pending: true\n"
            final_text = f"---\n{new_header}---\n\n{translated_body.lstrip()}"

        # Write target
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_text(final_text, encoding="utf-8")
        print(f"Created {target_path} (front-matter copied; translation-review-pending set).")
        return


    # If there are no new lines, nothing to patch
    if not added_lines:
        print(f" No additions detected in {source_path}")
        return

    tgt_lines = target_path.read_text(encoding="utf-8").splitlines()

    # Insert translated additions at same relative line number, skip blank lines. 
    for line_num, added_text in added_lines:
        stripped = added_text.strip()
        # Skip empty lines or structural/non-translatable content
        if (
            not stripped
            or stripped.startswith("---")      # YAML front matter
            or stripped.startswith("+++")      # YAML front matter
            or stripped.startswith("<") and stripped.endswith(">")
            or stripped.startswith("```")      # code fences
            or stripped.lower().startswith("<!--")  # HTML comments
            or any(stripped.startswith(key) for key in METADATA_KEYS)  # metadata fields
        ):
            print(f"Skipping line: {stripped}")
            continue

        translated = translate_text(added_text, src_lang, tgt_lang)
        insert_index = min(line_num - 1, len(tgt_lines))
        tgt_lines.insert(insert_index, translated)
        print(f"Inserted translation at line {insert_index+1} in {target_path}")

    # Add or update metadata flag, mark file as needing review after script edits
    final_text = "\n".join(tgt_lines)
    final_text = update_front_matter(final_text, "translation-review-pending", True)
    target_path.write_text(final_text, encoding="utf-8")
    print(f"Updated {target_path} and set translation-review-pending: true")


# ============================ MAIN ===============================

def main():

    watchdog = start_watchdog(300)  # 5 minutes hard cap for the run
 
    used, limit = get_deepl_character_quota(translator)
    remaining = limit - used

    print(f"DeepL character quota before run: {used}/{limit} (remaining: {remaining})")



    try:

        args = parse_cli_args()

        # -------------------------
        # CLI MODE (only when -f provided)
        # -------------------------

        if args.file:
            src_path = Path(args.file)
            if not src_path.exists():
                print(f"Source file not found: {src_path}")
                return

            # source language mandatory in CLI mode
            src_lang = getattr(args, "source_lang", None)
            if not src_lang:
                raise ValueError("CLI mode requires -s / --source-lang")

            # targets required
            raw_targets = getattr(args, "targets", None)
            if not raw_targets:
                raise ValueError("CLI mode requires -t / --targets")
            requested = raw_targets if isinstance(raw_targets, (list, tuple)) else [raw_targets]
            target_langs = [t for t in requested if t in ALL_LANGS]
            if not target_langs:
                raise ValueError("No valid target languages provided")

            # output dir (optional)
            output_dir_arg = getattr(args, "output_dir", None)
            output_dir = Path(output_dir_arg).expanduser() if output_dir_arg else None
            if output_dir:
                output_dir.mkdir(parents=True, exist_ok=True)

            # read source file once
            src_text = src_path.read_text(encoding="utf-8")

            # estimate characters to translate
            estimated = estimate_cli_chars(src_text)
            print(f"Estimated characters to translate: {estimated}")

            # split front-matter (robust helper)
            fm_type, header, body = split_front_matter(src_text)

            # decide text to translate: the body if front-matter exists, else whole file
            text_to_translate = body if fm_type is not None else src_text

            # abort if not enough characters to tranlsate 
            used, limit = get_deepl_character_quota(translator)
            remaining = limit - used

            SAFETY_BUFFER = 1000

            if estimated + SAFETY_BUFFER > remaining: #raise error if file is larger than available quota
                raise RuntimeError(
                    f"Insufficient DeepL quota:\n"
                    f"  Needed (est.): {estimated}\n"
                    f"  Remaining:    {remaining}\n"
                    f"  Buffer:       {SAFETY_BUFFER}"
    )

            print(f"CLI MODE: Translating {src_path} ({src_lang}) → {target_langs}")

            for lang in target_langs:
                tgt_path = build_cli_target_path(src_path, lang, output_dir)

                # translate only the body
                translated_body = translate_large_text(text_to_translate, src_lang, lang)

                # build header for target: copy header verbatim if present, ensure review flag is present
                if fm_type == "toml":
                    header_lines = [
                        ln for ln in (header.splitlines() if header else [])
                        if not re.match(r"\s*auto[-_]?translate\s*[:=]", ln, re.IGNORECASE)
                    ]
                    if not any(re.search(r"translation[-_]?review[-_]?pending\s*=", ln, re.IGNORECASE) for ln in header_lines):
                        header_lines.append('translation-review-pending = true')
                    new_header = "\n".join(header_lines).rstrip() + "\n"
                    final_text = f"+++\n{new_header}+++\n\n{translated_body.lstrip()}"
                elif fm_type == "yaml":
                    header_lines = [
                        ln for ln in (header.splitlines() if header else [])
                        if not re.match(r"\s*auto[-_]?translate\s*[:=]", ln, re.IGNORECASE)
                    ]
                    if not any(re.search(r"translation[-_]?review[-_]?pending\s*:", ln, re.IGNORECASE) for ln in header_lines):
                        header_lines.append('translation-review-pending: true')
                    new_header = "\n".join(header_lines).rstrip() + "\n"
                    final_text = f"---\n{new_header}---\n\n{translated_body.lstrip()}"
                else:
                    # no front-matter -> create YAML block with review flag
                    final_text = f"---\ntranslation-review-pending: true\n---\n\n{translated_body.lstrip()}"

                # write target
                tgt_path.parent.mkdir(parents=True, exist_ok=True)
                tgt_path.write_text(final_text, encoding="utf-8")
                print(f"Written translation: {tgt_path}")

            return  # stop; do not fall through to git-diff branch


        # -------------------------
        # No CLI args: run repo / git diff mode
        # -------------------------
        changed_files = get_changed_markdown_files()
        if not changed_files:
            print("No changed markdown files detected.")
            return

        # Filter out files that should not be processed as sources.
        file_diffs = {}
        for file_path in changed_files:
            # read file start to get front matter
            try:
                start = file_path.read_text(encoding="utf-8")
            except Exception:
                start = ""
            fm = read_front_matter(start)
            auto_translate = bool(fm.get("auto-translate", False))
            review_pending = bool(fm.get("translation-review-pending", False))

            # skip the file unless auto-translate explicitly true and review_pending is false
            if not auto_translate:
                print(f"Skipping {file_path} — auto-translate is not enabled (or missing).")
                continue
            if review_pending:
                print(f"Skipping {file_path} — translation-review-pending is true.")
                continue

            # now compute diff for files we intend to process
            added = get_added_lines_with_context(file_path)
            file_diffs[file_path] = added

            # Dry-run estimation (git diff mode)
            total_estimated = 0

            for file_path, added_lines in file_diffs.items():
                est = estimate_diff_chars(added_lines)
                total_estimated += est

            print(f"Estimated characters to translate (git diff): {total_estimated}")

            used, limit = get_deepl_character_quota(translator)
            remaining = limit - used

            SAFETY_BUFFER = 1000

            if total_estimated + SAFETY_BUFFER > remaining:
                raise RuntimeError(
                    f"Insufficient DeepL quota:\n"
                    f"  Needed (est.): {total_estimated}\n"
                    f"  Remaining:    {remaining}\n"
                    f"  Buffer:       {SAFETY_BUFFER}"
                )

        # If *no* file has additions, exit early
        if not any(file_diffs.values()):
            print("Nothing to translate - Exiting.")
            return

        # Process files with additions
        for file_path, added_lines in file_diffs.items():
            src_lang = detect_language(file_path)
            target_langs = [l for l in ALL_LANGS if l != src_lang]

            print(f"\nDetected changed content in file: {file_path}")
            print(f"Translating from source language: {src_lang}")

            if not added_lines:
                print(f"No additions detected in {file_path} — skipping.")
                continue

            for lang in target_langs:
                rel_path = file_path.relative_to(ROOT_DIR / src_lang)
                target_path = ROOT_DIR / lang / rel_path
                patch_translation_file(file_path, target_path, added_lines)
    
    finally:
        watchdog.cancel()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"FATAL: {e}")
        sys.exit(1)

