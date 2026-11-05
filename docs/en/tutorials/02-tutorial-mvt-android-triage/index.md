---

title: Tutorial - Using MVT for Technical Triage of Android Devices
summary: Guided excercise to learn how to use MVT to analyze an androidqf extraction
keywords: triage, android, mvt, androidqf
lang: en
tags: [tutorial, android, mvt]
last_updated: 2026-11-04
some_url:
created: 2026-11-04
comments: true
author:
    name: Daniel
    url: https://socialtic.org/quienes-somos/
    description: SocialTIC
translation-review-pending: false

---

# Tutorial: Using MVT for Technical Triage of Android Devices

## Introduction

This document is part of a technical documentation repository whose main objective is to establish a baseline of proven, flexible and accessible knowledge to boost consensual forensic analysis in support of civil society across the globe. To organize the contents, we use the technical documentation framework [Diataxis](../../references/00-glossary/index.md#diataxis).

This resource is a [tutorial](https://diataxis.fr/tutorials/) designed to learn the concepts and skills necessary to perform a technical forensic triage using the [Mobile Verification Toolkit](https://github.com/mvt-project/mvt). This open-source forensic tool, developed by the [Amnesty International Security Lab](https://securitylab.amnesty.org/), allows users to **analyze forensic artifacts from Android and iOS devices for signs of compromise**.

In this context, we define technical triage as the evaluation, with the owner’s consent, of artifacts extracted from a mobile device to **determine whether there are clues, indicators, or behaviors that match known attack vectors**, and which therefore warrant a more in-depth forensic analysis. The result of a technical triage is therefore neither a confirmation nor a dismissal of a possible intrusion, but rather an informed decision on how to proceed with a case.

MVT processes information that has already been extracted, for example, using the AndroidQF tool. It does not access the device directly or extract data on its own, but rather aggregates and organizes the information, comparing it against a set of heuristics for suspicious behavior and indicators of compromise (IOCs), such as known signs of spyware like [Pegasus](https://securitylab.amnesty.org/latest/2026/07/inside-pegasus-the-evolution-of-the-worlds-most-notorious-spyware/) or [Predator](https://securitylab.amnesty.org/latest/2025/12/intellexa-leaks-predator-spyware-operations-exposed/), or stalkerware families.

By the end of this tutorial, **we will know how to install MVT, how to triage an AndroidQF extraction, and how to methodically interpret its results through a guided example based on a hypothetical case**, which covers the entire triage process: from the triage interview to building a timeline of findings.

The original version of this document was written in Spanish by the SocialTIC team. **We appreciate the reviews and suggestions** from the 0xCHE team. Any errors or omissions are the responsibility of the authors. It was automatically translated using the [translation script](https://github.com/Socialtic/forensics/blob/main/scripts/translate-readme.md) and manually reviewed before publication.

We acknowledge the **efforts and leadership of Amnesty International’s Security Lab in developing the MVT tool**, as well as its work to strengthen the global digital forensics community through its [Digital Forensics Fellowship](https://securitylab.amnesty.org/digital-forensics-fellowship/). This material is intended to be compatible with and complementary to these technological and methodological efforts.

This document is complemented by other resources in this repository, including:

* [Explainer: Introduction to technical triage of Android devices](../../explainers/04-explainer-introduction-android-triage/index.md), which covers conceptual aspects of the Android operating system and how it can be compromised.
* [Explainer: Exploring the MVT tool for technical triage of Android devices](../../explainers/05-explainer-mvt-android-triage/index.md), which contains information on how MVT works and its modules for Android.
* [How-to: Technical triage of Android devices using MVT](../../how-tos/06-how-to-triage-android-mvt/index.md), which provides the commands and steps for triaging directly with MVT.
* Guides for the forensic extraction of artifacts, including [the how-to guide for extracting a bugreport](../../how-tos/05-how-to-extract-bugreport/index.md) and [the how-to guide for extraction using AndroidQF](../../how-tos/04-how-to-extract-with-androidqf/index.md).
* Reference materials with information on MVT output:
    * [MVT bugreport output file dictionary](../../references/02-reference-mvt-bugreport-dictionary/index.md)
    * [AndroidQF output file dictionary](../../references/01-reference-androidqf-dictionary/index.md)

## Requirements for following this tutorial

To follow this tutorial, you need the following:

* **Computer**: you need a computer, such as a laptop or desktop. Preferably, the computer should run Linux or macOS, as the tools to be installed are more compatible with these operating systems. If you have a Windows operating system, you can create a [Linux virtual machine](https://ubuntu.com/tutorials/how-to-run-ubuntu-desktop-on-a-virtual-machine-using-virtualbox#1-overview) or install [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/install).
* **Download the forensic sample to analyze**: to follow this tutorial, you need a forensic sample to analyze with MVT.
    * Download the test sample for this exercise from [this link](https://drive.google.com/file/d/1OpTwa5Bm5j34UaEY7j4hzI6D5OnwMr4E/view?usp=drive_link).
    * If you want to analyze a different sample, we recommend that you first complete this tutorial and the [Tutorial: Exploring AndroidQF for data acquisition on Android](../01-tutorial-learning-androidqf/index.md) to familiarize yourself with the tools. You can then use the how-to guides to guide your extraction and triage process.
* **Installing Git:** you need to [install Git on your computer](https://github.com/git-guides/install-git), since the tool is installed from its official repository.
* **Installing tools:** the [installation section](#installing-mvt) of this tutorial details the steps for installing MVT.
* **Prior knowledge:** this tutorial assumes you have basic familiarity with the command line (navigating between folders, running simple commands) and with general concepts of forensic triage, such as the importance of an initial interview and the responsible handling of sensitive data. Before you begin, we recommend reviewing the [explanatory material on technical triage of Android devices](../../explainers/04-explainer-introduction-android-triage/index.md) and the [explanatory material on technical triage using MVT](../../explainers/05-explainer-mvt-android-triage/index.md).

**Below is a fictional incident scenario and step-by-step instructions for performing the triage process**, accompanied by concise interpretive explanations to help analysts reach a triage conclusion.

## Case context

For this tutorial, **imagine that you are a digital forensics analyst working with at-risk individuals such as journalists, activists, human rights defenders, and members of civil society**. You received an email request for support from a trusted colleague at a human rights organization to analyze a mobile device (Android smartphone) belonging to a collaborator of a well-known collective. This colleague helps you verify the collaborator’s identity, gives you context on the situation, and mentions that they conducted an initial interview and an extraction of the device. They they provide the following incident report. 

### Incident

The extraction belongs to the device of a human rights defender whose phone was held during a period of detention. It is suspected that during that period, the actor involved had the technical capability to gain unauthorized physical access to the device.

The **following information was obtained during an initial interview:**

* On August 26, 2025, at approximately 14:30 GMT-6, the person was detained and handed over their unlocked phone, which remained in the actor’s possession.
* The device remained out of the person’s control until approximately 11:00 on August 27, 2025, a period of approximately 20 hours.
* When the person received the device back, it was completely turned off and out of battery.
* Over the following ten days, the person reported unusual behavior: the battery drained quickly, apps frequently froze, and the camera and microphone privacy indicators turned on without the person opening any app.
* Days later, people unrelated to the situation told the person directly that they knew the content of their private conversations, which prompted the collective’s collaborator to seek technical support.

!!! note "Note"

    This narrative is documented solely to provide context for the technical analysis. The purpose of the triage interview is not to confirm or rule out hypotheses, **but to identify events, dates, and behaviors that will guide the next steps of the investigation.**

## Formulating hypotheses

Before reviewing any MVT results, it is essential to **be clear about what we are trying to prove with the forensic analysis**. In this case, the working hypotheses are:

1. During the period when the device was out of the person’s control, someone with physical access performed an action on the device.
2. There is a temporal correlation between that possible action and the anomalous behavior reported by the person in the following days.

## Setting up the working folder

You must **create a working folder to store a copy of the collected extraction,** using a consistent approach. It may contain, for example, a combination of the date and a case or device identifier, without any data that could identify the person.

Before running any command, we follow the [data handling practices](../../explainers/05-explainer-mvt-android-triage/index.md#recommendations-for-handling-sensitive-information) described in the explainer on exploring MVT for Android triage. Although an AndroidQF extraction and a bugreport do not contain sensitive user content, that is, they do not include photographs or personal files, they must be **handled with the same care and always in accordance with the consent granted by the requesting person and any data retention agreements** that have been established.

In this case, we will create the working folder *mvt-triage-tutorial* and access it using the following commands:

```sh
mkdir mvt-triage-tutorial
cd mvt-triage-tutorial
```

Next, create the simulated case folder, referencing the device serial number ZY323X4MZK, using the following command. The command adds the current date and time to the folder name. 

```sh
mkdir "$(date +"%Y-%m-%d")"-android-ZY323X4MZK
cd "$(date +"%Y-%m-%d")"-android-ZY323X4MZK
```

Copy the extraction sample to the simulated case folder using the following command.

!!! note "Note"

    The following command moves the downloaded sample file from the Downloads folder to the working folder. The exact path may vary in your case, depending on where the file is stored and the system language.

```sh
mv ~/Downloads/android-mvt-tutorial-sample.zip .
```

Unzip the extraction into the working folder using the following command.

```sh
unzip android-mvt-tutorial-sample.zip
```

## Triage process with MVT

The steps for performing the triage with MVT are detailed below. First, you need to [install MVT](#installing-mvt) on your computer (see the computer requirements) or [update MVT](#updating-mvt) if you already have it installed.

### Installing MVT

MVT can be installed as a tool from Python's standard package manager (pipx).

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

To make sure you have the latest version of the tool, change to the cloned repository directory (for example, `cd mvt`) and run the following commands:

```sh
git pull
pipx uninstall mvt
pipx install --force .
```

Go back to the working folder where the sample is located. Once you have made sure you have the latest version of the tool, and before running any analysis, **download the most recent indicators of compromise using the following command:**

!!! note "Note"

    If you are installing MVT for the first time, you may need to close and reopen the terminal for the MVT commands to become available.

```sh
mvt-android download-iocs
```

### Running MVT on the test sample

You can now run the MVT command to analyze an AndroidQF extraction:

```sh
mvt-android check-androidqf ./f1b10850-c902-4e67-885a-6ae9b936d76d -o "$(date +"%Y-%m-%d")"-out-androidqf
```

During execution, you will be prompted to enter the password for the `backup.ab` file. **The sample extraction uses the password “sd”**, so you must enter these two characters to continue:

```sh
Enter backup password:

Enter "sd" as the password when prompted

```

You will know that the MVT analysis is complete when you see the alert summary, similar to the one shown below:

!!! note "Note"

    This output corresponds to the result of running the analysis on the test sample with MVT version 2026.10.5.

    It may differ due to changes in the tool that cause new behaviors to be detected as suspicious. Given the way this material was designed, these changes should not affect your ability to follow the exercise.

```sh

╭────────────────────────────────────────────────────────────────────────────────────────── ALERTS ──────────────────────────────────────────────────────────────────────────────────────────╮
│ MVT produced 0 INFORMATIONAL alerts.                                                                                                                                                       │
│ MVT produced 2 LOW alerts.                                                                                                                                                                 │
│ MVT produced 8 MEDIUM alerts.                                                                                                                                                              │
│ MVT produced 1 HIGH alerts.                                                                                                                                                                │
│ MVT produced 0 CRITICAL alerts.                                                                                                                                                            │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

╭─────────────────────────────────────────────────────────────────────────────────────────── NOTE ───────────────────────────────────────────────────────────────────────────────────────────╮
│ Please disable Developer Options and ADB (Android Debug Bridge) on the device once finished with the acquisition. ADB is a powerful tool which can allow unauthorized access to the        │
│ device.                                                                                                                                                                                    │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

╭───────────────────────────────────────────────────────────────────────────────────────── WARNING ──────────────────────────────────────────────────────────────────────────────────────────╮
│ MVT produced HIGH or CRITICAL alerts. Only expert review can confirm if the detected indicators are signs of an attack.                                                                    │
│                                                                                                                                                                                            │
│ Please seek reputable expert help if you have serious concerns about a possible spyware attack. Such support is available to human rights defenders and civil society through Amnesty      │
│ International's Security Lab at https://securitylab.amnesty.org/get-help/?c=mvt                                                                                                            │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```

**When using the -o argument, MVT creates output folders and files that are useful for triage and forensic analysis**. If you want to understand what each one contains, you can refer to [the MVT reference dictionaries available in this repository](../../references/index.md). The following code block lists the contents of the working folder using the `ls` command after MVT has finished running.

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

### Reviewing the output

The first thing we will see on screen is a brief summary of the run, along with the alerts at their different levels. In this case, you will notice that no alert reached the **CRITICAL** level, which means that no device data matched the indicators of compromise (IOCs) of known threats loaded by MVT.

We identified the following **MEDIUM** alerts:

The Facebook package ***“com.facebook.katana”*** was identified as a non-system package, installed via adb or another method. Although it is most likely an app preinstalled by the vendor, it is important to take note of it to verify whether it relates to the information sought in the triage.

```sh
MEDIUM ALERT   [mvt.android.modules.androidqf.aqf_packages] Found a non-system package installed via adb or another method: "com.facebook.katana"
```

The device has not received security updates for more than six months. This indicates that the phone is no longer supported or that the user has not updated the device.

```sh
MEDIUM ALERT   [mvt.android.modules.androidqf.aqf_getprop] This phone has not received security updates for more than six months (last update: 2021-02-01).
```

Google Play Protect was identified as disabled. This is an important indicator for the installation of apps from outside Google Play, which may be **untrusted**. It is important to keep this in mind throughout the triage.

```sh
MEDIUM ALERT   [mvt.android.modules.androidqf.aqf_settings] Found suspicious "global" setting "upload_apk_enable = 0" (disabled Google Play Protect)
```

The package ***“com.republicwireless.tel”*** was identified as uninstalled.

```sh
MEDIUM ALERT   [mvt.android.modules.bugreport.dumpsys_battery_daily] Detected uninstall of package com.republicwireless.tel (vers 0)
```

No tombstones could be found, which means that MVT did not identify any device crash.

```sh
ERROR          [mvt.android.modules.bugreport.tombstones] Unable to find any tombstone files. Did you provide a valid bugreport archive?
```

In addition to the **MEDIUM** alerts, there is also a **HIGH** alert, which we take note of:

```sh
HIGH ALERT     [mvt.android.modules.androidqf.aqf_files] Found executable file at suspicious path "/data/local/tmp/.studio/process-tracker"
```

This finding corresponds to a typical Android Studio artifact, so it is a good example of something that should be documented and cross-checked with the interview, for example, by asking the person if they usually connect their phone to a computer for development purposes, before assuming it is related to the incident.

Finally, we noted a LOW alert related to a trusted ADB key without its corresponding host key in the extraction, something that should be documented and, depending on the context, analyzed.

```sh
LOW ALERT      [mvt.android.modules.bugreport.dumpsys_adb_state] Found a trusted ADB host key, but the AndroidQF acquisition does not include its host key:
71:F7:D8:0B:1A:61:48:32:83:E7:21:0C:47:07:FA:F0 (unknown user)
```

#### Reviewing command.log

When carefully reviewing command.log with the hypothesis in mind (checking for activity during the window in which the device was out of the person’s sight), two MEDIUM alerts stand out:

```sh
MEDIUM ALERT   [mvt.android.modules.bugreport.dumpsys_appops] Package 'com.google.android.apps.nbu.files' had risky permission 'REQUEST_INSTALL_PACKAGES' set to 'Reject' at 2025-08-26 15:43:12.384000
MEDIUM ALERT   [mvt.android.modules.bugreport.dumpsys_appops] Package 'com.google.android.apps.nbu.files' had risky permission 'REQUEST_INSTALL_PACKAGES' set to 'Access' at 2025-08-26 16:25:50.885000
```

These lines show that the package **com.google.android.apps.nbu.files** (Files by Google) had a change in the ***REQUEST\_INSTALL\_PACKAGES*** permission (the permission that allows an app to install other apps): it was first denied at 15:43 and then granted at 16:25, on the same day and **within the time window during which the person confirms they did not have the device in sight.**

This is the kind of correlation we look for when **connecting the technical output with the triage interview** and the case timeline.

#### Reviewing timeline.csv

To dig deeper into this finding, **we search for that same time in timeline.csv**:

```sh
grep -C 25 "2025-08-26 16:25:50.885000" timeline.csv
```

In the output, we find the event we were missing to understand what happened at that moment:

```sh
"2025-08-26 16:25:50","DumpsysPackages","package_install","Install or update of package com.sterminator"
"2025-08-26 16:25:50.885000","DumpsysAppops","Access","com.google.android.apps.nbu.files access to REQUEST_INSTALL_PACKAGES: Access"
"2025-08-26 16:26:08","DumpsysPackages","package_first_install","Install or update of package com.sterminator"
"2025-08-26 16:26:08","DumpsysPackages","package_last_update","Install or update of package com.sterminator"
```

At the same instant that the installation permission is granted to Files by Google, **the timeline records the installation of a package named *“com.sterminator”***, which we do not recognize. Continuing the review of the timeline a few minutes later, we find additional activity associated with that same package: clipboard access, Wi-Fi network scanning, and pop-up windows, among others.

#### Reviewing *detected* files

To review the *detected* files, we list the results folder generated by MVT:

```sh
ls *_detected.json
```

The output shows the names of the files for the modules that matched patterns that triggered alerts according to MVT. These should be reviewed to understand the context of the detections:

```sh
aqf_files_detected.json     aqf_packages_detected.json  dumpsys_adb_state_detected.json  dumpsys_battery_daily_detected.json
aqf_get_prop_detected.json  aqf_settings_detected.json  dumpsys_appops_detected.json     dumpsys_get_prop_detected.json
```

When reviewing ***aqf\_packages\_detected.json***, we notice that **com.sterminator** does not appear there. The only package flagged by MVT in that file is still **com.facebook.katana**, detected only because it is a third-party package installed outside the system’s standard channels, with no apparent connection to our hypothesis. We can also see that its installation context is that of an app preinstalled by the vendor, and that **its certificate is trusted.**

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

Similarly, ***dumpsys\_appops\_detected.json*** only contains the Files by Google permission change we already identified, so it does not include the permissions that the **com.sterminator** package itself requested and used after it was installed.

```json
{
        "level": "MEDIUM",
        "module": "dumpsys_appops",
        "message": "Package 'com.google.android.apps.nbu.files' had risky permission 'REQUEST_INSTALL_PACKAGES' set to 'Reject' at 2025-08-26 15:43:12.384000",
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
        "message": "Package 'com.google.android.apps.nbu.files' had risky permission 'REQUEST_INSTALL_PACKAGES' set to 'Access' at 2025-08-26 16:25:50.885000",
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

This is an important learning point, since **the *detected* files only reflect what MVT’s heuristics and indicators identified automatically**. In this case, MVT **did not generate any alert specifically targeting the com.sterminator package**, nor did its permissions match any known IOC. We found the relevant finding by manually reviewing command.log and timeline.csv, guided by the context of the interview. This reinforces why triage cannot be limited to reading the alert summary.

Since the *detected* files did not provide further context about ***com.sterminator***, we search for that package in the rest of the results files by running:

```sh
grep -rl "com.sterminator" .
```

We find that the following files have some match with the suspicious package:

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

Reviewing each of these files, we find the following:

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

The package was installed from */data/app/com.sterminator-.../base.apk*, with **"installer": "com.google.android.apps.nbu.files"**, meaning it was installed through Files by Google, not the Google Play Store, and with an untrusted certificate, **"trusted\_certificate": false**.

***aqf\_settings.json*** shows that **com.sterminator** appears within *enabled\_notification\_policy\_access\_packages*, meaning it was granted access to notifications and to the system’s “Do Not Disturb” policy.

```sh
"enabled_notification_policy_access_packages": "com.motorola.camera2:com.google.android.apps.wellbeing:com.sterminator:com.motorola.arselfie",
```

***dumpsys\_activities.json*** shows that the package registers activities under the internal name **com.terminator** (com.sterminator/com.terminator.StartActivity, com.sterminator/com.terminator.ConfigMain), which suggests that the app has been active and performing different actions.

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

***dumpsys\_appops.json*** shows that the app requested and used permissions for precise location, GPS, camera, microphone, clipboard, system windows, and Wi-Fi scanning shortly after it was installed. These permissions are considered invasive, and it must be verified whether they were granted by the user.

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

***dumpsys\_battery\_history.json*** confirms multiple start\_top / end\_top events for com.sterminator, meaning that the process came to the foreground at different times after its installation.

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
        "package_name": "com.sterminator",
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

### Summary of initial findings

Based on the review of command.log, timeline.csv, and the manual review of the results files, we can build the following timeline:

1. On August 26, 2025, at 15:43:12, a first failed attempt (Reject) to grant the *REQUEST\_INSTALL\_PACKAGES* permission to the Files by Google app is recorded.

2. On August 26, 2025, at 16:25:50, the *REQUEST\_INSTALL\_PACKAGES* permission is granted to the same app, and at that same instant the system records the installation of the **com.sterminator** package. The manual review of ***aqf\_packages.json*** confirmed that this package was installed through Files by Google and that its signing certificate is not trusted.

3. On August 26, 2025, at 16:26:08, the first installation record of the package is confirmed.

4. Shortly after the installation, ***aqf\_settings.json*** shows that **com.sterminator** was added to the *enabled\_notification\_policy\_access\_packages* list, meaning it was granted access to notifications and to the system’s Do Not Disturb policy, a permission that is not granted automatically.

5. On August 26, 2025, between 16:29 and 16:42, the package showed sustained foreground activity. The review of ***dumpsys\_battery\_history.json*** confirms multiple start\_top / end\_top cycles during this period, and ***dumpsys\_activities.json*** records repeated executions of two internal activities of the package, *com.terminator.StartActivity* and *com.terminator.ConfigMain*, which suggests that the app may have been configured or actively used during this time. In this same period, ***dumpsys\_appops.json*** shows that the package requested and used sensitive permissions such as **precise location, GPS, camera, microphone, clipboard, and system windows**, permissions that can be checked with the person to verify whether they were granted with their knowledge.

Additionally, the review of ***dumpsys\_receivers.json*** shows that, besides the standard receivers from the WorkManager and Firebase libraries, the package registered a receiver for android.app.action.DEVICE\_ADMIN\_ENABLED, which indicates that the app **requests device administrator privileges**, along with custom receivers for the lock screen and for attempts to shut down the device.

All of this activity, from the installation and configuration to the device administrator request and the use of sensitive permissions, happens within the time window during which, according to the interview, the person did not have the device in their possession (approximately from 14:30 on August 26 to 11:00 on August 27).

It is important to note that MVT **did not generate any automatic alert or identify any match with known indicators of compromise for com.sterminator**. All of these findings come from the manual review of the results files, guided by the context of the interview and the case timeline, not from the alert summary alone.

### Additional analysis steps

Following this initial triage, we were able to confirm that there is evidence of the installation of a third-party app (**com.sterminator**) through Files by Google during the time window in which the device was out of the person’s control, and that this app requested and used sensitive system permissions shortly after it was installed. MVT did not generate an automatic alert or a match with known indicators of compromise for this specific package.

Next steps may include:

* Asking the human rights defender specific questions about this activity, such as whether they recognize the name **com.sterminator**, whether they remember seeing windows or notifications related to Files by Google or to the installation of an app during that period, whether they have an unlock pattern or PIN set up, and whether Developer Options or USB debugging were enabled on the device before the incident.

* Analyzing the suspicious app: if the base.apk file is still present in the extraction, you can perform static and dynamic analysis, review the permissions declared in its manifest and its network behavior, and compare its hashes (md5, sha1, sha256) against threat detection tools such as VirusTotal.

* Providing containment and initial recommendations to the human rights defender, such as avoiding further use of the device until the analysis is complete, backing up important information separately, and changing the credentials of any accounts that may have been exposed (email, social media).

!!! note "Note"

    It is important to emphasize that this is a triage, not a full forensic analysis. What we have documented so far is technical evidence that warrants a deeper investigation, potentially including reverse engineering of the installed app, for example. It is not a conclusion about the nature, purpose, or origin of that app.

## What you learned

In this tutorial, **we went through the different output files generated by MVT**, paying special attention to those that are key when investigating a suspected compromise: `command.log` as a starting point, `timeline.csv` for correlating activity over time, `alerts.json` as a consolidated summary of findings, and the files with the *detected* suffix to dig deeper into each specific alert.

Throughout the tutorial, we emphasized that in practice it is essential to gather key information during the triage interview so that we can develop hypotheses that serve as a starting point for the technical triage. Even when a forensic tool does **not** generate any automatic alert or match with indicators of compromise, a manual review based on the key data points obtained during the interview can lead to the discovery of suspicious activity. 

Without a clear hypothesis of what you are looking for and why, reviewing MVT output becomes like looking for a needle in a haystack, since you are faced with lines, packages, and file system events, with no common thread to tell you where to focus your attention.

## Conclusion

**MVT is a powerful tool, but, like any forensic tool, it does not replace an analyst’s judgment.** Its automated alerts and indicators of compromise are a valuable starting point, especially for already documented threats, but as we saw, many relevant findings can only come to light during a manual review grounded in the context of the case.

A good triage does not seek absolute certainty or hasty, definitive conclusions. Rather, **we look for enough evidence to decide whether a case warrants a more in-depth forensic analysis, and to offer timely containment recommendations to the person being supported in the meantime.** In our guided example, this meant identifying the installation of an app with permissions and behavior that warrant further investigation, without needing to state in advance what it was or who installed it, which belongs to later stages of the analysis.

We hope this tutorial gives you a solid foundation to start performing Android device triage with greater methodological precision.


## Comments

Do you have any **comments or suggestions** about this resource? You can use the **comment feature below** to share your ideas or feedback with us. Please be sure to follow our [code of conduct](../../community/code-of-conduct/index.md). The comment feature links directly to the [_Discussions_ section on GitHub](https://github.com/Socialtic/forensics/discussions), where you **can also participate in discussions directly**, if you prefer.
