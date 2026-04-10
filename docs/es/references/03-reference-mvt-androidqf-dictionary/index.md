---
title: Diccionario de archivos generados por mvt-androidqf
summary: Diccionario de archivos generados por mvt-androidqf
keywords: android, reference, bugreport
lang: es
tags: [explainer, intro]
last_updated: 2025-11-20
some_url:
created: 2025-11-20
comments: true
name: jose
auto-translate: true

---

# Diccionario de archivos generados por la herramienta MVT-androidqf

El presente documento contiene información sobre los archivos generados por la MVT a través del componente [mvt-check-androidqf.](https://github.com/mvt-project/mvt/tree/main/src/mvt/android/modules/androidqf) El objetivo de este diccionario, es que la persona analista tenga la facilidad de buscar información específica y conocer el formato en que la información del análisis forense es presentada.

Este recurso forma **parte de un repositorio de documentación técnica** que tiene como objetivo establecer una base de conocimientos probados, flexibles y accesibles para **impulsar el análisis forense consentido en beneficio de la sociedad civil**. Para organizar los contenidos, se utiliza el [marco de referencia de documentación técnica Diataxis](https://diataxis.fr/).

Este recurso en particular se enmarca dentro de la categoría de [referencias](https://diataxis.fr/reference), y contiene información sobre el análisis de la salida de adquisición generados por dispositivos Android mediante el comando ***mvt-android check-andoridqf***  durante el uso de la herramienta MVT (*Mobile Verification Toolkit)*, desarrollada y mantenida por el [Laboratorio de Seguridad de Amnistía Internacional](https://securitylab.amnesty.org/es/) y perteneciente al [MVT Project](https://github.com/mvt-project/). Esto con el objetivo de que una persona analista **conozca los archivos generados, cómo utilizarlos, donde buscar información específica y en qué formato la encontrará.**

MVT hace referencia a *Mobile Verification Toolkit*. Esta es una herramienta desarrollada, lanzada y mantenida por el [Laboratorio de Seguridad de Amnistía Internacional](https://securitylab.amnesty.org/es/) perteneciente al [MVT Project](https://github.com/mvt-project/).  La intención de esta herramienta es en esencia, facilitar el análisis forense consensuado de dispositivos Android e iOS con el propósito de identificar rastros de compromiso. 

Este recurso se actualizó por última vez el 18 de noviembre de 2025 y para la recopilación de la información se tomó como base el [*commit 339a1d0712c4cc051e880b8a777d2b8b6295e57b*](https://github.com/mvt-project/mvt/commit/339a1d0712c4cc051e880b8a777d2b8b6295e57b). 

La información generada por *mvt-androidqf* se puede agrupar en 5 categorías principales:

* Detalles de la adquisición  
* Configuración del dispositivo  
* Información sobre registros y eventos del sistema  
* Procesos y aplicaciones  
* Archivos respaldados

A su vez cada una de las categorías contiene archivos específicos generados por la herramienta, los cuales se enlistan en el **siguiente índice de contenidos**:

- [Detalles de la adquisición](#detalles-de-la-adquisición)
    - [info.json](#info.json)
    - [command.log](#command.log)
    - [timeline.csv](#timeline.csv)
- [Configuración del dispositivo](#configuración-del-dispositivo)
    - [aqf_getprop.json](#aqf_getprop.json)
    - [aqf_settings.json](#aqf_settings.json)
    - [mounts.json](#mounts.json)
- [Procesos y aplicaciones](#procesos-y-aplicaciones)
    - [aqf_packages.json](#aqf_packages.json)
    - [root_binaries.py](#root_binaries.py)
- [Archivos respaldados](#archivos-respaldados)
    - [aqf_files.json](#aqf_files.json)

Durante la ejecución del comando ***mvt-android check-andoridqf**,* MVT también ejecuta módulos que corresponden a  ***mvt-android check-bugreport*** y ***mvt-android check-backup,*** esto siempre y cuando exista un archivo bugreport.zip y un archivo backup.ab dentro de la carpeta de entrada de una extracción con androidqf.

En el material de referencia complementario [sobre archivos generados por la herramienta mvt al analizar un bugreport](../02-reference-mvt-bugreport-dictionary/index.md) se describe la salida del comando check-bugreport y los archivos resultantes. A continuación se muestra el **las referencias específicas a los módulos ejecutados por el comando check-androidqf para analizar el bugreport:**

- [Configuración del dispositivo](../02-reference-mvt-bugreport-dictionary/index.md#configuración-del-dispositivo-configuración-del-dispositivo)
    - [dumpsys_get_prop.json](../02-reference-mvt-bugreport-dictionary/index.md#getprop.json)
- [Información sobre registros y eventos del sistema](../02-reference-mvt-bugreport-dictionary/index.md#informacion-sobre-registros-y-eventos-del-sistema)
    - [dumpsys_adb_state.json](../02-reference-mvt-bugreport-dictionary/index.md#dumpsys_adb_state.json)
    - [bugreport_timestamps.json](../02-reference-mvt-bugreport-dictionary/index.md#bugreport_timestamps.json)
    - [dbinfo.json](../02-reference-mvt-bugreport-dictionary/index.md#dbinfo.json)
    - [dumpsys_receivers.json](../02-reference-mvt-bugreport-dictionary/index.md#receivers.json)
- [Procesos y aplicaciones](../02-reference-mvt-bugreport-dictionary/index.md#procesos-y-aplicaciones)
    - [dumpsys_packages.json](../02-reference-mvt-bugreport-dictionary/index.md#packages.json)
    - [dumpsys_activities.json](../02-reference-mvt-bugreport-dictionary/index.md#activities.json)
    - [dumpsys_appops.json](../02-reference-mvt-bugreport-dictionary/index.md#appops.json)
    - [dumpsys_accessibility.json](../02-reference-mvt-bugreport-dictionary/index.md#accesibility.json)
    - [tombstones.json](../02-reference-mvt-bugreport-dictionary/index.md#tombstones.json)
    - [dumpsys_battery_daily.json](../02-reference-mvt-bugreport-dictionary/index.md#battery_daily.json)
    - [dumpsys_battery_history.json](../02-reference-mvt-bugreport-dictionary/index.md#battery_history.json)
    - [dumpsys_platform_compact.json](../02-reference-mvt-bugreport-dictionary/index.md#platform_compact.json)


Asi mismo , también listamos los módulos ejecutado por ***check-backup***, los cuáles se detallan al final de este recurso.  

- [Información sobre registros y eventos del sistema](#información-sobre-registros-y-eventos-del-sistema)  
- [sms.json](#sms.json)

## Detalles de la adquisición {#detalles-de-la-adquisición}

### info.json {#info.json}

**Información contenida**

Este archivo se encuentra en formato *json* y contiene información relacionada con el análisis realizado a una extracción completada mediante AndroidQF. Contiene la siguiente información:

* Ruta del archivo analizado.  
* Versión utilizada de MVT.  
* Fecha del análisis.  
* Lista de archivos de indicadores de compromiso.  
* Hash de la carpeta de salida analizada (SHA-256).

**¿Por qué es importante?**

Este archivo nos permite **validar el análisis que se ha realizado**, documentando que se tiene un registro del proceso de adquisición y los indicadores que se consideraron para hacer la comparación.

Esta información permite establecer una referencia del archivo analizado y la herramientas de indicadores utilizados utilizados en el análisis , esto facilita el [proceso de custodia de la extracción forense](https://forensics.socialtic.org/explainers/01-explainer-introduccion-forense-digital/01-explainer-introduccion-forense-digital.html#cadena-de-custodia). 

**Estructura del archivo:**

```
{
	"target_path": "/ruta/del/archivo/acquision-with-androidqf",
	"mvt_version": "2.6.1",
	"date": "YYYY-MM-DD hh:mm:ss",
	"ioc_files": [
    	"/ruta/a/indicadores/pegasus.stix2",
    	"/ruta/a/indicadores/predator.stix2",
    	"/ruta/a/indicadores/rcs_lab.stix2",
    	"... más indicadores utilizados ..."
	],
	"hashes": [
    	{
        	"file_path": "/ruta/del/archivo/acquision-with-androidqf",
        	"sha256": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    	}
	]
}
```

### command.log {#command.log}

**Información contenida**

Este archivo se encuentra en texto plano con una extensión *.log* y contiene los registros detallados de la ejecución del comando *mvt-android check-androidqf*.

Su contenido enlista el análisis realizado sobre una carpeta de salida de una extracción de información forense realizada con AndroidQF, incluyendo la detección de indicadores de compromiso para identificar alertas de seguridad relacionadas con malware.

Los registros del archivo se presentan de manera estructurada con:

* Marcas de tiempo  
* Nombres del módulo en ejecución  
* Tipo de mensaje (*INFO*, *DEBUG*, WARNING, *ERROR*)  
* Acción correspondiente del módulo (parseo del archivo, carga de IoCs, comparación, y resultado de la comparación).

Los tipos de mensaje corresponden de la siguiente manera:

* *INFO*. Mensajes mostrados también en pantalla durante la ejecución.  
* *DEBUG*. Información no mostrada en pantalla pero asociada a una acción realizada durante el análisis por ejemplo la carga de un IoC o la revisión de un hash.  
* *WARNING.* Corresponde a alertas de actividad o información sospechosa que un analista debe verificar.  
* *ERROR.* Mensajes de error en alguna acción realizada durante el análisis, por ejemplo al cargar un archivo corrompido o un problema con la ejecución del código correspondiente.

**¿Por qué es importante?**

Permite generar un registro de las acciones realizadas durante el análisis. A través de este registro es posible verificar lo siguiente:

* Que el análisis se realizó de manera correcta  
* Si hubo coincidencias con IoCs  
* Si se identificó información o actividad sospechosa.

**Estructura del archivo:**

Este archivo sigue un formato línea por línea con la siguiente estructura.

```
[TIMESTAMP] - [MÓDULO] - [NIVEL DE LOG] - [MENSAJE]  
...
2025-01-17 17:06:14,035 - mvt.android.cmd_check_androidqf - INFO - Parsing STIX2 indicators file at path /home/user/.local/share/mvt/indicators/raw.githubusercontent.com_AmnestyTech_investigations_master_2021-07-18_nso_pegasus.stix2  
2025-01-17 17:06:14,098 - mvt.android.cmd_check_androidqf - DEBUG - Extracted 1549 indicators for collection with name "Pegasus"  
2025-01-17 17:06:14,812 - mvt.android.cmd_check_androidqf - DEBUG - Extracted 245 indicators for collection with name "mSpy"  
```

**Aprende más**

* [Introduction to STIX](https://oasis-open.github.io/cti-documentation/stix/intro.html)

### timeline.csv {#timeline.csv}

**Información contenida**  
Este archivo se encuentra en formato *csv* y almacena una línea de tiempo de la actividad del dispositivo. Esta actividad se obtiene de la ejecución de los módulos de análisis de MVT y se ordena por tiempo.

Cada línea del *csv* corresponde a:

* Marca de tiempo (Device Local Timestamp).  
* Módulo ejecutado (Plugin).  
* Actividad identificada en el dispositivo (Event)  
* Descripción de la actividad identificada en el dispositivo (Description).

**¿Por qué es importante?**

Este archivo permite dar seguimiento a la actividad interna del dispositivo, pudiendo generar una idea amplia de cómo se comportó el dispositivo e identificar eventos relevantes. 

**Estructura del archivo**

Este archivo sigue un formato línea por línea con la siguiente estructura.

```
"UTC Timestamp","Plugin","Event","Description"
"2025-01-01 00:00:00","Packages","package_first_install","com.example.app (system: False, third party: True)"
"2025-01-01 00:00:00","Packages","package_last_update","com.system.module (system: True, third party: False)"
"2025-01-01 00:00:00","Packages","package_install","com.example.newapp (system: False, third party: True)"
```

## Configuración del dispositivo {#configuración-del-dispositivo}

### aqf\_getprop.json {#aqf_getprop.json}

La información de este archivo es generada mediante el módulo [aqf\_getprop](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/androidqf/aqf_getprop.py) y el artefacto [getprop](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/artifacts/getprop.py).

**Información contenida**

Este archivo se encuentra en formato *json* y contiene una lista de las propiedades del dispositivo que son extraídas del archivo *getprop.tx*t generado durante una extracción con AndoridQF.

Estas propiedades del sistema son pares clave-valor de cadenas que se almacenan en el diccionario global [*build.prop*](https://xdaforums.com/t/guide-build-prop-wiki.2056266/) o en archivos de descripción *.sysprop*, y proporcionan una forma conveniente de compartir configuraciones dentro del sistema. 

La información se puede encontrar utilizando el siguiente formato:

```
[{prefix}.]{group}[.{subgroup}]*.{name}[.{type}]
```

Algunas propiedades aparecen con el prefijo *ro*, lo que indica que son propiedades de solo lectura, o que fueron asignadas luego del reinicio del dispositivo. Las propiedades con el prefijo *persist* se refieren a configuraciones resistentes al reinicio. Algunas propiedades no tendrán prefijo, por lo que inician directamente con el grupo al que pertenecen. 

Los grupos más comunes son:

* *bluetooth*, relacionado con Bluetooth  
* *boot*, sysprops de cmdline del kernel  
* *build*, sysprops que identifican una compilación  
* *telephony*, relacionado con la telefonía  
* *audio*, relacionado con el audio  
* *graphics*, relacionado con los gráficos  
* *vold*, relacionado con vold que gestiona el montaje de volúmenes físicos de almacenamiento externo

Para mayor detalle se puede revisar la [lista de propiedades ya definidas en el código fuente de Android](https://android.googlesource.com/platform/system/sepolicy/+/refs/heads/main/private/property_contexts).

**¿Por qué es importante?**

Las propiedades brindan información importante sobre el hardware y el software del dispositivo, las cuales pueden ser alteradas por software malicioso para ocultar su presencia o para modificar el comportamiento del dispositivo de forma inadvertida.

**Estructura del archivo:**

```
[
	{
    	"name": "aaudio.hw_burst_min_usec",
    	"value": "2000"
	},
	{
    	"name": "bluetooth.device.class_of_device",
    	"value": "90,2,12"
	},
	{
    	"name": "apex.all.ready",
    	"value": "true"
	}
]
```

### aqf_settings.json {#aqf_settings.json}

La información de este archivo se genera mediante el módulo [aqf\_settings](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/androidqf/aqf_settings.py) y el artefacto [settings](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/artifacts/settings.py).

**Información contenida**

Este archivo se encuentra en formato *json* y contiene información sobre el estado de configuraciones del dispositivo en los *namespaces* *system* (UI y comportamiento general como brillo, tono, rotación, etc.), *secure* (ajustes sensibles que requieren permisos elevados como la verificación de aplicaciones, ajustes de accesibilidad o estado ADB) y *global* (parámetros compartidos entre usuarios como redes, ubicación, roaming, volúmenes globales, etc). 

La información es presentada en 3 bloques, primero aparecen las Settings system, posteriormente Settings secure y finalmente Settings global. Cada configuración es presentada como un par clave valor en la estructura:

```json
[{setting}:{level}]
```

Los valores que tienen cada configuración tiene diferentes significados dependiendo de esta configuración, pero por lo general se trata de lo siguiente:

* **0** suele significar deshabilitado o apagado.  
* **1** suele significar habilitado o encendido.  
* **Números más grandes** pueden ser niveles como el brillo de pantalla por ejemplo.  
* Algunos valores son **paths** o rutas de sistema que apuntan a recursos.

Esta información es extraída directamente de los archivos settings\_global.txt, settings\_secure.txt y settings\_system.txt generados durante una extracción con AndoridQF.

**¿Por qué es importante?**

Permite identificar configuraciones anómalas que podrían comprometer la seguridad, privacidad  o funcionalidad del dispositivo. Configuraciones predeterminadas inusuales pueden señalar intentos de modificar el comportamiento del sistema, intencionados o accidentales.

**Estructura del archivo:**

```
{
	"system": {
    	"SEM_VIBRATION_FORCE_TOUCH_INTENSITY": "4",
    	"SEM_VIBRATION_NOTIFICATION_INTENSITY": "5",
    	"SMLDM_BEARER": "0",
    	"SOFTWARE_UPDATE_LAST_CHECKED_DATE": "1736527562578",
    	"SOFTWARE_UPDATE_WIFI_ONLY2": "1",
    	"SOUNDALIVE_AUDIO_PATH": "0",
    	"TIME_DIFFERENCE": "445",
    	"VIB_FEEDBACK_MAGNITUDE": "2",
    	"VIB_RECVCALL_MAGNITUDE": "5",
    	"acc_last_status_logging": "1736780772300",
	},
	"secure": {
    	"accessibility_allow_diagonal_scrolling": "1",
    	"accessibility_button_mode": "1",
    	"accessibility_button_target_component":     	"accessibility_change_magnification_size": "3",
    	"accessibility_display_magnification_enabled": "0",
    	"accessibility_display_magnification_scale": "2.0",
    	"accessibility_enabled": "0",
    	"accessibility_magnification_activated": "0",
    	"accessibility_magnification_capability": "3",
    	"accessibility_magnification_mode": "2",
    	"accessibility_shortcut_dialog_shown": "1",
    	"accessibility_shortcut_target_service": 
	},
	"global": {
    	"Contacts_move_simcontacts_not_now": "0",
    	"Phenotype_boot_count": "131",
    	"Phenotype_flags":     	"_boot_Phenotype_flags": "",
    	"activity_starts_logging_enabled": "1",
    	"adb_allowed_connection_time": "604800000",
    	"adb_enabled": "1",
    	"adb_wifi_enabled": "0",
    	"add_users_when_locked": "0",
    	"airplane_mode_on": "0",
    	"airplane_mode_radios": "cell,bluetooth,uwb,wifi,wimax",
    	"airplane_mode_toggleable_radios": "bluetooth,wifi",
   	}
}
```

**Aprende más**

* [Lista completa de preferencias del sistema \- Settings System](https://developer.android.com/reference/android/provider/Settings.System?hl=es-419)  
* [Lista completa de preferencias del sistema \- Settings Secure](https://developer.android.com/reference/android/provider/Settings.Secure?hl=es-419)  
* [Lista completa de preferencias del sistema \- Settings Global](https://developer.android.com/reference/android/provider/Settings.Global?hl=es-419)

### mounts.json {#mounts.json}

La información de este archivo se genera mediante el módulo [mounts](https://github.com/mvt-project/androidqf/blob/main/modules/mounts.go) y el artefacto [mounts](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/artifacts/mounts.py) 

**Información contenida**

Este archivo se encuentra en formato *json* y contiene información sobre las particiones y directorios de sistemas de archivos montados en un dispositivo en el espacio de usuario *y* en el kernel de linux de Android extraídas del archivo *mounts.json* generado durante una extracción con AndoridQF.

El módulo se encarga de identificar configuraciones sospechosas en puntos de montaje /system, /vendor, /product y /system\_ext como modo de acceso de lectura y escritura, marcas de tiempo noatime o nodiratime, posteriormente se encarga de formatear cada punto de montaje de la siguiente manera:

* **device**: Partición o volumen montado, en android las más comunes son:
    * Particiones de almacenamiento físico
        * /dev/block/sdX: Dispositivo de almacenamiento físico ([eMMC/UFS](https://new.c.mi.com/es/post/11738)) expuesto como sd por el kernel.
        * /dev/block/mmcblk: Dispositivo de almacenamiento eMMC presentado como mmcblk.
        * /dev/block/dm-X: Dispositivo manejado por device-mapper (cifrado, verity o particiones lógicas).
        * /dev/block/by-name/: Enlaces simbólicos que apuntan a las particiones reales por su nombre e.j. system, vendor, userdata.
    * Volumen virtual del kernel en RAM
        * proc: Interfaz virtual para obtener información del kernel y procesos.
        * sysfs: Expone información de dispositivos, drivers y parámetros del kernel.
        * selinuxfs: Muestra políticas, estados y etiquetas de SELinux.
        * tracefs: Sistema virtual para herramientas de trazado y debugging del kernel.
        * pstore: Almacena registros persistentes de fallos del kernel.
        * bpf: Expone interfaces para programas [eBPF](https://source.android.com/docs/core/architecture/kernel/bpf) cargados en el kernel.
    * Espacio de usuario
        * /dev/fuse: Interfaz [FUSE](https://source.android.com/docs/core/storage/fuse-passthrough) usada por Android para montar almacenamiento emulado p.j /storage/emulated.
    * Interfaces internas de control de kernel
        * none: Identificador que indica que el montaje no proviene de un dispositivo real.
        * binder: [Sistema de IPC](https://source.android.com/docs/core/architecture/ipc/binder-overview) interno de Android para comunicación entre procesos.
    * Archivos APEX montados como loopback
        * /dev/block/loopX: Dispositivos de bucle usados para montar paquetes APEX como si fueran particiones reales.

* **mount point**: Ruta de la carpeta raíz del almacenamiento donde se accede a la información, en android suelen ser los siguientes:
    * /system: Contiene el sistema operativo principal.
    * /vendor: Incluye componentes y drivers proporcionados por el fabricante del hardware como HALs, firmware y binarios específicos del proveedor.
    * /product: Almacena personalizaciones del fabricante sobre las funciones del sistema y aplicaciones específicas del dispositivo.
    * /data: Área de datos del usuario y almacenamiento de apps.
    * /cache: Espacio temporal usado para archivos de actualización y datos transitorios del sistema.
    * /metadata: Contiene información crítica necesaria para [AVB](https://source.android.com/docs/security/features/verifiedboot/avb), cifrado y validaciones del sistema.
    * /mnt/media_rw/: Punto de montaje para almacenamiento removible o adoptado e.j. SD card.
    * /storage/emulated: Vista emulada de almacenamiento interno del usuario.
    * /proc: Sistema virtual que expone información del kernel y procesos (no es almacenamiento real).
    * /sys: Sistema virtual que expone información sobre dispositivos y controladores del kernel.
    * /mnt/user/0/emulated: Vista específica del almacenamiento emulado para el usuario 0.

* **filesystem_type**: Tipo de sistema de archivos, en android son los siguientes:
    * ext4: Sistema de archivos de Linux usado en particiones internas.
    * f2fs: Sistema de archivos optimizado para almacenamiento flash.
    * erofs: Sistema de archivos de solo lectura optimizado.
    * vfat: Sistema de archivos FAT32 usado para tarjetas SD y almacenamiento externo.
    * sdfat: Implementación extendida de FAT/exFAT.
    * tmpfs: Sistema de archivos temporal en RAM usado para directorios volátiles e.j. /dev, /run, /apex.
    * proc: Sistema de archivos virtual que expone información del kernel y procesos.
    * sysfs: Sistema virtual que muestra información de hardware, drivers y controladores del kernel.
    * selinuxfs: Sistema virtual que expone parámetros y estado de SELinux en el dispositivo.
    * functionfs: Sistema usado para interfaces [USB gadget](https://source.android.com/docs/core/permissions/usb-hal) cuando Android actúa como dispositivo USB.
    * incremental-fs: Sistema diseñado para instalar o ejecutar apps “bajo demanda” mientras aún están descargándose.
    * binder: Sistema de comunicación interna IPC de Android.
    * cgroup: Sistema virtual basado en control groups para gestionar recursos por procesos e.j. CPU, memoria.
    * fuse: Sistema de archivos en espacio de usuario utilizado para almacenamiento emulado.

* **mount_options**
    * modos de acceso
        * ro: read only
        * rw: read and write
    * etiquetas de seguridad
        * seclabel: Habilita y aplica etiquetas SELinux al sistema de archivos.
        * nodev: Evita que se usen archivos de dispositivo en esa partición.
        * nosuid: Bloquea binarios con [set-UID/set-GID](https://www.cbtnuggets.com/blog/technology/system-admin/linux-file-permissions-understanding-setuid-setgid-and-the-sticky-bit) para evitar escalación.
        * noexec: Impide ejecutar archivos desde esa partición.
        * hidepid=invisible: Oculta procesos de otros usuarios en * /proc *.
        * user_xattr: Permite atributos extendidos definidos por el usuario.
        * acl: Permite listas de control de acceso más detalladas que *rwx*.
        * inlinecrypt: Usa cifrado en línea soportado por hardware/FS (Android).
        * usrquota: Habilita cuotas por usuario.
        * grpquota: Habilita cuotas por grupo.
    * marcas de tiempo
        * lazytime: Aplaza la escritura de timestamps al almacenamiento para mejorar el rendimiento.
        * relatime: Actualiza tiempos de acceso solo si es necesario.
        * noatime: Desactiva la actualización del tiempo de acceso.
    * usuarios o grupos relacionados
        * uid=0: Propietario del montaje (root).
        * gid=1000: Grupo base de Android (system o media_rw).
        * user_id=0: Usuario principal del sistema Android.
        * group_id=0: Grupo primario del usuario root.

* **is_system_partition**: Valor booleano que indica si la partición es /system o /sys.
* **is_read_write**: Valor booleano que indica si la partición tiene acceso de lectura y escritura.


**¿Por qué es importante?**

Los puntos de montaje permiten identificar las **áreas de almacenamiento montadas en el dispositivo**, su origen y cómo están configuradas. Con esta información se pueden conocer los permisos con los que fueron montadas las particiones, los usuarios asociados y en algunos casos las etiquetas de seguridad SELinux aplicadas. Esto resulta útil para la **identificación de montajes que pueden ser sospechosos** de actividades maliciosas en el dispositivo, por ejemplo, una partición del sistema como /system, /vendor, /product particiones cuyo montaje es usualmente de solo lectura se encuentre montada montada con permisos de escritura o carente de etiquetas de seguridad o una partición como /data esté montada con permisos de lectura en subcarpetas que contienen información de aplicaciones podría indicar montajes fraudulentos no autorizados evidenciando comportamientos altamente sospechosos.

**Ejemplo del contenido del archivo**

```
{
        "device": "/dev/block/mmcblk0p63",
        "mount_point": "/",
        "filesystem_type": "ext4",
        "mount_options": "ro,seclabel,relatime,discard",
        "options_list": [
            "ro",
            "seclabel",
            "relatime",
            "discard"
        ],
        "is_system_partition": false,
        "is_read_write": false
    }
  {
        "device": "tmpfs",
        "mount_point": "/dev",
        "filesystem_type": "tmpfs",
        "mount_options": "rw,seclabel,nosuid,relatime,size=1812632k,nr_inodes=453158,mode=755",
        "options_list": [
            "rw",
            "seclabel",
            "nosuid",
            "relatime",
            "size=1812632k",
            "nr_inodes=453158",
            "mode=755"
        ],
        "is_system_partition": false,
        "is_read_write": true
    },
    {
        "device": "devpts",
        "mount_point": "/dev/pts",
        "filesystem_type": "devpts",
        "mount_options": "rw,seclabel,relatime,mode=600,ptmxmode=000",
        "options_list": [
            "rw",
            "seclabel",
            "relatime",
            "mode=600",
            "ptmxmode=000"
        ],
        "is_system_partition": false,
        "is_read_write": true
    },
```

**Para aprender más:**

* [Descripción general de particiones de Android](https://source.android.com/docs/core/architecture/partitions?hl=es-419)   
* [Antecedentes y terminología de particiones dinámicas](https://source-android-com.translate.goog/docs/core/ota/virtual_ab?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=sge#background)  
* [File System of Android](https://medium.com/@aditi.kale20/file-system-of-android-a89dcbb693f1)   
* [Compatibilidad con el sistema de archivos del kernel de Android](https://source-android-com.translate.goog/docs/core/architecture/android-kernel-file-system-support?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc)  
* [SELinux compatibility](https://source.android.com/docs/security/features/selinux/compatibility)  
* [APEX file format](https://source.android.com/docs/core/ota/apex)  
* [SIstema de ficheros Android](https://keepcoding.io/blog/sistema-de-ficheros-android/) 

## Procesos y aplicaciones {#procesos-y-aplicaciones}

### aqf_packages.json {#aqf_packages.json}

La información de este archivo se genera mediante el módulo módulo [aqf\_packages](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/androidqf/aqf_packages.py).

**Información contenida**

Este archivo se encuentra en formato *json* y contiene información sobre las aplicaciones instaladas en el dispositivo. Esta información es extraída del archivo *packages.json* generado durante la adquisición de AndroidQF.

La información de este archivo se presenta de la siguiente manera:

* **name**: Nombre del paquete de la aplicación.  
* **files**: Ruta del archivo APK correspondiente con sus respectivos hashes e información del certificado.  
* **installer**: Desde cual aplicación se instaló.  
* **uid:** El PID asociado en ejecución.  
* **disabled**: Indica si la aplicación está deshabilitada.  
* **system**: Indica si el paquete pertenece al sistema.  
* **third\_party**: Indica si es una aplicación de terceros.

**¿Por qué es importante?**  
El contenido de este archivo incluye información que permite identificar aplicaciones instaladas y cuál es su estado en el dispositivo. Esto ayuda a los analistas a evaluar si existen aplicaciones de riesgo o maliciosas, que permisos tienen y cuales pueden comprometer la seguridad.

**Estructura del archivo:**

```
{
        "name": "com.samsung.android.arzone",
        "files": [
            {
                "path": "/data/app/ARZone/ARZone.apk",
                "local_name": "",
                "md5": "947b59f40de694e2359c007abe0c0191",
                "sha1": "508d9207ca6218bf599171c13f8141c37e97f580",
                "sha256": "76f972c04be51d0cad7980df85f76219eebfc0f770001e8ef02b4fa9a180f9d4",
                "sha512": "3b34c13fb1150df1b347f0cc0913f55d17abe2be96354a64e2ed8369fdce5b2fb10c5748deb7a66409153b766d84039fa01b0a1ced1bf2ccb62ab5368b38599a",
                "error": "",
                "verified_certificate": true,
                "certificate": {
                    "Md5": "d087e72912fba064cafa78dc34aea839",
                    "Sha1": "9ca5170f381919dfe0446fcdab18b19a143b3163",
                    "Sha256": "34df0e7a9f1cf1892e45c056b4973cd81ccf148a4050d11aea4ac5a65f900a42",
                    "ValidFrom": "2011-06-22T12:25:12Z",
                    "ValidTo": "2038-11-07T12:25:12Z",
                    "Issuer": "C=KR, ST=South Korea, L=Suwon City, O=Samsung Corporation, OU=DMC, CN=Samsung Cert",
                    "Subject": "C=KR, ST=South Korea, L=Suwon City, O=Samsung Corporation, OU=DMC, CN=Samsung Cert",
                    "SignatureAlgorithm": "SHA1-RSA",
                    "SerialNumber": 15134792569865480918
                },
                "certificate_error": "",
                "trusted_certificate": true
            }
        ],
        "installer": "null",
        "uid": 10295,
        "disabled": false,
        "system": false,
        "third_party": true
    }
```

### root\_binaries.py {#root_binaries.py}

La información de este archivo se genera mediante el módulo [root\_binaries](https://github.com/mvt-project/androidqf/blob/main/modules/root_binaries.go)

**Información contenida**

Este archivo se encuentra en formato *json* y contiene una lista de binarios relacionados con rooting en el dispositivo extraída del archivo r*oot\_binaries.json* generado durante una extracción con AndoridQF.

Este módulo se encarga extraer los binarios del archivo base para después poder identificar binarios sospechosos de rooting y sus rastros. El formato aplicado es el siguiente:

* path: Ruta al binario de rooting encontrado.  
* binary\_name: Nombre del binario, pueden ser los siguientes:  
    * su  
    * busybox  
    * supersu  
    * Superuser.apk  
    * KingoUser.apk  
    * SuperSu.apk  
    * magisk  
    * magiskhide  
    * magiskinit  
    * magiskpolicy  
* desciption: Descripcion del binario de rooting, pueden ser los siguientes:  
    * su: SuperUser binary  
    * busybox: BusyBox utilities  
    * supersu: SuperSU root management  
    * Superuser.apk: Superuser app  
    * KingoUser.apk: KingRoot app  
    * SuperSu.apk: SuperSU app  
    * magisk: Magisk root framework  
    * magiskhide: Magisk hide utility  
    * magiskinit: Magisk init binary  
    * magiskpolicy: Magisk policy binary

**¿Por qué es importante?**

Este archivo detecta herramientas de rooting, lo cual puede representar un indicativo  de accesos no autorizados y escalada de privilegios que pueda exponer alguna vulnerabilidad.  Así mismo, permite al analista identificar binarios sospechosos que podrían haberse instalado sin el conocimiento del usuario y ayuda a determinar si el dispositivo ha sido manipulado.

**Ejemplo del contenido del archivo**

```
    {
        "path": "/system/xbin/su",
        "binary_name": "su",
        "description": "SuperUser binary"
    },
    {
        "path": "/system/bin/su",
        "binary_name": "su",
        "description": "SuperUser binary"
    },
    {
        "path": "/system/bin/busybox",
        "binary_name": "busybox",
        "description": "BusyBox utilities"
    },
    {
        "path": "/data/local/tmp/magisk",
        "binary_name": "magisk",
        "description": "Magisk root framework"
    }
```

## Archivos respaldados {#archivos-respaldados}

### aqf_files.json {#aqf_files.json}

La información de este archivo se genera mediante el módulo [files](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/androidqf/files.py).  

**Información contenida**

Este archivo se encuentra en formato json y contiene información sobre los archivos y sus metadatos en las rutas /sdcard/, /system, /data, etc., en el dispositivo. Esta información es extraída del archivo *files.json* generado durante la adquisición de AndroidQF.

Cada entrada incluye un archivo con sus metadatos como: la ruta completa del archivo, tamaño, marca de tiempo (indica última modificación del archivo y último acceso al archivo), permisos del archivo, identificador del propietario, mensajes de error y hashes sha1, sha256, sha512, md5 si es que están pre-calculados.

La información de este archivo se presenta de la siguiente manera:

* **path**: Ruta del archivo  
* **size**: Tamaño del archivo en bytes  
* **mode**: Permisos del archivo (lectura, escritura o ejecución en formato unix)  
* **user\_id**: Identificador del usuario propietario  
* **user\_name**: Nombre de usuario propietario   
* **group\_id**: Identificador del grupo propietario  
* **group\_name**: Nombre del grupo propietario  
* **changed\_time**: Fecha y hora en que se modificaron los metadatos del archivo   
* **modified\_time**:Fecha y hora en que se modificó el contenido del archivo  
* **access\_time**: Fecha y hora del último acceso al archivo  
* **error**: Registro de errores durante la lectura del archivo  
* **context**: Etiqueta de seguridad SELinux  
* **Hashses:** Valores calculados de los hashes asociados a cada archivo

**¿Por qué es importante?**

Este archivo tiene relevancia para identificar archivos de interés en una investigación forense, incluyendo potenciales archivos utilizados por atacantes para comprometer un dispositivo y hacer los análisis oportunos que permitan dar seguimiento a actividad maliciosa. 

**Estructura del archivo**:

```
        "path": "/sdcard/Android/.Trash/com.sec.android.app.myfiles/.nomedia",
        "size": 62,
        "mode": "-rw-rw----",
        "user_id": 10276,
        "user_name": "",
        "group_id": 1023,
        "group_name": "",
        "changed_time": "2025-07-28 03:46:55.000000",
        "modified_time": "2025-07-28 03:46:55.000000",
        "access_time": "2024-05-05 13:35:15.000000",
        "error": "",
        "context": "u:object_r:fuse:s0",
        "sha1": "",
        "sha256": "",
        "sha512": "",
        "md5": ""
    },
    {
        "path": "/sdcard/Android/.Trash/com.sec.android.app.myfiles/0d2b854e-bc86-4478-b0a9-6802f21ba015/1753640873997/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Images/.!%#@$/IMG-20250727-WA0000.jpg",
        "size": 130802,
        "mode": "-rw-rw----",
        "user_id": 10276,
        "user_name": "",
        "group_id": 1023,
        "group_name": "",
        "changed_time": "2025-07-28 03:46:55.000000",
        "modified_time": "2025-07-27 12:06:02.000000",
        "access_time": "2025-07-27 12:06:02.000000",
        "error": "",
        "context": "u:object_r:fuse:s0",
        "sha1": "",
        "sha256": "",
        "sha512": "",
        "md5": ""
    }
```

### sms.json {#sms.json}

La información de este archivo se genera mediante el módulo de backup [sms](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/backup/sms.py) y el backup helper [helpers](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/backup/helpers.py) y el parser [backup](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/parsers/backup.py).

**Información contenida**

El archivo se encuentra en formato *json* y contiene información sobre los mensajes SMS y MMS recibidos y almacenados en el dispositivo móvil.  Esta información es extraída del archivo *backup.ab* generado durante un extracción con AndroidQF.

En términos generales, la información del respaldo de mensajes SMS y MMS son buscados y desencriptados (si fuera necesario) para poder descomprimir este respaldo, parsear fechas, detectar enlaces y homologar formatos.

La información de este archivo se presenta de la siguiente manera:

* **address**: Número de teléfono o dirección que envió o recibió el mensaje.  
* **body**: Contenido el mensaje en texto plano  
* **date**: Marca de tiempo en formato Unix del momento de recepción.  
* **date\_sent**: Marca de tiempo en formato Unix de cuándo el mensaje fue enviado. Si el valor es 0, significa que el mensaje fue recibido.  
* **status**: Código de estado del mensaje:  
    * \-1: Desconocido o sin información  
    * 0: Completo  
    * 64: Pendiente de envío  
    * 128: Borrador  
* **type**:Ttipo de mensaje   
    * 1: Recibido  
    * 2: Enviado  
    * 3: Borrador  
    * 4: Saliente  
* **recipients**: Lista de destinatarios del mensaje.  
* **read**: Indicador de si el mensaje fue leído (1) o no leído (0).  
* **isodate**: Fecha en formato ISO, para facilitar la comprensión.  
* **direction**: Dirección del mensaje (si fue enviado o recibido).  
    * sent: Enviado  
    * received: Recibido  
* **links**: Lista de enlaces identificados dentro del cuerpo del mensaje.

**¿Por qué es importante?**

El contenido de este archivo incluye información que permite dar seguimiento a conversaciones y comunicaciones que indiquen riesgo o intentos de ataques con contenidos maliciosos que indiques un vector de ataque como phishing.

**Estructura del archivo:**

```
[
	{
    	"address": "12345",
    	"body": "Reactiva tu aplicación para seguir disfrutando del servicio. Si tienes algún problema, te pedimos que la reinstales desde https://example.com/reactivacion",
    	"date": "1597872498518",
    	"date_sent": "1597872496000",
    	"status": "-1",
    	"type": "1",
    	"recipients": ["12345"],
    	"read": "1",
    	"isodate": "2025-01-01 00:00:00.000",
    	"direction": "sent",
    	"links": ["https://example.com/reactivacion"]
	},
	{
    	"address": "54321",
    	"body": "Este es un mensaje de ejemplo relacionado con la verificación de tu cuenta.",
    	"date": "1601498392068",
    	"date_sent": "1601498390000",
    	"status": "-1",
    	"type": "1",
    	"recipients": ["54321"],
    	"read": "0",
    	"isodate": "2025-01-01 00:00:00.000",
    	"direction": "sent"
	}
]
```

