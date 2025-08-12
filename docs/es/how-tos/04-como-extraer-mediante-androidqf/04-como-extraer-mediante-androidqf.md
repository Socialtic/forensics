---
title: Adquisición y extracción de dispositivos Android mediante AndroidQF
summary: Adquisición y extracción de dispositivos Android mediante AndroidQF 
keywords: android, adquisicion, extraccion, androidqf
authors: 
tags: [androidqf, extraction, acquisition, adquisicion, extraccion]
last_updated: 2025-08-01
some_url:
created: 2025-08-01
author:
    name: José Martínez
    url: https://socialtic.org/quienes-somos/
    description: SocialTIC

---

# Guia: ¿Cómo realizar una extracción mediante AndroidQF?

Este recurso se enmarca dentro de la categoría de [Guia, how-to](../how-tos/), y contiene las instrucciones para realizar una extracción forense con la herramienta [AndroidQF](../../references/00-glossary.md#androidqf).

## ¿Qué es AndroidQF?

[AndroidQF](https://github.com/mvt-project/androidqf) es una herramienta de software libre y de código abierto **enfocada en la extracción forense de dispositivos Android**. Actualmente mantenida por el [Laboratorio de Seguridad de Amnistía Internacional](https://securitylab.amnesty.org/es/). 

Su enfoque está pensado especialmente para periodistas, activistas, defensores de derechos humanos y los **laboratorios técnicos que acompañan casos de vigilancia digital y amenazas de software espía.**

AndroidQF funciona como un [wrapper](https://developer.mozilla.org/en-US/docs/Glossary/Wrapper) forense sobre [ADB](../../references/00-glossary.md#adb), automatizando comandos comunes mediante módulos que **permiten realizar extracciones rápidas, seguras y locales desde cualquier sistema operativo (Linux, Windows o macOS)**, sin depender de servicios en la nube ni instalaciones complejas.

Su utilidad en contextos de sociedad civil radica en su **[portabilidad](../../references/00-glossary.md#herramienta-portable), facilidad de uso y ejecución local.**

Esta guía es complementaria se complementa con otros materiales, como el [diccionario de archivos generados por AndroidQF](../references/01-reference-diccionario-androidqf/01-reference-diccionario-androidqf.md), sus formatos y recomendaciones de uso o el [explainer sobre forense basada en logs para dispositivos Android](../explainers/03-explainer-forense-logs-android/03-explainer-forense-logs-android.md).

## ¿Qué necesito para realizar una extracción con AndroidQF?

Para poder realizar una extracción con AndroidQF es **necesario**:

* El **dispositivo Android a ser analizado**: Activar el **[modo desarrollador](../../references/00-glossary.md#modo-de-desarrollador)** y **[activar la depuración por USB](../../references/00-glossary.md#adb)**. De ser necesario, consulta nuestras [guías sobre habilitar opciones de desarrollador](../02-como-habilitar-opciones-desarrollador/02-como-habilitar-opciones-desarrollador.md) o [la guía sobre cómo habilitar ADB](../03-como-habilitar-adb/03-como-habilitar-adb.md). 
* **Computadora Windows, Linux o Mac**: Se utilizará para realizar la extracción. Es necesario conocer cuál es [chip integrado del equipo](https://servernet.com.ar/como-saber-si-mi-procesador-es-amd-o-arm/) 
* Tener un **cable para transferencia de archivos** telefono-computadora. 

## Pasos para obtener un extracción forense con AndroidQF

A continuación se presentan los pasos detallados para realizar la extracción forense:

### :material-numeric-1-box: Descargar el binario en AndroidQF

* **Descarga** la versión más reciente del [binario](../../references/00-glossary.md#binario), y que **corresponda a la arquitectura del equipo** de cómputo donde se va a ejecutar. La descarga se realiza de los releases del repositorio: [https://github.com/mvt-project/androidqf/releases/](https://github.com/mvt-project/androidqf/releases/) 

    !!! question "¿Cómo identificar la arquitectura?"
        
        Si no estás seguro cuál es la arquitectura del equipo que estás utilizando, consulta este [recurso para conocer cuál es el chip integrado en el dispositivo](https://servernet.com.ar/como-saber-si-mi-procesador-es-amd-o-arm/). 

*  **Crea una nueva carpeta** para almacenar la exrtacción del dispositivo. Mueve el binario recién descargado a esta carpeta.

### :material-numeric-2-box: Asignar permisos de ejecución al binario descargado (**solo Linux y macOS**)

* Si estás utilizando un equipo con **Linux o macOS** para la extracción, es necesario asignar el permiso de ejcución al archivo antes de poder ejecutarlo. Para esto, **abre una terminal y navega a la carpeta donde se encuentra el binario**, luego ejecuta:


    !!! Warning "Completa el nombre"

        Al ejecutar el comando, **asegúrate de completar el nombre** *androidqf_* con el nombre completo del binario descargado en el paso 1. El comando resultante será algo como: 

        ```
        chmod +x ./androidqf_v1.7.1_linux_amd64
        ```


    **En linux:**

    ```
    chmod +x ./androidqf_
    ```

    **En macOS:**

    ```
    chmod +x ./androidqf_
    ```


### :material-numeric-3-box: Conectar el teléfono 

* **Conecta**  el dispositivo desbloqueado a la computadora utilizando un cable de datos USB.

    !!! failure "No todos los cables USB son iguales"

        Algunos cables USB no tienen las conexiones necesarias para transferir datos entre el dispositivo móvil y la computadora. Asegúrate de utilizar un cable que permita transferir datos. Es [difícil distinguirlos a simple vista](https://support.konnected.io/how-to-tell-a-usb-charge-only-cable-from-a-usb-data-cable), pero usualmente los cables de carga rápida o aquellos incluídos con los dispositivos suelen ser cables de datos.  

* Cuando se conecte el teléfono, aparecerá un nuevo mensaje. Selecciona **permitir** cuando el dispositivo Android **solicite permiso de acceso a los datos del dispositivo**, tal y como se muestra en la imagen 1.

    !!! failure "No aparece ningún mensaje"

        Si al conectar el dispositivo a la computadora no te aparece ningún mensaje sobre permisos, revisa lo siguiente: 

        * Asegúrate que la [depuración por USB se encuentre habilitada](../03-como-habilitar-adb/03-como-habilitar-adb.md).
        * Revisa las **configuraciones de USB** y asegúrate que la opción de _transferencia de archivos_ se encuentra habilitada.
        * Asegúrate de que el cable USB sea un **cable de datos**. 

    ![ Captura de pantalla de dispositivo móvil Android Samsung solicitando permiso de acceso a datos.](../04-como-extraer-mediante-androidqf/assets/01-captura-android-permisos-datos.png "imagen 1")
    /// caption
    **Imagen 1**. Captura de pantalla de dispositivo móvil Android Samsung solicitando permiso de acceso a datos.
    ///


### :material-numeric-4-box: Ejecutar AndroidQF 

En este punto es posible ejecutar androidQF siguiendo estas instrucciones:

=== "Linux y MacOS"

    Ejecuta con el **siguiente comando**. **Asegúrate de completar** *androidqf_* con el nombre completo del binario descargado. 
    
    ``` 
    ./androidqf-linux-v?
    ./androidqf-macos-v?
    ```

    ![Captura de pantalla de terminal de linux con ejecución del binario para el inicio de la extracción](../04-como-extraer-mediante-androidqf/assets/02-captura-terminal-linux-ejecucion.png "imagen 2")
    /// caption
    **Imagen 2**. Captura de pantalla de terminal de linux con ejecución del binario para el inicio de la extracción
    ///

=== "Windows"

    * Ingresa a la carpeta donde se guardó el binario descargado en el paso 1, y **da doble click primario sobre el archivo.** Aparecerá una ventana de protección de Windows, da click en **“Más información”**

    ![Captura de pantalla de ventana emergente de protección de Windows.](../04-como-extraer-mediante-androidqf/assets/03-captura-terminal-windows-ejecucion.png "imagen 3")
    /// caption
    **Imagen 3**. Captura de pantalla de ventana emergente de protección de Windows.
    ///

    * Selecciona **“Ejecutar de todas formas”**

    ![Captura de pantalla de ventana emergente de protección de Windows con la selección de ejecutar de todas formas..](../04-como-extraer-mediante-androidqf/assets/04-captura-pantalla-proteccion-windows.png "imagen 4")
    /// caption
    **Imagen 4**. Captura de pantalla de ventana emergente de protección de Windows con la selección de ejecutar de todas formas.
    ///



### :material-numeric-5-box: Confirmar y configurar la extracción 

Los próximos pasos se aplicarán de la **misma manera** en los 3 sistemas operativos considerados en este tutorial: **Linux, Windows and macOS.**

* **AndroidQF identificará el dispositivo de forma automática una vez que permita la depuración USB** y generará una carpeta con un identificador único (UUID). En esta carpeta se almacenará la extracción. 

    !!! question ¿Qué es un UUID?  

        Es un número generado de forma aleatoria, tse expresa mediante 32 dígitos hexadecimales divididos en cinco grupos separados por guiones de la forma 8-4-4-4-12 lo que da un total de 36 caracteres (32 dígitos y 4 guiones), por ejemplo ```0caba18f-20a7-48d0-b9ba-724fdaa3ff85```

* Posteriormente **AndroidQF preguntará el tipo de respaldo** que realizará la herramienta:

    * **Only** **SMS**: Realiza un respaldo limitado que incluye solo mensajes SMS y MMS.
    * **Everything**: Ejecuta un respaldo completo del dispositivo mediante adb backup.
    * **No** **Backup**: Omite completamente la generación de respaldos; solo extrae otros artefactos vía ADB.


    !!! warning "Alternativa"

        Para el ejemplo usamos la opción **Only-SMS** para limitar la extracción únicamente a mensajes, reduciendo la exposición de datos personales innecesarios. Si el **contexto del caso se considera de alto riesgo** o implica investigación más sofisticada se recomienda marcar la opción  **Everything**, aunque la opción **Only-SMS** en la mayoría de los casos sigue siendo suficiente para buscar intentos de phishing mediante SMS.


    ![Captura de pantalla de terminal de linux con el menú backup de AndroidQF y la opción Only SMS seleccionada.](../04-como-extraer-mediante-androidqf/assets/06-captura-linux-only-sms.png "imagen 7")
    /// caption
    **Imagen 6**. Captura de pantalla de terminal de linux con el menú backup de AndroidQF y la opción Only SMS seleccionada.
    ///

* Al seleccionar el tipo de respaldo, el teléfono solicitará utilizar una **contraseña temporal de cifrado** para cifrar el [respaldo generado a través de ADB](../../references/00-glossary.md#respaldo-generado-por-adb). En nuestro ejemplo utilizamos **la contraseña “sd”** de seguridad digital en español, tal y como se muestra en la imagen 7. 

    !!! warning "Alternativa"

        Esta contraseña permite cifrar la copia de seguridad que se genera al ejecutar androidqf. En caso de generar **contraseñas aleatorias**, asegúrate de utilizar un **gestor con adecuadas prácticas de respaldo**. De lo contrario, y sino representa un riesgo, establece una contraseá simple y equivalente para todas tus extracciones.
   
    ![Captura de pantalla de dispositivo móvil Android Samsung solicitando la contraseña temporal del backup sd](../04-como-extraer-mediante-androidqf/assets/07-captura-android-contraseña.png "imagen 7")
    /// caption
    **Imagen 7**. Captura de pantalla de dispositivo móvil Android Samsung solicitando la contraseña temporal del backup “sd”
    ///

* Selecciona: **“Copia de seguridad de mis datos”.**

    ![Captura de pantalla de dispositivo móvil Android Samsung con la opción “Copia de seguridad de mis datos” seleccionada](../04-como-extraer-mediante-androidqf/assets/08-captura-android-copia-seguridad.png "imagen 8")
    /// caption
    **Imagen 8**. Captura de pantalla de dispositivo móvil Android Samsung con la opción “Copia de seguridad de mis datos” seleccionada
    ///

    !!! failure "Mensajes de errores esperados"

        En algunas ocasiones, suelen aparecer errores sobre la búsqueda de las rutas donde se encuentran los paquetes, por lo que es común ver algunas de estas marcas de error, sin embargo, **estas marcas de error no afectan la extracción de datos forenses en el dispositivo.***

    ![Captura de pantalla de terminal de linux indicando la recolección de información de paquetes de aplicaciones por parte de AndroidQF.](../04-como-extraer-mediante-androidqf/assets/09-captura-linux-recoleccion.png "imagen 9")
    /// caption
    **Imagen 9**. Captura de pantalla de terminal de linux indicando la recolección de información de paquetes de aplicaciones por parte de AndroidQF.
    ///

* Cuando AndoridQF encuentra todos los paquetes instalados en el dispositivo preguntará qué **tipo de copias de las aplicaciones se desea descargar, para ello hay 3 opciones**:  

    * **All**: Descarga los [APK](../../references/00-glossary.md#apk) de todas las aplicaciones, incluidas las del sistema.  
    * **Only** **non-system** **packages**: Descarga solo los APK de aplicaciones instaladas por el usuario.  
    * **Do** **not** **download** **any**: Omite completamente la descarga de APKs del dispositivo.


    !!! warning "Alternativa"

        Aunque nuestra recomendación es seleccionar “Only non-system packages”, la selección depende de tu enfoque de análisis e investigación, por lo que en casos con sospechas de ataques sofisticados se puede utilizar la opción “All”.


    ![Captura de pantalla de terminal de linux con el menú copias de paquetes de aplicaciones de AndroidQF y la opción Only non-system packages seleccionada.](../04-como-extraer-mediante-androidqf/assets/10-captura-linux-copia-paquetes.png "imagen 10")
    /// caption
    **Imagen 10**. Captura de pantalla de terminal de linux con el menú copias de paquetes de aplicaciones de AndroidQF y la opción Only non-system packages seleccionada.
    ///

* Una vez seleccionada la opción de descargas de copias de paquetes, **AndroidQF preguntará acerca de eliminar los [APKs](../../references/00-glossary.md#apk)** firmados por desarrolladores o entidades confiables (como Google o el fabricante del dispositivo), esto con el fin de reducir el tamaño de la carpeta de extracción.

    * Responde **“Yes”** para que, al realizar la revisión de la información se pueda **enfocar el análisis en los paquetes que sean potencialmente sospechosos**, además de que ahorrará tiempo y espacio de almacenamiento.


    !!! warning "Alternativa"

        Aunque nuestra recomendación es seleccionar “Yes”, la selección depende de tu enfoque de análisis e investigación, por lo que en casos con sospechas de ataques sofisticados se puede utilizar la opción “No”.


    ![Captura de pantalla de terminal de linux con el menú de omisión de aplicaciones con certificado confiable de AndroidQF y la opción Yes seleccionada.](../04-como-extraer-mediante-androidqf/assets/11-captura-linux-omision-aplicaciones.png "imagen 11")
    /// caption
    **Imagen 11**. Captura de pantalla de terminal de linux con el menú de omisión de aplicaciones con certificado confiable de AndroidQF y la opción Yes seleccionada.
    ///

* **Espera** a que todos los módulos de AndroidQF se ejecuten de acuerdo a su programación.

    !!! info "Duración del proceso"
        **Esta etapa puede tomar varios minutos**, dependiendo del modelo del teléfono y la cantidad de datos almacenados. El progreso se muestra línea por línea en la terminal y no requiere intervención adicional, salvo al final, donde se debe presionar Enter para completar.

    ![Captura de pantalla de terminal de linux con el menú de omisión de aplicaciones con certificado confiable de AndroidQF y la opción Yes seleccionada.](../04-como-extraer-mediante-androidqf/assets/12-captura-pantalla-ejecucion-correcta.png "imagen 12")
    /// caption
    **Imagen 12**. Captura de pantalla de terminal de linux con información de ejecución correcta de la extracción forense con AndroidQF y solicitando presionar enter para terminar.
    ///


### :material-numeric-6-box: Verificar la extracción

Una vez finalizada la ejecución de AndroidQF, es importante **validar que la adquisición se completó correctamente**. Para ello, realiza los siguientes pasos:

* Abre el archivo command.log con un editor de texto y **busca las palabras warning o error**. Si aparece revisa si corresponden a fallos críticos o eventos no relevantes.


=== "Linux / MacOS"

    Puedes usar el comando siguiente dentro de la carpeta de la adquisición:

    ```
    grep -i "WARNING\|ERROR" command.log
    ```

    ![Captura de pantalla de terminal de linux con el comando grep para buscar errores en el archivo command.log generado por AndoridQF.](../04-como-extraer-mediante-androidqf/assets/13-captura-pantalla-terminal-linux-errores.png "imagen 12")
    /// caption
    **Imagen 13**. Captura de pantalla de terminal de linux con el comando grep para buscar errores en el archivo command.log generado por AndoridQF.
    ///
    

=== "Windows"

    Abre el archivo con “*Bloc de notas”*, selecciona la combinación de teclas **ctrl+b** y escribe ***WARNING*** o ***ERROR*****.**

    ![Captura de pantalla de terminal de linux con el comando grep para buscar errores en el archivo command.log generado por AndoridQF.](../04-como-extraer-mediante-androidqf/assets/14-captura-pantalla-windows-errores.png "imagen 14")
    /// caption
    **Imagen 14**. Captura de pantalla de Bloc de notas de Windows con la búsqueda de  errores en el archivo command.log generado por AndoridQF.
    ///

* Verifica la **existencia del archivo *acquisition.json*** y que su contenido se vea adecuado.

    ![Captura de pantalla de Sublime Text Con la salida del archivo acquisition.json generado por AndoridQF.](../04-como-extraer-mediante-androidqf/assets/15-captura-pantalla-acquisition.png "imagen 15")
    /// caption
    **Imagen 15**. Captura de pantalla de Sublime Text Con la salida del archivo acquisition.json generado por AndoridQF.
    ///

* Comprueba la creación de archivos y carpetas de salida. **Asegurate que se hayan generado los siguientes archivos y carpetas:**

    ```
    ├── apks/
    ├── logs/
    ├── tmp/
    ├── .json  
    ├── backup.ab  
    ├── bugreport.zip  
    ├── command.log  
    ├── dumpsys.txt  
    ├── env.txt  
    ├── files.json  
    ├── getprop.txt  
    ├── hashes.csv  
    ├── logcat.txt  
    ├── packages.json  
    ├── processes.txt  
    ├── root_binaries.json  
    ├── selinux.txt  
    ├── services.txt  
    ├── settings_global.txt  
    ├── settings_secure.txt  
    └── settings_system.txt  
    ```

    ![Captura de pantalla de la aplicación archivos en PopOS\! mostrando la carpeta de salida de archivos y directorios generados con la extracción forense con AndroidQF.](../04-como-extraer-mediante-androidqf/assets/16-captura-pantalla-archivos-salida.png "imagen 15")
    /// caption
    **Imagen 16**. Captura de pantalla de la aplicación archivos en PopOS\! mostrando la carpeta de salida de archivos y directorios generados con la extracción forense con AndroidQF.
    ///

## Conclusión

AndroidQF permite realizar adquirir y extraer evidencia forense de dispositivos Android. Es una **herramienta ampliamente utilizada por laboratorios de la sociedad civil**, debido a su practicidad, simplicidad y portabilidad. En esta guía detallamos el paso a paso a seguir para realizar extracciones utilizando Windows, MacOS o Linux. 

La extracción de potencial evidencia es una de las **[primeras etapas a seguir dentro de una investigación forense](../explainers/01-explainer-introduccion-forense-digital/01-explainer-introduccion-forense-digital.html#cuales-son-las-etapas-de-una-investigacion-forense)**, y es clave para poder iniciar un triaje. A partir de esta información extraída, se puede iniciar una etapa de análisis, ya sea de forma manual ([pudes consultar el diccionario de archivos aquí](../references/01-reference-diccionario-androidqf/01-reference-diccionario-androidqf.html)) o utilizando una herramienta como [MVT](https://docs.mvt.re/en/latest/). 

Si deseas contribuir con el desarrollo, la traducción o difusión de este recurso u otros recursos, **revisa nuestra [sección de comunidad](../comunidad/)** donde encontrarás más información al respecto.
