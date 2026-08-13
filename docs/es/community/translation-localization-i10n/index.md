---
title: Comunidad - Traducciones y localizaciones
summary: Consideraciones sobre traducciones y localizaciones
keywords: forense, comunidad, contribucion, traducción, traducir
lang: es
tags: [comunidad, intro, traducir]
last_updated: 2025-07-14
some_url:
author:
    name: Daniel
    url: https://socialtic.org/quienes-somos/
    description: SocialTIC
auto-translate: false
---


Desde SocialTIC comprendemos la importancia de mantener **recursos accesibles**, de **fácil lectura** y que puedan generar un impacto en **poblaciones con diferentes capacidades técnicas y en múltiples regiones del mundo**. Debido a nuestra experticia y ubicación geográfica, nuestros recursos frecuentemente estarán **disponibles primero en idioma español,**  y de forma posterior se traducirán a los demás idiomas disponibles. 

Para facilitar este proceso de traducción, se desarrolló un script que utiliza la API de *deepl* para generar traducciones automáticas e integrarlas a través de pull requests. Este script se [describe a detalle en la documentación correspondiente](https://github.com/socialtic/forensics/blob/main/scripts/translate-readme.md). Este script automático requiere de revisiones manuales, por lo que si tienes interés en **colaborar con la traducción de recursos del español al inglés**, o viceversa, por favor escríbenos a [**seguridad@socialtic.org**](mailto:seguridad@socialtic.org). 

Si bien este script de traducción automática facilita la localización de recursos, existen algunas consideraciones importantes antes de iniciar una traducción: 

* Capacidad y sostenibilidad: La traducción y localización de contenidos es un **trabajo arduo,** y desde **SocialTIC agradecemos cualquier esfuerzo** que impulse el análisis forense consensuado en poblaciones vulnerables, especialmente de la mayoría global. Sin embargo, antes de iniciar una traducción, recomendamos **evaluar la sostenibilidad del esfuerzo**  en el mediano-largo plazo.  
* Revisión de los contenidos: En nuestra experiencia, es ideal que además de la traducción inicial, **una segunda persona realice una revisión secundaria**. Si tienes problemas para identificar una segunda contraparte para revisar una traducción, puedes informarnos para apoyar en la coordinación.   
* Actualización y mantenimiento: Nuestra visión es que el **repositorio estará en constante crecimiento y actualización**. Esperamos que los **primeros años sean los más intensos** en la producción de contenidos de triaje y adquisición, para luego enfocarse en contenidos más especializados.   
* Reglas de estilo: Sugerimos generar unas reglas de estilo breves que consideren por ejemplo el **uso de anglicismos, lenguaje inclusivo, entre otros**.    
* Licencia de uso:  Este repositorio extiende [la licencia de MVT](https://docs.mvt.re/en/latest/license/) para fomentar el análisis forense consensuado. 

### Organización de los contenidos

El repositorio se encuentra **estructurado para aceptar traducciones a nuevos idiomas**. Para el manejo de las traducciones se utiliza el [plug-in mkdocs-static-i18n](https://ultrabug.github.io/mkdocs-static-i18n/). 

Se utilza la configuración de carpetas, por lo que en general, los contenidos en todos los idiomas **se estructuran de la siguiente manera**, con los **nombres de carpetas en idioma Inglés**. Se muestra a continuación la estructura para el idioma español: 

```
docs/
  es/
    localized-assets/
      resource 1/
        image1.png
    home/
      getting-started/
        index.md
      roadmap/
        index.md
    explainers/
      explainer-topic-01/
        index.md
      explainer-topic-n/
        index.md
    how-tos/
      how-to-topic-01/
        index.md  
      how-to-topic-n/
        index.md
    tutorials/
      tutorial-topic-01/
        index.md  
      tutorial-topic-n/
        index.md
    references/
      reference-topic-01/
        index.md
      reference-topic-n/
        index.md
    index.md

```

**Cada nuevo contenido tendrá su propia carpeta correspondiente**, donde se aloja el archivo en formato markdown de nombre 'index.md' con los contenidos. Por ejemplo, el contenido *Explainer:* *Introducción a la forense digital consentida para la defensa de los derechos humanos* se organiza de la siguiente forma en el idioma inglés y español: 

```
es/
  explainers/
    01-explainer-introduction-digital-forensics/
      index.md

en/
  explainers/
    01-explainer-introduction-digital-forensics/
      index.md
	
```

Tal y como se observa, **no existen diferencia en el nombre de los archivos o carpetas**, y la única diferencia radica en el folder en el cual se ubica la documentación. 

Para realizar contribuciones directamente al repositorio en relación a traducciones, se recomienda seguir las instrucciones en la sección de *pull requests* o [solicitudes de integración](../how-to-contribute/index.md#solicitudes-de-integracion-a-traves-de-pull-request). 
