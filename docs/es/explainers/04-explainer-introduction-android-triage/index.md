---

title: Explainer - Introducción al triaje técnico de dispositivos Android
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

Este documento presenta una **introducción al triaje técnico de dispositivos Android**, y explora elementos que una persona debe conocer antes de realizar el triaje técnico de un dispositivo Android, incluyendo el valor de la entrevista inicial, la forma en la que se atacan los dispositivos Android, los artefactos disponibles y las herramientas comunes para el análisis. 

La versión original de este recurso fue desarrollada en idioma inglés, y se tradujo al Español utilizando una herramienta automatizada, con una revisión manual posterior. 

Este material complementario a otros recursos, entre ellos:

* [Explainer: Explorando la herramienta MVT para el triaje técnico de dispositivos Android](../05-explainer-mvt-android-triage/index.md)
* [Tutorial: Uso de MVT para el triaje técnico de dispositivos Android](../../tutorials/02-tutorial-mvt-android-triage/index.md)
* [How-to: Triaje técnico de dispositivos Android utilizando MVT](../../how-tos/06-how-to-triage-android-mvt/index.md) 
* [¿Cómo realizar una extracción mediante AndroidQF?](../../how-tos/04-how-to-extract-with-androidqf/index.md)

## ¿Qué entendemos por triaje técnico de dispositivos Android?

El concepto de triaje se utiliza para describir diferentes partes del [proceso de respuesta a incidentes y análisis forens (DFIR)](../../references/00-glossary/index.md#dfir-digital-forensics-and-incident-response), por lo que conviene detallar a qué nos referimos con este término en el contexto de este recurso y repositorio.

En general, el triaje se refiere a una evaluación inicial rápida y con recursos limitados que se utiliza para decidir si es necesaria una investigación más profunda. El término proviene del [triaje médico](https://es.wikipedia.org/wiki/Triaje): clasificar y priorizar, no diagnosticar. Por ejemplo, la publicación [NIST SP 800-61r3](https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-61r3.pdf) describe el triaje (en el contexto de la validación de reportes de incidentes) como una revisión preliminar para confirmar que se ha producido un incidente y evaluar su gravedad y urgencia.

En el contexto de este recurso y repositorio, ampliamos esta definición de triaje para abarcar dos aspectos:

* **Triaje no técnico:** Que abarca la entrevista inicial, recopilación de contexto y formulación de hipótesis que tiene lugar antes de utilizar las herramientas técnicas. Este paso determina qué se debe buscar en la fase técnica, y es también donde se discute y obtiene el [consentimiento informado](../../references/00-glossary/index.md#consentimiento-informado).
* **Revisión técnica de artefactos:** se refiere a la revisión de [artefactos forenses](../../references/00-glossary/index.md#artefacto-forense) (bugreport, registros de intrusión, extracción de AndroidQF, etc.) para compararlos con IOC conocidos y con patrones o comportamientos sospechosos (TTP). Es importante destacar que, durante esta revisión inicial de artefactos, se buscan indicios de posible actividad maliciosa, con el fin de decidir si es necesario realizar un análisis manual más profundo.

Conviene **diferenciar este triaje técnico de un análisis forense a profundidad**, que suele realizarse mediante una revisión manual y que puede conducir a la identificación de IOC no detectados anteriormente.

Por lo tanto, en el contexto de este repositorio, definimos el **triaje técnico** como *la revisión acotada y basada en hipótesis de los artefactos del dispositivo que están disponibles (bugreport, extracción de AndroidQF, registros de intrusión, etc.) para identificar [indicadores de compromiso](../../references/00-glossary/index.md#indicador-de-compromiso-ioc) o [TTP](../../references/00-glossary/index.md#ttp) que coincidan con vectores de ataque conocidos.*

## ¿Cómo empezar a investigar posibles amenazas en dispositivos Android?

Antes de llevar a cabo un triaje técnico, debes tener acceso a información clave sobre el caso y la solicitud. **Comprender el contexto, la cronología y el historial de las posibles amenazas es fundamental** antes de revisar cualquier evidencia técnica. Esto puede marcar la diferencia entre buscar una aguja en un pajar y llevar a cabo una revisión más intencionada y acotada, guiada por una hipótesis.

Dependiendo de tu rol en la investigación, es posible establecer contacto directo con la persona que solicita apoyo o bien trabajar a través de una organización aliada en territorio. En cualquier caso, en el **análisis forense consentido**, las personas analistas suelen tener acceso a información contextual sobre posibles amenazas, posibles vectores, el historial de amenazas de la persona y el contexto más amplio del caso. **Esta es una de las ventajas clave del análisis forense consentido**, en comparación con los enfoques que se utilizan en otros contextos.

### Recopilación de contexto antes del triaje técnico

La mayor parte de esta información se **recopila durante una entrevistas inicial**, donde se establece contacto con la persona y se le explica el proceso a seguir. La persona no está en la obligación de responder a nuestras preguntas, y cualquier información que se obtenga será con su consentimiento.   

Ten en cuenta también que ser blanco de un ataque de spyware tiene impactos que van más allá del compromiso técnico. El [Estudio sobre los impactos psicosociales del spyware y la Guía para el acompañamiento psicosocial](https://www.acceso.or.cr/psychosocial-impacts-of-spyware/) analizan algunas de estas consecuencias y ofrecen orientación sobre cómo las personas que responden a incidentes pueden incorporar prácticas que conduzcan a un acompañamiento más integral y holístico.

Preparar preguntas orientadoras y documentación puede ser de gran ayuda para asegurarte de que recopilas lo que realmente necesitas. En general, al finalizar estas conversaciones deberías saber:

* ¿Qué ocurrió?
* ¿Cuándo ocurrió? ¿Cuál es la cronología de los hechos?
* ¿Cómo ocurrió?
* ¿Qué dispositivos estuvieron involucrados?
* ¿Qué acciones se han tomado ya?

**Documenta** esta información lo antes posible tras la conversación y asegúrate de que esté disponible para consultarla durante el triaje técnico. Es fácil olvidar detalles relevantes mencionados las llamadas, si estos no se registran a tiempo. 

### ¿Qué hacer cuando no hay indicios claros de que se haya producido una intrusión?

A veces, las personas se ponen en contacto para solicitar una **revisión preventiva o rutinaria de sus dispositivos**, sin ningún indicador específico de actividad maliciosa y sin una razón concreta más allá de su perfil de riesgo. Es una solicitud válida, y sigue siendo posible llevar a cabo una adquisición y ejecutar comprobaciones automatizadas en busca de IOC conocidos. Pero conviene ser **sincero sobre los límites de esta revisión**, ya que solo revelará coincidencias con amenazas *conocidas*, y pensar en examinar todo los rastros de un sistema operativo en busca de señales de actividad maliciosa, sin nada que oriente la búsqueda, resulta complicado y requiere muchos recursos.

### ¿Cómo se lleva a cabo un ataque a un dispositivo Android?

En general, independientemente de las vulnerabilidades específicas que se aprovechen, los atacantes siguen un proceso similar para comprometer los dispositivos y la información almacenada y generada por ellos. Podemos describir esta cadena de ataque del spyware de la siguiente manera:

![Cadena de ataque del spyware: pasos habituales en las infecciones por spyware](../../../en/assets/04-explainer/image1.png"){ loading=lazy }
/// caption
**Imagen 1**. Cadena de ataque del spyware. Adaptado del Grupo de Análisis de Amenazas de Google, [Buying Spying: Perspectivas sobre los proveedores de vigilancia comercial](https://storage.googleapis.com/gweb-uniblog-publish-prod/documents/Buying_Spying_-_Insights_into_Commercial_Surveillance_Vendors_-_TAG_report.pdf).
///


Los pasos pueden describirse de la siguiente manera:

* **Entrega inicial:** se refiere al paso inicial llevado a cabo por un atacante, que puede consistir en el envío de un mensaje de phishing para un ataque de «1 clic», la activación de un proceso a través de una vulnerabilidad de «0 clics» o la interceptación de la red para entregar un paquete malicioso.
* **Explotación:** en esta fase, se ejecuta el paquete entregado inicialmente, lo que explota una o varias vulnerabilidades y permite  la ejecución remota de código, el escape de un sandbox, o la escalación de privilegios.
* **Instalación:** una vez que el paquete consigue escapar el sandbox de la aplicación y obtiene privilegios suficientes, instala el agente de spyware.
* **Recopilación de información:** durante esta fase, el atacante puede recopilar información de interés, incluyendo mensajes, correos electrónicos, historial de navegación, conversaciones a través del micrófono y vídeos o fotos a través de la cámara.
* **Exfiltración:** por último, la información se extrae del dispositivo. Para ello, suele establecerse comunicación con un servidor de comando y control (C2). Este servidor remoto puede enviar comandos y recibir la información recopilada.

Además de comprender los pasos que suelen seguir los atacantes para comprometer un dispositivo, es útil revisar reportes técnicos previos que documenten ataques en contra de la sociedad civil.  Comprender el proceso, las tácticas y las técnicas del atacante puede ayudar a **desarrollar un modelo mental** que ayuda a identificar rastros de actividad sospechosa durante el análisis de artefactos.

A continuación describimos algunos vectores de ataque previamente observados.

#### Compromiso a nivel de cuenta (sin compromiso del dispositivo)

Aunque se trata de un tipo de incidente diferente, a veces un comportamiento malicioso que alguien sospecha que podría ser una infección de su dispositivo (por ejemplo, la exfiltración de datos) puede ser el resultado de una cuenta comprometida, en lugar de un dispositivo comprometido. La vulneración de una cuenta suele ser consecuencia de prácticas y configuraciones de seguridad débiles, como la reutilización de contraseñas o la falta de autenticación multifactorial, pero también puede deberse a ataques avanzados, dirigidos o apoyados por un Estado. 

También cabe mencionar que Google a veces [avisa cuando detecta intentos de comprometer cuentas por parte de atacantes respaldados por gobiernos](https://support.google.com/mail/answer/2591015). Por lo general, estas advertencias están relacionadas con problemas a nivel de cuenta y no son necesariamente indicativas de un intento de atacar un dispositivo. 


#### APK malicioso (a través de la proximidad física)

Esto no requiere una explotación avanzada del dispositivo, ya que se produce cuando los atacantes pueden manipular físicamente el dispositivo para instalar un agente. Un ejemplo de este tipo de ataque fue documentdo por el Citizen Lab en 2024 en su [informe: «Something to Remember Us By»](https://citizenlab.ca/research/device-confiscated-by-russian-authorities-returned-with-monokle-type-spyware-installed/), que revela cómo el software espía fue implantado en el teléfono de un programador ruso luego de ser retenido por las autoridades. 

Se debe resaltar también la [investigación de Amnistía Internacional: «Una prisión digital»: la vigilancia y la represión de la sociedad civil en Serbia](https://securitylab.amnesty.org/latest/2024/12/a-digital-prison-surveillance-and-the-suppression-of-civil-society-in-serbia/ que documenta el uso de /*NoviSpy*, un nuevo programa espía utilizado en Serbia, y que fue instalado mientras los dispositivos se encontraban bajo custodia física de la policía.

#### Explotación de vulnerabilidades

Por lo general, se trata de ataques sofisticados, a menudo ejecutados por Estados, que utilizan herramientas capaces de instalar el *spyware* de diferentes maneras:

* **1 clic:** la víctima tiene que interactuar con algo (un enlace, un mensaje) para que se ejecute el exploit.
* **0 clics:** no se requiere ninguna interacción por parte de la víctima.
* **Manipulación de la red:** los atacantes interceptan o manipulan el tráfico para dirigir a la víctima a sitios maliciosos que pueden aprovechar vulnerabilidades o redirigirla a descargas que infectan el dispositivo.
* **Publicidad dirigida:** en 2026, el [informe de Citizen Lab: Exposing AdFection](https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/) reveló por primera vez cómo los anuncios personalizados pueden convertirse en un canal para el spyware mercenario de cero clics.  

## Rastros comunes en Android

Al hablar de rastros comunes nos referimos a elementos o huellas que permanecen en un dispositivo tras una infección de *spyware*. Constituyen la materia prima para llevar a cabo la evaluación técnica. Comprobar estos rastros, categoría por categoría, evaluándolos contra indicadores conocidos y patrones sospechosos es la principal actividad de un triaje técnico. Algunos rastros comunes incluyen: 

* **Mensajes y enlaces:** suelen ser el primer paso de un ataque, y se utilizan para que la víctima haga clic en un enlace, abra un archivo o instale una aplicación.
* **Historial de navegación:** puede revelar los sitios que una persona visitó o a los que fue redirigida como parte de un ataque, incluso después de que el enlace inicial haya desaparecido de una aplicación de mensajería.
* **Aplicaciones:** pueden ser rastros directos de una intrusión, ya que, dependiendo del tipo de ataque, un agente malicioso podría instalarse como un app.
* **Permisos**: definen lo que una aplicación está realmente autorizada a hacer en un dispositivo, y una discrepancia entre los permisos de una aplicación y su finalidad declarada es una clara señal de uso indebido.
* ***Broadcast Receivers***: permiten que una aplicación detecte eventos del sistema o de otras aplicaciones, y revisarlos puede ayudar a identificar aplicaciones sospechosas. 
* **Servicios de accesibilidad** existen para ayudar a los usuarios con diferencias físicas puedan interactuar con su dispositivo, por ejemplo, leyendo en voz alta el contenido de la pantalla o realizando acciones en nombre del usuario. Ese propósito legítimo requiere amplias capacidades que pueden ser objeto de abuso por parte de aplicaciones maliciosas, como el spyware y el stalkerware. 
* **Configuraciones:** determinados ajustes del dispositivo, cuando se desactivan, eliminan protecciones que, de otro modo, señalarían o bloquearían actividades maliciosas. Comprobar su estado directamente puede revelar si dicha protección se desactivó deliberadamente.
* **Señales de rooting:** el rooting elimina muchas de las protecciones en las que se basa un dispositivo Android de serie. Esto puede ser el resultado de una acción del usuario o también de una actividad maliciosa.
* **Archivos sospechosos:** pueden quedar como rastro de una actividad maliciosa.
* **Fallos del sistema o *crashes*:** pueden indicar un intento fallido de explotación. Las cadenas de explotación suelen ser frágiles y no siempre funcionan, lo que provoca fallos en las aplicaciones. Dado que las diferentes partes de Android fallan de formas distintas, el tipo de fallo indica en qué parte del sistema se produjo el intento. Un proceso que falla repetidamente debe ser revisado. 

### Tabla de referencia de artefactos de Android

**Tabla 1.** Lista de artefactos de Android, su importancia y disponibilidad

| Artefacto | Qué buscar | Disponible en |
| ----- | ----- | ----- |
| Mensajes y enlaces | Enlaces sospechosos; mensajes de ingeniería social que solicitan información, acceso a un enlace, la descarga de un archivo o la instalación de un APK | Copias de seguridad de SMS, copias de seguridad de bases de datos de aplicaciones sin cifrar, Google Takeout, revisión manual de mensajes |
| Historial de navegación | Enlaces sospechosos, redireccionamientos entre sitios web, descargas de archivos | Google Takeout (si se ha activado la sincronización de la navegación), consulta de la base de datos de navegación a través de ADB (si el dispositivo está rooteado), revisión manual en el navegador (si no está rooteado) |
| Aplicaciones | Instaladas desde fuentes sospechosas, con firmas o certificados modificados, permisos extraños, nombres de paquetes extraños o aleatorios | Google Takeout a través del historial de actividad de Google, Bugreport, ADB, AndroidQF |
| Permisos | Funciones sensibles que no se corresponden con la finalidad de una aplicación, como el acceso a la cámara, al micrófono o a la ubicación | bugreport, ADB, AndroidQF |
| Broadcast Receivers | Aplicaciones registradas para recibir difusiones sensibles del sistema. Algunos ejemplos sospechosos son: <br>`android.provider.Telephony.NEW_OUTGOING_SMS`<br>`android.provider.Telephony.SMS_RECEIVED`<br>`android.intent.action.DATA_SMS_RECEIVED`<br>`android.intent.action.PHONE_STATE`<br>`android.intent.action.NEW_OUTGOING_CALL` | bugreport, ADB, AndroidQF |
| Servicios de accesibilidad | Aplicaciones con acceso a la accesibilidad que no tienen una razón legítima para necesitarlo | bugreport, ADB, AndroidQF |
| Configuraciones | Ajustes que desactivan Google Play Protect, el envío de registros de fallos o la confirmación de instalación de ADB. Por ejemplo:<br>**Relacionado con Google Play Protect:** `verifier_verify_adb_installs`, `package_verifier_enable`, `package_verifier_user_consent` (desactiva Google Play Protect), `upload_apk_enable` (desactiva Google Play Protect)<br>**Registros de fallos desactivados:** `send_security_reports`, `samsung_errorlog_agree`, `send_action_app_error`<br>**Confirmación de la instalación de aplicaciones mediante ADB desactivada:** `adb_install_need_confirm` | Informes de errores, ADB, AndroidQF |
| Señales de rooting | Binarios de rooting o aplicaciones de rooting instaladas en el dispositivo, por ejemplo:<br>**Binarios:** `su`, `busybox`, `magisk`<br>**Aplicaciones:** `com.noshufou.android.su` | bugreport, ADB, AndroidQF |
| Archivos sospechosos | Archivos en ubicaciones inusuales, o creados, modificados o con permisos que no se ajustan al uso normal | Informe de error, ADB, AndroidQF |
| Fallos o *crashes*| Fallos de aplicaciones, servicios, procesos o del kernel que pueden indicar un intento fallido de explotación | Bugreport, AndroidQF |

## Herramientas para la evaluación técnica de dispositivos Android

### MVT

[MVT](https://docs.mvt.re/en/latest/) (Mobile Verification Toolkit) es una herramienta que facilita el análisis forense consentido de dispositivos Android e iOS, con el fin de identificar rastros de compromiso. Fue desarrollado y publicado por el Laboratorio de Seguridad de Amnistía Internacional en julio de 2021 en el marco del Proyecto Pegasus, junto con una metodología forense técnica. Su mantenimiento sigue a cargo de Amnistía Internacional y personas y organizaciones aliadas.

Conceptualmente, funciona como un *parser* y un comparador. Toma los datos recopilados de un dispositivo (a través de AndroidQF, un bugreport o registros de intrusión) y los compara con indicadores conocidos de compromiso, al tiempo que **organiza la información para su posterior análisis**. Los resultados del MVT deben revisarse más allá de las alertas iniciales, ya que los diferentes archivos que crea incluyen información relevante sobre los artefactos descritos anteriormente. Los diccionarios de MVT disponibles en la [sección de referencias](../../references/index.md) proporcionan detalles adicionales sobre cada uno de los archivos generados por MVT. El recurso complementario [Guía explicativa: Triaje técnico con MVT](../05-explainer-mvt-android-triage/index.md) profundiza aún más en la lógica y el uso de la herramienta. 

MVT no es una herramienta concluyente en sí misma: **su ejecución, por sí sola, no confirma ni descarta un compromiso de seguridad.** Requiere de un análisis manual y una revisión de sus resultados, pero MVT puede resultar muy útil para detectar aspectos en los cuales profundizar la investigación. 

#### Módulos de MVT para Android

Los siguientes módulos están disponibles para la revisión de artefacts deo Android con MVT: 

* **mvt-android check-androidqf**: permite analizar una extracción realizada con la herramienta AndroidQF utilizando los [módulos para dicha extracción](https://github.com/mvt-project/mvt/tree/main/src/mvt/android/modules/androidqf). Estas extracciones suelen incluir también un bugreport y, si están disponibles, los registros de intrusión. Por lo tanto, el uso del módulo androidqf puede ser suficiente para realizar un análisis de todos los artefactos disponibles, ya que MVT detecta automáticamente estos archivos y también ejecuta los módulos correspondientes.
* **mvt-android check-bugreport**: permite el análisis directo de un bugreport. Si no dispones de una extracción de AndroidQF y deseas realizar un análisis rápido, se recomienda utilizar [este módulo](https://github.com/mvt-project/mvt/tree/main/src/mvt/android/modules/bugreport) como primer paso. Si se detectan indicios de actividad sospechosa, se recomienda complementar este análisis con un análisis completo de una extracción de AndroidQF.
* **mvt-android check-intrusion-logs**: los registros de intrusión solo están disponibles en dispositivos con Android 16 o superior y cuando la persona haya activado previamente el «Modo de protección avanzada» con el registro de intrusiones habilitado. Si dispones de un archivo de registro de intrusiones, es posible analizar este archivo concreto utilizando este comando y el [módulo MVT](https://github.com/mvt-project/mvt/tree/main/src/mvt/android/modules/intrusion_logs) para intrussion logs.

El comando que se utilice dependerá de los artefactos que tengas disponible. Una extracción de AndroidQF suele incluir ya un bugreport y, si se están disponibles, los registros de intrusión, por lo que ejecutar `check-androidqf` analizará la mayor parte de la información obtenida de una sola vez, sin necesidad de ejecutar los demás comandos por separado.

### ALEAPP

[ALEAPP](https://github.com/abrignoni/ALEAPP) (Android Logs Events And Protobuf Parser) es una herramienta de código abierto para analizar y procesar registros de Android, disponible tanto como herramienta de línea de comandos como con interfaz gráfica de usuario. A diferencia de MVT, ALEAPP no se basa en la comparación de artefactos con indicadores de compromiso (IOC) para detectar spyware. Se trata de una herramienta más general que ayuda a reconstruir la actividad del usuario, la cual se presenta posteriormente en un informe HTML.

!!! note "Nota"

    En este repositorio profundizamos específicamente en MVT, ya que es una herramienta desarrollada por la comunidad de análisis forense consentido y es ampliamente utilizada en este ámbito. Ese enfoque no limita la revisión y exploración de otras herramientas, incluidas muchas que no figuran en este documento.

## Conclusión

A través de este recurso hemos explorado aspectos clave a tener en cuenta a la hora de realizar una evaluación técnica de un dispositivo Android, incluida la importancia de la entrevista inicial, una visión general de cómo un dispositivo podría verse comprometido y los diferentes artefactos disponibles. La intención es construir un marco conceptual que pueda utilizarse para llevar a cabo el triaje técnico de un dispositivo Android. Los pasos concretos que se sigan dependerán en gran medida del contexto de cada caso y deben guiarse por una buena entrevista inicial.

Investigar una posible amenaza cuando el contexto no es claro puede resultar muy difícil, ya que podría haber una gran cantidad de información que revisar y recursos limitados para hacerlo. Por eso, **formular hipótesis y establecer objetivos concretos** para la investigación técnica puede marcar la diferencia. En la misma línea, disponer de un **modelo mental de cómo funcionan realmente estos ataques**, incluyendo los pasos que suele seguir un adversario y los vectores descritos  en este documento, permite tener una idea más clara de lo que realmente debes buscar.


## Comentarios

¿Tienes **comentarios o sugerencias** sobre este recurso? Puedes utilizar la **función de comentarios que se muestra a continuación** para compartir tus ideas u opiniones con nosotros. Asegúrate de seguir nuestro [código de conducta](../../community/code-of-conduct/index.md). La función de comentarios enlaza directamente con la [sección _Discusiones_ de GitHub](https://github.com/Socialtic/forensics/discussions), donde también puedes **participar directamente en los debates**, si lo prefieres.
