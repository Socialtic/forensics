---
title: How-to - Technical triage of Android devices using MVT
summary: Commands and steps to perform technical triage of an Android device using MVT
keywords: triage, android, mvt, androidqf, bugreport
lang: en
tags: [how-to, android, mvt]
last_updated: 2026-11-04
some_url:
created: 2026-11-04
comments: true
author:
    name: Daniel
    url: https://socialtic.org/quienes-somos/
    description: SocialTIC
auto-translate: true

---

# How-to: Technical triage of Android devices using MVT

This document is part of a **technical documentation repository** which has the main objective of establishing a baseline of proven, flexible and accessible knowledge to **boost consensual forensic analysis in support of civil society across the globe**. To organize the contents, we use the [Diátaxis technical documentation framework](../../references/00-glossary/index.md#diataxis). It is complementary to other resources in this repository including [explainers](../../explainers/index.md), [tutorials](../../tutorials/index.md) and [references](../../references/index.md).

This resource belongs to the [how-to guides](https://diataxis.fr/how-to-guides/) category. Its goal is to walk you through the commands and steps needed to perform technical triage of an Android device using the [Mobile Verification Toolkit (MVT)](https://github.com/mvt-project/mvt), assuming you are already familiar with the concepts involved and are looking for a direct reference of the process.

If you have not used MVT before to conduct a technical triage, we recommend you follow first the [Tutorial: Using MVT for Technical Triage of Android Devices](../../tutorials/02-tutorial-mvt-android-triage/index.md) that includes a guided walkthrough a practical excercise. 

We acknowledge the efforts and leadership of [Amnesty International Security Lab](https://securitylab.amnesty.org/) in developing the MVT tool, as well as its role in strengthening the global digital forensics community through its [Digital Forensics Fellowship](https://securitylab.amnesty.org/digital-forensics-fellowship/). This material is intended to be compatible with and complementary to these technological and methodological efforts.

This material is complementary to other resources in this repository, including:

* [Explainer: Introduction to technical triage of Android devices](../../explainers/04-explainer-introduction-android-triage/index.md), which covers the conceptual background of Android technical triage (threat vectors, artifact types, the role of the triage interview).
* [Explainer: Exploring the MVT tool for technical triage of Android devices](../../explainers/05-explainer-mvt-android-triage/index.md), which covers MVT's commands, modules and output files.
* Extraction how-to guides, including [How to extract a bugreport from an Android device?](../05-how-to-extract-bugreport/index.md) and [How to perform an extraction using AndroidQF?](../04-how-to-extract-with-androidqf/index.md)
* Tutorials and learning materials on [using MVT for technical triage of Android devices](../../tutorials/02-tutorial-mvt-android-triage/index.md) and [using AndroidQF for extraction of Android devices](../../tutorials/01-tutorial-learning-androidqf/index.md).
* Reference resources detailing MVT output files:
    * [MVT bugreport output file dictionary](../../references/02-reference-mvt-bugreport-dictionary/index.md)
    * [MVT AndroidQF output file dictionary](../../references/03-reference-mvt-androidqf-dictionary/index.md)

## Prerequisites to perform technical triage with MVT

Before following this guide, make sure that:

* **You have internet access.** This is required to install and update MVT, and to download the latest indicators of compromise (IOCs).
* **You have already conducted a triage interview** with the person you are accompanying, and you have the key dates, events, and context available to guide your analysis.
* **You have already collected the forensic information you need to analyze.** This guide does not cover extraction. If you haven't done so yet, follow the:
    * [How to extract a bugreport from an Android device?](../05-how-to-extract-bugreport/index.md)
    * [How to perform an extraction using AndroidQF?](../04-how-to-extract-with-androidqf/index.md)
* **You have an initial hypothesis you want to confirm or rule out.** MVT does not tell you whether a device is compromised. It can help surface artifacts and known indicators for you to interpret against the context of the case. Reviewing its output without a clear hypothesis makes it very difficult to know what to look for.

## 1️⃣ Install or update MVT

MVT is distributed as a Python package and is best installed through [pipx](https://pipx.pypa.io/), which isolates it from other Python packages on your system.

=== "Linux"

    ```sh
    sudo apt install python3 python3-venv python3-pip sqlite3 libusb-1.0-0
    sudo apt install pipx
    pipx ensurepath
    git clone https://github.com/mvt-project/mvt
    cd mvt
    pipx install --force .
    ```

=== "macOS"

    ```sh
    brew install python3 pipx libusb sqlite3
    git clone https://github.com/mvt-project/mvt
    cd mvt
    pipx install --force .
    ```

!!! warning "Note"

    Currently, MVT does not have a formal installation process for Windows. The tool can be used through the Windows Subsystem for Linux; however, proper functionality is not guaranteed

**If MVT is already installed, update it before every triage** to make sure you have the latest modules and IOC integrations:

```sh
cd mvt
git pull
pipx uninstall mvt
pipx install --force .
```

Finally, **download the latest indicators of compromise**:

```sh
mvt-android download-iocs
```

## 2️⃣ Confirm what information is available

The MVT command you run depends on what you collected during the extraction. Use the table below to decide:

| Information available | Command to use | What it gives you |
| :---- | :---- | :---- |
| Full AndroidQF extraction | `mvt-android check-androidqf` | A complete analysis, which includes the bugreport and, when available, the intrusion logs |
| Bugreport only | `mvt-android check-bugreport` | Initial triage using only the bugreport |
| Intrusion logs only | `mvt-android check-intrusion-logs` | A review of the advanced protection logs |

If you have a full AndroidQF extraction, use `check-androidqf` since it covers the other two already, as long as the specific artifacts are present in the extraction. 

You can list the modules available for each command with:

```sh
mvt-android check-bugreport --list-modules
mvt-android check-intrusion-logs --list-modules
mvt-android check-androidqf --list-modules
```

## 3️⃣ Set up the output folder

### Data handling considerations

Although a bugreport or AndroidQF extraction contains relatively little strictly private information (no photos or personal files, for example), it must still be handled with care:

* **Respect the informed consent** given by the person you are accompanying.
* Follow any **data retention agreement** established for the case.
* **Avoid** syncing or uploading any of this information to **unencrypted cloud services**.

We list additional recommendations in the [relevant section of the triaging with MVT explainer.](../../explainers/05-explainer-mvt-android-triage/index.md#recommendations-for-handling-sensitive-information) 

If you have not yet had this conversation with the person you're accompanying, see [How to obtain and document informed consent?](../01-how-to-obtain-informed-consent/index.md)

### Create the working folder

Create a folder to **hold a copy of the collected extraction**, and name it using a consistent convention. Keep in mind this convention is to be defined by each organization, depending on the specific context and needs, including in relation to confidentiality and anonymity of the person requesting the analysis.

As an example, we suggest using the date combined with a case alias or hash:

```sh
mkdir "$(date +"%Y-%m-%d")"-android-<case-alias-or-hash>-out-androidqf
mkdir "$(date +"%Y-%m-%d")"-android-<case-alias-or-hash>-out-bugreport
mkdir "$(date +"%Y-%m-%d")"-android-<case-alias-or-hash>-out-intrusion-logs

```

Copy the collected extraction (bugreport, AndroidQF folder, or intrusion logs) into this folder before continuing. We recommend you set up a working directory structure that includes a folder for the extraction (never to be touched), a copy of the extraction to conduct the analysis, a folder for the outputs (using the naming convention described above) and a document for notes. For example:

```
analysis/
└── YYYY-MM-DD-operative-system-<case-alias-or-hash>/
    ├── extraction-custody/       # Raw data, not to be touched
    ├── extraction-working/       # Copy of raw data, used for analysis
    ├── YYYY-MM-DD-out-<androidqf/bugreport/intrusion-logs>/ # to store MVT output
    └── notes.md          # Notes and logs from analysis
```

### Output disposal and retention

* Delete or archive the outputs generated by MVT once the analysis concludes, following the data retention agreement for the case.
* Do not keep copies outside the agreed storage location.

## 4️⃣ Run the check

Open a terminal in your working folder and run the command that matches what you have available (see Step 2). MVT will create the output folder (`-o`) with several files and subfolders, described in Step 5.

**AndroidQF extraction:**

```sh
mvt-android check-androidqf /path/to/aqf/extraction -o "$(date +"%Y-%m-%d")"-out-androidqf
```

**Bugreport:**

```sh
mvt-android check-bugreport /path/to/bugreport -o "$(date +"%Y-%m-%d")"-out-bugreport
```

**Intrusion logs:**

```sh
mvt-android check-intrusion-logs /path/to/intrusion/logs -o "$(date +"%Y-%m-%d")"-out-intrusion-logs
```

### Common errors

* **Prompted for a backup password:** if the extraction includes an encrypted `backup.ab`, MVT will ask for its password before continuing.
* **`ModuleNotFoundError` or missing dependency errors:** reinstall MVT following Step 1, making sure the system dependencies (`sqlite3`, `libusb-1.0-0`) are installed.
* **Command not found:** confirm `pipx ensurepath` was run and that you opened a new terminal session afterward.
* **No `_detected` files generated:** this does not necessarily mean the run failed. It can simply mean nothing matched a known indicator or heuristic. Continue to Step 5.

## 5️⃣ Triage the output

Before reviewing any output, **keep the key dates and information from the triage interview in mind and in writing**, along with the hypothesis you are trying to confirm or rule out.

* **`command.log`:** the same output MVT prints to the screen while running, saved to a file. It mixes process information (INFO, DEBUG) with alerts of different severity levels (LOW, MEDIUM, HIGH, CRITICAL), in chronological order. It's usually the best starting point. See the [reference dictionaries](../../references/index.md) for details on its structure.
* **`alerts.json`:** a single file that consolidates every alert generated during the run, without the informational lines that appear in `command.log`. Useful for getting a quick overview of everything MVT flagged before going module by module.
    * **Critical alerts:** warnings related to a match with an IOC, meaning a match with a previously known STIX2 indicator.
    * **Low, Medium and High alerts:** related to matches with TTPs (tactics, techniques and procedures), meaning these are matches based on heuristics and device behavior that are not related to a known IOC.
* **Files with the `_detected` suffix:** generated per module whenever MVT finds a match against a known indicator of compromise or a suspicious heuristic. Each file contains the matched indicator, the related artifact, and the corresponding timestamp.
    * **When you find a hit:** note the module name, the timestamp, and check it against the timeline from the triage interview, if relevant.
    * **Important:** the absence of a `_detected` file is not confirmation that the device is clean, and the presence of one is not confirmation of malicious activity. Both require further investigation and manual review.
* **`timeline.csv`:** every event MVT extracted, organized chronologically. Especially useful once you have a specific time window to investigate from the interview, since you can filter activity around it.
* **`alerts_timeline.csv`:** contains a timeline of all alerts raised during the execution of MVT, including specific information about the module that raised the alert.

For a full description of what each file and field contains, see the [MVT bugreport output file dictionary](../../references/02-reference-mvt-bugreport-dictionary/index.md) and the [MVT AndroidQF output file dictionary](../../references/03-reference-mvt-androidqf-dictionary/index.md).

## 6️⃣ Run targeted searches

Once you have an initial read of the output, use standard command-line tools to dig into specific packages, timestamps, or modules without opening every file manually.

* **`grep`:** search for text matches across files. Examples:

```sh
grep -l "<package_name>" *_detected.json
```

```sh
grep -E "LOW|MEDIUM|HIGH|CRITICAL" command.log
```

* **`find`:** locate files within the results folder.

```sh
find . -name "*_detected*"
```

* **`cat`:** print the full contents of a file to the terminal, useful for smaller files.

```sh
cat packages.json
```

* **`jq`:** filter and query JSON output, the format most MVT results are stored in.

```sh
jq '.[] | {level, module, message}' alerts.json
```

## 7️⃣ Document findings and next steps

* **Document every finding**, including the package name, artifact type, timestamp, and the matched indicator or TTP that flagged it.
* **Escalate for independent review** anything you need to confirm or investigate further. A second analyst's perspective is especially valuable when a finding is unclear.
* **Identify additional investigation pathways**, such as static or dynamic analysis of a suspicious APK, or a review of the associated Google account through Google Takeout.

## Conclusion

In this resource we provided **concrete guidance on how to use MVT to help in the triage of an Android device**. Importantly, this process should not rely solely on the tool, and instead should be built on a good initial interview that surfaces concrete aspects to investigate, and can help narrow down to more concrete hypotheses.

You should also keep in mind that the tool will help with the parsing of information and point to specific areas to investigate, but **will not replace the review and interpretation of an analyst.** Moreover, consider this triage process as an initial effort to find evidence of potential malicious activity, not necessarily a conclusive result. Based on initial findings from this triage process you might want to engage in further manual analysis, including potentially of a suspicious application.

Lastly, keep in mind the importance of informed consent and the adequate handling of forensic information, to prevent exposure to [known threats and risks](../../explainers/02-explainer-risks-threats/index.md).


## Comments

Do you have **comments or suggestions** about this resource? You can use the **comment feature shown below** to share your ideas or feedback with us. Please be sure to follow our [code of conduct](../../community/code-of-conduct/index.md). The comment feature links directly to the [_Discussions_ section on GitHub](https://github.com/Socialtic/forensics/discussions), where you can also **participate in discussions directly**, if you prefer.
