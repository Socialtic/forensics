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
auto-translate: true

---

# Tutorial: Uso de MVT para el triaje técnico de dispositivos Android

## Introducción

Este documento forma **parte de un repositorio de documentación técnica** que tiene como objetivo establecer una base de conocimientos probados, flexibles y accesibles para **impulsar el análisis forense consentido en beneficio de la sociedad civil**. Para organizar los contenidos, se utiliza el [marco de referencia de documentación técnica Diataxis](../../references/00-glossary/index.md#diataxis).

Este recurso es un [tutorial](https://diataxis.fr/tutorials/) que busca facilitar el aprendizaje de los conceptos y habilidades necesarias para realizar un triaje técnico forense con la herramienta [Mobile Verification Toolkit](https://github.com/mvt-project/mvt). Esta herramienta forense de código abierto, desarrollada por el [Security Lab de Amnistía Internacional](https://securitylab.amnesty.org/), permite **analizar artefactos forenses de dispositivos Android e iOS en busca de señales de compromiso**.

En este contexto, entendemos como triaje técnico la evaluación, con consentimiento de la persona dueña, de artefactos extraídos de un dispositivo móvil para **determinar si existen indicios, indicadores o comportamientos que coincidan con vectores de ataque conocidos**, y que por lo tanto justifiquen un análisis forense de mayor profundidad. Por lo tanto, el resultado del triaje técnico no es una confirmación ni un descarte de una posible intrusión, sino una decisión fundamentada sobre cómo proceder con un caso.

La MVT procesa la información que ya fue extraída previamente, por ejemplo, utilizando la herramienta con AndroidQF. No accede al dispositivo directamente ni realiza la extracción de datos por sí misma, sino que agrupa y organiza la información, y la compara contra un conjunto de heurísticas de comportamiento sospechoso, e indicadores de compromiso (IOCs), por ejemplo señales conocidas de spyware como [Pegasus](https://securitylab.amnesty.org/latest/2026/07/inside-pegasus-the-evolution-of-the-worlds-most-notorious-spyware/) o [Predator](https://securitylab.amnesty.org/latest/2025/12/intellexa-leaks-predator-spyware-operations-exposed/), o familias de stalkerware.

Al finalizar este tutorial, **sabrás cómo instalar la MVT, cómo ejecutar un triaje sobre una extracción de AndroidQF y cómo interpretar metódicamente sus resultados a través de un ejemplo guiado mediante un caso hipotético**, que contempla el proceso completo de triaje: desde la entrevista de triaje hasta la construcción de una línea de tiempo de hallazgos.

La versión original de este documento fue elaborada en idioma Español por el equipo de SocialTIC. **Agradecemos las revisiones y sugerencias** del equipo de 0xCHE. Cualquier error o omisión es responsabilidad de los autores.

Reconocemos el **esfuerzo y liderazgo del Laboratorio de Seguridad de Amnistía Internacional en el desarrollo de la herramienta MVT**, así como el fortalecimiento de la comunidad forense consentida alrededor del mundo a través de su programa [Digital Forensics Fellowship](https://securitylab.amnesty.org/digital-forensics-fellowship/). Este material busca ser compatible y complementarios con estos esfuerzos tecnológicos y metodológicos.

Este documento se complementa con otros recursos de este repositorio, incluyendo:

* [Explainer: Introducción al triaje técnico de dispositivos Android](../../explainers/04-explainer-introduction-android-triage/index.md), que cubre aspectos conceptuales sobre el sistema operativo Android y cómo puede ser vulnerado.
* [Explainer: Explorando la herramienta MVT para el triaje técnico de dispositivos Android](../../explainers/05-explainer-mvt-android-triage/index.md), que contiene información sobre el funcionamiento de MVT y los módulos para Android.
* [How-to: Triaje técnico de dispositivos Android utilizando MVT](../../how-tos/how-tos/06-how-to-triage-android-mvt/), con los comandos y pasos para realizar un triaje con MVT de forma directa.
* Guías para la extracción forense de artefactos, incluyendo [la guía how-to para extracción de un bugreport](../../how-tos/05-how-to-extract-bugreport/index.md) y [la guía how-to para la extracción con AndroidQF](../../how-tos/04-how-to-extract-with-androidqf/index.md).
* Materiales de referencia con información sobre las salidas de la MVT:
  * [Diccionario de archivos de salida del análisis de bugreport con MVT](../../references/02-reference-mvt-bugreport-dictionary/index.md)
  * [Diccionario de archivos de salida del análisis de AndroidQF con MVT](../../references/03-reference-mvt-androidqf-dictionary/index.md)

## Requerimientos para seguir este tutorial

Para seguir este tutorial, es necesario que consideres los siguientes requerimientos:

* **Computadora**: Necesitas un equipo de cómputo, como una laptop o un equipo de escritorio. De preferencia, el equipo deberá tener un sistema operativo Linux o MacOS, pues las herramientas a instalar tienen una mayor compatibilidad con estos sistemas operativos. En caso de contar con un sistema operativo Windows, se puede optar por crear una [Máquina Virtual Linux](https://ubuntu.com/tutorials/how-to-run-ubuntu-desktop-on-a-virtual-machine-using-virtualbox#1-overview) o instalar [Windows Subsystem For Linux](https://learn.microsoft.com/es-es/windows/wsl/install).
* **Descargar la muestra forense a analizar**: Para seguir este tutorial necesitas una muestra forense para analizar con MVT.
  * Descarga la muestra de prueba para este ejercicio desde [este enlace](https://drive.google.com/file/d/1OpTwa5Bm5j34UaEY7j4hzI6D5OnwMr4E/view?usp=drive_link).
  * Si deseas analizar una muestra diferente, te recomendamos primero completar este tutorial y el [Tutorial Explorando AndroidQF para la extracción forense en Android](../01-tutorial-learning-androidqf/index.md) para familiarizarte con las herramientas, y posteriormente puedes utilizar las guías how-to para guiar tu proceso de extracción y triaje.
* **Instalación del software git:** Necesitas [instalar git en tu computadora](https://github.com/git-guides/install-git), ya que la instalación de la herramienta se hace a través del repositorio oficial.
* **Instalación de herramientas:** En [la sección de instalación](#instalacion-de-la-mvt) de este tutorial, se detallan los pasos a seguir para la instalación de MVT.
* **Conocimientos previos:** Este tutorial asume que tienes familiaridad básica con la línea de comandos (navegar entre carpetas, ejecutar comandos simples) y con conceptos generales de triaje forense, como la importancia de una entrevista inicial y el manejo responsable de datos sensibles. Antes de iniciar, te recomendamos revisar el [material explicativo sobre triaje técnico en dispositivos Android](../../explainers//04-explainer-introduction-android-triage/) y el [material explicativo sobre triaje técnico usando MVT](../../explainers/05-explainer-mvt-android-triage/index.md).

**A continuación se presenta un contexto de incidente ficticio y las instrucciones para realizar el proceso de triaje paso a paso** acompañados de explicaciones concisas de interpretación que ayuda a los analistas a llegar a la conclusión del triaje.

## Contexto del caso

Para este tutorial, **imagina que eres un analista en forense digital que trabaja con actores de cambio social como periodistas, activistas, defensores de derechos y miembros de la sociedad civil**. Recibiste por correo electrónico una solicitud de apoyo de un colega de confianza para el análisis de un dispositivo móvil (smartphone Android) de una persona colaboradora de un colectivo conocido. Este colega te ayuda a verificar la identidad del colaborador, te pone en contexto de la situación y te menciona que realizó una entrevista inicial y una extracción de dicho dispositivo. A continuación te detalla el incidente y la información disponible.

### Incidente

La extracción corresponde al dispositivo de una persona defensora de derechos humanos, a quien se le retuvo su teléfono durante un periodo de custodia. Se sospecha que durante ese periodo, el actor de amenazas involucrado contó con la capacidad técnica para ejecutar un acceso físico no autorizado al dispositivo.

La **siguiente información se obtuvo a través de la entrevista inicial:**

* El 26 de agosto de 2025, alrededor de las 14:30 GMT-6, la persona fue detenida y entregó su teléfono desbloqueado, por lo que este quedó en posesión del actor.
* El dispositivo permaneció fuera de su control hasta aproximadamente las 11:00 del 27 de agosto de 2025, es decir aproximadamente 20 horas.
* Al recibir de vuelta su dispositivo, este estaba completamente apagado y sin batería.
* En los diez días posteriores, la persona reportó comportamiento anómalo, la batería se consumía rápidamente, notó que había aplicaciones que se congelaban con frecuencia y notó indicadores de privacidad de cámara y micrófono encendiéndose sin que la persona abriera ninguna app.
* Días después, personas ajenas a la situación le expresaron directamente que conocían el contenido de conversaciones privadas suyas, lo cual motivó al colaborador del colectivo a buscar ayuda técnica.

!!! note "Nota"
    Esta narrativa se documenta únicamente para dar contexto al análisis técnico. El objetivo de la entrevista de triaje no es confirmar ni descartar hipótesis, **sino identificar eventos, fechas y comportamientos que orienten los siguientes pasos de la investigación.**

## Formulación de hipótesis

Antes de revisar cualquier resultado de la MVT, es indispensable **tener claro qué buscamos probar con el análisis forense**. En este caso, las hipótesis de trabajo son:

1. Durante el periodo en que el dispositivo estuvo fuera del control de la persona, alguien con acceso físico realizó alguna acción sobre el dispositivo.
2. Existe una correlación temporal entre esa posible acción y el comportamiento anómalo reportado por la persona en los días posteriores.

## Configurar la carpeta de trabajo

Debes **crear una carpeta de trabajo para almacenar una copia de la extracción recolectada,** considerando un nombre estratégico para dicha carpeta, que puede contener, por ejemplo una combinación de la fecha con un identificador de caso o dispositivo sin datos que permitan identificar a la persona.

Antes de ejecutar cualquier comando, seguimos las [prácticas de manejo de datos](../../explainers/05-explainer-mvt-android-triage/index.md#recomendaciones-para-el-manejo-de-la-informacion-sensible) que se mencionan en el explainer de exploración de MVT para triajes de Android. Aunque una extracción de AndroidQF y un bugreport no contienen información sensible de una persona usuaria, es decir no incluyen fotografías o archivos personales, deben **tratarse con el mismo cuidado y siempre respetando el consentimiento otorgado por la persona solicitante y cualquier acuerdo de retención de datos** que se haya establecido.

En este caso, vamos a crear la carpeta de trabajo *tutorial-triaje-con-mvt* y vamos a acceder a ella utilizando los siguientes comandos:

```sh
mkdir tutorial-triaje-con-mvt
cd tutorial-triaje-con-mvt
```

Posteriormente, crea la carpeta del caso simulado, refiriendo el número serial del dispositivo ZY323X4MZK, utilizando el siguiente comando.

```sh
mkdir "$(date +"%Y-%m-%d")"-android-ZY323X4MZK
cd "$(date +"%Y-%m-%d")"-android-ZY323X4MZK
```

Copia el sample de extracción a la carpeta del caso simulado utilizando el siguiente comando.

!!! note "Nota"

    El siguiente comando mueve el archivo de muestra descargado desde la carpeta de descargas hasta la carpeta de trabajo. Es posible que la ruta exacta cambie en tu caso particular, dependiendo de dónde se almacena el archivo y el idioma del sistema.

```sh
mv ~/Descargas/android-mvt-tutorial-sample.zip .
```

Descomprime la extracción en el directorio de trabajo utilizando el siguiente comando.

```sh
unzip android-mvt-tutorial-sample.zip
```

## Proceso de Triaje con la MVT

A continuación se detallan los pasos para realizar el triaje con MVT. Para ello, lo primero que necesitas es realizar la [instalación de la MVT](#instalacion-de-la-mvt) en tu computadora (ver requisitos del equipo) o [actualiza la MVT](#actualizacion-de-la-mvt) si ya la tienes instalada.

### Instalación de la MVT

MVT puede ser instalada como herramienta desde el gestor de paquetes estándar de python a través de su forma aislada (pipx).

Los pasos para instalar MVT son los siguientes:

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

!!! warning "Nota"

    Actualmente MVT no tiene un proceso de ejecución formal en Windows. La herramienta puede usarse a través del Windows Subsystem For Linux, sin embargo, no se garantiza su correcto funcionamiento y este tutorial no incluye los pasos de instalación para este caso.

### Actualización de la MVT

Para asegurarte que tienes las últimas integraciones de la herramienta cambia al directorio del repositorio clonado (por ejemplo, `cd mvt`) y ejecuta los siguientes comandos:

```sh
git pull
pipx uninstall mvt
pipx install --force .
```

Regresa al directorio de trabajo donde tenemos la muestra de trabajo y una vez que te asegures tener la última versión de la herramienta y previo a ejecuciones, **descarga los indicadores de compromiso más recientes utilizando el siguiente comando:**

!!! note "Nota"

    Si estás instalando MVT por primera vez, es posible que tengas que cerrar y volver a abrir la terminal para que los comandos de MVT estén disponibles.

```sh
mvt-android download-iocs
```

### Ejecución de MVT sobre la muestra de prueba

Una vez instalada la herramienta, puedes ejecutar el comando correspondiente para analizar una extracción AndroidQF:

```sh
mvt-android check-androidqf ./f1b10850-c902-4e67-885a-6ae9b936d76d -o "$(date +"%Y-%m-%d")"-out-androidqf
```

Durante la ejecución, se solicitará escribir la contraseña del archivo `backup.ab`. La **extracción de ejemplo utiliza la contraseña “sd”**, por lo que deberás introducir estos dos caracteres para continuar:

```sh
Enter backup password:

Introducir "sd" como contraseña cuando se solicite

```

Sabrás que el proceso de análisis con la MVT terminó cuando veas el resumen de las alertas, similar al que se muestra a continuación:

!!! note "Nota"

    Esta salida corresponde al resultado de correr el análisis en la muestra de prueba con la versión 2026.10.5 de MVT.

    La misma puede contener diferencias debido a cambios en la herramienta que hacen que nuevos comportamientos sean detectados como sospechosos. Por la forma en que se diseñó este material, estos cambios no deberían afectar tu capacidad de seguir el ejercicio.

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

**Al usar el argumento \-o, la MVT crea carpetas y archivos de salida útiles para el triaje y el análisis forense**. Si quieres entender qué contiene cada uno, puedes apoyarte en [los diccionarios de referencia de la MVT que se encuentran disponibles en este repositorio](../../references/index.md). El siguiente bloque de código lista los contenidos de la carpeta de trabajo utilizando el comando `ls` luego de completar la ejecución de MVT.

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

### Revisión de salidas

Lo primero que veremos en pantalla es un breve resumen de la ejecución, además de las alertas en sus diferentes niveles. En este caso, notarás que ninguna alerta alcanzó el nivel **CRITICAL**, es decir, ningún dato del dispositivo coincidió con los indicadores de compromiso (IOCs) de amenazas conocidas cargados por la MVT.

Identificamos las siguientes alertas **MEDIUM**:

Se identifica el paquete de Facebook ***“com.facebook.katana”*** como un paquete que no es de sistema, instalado por adb u otro medio. Aunque probablemente se trate de una app preinstalada por el vendedor, es necesario tomar nota para verificar si se relaciona con la información buscada en el triaje.

```sh
MEDIUM ALERT   [mvt.android.modules.androidqf.aqf_packages] Found a non-system package installed via adb or another method: "com.facebook.katana"
```

Se identifica que el dispositivo no ha recibido actualizaciones de seguridad por más de seis meses, esto indica que el teléfono ya no tiene soporte de actualizaciones o el usuario no ha actualizado el dispositivo.

```sh
MEDIUM ALERT   [mvt.android.modules.androidqf.aqf_getprop] This phone has not received security updates for more than six months (last update: 2021-02-01).
```

Se identificó que Google Play Protect está deshabilitado. Esto es un indicador importante sobre instalación de aplicaciones externas a Google Play que pueden ser **no confiables**. Es importante tenerlo en consideración a lo largo del triaje.

```sh
MEDIUM ALERT   [mvt.android.modules.androidqf.aqf_settings] Found suspicious "global" setting "upload_apk_enable = 0" (disabled Google Play Protect)
```

Se identificó que se desinstaló el paquete ***“com.republicwireless.tel”***

```sh
MEDIUM ALERT   [mvt.android.modules.bugreport.dumpsys_battery_daily] Detected uninstall of package com.republicwireless.tel (vers 0)
```

Se identificó que no se pudo encontrar ningún tombstone, es decir, ningún crash del dispositivo fue identificado por la MVT.

```sh
ERROR          [mvt.android.modules.bugreport.tombstones] Unable to find any tombstone files. Did you provide a valid bugreport archive?
```

Además de las alertas **MEDIUM**, también hay una alerta de nivel **HIGH,** de la cual tomamos nota:

```sh
HIGH ALERT     [mvt.android.modules.androidqf.aqf_files] Found executable file at suspicious path "/data/local/tmp/.studio/process-tracker"
```

Este hallazgo corresponde a un artefacto típico de Android Studio, por lo que es un buen ejemplo de algo que debe documentarse y contrastarse con la entrevista por ejemplo, preguntando a la persona si suele conectar su teléfono a una computadora con fines de desarrollo antes de asumir que se trata de algo relacionado con el incidente.

Por último, notamos una alerta LOW relacionada con una llave ADB de confianza sin su llave de host correspondiente en la extracción, algo que se debe documentar y que dependiendo del contexto se deberá analizar.

```sh
LOW ALERT      [mvt.android.modules.bugreport.dumpsys_adb_state] Found a trusted ADB host key, but the AndroidQF acquisition does not include its host key:
71:F7:D8:0B:1A:61:48:32:83:E7:21:0C:47:07:FA:F0 (unknown user)
```

#### Revisión del command.log

Al revisar command.log con calma y teniendo en consideración la hipótesis (comprobar si hubo actividad durante la ventana en que el dispositivo estuvo fuera de vista de la persona), dos alertas de nivel MEDIUM llaman la atención:

```sh
MEDIUM ALERT   [mvt.android.modules.bugreport.dumpsys_appops] Package 'com.google.android.apps.nbu.files' had risky permission 'REQUEST_INSTALL_PACKAGES' set to 'Reject' at 2025-08-26 15:43:12.384000
MEDIUM ALERT   [mvt.android.modules.bugreport.dumpsys_appops] Package 'com.google.android.apps.nbu.files' had risky permission 'REQUEST_INSTALL_PACKAGES' set to 'Access' at 2025-08-26 16:25:50.885000
```

Estas líneas muestran que el paquete **com.google.android.apps.nbu.files** (Explorador de Archivos de Google) tuvo un cambio en el permiso ***REQUEST\_INSTALL\_PACKAGES*** (el permiso que le permite a una app instalar otras apps) donde primero fue rechazado a las 15:43 y después otorgado a las 16:25, el mismo día y **dentro de la ventana horaria en la que la persona confirma no tener el dispositivo a la vista.**

Este es el tipo de correlación que buscamos al **conectar la salida técnica con la entrevista de triaje** y la línea de tiempo del caso.

#### Revisión del timeline.csv

Para profundizar en ese hallazgo, **buscamos ese mismo horario dentro de timeline.csv**:

```sh
grep -C 25 "2025-08-26 16:25:50.885000" timeline.csv
```

Dentro de la salida encontramos el evento que nos faltaba para entender qué fue lo que ocurrió en ese momento:

```sh
"2025-08-26 16:25:50","DumpsysPackages","package_install","Install or update of package com.sterminator"
"2025-08-26 16:25:50.885000","DumpsysAppops","Access","com.google.android.apps.nbu.files access to REQUEST_INSTALL_PACKAGES: Access"
"2025-08-26 16:26:08","DumpsysPackages","package_first_install","Install or update of package com.sterminator"
"2025-08-26 16:26:08","DumpsysPackages","package_last_update","Install or update of package com.sterminator"
```

En el mismo instante en el que se otorga el permiso de instalación al Explorador de Archivos, **el timeline registra la instalación de un paquete llamado *“com.sterminator”***, que no reconocemos. Continuando la revisión del timeline unos minutos después, encontramos actividad adicional asociada a ese mismo paquete, acceso al portapapeles, escaneo de redes wifi, y ventanas emergentes tipo toast, entre otras.

#### Revisión de archivos detected

Para la revisión de archivos detected listamos la carpeta de resultados generada por la MVT:

```sh
ls *_detected.json
```

Obtendremos como salida los nombres de los archivos de los módulos que tuvieron coincidencias con patrones que generaron alertas según la MVT, estos deberán ser revisados para entender el contexto de las detecciones:

```sh
aqf_files_detected.json     aqf_packages_detected.json  dumpsys_adb_state_detected.json  dumpsys_battery_daily_detected.json
aqf_get_prop_detected.json  aqf_settings_detected.json  dumpsys_appops_detected.json     dumpsys_get_prop_detected.json
```

Al revisar ***aqf\_packages\_detected.json***, notamos que **com.sterminator** no aparece ahí; el único paquete marcado por la MVT en ese archivo sigue siendo **com.facebook.katana**, detectado únicamente por ser un paquete de terceros instalado fuera de los canales estándar del sistema, sin relación aparente con nuestra hipótesis, además de que se puede observar que su contexto de instalación es ser una aplicación pre instalada por el vendor y que **su certificado es de confianza.**

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

Del mismo modo, ***dumpsys\_appops\_detected.json*** únicamente contiene el cambio de permiso del Explorador de Archivos que ya identificamos, por lo que no contiene los permisos que el propio paquete **com.sterminator** solicitó y utilizó después de instalarse.

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

Este es un punto importante de aprendizaje, pues **los archivos *detected* reflejan únicamente lo que las heurísticas e indicadores de la MVT identificaron automáticamente**. En este caso la MVT **no generó ninguna alerta dirigida específicamente al paquete com.sterminator**, ni sus permisos coincidieron con ningún IOC conocido. El hallazgo relevante lo encontramos mediante la revisión manual del command.log y el timeline.csv, guiada por el contexto de la entrevista. Esto refuerza por qué el triaje no debe limitarse únicamente a revisar las alertas automáticas.

Dado que los archivos detected no aportaron mayor contexto sobre ***com.sterminator***, buscamos ese paquete en el resto de los archivos de resultados ejecutando

```sh
grep -rl "com.sterminator" .
```

Identificamos que los siguientes documentos tienen alguna coincidencia con el paquete sospechoso.

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

Revisando cada uno de estos archivos encontramos lo siguiente:

***aqf\_packages.json*** confirma los metadatos del paquete:

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

El paquete fue instalado desde */data/app/com.sterminator-.../base.apk*, con **"installer": "com.google.android.apps.nbu.files"**, es decir, instalado a través del Explorador de Archivos, no de Google Play Store y con un certificado no confiable **"trusted\_certificate": false**.

***aqf\_settings.json*** muestra que **com.sterminator** aparece dentro de *enabled\_notification\_policy\_access\_packages*, es decir, se le otorgó acceso a las notificaciones y a la política de "no molestar" del sistema.

```sh
"enabled_notification_policy_access_packages": "com.motorola.camera2:com.google.android.apps.wellbeing:com.sterminator:com.motorola.arselfie",
```

***dumpsys\_activities.json*** muestra que el paquete registra actividades bajo el nombre interno **com.terminator** (com.sterminator/com.terminator.StartActivity, com.sterminator/com.terminator.ConfigMain), lo cual sugiere que la aplicación ha estado activa y ejecutando diferentes acciones.

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

***dumpsys\_appops.json*** muestra que la aplicación solicitó y utilizó permisos de ubicación exacta, GPS, cámara, micrófono, portapapeles, ventanas de sistema y escaneo de wifi, poco después de haberse instalado, permisos considerados invasivos y que debe verificarse si fueron otorgados por la persona usuaria.

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

***dumpsys\_battery\_history.json*** confirma múltiples eventos start\_top / end\_top para com.sterminator, es decir, que el proceso pasó a primer plano en distintos momentos tras su instalación.

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

***dumpsys\_receivers.json*** muestra que el paquete registró múltiples receptores (BroadcastReceiver), entre ellos varios componentes estándar de las bibliotecas WorkManager y Firebase (ConstraintProxy, ProfileInstallReceiver, FirebaseMessagingDirectBootReceiver), y también un conjunto de receptores con nombres internos propios de la app.

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

### Resumen de hallazgos iniciales

Con base en la revisión del command.log, el timeline.csv, y la revisión manual de los archivos de resultados, podemos construir la siguiente línea de tiempo:

1. El día 26 de agosto de 2025, 15:43:12 se registra un primer intento fallido (Reject) de otorgar el permiso *REQUEST\_INSTALL\_PACKAGES* a la aplicación Explorador de Archivos de Google.

2. El día 26 de agosto de 2025, 16:25:50 se otorga el permiso *REQUEST\_INSTALL\_PACKAGES* a la misma aplicación y en el mismo instante el sistema registra la instalación del paquete **com.sterminator**. La revisión manual de ***aqf\_packages.json*** confirmó que este paquete fue instalado a través del Explorador de Archivos y que su certificado de firma no es confiable

3. El día 26 de agosto de 2025, 16:26:08 se confirma el primer registro de instalación del paquete.

4. Poco después de la instalación se muestra en el registro de ***aqf\_settings.json*** que **com.sterminator** fue agregado a la lista *enabled\_notification\_policy\_access\_packages*, es decir, se le otorgó acceso a las notificaciones y a la política de no molestar del sistema, un permiso que no se concede de forma automática.

5. 26 de agosto de 2025 entre las 16:29 y 16:42 el paquete presentó actividad sostenida en primer plano. La revisión del ***dumpsys\_battery\_history.json*** confirma múltiples ciclos start\_top / end\_top durante este periodo y ***dumpsys\_activities.json*** registra ejecuciones repetidas de dos actividades internas del paquete bajo *com.terminator.StartActivity* y *com.terminator.ConfigMain*, lo que sugiere que la aplicación pudo haber sido configurada o utilizada activamente durante este lapso. En este mismo periodo el ***dumpsys\_appops.json*** muestra que el paquete solicitó y utilizó permisos sensibles como **ubicación exacta, GPS, cámara, micrófono, portapapeles y ventanas de sistema**, permisos que pueden contrastarse con la persona usuaria para verificar si fueron otorgados con su conocimiento.

Adicionalmente, la revisión del ***dumpsys\_receivers.json*** muestra que además de los receptores estándar de las bibliotecas WorkManager y Firebase, el paquete registró un receptor para android.app.action.DEVICE\_ADMIN\_ENABLED, lo que indica que la aplicación **solicita privilegios de administrador de dispositivo,** junto con receptores personalizados para el bloqueo de pantalla e intentos de apagado del dispositivo.

Toda esta actividad, desde la instalación, configuración, solicitud de administrador de dispositivo y uso de permisos sensibles ocurre dentro de la ventana horaria en la que según la entrevista, la persona no tenía el dispositivo en su poder (aproximadamente de las 14:30 del 26 de agosto a las 11:00 del 27 de agosto).

Es importante identificar que la MVT **no generó ninguna alerta automática ni identificó ninguna coincidencia con indicadores de compromiso conocidos para com.sterminator**. Todos estos hallazgos provienen de la revisión manual de los archivos de resultados, guiada por el contexto de la entrevista y la línea de tiempo del caso, no del resumen de alertas por sí solo.

### Pasos de análisis adicionales

Siguiendo este triaje inicial, pudimos confirmar que existe evidencia de la instalación de una aplicación de terceros (**com.sterminator**) a través del Explorador de Archivos durante la ventana temporal en la que el dispositivo estuvo fuera del control de la persona y que dicha aplicación solicitó y utilizó permisos sensibles del sistema poco después de instalarse. La MVT no generó una alerta automática ni una coincidencia con indicadores de compromiso conocidos para este paquete específico.

Como siguientes pasos se puede:

* Hacer preguntas específicas a la persona defensora sobre esta actividad, es decir,  si reconoce el nombre **com.sterminator**, si recuerda haber visto ventanas o notificaciones relacionadas con el Explorador de Archivos o con la instalación de una app en ese periodo, si tiene configurado un patrón o PIN de desbloqueo y si el dispositivo tenía habilitadas las Opciones de Desarrollador o la depuración por USB antes del incidente.

* Analizar la aplicación sospechosa, si el archivo sigue presente en la extracción con AndroidQF, se puede realizar un análisis estático y dinámico, revisar los permisos declarados en su manifiesto, el comportamiento de red que presenta y contrastar sus hashes (md5, sha1, sha256) contra herramientas de detección de amenazas como VirusTotal.

* Brindar contención y recomendaciones iniciales a la persona defensora, como evitar seguir usando el dispositivo hasta concluir el análisis, respaldar por separado la información importante, cambiar las credenciales de las cuentas que pudieran haber sido expuestas (correo, redes sociales).

!!! note "Nota"
    Es importante resaltar que este es un triaje técnico inicial, y no un análisis forense completo. Lo que hemos documentado hasta aquí es evidencia técnica que amerita una investigación más profunda, incluyendo potencialmente ingeniería inversa de la aplicación instalada por ejemplo. No es una conclusión sobre la naturaleza, el propósito o el origen de dicha aplicación.

## Lo que aprendiste

En este tutorial **recorrimos los distintos archivos de salida que genera la MVT**, poniendo especial atención en los que resultan clave al investigar una posible sospecha de riesgo, siendo estos command.log como punto de partida, timeline.csv para correlacionar actividad en el tiempo, alerts.json como resumen consolidado de hallazgos y los archivos con sufijo detected para profundizar en cada alerta específica.

A lo largo del tutorial insistimos que en la práctica resulta fundamental obtener información clave durante la entrevista de triaje, de forma tal que podamos generar hipótesis que sirvan como punto de partida para el triaje técnico, ya que aunque una herramienta forense **no** genere ninguna alerta automática o alguna coincidencia con indicadores de compromiso, es importante considerar que los hallazgos son las principales fuentes de investigación. Fue necesario **conectar una alerta de nivel medio con la ventana de tiempo señalada por la persona entrevistada y revisar manualmente varios archivos de resultados (no solo los *detected*) para construir una línea de tiempo con sentido y llegar a una conclusión de triaje sólida.**

Sin una hipótesis clara de qué se está buscando y por qué, revisar la salida de la MVT se convierte en buscar una aguja en un pajar, pues nos enfrentamos a líneas, paquetes y eventos en el sistema de archivos, sin ningún hilo conductor que te diga dónde poner la atención.

## Conclusión

**La MVT es una herramienta poderosa, pero, como toda herramienta forense, no reemplaza el criterio de una analista.** Sus alertas automatizadas y sus indicadores de compromiso son un punto de partida valioso, especialmente frente a amenazas ya documentadas, pero como vimos, muchos hallazgos relevantes sólo pueden salir a la luz durante una revisión manual que tiene como base el contexto del caso.

El triaje técnico no busca certezas absolutas ni conclusiones precipitadas o definitivas, más bien **se enfoca en identificar evidencia suficiente para decidir si un caso amerita un análisis forense más profundo y, al mismo tiempo, ofrecer recomendaciones de contención oportunas a la persona acompañada.** En nuestro ejemplo guiado, esto significó identificar la instalación de una aplicación con permisos y comportamiento que ameritan mayor investigación, sin necesidad de afirmar de antemano de qué se trataba o quién la instaló, algo que corresponde a etapas posteriores del análisis.

Esperamos que este tutorial te dé una base sólida para comenzar a realizar triajes de dispositivos Android con mayor precisión metodológica.


## Comentarios

¿Tienes **comentarios o sugerencias** sobre este recurso? Puedes utilizar la **función de comentar que se muestra a continuación** para dejarnos tus ideas o apreciaciones. Por favor asegúrate de seguir nuestro [código de conducta](../../community/code-of-conduct/). La función de comentarios enlaza directamente a la sección de [_Discussions_ de Github](https://github.com/Socialtic/forensics/discussions), donde también **puedes participar en las discusiones de forma directa**, si lo prefieres.   
