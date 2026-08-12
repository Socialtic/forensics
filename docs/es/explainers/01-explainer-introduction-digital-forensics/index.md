---
title: Explainer - Introducción a la forense digital consentida para la defensa de los Derechos Humanos 
summary: Documento introductorio a la forense digital consentida en beneficio de la sociedad civil para la defensa de los Derechos Humanos
keywords: forense, consentimiento informado, introduccion, etapas, derechos humanos
lang: es
tags: [explainer, intro]
last_updated: 2025-08-13
some_url:
created: 2025-02-03
comments: true
author:
    name: Daniel
    url: https://socialtic.org/quienes-somos/
    description: SocialTIC
    
---

# Explainer: Introducción a la forense digital consentida para la defensa de los Derechos Humanos

Este documento forma parte de un repositorio de documentación técnica que tiene como objetivo establecer una base de conocimientos probados, flexibles y accesibles para impulsar el análisis forense consentido en beneficio de la sociedad civil. Para organizar los contenidos, se utiliza el [marco de referencia de documentación técnica Diataxis](../../references/00-glossary/index.md#diataxis).

El presente documento se clasifica como un [material explicativo](https://diataxis.fr/explanation/). Describe conceptos claves sobre la forense digital, incluyendo una definición acotada, una reseña de las etapas de una investigación y una exposición de cómo se aplica las [ciencias forenses](https://es.wikipedia.org/wiki/Criminal%C3%ADstica) en el contexto digital para la defensa de los Derechos Humanos. Es un material introductorio, que pretende sentar una base de conocimiento general sobre la práctica forense, y que se complementa con recursos adicionales como [guías](../../how-tos/), [tutoriales](../../tutorials/) y [referencias](../../references/).

## ¿Qué es  la forense digital y porqué es importante?

La forense digital es el proceso utilizado para la recolección, preservación, análisis y presentación de evidencia digital derivada de medios y dispositivos electrónicos, utilizando **técnicas de investigación y métodos científicos** que sean fiables, acertados y repetibles, de forma tal que los resultados puedan ser utilizados en **procedimientos judiciales**.[1](https://csrc.nist.gov/glossary/term/digital_forensics)

La forense digital se utiliza para descubrir y examinar datos de dispositivos electrónicos con el objetivo de **identificar, recuperar, documentar e interpretar la información** digital y su conexión con [ataques digitales](https://protege.la/ataques/). La utilización de procedimientos estándar, en apego a mejores prácticas, **permite generar evidencia útil** que impulse acciones de **rendición de cuentas**, que pueda reducir la impunidad con la que se ejecutan ataques digitales.

Por ejemplo, en Polonia, luego de [investigaciones forenses lideradas por el Citizen Lab, Amnesty Tech](https://www.amnesty.org/en/latest/news/2022/01/poland-use-of-pegasus-spyware-to-hack-politicians-highlights-threat-to-civil-society/) y otros grupos de Sociedad Civil, el gobierno de [Polonia inició una investigación sobre los posibles abusos de poder](https://cyberscoop.com/inside-polands-groundbreaking-effort-to-reckon-with-spyware-abuses/), aclarando el contexto en el cual se utilizó tecnologías de vigilancia en perjuicio de la sociedad civil y comprometiéndose a notificar a posibles personas afectadas.

## ¿En dónde se aplica la forense digital?

Las investigaciones forenses se pueden llevar a cabo con diferentes objetivos y enfoques: 


<div class="grid cards" markdown>

-   :material-police-badge:{ .lg .middle } __Investigaciones periciales__

    ---

    Se realizan en apego a marcos jurídicos, y su principal objetivo es recolectar y presentar evidencia que pueda ser utilizada en **procedimientos judiciales, ya sea civiles o criminales**. Las investigaciones periciales son lideradas mayoritariamente por entidades policiales y agencias de investigación gubernamentales. Históricamente, ha sido el enfoque de investigación más frecuente, y desde donde se originan algunas de las prácticas y marcos de referencia. 

-   :fontawesome-solid-university:{ .lg .middle } __Investigaciones académicas__

    ---

    Buscan identificar **nuevas líneas de investigación** que permitan avanzar en los métodos y generar conocimiento práctico y teórico que avance el área de investigación forense.

-   :fontawesome-solid-money-bill-1-wave:{ .lg .middle } __Investigaciones en el sector privado__

    ---

    Son lideradas por equipos internos o consultores externos. Buscan esclarecer el **orígen y los alcances de intrusiones e incidentes** en perjuicio de empresas o instituciones. 

-   :octicons-megaphone-16:{ .lg .middle } __Protección de defensores de Derechos Humanos (DDHH)__

    ---

    En el contexto de protección a personas defensoras de Derechos Humanos, las investigaciones forenses buscan generar, preservar y presentar evidencia de incidentes de seguridad digital en perjuicio de personas defensoras de Derechos Humanos. Se busca que las personas afectadas puedan acceder a mecanismos de justicia, que reduzcan la impunidad y permitan exponer los abusos de poder y las violaciones a sus derechos fundamentales. 


</div>


De forma frecuente, las investigaciones forenses inician cuando se detecta un posible incidente de seguridad. Si bien el **análisis forense y la respuesta a incidentes** persiguen objetivos distintos, consolidar ambos procesos permite fortalecer la forma en que se responde a los incidentes, al tiempo que se preserva evidencia. 

La [respuesta a incidentes](../../references/00-glossary/index.md#respuesta-a-incidentes-de-seguridad) se centra en **detectar y responder a eventos de seguridad**. A través de procedimientos de respuesta, se pretende minimizar el impacto y contener las consecuencias de los incidentes. Para una respuesta efectiva, es importante identificar la causa raíz de las intrusiones, de forma tal que se pueda erradicar la amenaza y se logre una recuperación oportuna.

Si la respuesta a un incidente y el análisis forense se realizan por separado, las acciones que se tomen podrían interferir y dificultar tanto la respuesta como el análisis. Por ejemplo, **al responder** a un incidente sin tomar en cuenta las necesidades de preservación de evidencia, **se podrían alterar o destruir pruebas** y artefactos necesarios para el análisis forense. De la misma manera, si únicamente nos enfocamos en el análisis forense, se podría **retrasar la contención de la amenaza** e incrementar las consecuencias y el tiempo de resolución de un incidente.

Por lo tanto, **resulta ventajoso [combinar ambos procesos en lo que se conoce como DFIR](../../references/00-glossary/index.md#dfir-digital-forensics-and-incident-response)**, de manera que durante la respuesta a un incidente se consideren mejores prácticas para la recolección y preservación de evidencia, y se utilicen hallazgos producto del análisis forense para contener y erradicar amenazas, y, ultimadamente, se prevengan futuros incidentes.

``` mermaid
flowchart LR
  A[Respuesta a Incidentes] --> C[DFIR];
  B[Forense Digital] --> C;
```

La presente guía y repositorio documental se enfocan en el análisis forense. Sin embargo, es importante **considerar la estrecha relación que existe con los procesos de respuesta a incidentes**, de forma tal que se puedan integrar buenas prácticas forenses durante la atención a casos y situaciones de emergencia.

## ¿Cuáles son las etapas de una investigación forense?

Existen diferentes marcos de referencia que proponen una serie de etapas para completar una investigación forense, como por ejemplo la [norma ISO 27037](https://www.amnafzar.net/files/1/ISO%2027000/ISO%20IEC%2027037-2012.pdf) o las guía de [NIST para la integración del análisis forense en procesos de respuesta a incidentes](https://nvlpubs.nist.gov/nistpubs/ir/2022/NIST.IR.8428.pdf).

!!! success "Buenas Prácticas" 

    A través de este conjunto de etapas se **busca garantizar la integridad de la evidencia y la confianza en el proceso aplicado**. Por su naturaleza, la evidencia digital es frágil, ya que puede ser alterada o destruida durante el proceso de recolección o análisis.  Es por esto que, independientemente del marco de referencia que se utilice, se deben tomar en consideración los siguientes principios básicos durante todo el ciclo de una investigación:
   
    * En la medida de lo posible, se debe evitar **manipular y trabajar directamente sobre la evidencia recolectada**. En su lugar, es recomendable utilizar copias de trabajo que no pongan en riesgo la evidencia original.
    * **Documentar es un aspecto clave durante una investigación forense**. Cualquier acción que se tome sobre la evidencia, herramientas que se utilicen para el análisis, hallazgos e hipótesis deben ser documentadas. Es importante que un tercero pueda reproducir y verificar de forma independiente el análisis realizado.
    * Si se pretende utilizar la evidencia como parte de un proceso judicial, se debe **conocer la legislación y el marco jurídico** que haga la evidencia admisible en una corte.

La mayoría de marcos de referencia coinciden en las siguientes etapas: **identificación, recolección, preservación, análisis y presentación**. A continuación se detalla en qué consiste cada una de estas etapas:

``` mermaid
graph LR
  A[1- Identificación] --> B[2- Recolección y adquisición];
  B --> C[3- Verificación y preservación];
  C --> D[4- Análisis];
  D --> E[5- Presentación];
```

=== "1- Identificación"

    Durante la identificación, la persona analista determina **cuáles dispositivos, cuentas o sistemas podrían contener información relevante para la investigación**. Ejemplos de dispositivos incluyen teléfonos móviles, computadoras, cuentas en línea, medios de almacenamiento, entre otros. Idealmente, para determinar la evidencia a recolectar, la persona analista debe tener contacto con la persona impactada, para entender qué sucedió, qué acciones se han tomado hasta el momento y qué evidencia podría estar disponible.

=== "2- Recolección y adquisición"

    Una vez que se identifican los dispositivos y sistemas que pueden contener evidencia útil, la persona analista forense debe determinar la mejor forma de recolectar la evidencia forense. **Qué priorizar y cómo realizar la extracción dependerá de diversos factores**, entre ellos el tipo de incidente, el tipo de atención (en sitio o remota), la [volatilidad de la evidencia](../../references/00-glossary/index.md#volatilidad) y el esfuerzo requerido para la extracción. Consideraciones adicionales para la extracción incluyen lo siguiente:

    * Es posible que la persona analista identifique **más fuentes de información de las que se tenga capacidad para extraer**. Por ejemplo, si se sospecha de una infección de spyware, podría existir información relevante en el dispositivo afectado, en los equipos de red, en los equipos del proveedor de servicio, entre otros. Se debe priorizar aquella evidencia que, de acuerdo a la experiencia, tenga mayor valor para la investigación y requiera un menor esfuerzo.
    * Por su naturaleza **algunos datos útiles para el análisis son volátiles**, es decir la información se destruye o altera en el tiempo, al apagar el dispositivo o al interactuar con el dispositivo. Un ejemplo de información volátil es la lista de procesos activos en un dispositivo en un momento determinado. En general, es recomendable priorizar la extracción de los datos volátiles sobre los no volátiles (como el sistema de archivos).
    * Tomando lo anterior en consideración, la persona analista puede optar por diferentes tipos de extracción.  Por ejemplo, se puede realizar una **imagen física**, o [copia bit a bit](../../references/00-glossary/index.md#copia-bit-a-bit) de una unidad de almacenamiento, a fin de duplicar de forma íntegra su contenido, incluyendo información presente en la unidad pero que pudo haber sido eliminada. Alternativamente, se puede realizar una **imagen lógica**, es decir una copia de los archivos visibles. En algunos casos, la persona analista puede realizar una extracción de **información específica**, por ejemplo archivos de logs únicamente.

=== "3- Verificación y preservación"

    Una vez que se realiza la extracción, es importante verificar la integridad de la evidencia recolectada. El objetivo es poder **demostrar que la evidencia que la persona analista ha utilizado para su análisis no ha sido alterada**. La verificación y preservación son siempre importantes, pero tienen especial relevancia si se pretende utilizar la evidencia en procedimientos judiciales. Usualmente, la verificación de la integridad implica la utilización de [funciones de hash criptográficas](../../references/00-glossary/index.md#hash), que permiten producir un único valor para un conjunto de datos dados. Por su parte, la preservación se relaciona con el establecimiento de una [**cadena de custodia**](../../references/00-glossary/index.md#cadena-de-custodia), especialmente para evidencia física (dispositivos físicos, discos duros, etc), a través de un registro y documentación de dónde, cómo y quién ha accedido a la evidencia.

=== "4- Análisis"

    Durante el análisis, la persona analista utiliza herramientas especializadas y análisis manual para estudiar y analizar la evidencia, a fin de **establecer hipótesis y conclusiones** sobre lo que sucedió. En muchas  ocasiones, la persona analista se enfrentará a grandes cantidades de información, por lo que un análisis manual puede ser poco efectivo y muy lento, en especial si no se tiene claridad en qué y dónde buscar. Algunas herramientas forenses pueden facilitar el proceso, en especial si se tiene acceso a [**indicadores de compromiso**](../../references/00-glossary/index.md#indicador-de-compromiso-ioc). Durante esta etapa, es clave utilizar metodologías y procedimientos consistentes, que puedan ser replicables y verificables. En algunas ocasiones no será posible establecer una conclusión a partir de la información existente.

=== "5- Presentación"

    La última etapa de un análisis forense que implica preparar y presentar la información derivada del análisis. Se debe tomar en consideración el objetivo y la audiencia a la que se le estará presentando la información para determinar la mejor estructura de contenidos. Por ejemplo, si se debe preparar un informe como parte de un procedimiento judicial, el reporte debe ser detallado e incluir información que permita verificar y reproducir los hallazgos. Por el contrario, si el reporte es de uso interno de una organización y está dirigido al equipo de liderazgo, el reporte puede enfocarse en las conclusiones y recomendaciones de remediación.



## ¿Cómo se aplica la forense digital en la práctica de defensa de Derechos Humanos?

Las personas y organizaciones defensoras de Derechos Humanos, en la gran mayoría de los casos, carecen de sistemas de monitoreo robustos que alerten sobre posibles intrusiones a sus redes o dispositivos de forma temprana. Por lo tanto, es común que **la detección de un posible ataque suceda cuando se perciben las consecuencias de un incidente**. Tampoco es común que organizaciones de la sociedad civil cuenten con personal especializado en seguridad digital, por lo que frecuentemente las tareas de respuesta a incidentes recaen en equipos internos de tecnología o comunicación, en ocasiones apoyados por líneas de ayuda o consultores externos.

Cuando una persona u organización identifica un potencial incidente, ya sea a través de un comportamiento sospechoso o alguna alerta (por ejemplo, las [notificaciones de amenazas avanzadas de Apple](../../references/00-glossary/index.md#notificación-de-amenaza-threat-notification), la línea de ayuda o el punto de contacto en seguridad digital inicia un proceso de investigación y [triaje](../../references/00-glossary/index.md#triaje) para entender qué sucedió, cuándo se identificó y qué acciones se han tomado hasta el momento. **Desde estas primeras etapas es clave que la persona manejadora de incidentes, además de [evaluar el bienestar emocional](https://vita-activa.org/2022/07/11/los-primeros-auxilios-psicologicos-en-7-claves/#:~:text=Los%20primeros%20auxilios%20psicol%C3%B3gicos%20nos,ti%20misma%20y%20tus%20acciones.), incorpore prácticas de forense digital** que puedan producir evidencia que sea de utilidad  para impulsar procesos de rendición de cuentas. 

Como se mencionó anteriormente, los procesos de **respuesta a incidentes y forense digital están estrechamente interconectados**. Es durante la etapa de triaje y respuesta inicial, que la persona manejadora de incidentes identifica cuáles dispositivos, sistemas y cuentas podrían contener evidencia forense relevante para la investigación. Vale resaltar que en nuestro contexto, las **investigaciones forenses deben ser siempre consentidas**, por lo que antes de recolectar cualquier evidencia se debe informar de forma clara a la persona en riesgo cuáles acciones se pueden tomar, el riesgo que conllevan y los resultados que se pueden esperar, de forma tal que sea la persona en riesgo quien mantenga el control y defina el curso de la investigación. 

Determinar exactamente qué recolectar depende de muchos factores, incluyendo la voluntad de la persona en riesgo, el tipo de incidente, las herramientas y recursos disponibles y la capacidad técnica disponible.  En algunas ocasiones, la persona manejadora de incidentes realiza un triaje y recolección inicial, que es apoyado por terceros de confianza, que tengan mayor capacidad técnica para la detección y atribución de ataques. **No es necesario tener un conocimiento técnico profundo para apoyar con la recolección y el manejo de evidencia,** pero sí es de gran utilidad que se comprendan conceptos y consideraciones claves incluídas en este documento.

Por ejemplo, en algunas ocasiones no es conveniente simplemente apagar y enviar un dispositivo a un laboratorio de confianza para un análisis posterior. Al hacer esto, se podría perder la **evidencia volátil**, es decir aquella que se modifica o destruye al manipular o apagar un dispositivo. En estos casos, lo conveniente es utilizar herramientas forenses que permitan hacer una **recolección en vivo** que permita recopilar información como listas de procesos, archivos temporales, entre otros.

!!! success "Buenas Prácticas" 
    Durante todo el proceso de atención es de suma importancia mantener una documentación cronológica de las acciones tomadas y las evidencias recopiladas, incluyendo hashes (identificadores únicos) que permitan una posterior verificación.

En la mayoría de los casos, la evidencia no puede analizarse en sitio, y es necesario utilizar herramientas y procesos especializados para intentar establecer conclusiones sobre lo sucedido. Este **análisis en frío** suele realizarse en un laboratorio forense, por personas con conocimientos específicos. 

En algunas ocasiones, **es posible que el análisis forense no arroje ningún resultado inmediato**, en especial si se trata de una amenaza avanzada, donde el atacante ha realizado un esfuerzo por eliminar rastros como logs, archivos o metadatos. Es posible que los atacantes también utilicen técnicas que busquen obstaculizar los esfuerzos de análisis forense, a través de técnicas conocidas como [anti-forense.](https://en.wikipedia.org/wiki/Anti%E2%80%93computer_forensics)

Además, **no siempre se tiene acceso a [inteligencia de amenazas](../../references/00-glossary/index.md#inteligencia-de-amenazas) robusta** que permita identificar y atribuir posibles ataques. El no poder confirmar un compromiso o intento de compromiso, no significa que no haya sucedido. En ocasiones, investigaciones posteriores al análisis inicial pueden revelar nuevas líneas de estudio, por lo que podría resultar valioso almacenar evidencia forense para análisis posteriores, siempre en apego a [políticas de seguridad](https://protege.la/guias-contenido/diseno-politicas-protocolos-lineamientos/) y de retención de la información, así como acuerdos establecidos en el consentimiento informado.

En los últimos años, diferentes proyectos y fondos que buscan incentivar el análisis forense en la sociedad civil han permitido impulsar la creación de laboratorios de amenazas para apoyar a personas defensoras alrededor del mundo. Esto ha permitido que el ecosistema y las capacidades se amplíen, en especial en el sur global. Sin embargo, **para el éxito de estas iniciativas es importante que se fomente y promueva la colaboración entre pares**, tanto dentro como fuera de la región, para compartir conocimientos e [inteligencia de amenazas](../../references/00-glossary/index.md#inteligencia-de-amenazas). **El establecimiento de un laboratorio forense es usualmente el primer paso en un proceso de maduración** que suele tomar años, por lo que la colaboración, especialmente en las primeras etapas, es fundamental para poder acompañar a personas en riesgo de forma positiva.

## Consideraciones importantes al realizar investigaciones forenses

A continuación se detallan algunos aspectos importantes a considerar al realizar investigaciones forenses en beneficio de personas en riesgo de la sociedad civil:

### Consentimiento Informado

 A diferencia de las investigaciones forenses en otros contextos (periciales o corporativos) las investigaciones forenses en beneficio de personas defensoras de derechos humanos **deben ser siempre consentidas**. Esto significa que la persona analista debe guiar y describir el proceso, a fin de que la persona defensora comprenda los alcances y pueda tomar una decisión informada sobre el proceder de la investigación, ya sea a través de un acuerdo verbal o escrito.

Es posible que algunos de los artefactos forenses que se recolectan contengan información personal (contactos, mensajes, aplicaciones, entre otros) por lo que mantener una comunicación transparente y respetar siempre las decisiones de la persona defensora debe ser siempre la prioridad. Algunos factores importantes a tomar en cuenta para obtener un consentimiento informado incluyen: qué información se debe recolectar, con quién se va a compartir, por cuánto tiempo se almacenará, entre otros.

[Consulta la guía práctica sobre consentimiento](../../how-tos/01-how-to-obtain-informed-consent/){ .md-button }


### Cadena de custodia

Al proceso de documentar con claridad quién y de qué forma se manipula  la evidencia se le conoce como **cadena de custodia**. La evidencia forense puede ser manipulada o destruída durante el proceso forense, por lo que la persona analista debe ser capaz de demostrar la [integridad de la evidencia](../../references/00-glossary/index.md#integridad-de-la-información).  En caso de que esta demostración no sea posible o suficientemente robusta, es posible que las evidencia **no sea admisible en procesos judiciales**, o sea refutada y desestimada por otros especialistas.

!!! abstract "Consideración Legal"
    Si la intención es utilizar evidencia forense para procesos judiciales es recomendable asesorarse con personas especialistas en el marco legal local. 

La mejor forma de demostrar y verificar la integridad de la evidencia es a través de **documentación** clara, que incluya hashes (identificadores únicos) o [firmas digitales](https://oneflow.com/es/blog/pki-de-firma-digita/) de los archivos recolectados, así como una cronología del proceso, que permita entender con claridad el manejo de la evidencia desde su identificación hasta la presentación. Existen algunas empresas que brindan servicios para registrar y verificar la integridad de pruebas en apego a marcos jurídicos, como por ejemplo [Verifact en Brasil](https://www.verifact.com.br/).

### Riesgos durante una investigación forense

Las investigaciones forenses pueden exponer abusos de Derechos Humanos en perjuicio de personas en riesgo por parte de estados u otros actores, en ocasiones con la complicidad de empresas proveedoras de tecnologías de espionaje. Debido al **impacto** que estas investigaciones pueden tener, tanto para los **estados como para las empresas con capacidades avanzadas**, existe una oposición y recursos para obstaculizar, paralizar y hasta criminalizar los esfuerzos de laboratorios de amenazas de la sociedad civil.

Es importante que antes de iniciar una práctica forense, se realice una **evaluación de riesgos holística**, que considere tanto a las personas analistas como a quienes sufren los ataques, a fin de establecer medidas de prevención y respuesta. Este análisis de riesgos debe enfocarse no solamente en aspectos digitales, sino también legales y de seguridad física. Algunas organizaciones que brindan apoyo para análisis de riesgos se listan en el [sitio de primeros auxilios digitales](https://digitalfirstaid.org/support/).

Además, por la naturaleza de la práctica forense, se estará frecuentemente en contacto con infraestructura maliciosa por lo que definir medidas de [**seguridad operaciona**](https://es.ifixit.com/Wiki/OPSEC_and_Personal_Online_Security)**l** que protejan a las personas analistas es fundamental. Y más allá de los riesgos operacionales, debe valorarse el riesgo de alertar a los atacantes sobre una investigación en curso, lo que podría llevar a un cambio en su infraestructura y operación, reduciendo el éxito de la investigación.

[Consulta el explainer sobre riesgos](../02-explainer-risks-threats/){ .md-button }

## Conclusión

La forense digital involucra una serie de **prácticas, metodologías, herramientas, conocimientos técnicos y estándares** que en conjunto permiten establecer conclusiones verificables sobre acontecimientos relacionados a incidentes de seguridad digital. En el contexto de la defensa de Derechos Humanos, la evidencia recolectada a través de investigaciones forenses puede potenciar acciones de rendición de cuentas e incidencia, que reduzcan la impunidad con la que se cometen ataques digitales.

El análisis forense consentido implica un **proceso riguroso a través de una serie de etapas**, donde se busca garantizar y demostrar la integridad de la evidencia y el análisis que se realiza. La mayoría de etapas, a excepción de la fase de análisis, no son técnicamente complejas, pero sí requieren de familiaridad con algunas herramientas y un entendimiento básico de conceptos como la cadena de custodia y el consentimiento informado. Los laboratorios y practicantes de la forense deben también evaluar y tomar medidas para mitigar riesgos que puedan surgir a raíz de las investigaciones.

En conjunto y a través de la confianza laboratorios forenses emergentes y otros ya establecidos pueden colaborar para fortalecer la práctica forense en la sociedad civil. Es a través de la colaboración entre pares que podremos responder de manera holística a las necesidades de las personas defensoras en riesgo.

## Comentarios

¿Tienes **comentarios o sugerencias** sobre este recurso? Puedes utilizar la **función de comentar que se muestra a continuación** para dejarnos tus ideas o apreciaciones. Por favor asegúrate de seguir nuestro [código de conducta](../../community/code-of-conduct/). La función de comentarios enlaza directamente a la sección de [_Discussions_ de Github](https://github.com/Socialtic/forensics/discussions), donde también **puedes participar en las discusiones de forma directa**, si lo prefieres.   


