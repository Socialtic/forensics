---

title: Explainer - Explorando la herramienta MVT para el triaje técnico de dispositivos Android
summary: Explorando la herramienta MVT para el triaje técnico de dispositivos Android
keywords: triaje, android, mvt, androidqf, bugreport
lang: es
tags: [explainer, android, mvt]
last_updated: 2026-11-03
some_url:
created: 2026-11-03
comments: true
author:
    name: Daniel
    url: https://socialtic.org/quienes-somos/
    description: SocialTIC

translation-review-pending: true
---

# Explainer: Exploring the MVT Tool for Technical Triage of Android Devices

This document is **part of a technical documentation repository** that aims to establish a proven, flexible, and accessible knowledge base to **promote consent-based forensic analysis for the benefit of civil society**. To organize the content, we use the [Diataxis technical documentation framework](../../references/00-glossary/index.md#diataxis).

This particular resource falls under the category of [explainers](https://diataxis.fr/explanation) and seeks to familiarize readers with the MVT tool and the concepts necessary to perform forensic triage using the [Mobile Verification Toolkit](https://github.com/mvt-project/mvt). In this material, we explore the tool’s modules and outputs, as well as the mental model to follow when performing a triage of Android devices with MVT.

The Mobile Verification Toolkit (MVT) is an open-source forensic tool developed by the [Amnesty International Security Lab](https://securitylab.amnesty.org/) that allows users to **analyze forensic artifacts from Android and iOS devices for signs of compromise**.

We acknowledge the efforts and leadership of Amnesty International’s Security Lab in developing the MVT tool, as well as its role in strengthening the global digital forensics community through its [Digital Forensics Fellowship](https://securitylab.amnesty.org/digital-forensics-fellowship/). This material is intended to be compatible with and complementary to these technological and methodological efforts.

This document is complemented by other resources in this repository, including:

* [Explainer: Introduction to Technical Triage of Android Devices](../04-explainer-introduction-android-triage/index.md), which covers important conceptual aspects of the Android operating system and how it can be compromised.
* [How-to: Technical Triage of Android Devices Using MVT](../../how-tos/06-how-to-triage-android-mvt/index.md), which provides the commands and steps for performing a direct triage with MVT.
* Guides for the forensic extraction of artifacts, including [the how-to guide for extracting a bug report](../../how-tos/05-how-to-extract-bugreport/index.md) and [the how-to guide for extraction using AndroidQF](../../how-tos/04-how-to-extract-with-androidqf/index.md).
* [The hands-on tutorial on using MVT for technical triage of Android devices](../../tutorials/02-tutorial-mvt-android-triage/index.md), which uses a sample extraction to better understand the process of using MVT.
* Reference materials with information about MVT output:
  * [Dictionary of MVT Bug Report Analysis Output Files](../../references/02-reference-mvt-bugreport-dictionary/index.md)
  * [Dictionary of AndroidQF Analysis Output Files with MVT](../../references/03-reference-mvt-androidqf-dictionary/index.md)

## Important Considerations Before Performing a Technical Triage

**Forensic artifacts may contain sensitive information**, so it is important to discuss, clarify, and agree with the person requesting the analysis on how their information will be handled. Keep in mind that when performing a triage with MVT, the tool generates lists of device packages, timestamps, or file paths that may reflect the behavior of the device belonging to the person who requested the analysis.

Therefore, we recommend that before collecting information or using forensic tools such as MVT, you obtain the informed consent of the person requesting the analysis, and also ensure you have the necessary capacity, measures, and controls to contain and limit the [risks faced by civil society forensic labs](../02-explainer-risks-threats/index.md).

The [how-to guide: How to Obtain Informed Consent for a Forensic Investigation?](../../how-tos/01-how-to-obtain-informed-consent/index.md) describes what informed consent is in the context of forensic investigations and provides a template that can be adapted to meet specific needs.

### Recommendations for Handling Sensitive Information

It is important to keep in mind that all files generated during triage—**from extraction to MVT results—must be treated as sensitive information**, even when the use of MVT does not yield any matches with indicators of compromise.

This means that **proper data handling practices** are required, including:

* Ensuring that the computing devices used for triage have **disk encryption**.
* **Consider an additional layer of encryption** for working folders if the results will be transferred between devices. You can use tools such as encrypted containers ([VeraCrypt](https://protege.la/guides-content/veracrypt-use-installation-file-encryption/) or [Cryptomator](https://protege.la/guias-contenido/guia-cryptomator/).
* **Restrict access to the results folders** to only those individuals directly involved in the case analysis, following a [need-to-know policy](https://en.wikipedia.org/wiki/Need_to_know).
* **Do not work on the original copy of the extracted data** to avoid making changes that could compromise its integrity. Create a working copy and use this copy for triage and analysis.
* Document the process, for example, in a notes.md file, where **you record the commands that were executed, the date, and any relevant observations**. This makes it easier to resume the analysis later or share it with another analyst.
* **Securely delete temporary or intermediate copies** that are no longer needed.
* **Avoid printing or exporting results to insecure channels** (such as unencrypted email or unencrypted messaging) when sharing findings with other team members or with the person being supported.
* Determine in advance **how long the information will be retained** once the analysis is complete.
* **Avoid using cloud storage services without end-to-end encryption** to store extraction folders or results.

Handling forensic information in accordance with these and other best practices is part of the **responsibility of participating in a consented forensic process**. The person who authorized the analysis of their device trusts that the data resulting from that analysis will not be exposed during the process or after it has concluded.

### Organizing Information

Before running the MVT tool for technical triage, it is important to define a clear and consistent folder structure where the resulting information will be stored. Below is an example of a basic and functional organization that can be adapted according to the specific needs and characteristics of each organization.

```
analysis/
└── YYYY-MM-DD-operative-system-<case-alias-or-hash>/
    ├── extraction-custody/ # Raw data, not to be touched
    ├── extraction-working/ # Copy of raw data, used for analysis
    ├── YYYY-MM-DD-out-<androidqf/bugreport/intrusion-logs>/ # to store MVT output
    └── notes.md # Notes and logs from analysis
```

When organizing the files, it is important to consider the following:

* **It is recommended to use consistent naming conventions across cases**, including the date of the analysis and a unique identifier.
* **Separate the extraction data from the results generated by MVT:** this allows you to rerun the triage if necessary, without losing or overwriting the extraction information. If you have sufficient space, it is recommended to create an archive folder containing the original extraction data, which should not be used for any of the analysis processes.
* **Do not mix files from different cases in the same folder.** Before running an analysis, it is important to create the necessary folder structure to store the information.

## Using MVT for Android Device Triage

The Mobile Verification Toolkit (MVT) is an open-source forensic tool developed by the [Amnesty International Security Lab](https://securitylab.amnesty.org/) that allows you to **analyze forensic artifacts from Android and iOS devices for signs of compromise**.

MVT does not access the device directly or perform data extraction on its own; rather, it processes information that has already been extracted, for example, using the AndroidQF tool. When using MVT to process an extraction, the tool groups and organizes the information and compares it against a set of heuristics for suspicious behavior and [indicators of compromise (IOCs)](../../references/00-glossary/index.md#indicator-of-compromise-ioc), such as certain known signs of spyware like [Pegasus](https://securitylab.amnesty.org/latest/2026/07/inside-pegasus-the-evolution-of-the-worlds-most-notorious-spyware/) or [Predator](https://securitylab.amnesty.org/latest/2025/12/intellexa-leaks-predator-spyware-operations-exposed/), or stalkerware families.

### MVT Commands and Modules for Android

MVT organizes its analysis modules according to the type of forensic artifact being processed. For Android devices, the following commands are available:

* **mvt-android check-androidqf**: allows you to analyze an extraction performed with the androidQF tool using the [modules for that extraction](https://github.com/mvt-project/mvt/tree/main/src/mvt/android/modules/androidqf). These extracts generally also include a *bugreport* and, if available, *intrusion logs* as well. Therefore, use the The androidqf module may be sufficient to **analyze all available artifacts**, since MVT automatically detects these files and also runs the [modules corresponding to bugreport](https://github.com/mvt-project/mvt/tree/main/src/mvt/android/modules/bugreport) and the [modules corresponding to backup](https://github.com/mvt-project/mvt/tree/main/src/mvt/android/modules/backup)
* **mvt-android check-bugreport**: This module allows you to directly analyze a [bug report](../../references/00-glossary/index.md#bugreport). If you do not have an AndroidQF extraction and are looking for a quick analysis, it is recommended that you **use this module as a first step**. If signs of suspicious activity are identified, it is recommended to follow up with a full analysis of an AndroidQF extraction.
* **mvt-android check-intrusion-logs**: *Intrusion logs* are only available on devices running Android 16 or higher and when the user has previously enabled Advanced Protection Mode with intrusion logging turned on. If you have an intrusion log file, you can analyze this specific file using this command and the MVT module.

!!! Note
    Unlike the bug report, which is always generated during an AndroidQF extraction, the [intrusion logs](https://securitylab.amnesty.org/latest/2026/05/android-intrusion-logging-as-a-new-source-of-data-for-consensual-forensic-analysis/) will only be present in the extraction if the device is running Android 16 or higher and the user has previously enabled Advanced Protection Mode with intrusion logging turned on.

#### Modules

The following tables describe each of the modules available for the different commands, the link to their source code, and their utility in forensic analysis.

!!! note "Note"
    This list corresponds to the modules available in the main branch of the official MVT repository at the time of writing (version 2026.10.5). Since MVT is an actively developed tool, modules may be added or modified over time. You can confirm the current list by checking the [MVT source code](https://github.com/mvt-project/mvt/tree/main/src/mvt/android/modules).

=== "androidqf"

 | Module | Source file | What it analyzes | Forensic utility |
    | :---: | ----- | ----- | ----- |
    | **AQFPackages** | [aqf\_packages.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/androidqf/aqf_packages.py) | List of installed applications (packages.json) | Identifies packages related to rooting and unofficial app store installers |
    | **AQFProcesses** | [aqf\_processes.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/androidqf/aqf_processes.py) | Running processes (ps.txt) | Allows you to check which processes were active at the time of extraction |
    | **AQFGetProp** | [aqf\_getprop.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/androidqf/aqf_getprop.py) | System properties (getprop.txt) | Provides technical context about the device (model, Android version, architecture, etc.) |
    | **AQFSettings** | [aqf\_settings.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/androidqf/aqf_settings.py) | System settings (settings\_system.txt, settings\_secure.txt, settings\_global.txt) | Allows you to review the device’s network, security, and accessibility settings |
    | **AQFFiles** | [aqf\_files.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/androidqf/aqf_files.py) | List of files and metadata (files.json) | Detects files in suspicious paths, such as /data/local/tmp/,  |
    | **AQFLogTimestamps** | [aqf\_log\_timestamps.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/androidqf/aqf_log_timestamps.py) | Timestamps of files in the logs/ folder | Builds a creation/modification timeline for the collected logs |
    | **RootBinaries** | [root\_binaries.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/androidqf/root_binaries.py) | The list of rooting binaries (root\_binaries.json) | Detects traces of rooting (su, Magisk, busybox, etc.). |
    | **Mounts** | [mounts.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/androidqf/mounts.py) | Mount point information (mounts.json) | Detects mount configurations, such as /system mounted in read/write mode. |

=== "bugreport"

    | Module | Source file | Dumpsys section analyzed | Forensic utility |
    | :---: | ----- | ----- | ----- |
    | **DumpsysAccessibility** | [dumpsys\_accessibility.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/bugreport/dumpsys_accessibility.py) | accessAccessibility | Review the use of accessibility services |
    | **DumpsysActivities** | [dumpsys\_activities.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/bugreport/dumpsys_activities.py) | package (Activity Resolver Table) | Extracts the activities and intent filters registered by each app and compares them against engagement metrics |
    | **DumpsysAppops** | [dumpsys\_appops.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/bugreport/dumpsys_appops.py) | appops | Displays the usage history of sensitive permissions (camera, microphone, location) by app |
    | **DumpsysBatteryDaily** | [dumpsys\_battery\_daily.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/bugreport/dumpsys_battery_daily.py) | batterystats (daily summary) | Provides a daily log of battery events and process activity |
    | **DumpsysBatteryHistory** | [dumpsys\_battery\_history.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/bugreport/dumpsys_battery_history.py) | batterystats (detailed history) | Allows you to build a granular timeline of process activity and power consumption |
    | **DumpsysDBInfo** | [dumpsys\_dbinfo.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/bugreport/dumpsys_dbinfo.py) | dbinfo | Retrieves information about SQLite databases opened by the system and apps |
    | **DumpsysGetProp** | [dumpsys\_getprop.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/bugreport/dumpsys_getprop.py) | getprop (embedded in the bug report) | Provides device properties obtained from a secondary source within the same bug report |
    | **DumpsysPackages** | [dumpsys\_packages.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/bugreport/dumpsys_packages.py) | package | Lists installed applications and their metadata, as reported in the bug report |
    | **DumpsysPlatformCompat** | [dumpsys\_platform\_compat.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/bugreport/dumpsys_platform_compat.py) | platform\_compat | Records applications that were uninstalled |
    | **DumpsysReceivers** | [dumpsys\_receivers.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/bugreport/dumpsys_receivers.py) | package (intent receivers) | Identifies registered receivers to intercept SMS messages, incoming/outgoing calls, or phone status changes  |
    | **DumpsysADBState** | [dumpsys\_adb\_state.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/bugreport/dumpsys_adb_state.py) | adb | Checks the ADB debugging status and authorized/trusted keys |
    | **BugReportTimestamps** | [fs\_timestamps.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/bugreport/fs_timestamps.py) | File system listing (FS/\*) | Builds a timeline from the file system timestamps captured in the bug report |
    | **Tombstones** | [tombstones.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/bugreport/tombstones.py) | Tombstone files\_\* | Analyzes application crash dumps |

=== "backup"

    | Module | Source file | What it analyzes | Forensic utility |
    | :---: | ----- | ----- | ----- |
    | **SMS** |  [sms.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/backup/sms.py) |  Backed-up SMS/MMS messages | Extracts message content, identifies links contained within them, and compares them against indicators of compromise |

=== "intrusion logs"

    | Module | Source file | What it analyzes | Forensic utility |
    | :---: | ----- | ----- | ----- |
    | **DnsEvent** | [dns\_event.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/intrusion_logs/dns_event.py) | DNS resolution events (queried hostnames and IPs) | Identifies domains or IPs belonging to malicious infrastructure contacted by the device, by comparing them against indicators of compromise |
    | **ConnectEvent** | [connect\_event.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/intrusion_logs/connect_event.py) | Outbound network connection events (destination IP and port) | Detects direct connections to IPs associated with known spyware infrastructure, even when there was no prior DNS query |
    | **SecurityEvent** | [security\_event.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/intrusion_logs/security_event.py) | System security events (ADB activity, app processes, screen lock/unlock, system boot, among others) | Provides context on sensitive activity on the device, such as commands executed via ADB (adb shell, adb pull, adb push) or the launch of app processes, which is useful for reconstructing a timeline of an incident |

### Logic MVT Execution

When running ***mvt-android check-androidqf*** on an AndroidQF build, the MVT follows an automated workflow that requires no manual intervention. During this process, the MVT:

1. Loads the relevant indicators of compromise and modules, depending on the type of artifacts present in the dump.
2. Loads data from the files generated by the acquisition that we pass as input.
3. Processes and *parses* that information using each module and its corresponding artifacts—that is, it transforms raw data (plain text, JSON, binaries) into structured, readable records.
4. Compares those records against the indicators of compromise (IOCs) loaded in the first step, and against a set of heuristics specific to each module.

This workflow repeats module by module, one after another, and is exactly what you see in the terminal as the execution progresses.

### Understanding MVT Log Lines

Each line produced by MVT begins by indicating which module generated it. This is key to knowing where in the execution you are, especially when the screen output combines results from multiple modules running one after another.

For example:

```sh
2026-08-14 11:21:06.364 - mvt.android.modules.androidqf.aqf_settings - MEDIUM - Found suspicious "global" setting "package_verifier_user_consent = -1" (Google Play Protect disabled)
```

The fragment ***mvt.android.modules.androidqf.aqf\_settings*** indicates that this alert comes specifically from the **AQFSettings** module, which analyzes the ***settings\_\*.txt*** files in the extraction.

What to look for and where **will depend largely on the context of the information we are analyzing**. The MVT does not provide customized results; rather, it delivers organized evidence so that the analyst can interpret the results while taking the context of the case into account.

The MVT will display alerts with different severity levels:

* **Low, Medium, and High**: related to [**TTPs** (Tactics, Techniques, and Procedures)](../../references/00-glossary/index.md#ttp), that is, heuristic warnings and suspicious behavior patterns that are not necessarily linked to a known threat. For example:

```sh
2026-08-14 11:21:06,116 - mvt.android.modules.androidqf.aqf_packages - MEDIUM - Found a non-system package installed via adb or another method: "com.facebook.katana"
2026-08-14 11:21:38,714 - mvt.android.modules.bugreport.dumpsys_battery_daily - MEDIUM - Detected uninstall of package com.SecUpwN.AIMSICD (vers 0)
```

* **Critical**: These are warnings related to a match against **indicators of compromise (IOCs)** loaded from STIX2 collections—that is, against a previously documented and attributed threat.

**Alerts are issued based on matches with behaviors and IOCs.** Alerts must be reviewed to determine their severity, the module that generated them, and the timestamp associated with the alert. Depending on the number of alerts, the modules they relate to, their severity, and their relationship to the timeline established during the initial interview, these alerts may indicate whether it is advisable to conduct a more in-depth analysis of certain information.

As detailed in the [introductory material on technical triage in Android](https://forensics.socialtic.org/en/explainers/04-explainer-introduction-android-triage/), having a clear understanding of the timeline and the reported events allows the search to be focused on specific artifacts and time periods. The initial triage interview sets the course for the technical review and forensic investigation, as this interview yields essential information of interest, such as:

* Whether the device was confiscated for a certain period of time
* Whether or not there are any suspicious apps that suddenly appeared
* Whether the person fell victim to a phishing attack and installed an app or downloaded a file
* Whether any apps suddenly crash

During the review, it is common to encounter **package names, processes, or services that we do not recognize**. This is normal, even for experienced analysts, given the enormous number of apps and system components that exist in the Android ecosystem. When this happens, we recommend:

* Note and document the name of the package or process, along with the context in which it appeared.
* Privately investigate the specific apps and processes using search engines such as [Virus Total](https://www.virustotal.com/) to determine whether they are a legitimate system component, a known commercial app, or something that warrants further attention.

### Useful Commands for Filtering MVT Output

To analyze MVT output efficiently, it is helpful to know some terminal commands that allow you to filter, search, and explore large volumes of information without having to Open each file manually:

* **grep**: [grep](https://linuxcommandlibrary.com/man/cat) searches for text matches within a file. It is especially useful for filtering lines by severity level or by module. For example, to filter only the alerts in our `command.log`:

```sh
grep -E "LOW|MEDIUM|HIGH|CRITICAL" command.log
```

Or to review only what a particular [module](#modules) reported:

```sh
grep "dumpsys_battery_daily" command.log
```

* **find**: [find](https://linuxcommandlibrary.com/man/cat) locates files within the results folder generated by the MVT, which is especially useful when the export contains many subdirectories and JSON files.

```sh
find ./YYYY-MM-DD-out-androidqf/ -name "*detected*"
```

* **cat**: [cat](https://linuxcommandlibrary.com/man/cat) displays the entire contents of a file directly in the terminal, which is useful for small files such as packages.json.

```sh
 cat packages.json
```

* **jq**: [jq](https://linuxcommandlibrary.com/man/jq) is a tool specialized in processing and filtering JSON files, the format in which the MVT saves most of its results. For example, to extract only the level, module, and message from each alert in `alerts.json`:

```sh
jq '.[] | {level, module, message}' alerts.json
```

### Reviewing MVT Output Files

#### command.log

This is the output that the MVT displays on screen while it is running, which is also saved to the command.log file. Generally, this is a good starting point for review, since **you can see both the entire execution process and the alerts that were generated in chronological order** within a single file.

Within `command.log`, you can find different types of lines: informational messages about the process (INFO, DEBUG), errors (ERROR), and alerts with different severity levels (LOW, MEDIUM, HIGH, CRITICAL), for example:

```sh
2026-08-14 11:21:38.714 - mvt.android.modules.bugreport.dumpsys_battery_daily - MEDIUM - Detected uninstall of package com.republicwireless.tel (vers 0)
```

**If you find an alert of interest, you can investigate further by reviewing the specific logs for that module.** For example, if you identify a line of interest such as the following:

```sh
2026-08-14 11:21:06.116 - mvt.android.modules.androidqf.aqf_packages - MEDIUM - Found a non-system package installed via adb or another method: "com.facebook.katana"
```

It is advisable to review the AQFPackages module’s results file (aqf\_packages.json inside the results folder) to examine the complete record for that package, including its installer, certificates, hashes, and other metadata.

**When the MVT identifies a relevant finding**—for example, a match with an IoC or medium-severity heuristic alerts—in addition to displaying it on screen, **it generates a file with the suffix *detected* corresponding to each module**, which contains only the information that triggered the alert.

It is important to keep in mind that **alerts are not necessarily confirmation of a compromise**, but they should certainly be investigated. It is important to document anything that appears suspicious and requires further review. For example, there may be alerts related to specific APKs, such as *com.facebook.katana* in the previous example.

#### timeline.csv

The timeline.csv is a CSV file that **contains all device events extracted by the MVT, organized by date**. This makes it a useful file for reconstructing device activity over a specific time range. Each row includes the device timestamp, the module that generated the event, a short event type, and a description. For example, here’s what some rows related to the installation of Facebook packages look like:

```
"Device Local Timestamp","Plugin","Event","Description"
"2008-12-31 19:00:00","DumpsysPackages","package_first_install","Install or update of package com.facebook.system"
"2008-12-31 19:00:00","DumpsysPackages","package_last_update","Install or update of package com.facebook.katana"
```

This file is **useful when you have a specific time window to investigate based on the triage interview**, as it allows you to filter all device activity around the timeline identified in the initial interview.

#### alerts.json

The alerts.json file **consolidates all alerts generated during the analysis into a single structured file**. Unlike the command.log, which mixes alerts with informational process lines, alerts.json contains only the findings.

Each alert includes the severity level, the source module, the message, the event timestamp (when applicable), and the complete event record that generated the alert. For example:

```json
{
    "level": "MEDIUM",
    "module": "aqf_packages",
    "message": "Found a non-syst"em package installed via adb or another method: \"com.facebook.katana\"",
    "event_time": "",
    "event": {
 "name": "com.facebook.katana",
        "installer": "null",
 "third_party": true
    }
}
```

Since it is a single consolidated file, it serves as a good starting point when you want to get an overview of everything MVT identified as suspicious before delving deeper module by module.

#### alerts\_timeline.csv

The alerts\_timeline.csv file **contains the timeline of alerts identified during an MVT scan**. The advantage of reviewing this file is that you can directly identify which alerts were generated by each executed module, along with the specific event.

```
"Event Time","Module","Message","Event"
"2021-02-01","dumpsys_battery_daily","Detected uninstall of package com.republicwireless.tel (vers 0)","{'action': 'update', 'from': '2021-02-01', 'to': '2021-02-13', 'package_name': 'com.republicwireless.tel', 'vers': '0'}"
"2026-08-10","dumpsys_battery_daily","Detected uninstall of package com.SecUpwN.AIMSICD (vers 0)","{'action': 'update', 'from': '2026-08-10', 'to': '2026-08-11', 'package_name': 'com.SecUpwN.AIMSICD', 'vers': '0'}"
"2026-08-10 18:21:03.799000","dumpsys_appops","Package 'com.google.android.apps.nbu.files' had the risky permission 'REQUEST_INSTALL_PACKAGES' set to 'Reject' on 2026-08-10 18:21:03.799000","{'package_name': 'com.google.android.apps.nbu.files', 'permissions': [{'name': 'REQUEST_INSTALL_PACKAGES', 'entries': [{'access': 'Access', 'type': 'top-s', 'timestamp': '2026-08-10 18:34:25.002000'}, {'access': 'Reject', 'type': 'top-s', 'timestamp': '2026-08-10 18:21:03.799000'}], 'access': 'allow'}], 'uid': 'u0a136'}"
"2026-08-10 18:34:25.002000","dumpsys_appops","Package 'com.google.android.apps.nbu.files' had the risky permission 'REQUEST_INSTALL_PACKAGES' set to 'Access' on 2026-08-10 18:34:25.002000","{'package_name': 'com.google.android.apps.nbu.files', 'permissions': [{'name': 'REQUEST_INSTALL_PACKAGES', 'entries': [{'access': 'Access', 'type': 'top-s', 'timestamp': '2026-08-10 18:34:25.002000'}, {'access': 'Reject', 'type': 'top-s', 'timestamp': '2026-08-10 18:21:03.799000'}], 'access': 'allow'}], 'uid': 'u0a136'}"
```

#### Files with the *detected* suffix

In addition to command.log, timeline.csv, alerts.json, and alerts\_timeline.csv, the **MVT generates individual files per module whenever it identifies suspicious behavior or a match with an IoC**. These files always have the suffix *detected* in their names and contain complete information about what triggered each alert.

## Conclusion

The value of the MVT lies in **consistently transforming raw, disorganized forensic artifacts into structured, comparable evidence**, without requiring a human analyst to manually review every file produced by a device extraction.

However, the structuring of the files should not be confused with interpretation. Understanding what a finding means, whether it matters, and what to do next depends on context that only a triage interview and a human analyst’s review can provide.

Understanding how the MVT tool is structured, the different modules available, its execution flow, and the output allows you to use the tool for technical triage.


## Comments

Do you have **comments or suggestions** about this resource? You can use the **comment feature shown below** to share your ideas or feedback with us. Please be sure to follow our [code of conduct](../../community/code-of-conduct/). The comment feature links directly to the [_Discussions_ section on GitHub](https://github.com/Socialtic/forensics/discussions), where you can also **participate in discussions directly**, if you prefer.   
