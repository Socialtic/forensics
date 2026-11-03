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
auto-translate: true

---

# Explainer: Explorando la herramienta MVT para el triaje técnico de dispositivos Android

Este documento forma **parte de un repositorio de documentación técnica** que tiene como objetivo establecer una base de conocimientos probados, flexibles y accesibles para **impulsar el análisis forense consentido en beneficio de la sociedad civil**. Para organizar los contenidos, se utiliza el [marco de referencia de documentación técnica Diataxis](../../references/00-glossary/index.md#diataxis).

Este recurso en particular se enmarca dentro de la categoría de [explainers](https://diataxis.fr/explanation), y busca crear familiaridad con la herramienta MVT y los conceptos necesarios para realizar un triaje forense con la herramienta [Mobile Verification Toolkit](https://github.com/mvt-project/mvt). En este material exploramos los módulos y salidas de la herramienta, así como el modelo mental a seguir al realizar un triaje de dispositivos android con MVT.

El Mobile Verification Toolkit o MVT es una herramienta forense de código abierto, desarrollada por el [Security Lab de Amnistía Internacional](https://securitylab.amnesty.org/), que permite **analizar artefactos forenses de dispositivos Android e iOS en busca de señales de compromiso**.

Reconocemos el esfuerzo y liderazgo del Laboratorio de Seguridad de Amnistía Internacional en el desarrollo de la herramienta MVT, así como el fortalecimiento de la comunidad forense consentida alrededor del mundo a través de su programa [Digital Forensics Fellowship](https://securitylab.amnesty.org/digital-forensics-fellowship/). Este material busca ser compatible y complementarios con estos esfuerzos tecnológicos y metodológicos.

Este documento se complementa con otros recursos de este repositorio, incluyendo:

* [Explainer: Introducción al triaje técnico de dispositivos Android](../04-explainer-introduction-android-triage/index.md), que cubre aspectos conceptuales importantes sobre el sistema operativo Android y cómo puede ser vulnerado.
* [How-to: Triaje técnico de dispositivos Android utilizando MVT](../../how-tos/06-how-to-triage-android-mvt/index.md), con los comandos y pasos para realizar un triaje con MVT de forma directa.
* Guías para la extracción forense de artefactos, incluyendo [la guía how-to para extracción de un bugreport](../../how-tos/05-how-to-extract-bugreport/index.md) y [la guía how-to para la extracción con AndroidQF](../../how-tos/04-how-to-extract-with-androidqf/index.md).
* [El tutorial práctico sobre el uso de MVT para el triaje técnico de dispositivos Android](../../tutorials/02-tutorial-mvt-android-triage/index.md), que utiliza una extracción de ejemplo para comprender mejor el proceso de uso de la MVT.
* Materiales de referencia con información sobre las salidas de la MVT:
  * [Diccionario de archivos de salida del análisis de bugreport con MVT](../../references/02-reference-mvt-bugreport-dictionary/index.md)
  * [Diccionario de archivos de salida del análisis de AndroidQF con MVT](../../references/03-reference-mvt-androidqf-dictionary/index.md)

## Consideraciones importantes antes de realizar un triaje técnico

**Los artefactos forenses pueden contener información sensible**, por lo que es importante discutir, aclarar y acordar con la persona que solicita el análisis la forma en que se manejará su información. Ten en consideración que al ejecutar un triaje con la MVT, la herramienta genera listados de paquetes de un dispositivo, marcas de tiempo o rutas de archivos que pueden reflejar el comportamiento del dispositivo de la persona que solicitó el análisis.

Por lo tanto, recomendamos que antes de recabar información o utilizar herramientas forenses como MVT se cuente con el consentimiento informado de la persona solicitante, y además se tenga la capacidad, medidas y controles necesarios para contener y limitar los [riesgos a los que se enfrentan los laboratorios forenses de la sociedad civil](../02-explainer-risks-threats/index.md).

La [guía how-to: ¿Cómo obtener un consentimiento informado para una investigación forense?](../../how-tos/01-how-to-obtain-informed-consent/index.md) describe qué es el consentimiento informado en el contexto de investigaciones forenses, y presenta un borrador que puede ser adaptado de acuerdo a las necesidades.

### Recomendaciones para el manejo de la información sensible

Es importante tener presente que todos los archivos generados durante un triaje **desde la extracción hasta los resultados de MVT debe tratarse como información sensible**, incluso cuando el uso de MVT no arroje coincidencias con indicadores de compromiso.

Esto implica que se requieren **prácticas adecuadas de manejo de datos**, entre ellas:

* Asegurarse que los dispositivos de cómputo utilizados para el triaje cuentan con **cifrado de disco**.
* **Considerar una capa de cifrado adicional** en las carpetas de trabajo, si los resultados se transportarán entre dispositivos. Puedes utilizar herramientas como contenedores cifrados ([VeraCrypt](https://protege.la/guias-contenido/veracrypt-uso-instalacion-crifrado-de-archivos/) o [Cryptomator](https://protege.la/guias-contenido/guia-cryptomator/) ).
* **Limitar el acceso a las carpetas de resultados** únicamente a las personas que participan directamente en el análisis del caso, siguiendo una [política de *need-to-know*](https://en.wikipedia.org/wiki/Need_to_know).
* **No trabajar sobre la copia original de la información extraída**, para evitar realizar cambios que impacten su integridad. Realizar una copia de trabajo, y utilizar esta copia para el triaje y análisis.
* Documentar el proceso por ejemplo, en un archivo de notas.md, donde **se registren los comandos que se ejecutaron, la fecha, y cualquier observación relevante**. Esto facilita retomar el análisis más adelante o compartirlo con otra persona analista.
* **Eliminar de forma segura las copias temporales o intermedias** que ya no sean necesarias.
* **Evitar imprimir o exportar resultados a canales inseguros** (como correo electrónico sin cifrar o mensajería no cifrada) al compartir hallazgos con otras personas del equipo o con la persona acompañada.
* Definir de antemano **cuánto tiempo se conservará la información** una vez concluido el análisis.
* **Evitar utilizar servicios de almacenamiento en la nube sin cifrado de extremo a extremo** para guardar carpetas de extracción o resultados.

Manejar la información forense en apego a estas y otras buenas prácticas es parte de la **responsabilidad de participar en un proceso forense consentido**. La persona que autorizó el análisis de su dispositivo confía en que los datos resultantes de ese análisis no quedarán expuestos durante el proceso ni después de haber concluido.

### Organización de la información

Antes de ejecutar la herramienta MVT para el triaje técnico, es importante definir una estructura de carpetas clara y consistente en donde se almacenará la información resultante. A continuación presentamos un ejemplo de organización básica y funcional que puede ser adaptado de acuerdo a las necesidades y particularidades específicas de cada organización.

```
analysis/
└── YYYY-MM-DD-operative-system-<case-alias-or-hash>/
    ├── extraction-custody/       # Raw data, not to be touched
    ├── extraction-working/       # Copy of raw data, used for analysis
    ├── YYYY-MM-DD-out-<androidqf/bugreport/intrusion-logs>/ # to store MVT output
    └── notes.md          # Notes and logs from analysis
```

Al organizar los archivos, es importante considerar lo siguiente:

* **Se recomienda utilizar una nomenclatura consistente a través de los casos**, que incluya la fecha del análisis y algún identificador único.
* **Separar los datos de extracción de los resultados generados por MVT:** esto te permite volver a ejecutar el triaje si es necesario, sin perder ni sobrescribir la información de extracción. Si se cuenta con espacio suficiente, es recomendable crear una carpeta de custodia, que contenga la extracción original, y que no se utilice para ninguno de los procesos de análisis.
* **No mezcles archivos de distintos casos en una misma carpeta.** Antes de ejecutar un análisis, es importante crear la estructura de carpetas necesaria para almacenar la información.

## Utilizando MVT para el triaje de dispositivos Android

El Mobile Verification Toolkit o MVT es una herramienta forense de código abierto, desarrollada por el [Security Lab de Amnistía Internacional](https://securitylab.amnesty.org/), que permite **analizar artefactos forenses de dispositivos Android e iOS en busca de señales de compromiso**.

MVT no accede al dispositivo directamente ni realiza la extracción de datos por sí misma, más bien procesa la información que ya fue extraída previamente, por ejemplo, utilizando la herramienta AndroidQF. Al utilizar MVT para procesar una extracción, la herramienta agrupa y organiza la información, y además la compara  contra un conjunto de heurísticas de comportamiento sospechoso, e [indicadores de compromiso (IOCs)](../../references/00-glossary/index.md#indicador-de-compromiso-ioc), como por ejemplo algunas señales conocidas de spyware como [Pegasus](https://securitylab.amnesty.org/latest/2026/07/inside-pegasus-the-evolution-of-the-worlds-most-notorious-spyware/) o [Predator](https://securitylab.amnesty.org/latest/2025/12/intellexa-leaks-predator-spyware-operations-exposed/), o familias de stalkerware.

### Comandos y módulos de MVT para Android

La MVT organiza sus módulos de análisis según el tipo de artefacto forense que procesa. Para dispositivos Android, los siguientes comandos se encuentran a disposición:

* **mvt-android check-androidqf**: permite analizar una extracción realizada con la herramienta androidQF utilizando los [módulos para tal extracción](https://github.com/mvt-project/mvt/tree/main/src/mvt/android/modules/androidqf). Estas extracciones generalmente incluyen también un *bugreport* y, en caso de estar disponibles, también incluye los *intrusion logs.* Por lo tanto, utilizar el módulo de androidqf puede ser suficiente para **realizar un análisis de todos los artefactos disponibles**, ya que MVT detecta estos archivos automáticamente y ejecuta también los [módulos correspondientes a bugreport](https://github.com/mvt-project/mvt/tree/main/src/mvt/android/modules/bugreport) y los [módulos correspondientes a backup](https://github.com/mvt-project/mvt/tree/main/src/mvt/android/modules/backup)
* **mvt-android check-bugreport**: Este módulo permite analizar de forma directa un [reporte de errores o bugreport](../../references/00-glossary/index.md#bugreport). En caso de no contar con una extracción de AndroidQF, y procurar un análisis rápido, se recomienda **utilizar este módulo como un primer paso**. En caso de identificar señales de actividad sospechosa, se recomienda complementar con el análisis completo de una extracción con AndroidQF.
* **mvt-android check-intrusion-logs**: Los *intrusion logs* solo están disponibles en dispositivos con Android 16 o superior y cuando la persona haya activado previamente el Modo de Protección Avanzada con el registro de intrusiones habilitado. En caso de contar con un archivo de registro de intrusiones, es posible realizar el análisis de este archivo específico utilizando este comando y módulo de MVT.

!!! note "Nota"
    A diferencia del bugreport, que siempre será generado durante una extracción con AndroidQF, los [intrusion logs](https://securitylab.amnesty.org/latest/2026/05/android-intrusion-logging-as-a-new-source-of-data-for-consensual-forensic-analysis/) solo estarán presentes en la extracción si el dispositivo cuenta con Android 16 o superior y la persona activó previamente el Modo de Protección Avanzada con el registro de intrusiones habilitado.

#### Módulos

Las siguientes tablas describen cada uno de los módulos disponibles para los diferentes comandos, el enlace a su código fuente y su utilidad en el análisis forense.

!!! note "Nota"
    Este listado corresponde a los módulos disponibles en la rama principal del repositorio oficial de MVT al momento de escribir este material (versión 2026.10.5). Dado que la MVT es una herramienta en desarrollo activo, es posible que se agreguen o modifiquen módulos con el tiempo. Puedes confirmar el listado vigente revisando el [código fuente de MVT](https://github.com/mvt-project/mvt/tree/main/src/mvt/android/modules).

=== "androidqf"

    | Módulo | Archivo fuente | Qué analiza | Utilidad forense |
    | :---: | ----- | ----- | ----- |
    | **AQFPackages** | [aqf\_packages.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/androidqf/aqf_packages.py) | El listado de aplicaciones instaladas (packages.json) | Identifica paquetes relacionados con rooteo, instaladores de tiendas no oficiales |
    | **AQFProcesses** | [aqf\_processes.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/androidqf/aqf_processes.py) | Los procesos en ejecución (ps.txt) | Permite revisar qué procesos estaban activos al momento de la extracción |
    | **AQFGetProp** | [aqf\_getprop.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/androidqf/aqf_getprop.py) | Las propiedades del sistema (getprop.txt) | Aporta contexto técnico del dispositivo (modelo, versión de Android, arquitectura, etc.) |
    | **AQFSettings** | [aqf\_settings.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/androidqf/aqf_settings.py) | Las configuraciones del sistema (settings\_system.txt, settings\_secure.txt, settings\_global.txt) | Permite revisar configuraciones de red, seguridad y accesibilidad del dispositivo |
    | **AQFFiles** | [aqf\_files.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/androidqf/aqf_files.py) | El listado de archivos y metadatos (files.json) | Detecta archivos en rutas sospechosas, como /data/local/tmp/,  |
    | **AQFLogTimestamps** | [aqf\_log\_timestamps.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/androidqf/aqf_log_timestamps.py) | Las marcas de tiempo de los archivos en la carpeta logs/ | Construye una línea de tiempo de creación/modificación de los logs recolectados |
    | **RootBinaries** | [root\_binaries.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/androidqf/root_binaries.py) | El listado de binarios de rooteo (root\_binaries.json) | Detecta rastros de rooteo (su, Magisk, busybox, etc.). |
    | **Mounts** | [mounts.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/androidqf/mounts.py) | La información de puntos de montaje (mounts.json) | Detecta configuraciones de montaje, como /system montado en modo lectura/escritura. |

=== "bugreport"

    | Módulo | Archivo fuente | Sección de dumpsys analizada | Utilidad forense |
    | :---: | ----- | ----- | ----- |
    | **DumpsysAccessibility** | [dumpsys\_accessibility.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/bugreport/dumpsys_accessibility.py) | accessibility | Revisa el uso de servicios de accesibilidad |
    | **DumpsysActivities** | [dumpsys\_activities.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/bugreport/dumpsys_activities.py) | package (Activity Resolver Table) | Extrae las actividades e intent-filters registrados por cada app y los compara contra indicadores de compromiso |
    | **DumpsysAppops** | [dumpsys\_appops.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/bugreport/dumpsys_appops.py) | appops | Muestra el historial de uso de permisos sensibles (cámara, micrófono, ubicación) por aplicación |
    | **DumpsysBatteryDaily** | [dumpsys\_battery\_daily.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/bugreport/dumpsys_battery_daily.py) | batterystats (resumen diario) | Aporta un registro diario de eventos de batería y actividad de procesos |
    | **DumpsysBatteryHistory** | [dumpsys\_battery\_history.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/bugreport/dumpsys_battery_history.py) | batterystats (historial detallado) | Permite construir una línea de tiempo granular de actividad de procesos y consumo energético |
    | **DumpsysDBInfo** | [dumpsys\_dbinfo.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/bugreport/dumpsys_dbinfo.py) | dbinfo | Extrae información sobre bases de datos SQLite abiertas por el sistema y las apps |
    | **DumpsysGetProp** | [dumpsys\_getprop.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/bugreport/dumpsys_getprop.py) | getprop (embebido en el bugreport) | Aporta propiedades del dispositivo obtenidas desde una segunda fuente dentro del mismo bugreport |
    | **DumpsysPackages** | [dumpsys\_packages.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/bugreport/dumpsys_packages.py) | package | Detalla las aplicaciones instaladas y sus metadatos, según lo reportado en el bugreport |
    | **DumpsysPlatformCompat** | [dumpsys\_platform\_compat.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/bugreport/dumpsys_platform_compat.py) | platform\_compat | Registra aplicaciones que fueron desinstaladas |
    | **DumpsysReceivers** | [dumpsys\_receivers.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/bugreport/dumpsys_receivers.py) | package (receptores de intents) | Identifica receptores registrados para interceptar SMS, llamadas entrantes/salientes o cambios de estado telefónico  |
    | **DumpsysADBState** | [dumpsys\_adb\_state.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/bugreport/dumpsys_adb_state.py) | adb | Revisa el estado de la depuración ADB y las llaves autorizadas/confiables |
    | **BugReportTimestamps** | [fs\_timestamps.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/bugreport/fs_timestamps.py) | Listado de sistema de archivos (FS/\*) | Construye una línea de tiempo a partir de las marcas de tiempo del sistema de archivos capturado en el bugreport |
    | **Tombstones** | [tombstones.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/bugreport/tombstones.py) | Archivos tombstone\_\* | Analiza los volcados de fallos (crashes) de aplicaciones |

=== "backup"

    | Módulo | Archivo fuente | Qué analiza | Utilidad forense |
    | :---: | ----- | ----- | ----- |
    | **SMS** |  [sms.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/backup/sms.py) |  Los mensajes SMS/MMS respaldados | Extrae el contenido de los mensajes, identifica enlaces incluidos en ellos y los compara contra indicadores de compromiso |

=== "intrusion logs"

    | Módulo | Archivo fuente | Qué analiza | Utilidad forense |
    | :---: | ----- | ----- | ----- |
    | **DnsEvent** | [dns\_event.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/intrusion_logs/dns_event.py) | Eventos de resolución DNS (hostnames e IPs consultadas) | Identifica dominios o IPs de infraestructura maliciosa contactados por el dispositivo, comparándolos contra indicadores de compromiso |
    | **ConnectEvent** | [connect\_event.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/intrusion_logs/connect_event.py) | Eventos de conexión de red saliente (IP y puerto de destino) | Detecta conexiones directas a IPs asociadas a infraestructura de spyware conocida, incluso cuando no hubo una consulta DNS previa |
    | **SecurityEvent** | [security\_event.py](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/intrusion_logs/security_event.py) | Eventos de seguridad del sistema (actividad ADB, procesos de apps, bloqueo/desbloqueo de pantalla, arranque del sistema, entre otros) | Aporta contexto sobre actividad sensible en el dispositivo, como comandos ejecutados por ADB (adb shell, adb pull, adb push) o inicio de procesos de apps, útil para reconstruir una línea de tiempo de un incidente |

### Lógica de ejecución de la MVT

Al ejecutar ***mvt-android check-androidqf*** sobre una extracción de AndroidQF, la MVT sigue un flujo de trabajo automático que no requiere intervención manual. Durante este proceso, MVT:

1. Carga los indicadores de compromiso y los módulos que correspondan, según el tipo de artefactos presentes en la extracción.
2. Carga los datos de los archivos generados por la adquisición que pasamos como input.
3. Procesa y *parsea* esa información con cada módulo y sus artefactos correspondientes, es decir, transforma datos crudos (texto plano, JSON, binarios) en registros estructurados y legibles.
4. Compara esos registros contra los indicadores de compromiso (IOCs) cargados en el primer paso, y contra un conjunto de heurísticas propias de cada módulo.

Este flujo se repite módulo por módulo, uno después del otro y es exactamente lo que se observa en la terminal a medida que la ejecución avanza.

### Entendiendo las líneas de log de MVT

Cada línea que produce la MVT comienza indicando qué módulo la generó. Esto es clave para saber en qué parte de la ejecución se está, especialmente cuando la salida en pantalla combina resultados de varios módulos ejecutándose uno tras otro.

Por ejemplo:

```sh
2026-08-14 11:21:06,364 - mvt.android.modules.androidqf.aqf_settings - MEDIUM - Found suspicious "global" setting "package_verifier_user_consent = -1" (disabled Google Play Protect)
```

El fragmento ***mvt.android.modules.androidqf.aqf\_settings*** indica que esta alerta proviene específicamente del módulo **AQFSettings**, el cual  analiza los archivos ***settings\_\*.txt*** de la extracción.

Qué buscar y en dónde **dependerá en gran medida del contexto de la información que analizamos**. La MVT no entrega resultados personalizados, más bien entrega evidencia organizada para que la persona analista interprete los resultados tomando en consideración el contexto del caso.

La MVT mostrará advertencias, con distintos niveles de severidad:

* **Low, Medium y High**: relacionadas con [**TTPs** (Tácticas, Técnicas y Procedimientos)](../../references/00-glossary/index.md#ttp), es decir, advertencias heurísticas y patrones de comportamiento sospechosos que no están necesariamente vinculados a una amenaza conocida. Por ejemplo:

```sh
2026-08-14 11:21:06,116 - mvt.android.modules.androidqf.aqf_packages - MEDIUM - Found a non-system package installed via adb or another method: "com.facebook.katana"
2026-08-14 11:21:38,714 - mvt.android.modules.bugreport.dumpsys_battery_daily - MEDIUM - Detected uninstall of package com.SecUpwN.AIMSICD (vers 0)
```

* **Critical**: son advertencias relacionadas con una coincidencia contra los **indicadores de compromiso (IOCs)** cargados desde las colecciones STIX2, es decir, contra una amenaza previamente documentada y atribuida.

**Las alertas son emitidas según las coincidencias con comportamientos e IOCs.** Las alertas deben ser revisadas identificando su severidad, el módulo que las produjo y la marca de tiempo asociada a la alerta. Dependiendo de la cantidad de alertas, los módulos con los que se relacionan, su severidad y relación con la temporalidad que marca la entrevista inicial, estas alertas pueden indicar si es conveniente profundizar en el análisis de alguna información.

Tal y cómo se detalla en el [material introductorio sobre triaje técnico en Android](https://forensics.socialtic.org/en/explainers/04-explainer-introduction-android-triage/), tener claridad en la línea de tiempo y los acontecimientos reportados  permite enfocar la búsqueda en artefactos y espacios de tiempo contenidos. La entrevista inicial de triaje dicta el rumbo que seguirá la revisión técnica y la investigación forense, ya que mediante esta entrevista se obtiene información esencial de interés, como por ejemplo:

* Si el dispositivo fue confiscado por un cierto tiempo
* Si hay o no aplicaciones sospechosas que aparecieron de repente
* Si la persona cayó en phishing e instaló una aplicación o descargó un archivo
* Si alguna aplicación se cierra repentinamente

Durante la revisión, es frecuente encontrar **nombres de paquetes, procesos o servicios que no reconocemos**. Esto es normal, incluso para analistas con experiencia, dada la enorme cantidad de aplicaciones y componentes del sistema que existen en el ecosistema Android. Cuando esto ocurra se recomienda:

* Anotar y documentar el nombre del paquete o proceso, junto con el contexto en el que apareció.
* Investigar de manera privada las aplicaciones y procesos específicos usando motores de búsqueda como [Virus Total](https://www.virustotal.com/), para entender si se trata de un componente legítimo del sistema, de una aplicación comercial conocida, o de algo que amerita mayor atención.

### Comandos útiles para el filtrado de la salida de MVT

Para analizar la salida de la MVT de manera eficiente, es conveniente conocer algunos comandos de la terminal que permiten filtrar, buscar y explorar grandes volúmenes de información sin necesidad de abrir cada archivo manualmente:

* **grep**: [grep](https://linuxcommandlibrary.com/man/cat) busca coincidencias de texto dentro de un archivo. Es especialmente útil para filtrar líneas por nivel de severidad o por módulo. Por ejemplo, para filtrar solo con las alertas de nuestro command.log:

```sh
grep -E "LOW|MEDIUM|HIGH|CRITICAL" command.log
```

O para revisar únicamente lo que reportó un [módulo](#modulos) en particular:

```sh
grep "dumpsys_battery_daily" command.log
```

* **find**: [find](https://linuxcommandlibrary.com/man/cat) localiza archivos dentro de la carpeta de resultados generada por la MVT, especialmente útil cuando la extracción contiene muchos subdirectorios y archivos JSON.

```sh
find ./YYYY-MM-DD-out-androidqf/ -name "*detected*"
```

* **cat**: [cat](https://linuxcommandlibrary.com/man/cat) muestra el contenido completo de un archivo directamente en la terminal, útil para archivos pequeños como packages.json.

```sh
 cat packages.json
```

* **jq**: [jq](https://linuxcommandlibrary.com/man/jq) es una herramienta especializada en procesar y filtrar archivos JSON, el formato en el que la MVT guarda la mayoría de sus resultados. Por ejemplo, para extraer únicamente el nivel, el módulo y el mensaje de cada alerta de alerts.json:

```sh
jq '.[] | {level, module, message}' alerts.json
```

### Revisión de archivos de salida de MVT

#### command.log

Este es el output que la MVT genera en pantalla mientras se ejecuta, y que también queda guardado en el archivo command.log. Por lo general, es un buen punto de partida para la revisión, ya que en un mismo archivo **se puede ver en orden cronológico tanto el proceso completo de ejecución como las alertas que se fueron generando**.

Dentro de command.log se pueden encontrar distintos tipos de líneas: informativas sobre el proceso (INFO, DEBUG), errores (ERROR), y alertas con distintos niveles de severidad (LOW, MEDIUM, HIGH, CRITICAL), por ejemplo:

```sh
2026-08-14 11:21:38,714 - mvt.android.modules.bugreport.dumpsys_battery_daily - MEDIUM - Detected uninstall of package com.republicwireless.tel (vers 0)
```

**Si se encuentra una alerta de interés, es posible profundizar revisando los logs específicos de ese módulo.** Por ejemplo, si identificamos una línea de interés como la siguiente:

```sh
2026-08-14 11:21:06,116 - mvt.android.modules.androidqf.aqf_packages - MEDIUM - Found a non-system package installed via adb or another method: "com.facebook.katana"
```

Es conveniente revisar el archivo de resultados del módulo AQFPackages (aqf\_packages.json dentro de la carpeta de resultados) para revisar el registro completo de ese paquete, su instalador, sus certificados, sus hashes y demás metadatos.

**Cuando la MVT identifica un hallazgo relevante**, por ejemplo, una coincidencia con un IoC o alertas medias heurísticas, además de mostrarlo en pantalla, **genera un archivo con el sufijo *detected* correspondiente a cada módulo**, donde queda registrado exclusivamente lo que generó la alerta.

Es importante tener presente que **las alertas no son necesariamente una confirmación de un compromiso**, pero sin duda deben investigarse. Es importante documentar todo lo que parezca sospechoso y que requiera una revisión posterior. Por ejemplo, pueden haber alertas relacionadas con APKs específicos, como en el caso de *com.facebook.katana* del ejemplo anterior.

#### timeline.csv

El timeline.csv es un archivo en formato CSV que **contiene todos los eventos del dispositivo que son extraídos por la MVT organizados por fecha**. Esto lo convierte en una archivo útil para reconstruir la actividad del dispositivo en un rango de tiempo específico. Cada fila incluye la marca de tiempo del dispositivo, el módulo que generó el evento, un tipo de evento corto, y una descripción. Por ejemplo, así se ven algunas filas relacionadas con la instalación de paquetes de Facebook:

```
"Device Local Timestamp","Plugin","Event","Description"
"2008-12-31 19:00:00","DumpsysPackages","package_first_install","Install or update of package com.facebook.system"
"2008-12-31 19:00:00","DumpsysPackages","package_last_update","Install or update of package com.facebook.katana"
```

Es un archivo **útil cuando se tiene una ventana de tiempo específica que investigar a partir de la entrevista de triaje**, ya que permite filtrar toda la actividad del dispositivo alrededor de la línea de tiempo identificada en la entrevista inicial.

#### alerts.json

El archivo alerts.json **concentra todas las alertas generadas durante el análisis ejecutado en un único archivo estructurado**. A diferencia del command.log, que mezcla alertas con líneas informativas del proceso, alerts.json contiene únicamente los hallazgos.

Cada alerta incluye el nivel de severidad, el módulo de origen, el mensaje, la marca de tiempo del evento (cuando aplica) y el registro completo (event) que generó la alerta. Por ejemplo:

```json
{
    "level": "MEDIUM",
    "module": "aqf_packages",
    "message": "Found a non-system package installed via adb or another method: \"com.facebook.katana\"",
    "event_time": "",
    "event": {
        "name": "com.facebook.katana",
        "installer": "null",
        "third_party": true
    }
}
```

Al ser un único archivo consolidado, es un buen punto de partida cuando se quiere tener una visión general de todo lo que MVT identificó como sospechoso, antes de profundizar módulo por módulo.

#### alerts\_timeline.csv

El archivo alerts\_timeline.csv **concentrará la línea de tiempo de alertas identificadas durante la ejecución de un análisis con MVT**. La ventaja de revisar este archivo es que directamente puedes identificar qué alertas produjo cada módulo ejecutado, además del evento específico.

```
"Event Time","Module","Message","Event"
"2021-02-01","dumpsys_battery_daily","Detected uninstall of package com.republicwireless.tel (vers 0)","{'action': 'update', 'from': '2021-02-01', 'to': '2021-02-13', 'package_name': 'com.republicwireless.tel', 'vers': '0'}"
"2026-08-10","dumpsys_battery_daily","Detected uninstall of package com.SecUpwN.AIMSICD (vers 0)","{'action': 'update', 'from': '2026-08-10', 'to': '2026-08-11', 'package_name': 'com.SecUpwN.AIMSICD', 'vers': '0'}"
"2026-08-10 18:21:03.799000","dumpsys_appops","Package 'com.google.android.apps.nbu.files' had risky permission 'REQUEST_INSTALL_PACKAGES' set to 'Reject' at 2026-08-10 18:21:03.799000","{'package_name': 'com.google.android.apps.nbu.files', 'permissions': [{'name': 'REQUEST_INSTALL_PACKAGES', 'entries': [{'access': 'Access', 'type': 'top-s', 'timestamp': '2026-08-10 18:34:25.002000'}, {'access': 'Reject', 'type': 'top-s', 'timestamp': '2026-08-10 18:21:03.799000'}], 'access': 'allow'}], 'uid': 'u0a136'}"
"2026-08-10 18:34:25.002000","dumpsys_appops","Package 'com.google.android.apps.nbu.files' had risky permission 'REQUEST_INSTALL_PACKAGES' set to 'Access' at 2026-08-10 18:34:25.002000","{'package_name': 'com.google.android.apps.nbu.files', 'permissions': [{'name': 'REQUEST_INSTALL_PACKAGES', 'entries': [{'access': 'Access', 'type': 'top-s', 'timestamp': '2026-08-10 18:34:25.002000'}, {'access': 'Reject', 'type': 'top-s', 'timestamp': '2026-08-10 18:21:03.799000'}], 'access': 'allow'}], 'uid': 'u0a136'}"
```

#### Archivos con sufijo *detected*

Además del command.log, timeline.csv, alerts.json y alerts\_timeline.csv, la **MVT genera archivos individuales por módulo cada vez que identifica un comportamiento sospechoso o una coincidencia con algún IoC**. Estos archivos siempre llevan el sufijo detected en el nombre y contiene la información completa de lo que generó cada alerta.

## Conclusión

El valor de la MVT radica en **transformar artefactos forenses crudos y desorganizados en evidencia estructurada y comparable,** de forma consistente, sin requerir que una persona analista revise manualmente cada archivo que produce la extracción de un dispositivo.

Sin embargo, no se debe confundir la estructuración de los archivos con la interpretación. Comprender qué significa un hallazgo, si importa, y qué hacer a continuación depende de un contexto que solo la entrevista de triaje y la revisión de una persona analista pueden aportar.

Comprender cómo se estructura la herramienta MVT, los diferentes módulos disponibles, su cadena de ejecución y la salida permite utilizar la herramienta para un triaje técnico.


## Comentarios

¿Tienes **comentarios o sugerencias** sobre este recurso? Puedes utilizar la **función de comentar que se muestra a continuación** para dejarnos tus ideas o apreciaciones. Por favor asegúrate de seguir nuestro [código de conducta](../../community/code-of-conduct/). La función de comentarios enlaza directamente a la sección de [_Discussions_ de Github](https://github.com/Socialtic/forensics/discussions), donde también **puedes participar en las discusiones de forma directa**, si lo prefieres.   
