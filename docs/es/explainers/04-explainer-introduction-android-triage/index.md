---

title: Explainer: Introducción al triaje técnico de dispositivos Android
summary: Conceptos, consideraciones y artefactos útiles antes de realizar el triaje técnico de un dispositivo Android
keywords: triaje, android, mvt, artefactos, dfir
lang: es
tags: [explainer, android, intro]
last_updated: 2026-11-04
some_url:
created: 2026-11-04
comments: true
author:
    name: Daniel
    url: https://socialtic.org/quienes-somos/
    description: SocialTIC
translation-review-pending: false
auto-translate: false

---

# Explainer: Introducción al triaje técnico de dispositivos Android

Este documento forma **parte de un repositorio de documentación técnica** que tiene como objetivo establecer una base de conocimientos probados, flexibles y accesibles para **impulsar el análisis forense consentido en beneficio de la sociedad civil**. Para organizar los contenidos, se utiliza el [marco de referencia de documentación técnica Diataxis](../../references/00-glossary/index.md#diataxis). Este recurso en particular se clasifica como un [explainer](../index.md) y es complementario a otros recursos de este repositorio, entre ellos [guías how-to](../../how-tos/index.md), [tutoriales](../../tutorials/index.md) y [referencias](../../references/index.md).

Este documento presenta una introducción al triaje técnico de dispositivos Android, y explora consideraciones que una persona debe conocer antes de realizar el triaje técnico de un dispositivo Android, incluyendo el valor de la entrevista inicial, la forma en la que se atacan los dispositivos Android, los artefactos disponibles y las herramientas comunes. 

La versión original de este recurso fue desarrollada en idioma inglés, y se realizó una traducción automática al español que fue revisada manualmente. 

Este material complementario a otros recursos, entre ellos:

* [Explainer: Explorando la herramienta MVT para el triaje técnico de dispositivos Android](../05-explainer-mvt-android-triage/index.md)
* [Tutorial: Uso de MVT para el triaje técnico de dispositivos Android](../../tutorials/02-tutorial-mvt-android-triage/index.md)
* [How-to: Triaje técnico de dispositivos Android utilizando MVT](https://forensics.socialtic.org/en/how-tos/06-how-to-triage-android-mvt/) (disponible en inglés)
* [¿Cómo realizar una extracción mediante AndroidQF?](../../how-tos/04-how-to-extract-with-androidqf/index.md)

## ¿Qué entendemos por triaje técnico de dispositivos Android?

El concepto de triaje se utiliza para describir diferentes partes del [proceso de respuesta a incidentes y análisis forens (DFIR)](../../references/00-glossary/index.md#dfir-digital-forensics-and-incident-response), por lo que conviene detallar a qué nos referimos con este término en el contexto de este recurso y repositorio.

En general, el triaje se refiere a una evaluación inicial rápida y con recursos limitados que se utiliza para decidir si es necesaria una investigación más profunda, y en qué centrarla. El término proviene del triaje médico: clasificar y priorizar, no diagnosticar. Por ejemplo, la publicación [NIST SP 800-61r3](https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-61r3.pdf) describe el triaje (en el contexto de la validación de reportes de incidentes) como una revisión preliminar para confirmar que se ha producido un incidente y evaluar su gravedad y urgencia.

En el contexto de este recurso y repositorio, ampliamos esta definición de triaje para abarcar dos aspectos:

* **Triaje no técnico:** Centrado especialmente en la entrevista inicial, recopilación de contexto y formulación de hipótesis que tiene lugar antes de utilizar las herramientas técnicas. Este paso determina qué se debe buscar realmente en la fase técnica, y es también donde se discute y obtiene el [consentimiento informado](../../how-tos/01-how-to-obtain-informed-consent/index.md).
* **Revisión técnica de artefactos:** se refiere al uso de la información adquirida (bugreport, registros de intrusión, extracción de AndroidQF, etc.) para compararla con IOC conocidos y con patrones o comportamientos sospechosos (TTP). Es importante destacar que, durante esta revisión inicial de artefactos, se buscan indicios de posible actividad maliciosa, con el fin de decidir si es necesario realizar un análisis manual más profundo.

Conviene **diferenciar este triaje técnico de un análisis forense más profundo**, que suele realizarse mediante revisión manual y que puede conducir a la identificación de IOC no detectados anteriormente.

Por lo tanto, en el contexto de este repositorio, definimos el **triaje técnico** como *la revisión acotada y basada en hipótesis de los artefactos del dispositivo que están fácilmente disponibles (bugreport, extracción de AndroidQF, registros de intrusión, etc.) para identificar [indicadores de compromiso](../../references/00-glossary/index.md#indicador-de-compromiso-ioc) o [TTP](../../references/00-glossary/index.md#ttp) coherentes con vectores de ataque conocidos.*

## ¿Cómo empezar a investigar posibles amenazas en dispositivos Android?

Antes de llevar a cabo un triaje técnico, debes tener acceso a información clave sobre el caso y la solicitud. **Comprender el contexto, la cronología y el historial de las posibles amenazas es fundamental** antes de revisar cualquier evidencia técnica. Esto puede marcar la diferencia entre buscar una aguja en un pajar y llevar a cabo una revisión más intencionada y acotada, guiada por hipótesis.

Dependiendo de tu rol en la investigación, es posible que tengas contacto directo con la persona que solicita apoyo o que trabajes a través de una organización aliada en territorio. En cualquier caso, en el **análisis forense consentido**, las personas analistas suelen tener acceso a información contextual sobre posibles amenazas, posibles vectores, el historial de amenazas de la persona y el contexto más amplio del caso. **Esta es una de las ventajas clave del análisis forense consentido**, en comparación con los enfoques adversariales que se utilizan en otros contextos.

### Recopilación de contexto antes del triaje técnico

La mayor parte de esta información se **recopila durante las entrevistas y conversaciones** cuando se recibe el caso por primera vez. Como en cualquier conversación relacionada con una posible amenaza, ten siempre presente el [consentimiento](../../how-tos/01-how-to-obtain-informed-consent/index.md): esta información solo está disponible porque la persona decidió compartirla, y **la forma de preguntar es tan importante como lo que se pregunta**.

Ten en cuenta también que ser blanco de un ataque de spyware tiene impactos que van más allá del compromiso técnico. El [Estudio sobre los impactos psicosociales del spyware y la Guía para el acompañamiento psicosocial](https://www.acceso.or.cr/psychosocial-impacts-of-spyware/) analizan algunas de estas consecuencias y ofrecen orientación sobre cómo las personas que responden a incidentes pueden incorporar prácticas que conduzcan a un acompañamiento más integral y holístico.

Preparar preguntas orientadoras y documentación puede ser de gran ayuda para asegurarte de que recopilas lo que realmente necesitas. En general, al finalizar estas conversaciones deberías saber:

* ¿Qué ocurrió?
* ¿Cuándo ocurrió? ¿Cuál es la cronología de los hechos?
* ¿Cómo ocurrió?
* ¿Qué dispositivos estuvieron involucrados?
* ¿Qué acciones se han tomado ya?

**Documenta** esta información lo antes posible tras la conversación y asegúrate de que esté disponible para consultarla durante el triaje técnico. Es fácil perder de vista un detalle mencionado en una llamada inicial cuando ya llevas varias fases de revisión de artefactos.

### ¿Qué hacer cuando no hay indicios claros de compromiso?

A veces, las personas se ponen en contacto para solicitar una **revisión preventiva o rutinaria de sus dispositivos**, sin ningún indicador específico de actividad maliciosa y sin una razón concreta más allá de su perfil de riesgo. Se trata de una solicitud válida, y sigue siendo posible realizar una adquisición y ejecutar revisiones automatizadas en busca de IOC conocidos. Pero conviene ser **transparente sobre los límites de esta revisión**, ya que solo sacará a la luz amenazas *conocidas*, y examinar todo un sistema operativo en busca de rastros de actividad maliciosa, sin nada que acote la búsqueda, resulta complicado y requiere muchos recursos.

### ¿Cómo se comprometen los dispositivos Android?

En general, independientemente de las vulnerabilidades específicas que se aprovechen, los atacantes siguen un proceso similar para comprometer los dispositivos y la información almacenada y generada en ellos. Podemos describir esta cadena de ataque (kill chain) del spyware de la siguiente manera:

![Cadena de ataque del spyware: pasos habituales en las infecciones por spyware](../../../assets/04-explainer/spyware-kill-chain.png "imagen 1"){ loading=lazy }
/// caption
**Imagen 1**. Cadena de ataque del spyware. Adaptado de Google Threat Analysis Group, [Buying Spying: Insights into Commercial Surveillance Vendors](https://storage.googleapis.com/gweb-uniblog-publish-prod/documents/Buying_Spying_-_Insights_into_Commercial_Surveillance_Vendors_-_TAG_report.pdf) (en inglés).
///

Los pasos pueden describirse de la siguiente manera:

* **Entrega inicial:** se refiere al paso inicial que lleva a cabo un atacante, que puede consistir en el envío de un mensaje de phishing para un ataque de 1 clic, la activación de un proceso a través de una vulnerabilidad de 0 clics o la interceptación de la red para entregar un paquete malicioso.
* **Explotación:** en esta fase se ejecuta el paquete entregado inicialmente, lo que puede dar lugar a la ejecución remota de código, el escape del sandbox o la escalada local de privilegios.
* **Instalación:** una vez que el paquete consigue escapar del sandbox de la aplicación y obtiene privilegios suficientes, instala el agente de spyware.
* **Recopilación de información:** durante esta fase, el atacante puede recopilar información de interés, como mensajes, correos electrónicos, historial de navegación, conversaciones a través del micrófono y videos o fotos a través de la cámara.
* **Exfiltración:** por último, la información se exfiltra del dispositivo. Para ello, suele establecerse comunicación con un servidor de comando y control (C2). Este servidor remoto puede enviar comandos y recibir la información recopilada.

Además de comprender los pasos que suelen seguir los atacantes para comprometer un dispositivo, resulta útil analizar específicamente los dispositivos Android y los reportes históricos de ataques contra la sociedad civil. Comprender el proceso, las tácticas y las técnicas del atacante puede ayudar a **desarrollar un modelo mental de qué rastros hay que buscar** al examinar la evidencia. Buscar cualquier cosa *inusual* puede ser una tarea complicada, sobre todo si buscamos en todas partes y en todas las fechas, sin tener claro qué rastros concretos estamos buscando.

A continuación describimos algunos vectores de ataque que pueden utilizarse para obtener acceso a un dispositivo Android.

#### Compromiso a nivel de cuenta (sin compromiso del dispositivo)

Aunque se trata de un tipo de incidente diferente, a veces un comportamiento malicioso que alguien sospecha que podría ser una infección de su dispositivo, por ejemplo la exfiltración de datos, puede ser en realidad el resultado de una cuenta comprometida y no de un dispositivo comprometido. El compromiso de una cuenta suele ser consecuencia de prácticas y configuraciones de seguridad deficientes, como la reutilización de contraseñas o la falta de autenticación multifactor, pero también puede deberse a ataques avanzados, dirigidos o patrocinados por un Estado.

También cabe mencionar que Google a veces envía [alertas cuando detecta intentos de comprometer cuentas por parte de atacantes respaldados por gobiernos](https://support.google.com/mail/answer/2591015). Por lo general, estas alertas están relacionadas con la cuenta y no indican necesariamente un intento de atacar un dispositivo.

#### APK malicioso (a través de acceso físico)

Esto no requiere una explotación avanzada del dispositivo, ya que se produce cuando los atacantes pueden manipular físicamente el dispositivo para instalar un agente. Actores patrocinados por Estados han utilizado esta técnica, tal y como documentó Citizen Lab en 2024 en su [reporte «Something to Remember Us By»](https://citizenlab.ca/research/device-confiscated-by-russian-authorities-returned-with-monokle-type-spyware-installed/) (en inglés), sobre un teléfono que fue devuelto a un programador ruso tras su liberación con spyware instalado de forma encubierta.

Cabe destacar también la investigación de Amnistía Internacional [«Una prisión digital»: vigilancia y represión de la sociedad civil en Serbia](https://securitylab.amnesty.org/latest/2024/12/a-digital-prison-surveillance-and-the-suppression-of-civil-society-in-serbia/), que documenta el uso de *NoviSpy*, un nuevo spyware instalado mientras los dispositivos se encontraban bajo custodia de la policía, y que permite capturar datos personales sensibles del teléfono de la persona afectada.

#### Explotación de vulnerabilidades

Por lo general, se trata de ataques muy dirigidos, a menudo patrocinados por Estados, que utilizan distintos vectores para instalar un agente de spyware en el dispositivo:

* **1 clic:** la persona objetivo tiene que interactuar con algo (un enlace, un mensaje) para que se ejecute el exploit.
* **0 clics:** no se requiere ninguna interacción por parte de la persona objetivo.
* **Manipulación de la red:** los atacantes interceptan o manipulan el tráfico para dirigir a la persona objetivo a sitios maliciosos que pueden aprovechar vulnerabilidades, o redirigirla a descargas que infectan el dispositivo.
* **Publicidad dirigida:** en 2026, el [reporte de Citizen Lab «Exposing AdFection»](https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/) (en inglés) reveló por primera vez cómo los anuncios dirigidos pueden convertirse en un canal para spyware mercenario de 0 clics.

## Artefactos comunes en Android

Los artefactos comunes son los elementos o rastros que permanecen en un dispositivo tras una infección por malware. Constituyen la materia prima para llevar a cabo el triaje técnico. Revisar estos rastros, categoría por categoría, contrastándolos con indicadores conocidos y patrones sospechosos (a partir de lo obtenido en la entrevista) es la forma en que se realiza el triaje.

* **Mensajes y enlaces:** suelen ser el primer paso de un ataque, y se utilizan para que la persona objetivo haga clic en un enlace, abra un archivo o instale una aplicación.
* **Historial de navegación:** puede revelar los sitios que una persona visitó o a los que fue redirigida como parte de un ataque, incluso después de que el enlace inicial haya desaparecido de una aplicación de mensajería.
* **Aplicaciones:** pueden ser uno de los rastros más directos de un compromiso ya que, dependiendo del tipo de ataque, un agente malicioso podría instalarse como una aplicación.
* **Permisos:** definen lo que una aplicación está realmente autorizada a hacer en un dispositivo, y una discrepancia entre los permisos de una aplicación y su finalidad declarada es una clara señal de uso indebido.
* **Receptores de difusión generales (broadcast receivers):** permiten que una aplicación detecte eventos del sistema o de otras aplicaciones, y revisarlos puede ayudar a identificar aplicaciones en posición de acceder a información sensible.
* **Servicios de accesibilidad:** existen para ayudar a las personas con discapacidad a interactuar con su dispositivo, por ejemplo, leyendo en voz alta el contenido de la pantalla o realizando acciones en su nombre. Ese propósito legítimo requiere amplias capacidades que pueden ser objeto de abuso por parte de aplicaciones maliciosas, como el spyware y el stalkerware.
* **Configuraciones:** determinados ajustes del dispositivo, cuando se desactivan, eliminan protecciones que de otro modo señalarían o bloquearían actividades maliciosas. Revisar su estado directamente puede revelar si dicha protección se desactivó deliberadamente.
* **Señales de rooteo:** el rooteo elimina muchas de las protecciones en las que se basa un dispositivo Android de fábrica. Esto puede ser el resultado de una acción de la persona usuaria o de una actividad maliciosa.
* **Archivos sospechosos:** pueden quedar como rastro de una actividad maliciosa. Pueden ser diferentes tipos de archivos, como cargas maliciosas (payloads), datos o registros.
* **Fallos (crashes):** pueden indicar un intento fallido de explotación. Las cadenas de explotación suelen ser frágiles y no siempre funcionan, lo que provoca fallos en las aplicaciones. Dado que las diferentes partes de Android fallan de formas distintas, el tipo de fallo indica en qué parte del sistema se produjo el intento. Merece la pena investigar más a fondo un proceso que falla repetidamente o que falla en torno a un evento sospechoso.

### Tabla de referencia de artefactos de Android

**Tabla 1.** Lista de artefactos de Android, su importancia y disponibilidad

| Artefacto | Qué buscar | Disponible en |
| ----- | ----- | ----- |
| Mensajes y enlaces | Enlaces sospechosos; mensajes de ingeniería social que solicitan información, acceso a un enlace, la descarga de un archivo o la instalación de un APK | Respaldos de SMS, respaldos de bases de datos de aplicaciones sin cifrar, Google Takeout, revisión manual de mensajes |
| Historial de navegación | Enlaces sospechosos, redirecciones entre sitios web, descargas de archivos | Google Takeout (si se activó la sincronización de la navegación), base de datos de navegación a través de ADB (si el dispositivo está rooteado), revisión manual en el navegador (si no está rooteado) |
| Aplicaciones | Instaladas desde fuentes sospechosas, con firmas o certificados modificados, permisos extraños, nombres de paquetes extraños o aleatorios | Google Takeout a través del historial de actividad de Google, bugreport, ADB, AndroidQF |
| Permisos | Funciones sensibles que no se corresponden con la finalidad declarada de una aplicación, como el acceso a la cámara, al micrófono o a la ubicación | Bugreport, ADB, AndroidQF |
| Receptores de difusión generales | Aplicaciones registradas para recibir difusiones sensibles del sistema o de telefonía. Algunos ejemplos sospechosos son: <br>`android.provider.Telephony.NEW_OUTGOING_SMS`<br>`android.provider.Telephony.SMS_RECEIVED`<br>`android.intent.action.DATA_SMS_RECEIVED`<br>`android.intent.action.PHONE_STATE`<br>`android.intent.action.NEW_OUTGOING_CALL` | Bugreport, ADB, AndroidQF |
| Servicios de accesibilidad | Aplicaciones con permisos de accesibilidad que no tienen una razón legítima para necesitarlos | Bugreport, ADB, AndroidQF |
| Configuraciones | Ajustes que desactivan Google Play Protect, el envío de registros de fallos o la confirmación de instalaciones mediante ADB. Por ejemplo:<br>**Relacionados con Google Play Protect:** `verifier_verify_adb_installs`, `package_verifier_enable`, `package_verifier_user_consent` (desactiva Google Play Protect), `upload_apk_enable` (desactiva Google Play Protect)<br>**Registros de fallos desactivados:** `send_security_reports`, `samsung_errorlog_agree`, `send_action_app_error`<br>**Confirmación de instalación de aplicaciones mediante ADB desactivada:** `adb_install_need_confirm` | Bugreport, ADB, AndroidQF |
| Señales de rooteo | Binarios o aplicaciones de rooteo instalados en el dispositivo, por ejemplo:<br>**Binarios:** `su`, `busybox`, `magisk`<br>**Aplicaciones:** `com.noshufou.android.su` | Bugreport, ADB, AndroidQF |
| Archivos sospechosos | Archivos en ubicaciones inusuales, o creados, modificados o con permisos que no se ajustan al uso normal | Bugreport, ADB, AndroidQF |
| Fallos | Fallos de aplicaciones, servicios, procesos o del kernel que pueden indicar un intento fallido de explotación | Bugreport, AndroidQF |

## Herramientas para el triaje técnico de dispositivos Android

### MVT

[MVT](https://docs.mvt.re/en/latest/) (Mobile Verification Toolkit) es una herramienta que facilita el análisis forense consentido de dispositivos Android e iOS, con el fin de identificar rastros de compromiso. Fue desarrollada y publicada por el Laboratorio de Seguridad de Amnistía Internacional en julio de 2021 en el marco del Proyecto Pegasus, junto con una metodología forense técnica. Su mantenimiento sigue a cargo de Amnistía Internacional y otras personas colaboradoras.

Conceptualmente, funciona como un analizador (parser) y un comparador. Toma los datos recopilados de un dispositivo (a través de AndroidQF, un bugreport o registros de intrusión) y los compara con indicadores de compromiso conocidos, al tiempo que **facilita la revisión de la propia información procesada**. Los resultados de MVT deben revisarse más allá de las advertencias iniciales, ya que los diferentes archivos que genera incluyen información relevante sobre los artefactos descritos anteriormente. Los diccionarios de MVT disponibles en la [sección de referencias](../../references/index.md) proporcionan detalles adicionales sobre cada uno de los archivos generados por MVT, y el [Explainer: Explorando la herramienta MVT para el triaje técnico de dispositivos Android](../05-explainer-mvt-android-triage/index.md) profundiza en la lógica y el uso de la herramienta.

Ten en cuenta que MVT no es una solución mágica: **ejecutarla, por sí sola, no confirma ni descarta un compromiso.** Requiere un análisis manual y una revisión de sus resultados, pero MVT puede resultar útil para detectar aspectos que merecen ser investigados.

#### Módulos de MVT para Android

Es útil saber qué módulos están disponibles para cada comando, ya que el que corresponda dependerá de los datos con los que cuentes:

* **mvt-android check-androidqf**: permite analizar una extracción realizada con la herramienta AndroidQF utilizando los [módulos para dicha extracción](https://github.com/mvt-project/mvt/tree/main/src/mvt/android/modules/androidqf). Estas extracciones suelen incluir también un bugreport y, si están disponibles, los registros de intrusión. Por lo tanto, utilizar el módulo de androidqf puede ser suficiente para realizar un análisis de todos los artefactos disponibles, ya que MVT detecta automáticamente estos archivos y ejecuta también los [módulos correspondientes a bugreport](https://github.com/mvt-project/mvt/tree/main/src/mvt/android/modules/bugreport) y los [módulos correspondientes a backup](https://github.com/mvt-project/mvt/tree/main/src/mvt/android/modules/backup).
* **mvt-android check-bugreport**: permite el análisis directo de un bugreport. Si no cuentas con una extracción de AndroidQF y buscas un análisis rápido, se recomienda utilizar este módulo como primer paso. Si se identifican indicios de actividad sospechosa, se recomienda complementarlo con el análisis completo de una extracción de AndroidQF.
* **mvt-android check-intrusion-logs**: los registros de intrusión (intrusion logs) solo están disponibles en dispositivos con Android 16 o superior y cuando la persona activó previamente el Modo de Protección Avanzada con el registro de intrusiones habilitado. Si cuentas con un archivo de registro de intrusiones, es posible analizar este archivo específico utilizando este comando y módulo de MVT.

El comando a utilizar depende de lo que tengas disponible. Una extracción de AndroidQF suele incluir ya un bugreport y, si se recopilaron, los registros de intrusión, por lo que ejecutar `check-androidqf` sobre ella analizará la mayor parte de la información adquirida de una sola vez, sin necesidad de ejecutar los demás comandos por separado.

### ALEAPP

[ALEAPP](https://github.com/abrignoni/ALEAPP) (Android Logs Events And Protobuf Parser) es una herramienta de código abierto para procesar y analizar registros de Android, disponible como herramienta de línea de comandos y con interfaz gráfica. A diferencia de MVT, ALEAPP no se basa en la comparación de artefactos con indicadores de compromiso (IOC) de spyware. Se trata de una herramienta más general que ayuda a reconstruir la actividad del dispositivo, que se presenta posteriormente en un reporte HTML.

!!! note "Nota"

    En este repositorio profundizamos específicamente en MVT, ya que es una herramienta comunitaria construida en torno al análisis consentido y es ampliamente utilizada en este ámbito. Ese enfoque no debería desanimarte a explorar otras herramientas, incluidas muchas que no figuran en esta lista.

## Conclusión

A través de este recurso exploramos aspectos clave a tener en cuenta al realizar el triaje técnico de un dispositivo Android, incluida la importancia de la entrevista inicial, una visión general de cómo un dispositivo podría verse comprometido y los diferentes artefactos disponibles. La intención es construir un marco conceptual que pueda utilizarse para llevar a cabo el triaje técnico de un dispositivo Android. Los pasos concretos que sigas dependerán en gran medida del contexto de cada caso y deben guiarse por la entrevista inicial descrita anteriormente en este documento.

Investigar una posible amenaza cuando ese contexto no está claro puede resultar muy difícil, ya que puede haber una gran cantidad de información que revisar y recursos limitados para hacerlo. Por eso, formular hipótesis y establecer objetivos concretos para la investigación técnica puede marcar la diferencia. En la misma línea, contar con un **modelo mental de cómo funcionan realmente estos ataques**, incluyendo los pasos que suele seguir un adversario y los vectores descritos anteriormente en este documento, te permite tener una idea mucho más clara de qué buscar realmente, en lugar de revisar artefactos sin una razón o un enfoque claros.


## Comentarios

¿Tienes **comentarios o sugerencias** sobre este recurso? Puedes utilizar la **función de comentarios que se muestra a continuación** para compartir tus ideas u opiniones con nosotros. Asegúrate de seguir nuestro [código de conducta](../../community/code-of-conduct/index.md). La función de comentarios enlaza directamente con la [sección _Discussions_ de GitHub](https://github.com/Socialtic/forensics/discussions), donde también puedes **participar directamente en las discusiones**, si lo prefieres.
