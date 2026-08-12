---
title: How to enable developer options on an Android device?
summary: How to enable developer options on an Android device?
keywords: triage, android, developer options
lang: en
tags: [how-to, intro]
last_updated: 2025-08-14
some_url:
created: 2025-08-14
comments: true
author:
    name: Daniel
    url: https://socialtic.org/quienes-somos/
    description: SocialTIC

---


# How to enable developer options on an Android device?

This resource falls under the **[how-to guides](../)** category and shows the steps to enable the _Developer Options_ menu on different Android devices, as well as a brief explanation of **what developer options are** and **why they are useful in digital forensics**. This is introductory material, complementary to other resources such as the explainer on [log-based forensics for Android devices](), and is part of the steps to follow for an initial triage.

**We appreciate the collaboration of [RSF Security Lab](https://rsf.org/en/digital-security-lab)**, who provided us with a set of guides and screenshots that enabled the development of this resource. 


## What are developer options and why they are helpful?

[Developer options](https://developer.android.com/studio/debug/dev-options) refer to a hidden menu in the Android operating system that **grants access to additional functions**, primarily intended to support [debugging](https://en.wikipedia.org/wiki/Debugging) during the development of new applications. Embeded in the developer options, there are also advanced settings such as preferences of graphics drivers, network configurations and even experimental features being tested or developed. 

From a digital forensics perspective, particularly when conducting [log-based investigations](../../explainers/03-explainer-log-forensics-android/) using tools such as [MVT](../../references/00-glossary/index.md#mvt) and [AndroidQF](../../references/00-glossary/index.md#androidqf), developer options allow us to **enable key functions like USB debugging, the ADB console, or the generation of bug reports**. For this reason, **enabling the developer options menu is often the first step** in the acquisition process.


## Why are there different ways to enable them?

The Android operating system is based on the [Android Open Source Project](https://source.android.com/) (AOSP). However, most manufacturers use a proprietary version from Google, on **top of which they add additional, mostly proprietary, customization layers**. There are also **alternatives such as LineageOS, GrapheneOS, and CalyxOS,** which are entirely based on open-source principles and aim to move away from proprietary ecosystems.

The result of these additional developments on the base project is a **wide variety of graphical interfaces** for the operating system. Some examples include:

* [Pixel UI](https://en.wikipedia.org/wiki/Google_Pixel): User interface developed by **Google** for Pixel devices. Similar to the base Android version but includes additional [proprietary customizations from Google](https://www.howtogeek.com/google-pixel-devices-stock-android/).
* [One UI](https://en.wikipedia.org/wiki/One_UI): User interface developed by **Samsung** for smart devices, including Android mobile devices since 2017. Versions exist for phones, tablets, smartwatches, and computers.
* [HyperOS](https://en.wikipedia.org/wiki/Xiaomi_HyperOS): User interface developed by **Xiaomi**, launched in 2023, replacing the previous [MIUI](https://en.wikipedia.org/wiki/MIUI)
* [ColorOS](https://en.wikipedia.org/wiki/ColorOS): Mobile operating system and user interface created by **Oppo Electronics**  
* [Realme UI](https://en.wikipedia.org/wiki/Realme): User interface developed by **Realme**, a subsidiary of [Oppo Electronics](https://en.wikipedia.org/wiki/Oppo), which also owns the OnePlus brand.
* [Oxygen OS](https://en.wikipedia.org/wiki/OxygenOS): Operating system developed by **OnePlus** exclusively for its smartphones. 
* [Harmony OS](https://en.wikipedia.org/wiki/HarmonyOS): 	Operating system developed by **Huawei**. While sometimes presented as an entirely separate operating system, it is still based on Android and its prior customization layer, [EMUI](https://en.wikipedia.org/wiki/EMUI).  
* [Hello UI](https://beebom.com/motorola-hello-ui-review/): Graphic interface developed by **Motorola**, part of **Lenovo**. [This video](https://www.google.com/url?q=https://www.youtube.com/watch?v%3Di3ZU9-TGJlE&sa=D&source=docs&ust=1753486266796661&usg=AOvVaw14C09MkoaBDTU4pbef9Aqq) shows relevant aspects of the graphic interface. 
* [Xperia UI](https://en.wikipedia.org/wiki/Sony_Xperia): User interface developed by **Sony**.   
* [Magic OS](https://en.wikipedia.org/wiki/Honor_\(brand\)#MagicOS): Operating system developed by **Honor**, previously a subsidiary of Huawei.


## Step-by-step instructions

The following section shows the steps to **enable the developer options menu on different devices**, along with screenshots of the relevant menus for each interface.

### Google (Pixel OS) 

To enable the developer options in **Pixel devices** follow these steps, shown also on **image 1**. 

1. Open the device **Settings** ⚙️  
2. Navigate to the last option **About phone** 📱  
3. Navigate to the bottom and locate the **Build Number** 🔢   
4. **Tap 7 times** the  build number, until you see a confirmation message  👆

![Steps to enable developer options on a Google Pixel running Android 13.](../../../assets/02-how-to/enable-dev-options-Google.gif "image 1")
/// caption
**Image 1**. Steps to enable developer options on a Google Pixel running Android 13.
///

From now on, the developer options will appear as an additional menu under **System**, and **will remain enabled** until they are manually disabled from the developer options menu. 

### Honor (Magic OS) 

To enable the developer options in **Honor devices** follow these steps, shown also on **image 2**. 


1. Open the device **Settings** ⚙️  
2. Navigate to the last option **About phone** 📱  
3. Locate the **Build Number** 🔢   
4. **Tap 7 times** the  build number, until you see a confirmation message  👆

From now on, the developer options will appear as an additional menu under **System & Updates**, and **will remain enabled** until they are manually disabled from the developer options menu. 

![Steps to enable developer options on a Honor Magic Lite running Magic OS 7.1 and Android 13.](../../../assets/02-how-to/enable-dev-options-Honor.gif "image 2")
/// caption
**Image 2**. Steps to enable developer options on a Honor Magic Lite running Magic OS 7.1 and Android 13.
///

### Motorola (Hello UI)

To enable the developer options in **Motorola devices** follow these steps, shown also on **image 3**. 

1. Open the device **Settings** ⚙️  
2. Navigate to the last option **About phone** 📱  
3. Navigate to the bottom and locate the **Build Number** 🔢   
4. **Tap 7 times** the  build number, until you see a confirmation message  👆

From now on, the developer options will appear as an additional menu under **System**, and **will remain enabled** until they are manually disabled from the developer options menu. 

![Steps to enable developer options on a Motorola Edge Neo 40 running Hi OS and Android 13](../../../assets/02-how-to/enable-dev-options-Motorola.gif "image 3")
/// caption
**Image 3**. Steps to enable developer options on a Motorola Edge Neo 40 running Hi OS and Android 13.
///


### Nokia  

To enable the developer options in **Nokia devices** follow these steps, shown also on **image 4**. 

1. Open the device **Settings** ⚙️  
2. Navigate to the last option **About phone** 📱  
3. Navigate to the bottom and locate the **Build Number** 🔢   
4. **Tap 7 times** the  build number, until you see a confirmation message  👆

From now on, the developer options will appear as an additional menu under **System**, and **will remain enabled** until they are manually disabled from the developer options menu. 

![Steps to enable developer options on a Nokia G42 5G running Android 13](../../../assets/02-how-to/enable-dev-options-Nokia.gif "image 4")
/// caption
**Image 4**.  Steps to enable developer options on a Nokia G42 5G running Android 13.
///

### Oppo Reno 10 (Color OS)

To enable the developer options in **OPPO devices** follow these steps, shown also on **image 5**. 

1. Open the device **Settings** ⚙️  
2. Navigate to the last option **About phone** 📱
3. Open the menu **Version** 📝
4. Navigate to the bottom and locate the **build number** 🔢   
5. **Tap 7 times** the  version number, until you see a confirmation message  👆

From now on, the developer options will appear as an additional menu under **Additional Settings**, and **will remain enabled** until they are manually disabled from the developer options menu. 

![Steps to enable developer options on a Oppo device](../../../assets/02-how-to/enable-dev-options-oppo.gif "image 5"){: style="height:480x;width:216px"}
/// caption
**Image 5**. Steps to enable developer options on a Oppo device.
///


### Realme (Realme UI)

To enable the developer options in **Realme devices** follow these steps, shown also on **image 6**. 

1. Open the device **Settings** ⚙️  
2. Navigate to the last option **About phone** 📱
3. Open the menu **Version** 📝
4. Navigate to the bottom and locate the **build number** 🔢   
5. **Tap 7 times** the  version number, until you see a confirmation message  👆

From now on, the developer options will appear as an additional menu under **Additional Settings**, and **will remain enabled** until they are manually disabled from the developer options menu. 

![Steps to enable developer options on a  Realme GT2 Pro with RealMe UI 4.0 and Android 13](../../../assets/02-how-to/enable-dev-options-Realme.gif "image 6")
/// caption
**Image 6**. Steps to enable developer options on a Realme GT2 Pro with RealMe UI 4.0 and Android 13
///

### Samsung (One UI)

To enable the developer options in **Samsung devices** follow these steps, shown also on **image 7**. 

1. Open the device **Settings** ⚙️  
2. Navigate to the last option **About phone** 📱
3. Open the menu **Software Information** 📝
4. Locate the **build number** 🔢   
5. **Tap 7 times** the  version number, until you see a confirmation message  👆


![Steps to enable developer options on a Samsung Galaxy A54 with One UI and Android 13](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExdnB4bTJ0dWpnaWVsY2s0aWVnYTZyejN3a3N1bnhwZnV2NW10cGN2eSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ctCvv5Is6UZ6CEhQ4D/giphy.gif "image 7")
/// caption
**Image 7**. Steps to enable developer options on a Samsung Galaxy A54 with One UI and Android 13
///

### Sony (Xperia UI)

To enable the developer options in **Sony devices** follow these steps, shown also on **image 8**. 

1. Open the device **Settings** ⚙️  
2. Navigate to the last option **About phone** 📱  
3. Navigate to the bottom and locate the **Build Number** 🔢   
4. **Tap 7 times** the  build number, until you see a confirmation message  👆

From now on, the developer options will appear as an additional menu under **System**, and **will remain enabled** until they are manually disabled from the developer options menu. 

![Steps to enable developer options on a Sony Xperia 10V with Xperia UI 4.0 and Android 14](../../../assets/02-how-to/enable-dev-options-Sony.gif "image 8")
/// caption
**Image 8**.  Steps to enable developer options on a Sony Xperia 10V with Xperia UI 4.0 and Android 14.
///


### Tecno (Hi OS)

To enable the developer options in **Tecno Spark devices** follow these steps, shown also on **image 9**. 

1. Open the device **Settings** ⚙️  
2. Navigate to the last option **My phone** 📱  
3. Locate the **Build Number** 🔢   
4. **Tap 7 times** the  build number, until you see a confirmation message  👆

![Steps to enable developer options on a Tecno Spark Go with Hi OS and Android 13.](../../../assets/02-how-to/enable-dev-options-Tecno.gif "image 9")
/// caption
**Image 9**.  Steps to enable developer options on a Tecno Spark Go with Hi OS and Android 13.
///

### Xiaomi (Hyper OS)

To enable the developer options in **Xiaomi devices** follow these steps, shown also on **image 10**. 

1. Abre el menú de **Ajustes** ⚙️  
2. Ingresa a la opción de **Acerca del teléfono** 📱  
3. Ubica la información sobre el **Versión de Sistema Operativo** 🔢   
4. Presiona **7 veces** sobre el número de compilación, hasta que veas un mensaje de confirmación. 👆

![Steps to enable developer options on a Xiamoi device](../../../assets/02-how-to/enable-dev-options-Xiaomi.gif "image 10")
/// caption
**image 10**.  Steps to enable developer options on a Xiamoi device.
///

Las opciones de desarrollador aparecerán como un nuevo submenú dentro del apartado de **Opciones avanzadas,** y se **mantendrán habilitadas** hasta que se deshabiliten (desde el menú de opciones de desarrollador). 

## Conclusion

The graphical interface of Android devices varies between manufacturers that use the [Android Open Source Project (AOSP)](https://source.android.com/?hl=es-419) as a base. Each manufacturer develops its own customization layer, with different levels of modification, resulting in interfaces with different appearances, menus, and options.

The developer options menu is a **hidden menu that can be enabled through a simple procedure in the graphical interface** and is necessary to modify key settings **required during a forensic extraction **process, such as the ADB console or generating a bug report. This resource compiles screenshots from different manufacturers and interfaces to make it easier for civil society analysts to enable developer options.

If you have access to a **graphical interface not shown in this list** and would like to **contribute** a screenshot to this resource, you can contact us through an [issue](../../community/how-to-contribute/index.md#reporting-issues) or, if you are comfortable with markdown, submit a [pull request](../../community/how-to-contribute/index.md#integrating-new-content-through-pull-requests).


## Comments

Do you have any **comment or suggestion** about this resource? You can use the **comment function provided below** to leave your ideas, corrections or thoughts. Please make sure to follow our [code of conduct](../../community/code-of-conduct/) when leaving your comment. If you prefer, you can also participate in the discussion directly in the [github repository](https://github.com/Socialtic/forensics/discussions). 
