---

title: Explainer - Introduction to technical triage of Android devices
summary: Concepts, considerations and artifacts to know before performing technical triage of an Android device
keywords: triage, android, mvt, artifacts, dfir
lang: en
tags: [explainer, android, intro]
last_updated: 2026-11-04
some_url:
created: 2026-11-04
comments: true
author:
    name: Daniel
    url: https://socialtic.org/quienes-somos/
    description: SocialTIC

translation-review-pending: true
---

# Guía explicativa: Introducción a la evaluación técnica de dispositivos Android

Este documento forma parte de un **repositorio de documentación técnica** cuyo objetivo principal es establecer una base de conocimientos contrastados, flexibles y accesibles para **impulsar el análisis forense consensuado en apoyo de la sociedad civil en todo el mundo**. Para organizar los contenidos, utilizamos el [marco de documentación técnica Diátaxis](../../references/00-glossary/index.md#diataxis). Este recurso concreto se enmarca en [la categoría «explicación» de Diátaxis](https://diataxis.fr/explanation/). Es complementario a otros recursos de este repositorio, entre los que se incluyen [guías prácticas](../../how-tos/index.md), [tutoriales](../../tutorials/index.md) y [referencias](../../references/index.md).

Este documento ofrece una introducción a la evaluación técnica de dispositivos Android. Se trata de un documento narrativo que detalla conceptos, consideraciones y aspectos técnicos que una persona debe conocer antes de llevar a cabo la evaluación técnica de un dispositivo Android. Es complementario a otros recursos, entre los que se incluyen:

* [Guía explicativa: Exploración de la herramienta MVT para el triaje técnico de dispositivos Android](../05-explainer-mvt-android-triage/index.md)
* [Tutorial: Uso de MVT para la evaluación técnica de dispositivos Android](../../tutorials/02-tutorial-mvt-android-triage/index.md)
* [Guía práctica: Triaje técnico de dispositivos Android con MVT](../../how-tos/06-how-to-triage-android-mvt/index.md)
* [Guía práctica: ¿Cómo realizar una extracción con AndroidQF?](../../how-tos/04-how-to-extract-with-androidqf/index.md)

## ¿Qué entendemos por «triaje técnico de dispositivos Android»?

El concepto de «triaje» se utiliza para describir diferentes partes del [proceso DFIR](../../references/00-glossary/index.md#dfir-digital-forensics-and-incident-response), por lo que conviene detallar a qué nos referimos con este término en el contexto de este recurso y repositorio.

En el uso clásico del DFIR, el triaje se refiere a una evaluación inicial rápida que se utiliza para decidir si es necesaria una investigación más profunda y en qué aspectos centrarla. El término proviene del triaje médico: clasificar y priorizar, no diagnosticar. Por ejemplo, la [NIST SP 800-61r3](https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-61r3.pdf) describe el triaje (en el contexto de la validación de informes de incidentes) como una revisión preliminar para confirmar que se ha producido un incidente y evaluar su gravedad y urgencia, o como una decisión tomada antes de que comience una investigación más profunda, no como la investigación en sí misma.

En el contexto de este recurso y repositorio, ampliamos esta definición de triaje para abarcar dos aspectos:

* **Triaje no técnico:** el trabajo de entrevista, recopilación de contexto y formulación de hipótesis que tiene lugar antes de tocar ningún dispositivo. Este paso determina qué es lo que realmente debe buscarse en la fase técnica, y es donde se abordan directamente con la persona que solicita asistencia las [consideraciones sobre el consentimiento](../../how-tos/01-how-to-obtain-informed-consent/index.md).
* **Revisión técnica de los artefactos:** se refiere al uso de la información obtenida (informes de errores, registros de intrusiones, extracción de AndroidQF, etc.) para compararla con los IOC conocidos y con patrones o comportamientos sospechosos (TTP). Es importante destacar que, durante esta revisión inicial de los artefactos, se buscan indicios de una posible actividad maliciosa, con el fin de decidir si es necesario realizar un análisis manual más exhaustivo.

Conviene **diferenciar esta clasificación técnica de un análisis forense más profundo**, que suele realizarse mediante revisión manual y que puede conducir a la identificación de IOC no detectados anteriormente.

Por lo tanto, en el contexto de este repositorio, definimos **triaje técnico** como *la revisión delimitada y basada en hipótesis de los artefactos del dispositivo fácilmente disponibles (informes de errores, extracción de AndroidQF, registros de intrusión, etc.) para identificar [indicadores de compromiso](../../references/00-glossary/index.md#indicator-of-compromise-ioc) o [TTP](../../references/00-glossary/index.md#ttp) coherentes con vectores de ataque conocidos.*

## ¿Cómo empezar a investigar posibles amenazas en dispositivos Android?

Antes de llevar a cabo una evaluación técnica, debes tener acceso a información clave sobre el caso y la solicitud. **Comprender el contexto, la cronología y el historial de las posibles amenazas es fundamental** antes de analizar cualquier prueba técnica. Esto puede marcar la diferencia entre intentar encontrar una aguja en un pajar y llevar a cabo un análisis más específico y centrado, guiado por esta hipótesis.

Dependiendo de tu función en la investigación, es posible que tengas contacto directo con la persona que solicita ayuda o que trabajes a través de un colaborador sobre el terreno. En cualquier caso, en la **análisis forense consensuado**, los analistas suelen tener acceso a información contextual sobre posibles amenazas, posibles vectores, el historial de amenazas de la persona y el contexto más amplio del caso. **Esta es una de las ventajas clave de la investigación forense consensuada**, en comparación con los enfoques más contradictorios que se utilizan en otros contextos.

### Recopilación de contexto antes de la evaluación técnica

La mayor parte de esta información se **recopila durante las entrevistas y co**Conversaciones** cuando se recibe el caso por primera vez. Al igual que en cualquier conversación relacionada con una posible amenaza, ten siempre presente el [consentimiento](../../how-tos/01-how-to-obtain-informed-consent/index.md): esta información solo está disponible porque la persona decidió compartirla, y **la forma de preguntar es tan importante como lo que se pregunta**.

Ten en cuenta también que ser víctima de un ataque de spyware tiene repercusiones que van más allá del problema técnico. El [Estudio sobre los impactos psicosociales del spyware y la Guía para el acompañamiento psicosocial](https://www.acceso.or.cr/psychosocial-impacts-of-spyware/) analizan algunas de estas consecuencias y ofrecen orientación sobre cómo los responsables de la respuesta a incidentes pueden incorporar prácticas que conduzcan a un acompañamiento más completo y holístico.
 
Preparar preguntas orientativas y documentación puede ser de gran ayuda para asegurarte de que recopilas lo que realmente necesitas. En general, al finalizar estas conversaciones deberías saber:

* ¿Qué ha ocurrido?
* ¿Cuándo ocurrió? ¿Cuál es la cronología de los hechos?
* ¿Cómo ocurrió?
* ¿Qué dispositivos se vieron afectados?
* ¿Qué medidas se han tomado ya?

**Documenta** esta información lo antes posible tras la conversación y asegúrate de que esté disponible para consultarla durante la propia evaluación técnica. Es fácil perder de vista un detalle mencionado en una llamada inicial cuando ya te has adentrado en varias fases de la revisión de los artefactos.

### ¿Qué hacer cuando no hay indicios claros de que se haya producido una intrusión?

A veces, las personas se ponen en contacto para solicitar una **revisión preventiva o rutinaria de sus dispositivos**, sin ningún indicador específico de actividad maliciosa y sin una razón concreta más allá de su perfil de riesgo. Se trata de una solicitud válida, y sigue siendo posible llevar a cabo una adquisición y ejecutar comprobaciones automatizadas en busca de IOC conocidos. Pero conviene ser **sincero sobre los límites de esta revisión**, ya que solo sacará a la luz amenazas *conocidas*, y examinar todo un sistema operativo en busca de rastros de actividad maliciosa, sin nada que acote la búsqueda, resulta complicado y requiere muchos recursos.

### ¿Cómo se ven comprometidos los dispositivos Android?

En general, independientemente de las vulnerabilidades específicas que se aprovechen, los atacantes siguen un proceso similar para comprometer los dispositivos y la información almacenada y generada por ellos. Podemos describir esta cadena de ataque del spyware de la siguiente manera:

![Cadena de ataque del spyware: pasos habituales en las infecciones por spyware](../../../assets/04-explainer/spyware-kill-chain.png "imagen 1"){ loading=lazy }
/// pie de foto
**Imagen 1**. Cadena de ataque del spyware. Adaptado del Grupo de Análisis de Amenazas de Google, [Buying Spying: Perspectivas sobre los proveedores de vigilancia comercial](https://storage.googleapis.com/gweb-uniblog-publish-prod/documents/Buying_Spying_-_Insights_into_Commercial_Surveillance_Vendors_-_TAG_report.pdf).
///


Los pasos pueden describirse de la siguiente manera:

* **Entrega inicial:** se refiere al paso inicial llevado a cabo por un atacante, que puede consistir en el envío de un mensaje de phishing para un ataque de «1 clic», la activación de un proceso a través de una vulnerabilidad de «0 clics» o la interceptación de la red para entregar un paquete malicioso.
* **Explotación:** en esta fase, se ejecuta el paquete entregado inicialmente, lo que puede dar lugar a la ejecución remota de código, la fuga del entorno de pruebas o la escalada de privilegios locales.
* **Instalación:** una vez que el paquete consigue escapar del entorno aislado de la aplicación y obtiene privilegios suficientes, instala el agente de spyware.
* **Recopilación de información:** durante esta fase, el atacante puede recopilar información de interés, incluyendo mensajes, correos electrónicos, historial de navegación, conversaciones a través del micrófono y vídeos o fotos a través de la cámara.
* **Exfiltración:** por último, la información se extrae del dispositivo. Para ello, suele establecerse comunicación con un servidor de comando y control (C2). Este servidor remoto puede enviar comandos y recibir la información recopilada.

Además de comprender los pasos que suelen seguir los atacantes para comprometer un dispositivo, resulta útil analizar específicamente los dispositivos Android y los informes históricos de ataques contra la sociedad civil. Comprender el proceso, las tácticas y las técnicas del atacante puede ayudar a **desarrollar un modelo mental de qué rastros hay que buscar** al examinar las pruebas. Buscar cualquier cosa *inusual* puede ser una tarea complicada, sobre todo si buscamos en todas partes y en todas las fechas, sin tener claro qué rastros concretos estamos buscando.

A continuación describimos algunos vectores de ataque diferentes que pueden utilizarse para obtener acceso a un dispositivo Android. 

#### Compromiso a nivel de cuenta (sin compromiso del dispositivo)

Aunque se trata de un tipo de incidente diferente, a veces un comportamiento malicioso que alguien sospecha que podría ser una infección de su dispositivo —por ejemplo, la exfiltración de datos— puede ser, en realidad, el resultado de una cuenta comprometida en lugar de un dispositivo comprometido. La vulneración de una cuenta suele ser consecuencia de prácticas y configuraciones de seguridad poco seguras, como la reutilización de contraseñas o la falta de autenticación multifactorial, pero también puede deberse a ataques avanzados, dirigidos o patrocinados por un Estado. 

También cabe mencionar que Google a veces envíads [avisa cuando detecta intentos de comprometer cuentas por parte de atacantes respaldados por gobiernos](https://support.google.com/mail/answer/2591015). Por lo general, estas advertencias están relacionadas con problemas a nivel de cuenta y no son necesariamente indicativas de un intento de atacar un dispositivo. 


#### APK malicioso (a través de la proximidad física)

Esto no requiere una explotación avanzada del dispositivo, ya que se produce cuando los atacantes pueden manipular físicamente el dispositivo para instalar un agente. Actores patrocinados por el Estado han utilizado esta técnica, tal y como informó Citizen Lab en 2024 en su [informe: «Something to Remember Us By»](https://citizenlab.ca/research/device-confiscated-by-russian-authorities-returned-with-monokle-type-spyware-installed/), que documenta cómo el software espía, implantado de forma encubierta en un teléfono, fue devuelto a un programador ruso tras su puesta en libertad.

Cabe destacar que la [investigación de Amnistía Internacional: «Una prisión digital»: la vigilancia y la represión de la sociedad civil en Serbia](https://securitylab.amnesty.org/latest/2024/12/a-digital-prison-surveillance-and-the-suppression-of-civil-society-in-serbia/) documenta el uso de /*NoviSpy*, un nuevo programa espía instalado mientras los dispositivos se encontraban bajo custodia física de la policía, y que permite capturar datos personales sensibles del teléfono de una víctima.

#### Aprovechamiento de vulnerabilidades

Por lo general, se trata de ataques muy específicos, a menudo patrocinados por el Estado, que utilizan varios vectores para instalar el software espía en el dispositivo:

* **1 clic:** la víctima tiene que interactuar con algo (un enlace, un mensaje) para que se ejecute el exploit.
* **0 clics:** no se requiere ninguna interacción por parte de la víctima.
* **Manipulación de la red:** los atacantes interceptan o manipulan el tráfico para dirigir a la víctima a sitios maliciosos que pueden aprovechar vulnerabilidades o redirigirla a descargas que infectan el dispositivo.
* **Publicidad dirigida:** en 2026, el [informe de Citizen Lab: Exposing AdFection](https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/) reveló por primera vez cómo los anuncios personalizados pueden convertirse en un canal para el spyware mercenario de cero clics.  

## Rastros comunes en Android

Los rastros comunes son los elementos o huellas que permanecen en un dispositivo tras una infección por malware. Constituyen la materia prima para llevar a cabo la evaluación técnica. Comprobar estos rastros, categoría por categoría, cotejándolos con indicadores conocidos y patrones sospechosos (obtenidos a partir de la entrevista) forma parte de la evaluación técnica.

* **Mensajes y enlaces:** suelen ser el primer paso de un ataque, y se utilizan para que la víctima haga clic en un enlace, abra un archivo o instale una aplicación.
* **Historial de navegación:** puede revelar los sitios que una persona visitó o a los que fue redirigida como parte de un ataque, incluso después de que el enlace inicial haya desaparecido de una aplicación de mensajería.
* **Aplicaciones:** pueden ser rastros directos de una intrusión, ya que, dependiendo del tipo de ataque, un agente malicioso podría instalarse como tal.
* **Permisos**: definen lo que una aplicación está realmente autorizada a hacer en un dispositivo, y una discrepancia entre los permisos de una aplicación y su finalidad declarada es una clara señal de uso indebido.
* **Receptores de difusión generales**: permiten que una aplicación detecte eventos del sistema o de otras aplicaciones, y revisarlos puede ayudar a identificar aplicaciones en posición de acceder a información confidencial.
* **Los servicios de accesibilidad** existen para ayudar a los usuarios con discapacidad a interactuar con su dispositivo, por ejemplo, leyendo en voz alta el contenido de la pantalla o realizando acciones en nombre del usuario. Ese propósito legítimo requiere amplias capacidades que pueden ser objeto de abuso por parte de aplicaciones maliciosas, como el spyware y el stalkerware. 
* **Configuraciones:** determinados ajustes del dispositivo, cuando se desactivan, eliminan protecciones que, de otro modo, señalarían o bloquearían actividades maliciosas. Comprobar su estado directamente puede revelar si dicha protección se desactivó deliberadamente.
* **Señales de rooting:** el rooting elimina muchas de las protecciones en las que se basa un dispositivo Android de serie. Esto puede ser el resultado de una acción del usuario o también de una actividad maliciosa.
* **Archivos sospechosos:** pueden quedar como rastro de una actividad maliciosa. Pueden ser diferentes tipos de archivos, incluyendo cargas maliciosas, datos o registros. 
* **Fallos del sistema:** pueden indicar un intento fallido de explotación. Las cadenas de explotación suelen ser frágiles y no siempre funcionan, lo que provoca fallos en las aplicaciones. Dado que las diferentes partes de Android fallan de formas distintas, el tipo de fallo indica en qué parte del sistema se produjo el intento. Merece la pena investigar más a fondo un proceso que se bloquea repetidamente o que falla en torno a un evento sospechoso.

### Tabla de referencia de artefactos de Android

**Tabla 1.** Lista de artefactos de Android, su importancia y disponibilidad

| Artefacto | Qué buscar | Disponible en |
| ----- | ----- | ----- |
| Mensajes y enlaces | Enlaces sospechosos; mensajes de ingeniería social que solicitan información, acceso a un enlace, la descarga de un archivo o la instalación de un APK | Copias de seguridad de SMS, copias de seguridad de bases de datos de aplicaciones sin cifrar, Google Takeout, revisión manual de mensajes |
| Historial de navegación | SuEnlaces sospechosos, redireccionamientos entre sitios web, descargas de archivos | Google Takeout (si se ha activado la sincronización de la navegación), consulta de la base de datos de navegación a través de ADB (si el dispositivo está rooteado), revisión manual en el navegador (si no está rooteado) |
| Aplicaciones | Instaladas desde fuentes sospechosas, con firmas o certificados modificados, permisos extraños, nombres de paquetes extraños o aleatorios | Google Takeout a través del historial de actividad de Google, Bugreport, ADB, AndroidQF |
| Permisos | Funciones sensibles que no se corresponden con la finalidad declarada de una aplicación, como el acceso a la cámara, al micrófono o a la ubicación | Informe de errores, ADB, AndroidQF |
| Receptores de difusión generales | Aplicaciones registradas para recibir difusiones sensibles del sistema o de telefonía. Algunos ejemplos sospechosos son: <br>`android.provider.Telephony.NEW_OUTGOING_SMS`<br>`android.provider.Telephony.SMS_RECEIVED`<br>`android.intent.action.DATA_SMS_RECEIVED`<br>`android.intent.action.PHONE_STATE`<br>`android.intent.action.NEW_OUTGOING_CALL` | Informe de errores, ADB, AndroidQF |
| Servicios de accesibilidad | Aplicaciones con acceso a la accesibilidad que no tienen una razón legítima para necesitarlo | Informe de errores, ADB, AndroidQF |
| Configuraciones | Ajustes que desactivan Google Play Protect, el envío de registros de fallos o la confirmación de instalación de ADB. Por ejemplo:<br>**Relacionado con Google Play Protect:** `verifier_verify_adb_installs`, `package_verifier_enable`, `package_verifier_user_consent` (desactiva Google Play Protect), `upload_apk_enable` (desactiva Google Play Protect)<br>**Registros de fallos desactivados:** `send_security_reports`, `samsung_errorlog_agree`, `send_action_app_error`<br>**Confirmación de la instalación de aplicaciones mediante ADB desactivada:** `adb_install_need_confirm` | Informes de errores, ADB, AndroidQF |
| Señales de rooting | Binarios de rooting o aplicaciones de rooting instaladas en el dispositivo, por ejemplo:<br>**Binarios:** `su`, `busybox`, `magisk`<br>**Aplicaciones:** `com.noshufou.android.su` | Informe de errores, ADB, AndroidQF |
| Archivos sospechosos | Archivos en ubicaciones inusuales, o creados, modificados o con permisos que no se ajustan al uso normal | Informe de error, ADB, AndroidQF |
| Fallos | Fallos de aplicaciones, servicios, procesos o del kernel que pueden indicar un intento fallido de explotación | Informe de error, AndroidQF |

## Herramientas para la evaluación técnica de dispositivos Android

### MVT

[MVT](https://docs.mvt.re/en/latest/) (Mobile Verification Toolkit) es una herramienta que facilita el análisis forense consensuado de dispositivos Android e iOS, con el fin de identificar rastros de compromiso. Fue desarrollado y publicado por el Laboratorio de Seguridad de Amnistía Internacional en julio de 2021 en el marco del Proyecto Pegasus, junto con una metodología forense técnica. Su mantenimiento sigue a cargo de Amnistía Internacional y otros colaboradores.

Conceptualmente, funciona como un analizador sintáctico y un comparador. Toma los datos recopilados de un dispositivo (a través de AndroidQF, un informe de errores o registros de intrusión) y los compara con indicadores conocidos de compromiso, al tiempo que **facilita la revisión de la propia información analizada**. Los resultados del MVT deben revisarse más allá de las advertencias iniciales, ya que los diferentes archivos que crea incluyen información relevante sobre los artefactos descritos anteriormente. Los diccionarios de MVT disponibles en la [sección de referencias](../../references/index.md) proporcionan detalles adicionales sobre cada uno de los archivos generados por MVT, y el recurso complementario [Guía explicativa: Triaje técnico con MVT](../05-explainer-mvt-android-triage/index.md) profundiza aún más en la lógica y el uso de la herramienta. 

Hay que tener en cuenta que MVT no es una solución milagrosa: **su ejecución, por sí sola, no confirma ni descarta un compromiso de seguridad.** Requiere un análisis manual y una revisión de sus resultados, pero MVT puede resultar útil para detectar aspectos que merezcan ser investigados.

#### Módulos de MVT para Android

Es útil saber qué módulos están disponibles para un comando determinado, ya que el que se aplique dependerá de los datos de los que se disponga:

* **mvt-android check-androidqf**: permite analizar una extracción realizada con la herramienta AndroidQF utilizando los [módulos para dicha extracción](https://github.com/mvt-project/mvt/tree/main/src/mvt/android/modules/androidqf). Estas extracciones suelen incluir también un informe de errores y, si están disponibles, los registros de intrusión. Por lo tanto, el uso del módulo androidqf puede ser suficiente para realizar un análisis de todos los artefactos disponibles, ya que MVT detecta automáticamente estos archivos y también ejecuta los [módulos correspondientes al informe de errores](https://github.com/mvt-project/mvt/tree/main/src/mvt/android/modules/bugreport) y los [módulos correspondientes a la copia de seguridad](https://github.com/mvt-project/mvt/tree/main/src/mvt/android/modules/backup).
* **mvt-android check-bugreport**: permite el análisis directo de un informe de errores. Si no dispones de una extracción de AndroidQF y deseas realizar un análisis rápido, se recomienda utilizar este módulo como primer paso. Si se detectan indicios de actividad sospechosa, se recomienda complementar este análisis con un análisis completo de una extracción de AndroidQF.
* **mvt-android check-intrusion-logs**: los registros de intrusión solo están disponibles en dispositivos con Android 16 o superior y cuando la persona haya activado previamente el «Modo de protección avanzada» con el registro de intrusiones habilitado. Si dispones de un archivo de registro de intrusiones, es posible analizar este archivo concreto utilizando este comando y el módulo MVT.

El comando que se utilice dependerá de lo que tengas disponible. Una extracción de AndroidQF suele incluir ya un informe de errores y, si se han recopilado, los registros de intrusión, por lo que ejecutar `check-androidqf` sobre ella analizará la mayor parte de la información obtenida de una sola vez, sin necesidad de ejecutar los demás comandos por separado.

### ALEAPP

[ALEAPP](https://github.com/abrignoni/ALEAPP) (Android Logs Events And Protobuf Parser) es una herramienta de código abierto para analizar y procesar registros de Android, disponible tanto como herramienta de línea de comandos como con interfaz gráfica de usuario. A diferencia de MVT, ALEAPP no se basa en la comparación de artefactos con indicadores de compromiso (IOC) para detectar spyware. Se trata de una herramienta más general que ayuda a reconstruir la actividad del usuario, la cual se presenta posteriormente en un informe HTML.

!!! nota «Nota»

 En este repositorio profundizamos específicamente en MVT, ya que es una herramienta comunitaria basada en el análisis consensuado y muy utilizada en este ámbito. Ese enfoque no debería disuadirte de explorar otras herramientas, incluidas muchas que no figuran en la lista anterior.

## Conclusión

A través de este recurso hemos explorado aspectos clave a tener en cuenta a la hora de realizar una evaluación técnica de un dispositivo Android, incluida la importancia de la entrevista inicial, una visión general de cómo un dispositivo podría verse comprometido y los diferentes artefactos disponibles. La intención es construir un marco conceptual que pueda utilizarse para llevar a cabo el triaje técnico de un dispositivo Android. Los pasos concretos que se sigan dependerán en gran medida del contexto de cada caso y deben guiarse por la entrevista inicial descrita anteriormente en este documento.

Investigar una posible amenaza cuando ese contexto no está claro puede resultar muy difícil, ya que podría haber una gran cantidad de información que revisar y recursos limitados para hacerlo. Por eso, formular hipótesis y establecer objetivos concretos para la investigación técnica puede marcar la diferencia. En la misma línea, disponer de un **modelo mental de cómo funcionan realmente estos ataques**, incluyendo los pasos que suele seguir un adversario y los vectores descritos anteriormente en este documento, te permite tener una idea mucho más clara de qué es lo que realmente debes buscar, en lugar de revisar elementos sin una razón o una mentalidad claras.


## Comentarios

¿Tienes **comentarios o sugerencias** sobre este recurso? Puedes utilizar la **función de comentarios que se muestra a continuación** para compartir tus ideas u opiniones con nosotros. Asegúrate de seguir nuestro [código de conducta](../../community/code-of-conduct/index.md). La función de comentarios enlaza directamente con la [sección _Discusiones_ de GitHub](https://github.com/Socialtic/forensics/discussions), donde también puedes **participar directamente en los debates**, si lo prefieres.
