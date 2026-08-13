---
title: Explainer - Riesgos y amenazas para laboratorios forenses de la sociedad civil
summary: Riesgos y amenazas que enfrentan analistas y laboratorios forenses de la sociedad civil, y recursos para hacer análisis.
keywords: riesgo, amenaza, mitigación, analisis de riesgos
lang: es
tags: [explainer, intro]
last_updated: 2025-05-27
some_url:
comments: true
created: 2025-05-27
authors:
    - Daniel Bedoya
    - Gurshabad Grover

---

# Explainer: Riesgos y amenazas para laboratorios forenses de la sociedad civil

Este documento forma **parte de un repositorio de documentación técnica** que tiene como objetivo establecer una base de conocimientos probados, flexibles y accesibles para **impulsar el análisis forense consentido en beneficio de la sociedad civil**. Para organizar los contenidos, se utiliza el [marco de referencia de documentación técnica Diataxis](../../references/00-glossary/index.md#diataxis).

Este recurso en particular se enmarca dentro de la categoría de [explainers](https://diataxis.fr/explanation/), y **describe los riesgos, amenazas y vulnerabilidades** que analistas y laboratorios forenses de la sociedad civil enfrentan por causa de su trabajo. Es un material introductorio que incluye ejemplos y enlaces a recursos preventivos que pueden ayudar a entender y mitigar los riesgos a los que se enfrentan.

La versión original de este documento fue co-elaborada en idioma inglés en conjunto con el equipo de Internet Research Lab. La traducción fue liderada por el equipo de SocialTIC. Agradecemos las revisiones y sugerencias de Access Now y Marianne Parrott para este mejorar el contenido en su versión original. Cualquier error o omisión es responsabilidad de los autores.

## Amenazas, vulnerabilidades y riesgos: ¿por qué debemos prestar atención?

En el contexto de la seguridad en línea para personas u organizaciones en riesgo de la sociedad civil, **una amenaza** se refiere a eventos o posibles situaciones que pueden poner en peligro o dañar a personas o recursos, incluyendo dispositivos y cuentas en línea. Las amenazas pueden ser de diferentes tipos (físicas, legales o digitales) y tener diferentes causas (desastres naturales, robos, ataques dirigidos, etc). 

Por otro lado, una **vulnerabilidad** se refiere a una deficiencia o debilidad en procesos, sistemas, prácticas o hábitos que pueden propiciar amenazas o incrementar el impacto y las consecuencias de un incidente. 

El **riesgo** resulta de combinar la posibilidad de que una amenaza se materialice con la severidad del impacto, si termina ocurriendo. El riesgo no es un concepto estático; varía con el tiempo, dependiendo de factores internos y externos, por lo que realizar ejercicios regulares de análisis de riesgos es una práctica necesaria para reducir la probabilidad y severidad de las amenazas. 

En el contexto de la forense consentida en beneficio de la sociedad civil, como describimos anteriormente en [nuestro explainer sobre forense para la defensa de los derechos humanos](../01-explainer-introduction-digital-forensics/), el proceso de atención usualmente inicia cuando una persona defensora de Derechos Humanos se acerca a un punto de contacto o a un laboratorio de amenazas para solicitar asistencia. En muchos casos, y **en particular cuando se sospecha de una amenaza avanzada**, es posible que la persona se encuentre en un **contexto de alto riesgo, expuesta a ataques digitales, legales, físicos y psicosociales**. 

Los riesgos particulares que una organización o individuo enfrenta, **dependen del contexto y de su trabajo particular**. Si bien el enfoque de las investigaciones forenses no es la contención y mitigación de amenazas, **es importante tener conciencia del entorno de riesgos**, y evitar iniciar acciones que puedan llevar a un incremento en los daños e impactos experimentados por la persona en riesgo. 

Este recurso se enfoca principalmente en los *riesgos para los laboratorios forenses* apoyando a personas defensoras de derechos humanos, pero es importante extender el ejercicio de análisis a otros procesos, servicios o políticas que puedan impactar el bienestar de las personas en riesgo. 

Adicionalmente, es importante que los laboratorios forenses, analistas y puntos de contacto **también consideren los riesgos a los que se expone su personal y sus operaciones al participar en investigaciones técnicas.** A través de estas investigaciones, la sociedad civil busca impulsar acciones de rendición de cuentas que pueden tener un impacto en la industria de vigilancia, al exponer evidencia de prácticas ilegales o carentes de ética. Por este motivo, **algunos actores de la industria pueden incluso considerar a los analistas e investigadores de sociedad civil como una amenaza**. 

En las próximas secciones presentaremos un detalle de los tipos de actores, amenazas y ataques que investigadores y laboratorios de amenazas han sufrido en el pasado, así como una serie de recursos para iniciar ejercicios de análisis de riesgos. 

## ¿De dónde vienen las amenazas?

Para conocer de forma precisa de dónde vienen las amenazas que una persona analista o un laboratorio de amenazas enfrenta en un momento determinado es necesario realizar un [ejercicio de análisis de riesgo](https://protege.la/guias-contenido/analisis-de-riesgos-como-evaluar-y-mitigar-riesgos-en-internet/). Sin embargo, es posible listar algunos actores de amenazas (threat actors) que han sido identificados a partir de investigaciones anteriores: 

* **Empresas y comercializadoras de spyware y herramientas de vigilancia**: Hoy, en 2025, podemos afirmar que existe un [ecosistema amplio de empresas](https://storage.googleapis.com/gweb-uniblog-publish-prod/documents/Buying_Spying_-_Insights_into_Commercial_Surveillance_Vendors_-_TAG_report.pdf) que desarrollan, comercializan e implementan tecnologías de vigilancia, en su mayoría de capital privado y con fines de lucro. Existen algunos listados de estas empresas, incluyendo esta publicación por el [Atlantic Council](https://www.atlanticcouncil.org/in-depth-research-reports/report/markets-matter-a-glance-into-the-spyware-industry/) o [este recurso de la organización Business and Human Rights](https://www.business-humanrights.org/en/companies/). Con frecuencia, las empresas, fundadores o empleados tienen vínculos con el sector militar y de inteligencia. Por ejemplo, en el caso de la empresa NSO Group, [uno de los co-fundadores fue parte de la agencia de inteligencia Israelí Mossad](https://en.wikipedia.org/wiki/NSO_Group#Founding). En general, son actores con capacidades técnicas, recursos financieros, consejería legal y en algunas ocasiones conexiones e influencia política. Las investigaciones de la sociedad civil pueden tener un impacto en los negocios y la reputación de estas empresas, como lo fue la millonaria multa impuesta a NSO como parte del [castigo en el caso WhatsApp vs. NSO](https://thehackernews.com/2025/05/nso-group-fined-168m-for-targeting-1400.html) o el [impacto a la empresa Cellebrite a raíz de las investigaciones lideradas por Amnesty International](https://www.amnesty.org/en/latest/news/2025/02/cellebrite-halts-product-use-in-serbia-following-amnesty-surveillance-report/) en Serbia y otros países. 


* **Actores estatales:** En algunas ocasiones, los estados, policías, militares o agencias de inteligencia actúan como los **operadores de tecnologías de vigilancia**, lo que significa que mantienen el control sobre quién es atacado, cuando, por cuánto tiempo y con qué fin. Si bien muchos gobiernos dependen de herramientas comerciales o soluciones de spyware mercenario, algunos estados tienen la capacidad para desarrollar su propia tecnología, con diferentes niveles de sofisticación técnica. La investigación forense de parte de la sociedad civil puede llevar a la exposición de abusos y violaciones de Derechos Humanos de parte de los Estados, e incluso la rendición de cuentas a través de procesos judiciales. Por ende, muchos actores dentro de los estados buscan obscurecer, obstaculizar e incluso criminalizar la investigación forense desde la sociedad civil. 

* **Troles y actores de desinformación:** Conforme nuevos reportes continúan exponiendo el mal uso de tecnologías de vigilancia, al menos desde el año 2022 han aparecido [actores persistentes, especialmente en redes sociales](https://www.cmu.edu/ideas-social-cybersecurity/events/syynimaa_attacking_ngo.pdf), que utilizan la desinformación y pseudociencia para desacreditar hallazgos e investigaciones. Estas campañas resultan en acoso a investigadores u organizaciones, y distraen a las personas investigadoras de sus labores. En algunos contextos, en especial donde existen [redes sólidas para la manipulación de algoritmos y discursos](https://cjp.org.in/india-among-nations-manipulating-social-media-oxford-study/), con frecuencia aparecen redes de troles en conexión con eventos como notificaciones de amenazas, para esparcir desinformación y desacreditar esfuerzos de investigación y rendición de cuentas. 

* **Empresas de ciberseguridad con fines de lucro:** En los últimos años, han aparecido algunas empresas privadas de ciberseguridad que buscan lucrar a través de productos orientados a detectar y prevenir infecciones de Spyware. Estas empresas, en algunas ocasiones, se acercan a la sociedad civil en búsqueda de inteligencia de amenazas o indicadores de compromiso, que les permita avanzar sus investigaciones y productos. Debido a la diferencia en incentivos y recursos, en muchas ocasiones estas relaciones resultan en acuerdos extractivistas, que pueden terminar por dañar la reputación de laboratorios forenses, y potencialmente tener un impacto en las víctimas si su información no se maneja de forma responsable. Algunos ejemplos específicos han sido reportados de forma privada, e incluso [algunas críticas y discusiones públicas hacen hincapié en el oportunismo y las prácticas poco éticas de empresas como empresa iVerify](https://discuss.grapheneos.org/d/14993-debunking-fake-stock-pixel-os-vulnerability-from-an-edr-company). 

## Ejemplos de amenazas 

A pesar de que no es posible compilar una lista completa de todas las amenazas que un laboratorio forense puede enfrentar, podemos partir de ejemplos y reportes anteriores para explorar algunos ejemplos de amenazas que han sido documentadas. 

### Digitales

Por ataques digitales, nos referimos a acciones o comportamientos con una intención maliciosa, que utilizan tecnologías digitales. Por ejemplo: 

* **Phishing dirigido:** El phishing dirigido se refiere a mensajes bien construidos, personalizados con información confidencial o sensible, y que buscan que el receptor abra enlaces o descargue adjuntos maliciosos. Esta técnica ha sido utilizada anteriormente en perjuicio de la sociedad civil. Por ejemplo, en 2024 [Citizen Lab y Access Now documentaron como un actor avanzado utilizó phishing dirigido](https://citizenlab.ca/2024/08/sophisticated-phishing-targets-russias-perceived-enemies-around-the-globe/) para comprometer cuentas de investigadores de alto perfil que se encontraban desarrollando un reporte sobre corrupción y abusos de poder en Rusia.  
  
* **Ataques de spyware**: Anteriormente se han documentado situaciones donde investigadores y activistas de la sociedad civil han sido víctimas de ataques de Spyware. Por ejemplo, en 2024 [Access Now reportó](https://www.accessnow.org/publication/between-a-hack-and-a-hard-place-how-pegasus-spyware-crushes-civic-space-in-jordan/#who-was-hacked) como miembros de Human Rights Watch (HRW) en Jordania fueron víctimas de Spyware. El ataque sucedió luego de que el equipo de HRW lanzara un reporte criticando la represión por parte del gobierno. 

* **Doxxing (doxing o doxeo)**: El doxxing consiste en la recolección y publicación de información sensible y confidencial sobre una persona, como su dirección física o número telefónico, en especial utilizando fuentes abiertas de información disponible en Internet (OSINT, o [inteligencia de fuentes abiertas](https://es.wikipedia.org/wiki/Inteligencia_de_fuentes_abiertas)). Si bien hay pocos reportes públicos sobre doxing en perjuicio de analistas o laboratorios forenses, varios casos han sido reportados de forma privada.

* **Compromisos o fugas de información**: Los adversarios pueden intentar obtener acceso a información sensible como por ejemplo la identidad de las víctimas que buscan apoyo, o información sobre infraestructura, vulnerabilidades o indicadores de compromiso que no es pública. Adicionalmente, los adversarios podrían buscar tener acceso a información sensible sobre el personal del laboratorio forense, en especial si las investigaciones se han llevado a cabo a través del uso de alias o pseudónimos. Es importante tener en cuenta que los ataques también pueden ser dirigidos a proveedores de servicios, como por ejemplo sistemas de manejo de casos o de almacenamiento de información en la nube. En el año 2022, se reportó un ataque en contra del Comité Internacional de la Cruz Roja (IRCC) que [comprometió registros sensibles luego de un compromiso en un proveedor de servicio utilizado por la organización](https://www.theregister.com/2022/01/20/red_cross_hit_by_cyberattack/).

### Legales

Los ataques legales pueden suceder cuando los estados utilizan leyes de seguridad nacional o ciberseguridad para criminalizar las acciones y actividades de analistas y laboratorios forenses. También es posible que las amenazas legales se presenten por parte de empresas de spyware como parte de procesos de litigación. 

* **Criminalización de las investigaciones forenses:** En 2019 en Ecuador, el investigador Ola Bini fue [arrestado y acusado de cargos bajo la ley de cibercrimen](https://www.eff.org/deeplinks/2023/03/aftermath-ola-binis-unanimous-acquittal-ecuadorian-court). Ola fue parte de un extenso proceso legal, plagado de errores, y donde a pesar de haber sido absuelto de todos los cargos en 2023, aún [continúa batallando con apelaciones y procedimientos legales.](https://peoplesdispatch.org/2024/04/08/activist-ola-bini-sentenced-to-one-year-in-prison-after-ecuadorian-court-overturns-acquittal/)  
  
* **Guerra legal (lawfare)**: Guerra legal o lawfare se refiere al uso del sistema o instituciones legales para dañar, desacreditar o afectar individuos o organizaciones. Por ejemplo, en relación al caso en las cortes de Estados Unidos entre NSO y WhatsApp, el Citizen Lab enfrentó una serie de recursos y solicitudes legales que buscaban desmantelar su trabajo y acceder a información sensible, incluída la lista de víctimas. En otro ejemplo, en 2018 la empresa Candiense Sandvine amenazó al Citizen Lab con una demanda por difamación a raíz de su publicación concerniente al uso de equipos Sandvine para la implantación de spyware.  
  
* **Citas judiciales y solicitudes de datos (subpoenas)**: En línea con los esfuerzos por criminalizar las investigaciones forenses, es posible que las autoridades utilicen recursos y procesos legales, como subpoenas y solicitudes de datos, para obtener información personal sobre analistas y laboratorios forenses. Por ejemplo, en 2019, el investigador argentino Javier Smaldone [hizo público una serie de solicitudes hechas por la policía](https://peoplesdispatch.org/2024/04/08/activist-ola-bini-sentenced-to-one-year-in-prison-after-ecuadorian-court-overturns-acquittal/) a proveedores de servicio, incluído WhatsApp.  
  
* **Subpoenas and data requests:** In line with attempts to criminalize research, it is possible that authorities try to use legal processes, subpoenas and other mechanisms to obtain personal information of researchers or forensic labs. For example, in 2019, the Argentinian researcher Javier Smaldone made [public data requests made by the police to ISPs and service providers](https://blog.smaldone.com.ar/2020/01/25/allanado-y-detenido-por-tuitear/) (including WhatsApp). 

### Reputacionales

Los laboratorios forenses también pueden sufrir una serie de amenazas a su reputación, algunas veces a través de afirmaciones sin fundamento o campañas de desinformación. Trolls y redes de manipulación de la información pueden propagar y hacer eco de estas campañas en un esfuerzo por desacreditar resultados y menoscabar las llamadas a rendición de cuentas. 

* **Publicaciones y pseudociencia:** La pseudociencia se refiere a afirmaciones, creencias o prácticas que se dicen científicas y verificables pero que en realidad no son compatibles con el método científico. Anteriormente, investigaciones por parte de Citizen Lab y Amnistía Internacional fueron criticadas por “expertos” en ciberseguridad, lo que generó disrupciones en su trabajo. Ejemplos incluyen [perfiles en redes sociales que intentaron desacreditar la investigación de Citizen Lab \#CatalanGate](https://medium.com/@maldr0id/misinformation-in-malware-analysis-232c7bb6b73e). 

### Físicas

Los ataques o amenazas físicas buscan intimidar y desincentivar el uso de las ciencias forenses para investigaciones en la sociedad civil.. 

* **Acoso y vigilancia física:** En el año 2020, el periódico [New York Times publicó un artículo donde se reporta un caso de acoso y vigilancia en perjuicio de un investigador del Citizen Lab](https://www.nytimes.com/2019/01/28/world/black-cube-nso-citizen-lab-intelligence.html) por parte de un espía Israelí. 
  
* **Detenciones, allanamientos y arrestos:** Como se mencionó antes, diferentes leyes puden ser utilizadas para criminalizar las investigaciones forenses, incluyendo leyes de ciberseguridad y seguridad nacional. A través de la aplicación desmedida y dirigida de estas leyes, se puede criminalizar y detener los esfuerzos de investigación forense. Por ejemplo, en el año 2019, el investigador Argentino [Javier Smaldone fue víctima de detenciones simplemente por criticar la seguridad de las máquinas de sufragio electrónico](https://blog.smaldone.com.ar/2020/01/25/allanado-y-detenido-por-tuitear/).

### Psicosociales

Los analistas y laboratorios forenses también sufren de consecuencias a su bienestar emocional a raíz de su apoyo a personas en riesgo víctimas de spyware. [Este reporte de Access Now describe el impacto psicológico](https://www.accessnow.org/women-human-rights-defenders-pegasus-attacks-bahrain-jordan/) que enfrentan las personas víctimas de spyware, lo que usualmente requiere apoyo emocional y contención, frecuentemente de los puntos de contacto o líneas de ayuda de la sociedad civil. 

* **Fatiga de compasión o trauma secundario:** [La fatiga de compasión](https://www.unir.net/revista/salud/fatiga-por-compasion/) o [trauma secundario](https://en.wikipedia.org/wiki/Secondary_trauma#cite_note-Cieslak_2014-1) se refieren a traumas psicológicos que se presentan debido al contacto con una persona que haya experimentado un evento traumático (como la infección de sus dispositivo con spyware), la exposición a descripción  
  
* **Síndrome de desgaste profesional (burnout)**: [El síndrome de desgaste profesional](https://es.wikipedia.org/wiki/S%C3%ADndrome_de_desgaste_profesional) o burnout es un estado crónico de estrés que conlleva a padecimientos físicos y desgaste emocional, generando sentimientos de cinismo, desapego e inefectividad. El burnout puede inhabilitar a una persona a nivel profesional. Quienes sufren de burnout podrían necesitar tiempo libre adicional para recuperar su salud física y mental, o incluso en determinadas situaciones podrían no ser capaces de reintegrarse a sus tareas usuales.

### Operacionales

Aparte de posibles amenazas digitales, físicas, legales y psicosociales, es importante tener presente los riesgos relacionados a la parte operativa y la sostenibilidad de los laboratorios forenses. 

* **Sostenibilidad y acceso a recursos:** La provisión provisión de servicios de análisis forense requiere una combinación de experticia técnica, acceso a herramientas, experiencia y procedimientos. Usualmente los laboratorios forenses atraviesan un proceso de madurez que suele tardar varios años. Por lo tanto, es importante que los laboratorios forense consideren una estrategia para su sostenibilidad, en especial mientras se desarrollan y fortalecen las habilidades necesarias para llevar a cabo investigaciones forenses.  
  
* **Retención de personal:** Existe una [escasez de personal técnico](https://www.weforum.org/stories/2024/04/cybersecurity-industry-talent-shortage-new-report/) con conocimientos en seguridad digital, y en particular con experiencia en ciencias forenses. La sociedad civil no es la excepción, y múltiples organizaciones y laboratorios de amenazas han enfrentado dificultades para encontrar y contratar personal técnico que al mismo tiempo tenga la sensibilización necesaria para trabajar con personas en riesgo. También debe tomarse en cuenta el riesgo de que las personas técnicas persigan nuevas oportunidades mejor remuneradas en el sector privado.  
  
* **Infraestructura y servicios resilientes**: El trabajo de los laboratorios forenses se ve afectado por eventos y factores externos, como por ejemplo un aumento en el número de solicitudes a raíz de una crisis social o política. Por ejemplo, se ha reportado anteriormente incrementos en la cantidad de solicitudes a raíz de publicaciones virales en redes sociales impulsando a contactar en masa a líneas de asistencia o servicios de apoyo, lo que termina por desbordar e impedir la provisión de servicios. Es importante explorar este tipo de escenarios para poder desarrollar planes de contingencia e infraestructura resiliente. 


## Prevención y manejo de los riesgos

Como hemos mencionado a lo largo de este recurso, instamos a los analistas y laboratorios de amenazas forenses apoyando a personas en riesgo de la sociedad civil a completar ejercicios de evaluación de riesgos de forma regular, y de forma particular antes de iniciar investigaciones con personas en contextos de alto riesgo. 

Este recurso **no es una guía paso a paso para realizar un análisis de riesgos,** sin embargo enlazamos a diferentes recursos y organizaciones cercanas que pueden brindar asistencia para prevenir diferentes tipos de amenazas. 

### Recursos para análisis de riesgos

Los siguientes son algunos recursos para iniciar ejercicios de análisis de riesgos: 

* [Cybersecurity Assessment Tool (CAT)](https://cybercat.tools/#assessment): La herramienta de análisis de ciberseguridad, o CAT por sus siglas en Inglés, es una herramienta diseñada para medir el nivel de madurez, resiliencia y fortaleza de una organización en relación a su ciberseguridad. Puede ayudar a los laboratorios de amenazas, o las organizaciones donde se hospedan, a identificar sus propios riesgos, amenazas, vulnerabilidades y oportunidades.  
  
* [SAFETAG](https://safetag.org/): SAFETAG es un marco de referencia para sociedad civil que adapta modelos tradicionales de pruebas de penetración y análisis de riesgos para que sean útiles y prácticos para organizaciones pequeñas o medianas de la sociedad civil.  
  
* [Plan de seguridad (EFF)](https://ssd.eff.org/module/your-security-plan): EFF tiene a disposición un recurso bajo sus guías de SSD específicamente orientado a individuos o analistas independientes para crear un plan para manejar riesgos digitales. 

### Organizaciones y redes de apoyo

La siguiente es una lista de organizaciones que pueden apoyar en el análisis, la mitigación y el manejo de diferentes tipos de riesgos: 

**Digitales o técnicos**

* [Access Now Digital Security Helpline](http://accessnow.org/help) 
* [Cyber hub](https://cyberhub.am/en/) 
* [SocialTIC](https://socialtic.org/) 
* [Frontline Defenders](https://www.frontlinedefenders.org/)  
* [Open briefing](https://openbriefing.org/)  

      
**Legal**   

* [Media Legal Defense Initiative](https://www.rcmediafreedom.eu/Tools/Support-centres/Media-Legal-Defence-Initiative-MLDI)  
* [Access Now](http://accessnow.org/help)  
* [Article 19](https://www.article19.org/regional-office/mexico-and-central-america/)

**Psicosocial y bienestar**

* [Línea de atención feminista de vita activa](https://vita-activa.org/)   
  * Entre sus recursos, se incluyen prácticas para [lidiar con el trauma indirecto](https://vita-activa.org/2021/02/08/trauma-indirecto/) y recursos sobre el síndrome de [desgaste laboral y cómo afecta más a mujeres](https://vita-activa.org/2022/03/15/el-burnout-por-que-afecta-mas-a-las-mujeres/).   
* [Open briefing](https://openbriefing.org/)  
  * Entre sus recursos se incluye una [herramienta para análisis de riesgos](https://www.openbriefing.org/services/security/risk-assessments/) y un recurso sobre [la fatiga de compasión y trauma vicario en personas que apoyan a defensores de derechos humanos](https://openbriefing.org/resources/compassion-fatigue-vicarious-trauma-and-burnout-infosheet-for-those-supporting-human-rights-defenders/).   
      
**Seguridad física**   

* [Frontline Defenders](https://www.frontlinedefenders.org/)  
      
**Sostenibilidad**   

* [Engine Room](https://www.theengineroom.org/)  
  * Entre sus recursos se incluye una [material sobre compensación en un equipos remotos globales](https://www.theengineroom.org/library/rethinking-compensation-for-a-global-remote-team/) así como un reporte sobre [cómo identificar fuentes sostenibles de financiamiento](https://www.theengineroom.org/library/tipping-the-scales-what-it-takes-to-fund-an-equitable-tech-human-rights-ecosystem/). 

**Recursos para responder a incidentes**  

* [Feminist Helplines](https://feministhelplines.org/)  
* [DFAK](https://digitalfirstaid.org/) \- Kit de primeros auxilios digitales

    

## Conclusión

A través de este documento hemos presentado una descripción de las actores de amenazas y los riesgos a los que se enfrentan los analistas y laboratorios forenses de la sociedad civil debido a su trabajo. Existe un ecosistema amplio de actores de amenaza que buscan prevenir o dificultar los esfuerzos de análisis forense. Recomendamos iniciar ejercicios individuales de análisis de riesgos, y en especial antes de iniciar investigaciones en contextos de alto riesgo. 

Nuestra intención a través de este documento no es minimizar o socavar esfuerzos emergentes para hacer más análisis forense desde la sociedad civil. Al contrario, **resaltamos la importancia de implementar prácticas y políticas de seguridad operacional de forma tal que se inicien investigaciones de forma responsable** y sin incrementar el riesgo para personas, ya de por sí, en situaciones vulnerables. 

**Te invitamos a colaborar con la documentación en este repositorio**. Si tienes alguna observación o solicitud, puedes hacerla a través de la [sección de problemas (issues) del repositorio](../../community/how-to-contribute/index.md#propuestas-de-mejora-o-correcciones-a-traves-de-issues). Si tienes recursos que deseas integrar a este repositorio documental, escríbenos a [seguridad@socialtic.org](mailto:seguridad@socialtic.org). 



## Comentarios

¿Tienes **comentarios o sugerencias** sobre este recurso? Puedes utilizar la **función de comentar que se muestra a continuación** para dejarnos tus ideas o apreciaciones. Por favor asegúrate de seguir nuestro [código de conducta](../../community/code-of-conduct/). La función de comentarios enlaza directamente a la sección de [_Discussions_ de Github](https://github.com/Socialtic/forensics/discussions), donde también **puedes participar en las discusiones de forma directa**, si lo prefieres.   


