---
title: Glosario 
summary: Glosario 
keywords: glosario
lang: es
tags: [glossary, glosario, reference]
last_updated: 2025-08-04
some_url:
created: 2025-08-04
author:
    name: Daniel
    url: https://socialtic.org/quienes-somos/
    description: SocialTIC
alternate: 
    en: en/references/00-glossary.html
auto-translate: true
---


# Glosario

Este documento forma **parte de un repositorio de documentación técnica** que tiene como objetivo establecer una base de conocimientos probados, flexibles y accesibles para **impulsar el análisis forense consentido en beneficio de la sociedad civil**.

Este recurso en particular es un glosario de términos que incluye **conceptos, abreviaciones y otros términos** que se consideran de importancia para la comprensión de los contenidos. Se organizan en orden alfabético. 

## Términos

### ADB

ADB hace referencia a *Android Debug Bridge*, o puente de depuración de Android. ADB es una **herramienta de línea de comandos** **que permite comunicarse directamente a través de USB con un dispositivo Android**, e iniciar diferentes acciones y comandos.  

Desde el punto de vista de **forense digital**, y en particular al hacer [investigaciones basadas en logs](../../explainers/03-explainer-log-forensics-android/) utilizando herramientas como AndroidQF, **ADB permite establecer una comunicación directa con un dispositivo**. Es útil en situaciones donde **se tiene acceso físico al dispositivo**, y cuando se desea obtener información directamente desde el equipo a través de **comandos nativos**, sin utilizar herramientas adicionales. 


### Adquisición

Se refiere a una etapa de investigación forense, la persona analista forense debe determinar la mejor forma de recolectar la evidencia forense, y aplicar los procedimientos necesarios para extraer los artefactos forenses.


### Análisis de riesgos

Los riesgos particulares que una organización o individuo enfrenta, **dependen del contexto y de su trabajo particular**. Al proceso de identificar vulnerabilidades, riesgos y amenazas en un momento determinado se le conoce como análisis de riesgos. 

### AndroidQF

[AndroidQF](https://github.com/mvt-project/androidqf) es una herramienta de software libre y de código abierto **enfocada en la extracción forense de dispositivos Android**. Actualmente mantenida por el [Laboratorio de Seguridad de Amnistía Internacional](https://securitylab.amnesty.org/es/). 

Su enfoque está pensado especialmente para periodistas, activistas, defensores de derechos humanos y los **laboratorios técnicos que acompañan casos de vigilancia digital y amenazas de software espía.**

### APK

De acuerdo a Wikipedia, un [APK](https://es.wikipedia.org/wiki/APK_(formato)) es un archivo con extensión .apk (Android Application Package, significado en español: Paquete de Aplicación Android) es un paquete para el sistema operativo Android. Este formato es una variante del formato JAR de Java y se usa para distribuir e instalar componentes empaquetados para la plataforma Android para teléfonos inteligentes y tabletas 

### Artefacto forense

Un artefacto forense se refiere a la evidencia o los datos recuperados durante el análisis forense digital, lo incluye arhivos, registros de procesos, logs, metadatos, etc. 

### Binario

Los binarios de software hacen referencia a archivos que contienen únicamente código binario precompilado, es decir instrucciones que solo son legibles por la máquina y **ya están listos para ejecutarse.** Ejemplos incluyen archivos con la extensión ```.bin```, ```.exe``` o ```.app```.

### Bugreport

Es una herramienta nativa de línea de comandos en Android, disponible desde la interfaz gráfica o desde el shell de ADB. Permite generar un informe de errores que contiene logs de diagnóstico, generados a partir de el llamado a logcat, dumsptate y dumpsys. Se genera dentro de un archivo .zip y está compuesto de una estructura de carpetas con información sobre errores, uso de memoria, llamados al sistema, información de red, información del dispositivo, entre otros.

### Cadena de custodia

Al proceso de documentar con claridad quién y de qué forma se manipula  la evidencia se le conoce como **cadena de custodia**. La evidencia forense puede ser manipulada o destruída durante el proceso forense, por lo que la persona analista debe ser capaz de demostrar la [integridad de la evidencia](https://www.ibm.com/es-es/topics/data-integrity).  En caso de que esta demostración no sea posible o suficientemente robusta, es posible que las evidencia **no sea admisible en procesos judiciales**, o sea refutada y desestimada por otros especialistas.

### Consentimiento informado

El [consentimiento](https://es.wikipedia.org/wiki/Consentimiento) es un principio que hace referencia a la exteriorización de la voluntad entre dos o más personas para aceptar derechos y obligaciones. En el contexto de análisis forense digital en beneficio de personas de la sociedad civil, el consentimiento informado se refiere al **acuerdo y aprobación de acciones para facilitar la recolección, análisis, presentación y preservación de evidencia digital**. 

Un aspecto clave en cualquier acuerdo de consentimiento es la capacidad de quién acepta el acuerdo de tomar una **decisión informada** sobre el curso de la investigación, e incluso poder rechazar la asistencia. En la práctica forense, esto significa brindar toda la información necesaria para que quién solicita el análisis comprenda las acciones, riesgos, derechos y obligaciones que conlleva el proceso de investigación. Es importante que la **persona analista se comunique de forma clara y transparente**, y respete la voluntad de quién solicita el apoyo. 

### Copia bit a bit

Copia bit a bit, DD o duplicación de disco se refiere al proceso de crear una réplica exacta de un medio electrónico. Permiten proteger la evidencia original, de forma tal que se proteja su integridad y se preserve en apego a mejores prácticas. 

### CVE

Es un programa de reporte, clasificación y publicación de vulnerabilidades de seguridad. Se establecen registros CVE únicos para cada vulnerabilidad, como por ejemplo ```CVE-2014-0160```

### Diátaxis

[Diátaxis](https://diataxis.fr/start-here/) es un marco de referencia para la escritura y organización de documentación técnica. Cómo principio clave, trata de agrupar la documentación en 4 diferentes categorías:  **Explainers**,  **Guías how-to**, **Tutoriales** y **Referencias**; que a su vez responden a necesidades concretas de la persona lectora. Cada tipo de material tiene un propósito y un estilo diferente. 

### DFIR (Digital Forensics and Incident Response)

Sus siglas en Inglés hacen referencia a la combinación y unificación de los procedimientos de respuesta a incidentes y análisis forense. Se pretende que durante la respuesta a un incidente se consideren mejores prácticas para la recolección y preservación de evidencia, y se utilicen hallazgos producto del análisis forense para contener y erradicar amenazas, y, ultimadamente, se prevengan futuros incidentes.

### Exploit

[Exploit](https://es.wikipedia.org/wiki/Exploit) es una palabra inglesa que significa explotar o aprovechar, y que en el ámbito de la informática es un fragmento de software, fragmento de datos o secuencia de comandos o acciones, utilizada con el fin de aprovechar una vulnerabilidad de seguridad de un sistema de información para conseguir un comportamiento no deseado del mismo.
​

### Forense digital

La forense digital es el proceso utilizado para la recolección, preservación, análisis y presentación de evidencia digital derivada de medios y dispositivos electrónicos, utilizando **técnicas de investigación y métodos científicos** que sean fiables, acertados y repetibles, de forma tal que los resultados puedan ser utilizados en **procedimientos judiciales**.[1](https://csrc.nist.gov/glossary/term/digital_forensics)

La forense digital se utiliza para descubrir y examinar datos de dispositivos electrónicos con el objetivo de **identificar, recuperar, documentar e interpretar la información** digital y su conexión con [ataques digitales](https://protege.la/ataques/). La utilización de procedimientos estándar, en apego a mejores prácticas, **permite generar evidencia útil** que impulse acciones de **rendición de cuentas**, que pueda reducir la impunidad con la que se ejecutan ataques digitales.


### Google Takeout

Es una función para cuentas en línea de Google que permite extraer información de diferentes aplicaciones, registros de acceso, logs de seguridad, correo electrónico, entre otros. El proceso tarda algunos días en completarse. 

 [Sige este enlace para acceder a la función e inicar un takeout request.](https://takeout.google.com/?pli=1).  


### Guerra legal (lawfare)

Guerra legal o lawfare se refiere al uso del sistema o instituciones legales para dañar, desacreditar o afectar individuos o organizaciones. Por ejemplo, en relación al caso en las cortes de Estados Unidos entre NSO y WhatsApp, el Citizen Lab enfrentó una serie de recursos y solicitudes legales que buscaban desmantelar su trabajo y acceder a información sensible, incluída la lista de víctimas. En otro ejemplo, en 2018 la empresa Candiense Sandvine amenazó al Citizen Lab con una demanda por difamación a raíz de su publicación concerniente al uso de equipos Sandvine para la implantación de spyware.  

### Hash

[Hash](https://es.wikipedia.org/wiki/Funci%C3%B3n_hash) son  funciones de criptográficas, que permiten producir un único valor para un conjunto de datos dados. Ejemplos incluyen MD5, SHA1. 

### Herramienta portable

Hace referencia a una herramienta de software que no requiere ser instalada para su ejecución. La herramienta no modifica ni agrega archivos al sistema, sino que incluye todos los archivos que necesita para ejecutarse dentro de su misma carpeta o binario de ejecución. 

Una de las ventajas de este tipo de programas es que deja menos rastros sobre su ejecución, en comparación con programas que deben ser instalados.

### Identificación

Se refiere a una etapa de investigación forense, donde la persona analista determina **cuáles dispositivos, cuentas o sistemas podrían contener información relevante para la investigación**. Ejemplos de dispositivos incluyen teléfonos móviles, computadoras, cuentas en línea, medios de almacenamiento, entre otros. Idealmente, para determinar la evidencia a recolectar, la persona analista debe tener contacto con la persona impactada, para entender qué sucedió, qué acciones se han tomado hasta el momento y qué evidencia podría estar disponible.

### Indicador de compromiso (IOC)

[Un indicador de compromiso o IDC](https://es.wikipedia.org/wiki/Indicador_de_compromiso) (en inglés: indicator of compromise, IoC) es toda aquella información relevante que describe cualquier incidente de ciberseguridad, actividad y/o artefacto malicioso, mediante el análisis de sus patrones de comportamiento.[1]​ La intención de un indicador de compromiso es esquematizar la información que se recibe o se extrae durante el análisis de un incidente, de tal manera que pueda reutilizarse por otros investigadores o afectados, para descubrir la misma evidencia en sus sistemas y llegar a determinar si han sido o no comprometidos ya sea desde el punto de vista de monitorización frente a amenazas o por análisis forense.[2]​ Por ejemplo, se identifican ficheros creados, entradas de registro modificadas, procesos o servicios nuevos. La idea subyacente es que, si se analiza un sistema y se encuentran los detalles recogidos en un indicador de compromiso concreto, se está ante una infección provocada por el programa malicioso (malware) al que hace referencia dicho indicador de compromiso.[3]​ Los indicadores de compromiso permiten realizar un intercambio sencillo y práctico de información con el fin de detectar intrusos a partir de análisis forenses, respuestas a incidentes o análisis de malware.

### Integridad de la información

La integridad de ala información, junto con la confidencialidad y disponibilidad, forman parte de los principios clave para la protección de la información.  La integridad busca garantizar que los datos son son exactos y fiables y **que no han sido modificados accidentalmente o de manera intencional por terceros no autorizados**, ni cuando están en reposo, en uso o en movimiento.

### Inteligencia de amenazas

De acuerdo a [wikipedia](https://es.wikipedia.org/wiki/Inteligencia_de_Ciberamenazas), la Inteligencia de Ciberamenazas (en inglés: Cyber Threat Intelligence, CTI), también conocida como Inteligencia de Amenazas Cibernéticas, es la actividad de recopilar información basada en conocimientos, habilidad y experiencias sobre la ocurrencia y evaluación de amenazas cibernéticas y físicas, así como en los actores de amenazas que tienen la intención y el objetivo de ayudar a mitigar los posibles ataques y eventos dañinos que ocurren en el ciberespacio.

Este concepto surgió para combatir la gran variedad de amenazas que se están produciendo así como para ayudar a los profesionales de la seguridad a reconocer los indicadores de los ciberataques, extraer información sobre los métodos de los ataques, y en consecuencia, responder a los mismos de manera idónea y precisa.

La Inteligencia de Ciberamenazas busca generar conocimiento en torno al enemigo con la finalidad de reducir el riesgo que puede ocasionar sobre cualquier institución. Es una estrategia que en todo momento buscará anteponerse a los ataques y contrarrestarlos analizando la amenaza en su conjunto para detectar los datos clave que ayudan a identificar al autor del ataque, al ciberdelincuente.​ Su finalidad última es proporcionar la capacidad de percibir, reconocer, razonar, aprender y actuar de manera inteligente y oportuna sobre indicadores de escenarios de ataque y ataques cibernéticos avanzados, dicho de otra forma, tomar las acciones defensivas inteligentes correspondientes.

### Log (bitácora)

Los logs, también conocidos como registros o bitácoras, son archivos que documentan actividades que ocurren dentro de un sistema informático, red o aplicación. Estos registros pueden contener información sobre accesos de usuarios, cambios en el sistema, errores, y otras actividades relevantes para una investigación forense. 

En este recurso detallamos consideraciones importantes sobre [investigaciones forenses basadas en logs en dispositivos Android](../../explainers/03-explainer-log-forensics-android/). 

### Malware

Un malware, traducido del inglés como programa malicioso, programa maligno, programa malintencionado o código maligno, es cualquier tipo de software que realiza acciones dañinas en un sistema informático de forma intencionada (al contrario software defectuoso) y sin el conocimiento del usuario (al contrario que el software potencialmente no deseado. 

### Modo de desarrollador

Las [**opciones de desarrollador**](https://developer.android.com/studio/debug/dev-options) hacen referencia a un **menú oculto** del sistema operativo **Android** que permite configurar algunas **funciones adicionales**, pensadas especialmente para apoyar el proceso de [depuración](https://es.wikipedia.org/wiki/Depuraci%C3%B3n_de_programas) durante la **creación de nuevas aplicaciones o cambios en el sistema**. Entre las opciones de desarrollador, también se suelen colocar algunas **configuraciones avanzadas** como por ejemplo, ajustar las preferencias del controlador gráfico o configuraciones avanzadas de redes e incluso **opciones experimentales** que aún están en prueba o desarrollo. 


### MVT

MVT es una herramienta para facilitar el análisis forense consentido de dispositivos que pertenezcan a personas que podrían ser objetivo de ataques de spyware avanzados, y en específico personas parte de la sociedad civil y de comunidades en riesgo.

Se indica en su [sitio web](../../community/license/):

_Mobile Verification Toolkit (MVT) is a tool to facilitate the consensual forensic analysis of Android and iOS devices, for the purpose of identifying traces of compromise._

_It has been developed and released by the Amnesty International Security Lab in July 2021 in the context of the Pegasus Project along with a technical forensic methodology. It continues to be maintained by Amnesty International and other contributors._

_In this documentation you will find instructions on how to install and run the mvt-ios and mvt-android commands, and guidance on how to interpret the extracted results._

### Notificación de amenaza (Threat notification)

Las notificaciones de amenaza se refieren a mensajes envíados por plataformas y fabricantes a personas que podrían haber sido 

According to Apple, threat notifications inform and assist people using devices that may have been targeted by mercenary spyware attacks. Apple sends such notifications by email and iMessage to the registered addresses and phone numbers across all devices associated with a person’s Apple Account. The notification is also displayed at the top of the page after the person has signed in to account.apple.com.

### n-day

n-day se refiere a un tipo de [vulnerabilidad](#vulnerabilidad) que ya es conocida, pero que aún no ha sido resuelta en todos los sistemas afectados. En algunos casos, podrían existir parches de seguridad o mitigaciones oficiales pero que aún no han sido aplicadas a los equipos afectados.  

### Persona experta (perito/a)

De acuerdo a [wikipedia](https://es.wikipedia.org/wiki/Perito), un perito o experto (en femenino, perita o experta)[1]​ es una persona reconocida como una fuente confiable en un determinado tema, técnica o habilidad cuya capacidad para juzgar o decidir en forma correcta, equilibrada e inteligente le confiere autoridad y estatus por sus pares o por el público en una materia específica. 

En el contexto de investigaciones forenses, una persona experta o perita es aquella que tiene un conocimiento reconocido (por ejemplo a través de certificaciones), y que a través de su conocimiento puede analizar, evaluar y emitir juicios sobre evidencia recolectada. 

### Phishing

El phishing es una técnica que se basa en suplantar o falsificar información para incitar a la persona a realizar una acción, como dar clic a un enlace, abrir un archivo infectado, conectarse a una red o sistema falso, o ingresar información en sitios falsos. Generalmente con el objetivo de robar información, infectar un equipo o sistema de información. 

* Ej. correos electrónicos o SMS sospechosos solicitando dar clic a enlaces.
* Ej. correos electrónicos o SMS sospechosos solicitando enviar o responder información privada, sensible o financiera.
* Ej. correos electrónicos sospechosos solicitando abrir archivos adjuntos.

### Proveedor de servicios de Internet (ISP)

Se refiere a la empresa que brinda el servicio de Internet a la persona usuaria. Usualmente proveen _conexión de última milla_, 

### Respuesta a incidentes de seguridad

La [respuesta a incidentes](https://www.ibm.com/es-es/topics/incident-response) se centra en **detectar y responder a eventos de seguridad**. A través de procedimientos de respuesta, se pretende minimizar el impacto y contener las consecuencias de los incidentes. Para una respuesta efectiva, es importante identificar la causa raíz de las intrusiones, de forma tal que se pueda erradicar la amenaza y se logre una recuperación oportuna.

### Respaldo generado por ADB

Uno de los comandos de la herramienta de consola [ADB](#adb) permite generar un respaldo completo del dispositivo que incluye las aplicaciones y algunas configuraciones. Usualmente se accede en ADB a través del comand ```adb backup```, o se utiliza a través de herramientas como AndroidQF. Al ejecutarse, el dispositivo solicitá una contraseña para cifrar la información.  

### SocialTIC

[SocialTIC](https://socialtic.org) es una organización de la sociedad civil basada en México. Su misión es SocialTIC **empoderar de manera segura a actores de cambio en América Latina** reforzando sus acciones de análisis, comunicación social e incidencia a través del uso estratégico de tecnologías digitales y datos.

### Software espía (spyware)

Tipo de malware que recopila información de una computadora o dispositivo móvil y después transmite esta información a una entidad externa sin el conocimiento o el consentimiento del propietario del computador. Las funcionalidades de este tipo de herramientas son variadas, pero en general permiten acceder y extraer información almacenada y en tránsito, así como manipular los sensores del dispositivo (cámara, microfono, etc).  

### Stalkerware

Un stalkerware es un software espía utilizado en pequeña escala, principalmente en círculos íntimos como son los de pareja, familia o amistades. 

En lo habitual, se instalan al tener acceso físico al dispositivo, y buscaban recabar toda la información posible. El atacante puede tener acceso a un panel de control en donde visualiza toda la información.

Este tipo de herramientas suelen venderse como opciones de protección familiar para evitar el uso malintencionado del dispositivo o prevenir el robo de los mismos, sin embargo, sus funciones y capacidades permiten utilizarlas como herramientas de monitoreo y espionaje casero.


### TTP

Proviene de la abreviatura en inglés de _Techniques, Tactics and Procedures_, y se refiere a un listado de técnicas, tácticas y comportamientos utilizados por actores de amenazas. El marco de referencia de TTPs más conocido es el de [MITRE ATT&CK](https://attack.mitre.org/), que incluye además un registro histórico de [TTPs asociadas a ciertos actores de amenazas](https://attack.mitre.org/groups/). 

### Triaje

El triage de incidentes de seguridad se refiere al proceso de evaluación inicial y clasificación de los incidentes de seguridad en función de distintos factores, como la gravedad, la urgencia, y el impacto potencial. Su objetivo principal es asignar recursos y prioridades de manera efectiva, permitiendo que los equipos de respuesta a incidentes se enfoquen en las amenazas más críticas y reduzcan el riesgo para la organización. Este proceso, fundamental en la gestión de incidentes, es similar al triage médico, donde los pacientes son clasificados según la gravedad de su condición para determinar el orden de atención.


### Volatilidad

La volatilidad de la evidencia digital hace referencia al hecho de que alguna información disponible en los sistemas se destruye o altera conforme pasa el tiempo. 

Por ejemplo, algunos arhivos de logs se sobre-escriben al llegar a cierto límite, por lo que alguna de esta evidencia podría no existir de forma permanente en el tiempo. 

### Vulnerabilidad

Por otro lado, una vulnerabilidad se refiere a una deficiencia o debilidad en procesos, sistemas, prácticas o hábitos que pueden propiciar amenazas o incrementar el impacto y las consecuencias de un incidente.

### Zero click

Se refiere a un tipo de ataque en el que **no se requiere la intervención de la persona usuaria para la implantación del malware**. Usualmente este tipo de ataques son muy sofisticados y costosos, y requieren de múltiples vulnerabilidades encadenadas para tener éxito.


### Zero day

Se refiere a un tipo de ataque que explota una [vulnerabilidad](#vulnerabilidad) que no es conocida, ni siquiera por el fabricante del dispositivo. Por lo tanto, no existen parches o soluciones que puedan ser aplicadas. 

Puede consultar aquí la [página de wikipedia para "Ataque de día cero"](https://es.wikipedia.org/wiki/Ataque_de_d%C3%ADa_cero). 
