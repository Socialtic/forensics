---
title: Principios para forense basada en logs en dispositivos Android 
summary: Documento introductorio con principios para forense basada en logs en dispositivos Android
keywords: forense, logs, android, androidqf
lang: es
tags: [explainer, intro]
last_updated: 2025-06-23
some_url:
created: 2025-06-23
comments: true
author:
    name: Daniel
    url: https://socialtic.org/quienes-somos/
    description: SocialTIC

---

# Explainer: Principios para forense basada en logs en dispositivos Android

Este documento forma **parte de un repositorio de documentación técnica** que tiene como objetivo establecer una base de conocimientos probados, flexibles y accesibles para **impulsar el análisis forense consentido en beneficio de la sociedad civil**. Para organizar los contenidos, se utiliza el [marco de referencia de documentación técnica Diataxis](../../references/00-glossary/index.md#diataxis).

Este recurso en particular se enmarca dentro de la categoría de materiales explicativos, y presenta los **fundamentos de la forense basada en logs para dispositivos Android**, incluyendo una definición de forense basada en logs y una comparación con otros tipos de análisis, así como casos de uso. Este es un **material introductorio que no requiere conocimientos previos**, y se complementa con otras [guías](https://forensics.socialtic.org/how-tos/index.html) de [extracción forense](../../references/00-glossary/index.md#adquisicion).


## ¿Qué es el análisis forense basado en logs y porqué es útil? 

La forense basada en logs se refiere a un tipo de investigación que **utiliza diferentes registros del sistema cómo reportes de errores, capturas de memoria, archivos de configuración, entre otros, para identificar e investigar rastros e indicadores de potenciales [ataques digitales](https://socialtic.org/wp-content/uploads/2020/11/Tipologia_AtaquesDigitales-2020-1.pdf).**

Para realizar un análisis forense basado en logs se atraviesan [las diferentes etapas de una investigación forense](../01-explainer-introduction-digital-forensics/index.md#cuales-son-las-etapas-de-una-investigacion-forense), iniciando con la **identificación y recolección** de potenciales evidencias. Al recoger evidencia es importante obtener un [consentimiento informado](../../references/00-glossary/index.md#consentimiento-informado),  reducir la cantidad de información personal y mantener adecuados procesos de [verificación, preservación y protección de la información](../01-explainer-introduction-digital-forensics/index.md#consideraciones-importantes-al-realizar-investigaciones-forenses).

En el caso de dispositivos móviles, y en particular cuando se sospecha de una posible infección avanzada o spyware, **la mayor parte de los análisis** realizados por organizaciones de la sociedad civil como Amnesty Tech o Citizen Lab **utilizan forense basada en logs**. La posibilidad de recolectar información clave y dirigida (por ejemplo, un reporte de errores de Android), **incluso en situaciones de atención remota**, hace que este tipo de análisis sea común dentro de la sociedad civil. 

Las evidencias recolectadas usualmente se **analizan** de forma posterior, idealmente en un ambiente de laboratorio en apego a **buenas prácticas de [seguridad operacional](https://en.wikipedia.org/wiki/Operations_security)**. Herramientas como [MVT](../../references/00-glossary/index.md#mvt) o [AndroidQF](../../references/00-glossary/index.md#androidqf) facilitan diferentes acciones durante la captura y el análisis de artefactos. De manera general, se busca **probar similaridad con [indicadores de compromiso](../../references/00-glossary/index.md#indicador-de-compromiso-ioc)** (IoC, por sus siglas en inglés) de ataques previamente registrados y documentados; o documentar anomalías al comparar con una línea base establecida, que permita evidenciar comportamientos sospechosos o vulnerabilidades que quizás no han sido reportadas. Debido a su aproximación metodológica, detecciones positivas a través de forense basada en logs suelen tener un **alto nivel de confiabilidad**. 

Es importante tomar en cuenta que **los logs y registros de un sistema** **cambian** de forma constante en el tiempo, y pueden sobreescribirse o eliminarse después de cierto período. Por lo tanto, a pesar de que la forense basada en logs puede aplicarse de forma posterior a un incidente de seguridad, **la posibilidad de detectar alguna actividad maliciosa disminuye si ha transcurrido mucho tiempo** entre la posible actividad y la adquisición de artefactos. 

Si bien los registros podrían no ser de utilidad para ataques que tuvieron lugar años atrás, **de forma posterior podrían descubrirse nuevas vulnerabilidades**, metodologías o indicadores de compromiso para identificar ataques digitales que anteriormente no eran detectables. Si se planea almacenar registros para análisis posteriores, es importante que exista una carta o formulario de consentimiento documentado; y reducir o eliminar  cualquier información personal que no sea relevante para la investigación forense. 

La publicación de Internet Research Lab: “[Detección y análisis de spyware: metodologías, limitaciones y oportunidades](https://irl.works/blog/2025/03/19/spyware-detection-analysis.html)” **resume y presenta diferentes metodologías en uso por parte de la sociedad civil**, específicamente para la detección de spyware. Además de investigaciones forenses de dispositivos, incluídas investigaciones basadas en logs, se describen **investigaciones a partir de señales o sistemas de monitoreo** instalado en los sistemas, donde un componente de software monitorea en tiempo real los procesos y otras actividades para alertar sobre posibles intrusiones a partir de métodos determinísticos o estadísticos. Adicionalmente se hace mención a la **detección de incidentes a través de análisis de tráfico**, donde se busca detectar trazas de un software malicioso investigando metadatos de las comunicaciones de red de los dispositivos. 

En resumen, algunas de las **ventajas de la forense basada en logs** son: 

* Permite **atención remota.**  
* Recolecta **menos información privada**, en especial si se hace una recolección puntual y se eliminan archivos o datos sensibles.  
* Permite obtener **resultados con un** **nivel de confianza alto**, en particular cuando se logra establecer una concordancia con algún IoC conocido.  
* Es útil para hacer **comparaciones cuando se conoce una línea base** contra la cual comparar.  
* **Es posible continuar evaluando los registros capturados** contra nuevos IoC que se publiquen de forma posterior a la recolección inicial.

Y algunos de los **retos de utilizar forense basada en logs** son: 

* Aún cuando se realicen extracciones dirigidas, **es posible que los archivos incluyan cientos de miles de líneas**, por lo que realizar análisis manual requiere experticia en el filtrado e identificación.  
* Algunos logs y registros podrían no estar disponibles desde el perfil del usuario, o **podrían requerir permisos adicionales del sistema** (como por ejemplo, acceso de root en Android).  
* Muchos archivos de logs funcionan con **[buffers circulares](https://es.m.wikipedia.org/wiki/Buffer_circular) que se sobreescriben** conforme se van llenando, por lo que la información más antigua se sobreescribe de forma constante.   
* Para la extracción de logs y registros, **es necesario tener un conocimiento básico del sistema** operativo, en especial cuando el almacenamiento está particionado o utiliza diferentes rutas para almacenar información. 

## ¿Cómo se inicia un análisis forense basado en logs en un dispositivo Android? 

Para realizar un análisis forense basado en logs es necesario atravesar las etapas típicas de una investigación forense, **iniciando con la captura de los registros clave** del sistema que se desea investigar. Para realizar el análisis también será necesario contar con una línea base de referencia, que nos permita entender cuál es el comportamiento esperado del dispositivo ante situaciones normales. Como se mencionó anteriormente, el **acceso a indicadores de compromiso**, como los que publican [Amnesty International](https://github.com/mvt-project/mvt-indicators) o [Citizen Lab](https://github.com/citizenlab/malware-indicators), facilitan la identificación de amenazas y el triaje de posibles incidentes, aunque cabe mencionar que estos pueden perder vigencia conforme el atacante modifica su infraestructura, tecnología o vectores de ataque, por lo que deben ser actualizados o complementados con análisis manuales.   

Para extraer la información clave de un dispositivo Android es posible utilizar algunas **herramientas que facilitan el empaquetado y la captura de registros**, como por ejemplo el reporte de errores de Google (bugreport) o el shell de ADB, y también herramientas desarrolladas por terceros como AndroidQF. 

## Tipos de logs y herramientas de empaquetado

En el caso de los dispositivos móviles con sistema operativo Android, debido a la **diversidad de fabricantes y sus preferencias particulares**, así como el ecosistema diverso de desarrolladores y componentes, existen diferentes aproximaciones para el registro de logs. En general se utilizan una mezcla de los [siguientes estándares](https://source.android.com/docs/core/tests/debug/understanding-logging): 

* [RCF 5424 (protocolo syslog)](https://datatracker.ietf.org/doc/html/rfc5424): Se utiliza para el registro de **eventos del kernel y de aplicaciones tipo UNIX**, como por ejemplo servicios del sistema.   
* [android.util.log](https://android.googlesource.com/platform/frameworks/base/+/master/core/java/android/util/Log.java) : Se utiliza para el registro de **eventos de Android y de aplicaciones del sistema**  
* [java.util.logging.level:](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Level.html) Se utiliza para el **registro en aplicaciones Java**, lo que incluye muchas de las aplicaciones de terceros. 

Cada uno de los estándares posee una construcción similar, pero **diferentes niveles para el registro** y alerta ante situaciones de error. Por ejemplo, en **syslog existen 8 niveles**: desde logs de depuración hasta logs de emergencia; mientras que en **android.util únicamente existen 5 niveles**, que van desde verboso hasta error. 

Si bien entender con exactitud los niveles y construcción de cada uno de los logs de Android está fuera del alcance de este recurso, **es importante tener presente la fragmentación del ecosistema**, puesto que esto también se verá reflejado en las diferencias para navegar las interfaces gráficas, acceder a opciones avanzadas o extraer información. 

Si bien la diversidad del ecosistema impide establecer una lista definitiva para todos los sistemas Android, a continuación se detallan algunos de lo**s tipos de logs y registros que se utilizan más comúnmente durante un análisis forense** y que se pueden acceder sin necesidad de tener privilegios de administración (i.e root level access):

* **logs principales (main log):** Los logs principales registran mensajes generales de las aplicaciones y del sistema.   
* **logs de pánico del kernel (kernel panic):** Los logs de pánico se refieren a registros que se crean cuando el sistema operativo detecta un error del cual no se puede recuperar, como por ejemplo una violación de memoria o algún problema con un llamado al sistema. En la mayoría de los casos se utiliza la función del kernel de linux [‘ramoops’](https://www.kernel.org/doc/html/v4.19/admin-guide/ramoops.html) para escribir los logs antes de que el sistema se detenga.  
* **Reportes de interrupciones (crash reports) y tombstones:**  Los logs de interrupciones usualmente se registran cuando una aplicación o algún proceso se detiene inesperadamente. Por su parte los tombstones se refieren a reportes detallados de fallas para aplicaciones nativas de Android.   
* **logs de radio**: Los logs de radio y componentes de red capturan información sobre la actividad que sucede entre el celular y las torres de comunicaciones, relacionado a datos móviles, llamadas de voz, SMS, entre otros.   
* **logs de seguridad**:  Los logs de seguridad se refieren a registros relacionados con configuraciones de seguridad como [SELinux](https://www.redhat.com/en/topics/linux/what-is-selinux) o logs que se encuentren dentro del buffer de seguridad. 

Existen algunas herramientas nativas que permiten extraer y empaquetar los registros (logs, aplicaciones, lista de procesos, etc) de forma sencilla y puntual. Algunas de estas herramientas son:  

* [**dumpsys**](https://developer.android.com/tools/dumpsys): Es una herramienta nativa de línea de comandos en Android, disponible desde el shell de depuración de Android o ADB por sus siglas en inglés. **Permite extraer información detallada de servicios del sistema** como la batería, red wifi, uso de memoria, entre otros.   
* **dumpstate**: Es una herramienta nativa que **permite recolectar información del registro de errores** de un dispositivo. Se encuentra disponible a través de  la herramienta de creación de reportes de errores o bugreport.   
* [**logcat**](https://developer.android.com/tools/logcat): Es una herramienta nativa de línea de comandos en Android, disponible desde el shell de depuración de Android o ADB por sus siglas en inglés. **Permite extraer los mensajes o logs del sistema,** incluyendo muchos de los logs descritos anteriormente.   
* [**bugreport**](https://developer.android.com/studio/debug/bug-report): Es una herramienta nativa de línea de comandos en Android, disponible desde la interfaz gráfica o desde el shell de ADB. **Permite generar un informe de errores** que contiene logs de diagnóstico, generados a partir de el llamado a logcat, dumsptate y dumpsys. Se genera dentro de un archivo .zip y está compuesto de una estructura de carpetas con información sobre errores, uso de memoria, llamados al sistema, información de red, información del dispositivo, entre otros.   
* [**androidqf**](https://github.com/mvt-project/androidqf): Es una herramienta desarrollada inicialmente por Claudio Gurnieri y actualmente soportada por el equipo del [laboratorio de seguridad de Amnistía Internacional.](https://securitylab.amnesty.org/latest/2024/12/tech-guide-detecting-novispy-spyware-with-androidqf-and-the-mobile-verification-toolkit-mvt/)   
* [**Perfetto**](https://perfetto.dev/docs/)**:** Es una herramienta de código abierto que permite realizar una depuración avanzada de aplicaciones en el sistema operativo Android y Linux. Recopila información de memoria, CPU, consumo de batería, entre otros. 

## Consideraciones adicionales de la forense basada en logs

Antes de iniciar un análisis forense basado en logs, es importante tener en cuenta los siguientes aspectos: 

* **Reducción y protección de información sensible**: A diferencia de [otras aproximaciones a la forense digital](../01-explainer-introduction-digital-forensics/index.md#en-donde-se-aplica-la-forense-digital), en la sociedad civil se busca desarrollar investigaciones a partir de información específica y dirigida, y **evitar hacer una recolección excesiva de información personal** no relevante para la investigación. Si los empaquetados de información [incluyen información sensible](../../how-tos/01-how-to-obtain-informed-consent/index.md#que-informacion-sensible-se-recolecta-durante-un-analisis-forense), como por ejemplo fotografías personales, es altamente recomendable aplicar procedimientos automatizados para mantener únicamente la información relevante. Dichos procedimientos deben estar debidamente documentados y ser replicables para poder **garantizar siempre la integridad de la información**.   

* **Consentimiento informado**: Antes de recolectar logs o registros de un dispositivo, es importante discutir y obtener un consentimiento informado. [Este recurso brinda guía y orientación para generar una carta de consentimiento](../../how-tos/01-how-to-obtain-informed-consent/) y acordar buenas prácticas con quién solicita el análisis. 

* **Roles, fases y etapas del análisis forense basado en logs:** El análisis forense basado en logs atraviesa una [serie de etapas](../01-explainer-introduction-digital-forensics/index.md#cuales-son-las-etapas-de-una-investigacion-forense), comenzando por la **identificación y recolección** de información clave. Durante estas etapas es posible seguir guías prácticas para ejecutar procedimientos de recolección y empaquetado de la información, que en general, **no requieren de conocimientos avanzados en análisis forense**. El triaje y análisis de la información recopilada requiere de conocimientos adicionales, tanto en el uso de herramientas de análisis como en la aplicación y revisión manual.   

* **Manejo de expectativas**: Al realizar la revisión de un dispositivo, **es posible que no se encuentren rastros de alguna amenaza,** al comparar con amenazas conocidas. Si bien esto es una señal positiva, no es suficiente para afirmar que ninguna amenaza se ha presentado o materializado. Incluso después de realizar un análisis manual, podrían haber factores que limiten el éxito de un análisis forense basado en logs. En caso de existir sospechas fuertes de un compromiso (por ejemplo, notificación de amenazas de plataformas), se recomienda también considerar algunos de los métodos forenses antes mencionados.  

* **Revisión de pares y trabajo colaborativo**: Al hacer investigaciones forenses de cualquier tipo, incluyendo aquellas basadas en logs, es importante verificar los hallazgos con contrapartes de confianza que puedan replicar de forma independiente la metodología a fin de confirmar los resultados. Es altamente recomendable realizar revisiones de pares antes de realizar publicaciones, en especial si se presentan resultados a través de una nueva metodología, o si se trata de una nueva vulnerabilidad.

## Conclusión

La **forense basada en logs** utiliza registros clave de dispositivo, como información de procesos, reportes de errores o logs del sistema, para identificar indicadores de compromiso conocidos; o resaltar anomalías al comparar con una línea base establecida. 

En el caso del **sistema Android,** debido a la diversidad de fabricantes y tecnologías involucradas en su creación y desarrollo, existen una variedad de estándares y herramientas con las cuales es importante familiarizarse, incluyendo syslog, dumspate y ADB. Además, algunas herramientas como AndroidQF son de gran utilidad durante la recolección  de información forense en Android. 

Una gran parte de los reportes hasta ahora publicados por sociedad civil han utilizado la forense basada en logs para justificar y documentar sus hallazgos, debido en parte a que permite realizar investigaciones de forma remota, minimiza la información personal a recolectar y entrega resultados de alta confiabilidad. 

Si deseas contribuir con el desarrollo, la traducción o difusión de este recurso por favor escríbenos a [seguridad@socialtic.org](mailto:seguridad@socialtic.org) 


## Comentarios

¿Tienes **comentarios o sugerencias** sobre este recurso? Puedes utilizar la **función de comentar que se muestra a continuación** para dejarnos tus ideas o apreciaciones. Por favor asegúrate de seguir nuestro [código de conducta](../../community/code-of-conduct/). La función de comentarios enlaza directamente a la sección de [_Discussions_ de Github](https://github.com/Socialtic/forensics/discussions), donde también **puedes participar en las discusiones de forma directa**, si lo prefieres.   


