---

title: How-to - Triaje técnico de dispositivos Android utilizando MVT
summary: Comandos y pasos para realizar el triaje técnico de un dispositivo Android mediante MVT
keywords: triaje, android, mvt, androidqf, bugreport
lang: es
tags: [how-to, android, mvt]
last_updated: 2026-11-04
some_url:
created: 2026-11-04
comments: true
author:
    name: Daniel
    url: https://socialtic.org/quienes-somos/
    description: SocialTIC
translation-review-pending: true
auto-translate: false

---

# How-to: Triaje técnico de dispositivos Android utilizando MVT

Este documento forma **parte de un repositorio de documentación técnica** que tiene como objetivo establecer una base de conocimientos probados, flexibles y accesibles para **impulsar el análisis forense consentido en beneficio de la sociedad civil**. Para organizar los contenidos, se utiliza el [marco de referencia de documentación técnica Diataxis](../../references/00-glossary/index.md#diataxis). 

Este recurso pertenece a la categoría de [guías How-To](https://diataxis.fr/how-to-guides/). Su objetivo es guiarte a través de los comandos y pasos necesarios para realizar un triaje técnico de un dispositivo Android utilizando el [Mobile Verification Toolkit (MVT)](https://github.com/mvt-project/mvt). Se asume familiaridad con los [conceptos básicos de triaje](../../explainers/04-explainer-introduction-android-triage/index.md) de Android y la [herramienta MVT](../../explainers/05-explainer-mvt-android-triage/index.md). 

Si aún no has utilizado el MVT para realizar una evaluación técnica, te recomendamos que sigas primero el [Tutorial: Uso de MVT para el triaje técnico de dispositivos Android](../../tutorials/02-tutorial-mvt-android-triage/index.md), que incluye una guía paso a paso y un ejercicio práctico. 

Reconocemos los esfuerzos y el liderazgo del [Laboratorio de Seguridad de Amnistía Internacional](https://securitylab.amnesty.org/) en el desarrollo de la herramienta MVT, así como su papel en el fortalecimiento de la comunidad global de análisis forense digital consentido a través de su [Programa Digital Forensics Fellowship](https://securitylab.amnesty.org/digital-forensics-fellowship/). Este material pretende ser compatible y complementario a estas iniciativas tecnológicas y metodológicas.

Este material suma a otros recursos de este repositorio:

* [Guía explicativa: Introducción al triaje técnico de dispositivos Android](../../explainers/04-explainer-introduction-android-triage/index.md), que aborda los fundamentos conceptuales de la evaluación técnica de dispositivos Android (vectores de amenaza, tipos de artefactos, el papel de la entrevista inicial).
* [Guía explicativa: Exploración de la herramienta MVT para el triaje técnico de dispositivos Android](../../explainers/05-explainer-mvt-android-triage/index.md), que aborda los comandos, módulos y archivos de salida de MVT.
* How-to's de extracción, entre las que se incluyen [¿Cómo extraer un bugreport de un dispositivo Android?](../05-how-to-extract-bugreport/index.md) y [¿Cómo realizar una extracción con AndroidQF?](../04-how-to-extract-with-androidqf/index.md)
* Tutoriales y materiales de aprendizaje sobre [el uso de MVT el triaje técnico de dispositivos Android](../../tutorials/02-tutorial-mvt-android-triage/index.md) y [el uso de AndroidQF para la extracción de datos de dispositivos Android](../../tutorials/01-tutorial-learning-androidqf/index.md).
* Recursos de referencia que detallan los archivos de salida de MVT:
    * [Diccionario de archivos de salida de bugreport de MVT](../../references/02-reference-mvt-bugreport-dictionary/index.md)
    * [Diccionario de archivos de salida de MVT para AndroidQF](../../references/03-reference-mvt-androidqf-dictionary/index.md)

## Requisitos previos para realizar una evaluación técnica con MVT

Antes de seguir esta guía, asegúrate de que:

* **Dispones de acceso a Internet.** Esto es necesario para instalar y actualizar MVT, así como para descargar los últimos indicadores de compromiso (IOC).
* **Ya has realizado una entrevista de triaje** con la persona a la que estás acompañando y dispones de las fechas clave, los acontecimientos y el contexto necesarios para orientar tu análisis.
* **Ya has recopilado la información forense que necesitas analizar.** Esta guía no trata sobre la extracción. Si aún no lo has hecho, sigue las instrucciones de:
    * [¿Cómo extraer un bugreport de un dispositivo Android?](../05-how-to-extract-bugreport/index.md)
    * [¿Cómo realizar una extracción con AndroidQF?](../04-how-to-extract-with-androidqf/index.md)
* **Tienes una hipótesis inicial que quieres confirmar o descartar.** MVT no te indica si un dispositivo está comprometido. Puede ayudarte a detectar artefactos e indicadores conocidos para que los interpretes en el contexto del caso. Revisar sus resultados sin una hipótesis clara hace que sea muy difícil saber qué buscar.

## 1️⃣ Instalar o actualizar MVT

MVT se distribuye como un paquete de Python y lo mejor es instalarlo mediante [pipx](https://pipx.pypa.io/), que lo aísla de otros paquetes de Python del sistema.

=== "Linux"

    ```sh
    sudo apt install python3 python3-venv python3-pip sqlite3 libusb-1.0-0
    sudo apt install pipx
    pipx ensurepath
    git clone https://github.com/mvt-project/mvt
    cd mvt
    pipx install --force .
    ```

=== "macOS"

    ```sh
    brew install python3 pipx libusb sqlite3
    git clone https://github.com/mvt-project/mvt
    cd mvt
    pipx install --force .
    ```

!!! warning "Nota"

    Actualmente, MVT no cuenta con un proceso de instalación oficial para Windows. La herramienta se puede utilizar a través del Subsistema de Windows para Linux; sin embargo, no se garantiza su correcto funcionamiento.

**Si MVT ya está instalado, actualízalo antes de cada triaje** para asegurarte de que dispones de los módulos más recientes:

```sh
cd mvt
git pull
pipx uninstall mvt
pipx install --force .
```

Por último, **descarga los indicadores de compromiso más recientes**:

```sh
mvt-android download-iocs
```

## 2️⃣ Confirma qué información está disponible

El comando MVT que ejecutes dependerá de lo que hayas recopilado durante la extracción. Utiliza la tabla siguiente para decidir:

| Información disponible | Comando a utilizar | Qué te proporciona |
| :---- | :---- | :---- |
| Extracción completa de AndroidQF | `mvt-android check-androidqf` | Un análisis completo, que incluye el bugreport y, cuando estén disponibles, los registros de intrusión |
| Solo bugreport | `mvt-android check-bugreport` | Clasificación inicial utilizando únicamente el bugreport |
| Solo registros de intrusión | `mvt-android check-intrusion-logs` | Una revisión de los registros de protección avanzada |

Si dispones de una extracción completa de AndroidQF, utiliza `check-androidqf`, ya que esta opción cubre las otras dos, siempre y cuando los artefactos específicos estén presentes en la extracción. 

Puedes ver la lista de módulos disponibles para cada comando con:

```sh
mvt-android check-bugreport --list-modules
mvt-android check-intrusion-logs --list-modules
mvt-android check-androidqf --list-modules
```

## 3️⃣ Configurar la carpeta de salida

### Consideraciones sobre el manejo de datos

Aunque una extracción de bugreport o AndroidQF contiene relativamente poca información estrictamente privada (por ejemplo, no hay fotos ni archivos personales), debe manejarse con cuidado:

* **Respeta el consentimiento informado** otorgado por la persona a la que estás acompañando.
* Sigue cualquier **acuerdo de protección de datos** establecido para el caso.
* **Evita** sincronizar o subir cualquier dato de este tipo a **servicios en la nube no cifrados**.

En la [sección correspondiente de la guía explicativa sobre la clasificación con MVT](../../explainers/05-explainer-mvt-android-triage/index.md#recomendaciones-para-el-manejo-de-la-informacion-sensible) se enumeran recomendaciones adicionales. 

Si aún no cuentas con el consentimiento informado de la persona que acompañas, consulta [¿Cómo obtener y documentar el consentimiento informado?](../01-how-to-obtain-informed-consent/index.md)

### Crear la carpeta de trabajo

Crea una carpeta para **almacenar una copia de la extracción recopilada** y asígnale un nombre siguiendo una convención coherente. Ten en cuenta que esta convención debe definirla cada organización, en función del contexto y las necesidades específicas, incluyendo aspectos relacionados con la confidencialidad y el anonimato de la persona que solicita el análisis.

A modo de ejemplo, sugerimos utilizar la fecha combinada con un alias del caso o un hash:

```sh
mkdir "$(date +"%Y-%m-%d")"-android-<alias-del-caso-o-hash>-out-androidqf
mkdir "$(date +"%Y-%m-%d")"-android-<alias-del-caso-o-hash>-out-bugreport
mkdir "$(date +"%Y-%m-%d")"-android-<alias-del-caso-o-hash>-out-intrusion-logs

```

Copia la extracción recopilada (bugreport, carpeta AndroidQF o registros de intrusión) en esta carpeta antes de continuar. Te recomendamos que configures una estructura de directorios de trabajo que incluya una carpeta para la extracción (que no debe modificarse nunca), una copia de la extracción para realizar el análisis, una carpeta para los resultados (siguiendo la convención de nomenclatura descrita anteriormente) y un documento para las notas. Por ejemplo:

```
analysis/
└── AAAA-MM-DD-sistema-operativo-<alias-del-caso-o-hash>/
    ├── extraction-custody/ # Datos sin procesar, no deben modificarse
    ├── extraction-working/ # Copia de los datos sin procesar, utilizada para el análisis
    ├── AAAA-MM-DD-out-<androidqf/bugreport/intrusion-logs>/ # para almacenar los resultados de MVT
    └── notes.md # Notas y registros del análisis
```

### Eliminación y conservación de resultados

* Elimina los resultados generados por MVT una vez concluido el análisis, siguiendo el acuerdo de conservación de datos del caso. Si tienes consentimiento para retener la información, almacénala siguiendo buenas prácticas para la protección de información. 
* No guardes copias en lugares donde no debería estar, como por ejemplo carpetas de descarga, o copias temporales. 

## 4️⃣ Ejecutar MVT

Abre un terminal en tu carpeta de trabajo y ejecuta el comando que se ajuste a lo que tengas disponible (véase el paso 2). MVT creará la carpeta de salida (`-o`) con varios archivos y subcarpetas, tal y como se describe en el paso 5.

**Extracción de AndroidQF:**

```sh
mvt-android check-androidqf /ruta/a/la/extraccion/aqf -o "$(date +"%Y-%m-%d")"-out-androidqf
```

**bugreport:**

```sh
mvt-android check-bugreport /ruta/al/informe-de-errores -o "$(date +"%Y-%m-%d")"-out-bugreport
```

**Registros de intrusión:**

```sh
mvt-android check-intrusion-logs /ruta/a/registros/de/intrusión -o "$(date +"%Y-%m-%d")"-out-intrusion-logs
```

### Errores comunes

* **Se solicita una contraseña de copia de seguridad:** si la extracción incluye un archivo `backup.ab` cifrado, MVT solicitará su contraseña antes de continuar.
* **`ModuleNotFoundError` o errores de dependencias que faltan:** reinstala MVT siguiendo el paso 1, asegurándote de que las dependencias del sistema (`sqlite3`, `libusb-1.0-0`) estén instaladas.
* **Comando no encontrado:** confirma que se ha ejecutado `pipx ensurepath` y que has abierto una nueva sesión de terminal después de ejecutarlo.
* **No se han generado archivos `_detected`:** esto no significa necesariamente que la ejecución haya fallado. Simplemente puede significar que nada coincidió con un indicador conocido o una heurística. Continúa con el paso 5.

## 5️⃣ Analiza los resultados

Antes de revisar cualquier resultado, **ten en cuenta y anota por escrito las fechas clave y la información de la entrevista de triaje**, junto con la hipótesis que intentas confirmar o descartar.

* **`command.log`:** la misma salida que MVT muestra en pantalla mientras se ejecuta, guardada en un archivo. Mezcla información del proceso (INFO, DEBUG) con alertas de diferentes niveles de gravedad (LOW, MEDIUM, HIGH, CRITICAL), en orden cronológico. Suele ser el mejor punto de partida. Consulta los [diccionarios de referencia](../../references/index.md) para obtener más detalles sobre su estructura.
* **`alerts.json`:** un único archivo que recopila todas las alertas generadas durante la ejecución, sin las líneas informativas que aparecen en `command.log`. Resulta útil para obtener una visión general rápida de todo lo que MVT ha identificado como sospechoso antes de revisar módulo por módulo.
    * **Alertas críticas:** advertencias relacionadas con una coincidencia con un IOC, es decir, una coincidencia con un indicador STIX2 conocido previamente.
    * **Alertas de nivel bajo, medio y alto:** relacionadas con coincidencias con TTP (tácticas, técnicas y procedimientos), lo que significa que se trata de coincidencias basadas en heurística y en el comportamiento de los dispositivos que no están relacionadas con un IOC conocido.
* **Archivos con el sufijo `_detected`:** se generan por módulo cada vez que MVT encuentra una coincidencia con un indicador de compromiso conocido o una heurística sospechosa. Cada archivo contiene el indicador con el que ha coincidido, el artefacto relacionado y la marca de tiempo correspondiente.
    * **Cuando encuentres una coincidencia:** toma nota del nombre del módulo y de la marca de tiempo, y compáralos con la cronología de la entrevista de triaje, si procede.
    * **Importante:** la ausencia de un archivo `_detected` no confirma que el dispositivo esté limpio, y la presencia de uno no confirma la existencia de actividad maliciosa. Ambos casos requieren una investigación más exhaustiva y una revisión manual.
* **`timeline.csv`:** todos los eventos extraídos por MVT, organizados cronológicamente. Resulta especialmente útil una vez que se dispone de un intervalo de tiempo específico para investigar a partir de la entrevista, ya que permite filtrar la actividad en torno a él.
* **`alerts_timeline.csv`:** contiene una cronología de todas las alertas generadas durante la ejecución de MVT, incluida información específica sobre el módulo que generó la alerta.

Para obtener una descripción completa del contenido de cada archivo y campo, consulta el [diccionario de archivos de salida de bugreport de MVT](../../references/02-reference-mvt-bugreport-dictionary/index.md) y el [diccionario de archivos de salida de MVT para AndroidQF](../../references/03-reference-mvt-androidqf-dictionary/index.md).

## 6️⃣ Realizar búsquedas específicas

Una vez que hayas realizado una primera revisión de la salida, utiliza herramientas estándar de línea de comandos para profundizar en archivos específicos sin tener que abrirlos manualmente. Por ejemplo: 

* **`grep`:** busca coincidencias de texto en los archivos. Ejemplos:

```sh
grep -l "<nombre_del_paquete>" *_detected.json
```

```sh
grep -E "LOW|MEDIUM|HIGH|CRITICAL" command.log
```

* **`find`:** localiza archivos dentro de la carpeta de resultados.

```sh
find . -name "*_detected*"
```

* **`cat`:** muestra el contenido completo de un archivo en la terminal, útil para archivos más pequeños.

```sh
cat packages.json
```

* **`jq`:** filtra y consulta la salida JSON, el formato en el que se almacenan la mayoría de los resultados de MVT.

```sh
jq '.[] | {level, module, message}' alerts.json
```

## 7️⃣ Documentar los hallazgos y los siguientes pasos

* **Documenta cada hallazgo**, incluyendo el nombre del paquete, el tipo de artefacto, la marca de tiempo y el indicador o TTP coincidente que lo ha señalado.
* **Considera una revisión independiente** de cualquier cosa que necesites confirmar o investigar más a fondo. La perspectiva de un(e) segundo analista resulta especialmente valiosa cuando un hallazgo no está claro.
* **Identifica caminos de investigación adicionales**, como el análisis estático o dinámico de un APK sospechoso, o una revisión de la cuenta de Google asociada a través de Google Takeout.

## Conclusión

En este recurso hemos proporcionado **pasos concretas sobre cómo utilizar MVT para el triaje técnico de un dispositivo Android**. Es importante destacar que este proceso no debe basarse únicamente en la herramienta, sino que debe partir de una buena entrevista inicial que ponga de manifiesto aspectos concretos que investigar y que pueda ayudar a identificar hipótesis.

También hay que tener en cuenta que la herramienta ayudará a analizar la información y señalará áreas específicas que investigar, pero **no sustituirá la interpretación de una persona analista.** Además, considera este proceso de triaje como un esfuerzo inicial para encontrar pruebas de una posible actividad maliciosa, no necesariamente como un resultado concluyente. En función de los hallazgos iniciales de este proceso de triaje, es posible que desees realizar un análisis manual más detallado, que podría incluir una aplicación sospechosa.

Por último, ten en cuenta la importancia del consentimiento informado y del tratamiento adecuado de la información forense, para evitar la exposición a [amenazas y riesgos conocidos](../../explainers/02-explainer-risks-threats/index.md).


## Comentarios

¿Tienes **comentarios o sugerencias** sobre este recurso? Puedes utilizar la **función de comentarios que se muestra a continuación** para compartir tus ideas u opiniones con nosotros. Asegúrate de seguir nuestro [código de conducta](../../community/code-of-conduct/index.md). La función de comentarios enlaza directamente con las [sección _Discusiones_ en GitHub](https://github.com/Socialtic/forensics/discussions), donde también puedes **participar directamente en los debates**, si lo prefieres.
