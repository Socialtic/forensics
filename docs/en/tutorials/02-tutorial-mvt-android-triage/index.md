---

title: Tutorial - Uso de MVT para el triaje técnico de dispositivos Android
summary: Tutorial guiado para realizar un triaje técnico de dispositivos Android con MVT
keywords: triaje, android, mvt, androidqf
lang: es
tags: [tutorial, android, mvt]
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

# Tutorial: Using MVT for Technical Triage of Android Devices

## Introduction

This document is **part of a technical documentation repository** that aims to establish a proven, flexible, and accessible knowledge base to **promote consent-based forensic analysis for the benefit of civil society**. To organize the content, we use the [Diataxis technical documentation framework](../../references/00-glossary/index.md#diataxis).

This resource is a [tutorial](https://diataxis.fr/tutorials/) designed to facilitate learning the concepts and skills necessary to perform technical forensic triage using the [Mobile Verification Toolkit](https://github.com/mvt-project/mvt). This open-source forensic tool, developed by the [Amnesty International Security Lab](https://securitylab.amnesty.org/), allows users to **analyze forensic artifacts from Android and iOS devices for signs of compromise**.

In this context, we define technical triage as the evaluation—with the owner’s consent—of evidence extracted from a mobile device to **determine whether there are clues, indicators, or behaviors that match known attack vectors**, and which therefore warrant a more in-depth forensic analysis. Therefore, the result of technical triage is neither a confirmation nor a dismissal of a possible intrusion, but rather an informed decision on how to proceed with a case.

MVT processes information that has already been extracted, for example, using the AndroidQF tool. It does not access the device directly or extract data on its own, but rather aggregates and organizes the information, comparing it against a set of heuristics for suspicious behavior and indicators of compromise (IOCs)—such as known signs of spyware like [Pegasus](https://securitylab.amnesty.org/latest/2026/07/inside-pegasus-the-evolution-of-the-worlds-most-notorious-spyware/) or [Predator](https://securitylab.amnesty.org/latest/2025/12/intellexa-leaks-predator-spyware-operations-exposed/), or families of stalkerware.

By the end of this tutorial, **you’ll know how to install the MVT, how to perform a triage on an AndroidQF dump, and how to methodically interpret its results through a guided example based on a hypothetical case**, which covers the entire triage process: from the triage interview to the creation of a timeline of findings.

The original version of this document was written in Spanish by the SocialTIC team. **We appreciate the reviews and suggestions** from the 0xCHE team. Any errors or omissions are the responsibility of the authors.

We acknowledge the **efforts and leadership of Amnesty International’s Security Lab in developing the MVT tool**, as well as its work to strengthen the global digital forensics community through its [Digital Forensics Fellowship](https://securitylab.amnesty.org/digital-forensics-fellowship/). This material is intended to be compatible with and complementary to these technological and methodological efforts.

This document is complemented by other resources in this repository, including:

* [Explainer: Introduction to Technical Triage of Android Devices](../../explainers/04-explainer-introduction-android-triage/index.md), which covers conceptual aspects of the Android operating system and how it can be compromised.
* [Explainer: Exploring the MVT Tool for Technical Triage of Android Devices](../../explainers/05-explainer-mvt-android-triage/index.md), which contains information on how MVT works and its modules for Android.
* [How-to: Technical Triage of Android Devices Using MVT](../../how-tos/how-tos/06-how-to-triage-android-mvt/), which provides the commands and steps for performing a triage directly with MVT.
* Guides for the forensic extraction of artifacts, including [the how-to guide for extracting a bug report](../../how-tos/05-how-to-extract-bugreport/index.md) and [the how-to guide for extraction using AndroidQF](../../how-tos/04-how-to-extract-with-androidqf/index.md).
* Reference materials with information on MVT output:
  * [Dictionary of MVT bug report analysis output files](../../references/02-reference-mvt-bugreport-dictionary/index.md)
  * [Dictionary of AndroidQF Analysis Output Files with MVT](../../references/03-reference-mvt-androidqf-dictionary/index.md)

## Requirements for Following This Tutorial

To follow this tutorial, you must meet the following requirements:

* **Computer**: You need a computer, such as a laptop or desktop. Preferably, the computer should run Linux or macOS, as the tools to be installed are more compatible with these operating systems. In case ofIf you don't have a Windows operating system, you can choose to create a [Linux Virtual Machine](https://ubuntu.com/tutorials/how-to-run-ubuntu-desktop-on-a-virtual-machine-using-virtualbox#1-overview) or install [Windows Subsystem for Linux](https://learn.microsoft.com/es-es/windows/wsl/install).
* **Download the forensic sample to analyze**: To follow this tutorial, you’ll need a forensic sample to analyze with MVT.
  * Download the test sample for this exercise from [this link](https://drive.google.com/file/d/1OpTwa5Bm5j34UaEY7j4hzI6D5OnwMr4E/view?usp=drive_link).
  * If you want to analyze a different sample, we recommend that you first complete this tutorial and the [Tutorial: Exploring AndroidQF for Forensic Extraction on Android](../01-tutorial-learning-androidqf/index.md) to familiarize yourself with the tools; you can then use the how-to guides to guide your extraction and triage process.
* **Installing Git:** You need to [install Git on your computer](https://github.com/git-guides/install-git), since the tool is installed via the official repository.
* **Installing tools:** The [installation section](#instalacion-de-la-mvt) of this tutorial details the steps for installing MVT.
* **Prerequisites:** This tutorial assumes you have a basic familiarity with the command line (navigating between folders, running simple commands) and with general concepts of forensic triage, such as the importance of an initial interview and the responsible handling of sensitive data. Before you begin, we recommend reviewing the [explanatory material on technical triage for Android devices](../../explainers//04-explainer-introduction-android-triage/) and the [explanatory material on technical triage using MVT](../../explainers/05-explainer-mvt-android-triage/index.md).

**Below is a fictional incident scenario and step-by-step instructions for performing the triage process**, accompanied by concise interpretive explanations to help analysts reach a triage conclusion.

## Case Context

For this tutorial, **imagine that you are a digital forensics analyst working with social change actors such as journalists, activists, human rights advocates, and members of civil society**. You received an email request for assistance from a trusted colleague to analyze a mobile device (Android smartphone) belonging to a collaborator with a well-known collective. This colleague helps you verify the collaborator’s identity, provides context for the situation, and mentions that they conducted an initial interview and performed a data extraction from the device. They then detail the incident and the available information.

### Incident

The data extraction pertains to the device of a human rights defender whose phone was confiscated during a period of detention. It is suspected that during that period, the perpetrator of the threats had the technical capability to gain unauthorized physical access to the device.

The **following information was obtained through the initial interview:**

* On August 26, 2025, at approximately 2:30 p.m. GMT-6, the individual was detained and handed over their unlocked phone, which remained in the perpetrator’s possession.
* The device remained out of the individual’s control until approximately 11:00 a.m. on August 27, 2025—a period of approximately 20 hours.
* Upon receiving the device back, it was completely turned off and out of battery power.
* Over the next ten days, the individual reported unusual behavior: the battery drained quickly, apps frequently froze, and the camera and microphone privacy indicators lit up even when the individual wasn’t opening any apps.
* Days later, people unrelated to the situation directly told the user that they were aware of the content of the user’s private conversations, which prompted the collective’s collaborator to seek technical assistance.

!!! Note
    This narrative is documented solely to provide context for the technical analysis. The purpose of the triage interview is not to confirm or rule out hypotheses, **but to identify events, dates, and behaviors that will guide the next steps of the investigation.**

## Formulating Hypotheses

Before reviewing any MVT results, it is essential to **be clear about what we are trying to prove with the forensic analysis**. In this case, the working hypotheses are:

1. During the period when the device was out of the person’s control, someone with physical access performed an action on the device.
2. There is a temporal correlation between that possible action and the anomalous behavior reported by the individual in the days that followed.

## Setting Up the Working Folder

You must **create a working folder to store a copy of the extraction collected,** choosing a strategic name for that folder, which may contain, for example, a combination of the date and a case or device identifier—without any data that could identify the individual.

Before executing any command, we follow the [data handling practices](../../explainers/05-explainer-mvt-android-triage/index.md#recommendations-for-handling-sensitive-information) mentioned in the MVT exploration explainer for Android triage. Although an AndroidQF dump and a bug report do not contain sensitive user information—that is, they do not include photographs or personal files—they must be **handled with the same care and always in accordance with the consent granted by the requesting individual and any data retention agreements** that have been established.

In this case, we will create the working directory *tutorial-triaje-con-mvt* and access it using the following commands:

```sh
mkdir tutorial-triaje-con-mvt
cd tutorial-triaje-con-mvt
```

Next, create the simulated case folder, referencing the serial number of the ZY323X4MZK device, using the following command.

```sh
mkdir "$(date +"%Y-%m-%d")"-android-ZY323X4MZK
cd "$(date +"%Y-%m-%d")"-android-ZY323X4MZK
```

Copy the extraction sample to the simulated case folder using the following command.

!!! Note "Note"

The following command moves the downloaded sample file from the Downloads folder to the working folder. The exact path may vary in your specific case, depending on where the file is stored and the system language.

```sh
mv ~/Downloads/android-mvt-tutorial-sample.zip .
```

Unzip the archive into the working directory using the following command.

```sh
unzip android-mvt-tutorial-sample.zip
```

## Triage Process with MVT

The steps for performing triage with MVT are detailed below. To do this, first you need to [install MVT](#installing-mvt) on your computer (see system requirements) or [update MVT](#updating-mvt) if you already have it installed.

### Installing MVT

MVT can be installed as a tool from the standard Python package manager using its standalone version (pipx).

The steps to install MVT are as follows:

=== "Linux"

 ```sh
    sudo apt install python3 python3-venv python3-pip sqlite3 libusb-1.0-0
    sudo apt install pipx
    git clone https://github.com/mvt-project/mvt
    cd mvt
    pipx install --force .
    pipx ensurepath
    ```

=== "macOS"

    ```sh
    brew install python3 pipx libusb sqlite3
    git clone https://github.com/mvt-project/mvt
    cd mvt
    pipx install --force .
    ```

!!! warning "Note"

    Currently, MVT does not have a formal installation process for Windows. The tool can be used through the Windows Subsystem for Linux; however, proper functionality is not guaranteed, and this tutorial does not include installation steps for this scenario.

### Updating MVT

To ensure you have the latest tool integrations, change to the cloned repository directory (for example, `cd mvt`) and run the following commands:

```sh
git pull
pipx uninstall mvt
pipx install --force .
```

Return to the working directory where your sample project is located. Once you’ve verified that you have the latest version of the tool—and before running any commands—**download the most recent indicators of compromise using the following command:**

!!! Note

    If you are installing MVT for the first time, you may need to close and reopen the terminal for the MVT commands to become available.

```sh
mvt-android download-iocs
```

### Running MVT on the Test Sample

Once the tool is installed, you can run the corresponding command to analyze an AndroidQF dump:

```sh
mvt-android check-androidqf ./f1b10850-c902-4e67-885a-6ae9b936d76d -o "$(date +"%Y-%m-%d")"-out-androidqf
```

During execution, you will be prompted to enter the password for the `backup.ab` file. The **sample dump uses the password “sd”**, so you must enter these two characters to continue:

```sh
Enter backup password:

Enter "sd" as the password when prompted

```

You’ll know that the MVT analysis process is complete when you see the alert summary, similar to the one shown below:

!!! note "Note"

 This output corresponds to the result of running the analysis on the test sample using MVT version 2026.10.5.

    It may contain differences due to changes in the tool that cause new behaviors to be detected as suspicious. Given the way this material was designed, these changes should not affect your ability to follow along with the exercise.

```sh

╭────────────────────────────────────────────────────────────────────────────────────────── ALERTS ──────────────────────────────────────────────────────────────────────────────────────────╮
│ MVT generated 0 INFORMATIONAL alerts. │
│ MVT generated 2 LOW alerts. │
│ MVT generated 8 MEDIUM alerts. │
│ MVT generated 1 HIGH alert. │
│ MVT generated 0 CRITICAL alerts. │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────────────────────────────────────────────── NOTE ───────────────────────────────────────────────────────────────────────────────────────────╮
│ Please disable Developer Options and ADB (Android Debug Bridge) on the device once you have finished the data acquisition. ADB is a powerful tool that can allow unauthorized access to the │
│ device. │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

╭───────────────────────────────────────────────────────────────────────────────────────── WARNING ──────────────────────────────────────────────────────────────────────────────────────────╮
│ MVT generated HIGH or CRITICAL alerts. Only an expert review can confirm whether the detected indicators are signs of an attack. │
│ │
│ Please seek assistance from a reputable expert if you have serious concerns about a possible spyware attack. Such support is available to human rights defenders and civil society through Amnesty │
│ International’s Security Lab at https://securitylab.amnesty.org/get-help/?c=mvt │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```

**When using the \-o argument, MVT creates output folders and files that are useful for triage and forensic analysis**. If you want to understand what each one contains, you can refer to [the MVT reference guides available in this repository](../../references/index.md). The following code block lists the contents of the working directory using the `ls` command after MVT has finished running.

```sh
alerts.json
alerts_timeline.csv
aqf_files.json
aqf_files_detected.json
aqf_get_prop.json
aqf_get_prop_detected.json
aqf_packages.json
aqf_packages_detected.json
aqf_settings.json
aqf_settings_detected.json
bugreport_timestamps.json
command.log
dbinfo.json
dumpsys_activities.json
dumpsys_adb_state.json
dumpsys_adb_state_detected.json
dumpsys_appops.json
dumpsys_appops_detected.json
dumpsys_battery_daily.json
dumpsys_battery_daily_detected.json
dumpsys_battery_history.json
dumpsys_get_prop.json
dumpsys_get_prop_detected.json
dumpsys_packages.json
dumpsys_receivers.json
info.json
timeline.csv
```

### Reviewing Output

The first thing you’ll see on the screen is a brief summary of the run, along with alerts at their various levels. In this case, you’ll notice that no alerts reached the **CRITICAL** level—in other words, no device data matched the indicators of compromise (IOCs) for known threats uploaded by the MVT.

We identified the following **MEDIUM** alerts:

The Facebook package ***“com.facebook.katana”*** was identified as a non-system package, installed via adb or another method. Although this is likely an app preinstalled by the vendor, it’s important to make a note of it to verify whether it relates to the information sought during triage.

```sh
MEDIUM ALERT   [mvt.android.modules.androidqf.aqf_packages] Found a non-system package installed via adb or another method: "com.facebook.katana"
```

The device has not received security updates for more than six months; this indicates that the phone is no longer supported for updates or that the user has not updated the device.

```sh
MEDIUM ALERT   [mvt.android.modules.androidqf.aqf_getprop] This phone has not received security updates for more than six months (last update: 2021-02-01).
```

Google Play Protect has been identified as disabled. This is a significant indicator of apps being installed from sources outside of Google Play, which may be **unreliable**. It is important to take this into account throughout the triage process.

```sh
MEDIUM ALERT   [mvt.android.modules.androidqf.aqf_settings] Found suspicious "global" setting "upload_apk_enable = 0" (Google Play Protect disabled)
```

The package ***“com.republicwireless.tel”*** was identified as having been uninstalled

```sh
MEDIUM ALERT   [mvt.android.modules.bugreport.dumpsys_battery_daily] Detected uninstall of package com.republicwireless.tel (vers 0)
```

It was determined that no tombstones could be found; in other words, no device crashes were identified by the MVT.

```sh
ERROR [mvt.android.modules.bugreport.tombstones] Unable to find any tombstone files. Did you provide a valid bug report archive?
```

In addition to the **MEDIUM** alerts, there is also a **HIGH**-level alert, which we note:

```sh
HIGH ALERT     [mvt.android.modules.androidqf.aqf_files] Found executable file at suspicious path "/data/local/tmp/.studio/process-tracker"
```

This finding corresponds to a typical Android Studio artifact, so it’s a good example of something that should be documented and cross-checked with the interview—for example, by asking the person if they usually connect their phone to a computer for development purposes—before assuming it’s related to the incident.

Finally, we noted a LOW alert related to a trusted ADB key without its corresponding host key in the dump—something that should be documented and, depending on the context, analyzed.

```sh
LOW ALERT [mvt.android.modules.bugreport.dumpsys_adb_state] Found a trusted ADB host key, but the AndroidQF acquisition does not include its host key:
71:F7:D8:0B:1A:61:48:32:83:E7:21:0C:47:07:FA:F0 (unknown user)
```

#### Review of command.log

Upon carefully reviewing command.log and considering the hypothesis (to check for activity during the time the device was out of the person’s sight), two MEDIUM-level alerts stand out:

```sh
MEDIUM ALERT   [mvt.android.modules.bugreport.dumpsys_appops] Package 'com.google.android.apps.nbu.files' had the risky permission 'REQUEST_INSTALL_PACKAGES' set to 'Reject' on 2025-08-26 15:43:12.384000
MEDIUM ALERT   [mvt.android.modules.bugreport.dumpsys_appops] Package 'com.google.android.apps.nbu.files' had the risky permission 'REQUEST_INSTALL_PACKAGES' set to 'Access' on 2025-08-26 16:25:50.885000
```

These lines show that the package **com.google.android.apps.nbu.files** (Google File Explorer) had a change in the ***REQUEST_INSTALL_PACKAGES*** permission (the permission that allows an app to install other apps), which was first denied at 3:43 PM and then granted at 4:25 PM on the same day and **within the time window during which the person confirms they did not have the device in view.**

This is the kind of correlation we look for when **linking the technical output with the triage interview** and the case timeline.

#### Review of timeline.csv

To delve deeper into this finding, **we searched for that exact time in timeline.csv**:

```sh
grep -C 25 "2025-08-26 16:25:50.885000" timeline.csv
```

In the output, we found the event we needed to understand what happened at that moment:

```sh
"2025-08-26 16:25:50","DumpsysPackages","package_install","Install or update of package com.sterminator"
"2025-08-26 16:25:50.885000","DumpsysAppops","Access","com.google.android.apps.nbu.files access to REQUEST_INSTALL_PACKAGES: Access"
"2025-08-26 16:26:08","DumpsysPackages","package_first_install","Install or update of package com.sterminator"
"2025-08-26 16:26:08","DumpsysPackages","package_last_update","Install or update of package com.sterminator"
```

At the exact moment that installation permission is granted to File Explorer, **the timeline records the installation of a package named *“com.sterminator”***, which we do not recognize. Continuing our review of the timeline a few minutes later, we find additional activity associated with that same package, including access to the clipboard, Wi-Fi network scanning, and toast-style pop-ups, among other things.

#### Review of Detected Files

To review the detected files, we list the results folder generated by the MVT:

```sh
ls *_detected.json
```

We will get the following output:For the names of the module files that matched patterns that triggered alerts according to the MVT, these should be reviewed to understand the context of the detections:

```sh
aqf_files_detected.json     aqf_packages_detected.json  dumpsys_adb_state_detected.json  dumpsys_battery_daily_detected.json
aqf_get_prop_detected.json  aqf_settings_detected.json  dumpsys_appops_detected.json     dumpsys_get_prop_detected.json
```

Upon reviewing ***aqf_packages_detected.json***, we noticed that **com.sterminator** does not appear there; the only package flagged by the MVT in that file remains **com.facebook.katana**, detected solely because it is a third-party package installed outside the system’s standard channels, with no apparent connection to our hypothesis. Furthermore, it can be observed that its installation context is that of an application pre-installed by the vendor and that **its certificate is trusted.**

```json
{
 "level": "MEDIUM",
 "module": "aqf_packages",
 "message": "Found a non-system package installed via adb or another method: \"com.facebook.katana\"",
        "event_time": "",
 "event": {
 "name": "com.facebook.katana",
 "files": [
 {
 "path": "/system/preinstall/facebook/facebook.apk",
 "local_name": "",
 "md5": "96cda5cd37eaed2a8fe62c2b4e7f80b5",
                    "sha1": "135cbf12359440ff66e9e27952a6ce527ba03fbb",
 "sha256": "efc392b747e4031d1424662fa8bec2953c1356adcc11d7f21c1d2d74a0423914",
 "sha512": "e0959eb9b39e4f98ff174ee6cbc5416c5cd18a168a38bff0d0671650c1f4624e5aaac551574733299760f8debf121c30e71707c972c8ec45080e895ebe94ffa2",
 "error": "",
 "verified_certificate": true,
                    "certificate": {
 "Md5": "3fad024f2dcbe3ee693c96f350f8e376",
                        "Sha1": "8a3c4b262d721acd49a4bf97d5213199c86fa2b9",
                        "Sha256": "e3f9e1e0cf99d0e56a055ba65e241b3399f7cea524326b0cdd6ec1327ed0fdc1",
                        "ValidFrom": "2009-08-31T21:52:16Z",
 "ValidTo": "2050-09-25T21:52:16Z",
                        "Issuer": "C=US, ST=CA, L=Palo Alto, O=Facebook Mobile, OU=Facebook, CN=Facebook Corporation",
 "Subject": "C=US, ST=CA, L=Palo Alto, O=Facebook Mobile, OU=Facebook, CN=Facebook Corporation",
 "SignatureAlgorithm": "MD5-RSA",
 "SerialNumber": 1251755536
                    },
 "certificate_error": "",
 "trusted_certificate": true
 }
            ],
 "installer": "null",
 "uid": 10204,
 "disabled": false,
 "system": false,
 "third_party": true
        },
 "matched_indicator": null
    }
```

Similarly, ***dumpsys\_appops\_detected.json*** contains only the File Explorer permission change we previously identified; therefore, it does not include the permissions that the **com.sterminator** package itself requested and used after installation.

```json
{
 "level": "MEDIUM",
 "module": "dumpsys_appops",
 "message": "Package 'com.google.android.apps.nbu.files' had the risky permission 'REQUEST_INSTALL_PACKAGES' set to 'Reject' on 2025-08-26 15:43:12.384000",
        "event_time": "2025-08-26 15:43:12.384000",
 "event": {
 "package_name": "com.google.android.apps.nbu.files",
 "permissions": [
 {
 "name": "REQUEST_INSTALL_PACKAGES",
 "entries": [
 {
                            "access": "Access",
 "type": "top-s",
 "timestamp": "2025-08-26 16:25:50.885000"
                        },
 {
                            "access": "Reject",
 "type": "top-s",
 "timestamp": "2025-08-26 15:43:12.384000"
                        }
 ],
 "access": "allow"
 }
 ],
 "uid": "u0a137"
        },
 "matched_indicator": null
    },
    {
 "level": "MEDIUM",
 "module": "dumpsys_appops",
 "message": "The package 'com.google.android.apps.nbu.files' had the risky permission 'REQUEST_INSTALL_PACKAGES' set to 'Access' on 2025-08-26 16:25:50.885000",
        "event_time": "2025-08-26 16:25:50.885000",
 "event": {
 "package_name": "com.google.android.apps.nbu.files",
 "permissions": [
 {
 "name": "REQUEST_INSTALL_PACKAGES",
 "entries": [
 {
                            "access": "Access",
 "type": "top-s",
 "timestamp": "2025-08-26 16:25:50.885000"
 },
 {
                            "access": "Reject",
 "type": "top-s",
 "timestamp": "2025-08-26 15:43:12.384000"
                        }
 ],
 "access": "allow"
 }
 ],
 "uid": "u0a137"
 },
 "matched_indicator": null
    }
```

This is an important lesson, as **the *detected* files reflect only what the MVT’s heuristics and indicators automatically identified**. In this case, the MVT **did not generate any alerts specifically targeting the com.sterminator package**, nor did its permissions match any known IOCs. We found the relevant discovery by manually reviewing the command.log and timeline.csv, guided by the context of the interview. This reinforces why triage should not be limited solely to reviewing automatic alerts.

Since the *detected* files did not provide further context about ***com.sterminator***, we searched for that package in the rest of the results files by running

```sh
grep -rl "com.sterminator" .
```

We identified that the following files contain some match with the suspicious package.

```sh
./aqf_packages.json
./aqf_settings.json
./dumpsys_activities.json
./dumpsys_appops.json
./dumpsys_battery_history.json
./dbinfo.json
./dumpsys_packages.json
./dumpsys_receivers.json
./timeline.csv
```

Upon reviewing each of these files, we found the following:

***aqf\_packages.json*** confirms the package metadata:

```json
{
 "name": "com.sterminator",
 "files": [
 {
                "path": "/data/app/com.sterminator-Zg6Dv1AHZw3iKUb3Y_8gnQ==/base.apk",
 "local_name": "",
                "md5": "16eb7670e1c4c8cc52820db488811569",
                "sha1": "10d1fe278b821e2e0695857595c12716e3c15792",
 "sha256": "2314d6179c30c6974b3feaf71dc67190767789a1b23569bc01a789bcd058c217",
 "sha512": "1b69e290ab07a58d8eda810ccfa355998d82cd9a3ff800cd4a9a1507242c09ef555a286d83b03d17b7842dfbc4c020b5d0345e31590067a2a9f9a0dc2e419655",
 "error": "",
 "verified_certificate": true,
                "certificate": {
 "Md5": "11ecf9600337646693af674f4a74a85c",
                    "Sha1": "187a87f7f5ede2d279dda0ccde55e6ab85549d70",
                    "Sha256": "1674ab757f8323c10735a600bb06f90354f68f4ee61c71baf22795fa2cc911e6",
                    "ValidFrom": "2023-06-26T13:45:22Z",
 "ValidTo": "2048-06-19T13:45:22Z",
                    "Issuer": "C=IT, CN=LSDroid srl",
 "Subject": "C=IT, CN=LSDroid srl",
 "SignatureAlgorithm": "SHA256-RSA",
                    "SerialNumber": 1
 },
 "certificate_error": "",
 "trusted_certificate": false
 }
        ],
 "installer": "com.google.android.apps.nbu.files",
 "uid": 10210,
 "disabled": false,
 "system": false,
 "third_party": true
    }
```

The package was installed from */data/app/com.sterminator-.../base.apk*, with **"installer": "com.google.android.apps.nbu.files"**—meaning it was installed via File Explorer, not the Google Play Store—and with an untrusted certificate **"trusted\_certificate": false**.

***aqf\_settings.json*** shows that **com.sterminator** appears within *enabled\_notification\_policy\_access\_packages*, meaning it was granted access to notifications and the system’s “Do Not Disturb” policy.

```sh
"enabled_notification_policy_access_packages": "com.motorola.camera2:com.google.android.apps.wellbeing:com.sterminator:com.motorola.arselfie",
```

***dumpsys\_activities.json*** shows that the package registers activities under the internal name **com.terminator** (com.sterminator/com.terminator.StartActivity, com.sterminator/com.terminator.ConfigMain), which suggests that the app has been active and performing various actions.

```json
{
 "intent": "android.intent.action.MAIN",
 "package_name": "com.sterminator",
 "activity": "com.sterminator/com.terminator.StartActivity"
    }
{
 "intent": "android.intent.action.VIEW",
 "package_name": "com.sterminator",
 "activity": "com.sterminator/com.terminator.ConfigMain"
    }
{
 "intent": "android.intent.action.MAIN",
 "package_name": "com.sterminator",
 "activity": "com.sterminator/com.terminator.StartActivity"
    }
{
 "intent": "android.intent.action.VIEW",
 "package_name": "com.sterminator",
 "activity": "com.sterminator/com.terminator.ConfigMain"
    }
{
 "intent": "android.intent.action.MAIN",
 "package_name": "com.sterminator",
 "activity": "com.sterminator/com.terminator.StartActivity"
    }
```

***dumpsys\_appops.json*** shows that theThe app requested and used permissions for precise location, GPS, camera, microphone, clipboard, system windows, and Wi-Fi scanning shortly after it was installed—permissions considered invasive, and it must be verified whether they were granted by the user.

```json
{
 "package_name": "com.sterminator",
 "permissions": [
 {
 "name": "COARSE_LOCATION",
                "entries": [],
 "access": "allow"
 },
 {
 "name": "FINE_LOCATION",
 "entries": [
 {
 "access": "Access",
 "type": "top-s",
 "timestamp": "2025-08-26 16:38:12.301000"
                    },
 {
 "access": "Access",
 "type": "fgsvcl-s",
 "timestamp": "2025-08-26 16:41:04.652000"
                    }
 ],
 "access": "all"
 },
 {
 "name": "GPS",
 "entries": [
                    {
 "access": "Access",
 "type": "top-s",
 "timestamp": "2025-08-26 16:38:14.184000"
 },
 {
                        "access": "Access",
 "type": "fgsvcl-s",
 "timestamp": "2025-08-26 16:41:13.906000"
 }
                ],
 "access": "all"
 },
 {
 "name": "VIBRATE",
 "entries": [
 {
                        "access": "Access",
 "type": "top-s",
 "timestamp": "2025-08-26 16:41:31.431000"
                    },
 {
 "access": "Access",
 "type": "fgsvcl-s",
 "timestamp": "2025-08-26 16:41:31.356000"
                    }
 ],
 "access": "allow"
 },
 {
 "name": "WIFI_SCAN",
 "entries": [
 {
                        "access": "Access",
 "type": "top-s",
 "timestamp": "2025-08-26 16:33:05.821000"
                    },
 {
 "access": "Access",
 "type": "fgsvcl-s",
 "timestamp": "2025-08-26 16:40:00.310000"
                    }
 ],
 "access": "all"
 },
 {
 "name": "WRITE_SETTINGS",
 "entries": [
 {
                        "access": "Access",
 "type": "top-s",
 "timestamp": "2025-08-26 16:41:31.252000"
 },
 {
                        "access": "Access",
 "type": "fgsvcl-s",
 "timestamp": "2025-08-26 16:42:17.564000"
 }
                ],
 "access": "allow"
 },
 {
 "name": "SYSTEM_ALERT_WINDOW",
 "entries": [
 {
                        "access": "Access",
 "type": "top-s",
 "timestamp": "2025-08-26 16:38:09.488000"
                    },
 {
 "access": "Access",
 "type": "fgsvcl-s",
 "timestamp": "2025-08-26 16:42:17.568000"
                    }
 ],
 "access": "allow"
 },
 {
 "name": "CAMERA",
 "entries": [
 {
                        "access": "Access",
 "type": "top-s",
 "timestamp": "2025-08-26 16:42:00.975000"
 },
                    {
 "access": "Access",
 "type": "fgsvcl-s",
 "timestamp": "2025-08-26 16:42:11.306000"
                    }
 ],
 "access": "allow"
 },
 {
 "name": "RECORD_AUDIO",
 "entries": [
 {
                        "access": "Access",
 "type": "top-s",
 "timestamp": "2025-08-26 16:42:01.039000"
                    },
 {
 "access": "Access",
 "type": "fgsvcl-s",
 "timestamp": "2025-08-26 16:42:11.146000"
                    }
 ],
 "access": "allow"
 },
 {
 "name": "READ_CLIPBOARD",
 "entries": [
 {
 "access": "Access",
      "type": "top-s",
 "timestamp": "2025-08-26 16:29:55.458000"
                    }
 ],
 "access": "allow"
 },
 {
 "name": "WRITE_CLIPBOARD",
 "entries": [
                    {
 "access": "Access",
 "type": "top-s",
 "timestamp": "2025-08-26 16:29:38.637000"
                    }
 ],
 "access": "allow"
 },
 {
 "name": "AUDIO_MEDIA_VOLUME",
 "entries": [
 {
                        "access": "Access",
 "type": "top-s",
 "timestamp": "2025-08-26 16:38:14.191000"
                    }
 ],
 "access": "allow"
 },
 {
 "name": "AUDIO_ALARM_VOLUME",
 "entries": [
 {
                        "access": "Access",
 "type": "top-s",
 "timestamp": "2025-08-26 16:37:58.699000"
                    }
 ],
 "access": "allow"
 },
 {
 "name": "WAKE_LOCK",
 "entries": [
                    {
 "access": "Access",
 "type": "top-s",
 "timestamp": "2025-08-26 16:41:31.356000"
                    },
 {
 "access": "Access",
 "type": "fgsvcl-s",
 "timestamp": "2025-08-26 16:42:32.511000"
                    }
 ],
 "access": "allow"
 },
 {
 "name": "MONITOR_LOCATION",
 "entries": [
 {
                        "access": "Access",
 "type": "top-s",
 "timestamp": "2025-08-26 16:38:14.184000"
 },
                    {
 "access": "Access",
 "type": "fgsvcl-s",
 "timestamp": "2025-08-26 16:41:13.893000"
                    }
 ],
 "access": "all"
 },
 {
 "name": "MONITOR_HIGH_POWER_LOCATION",
 "entries": [
 {
                        "access": "Access",
 "type": "top-s",
 "timestamp": "2025-08-26 16:38:14.184000"
                    },
 {
 "access": "Access",
 "type": "fgsvcl-s",
 "timestamp": "2025-08-26 16:41:13.891000"
                    }
 ],
 "access": "all"
            },
 {
 "name": "TOAST_WINDOW",
 "entries": [
 {
 "access": "Access",
 "type": "top-s",
                        "timestamp": "2025-08-26 16:36:47.690000"
                    },
 {
 "access": "Access",
 "type": "fgsvcl-s",
 "timestamp": "2025-08-26 16:30:55.299000"
                    }
 ],
 "access": "allow"
 },
 {
 "name": "TURN_ON_SCREEN",
 "entries": [
                    {
 "access": "Access",
 "type": "top-s",
 "timestamp": "2025-08-26 16:38:09.529000"
                    }
 ],
 "access": "allow"
 },
 {
 "name": "START_FOREGROUND",
 "entries": [
 {
                        "access": "Access",
 "type": "top-s",
 "timestamp": "2025-08-26 16:41:31.356000"
 },
                    {
 "access": "Access",
 "type": "fgsvcl-s",
 "timestamp": "2025-08-26 16:41:31.356000"
 }
                ],
 "access": "allow"
 }
 ],
 "uid": "u0a210"
    }
```

***dumpsys\_battery\_history.json*** confirms multiple start\_top / end\_top events for com.sterminator, meaning that the process came to the foreground at various times after its installation.

```json
{
 "time_elapsed": "+5s349ms",
 "event": "start_top",
 "uid": "u0a210",
 "package_name": "com.sterminator",
        "service": ""
    }
{
 "time_elapsed": "+31s564ms",
 "event": "end_top",
 "uid": "u0a210",
        "package_name": "com.sterminator",
 "service": ""
    }
{
 "time_elapsed": "+32s524ms",
 "event": "start_top",
 "uid": "u0a210",
 ""package_name": "com.sterminator",
 "service": ""
    }
{
 "time_elapsed": "+49s070ms",
        "event": "end_top",
 "uid": "u0a210",
 "package_name": "com.sterminator",
 "service": ""
    }
{
 "time_elapsed": "+50s494ms",
 "event": "start_top",
        "uid": "u0a210",
 "package_name": "com.sterminator",
 "service": ""
    }
```

***dumpsys\_receivers.json*** shows that the package registered multiple receivers (BroadcastReceiver), including several standard components from the WorkManager and Firebase libraries (ConstraintProxy, ProfileInstallReceiver, FirebaseMessagingDirectBootReceiver), as well as a set of receivers with internal names specific to the app.

```json
    {
 "android.intent.action.BOOT_COMPLETED": [
 {
 "package_name": "com.sterminator",
 "receiver": "com.sterminator/com.terminator.BootReceiver"
 }
 ],
 "android.app.action.DEVICE_ADMIN_ENABLED": [
 {
 "package_name": "com.sterminator",
 "receiver": "com.sterminator/com.terminator.AdminReceiver"
 }
      ],
 "android.intent.action.CLOSE_SYSTEM_DIALOGS": [
 {
 "package_name": "com.sterminator",
 "receiver": "com.sterminator/com.terminator.LockScreenReceiver"
 }
      ],
 "shutshut": [
 {
 "package_name": "com.sterminator",
 "receiver": "com.sterminator/com.terminator.LockScreenReceiver"
 }
      ],
 "com.lsdroid.shutdownattempt": [
 {
 "package_name": "com.sterminator",
 "receiver": "com.sterminator/com.terminator.ShutdownAttemptReceiver"
 }
      ],
 "android.net.conn.CONNECTIVITY_CHANGE": [
 {
 "package_name": "com.sterminator",
 "receiver": "com.sterminator/com.terminator.ConnectivityReceiver"
 }
      ],
 "com.terminator.CONN_DELAY": [
 {
 "package_name": "com.sterminator",
 "receiver": "com.sterminator/com.terminator.ConnectivityReceiver"
 }
      ],
 "com.terminator.DAILY_PING": [
 {
 "package_name": "com.sterminator",
 "receiver": "com.sterminator/com.terminator.ConnectivityReceiver"
 }
 ]
    }
```

### Summary of Initial Findings

Based on a review of the command.log, the timeline.csv, and a manual review of the results files, we can construct the following timeline:

1. On August 26, 2025, at 15:43:12, a first failed attempt (Reject) to grant the *REQUEST\_INSTALL\_PACKAGES* permission to the Google File Explorer app was logged.

2. On August 26, 2025, at 16:25:50, the *REQUEST\_INSTALL\_PACKAGES* permission was granted to the same app, and at that exact moment, the system logged the installation of the **com.sterminator** package. A manual review of ***aqf\_packages.json*** confirmed that this package was installed via File Explorer and that its signing certificate is not trusted

3. On August 26, 2025, at 4:26:08 PM, the first installation entry for the package is confirmed.

4. Shortly after installation, the ***aqf\_settings.json*** log shows that **com.sterminator** was added to the *enabled\_notification\_policy\_access\_packages* list, meaning it was granted access to system notifications and the Do Not Disturb policy—a permission that is not automatically granted.

5. On August 26, 2025, between 4:29 PM and 4:42 PM, the package exhibited sustained foreground activity. A review of ***dumpsys\_battery\_history.json*** confirms multiple start\_top / end\_top cycles during this period, and ***dumpsys\_activities.json*** records repeated executions of two internal package activities under *com.terminator.StartActivity* and *com.terminator.ConfigMain*, suggesting that the app may have been configured or actively used during this time. During this same period, the ***dumpsys\_appops.json*** shows that the package requested and used sensitive permissions such as **precise location, GPS, camera, microphone, clipboard, and system windows**—permissions that can be cross-checked with the user to verify whether they were granted with the user’s knowledge.

Additionally, a review of the ***dumpsys\_receivers.json*** file shows that, in addition to the standard receivers from the WorkManager and Firebase libraries, the package registered a receiver for android.app.action.DEVICE\_ADMIN\_ENABLED, indicating that the app **requests device administrator privileges,** along with custom receivers for the lock screen and attempts to power off the device.

All of this activity—from installation, configuration, the device administrator request, and the use of sensitive permissions—occurs within the time window during which, according to the interview, the person did not have the device in their possession (approximately from 2:30 p.m. on August 26at 11:00 a.m. on August 27).

It is important to note that the MVT **did not generate any automatic alerts or identify any matches with known compromise indicators for com.sterminator**. All of these findings stem from a manual review of the results files, guided by the context of the interview and the case timeline, not from the alert summary alone.

### Additional Analysis Steps

Following this initial triage, we were able to confirm that there is evidence of the installation of a third-party application (**com.sterminator**) via File Explorer during the time window when the device was out of the individual’s control, and that this application requested and used sensitive system permissions shortly after installation. The MVT did not generate an automatic alert or a match with known indicators of compromise for this specific package.

Next steps may include:

* Asking the victim specific questions about this activity, such as whether they recognize the name **com.sterminator**, whether they recall seeing windows or notifications related to File Explorer or the installation of an app during that period, whether they have a pattern or PIN set up to unlock the device, and whether Developer Options or USB debugging were enabled on the device prior to the incident.

* Analyze the suspicious app; if the file is still present in the AndroidQF dump, perform static and dynamic analysis, review the permissions declared in its manifest, examine its network behavior, and compare its hashes (MD5, SHA1, SHA256) against threat detection tools such as VirusTotal.

* Provide containment measures and initial recommendations to the affected individual, such as avoiding further use of the device until the analysis is complete, backing up important information separately, and changing the credentials for any accounts that may have been compromised (email, social media).

!!! See "Note"
    It is important to emphasize that this is an initial technical triage, not a full forensic analysis. What we have documented so far is technical evidence that warrants further investigation, potentially including reverse engineering of the installed application, for example. It is not a conclusion regarding the nature, purpose, or origin of that application.

## What You Learned

In this tutorial, **we went through the various output files generated by the MVT**, paying special attention to those that are key when investigating a potential security risk. These include `command.log` as a starting point, `timeline.csv for correlating activity over time, `alerts.json` as a consolidated summary of findings, and the files with the `detected` suffix for delving deeper into each specific alert.

Throughout the tutorial, we emphasized that in practice, it is essential to gather key information during the triage interview so that we can develop hypotheses that serve as a starting point for technical triage. Although a forensic tool **may not** generate any automatic alerts or matches with indicators of compromise, it is important to recognize that the findings themselves are the primary sources of investigation. It was necessary to **link a medium-level alert to the time window indicated by the interviewee and manually review several result files (not just the *detected* ones) to construct a coherent timeline and reach a solid triage conclusion.**

Without a clear hypothesis of what you’re looking for and why, reviewing the MVT output becomes like looking for a needle in a haystack, since you’re faced with lines, packets, and events in the file system, with no common thread to guide you on where to focus your attention.

## Conclusion

**MVT is a powerful tool, but, like any forensic tool, it does not replace an analyst’s judgment.** Its automated alerts and indicators of compromise are a valuable starting point, especially when dealing with already documented threats, but as we’ve seen, many relevant findings can only come to light during a manual review grounded in the context of the case.

Technical triage does not seek absolute certainties or hasty or definitive conclusions; rather, **it focuses on identifying sufficient evidence to determine whether a case warrants a more in-depth forensic analysis and, at the same time, providing timely containment recommendations to the person being assisted.** In our guided example, this meant identifying the installation of an app with permissions and behavior that warrant further investigation, without needing to determine in advance what it was or who installed it—details that are addressed in later stages of the analysis.

We hope this tutorial gives you a solid foundation for getting started with Android device triage. with greater methodological precision.


## Comments

Do you have any **comments or suggestions** about this resource? You can use the **comment feature below** to share your ideas or feedback with us. Please be sure to follow our [code of conduct](../../community/code-of-conduct/). The comment feature links directly to the [_Discussions_ section on GitHub](https://github.com/Socialtic/forensics/discussions), where you **can also participate in discussions directly**, if you prefer.   
