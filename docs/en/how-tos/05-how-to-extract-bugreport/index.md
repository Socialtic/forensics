---
title: How to extract a bugreport from an Android device?
summary: Instructiones extract a bugreport from an Android device
keywords: triage, android, bugreport, 
lang: en
tags: [how-to, intro]
last_updated: 2025-08-27
some_url:
created: 2025-08-27
comments: true
author:
    name: Daniel
    url: https://socialtic.org/quienes-somos/
    description: SocialTIC

---

# How to extract a bugreport from an Android device?


This resource falls under the **[how-to guides](../)** and details the steps required to generate a bugreport, both using the ADB debugging console and through the device’s graphical user interface (GUI). It is an introductory material, complementary to other resources such as the [explainer on log-based forensics for Android devices](../../explainers/03-explainer-log-forensics-android/) and the guide on [how to enable ADB](../../how-tos/03-how-to-enable-adb/).


**We appreciate the collaboration of [RSF Security Lab](https://rsf.org/en/digital-security-lab)**, who provided us with a set of guides and screenshots that enabled the development of this resource. 


## What is a bugreport and why is it useful?

As the name suggests, a bugreport is a collection of **logs and diagnostic information** that helps identify and fix errors when developing an Android application.  In the context of consent-based forensic analysis, the bugreport is a valuable forensic artifact for Android device triage, including use with the MVT tool. For instance, Amnesty Tech used a similar technique to [detect the NoviSpy spyware](https://securitylab.amnesty.org/latest/2024/12/tech-guide-detecting-novispy-spyware-with-androidqf-and-the-mobile-verification-toolkit-mvt/).

Android natively allows generating bugreports both through the [graphical user interface](../../references/00-glossary/index.md#graphical-user-interface) and through the ADB console. Below we include instructions on how to generate a bugreport through both approaches. 


## What do you need to extract a bugreport?

Below are the requirements for extracting a bugreport using the graphical interface (GUI) and the ADB console.

=== "GUI"

    To extract the bugreport from the GUI, it is necessary to have access to the Android device and to **enable developer options**. If you are not sure how to enable developer options on your device, consult this [how-to guide](../02-how-to-enable-developer-options/).

=== "Using ADB"

    To extract Para extraer un bugreport a través de la consola de ADB es necesario: 

    * The **Android device to be analyzed**: Enable Developer Mode and USB Debugging. If needed, consult our guides on [enabling Developer Options](../../references/00-glossary/index.md#developer-mode) or on how to [enable ADB](../../references/00-glossary/index.md#adb).
    * **A computer (Windows, Linux, or macOS):** This will be used for the extraction. 
    * A **data transfer cable** (phone-to-computer).


## Steps to generate a bugreport using the GUI

On most Android devices, it is possible to **generate a bugreport without installing additional tools**, simply by navigating through the device menus. This is the **preferred method** when asking a defender to share this forensic artifact **remotely**.


!!! Tip "Do you need to generate bugreports on several devices? Try ADB"

    Extracting a bugreport using ADB might be quicker and more efficient if you need to extract information from more than one device.  

    [:octicons-arrow-right-24: Take me to the ADB instructions](#steps-to-generate-a-bugreport-via-the-adb-console)


Because of how the Android operating system is developed and the additional customization layers added by each manufacturer, the **exact instructions to generate a bugreport vary slightly across manufacturers**. Below we present instructions for a few common models and customization layers. 


!!! question "WWhy do instructions vary across devices?"

    The Android operating system is based on the [*Android Open Source Project*](https://source.android.com/)*.* However, most manufacturers [use a propietary version developed by Google](https://www.makeuseof.com/tag/android-really-open-source-matter/), on top of which manufacturers add personalization layers. 

    [:octicons-arrow-right-24: Read more here](../02-how-to-enable-developer-options/#why-are-there-different-ways-to-enable-them) 



### Honor Magic 5 Lite (Magic OS) 

To generate a bugreport you **need access to developer options**. If this menu has not yet been enabled, follow these [steps to enable developer options on a Honor device](../02-how-to-enable-developer-options/#honor-magic-os).

Once developer options are enabled, follow these steps to generate a bugreport (see Image 1):
 

1. Open **Settings**
2. Navigate to the menu **System & Updates**
3. Go to **Developer Options**
4. Select **Create bug report**
5. Choose **Full Report**
6. Tap “**Report”**
7. When the bugreport is complete, a notification indicating "**Bug report captured**" will appear. Tap the notification to **open the sharing settings**.   
8. You will see a warning message informing about sensitive data. Click **Ok**  
9. Select the preferred mechanism and **share the bugreport**  


![ Steps to generate a bug report on a Honor Magic Lite con la versión Magic OS 7.1 en Android 13](../../../assets/05-how-to/bug-report-honor-magic5-lite.gif "image 1"){: style="height:480x;width:216px"}
/// caption
**image 1**.  Steps to generate a bug report on a Honor Magic Lite running Magic OS 7.1.
///


### Motorola (Hello UI)

To generate a bugreport you **need access to developer options**. If this menu has not yet been enabled, follow these [steps to enable developer options on a  Motorola device](../02-how-to-enable-developer-options/index.md#motorola-hello-ui)**.

Once developer options are enabled, follow these steps to generate a bugreport (see Image 2):

1. Open **Settings**
2. Navigate to the menu **System**
3. Go to **Developer Options**
4. Select **Bug report**
5. Choose **Full Report**
6. Tap “**Report”**
7. When the bugreport is complete, a notification indicating "**Bug report captured**" will appear. Tap the notification to **open the sharing settings**.   
8. You will see a warning message informing about sensitive data. Click **Ok**  
9. Select the preferred mechanism and **share the bugreport**  

![ Steps to generate a bug report on a Motorola Edge Neo 40 utilizando Hello UI en Android 13](../../../assets/05-how-to/bug-report-motorola-edge-40-neo.gif "image 4"){: style="height:480x;width:216px"}
/// caption
**image 2**.  Steps to generate a bug report on a Motorola Edge Neo 40 running Hello UI.
///

### Nokia  

To generate a bugreport you **need access to developer options**. If this menu has not yet been enabled, follow these [steps to enable developer options on a  Nokia device](../02-how-to-enable-developer-options/index.md#nokia)**. 

Once developer options are enabled, follow these steps to generate a bugreport (see Image 3):


1. Open **Settings**
2. Navigate to the menu **System**
3. Go to **Developer Options**
4. Select **Bug report**
5. Choose **Full Report**
6. Tap “**Report”**
7. When the bugreport is complete, a notification indicating "**Bug report captured**" will appear. Tap the notification to **open the sharing settings**.   
8. You will see a warning message informing about sensitive data. Click **Ok**  
9. Select the preferred mechanism and **share the bugreport**  

![ Steps to generate a bug report on a Nokia G42 5G utilizando Android 13\.](../../../assets/05-how-to/bug-report-nokia-g42.gif "image 4"){: style="height:480x;width:216px"}
/// caption
**image 3**.  Steps to generate a bug report on a Nokia G42 5G running Android 13.
///

### Oppo (Magic OS)

To generate a bugreport you **need access to developer options**. If this menu has not yet been enabled, follow these [steps to enable developer options on a Oppo device](../02-how-to-enable-developer-options/index.md#oppo-reno-10-color-os)**. 

Once developer options are enabled, follow these steps to generate a bugreport (see Image 4):

1. Open **Settings**
2. Navigate to the menu **Additional Settings**
3. Go to **Developer Options**
4. Select **Bug report**
5. Choose **Full Report**
6. Tap “**Report”**
7. When the bugreport is complete, a notification indicating "**Bug report captured**" will appear. Tap the notification to **open the sharing settings**.   
8. You will see a warning message informing about sensitive data. Click **Ok**  
9. Select the preferred mechanism and **share the bugreport**  



![Steps to generate a bug report on a OPPO Reno 10 utilizando Android 13](../../../assets/05-how-to/bug-report-oppo-reno10-5g.gif "image 5"){: style="height:480x;width:216px"}
/// caption
**image 4**. Steps to generate a bug report on a OPPO Reno 10 running Android 13
///


### Realme (Realme UI)

To generate a bugreport you **need access to developer options**. If this menu has not yet been enabled, follow these [steps to enable developer options on a Realme device](../02-how-to-enable-developer-options/index.md#realme-realme-ui)**. 

Once developer options are enabled, follow these steps to generate a bugreport (see Image 5):

1. Open **Settings**
2. Navigate to the menu **Additional Settings**
3. Go to **Developer Options**
4. Select **Bug report**
5. Choose **Full Report**
6. Tap “**Report”**
7. When the bugreport is complete, a notification indicating "**Bug report captured**" will appear. Tap the notification to **open the sharing settings**.   
8. You will see a warning message informing about sensitive data. Click **Ok**  
9. Select the preferred mechanism and **share the bugreport**  


![ Steps to generate a bug report on a Realme GT2 Pro con RealMe UI 4.0 utilizando Android 13](../../../assets/05-how-to/bug-report-realme-gt2-pro.gif "image 6"){: style="height:480x;width:216px"}
/// caption
**image 5**. Steps to generate a bug report on a Realme GT2 Pro with RealMe UI 4.0 and Android 13
///

### Samsung (One UI)

To generate a bugreport you **need access to developer options**. If this menu has not yet been enabled, follow these [steps to enable developer options on a Samsung device](../02-how-to-enable-developer-options/index.md#samsung-one-ui)**. 

Once developer options are enabled, follow these steps to generate a bugreport (see Image 6):

1. Open **Settings**
2. Go to **Developer Options**
3. Select **Bug report**
4. Choose **Full Report**
5. Tap “**Report”**
6. When the bugreport is complete, a notification indicating "**Bug report captured**" will appear. Tap the notification to **open the sharing settings**.   
7. You will see a warning message informing about sensitive data. Click **Ok**  
8. Select the preferred mechanism and **share the bugreport**  

![ Steps to generate a bug report on a Samsung Galaxy A54 con One UI en un dispositivo utilizando Android 13](../../../assets/05-how-to/bug-report-samsung-galaxy-a54-5g.gif "image 7"){: style="height:480x;width:216px"}
/// caption
**image 6**. Steps to generate a bug report on a Samsung Galaxy A54 with One UI and Android 13
///

### Sony (Xperia UI)


To generate a bugreport you **need access to developer options**. If this menu has not yet been enabled, follow these [steps to enable developer options on a Sony device](../02-how-to-enable-developer-options/index.md#sony-xperia-ui)**.

Once developer options are enabled, follow these steps to generate a bugreport (see Image 7):

1. Open **Settings**
2. Navigate to the menu **System**
3. Go to **Developer Options**
4. Select **Bug report**
5. Choose **Full Report**
6. Tap “**Report”**
7. When the bugreport is complete, a notification indicating "**Bug report captured**" will appear. Tap the notification to **open the sharing settings**.   
8. You will see a warning message informing about sensitive data. Click **Ok**  
9. Select the preferred mechanism and **share the bugreport**  

![ Steps to generate a bug report on a Sony Xperia 10V con Xperia UI 4.0 utilizando Android 14\.](../../../assets/05-how-to/bug-report-sony-xperia-10-v.gif "image 8"){: style="height:480x;width:216px"}
/// caption
**image 7**. Steps to generate a bug report on a Sony Xperia 10V with Xperia UI 4.0 running Android 14\.
///


### Tecno (Hi OS)

To generate a bugreport you **need access to developer options**. If this menu has not yet been enabled, follow these [steps to enable developer options on a Tecno device](../02-how-to-enable-developer-options/index.md#tecno-hi-os)**.  . 

Once developer options are enabled, follow these steps to generate a bugreport (see Image 8):

1. Open **Settings**
2. Navigate to the menu **System**
3. Go to **Developer Options**
4. Select **Bug report**
5. Choose **Full Report**
6. Tap “**Report”**
7. When the bugreport is complete, a notification indicating "**Bug report captured**" will appear. Tap the notification to **open the sharing settings**.   
8. You will see a warning message informing about sensitive data. Click **Ok**  
9. Select the preferred mechanism and **share the bugreport**  

![Pasos para generar un reporte de errores en un dispositivo Tecno Spark Go con Hi OS utilizando Android 13](../../../assets/05-how-to/bug-report-tecno-spark-go-2023.gif"image 9"){: style="height:480x;width:216px"}
/// caption
**image 8**.  Steps to generate a bug report on a Tecno Spark Go with Hi OS running Android 13.
///

### Xiaomi (Hyper OS)

To generate a bugreport you **need access to developer options**. If this menu has not yet been enabled, follow these [steps to enable developer options on a Xiaomi device](../02-how-to-enable-developer-options/#xiaomi-hyper-os). 

Once developer options are enabled, follow these steps to generate a bugreport (see Image 9):

1. Open **Settings**
2. Navigate to the menu **About phone**
3. Go to **Detailed info and specs**
4. Find the information corresponding to **CPU and tap 5 times report**
5. A notification pop-up will appear warning about personal data in the bugreport. Click **Agree**
6. Tap “**Report”**
7. When the bugreport is complete, a notification indicating "**Bug report captured**" will appear. Tap the notification to **open the file explorer**.   
8. Locate the bugreport that has been just generated, and clikc to open the **Sharing settings**. 
9. Select the preferred mechanism and **share the bugreport**  


![Pasos para generar un reporte de errores en un dispositivo Xiaomi 13T.](../../../assets/05-how-to/bug-report-xiaomi-13t.gif "image 10"){: style="height:480x;width:216px"}
/// caption
**image 9**.  Steps to generate a bug report on a Xiaomi 13T.
///


## Steps to generate a bugreport via the ADB console

In addition to the graphical method, it is possible to generate a bugreport via the ADB console. Remember to [enable USB debugging](../03-how-to-enable-adb/) before following these steps.


### Generate the bugreport

If you only have **one device connected**, you can obtain a bugreport using the following command:

```
$ adb bugreport
```


By default, the report is **saved in the local directory**. To specify a path you can add the parameter at the end of the command as follows:

```
$ adb bugreport E:\Reports\MyBugReportsPath

```

!!! warning "Multiple Devices"

    If multiple devices are connected, **specify the device with the -s option**. First, list connected devices using `adb devices` to obtain the device identifier and **generate the bugreport as follows**: 

    ```
    $ adb devices
    List of devices attached
    emulator-5554      device
    8XV7N15C31003476 device

    $ adb -s 8XV7N15C31003476 bugreport

    ```

### Extract the bugreport

In order to extract the bugreport, you have to first **identify which bugreport to extract**. To do this, you can use the command `adb shell ls /bugreports/` to see the stored reports on the default location `/bugreports/.` 

```
$ adb shell ls /bugreports/
bugreport-foo-bar.xxx.YYYY-MM-DD-HH-MM-SS-dumpstate_log-yyy.txt
bugreport-foo-bar.xxx.YYYY-MM-DD-HH-MM-SS.zip
dumpstate-stats.txt
```

Once you identify the bugreport to extract, you can **copy to the local computer using the following command**. 


```
$ adb pull /bugreports/bugreport-foo-bar.xxx.YYYY-MM-DD-HH-MM-SS.zip
```


## Conclusión

A **bugreport** is an error report generated by the Android operating system  that contains diagnostic information designed **primarily for debugging application errors**. However, **many of the logs and behaviors included are also useful for forensic analysis**. Extracting a bugreport is one of the first steps in an investigation cycle and is a frequent way to begin the triage process on Android devices.

Due to the **diversity of manufacturers and Android versions**, this guide presents a list of step-by-step instructions to generate a bugreport, to facilitate and promote consent-based forensic analysis in benefit of civil society. Always ensure you discuss and obtain [informed consent](../../how-tos/01-how-to-obtain-informed-consent/) before extracting forensic information.

If you have access to a **graphical interface not captured in this resource** and would like to **contribute** the necessary screenshots to add this resource, you can contact us through an [issue](../../community/how-to-contribute/index.md#reporting-issues) or, if you are comfortable with markdown, submit a [pull request](../../community/how-to-contribute/index.md#integrating-new-content-through-pull-requests).

## Comments

Do you have any **comment or suggestion** about this resource? You can use the **comment function provided below** to leave your ideas, corrections or thoughts. Please make sure to follow our [code of conduct](../../community/code-of-conduct/) when leaving your comment. If you prefer, you can also participate in the discussion directly in the [github repository](https://github.com/Socialtic/forensics/discussions). 
