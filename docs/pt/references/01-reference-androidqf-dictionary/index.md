---
title: Dicionário de arquivos gerados pela ferramenta androidqf
summary: dicionário de arquivos resultantes do androidqf
keywords: android, androidqf, referência
lang: pt-br
tags: [explainer, intro]
last_updated: 2025-09-05
some_url:
created: 2025-06-16
comments: true
authors:
    - Jose Martinez
    - MariaLab
    - Data Privacy Brasil

---


# Dicionário de arquivos gerados pela ferramenta androidqf

Este documento faz **parte de um repositório de documentação técnica** que tem como objetivo estabelecer uma base de conhecimento comprovada, flexível e acessível para **impulsionar a análise forense consentida em benefício da sociedade civil**. Para organizar o conteúdo, é utilizado o [quadro de referência de documentação técnica Diataxis](https://diataxis.fr/).

Este recurso em particular se enquadra na categoria de [referências](https://diataxis.fr/reference) e contém informações sobre os arquivos gerados pelo [androidqf](https://github.com/mvt-project/androidqf) ao realizar uma extração forense de um dispositivo Android, com o objetivo de que uma pessoa analista **conheça os arquivos gerados, como utilizá-los, onde procurar informações específicas e em que formato as encontrará.

Este recurso foi atualizado pela última vez em 16 de junho de 2025 e, para a compilação das informações, foi utilizado como base a [verção 1.7.1](https://github.com/mvt-project/androidqf/tree/v1.7.1).

[Androidqf](https://github.com/mvt-project/androidqf) é uma ferramenta de extração forense que pertence ao [MVT Project](https://github.com/mvt-project/). Desenvolvida inicialmente por [Claudio Guarnieri](https://nex.sx/) e atualmente mantida pelo [Laboratório de Segurança da Anistia Internacional](https://securitylab.amnesty.org/es/).

Seu nome vem da expressão em inglês *Android Quick Forensics*. Caracteriza-se por ser uma **ferramenta portátil**, ou seja, pode ser executada no Windows, GNU/Linux e Mac OS através de um binário pré-compilado para a [aquisição de informações forenses](../../explainers/01-explainer-introduction-digital-forensics/index.md#quais-são-as-etapas-de-uma-investigação-forense) de dispositivos Android. 

As informações geradas pelo androidqf podem ser agrupadas em 5 categorias principais:

* Detalhes da aquisição
* Configuração do dispositivo
* Informações sobre registros e eventos do sistema
* Processos e aplicativos
* Arquivos copiados

## Aquisição e Extração

### acquisition.json

As informações deste arquivo são geradas pelo módulo [acquisition.go](https://github.com/mvt-project/androidqf/blob/main/acquisition/acquisition.go)*.*

**O que este arquivo contém?**

Este arquivo está no formato *json* e registra informações relacionadas ao processo de aquisição de dados do dispositivo. Ele contém as seguintes informações:
* Identificador único ou UUID da extração (usado como nome da pasta onde as informações são armazenadas.
* Versão do androidqf.
* Local onde a extração é armazenada.
* Data e hora de início e término da aquisição.
* Informações do binário *collector* utilizado.
* Informações do binário *adb* utilizado.
* Localização do armazenamento *sdcard*.
* Arquitetura da CPU do dispositivo.
* 
**Por que isso é importante?**

Essas informações permitem conhecer informações básicas da extração e obter identificadores únicos do sistema que facilitam o [processo de custódia da extração forense](../../explainers/01-explainer-introduction-digital-forensics/index.md#cadeia-de-custódia). 

**Exemplo:**

```
{
 "uuid": "0f615832-ed22-411e-9317-b429d28ecf9a",
 "androidqf_version": "v1.7.0-1-gf7642bf",
 "storage_path": "/home/user/0f615832-ed22-411e-9317-b429d28ecf9a",
 "started": "2025-01-01T18:36:37.443498116Z",
 "completed": "2025-01-01T18:50:04.947856405Z",
 "collector": {
  "ExePath": "/data/local/tmp/collector",
  "Installed": false,
  "Adb": {
   "ExePath": "/usr/bin/adb",
  },
  "Architecture": "arm64-v8a"
 },
 "tmp_dir": "/data/local/tmp/",
 "sdcard": "/sdcard/",
 "cpu": "arm64-v8a"
}
```

### command.log

As informações deste arquivo são geradas pelo módulo [logger.go](https://github.com/mvt-project/androidqf/blob/main/log/logger.go). Este módulo apresenta os registros do processo de captura e aquisição das informações.

**Informações contidas**

Este arquivo está em texto simples com extensão *.log* e contém um registro dos comandos executados durante a aquisição de dados. Ele documenta cada comando usado (*DEBUG*) e sua saída na tela (*INFO*), mensagens de alerta (*WARNING*) e mensagens de erro (*ERROR*) durante a execução. Ele usa o seguinte formato:

* Data e hora do comando ou mensagem
* Tipo de mensagem
* Conteúdo da mensagem

**Por que é importante?**

Permite gerar um registro das ações realizadas pelo aplicativo durante a aquisição de informações. Através deste registro, é possível  verificar a integridade da extração, garantindo que todas as etapas foram realizadas; ou, caso existam alertas ou erros, permite identificá-los.

**Exemplo do conteúdo do arquivo**

```
2025-01-01T14:22:39-06:00 [INFO] Started new acquisition in /home/user/1c3c6742-f225-479f-a836-4a6a86a056b7
2025-01-01T14:22:39-06:00 [INFO] Would you like to take a backup of the device?
2025-01-01T14:22:41-06:00 [INFO] Generating a backup with argument com.android.providers.telephony. Please check the device to authorize the backup...

2025-01-01T14:22:52-06:00 [INFO] Backup completed!
2025-01-01T14:22:52-06:00 [INFO] Collecting information on installed apps. This might take a while...
2025-01-01T14:22:52-06:00 [INFO] Collecting device properties...
2025-01-01T14:22:52-06:00 [INFO] Collecting device diagnostic information. This might take a while...
2025-01-01T14:24:11-06:00 [INFO] Collecting list of running processes...
2025-01-01T14:24:11-06:00 [DEBUG] Deploying collector binary 'collector_arm64' for architecture 'arm64-v8a'.
2025-01-01T14:24:11-06:00 [INFO] Collecting list of services...
2025-01-01T14:24:12-06:00 [INFO] Generating a bugreport for the device...
2025-01-01T14:26:22-06:00 [DEBUG] Bugreport completed!
2025-01-01T14:26:22-06:00 [INFO] Collecting list of files... This might take a while...
2025-01-01T14:26:22-06:00 [DEBUG] Using collector to collect list of files
2025-01-01T14:39:20-06:00 [INFO] Collecting device settings...
2025-01-01T14:39:20-06:00 [INFO] Collecting SELinux status...
```

### hashes.csv

As informações deste arquivo são geradas pela função [*HashFiles*](https://github.com/mvt-project/androidqf/blob/main/acquisition/acquisition.go#L134) do módulo [acquisition.go](https://github.com/mvt-project/androidqf/blob/main/acquisition/acquisition.go). 

**Informações contidas**

Este arquivo está no formato [csv](https://pt.wikipedia.org/wiki/Comma-separated_values) e armazena os hashes [SHA-256](https://pt.wikipedia.org/wiki/SHA-2) para cada arquivo gerado durante a extração ou cópia do do dispositivo. Segue a estrutura:

* Localização e nome do arquivo
* Valor hash utilizando *sha256*

**Por que é importante?**

Os hashes permitem garantir a integridade das informações e assegurar que elas não tenham sido modificadas após a aquisição, favorecendo também os procedimentos de cadeia de custódia.

**Exemplo do conteúdo do arquivo**

```
2ab44150-35d3-4b40-a820-c9152fe93a13\apks\gov.dhs.cbp.cbpone_gov.dhs.cbp.cbpone-NYwrqdamzef6AVKRRGXzgA.apk,2d553aada9039d4def18a09b84c317a70d9fdde87524a043db5f0eeb1862e89a
2ab44150-35d3-4b40-a820-c9152fe93a13\backup.ab,48202a8cb422d7eeb12ff8ad13fac3a67b37600c63eae8089d9674465da32990
2ab44150-35d3-4b40-a820-c9152fe93a13\bugreport.zip,ec82812dba70891b78d7130dc16e3474918e4a0e02bb15ec00e1015679f720ee
2ab44150-35d3-4b40-a820-c9152fe93a13\command.log,c0ae883bebee7503b0ca94a54cdbb43628602046c68b770c760f730a55d6dc8c
2ab44150-35d3-4b40-a820-c9152fe93a13\dumpsys.txt,e54a613502ca362584766c0f75e17ca366d7ecdc4aa6869c50424dff83acbc15
2ab44150-35d3-4b40-a820-c9152fe93a13\env.txt,387301687084cca0e124a9c365e930b4e5e6303b3e6f9dc64e2146f168b79c1a
2ab44150-35d3-4b40-a820-c9152fe93a13\files.json,832f8121a69f131c9f434e1ca68d7b1e2deda40de72ff8396ea386a6a8cf69d3
2ab44150-35d3-4b40-a820-c9152fe93a13\getprop.txt,b8dbad7e900aeeb3c60e48dd988c44905741a7e5b124055a09c2c417aa1556b3
2ab44150-35d3-4b40-a820-c9152fe93a13\hashes.csv,cea94f56c720436d217b44ee746e2a6d69ddd226325a94bf3a3adeb32be4658a
2ab44150-35d3-4b40-a820-c9152fe93a13\logcat.txt,6c080ba0357c6e82818e5a89135ff06aa9386f811daf898fc1797e1b9e6299d3
2ab44150-35d3-4b40-a820-c9152fe93a13\logs\data\anr\anr_2024-12-20-00-11-38-831,e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
2ab44150-35d3-4b40-a820-c9152fe93a13\logs\sdcard\log\thermal_log-shm,e9eed4a2f55edd11e022b7b089d69a5de929d2bd484041a64e957861a5ab055b
2ab44150-35d3-4b40-a820-c9152fe93a13\packages.json,69d560bfbbb75e074a49d107811c350461badac885b3925ed816d716f1f1144a
2ab44150-35d3-4b40-a820-c9152fe93a13\processes.txt,9e933447e79e4743722691af88e9a4bdcc11029a92b84b0ebd9d54e0bfcf2694
2ab44150-35d3-4b40-a820-c9152fe93a13\root_binaries.json,4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
2ab44150-35d3-4b40-a820-c9152fe93a13\selinux.txt,1ca5672ae970bdc4f5b584898245b3d884e11deb6867e9563bdfbc8b82e8f62e
2ab44150-35d3-4b40-a820-c9152fe93a13\services.txt,b3ae6ad626b3a5ba8fc3b68771d42baf9795e03cc7b4b1ccbe361d9625e0f1fe
2ab44150-35d3-4b40-a820-c9152fe93a13\settings_global.txt,410f788450907331183ee36979e93fc7dc0b1805e574d1ac1d5fbc9869897c53
2ab44150-35d3-4b40-a820-c9152fe93a13\settings_secure.txt,be67f431c457edfb88d733594aba662310dbe3863c62da21cbf7dad5bcc0f136
2ab44150-35d3-4b40-a820-c9152fe93a13\settings_system.txt,b0e7452110867ca3f5c15ea52b9b9a198433a836f97d6fd8b95fcd39fd30c714
```

## Información y configuración del dispositivo 

### getprop.txt 

As informações deste arquivo são geradas pelo módulo [getprop.go](https://github.com/mvt-project/androidqf/blob/main/modules/getprop.go).

**Informações contidas**

Este arquivo está no formato *TXT* e contém a saída do comando `adb getprop`, que detalha as **propriedades do sistema**.

As propriedades do sistema são pares chave-valor de strings que são armazenadas no dicionário global [*build.prop*](https://xdaforums.com/t/guide-build-prop-wiki.2056266/) ou em arquivos de descrição *.sysprop*, e fornecem uma maneira conveniente de compartilhar configurações dentro do sistema.
As informações podem ser encontradas usando o seguinte formato:

```
[{prefix}.]{group}[.{subgroup}]*.{name}[.{type}]
```

Algumas propriedades aparecem com o prefixo *ro*, indicando que são propriedades somente de leitura ou que foram atribuídas após a reinicialização do dispositivo. As propriedades com o prefixo *persist* referem-se a configurações resistentes à reinicialização. Algumas propriedades não terão prefixo, portanto, começam diretamente com o grupo ao qual pertencem.

Os grupos mais comuns são:
* *bluetooth*, relacionado ao Bluetooth
* *boot*, sysprops da linha de comando do kernel
* *build*, sysprops que identificam uma compilação
* *telephony*, relacionado à telefonia
* *audio*, relacionado ao áudio
* *graphics*, relacionado aos gráficos
* *vold*, relacionado ao vold que gerencia a montagem de volumes físicos de armazenamento externo

Para mais detalhes, consulte a [lista de propriedades já definidas no código-fonte do Android](https://android.googlesource.com/platform/system/sepolicy/+/refs/heads/main/private/property_contexts).

**Por que isso é importante?**

As propriedades fornecem informações importantes sobre o hardware e o software do dispositivo, que podem ser alteradas por software malicioso para ocultar sua presença ou modificar o comportamento do dispositivo de forma inadvertida.

**Exemplo do conteúdo do arquivo**

```
[property_name]: [value]
[aaudio.hw_burst_min_usec]: [2000]
[aaudio.mmap_exclusive_policy]: [2]
[aaudio.mmap_policy]: [2]
[apex.all.ready]: [true]
[bluetooth.device.class_of_device]: [90,2,12]
[ro.boot.product.model]: [SM-A715F]
[ro.boot.serialno]: [R58N84XXXXX]
[ro.bootimage.build.date]: [Thu Feb 29 13:55:21 +07 2024]
[ro.bootimage.build.date.utc]: [1709189721]
[ro.bootimage.build.fingerprint]: [samsung/a71naxx/a71:11/RP1A.200720.012/A715FXXSBDXB1:user/release-keys]
[ro.build.selinux]: [1]
[ro.build.selinux.enforce]: [1]
[ro.build.version.security_patch]: [2024-02-01]
[ro.gfx.driver.1]: [com.qualcomm.qti.gpudrivers.sm6150.api30]
[ro.hardware]: [qcom]
[ro.hardware.chipname]: [SM7150]
[ro.product.system.model]: [SM-A715F]
[ro.vendor.product.cpu.abilist]: [arm64-v8a,armeabi-v7a,armeabi]
[ro.vendor.product.cpu.abilist32]: [armeabi-v7a,armeabi]
[ro.vendor.product.cpu.abilist64]: [arm64-v8a]
```

**Saiba mais**

* [Visão geral da configuração | Propriedades do sistema | Android Open Source Project](https://source.android.com/docs/core/architecture/configuration?hl=es-419#system-properties)   
* [Como implementar propriedades do sistema como APIs | Android Open Source Project](https://source.android.com/docs/core/architecture/configuration/sysprops-apis?hl=es-419)  
* [Adicionar propriedades do sistema | Android Open Source Project](https://source.android.com/docs/core/architecture/configuration/add-system-properties?hl=es-419)  
* [Compatibilidade de políticas | Android Open Source Project](https://source.android.com/docs/security/features/selinux/compatibility?hl=es-419#system-property-and-ownership) 

### selinux.txt 

As informações deste arquivo são geradas pelo módulo [selinux.go](https://github.com/mvt-project/androidqf/blob/main/modules/selinux.go)*.*

**Informações contidas**

Este arquivo está no formato *txt* e contém a saída do comando `adb shell getenforce` e indica a política de segurança *SELinux* aplicada no dispositivo, indicando o modo em que se encontra (*enforcing*, *permissive* ou *disabled*).

**Por que isso é importante?**

[*SELinux*](https://en.wikipedia.org/wiki/Security-Enhanced_Linux) é uma camada de segurança fundamental no Android. Alterações na sua configuração podem ser um indicativo de compromissos na segurança do dispositivo.

**Exemplo do conteúdo do arquivo**

```
Enforcing
```

**Saiba mais**

* [Conceitos do SELinux | Android Open Source Project](https://source.android.com/docs/security/features/selinux/concepts?hl=pt-br)
* [Projeto SELinux](https://github.com/selinuxproject)
* [O que é SElinux? SELinux (Security Enhanced Linux) permite configurar o nível de segurança dos seus sistemas Linux](https://www.redhat.com/pt-br/topics/linux/what-is-selinux)

### settings\_global.txt 

As informações deste arquivo são geradas pelo módulo [settings.go](https://github.com/mvt-project/androidqf/blob/main/modules/settings.go)*.*

**Informações contidas**

Este arquivo está no formato *txt* e contém a saída do comando `adb shell cmd settings list global` , que mostra as preferências que sempre se aplicam de forma idêntica a todos os usuários definidos ([well-defined user](https://source.android.com/docs/devices/admin/multi-user#user_types)). Os aplicativos podem lê-las, mas não podem gravá-las, pois são preferências que o usuário deve modificar explicitamente por meio da interface do usuário do sistema ou APIs especializadas para esses valores.

Essas configurações incluem opções de desenvolvedor, inicialização e status da conexão Bluetooth, Wi-Fi e telefonia. Para ver a [lista completa de preferências globais](https://developer.android.com/reference/android/provider/Settings.Global), consulte a documentação correspondente do Android.

**Por que isso é importante?**

Permite identificar configurações anormais que podem comprometer a segurança, a privacidade ou a funcionalidade do dispositivo. Configurações padrão incomuns podem indicar tentativas de alterar o comportamento do sistema, intencionais ou acidentais.

**Exemplo do conteúdo do arquivo**

```
Phenotype_boot_count=68
adb_enabled=1
airplane_mode_on=0
bluetooth_on=1
boot_count=71
bug_report=0
default_device_name=Galaxy A14 5G
package_verifier_user_consent=1
phone_play_store_availability=0
require_password_to_decrypt=1
spam_call_enable=1
subscription_mode=0
turnOff_5g_network_mode_set=0
wifi_networks_available_notification_on=0
wifi_on=1
wifi_scan_always_enabled=1
zram_enabled=1
```

**Saiba mais**

* [Configurações | Desenvolvedores Android](https://developer.android.com/reference/android/provider/Settings)
* [Configurações.Global | Desenvolvedores Android](https://developer.android.com/reference/android/provider/Settings.Global?hl=es-419)

### settings\_secure.txt 

As informações deste arquivo são geradas pelo módulo [settings.go](https://github.com/mvt-project/androidqf/blob/main/modules/settings.go)*.*

**Informações contidas**

Este arquivo está no formato *txt* e contém a saída do comando `adb shell cmd settings list secure` Mostra as preferências de segurança do sistema que os aplicativos podem ler, mas não gravar. São preferências que o usuário deve modificar explicitamente através da interface do usuário de um aplicativo do sistema. 

Os aplicativos normais não podem modificar o banco de dados de configurações de segurança. Essas configurações incluem opções de desenvolvedor, acessibilidade, localização, entrada de dados, bloqueio de tela, controle parental, conversão de texto em fala e conexão Bluetooth, Wi-Fi e telefonia. 

Para ver a [lista completa de preferências de segurança](https://developer.android.com/reference/android/provider/Settings.Secure?hl=es-419), consulte a documentação correspondente do Android.

**Por que isso é importante?**

Permite identificar configurações anormais que podem comprometer a segurança, a privacidade ou a funcionalidade do dispositivo. Configurações padrão incomuns podem indicar tentativas de modificar o comportamento do sistema, intencionais ou acidentais.

**Exemplo do conteúdo do arquivo**

```
accessibility_allow_diagonal_scrolling=1
accessibility_button_mode=1
accessibility_button_target_component=com.android.settings/com.samsung.android.settings.accessibility.shortcut.AmplifyShortcut
accessibility_display_magnification_enabled=0
accessibility_enabled=0
android_id=af4de9XXXXXXXXXX
autofill_service=null
assistant=com.google.android.googlequicksearchbox/com.google.android.voiceinteraction.GsaVoiceInteractionService
aware_enabled=0
backup_auto_restore=1
backup_encryption_opt_in_displayed=1
bluetooth_settings_foreground=0
clipboard_show_access_notifications=0
default_input_method=com.samsung.android.honeyboard/.service.HoneyBoardService
fingerprint_screen_lock=1
location_mode=3
location_time_zone_detection_enabled=1
lockscreen.disabled=0
wifi_saved_state=0
```

**Saiba mais**

* [Settings | Android Developers](https://developer.android.com/reference/android/provider/Settings?hl=es-419)   
* [Settings.Secure | Android Developers](https://developer.android.com/reference/android/provider/Settings.Secure?hl=es-419) 

### settings\_system.txt 

As informações deste arquivo são geradas pelo módulo [settings.go](https://github.com/mvt-project/androidqf/blob/main/modules/settings.go)*.*

**Informações contidas**

Este arquivo está no formato *txt* e contém a saída do comando `adb shell cmd settings list system` , que mostra várias preferências gerais do dispositivo. Essas preferências afetam a experiência do usuário e o funcionamento básico do dispositivo.

Essas configurações incluem opções de sensores como acelerômetro ou giroscópio, fuso horário, tela, alarmes, som, vibração, atualizações e conexão Bluetooth, Wi-Fi e telefonia.

Para ver a [lista completa de preferências do sistema](https://developer.android.com/reference/android/provider/Settings.System?hl=es-419), consulte a documentação correspondente do Android.

**Por que isso é importante?**

Permite identificar configurações anormais que podem comprometer a segurança, privacidade ou funcionalidade do dispositivo. Configurações padrão incomuns podem indicar tentativas de modificar o comportamento do sistema, intencionais ou acidentais.

**Exemplo do conteúdo do arquivo**

```
FOTA_CLIENT_POLLING_TIME=1710699386219
FOTA_CLIENT_REGISTRATION=1
FOTA_CLIENT_TEST=0
SEM_VIBRATION_FORCE_TOUCH_INTENSITY=4
SEM_VIBRATION_NOTIFICATION_INTENSITY=5
SOFTWARE_UPDATE_LAST_CHECKED_DATE=1728477705778
SOFTWARE_UPDATE_WIFI_ONLY2=1
alarm_alert_set=1
anykey_mode=0
aod_mode=0
automatic_unlock=1
block_unwanted_call=1
block_unwanted_call_type=1
lockscreen_sounds_enabled=1
lockscreen_wallpaper=1
login_state=0
mic_mode_enable=0
mic_mode_wificall=0
samsung_errorlog_agree=1
tty_mode=0
unknown_mode=0
volume_alarm=11
volume_alarm_ble_headset=11
volume_alarm_earpiece=11
volume_alarm_speaker=11
volume_assistant=7
wifi_call_enable1=0
wifi_call_preferred1=2
wifi_call_when_roaming1=0
wireless_fast_charging=0
```

**Saiba mais**

* [Settings | Android Developers](https://developer.android.com/reference/android/provider/Settings?hl=es-419)   
* [Settings.System | Android Developers](https://developer.android.com/reference/android/provider/Settings.System?hl=es-419) 

### env.txt 

As informações deste arquivo são geradas pelo módulo [env.go](https://github.com/mvt-project/androidqf/blob/main/modules/env.go)*.*

**Informações contidas**

Este arquivo está no formato *txt* e contém a saída do comando `adb shell env`, que mostra a configuração das variáveis de ambiente do terminal (shell) [*mkshrc*](http://mirbsd.de/mksh), que é usado pelo Android.
Por padrão, as variáveis *mkshrc* no Android estão no arquivo *mkshrc* ou *profile*, que pode estar em um dos seguintes diretórios.

```
/system/etc
/system/etc/profile
$HOME/
/data/local
```

Enquanto que [o binário *mkshrc* pode ser encontrado em algum dos seguintes diretórios](https://android.googlesource.com/platform/bionic/+/refs/heads/master/libc/include/paths.h#50).

```
/product/bin
/apex/com.android.runtime/bin
/apex/com.android.art/bin
/system_ext/bin
/system/bin
/system/xbin
/odm/bin
/vendor/bin
/vendor/xbin
```

As variáveis contidas podem indicar:

* Localizações de partições
* Valores do ambiente de execução da máquina virtual Android
* Configurações do terminal

**Por que isso é importante?**

As variáveis de ambiente podem indicar alterações nas configurações do terminal, do interpretador de comandos, do ambiente de execução da máquina virtual Android ou dos pontos de montagem de algumas partições e pastas. Isso pode ser um indicador de comportamento suspeito.

**Exemplo do conteúdo do arquivo**

```
_=/system/bin/env
ANDROID_DATA=/data
ANDROID_ART_ROOT=/apex/com.android.art
LOGNAME=shell
STANDALONE_SYSTEMSERVER_JARS=/apex/com.android.btservices/javalib/service-bluetooth.jar:/apex/com.android.devicelock/javalib/service-devicelock.jar:/apex/com.android.os.statsd/javalib/service-statsd.jar:/apex/com.android.scheduling/javalib/service-scheduling.jar:/apex/com.android.tethering/javalib/service-connectivity.jar:/apex/com.android.uwb/javalib/service-uwb.jar:/apex/com.android.wifi/javalib/service-wifi.jar:/apex/com.samsung.android.lifeguard/javalib/service-lifeguard.jar
HOME=/
ANDROID_TZDATA_ROOT=/apex/com.android.tzdata
ANDROID_ROOT=/system
TERM=xterm-256color
SHELL=/bin/sh
ANDROID_BOOTLOGO=1
ANDROID_ASSETS=/system/app
ANDROID_SOCKET_adbd=21
HOSTNAME=a14x
DOWNLOAD_CACHE=/data/cache
SECONDARY_STORAGE=/storage/sdcard:/storage/usb1:/storage/usb2
ANDROID_STORAGE=/storage
USER=shell
TMPDIR=/data/local/tmp
PATH=/product/bin:/apex/com.android.runtime/bin:/apex/com.android.art/bin:/system_ext/bin:/system/bin:/system/xbin:/odm/bin:/vendor/bin:/vendor/xbin
SYSTEMSERVERCLASSPATH=/system/framework/com.android.location.provider.jar:/system/framework/knoxanalyticssdk.jar:/system/framework/mcfsdk.jar:/system/framework/uibc_java.jar:/system/framework/services.jar:/system/framework/semwifi-service.jar:/system/framework/ssrm.jar:/apex/com.android.adservices/javalib/service-adservices.jar:/apex/com.android.adservices/javalib/service-sdksandbox.jar:/apex/com.android.appsearch/javalib/service-appsearch.jar:/apex/com.android.art/javalib/service-art.jar:/apex/com.android.configinfrastructure/javalib/service-configinfrastructure.jar:/apex/com.android.healthfitness/javalib/service-healthfitness.jar:/apex/com.android.media/javalib/service-media-s.jar:/apex/com.android.ondevicepersonalization/javalib/service-ondevicepersonalization.jar:/apex/com.android.permission/javalib/service-permission.jar:/apex/com.android.rkpd/javalib/service-rkp.jar:/apex/com.samsung.android.shell/javalib/service-samsung-shell.jar
ASEC_MOUNTPOINT=/mnt/asec
ANDROID_I18N_ROOT=/apex/com.android.i18n
EXTERNAL_STORAGE=/sdcard
```

**Saiba mais**

* [Shell (informática) \- Wikipedia, a enciclopédia livre](https://pt.wikipedia.org/wiki/Shell_(computa%C3%A7%C3%A3o))  
* [Can I update the adb shell's environment variables? \- Android Enthusiasts Stack Exchange](https://android.stackexchange.com/questions/53389/can-i-update-the-adb-shells-environment-variables/64926#64926)   
* [Update mksh to latest version \- Android Enthusiasts Stack Exchange](https://android.stackexchange.com/questions/217617/update-mksh-to-latest-version/217627#217627) 


## Registros e eventos do sistema

### logcat.txt y logcat\_old.txt 

As informações desses arquivos são geradas pelo módulo [logcat.go](https://github.com/mvt-project/androidqf/blob/main/modules/logcat.go) .

**Informações contidas**

Esses arquivos estão em texto simples com extensão .*txt* e contêm a saída dos comandos `adb shell logcat -d -b all` e `adb shell logcat -L -b all`, respectivamente, que mostram o registro de mensagens do sistema. Alguns exemplos das informações contidas são:

* Mensagens de erro e aviso (FATAL EXCEPTION).
* Mensagens de aplicativos, processos e serviços do sistema operacional.
* Logs de depuração e eventos informativos.

O arquivo contém a seguinte estrutura:

* Início do registro (contém divisões de registros).
* Marca de tempo (timestamp).
* Identificador do processo e do thread (PID) e (TID).
- Nível de prioridade:
    - E: Erro
    - W: Aviso (de _Warning_, em inglês_)
    - I: Informação
    - D: Depuração
    - F: Fatal
    - V: Verborrágico (de _Verbose_, em inglês_)
* Etiqueta que indica o componente ou processo do sistema.
* Descrição e detalhes das mensagens ou erros.

**Por que é importante?**

Essas informações podem ser utilizadas para analisar o comportamento e a execução de eventos no sistema e nas aplicações do dispositivo, a fim de identificar anomalias ou padrões que possam indicar a presença de malware. Em termos forenses, são os arquivos mais relevantes devido ao seu conteúdo.


**Exemplo do conteúdo do arquivo**

```
--------- beginning of crash  
2025-01-01 00:00:00.000 12345 12345 E AndroidRuntime: FATAL EXCEPTION: main  
2025-01-01 00:00:00.000 12345 12345 E AndroidRuntime: Process: example.android.app, PID: 12345  
2025-01-01 00:00:00.000 12345 12345 E AndroidRuntime: java.lang.RuntimeException: Unable to instantiate receiver example.android.app.MyBroadCastReceiver  
2025-01-01 00:00:00.000 12345 12345 E AndroidRuntime: at android.app.ActivityThread.handleReceiver(ActivityThread.java:4861)  
2025-01-01 00:00:00.000 12345 12345 E AndroidRuntime: at android.os.Handler.dispatchMessage(Handler.java:106)  
2025-01-01 00:00:00.000 30144 30860 I ActivityManager: Process example.android.app has died.  
```

**Saiba mais**

* [Ferramenta de linha de comando Logcat](https://developer.android.com/tools/logcat?hl=pt-br)

### dumpsys.txt 

As informações deste arquivo são geradas pelo módulo [dumpsys.go](https://github.com/mvt-project/androidqf/blob/main/modules/dumpsys.go) .

**Informações contidas**

Este arquivo está no formato *txt* e contém a saída do comando `adb shell dumpsys`, que mostra informações detalhadas sobre os serviços em execução, incluindo processos e aplicativos.

O arquivo é dividido em seções específicas para cada serviço, seguindo uma ordem:

* Lista de serviços ativos
* Detalhes de cada serviço
* Logs detalhados

Para conhecer a lista de serviços que podem ser encontrados em um *dumpsys* de um dispositivo, execute o comando `adb shell service list`

**Por que é importante?**

O arquivo fornece uma perspectiva completa do estado do sistema no dispositivo, fundamental para conhecer a atividade realizada por serviços, aplicativos e processos no dispositivo. Em termos forenses, é um dos arquivos mais relevantes devido ao seu conteúdo.

**Exemplo do conteúdo do arquivo**

```
Currently running services:
  accessibility
  account
  adb
  alarm
  android.frameworks.cameraservice.service.ICameraService/default
  android.hardware.biometrics.face.IFace/default
  android.hardware.vibrator.IVibratorManager/default
  android.os.UpdateEngineService
  android.security.authorization
  anrmanager
  anti_root_dialog
  app_binding
  appops
  audio
  auth
  battery
  batteryproperties
  batterystats
  bluetooth_manager
  bugreport
  cpuinfo
  critical.log
  dataloader_manager
  dbinfo
  input
  logcat
  meminfo
  netstats
  ostats_pullerd
  ostats_tpd
  ostatsd
  package
  permission
  phone
  power
  processinfo
  procstats
  settings
  stats
  statsbootstrap
  usb
  wifi
  window

-------------------------------------------------------------------------------
DUMP OF SERVICE AtlasService:
--------- 0.001s was the duration of dumpsys AtlasService, ending at: 2025-05-08 18:12:33
-------------------------------------------------------------------------------
DUMP OF SERVICE DockObserver:
Current Dock Observer Service state:
  reported state: 0
  previous state: 0
  actual state: 0
--------- 0.007s was the duration of dumpsys DockObserver, ending at: 2025-05-08 18:12:33
-------------------------------------------------------------------------------
DUMP OF SERVICE ISubsysRadio:
--------- 0.005s was the duration of dumpsys ISubsysRadio, ending at: 2025-05-08 18:12:33
-------------------------------------------------------------------------------
DUMP OF SERVICE MMListService:
--------- 0.001s was the duration of dumpsys MMListService, ending at: 2025-05-08 18:12:33
-------------------------------------------------------------------------------
DUMP OF SERVICE OPLUSExService:
--------- 0.001s was the duration of dumpsys OPLUSExService, ending at: 2025-05-08 18:12:33
-------------------------------------------------------------------------------
DUMP OF SERVICE OplusLocationManager:
--------- 0.001s was the duration of dumpsys OplusLocationManager, ending at: 2025-05-08 18:>
-------------------------------------------------------------------------------
DUMP OF SERVICE appops:
Current AppOps Service state:
  Settings:
	top_state_settle_time=+5s0ms
	fg_service_state_settle_time=+5s0ms
	bg_state_settle_time=+1s0ms

  Op mode watchers:
	Op COARSE_LOCATION:
  	#0: ModeCallback{12983a3 watchinguid=-1 flags=0x0 op=READ_WRITE_HEALTH_DATA from uid=1000 pid=1807}
  	#1: ModeCallback{21558a8 watchinguid=-1 flags=0x1 op=MONITOR_LOCATION from uid=u0a124 pid=3315}
  	#2: ModeCallback{c7241f6 watchinguid=-1 flags=0x1 op=COARSE_LOCATION from uid=1000 pid=1807}
  	#3: ModeCallback{f993e3b watchinguid=-1 flags=0x1 op=FINE_LOCATION from uid=u0a124 pid=3315}
	Op FINE_LOCATION:
  	#0: ModeCallback{12983a3 watchinguid=-1 flags=0x0 op=READ_WRITE_HEALTH_DATA from uid=1000 pid=1807}
  	#1: ModeCallback{e5bfc6d watchinguid=-1 flags=0x1 op=FINE_LOCATION from uid=1000 pid=1807}
  	#2: ModeCallback{f993e3b watchinguid=-1 flags=0x1 op=FINE_LOCATION from uid=u0a124 pid=3315}
	Op READ_CONTACTS:
  	#0: ModeCallback{12983a3 watchinguid=-1 flags=0x0 op=READ_WRITE_HEALTH_DATA from uid=1000 pid=1807}
	Op WRIT E_CONTACTS:
  	#0: ModeCallback{12983a3 watchinguid=-1 flags=0x0 op=READ_WRITE_HEALTH_DATA from uid=1000 pid=1807}
	Op READ_CALL_LOG:
  	#0: ModeCallback{12983a3 watchinguid=-1 flags=0x0 op=READ_WRITE_HEALTH_DATA from uid=1000 pid=1807}
	Op WRITE_CALL_LOG:
  	#0: ModeCallback{12983a3 watchinguid=-1 flags=0x0 op=READ_WRITE_HEALTH_DATA from uid=1000 pid=1807}
	Op READ_CALENDAR:
  	#0: ModeCallback{12983a3 watchinguid=-1 flags=0x0 op=READ_WRITE_HEALTH_DATA from uid=1000 pid=1807}
	Op WRITE_CALENDAR:
  	#0: ModeCallback{12983a3 watchinguid=-1 flags=0x0 op=READ_WRITE_HEALTH_DATA from uid=1000 pid=1807}
	Op POST_NOTIFICATION:
  	#0: ModeCallback{12983a3 watchinguid=-1 flags=0x0 op=READ_WRITE_HEALTH_DATA from uid=1000 pid=1807}


```

**Saiba mais**

* [dumpsys no Android](https://developer.android.com/tools/dumpsys?hl=es-419)

### bugreport.zip 

As informações deste arquivo são geradas pelo módulo [bugreport.go](https://github.com/mvt-project/androidqf/blob/main/modules/bugreport.go) .

**Informações contidas**

Este é um arquivo compactado no formato *zip* e contém a saída do comando `adb shell bugreport`, que é um relatório completo sobre o estado atual do dispositivo, incluindo dados do sistema, logs e configurações.

Este arquivo compactado pode ser analisado pela ferramenta MVT através do comando `mvt-android check-bugreport bugreport.zip`

Os arquivos e pastas contidos no compactado incluem o seguinte:

* **dumpstate-yyyy-mm-dd-hh-mm-ss.txt:** Arquivo que fornece um resumo das principais características do dispositivo móvel e o estado atual do sistema.
* **dumpstate_board.txt:** Arquivo que fornece logs de inicialização do sistema com dados detalhados sobre os eventos e serviços executados durante a inicialização do dispositivo.
* **dumpstate_log.txt:** Arquivo que apresenta os logs do processo de geração do relatório. Contém possíveis erros ou avisos durante a coleta de dados.
* **main_entry.txt:** Este arquivo serve como um índice do conteúdo dos componentes coletados no bugreport.
* **version.txt:** Mostra a versão do formato de geração dos registros do bugreport.
* `fs/cache/recovery/`
    * **last_data_partition_info:** Esta informação fornece as características do armazenamento do dispositivo, o tamanho total, o tamanho do setor e o número de blocos presentes. Além disso, informa a capacidade de armazenamento utilizada e a disponibilidade.
    * **last_dataresizing:** Essas informações registram o início e a configuração de vários sensores do dispositivo. Também mostra mensagens de instâncias criadas para sensores específicos (como rotação automática, alerta inteligente, etc.).  
    * **last_postrecovery:** Essas informações descrevem atividades relacionadas à comunicação entre componentes de software seguros.  
* `fs/data/anr/`
    * **arn_yyyy-mm-dd-hh-mm-ss:** Fornece um diagnóstico detalhado de aplicativos que não respondem. ARN é originário de *App Not Responding*.
* `fs/data/log/bt/`
    * **btsnooz_hci.log:** Registro gerado por dispositivos Android que contém informações sobre a atividade da interface HCI (*Host Controller Interface*) do Bluetooth.
    * **btsnooz_hci.log.last:** Contém um registro mais detalhado e extenso do histórico de eventos da HCI Bluetooth.  
* `fs/misc/recovery`
    * **ro.buil.fingerprint:** O arquivo contém o identificador exclusivo da versão de software que está sendo executada no dispositivo.
    * **ro.build.fingerprint.1:** O arquivo contém uma variante do identificador de compilação no dispositivo.  
* `fs/data/tombstones/`
    * **tombstone_xx:** Esses arquivos são registros de falhas (*crash dumps*) que o sistema gera automaticamente quando um processo do usuário ou do sistema trava inesperadamente.
* `fs/proc/`
    * **mountinfo:** Este arquivo fornece informações detalhadas sobre os pontos de montagem em um sistema operacional baseado em Linux. Basicamente, ele permite entender como os sistemas de arquivos e as partições montadas estão configurados.  

**Por que isso é importante?**

Este arquivo compactado é uma fonte de informações muito valiosa para a análise forense, permitindo identificar o estado geral do dispositivo e acompanhar irregularidades ou falhas de software ou hardware que possam surgir em contextos de exploração de vulnerabilidades.

**Saiba mais**

* [Como capturar e ler relatórios de erros](https://developer.android.com/studio/debug/bug-report?hl=pt-br)

### logs/

As informações desta pasta são geradas pelo módulo [logs.go](https://github.com/mvt-project/androidqf/blob/main/modules/logs.go).

**Informações contidas**

Contém arquivos de registro coletados diretamente do dispositivo, usando o comando `adb pull` em várias pastas.

O módulo acessa rotas específicas do sistema para extrair arquivos que documentam o comportamento, erros e eventos do sistema operacional, que são:

* /data/anr/
* /data/log/
* /sdcard/log/

Os arquivos e pastas contidos neste diretório são os seguintes:

* `anr/anr_yyyy-mm-dd-hh-mm-ss`
    * **anr_yyyy-mm-dd-hh-mm-ss**: Arquivo que fornece um diagnóstico detalhado do estado do sistema e da atividade de um processo específico.
* `log/acore/0_dump_all.zip`
    * **0_dump_all.zip**: Arquivo que contém um dump do estado do sistema associado ao processo acore.  
* `log/batterystats/newbatterystats240905095247`
    * **newbatterystats240905095247**: Arquivo que contém métricas sobre o uso de energia do dispositivo.
* `log/dropbox.txt`
    * **dropbox.txt**: Arquivo que contém registros de eventos do sistema gerenciados pelo DropBoxManager.
* `log/dumpstate_debug_history.lst`
    * **dumpstate_debug_history.lst**: Arquivo que contém o histórico de execuções do processo de coleta de logs do sistema.
* `log/dumpstate_lastkmsg_20240423_152746_0_MP.log.gz`
    * **dumpstate_lastkmsg_20240423_152746_0_MP.log.gz**: Arquivo que contém a última mensagem do kernel após uma reinicialização inesperada.
* `log/dumpstate_latest_lastkmsg.log.gz`
    * **dumpstate_latest_lastkmsg.log.gz**: Arquivo que contém o log persistente mais recente do kernel após uma reinicialização.
* `log/dumpstate-stats.txt`
    * **dumpstate-stats.txt**: Arquivo que contém estatísticas geradas durante a coleta do estado do sistema.  
* `log/dumpstate_sys_error.zip`
    * **dumpstate_sys_error.zip**: Arquivo compactado que contém informações sobre erros críticos do sistema.
* `log/lom_log.txt`
    * **lom_log.txt**: Arquivo que contém registros relacionados ao armazenamento ou monitoramento do sistema.  
* `log/pm_debug_info.txt`
    * **pm_debug_info.txt**: Arquivo que contém informações de depuração do gerenciador de pacotes do sistema.
* `log/power_off_reset_reason.txt`
    * **power_off_reset_reason.txt**: Arquivo que indica a causa do último desligamento ou reinicialização do dispositivo.  
* `log/prev_dump.log`
    * **prev_dump.log**: Arquivo que contém uma captura anterior do estado do sistema antes de um evento crítico.
* `log/radio_PRECONFG_SET.log`
    * **radio_PRECONFG_SET.log**: Arquivo que documenta a configuração inicial do módulo de rádio do dispositivo.
* `log/shutdown_profile.1.txt`
    * **shutdown_profile.1.txt**: Arquivo que contém o perfil de desligamento registrado pelo sistema.  
* `log/shutdown_profile_latest.txt`
    * **shutdown_profile_latest.txt**: Arquivo que contém o perfil de desligamento mais recente do sistema.
* `log/err/`
    * **mobiledata_dns.dat**: Arquivo que contém erros relacionados à resolução DNS em redes móveis.  
    * **mobiledata_tp2.dat**: Arquivo que contém erros na transferência de pacotes móveis.  
    * **mobiledata_tp.dat**: Arquivo que contém erros na transferência de pacotes móveis.
* `log/ewlogd/ewlog0_20240920_144426188369.log`
    * **ewlog0_20240920_144426188369.log**: Arquivo que contém registros de eventos do sistema gerados pelo serviço ewlogd.
* `log/imscr/imscr.log.0`
    * **imscr.log.0**: Arquivo que contém registros do componente IMS para serviços de comunicação.
* `log/omc/`
    * **cidmanager.log**: Arquivo que contém informações do gerenciador de códigos de operadora (CID).
* **csc_update_log.txt**: Arquivo que contém o registro de atualizações do pacote de personalização CSC.  
    * **home_fota_update_log.txt**: Arquivo que contém registros de atualizações FOTA na rede doméstica.  
    * **prev_csc_log.txt**: Arquivo que contém um histórico anterior da configuração da operadora.
* `log/search/0_com.samsung.android.scs_index_encrypted.tar.gz`
    * **0_com.samsung.android.scs_index_encrypted.tar.gz**: Arquivo compactado criptografado que contém dados do índice de pesquisa do sistema.
* `log/sfslog/sfslog.0.gz`
    * **sfslog.0.gz**: Arquivo compactado que contém registros do sistema de arquivos seguros (Secure File System).  
* `log/smartswitch/1726696227738SmartSwitchSimpleLog.log`
    * **1726696227738SmartSwitchSimpleLog.log**: Arquivo que contém registros do processo de transferência de dados através do Smart Switch.  
* `log/update_engine_log/update_engine.20240603-222843`
    * **update_engine.20240603-222843**: Arquivo que contém registros do mecanismo de atualização de software do sistema.  
* `log/wfd/wfdDumpSource.log`
    * **wfdDumpSource.log**: Arquivo que contém a atividade registrada do componente Wifi direct (WFD).
* `log/wifi/`
* `system/proc/`
    * **kmsg**: Arquivo que contém o log atual do kernel com atividades do sistema em baixo nível.
    * **last_kmsg**: Arquivo que contém o último log persistente do kernel após uma reinicialização.
* `sys/fs/pstore/`

## Processos e Aplicações

### packages.json

As informações desta pasta são geradas pelo módulo [packages.go](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/adb/packages.py).

**Informações contidas**

Este arquivo está no formato *json* e contém a saída do comando `adb shell pm list packages` , que mostra uma lista de aplicativos instalados no dispositivo.

O arquivo contém:

* name: Nome do pacote do aplicativo.
* files: Caminho do arquivo APK correspondente com seus respectivos hashes e informações do certificado.
* installer: A partir de qual aplicativo foi instalado.
* uid: O PID associado em execução.
* disabled: Indica se o aplicativo está desativado.
* system: Indica se o pacote pertence ao sistema.
* third\_party: Indica se é um aplicativo de terceiros.

**Por que isso é importante?**

O conteúdo deste arquivo inclui informações que permitem identificar os aplicativos instalados e seu status no dispositivo. Isso ajuda os analistas a avaliar se existem aplicativos de risco ou maliciosos, quais permissões eles têm e quais podem comprometer a segurança.

**Estrutura do arquivo**

```
[
	{
    	"name": "com.whatsapp",
    	"files": [
        	{
            	"path": "/data/app/~~bqy7OQa_ZY_wDTFdG5YZRA==/com.whatsapp-3CExO11mXQz7SoP-3>
            	"local_name": "",
            	"md5": "a6014f075183b8872d115e04f546a19a",
            	"sha1": "7c52f9781c44c4902aecb4fc8a13584998e02376",
            	"sha256": "26721b2669943d57f9de57614a11077b7c3f3036396d48c3e54cbf0effd2268e",
            	"sha512": "21bea0ff94a748826041a1a8b3b9189090340086469ec62d31cf0d263c743fc2e>
            	"error": "",
            	"verified_certificate": true,
            	"certificate": {
                	"Md5": "556c6019249bbc0cab70495178d3a9d1",
                	"Sha1": "38a0f7d505fe18fec64fbf343ecaaaf310dbd799",
                	"Sha256": "3987d043d10aefaf5a8710b3671418fe57e0e19b653c9df82558feb5ffce5>
                	"ValidFrom": "2010-06-25T23:07:16Z",
                	"ValidTo": "2044-02-15T23:07:16Z",
                	"Issuer": "C=US, ST=California, L=Santa Clara, O=WhatsApp Inc., OU=Engin>
                	"Subject": "C=US, ST=California, L=Santa Clara, O=WhatsApp Inc., OU=Engi>
                	"SignatureAlgorithm": "DSA-SHA1",
                	"SerialNumber": 1277507236
            	},
            	"certificate_error": "",
            	"trusted_certificate": true
        	}
    	],
    	"installer": "com.facebook.system",
    	"uid": 10267,
    	"disabled": false,
    	"system": false,
    	"third_party": true
	}
]
```

### apks/ 

As informações desta pasta são geradas pelo módulo [packages.go](https://github.com/mvt-project/androidqf/blob/main/modules/packages.go).

**Informações contidas**

Este diretório armazena os arquivos APK (pacotes de aplicativos Android) extraídos do dispositivo. Estes são os arquivos de instalação dos aplicativos que estavam presentes no sistema no momento da análise.

**Por que isso é importante?**

A análise dos APKs permite examinar os aplicativos instalados no dispositivo, identificar possíveis amostras de malware ou aplicativos maliciosos, bem como validar as versões instaladas e suas assinaturas.

### processes.txt

As informações deste arquivo são geradas pelo módulo [processes.go](https://github.com/mvt-project/androidqf/blob/main/modules/processes.go).

**Informações contidas**

Este arquivo está no formato *json* e contém a saída do comando `adb shell ps -A` , que mostra informações detalhadas sobre os processos em execução.

Este arquivo apresenta as informações de forma estruturada, ordenadas por identificadores, detalhes da execução, consumo de recursos e status do processo.

**Por que isso é importante?**

Este arquivo permite identificar processos que são executados de maneira incomum ou que são executados por usuários não autorizados como resultado de uma escalada de privilégios. Da mesma forma, podemos garantir que os processos e suas hierarquias correspondam às configurações estabelecidas ou normais.

**Exemplo do conteúdo do arquivo**

```
[
	{
    	"pid": 1,
    	"uid": 0,
    	"ppid": 0,
    	"pgroup": 0,
    	"psid": 0,
    	"filename": "(init)",
    	"priority": 0,
    	"state": "S",
    	"user_time": 0,
    	"kernel_time": 0,
    	"path": "/system/bin/init",
    	"context": "u:r:init:s0",
    	"previous_context": "u:r:kernel:s0",
    	"command_line": ["/system/bin/init", "second_stage"],
    	"env": null,
    	"cwd": "/"
	},
	{
    	"pid": 2,
    	"uid": 0,
    	"ppid": 0,
    	"pgroup": 0,
    	"psid": 0,
    	"filename": "(kthreadd)",
    	"priority": 0,
    	"state": "S",
    	"user_time": 0,
    	"kernel_time": 0,
    	"path": "",
    	"context": "u:r:kernel:s0",
    	"previous_context": "u:r:kernel:s0",
    	"command_line": null,
    	"env": null,
    	"cwd": ""
	},
	{
    	"pid": 20430,
    	"uid": 0,
    	"ppid": 0,
    	"pgroup": 0,
    	"psid": 0,
    	"filename": "(com.whatsapp)",
    	"priority": 0,
    	"state": "",
    	"user_time": 0,
    	"kernel_time": 0,
    	"path": "",
    	"context": "u:r:untrusted_app:s0:c11,c257,c512,c768",
    	"previous_context": "u:r:init:s0",
    	"command_line": [
        	"com.whatsapp"
    	],
    	"env": null,
    	"cwd": ""
	},
]
```

**Saiba mais**

* [Visão geral dos processos e subprocessos](https://developer.android.com/guide/components/processes-and-threads?hl=es-419)

### services.txt 

As informações deste arquivo são geradas pelo módulo [services.go](https://github.com/mvt-project/androidqf/blob/main/modules/services.go)

**Informações contidas**

Este arquivo está no formato *txt* e contém a saída do comando `adb shell service list`, que mostra informações detalhadas sobre os serviços em execução.

A estrutura do arquivo é o nome do serviço e o processo ou pacote que está em execução para esse serviço.

**Por que isso é importante?**

Este arquivo permite identificar os serviços em execução ou, inversamente, identificar se um serviço não estava em execução. Isso é útil para identificar se todos os serviços necessários estão em execução para manter a integridade da segurança do dispositivo.

**Exemplo do conteúdo do arquivo**

```
Found 368 services:
0	AtlasService: [android.atlas.service]
1	DockObserver: []
9	accessibility: [android.view.accessibility.IAccessibilityManager]
10	account: [android.accounts.IAccountManager]
11	activity: [android.app.IActivityManager]
13	adb: [android.debug.IAdbManager]
16	alarm: [android.app.IAlarmManager]
26	android.hardware.power.IPower/default: [android.hardware.power.IPower]
27	android.hardware.power.stats.IPowerStats/default: []
43	anrmanager: [android.app.IAnrManager]
44	anti_root_dialog: [com.oplus.exsystemservice.antirootdialog.IAntiRootDialog]
50	appops: [com.android.internal.app.IAppOpsService]
56	audio: [android.media.IAudioService]
61	battery: []
63	batterystats: [com.android.internal.app.IBatteryStats]
68	bugreport: [android.os.IDumpstate]
70	cacheinfo: []
72	clipboard: [android.content.IClipboard]
78	connectivity: [android.net.IConnectivityManager]
84	cpuinfo: []
85	critical.log: []
89	dbinfo: []
130	input: [android.hardware.input.IInputManager]
133	installd: []
146	location: [android.location.ILocationManager]
149	logcat: [android.os.logcat.ILogcatManagerService]
169	meminfo: []
181	netstats: [android.net.INetworkStatsService]
191	notification: [android.app.INotificationManager]
234	package: [android.content.pm.IPackageManager]
238	permission: [android.os.IPermissionController]
240	permissionmgr: [android.permission.IPermissionManager
242	phone: [com.android.internal.telephony.ITelephony]
247	power: [android.os.IPowerManager]
248	power_hal_mgr_service: [com.mediatek.powerhalmgr.IPowerHalMgr]
249	power_monitor: [com.oplus.os.IOplusPowerMonitor]
250	powerstats: []
252	processinfo: [android.os.IProcessInfoService]
253	procstats: [com.android.internal.app.procstats.IProcessStats]
255	recovery: [android.os.IRecoverySystem]
273	sensorservice: [android.gui.SensorServer]
274	serial: [android.hardware.ISerialManager]
276	settings: []
298	system_server_dumper: []
299	system_update: [android.os.ISystemUpdateManager]
301	telecom: [com.android.internal.telecom.ITelecomService]
302	telephony.registry: [com.android.internal.telephony.ITelephonyRegistry]
314	tracing.proxy: [android.tracing.ITracingServiceProxy]
322	usb: [android.hardware.usb.IUsbManager]
323	user: [android.os.IUserManager]
354	virtualdevice: [android.companion.virtual.IVirtualDeviceManager]
355	vodata: [com.mediatek.ims.internal.IVoDataService]
357	vold: []
358	vpn_management: [android.net.IVpnManager]
363	wifi: [android.net.wifi.IWifiManager]
367	window: [android.view.IWindowManager]
```

**Saiba mais**

* [Como funcionam os serviços no Android?](https://developer.android.com/develop/background-work/services?hl=es-419)

### root\_binaries.json 

Este arquivo está no formato *json* e contém a saída do comando `adb shell which -a` aplicado a uma lista de binários para saber se eles estão presentes no sistema.

Os binários aos quais ele se aplica são usados para obter acesso root ou elevar privilégios no dispositivo.

A lista de binários e arquivos é:

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

Se nenhum desses arquivos estiver presente no dispositivo, o conteúdo do arquivo estará vazio.

**Por que isso é importante?**

Este arquivo detecta ferramentas de rooting, o que pode ser um indicativo de acessos não autorizados e escalonamento de privilégios que podem expor alguma vulnerabilidade.  Da mesma forma, permite ao analista identificar binários suspeitos que podem ter sido instalados sem o conhecimento do usuário e ajuda a determinar se o dispositivo foi manipulado.

**Exemplo do conteúdo do arquivo**

O arquivo vazio tem a seguinte estrutura:

```
[]
```

Quando o módulo identifica binários relacionados ao rooting nas rotas padrão do sistema no dispositivo, ele conterá uma lista dessas rotas para os binários detectados:

```
[
        "/system/xbin/su",
        "/system/bin/su",
        "/data/local/xbin/su",
        "/data/local/bin/busybox",
        "/sbin/su",
        "/su/bin/magisk",
        "/system/bin/.ext/.su",
        "/data/local/tmp/Superuser.apk",
        "/data/local/tmp/magiskhide"
]
```


## Informações dos arquivos no dispositivo

### backup.ab 

As informações deste arquivo são geradas pelo módulo [backup.go](https://github.com/mvt-project/androidqf/blob/main/modules/backup.go).
Este módulo foi projetado especificamente para fazer cópias de segurança dos dados armazenados em dispositivos móveis com Android.

**Informações contidas**

Este arquivo está no formato binário e contém dados relacionados com a cópia de segurança de aplicações e configurações do dispositivo. Os dados binários presentes neste arquivo estão compactados e incluem informações confidenciais do dispositivo.

Dependendo da opção selecionada no androidqf, o conteúdo do arquivo pode ser apenas os SMS ou pode ser uma cópia dos dados das aplicações que têm declarada no seu manifesto a possibilidade de realizar cópias.

Este arquivo compactado pode ser analisado pelo MVT através do comando `mvt-android check-backup backup.ab`

**Por que é importante?**

No caso de uma análise forense, este backup permite analisar os SMS em busca de links suspeitos ou maliciosos.


**Exemplo do conteúdo do arquivo**

```
(Binary data containing app backups and settings)
414e 4452 4f49 4420 4241 434b 5550 0a35
0a30 0a6e 6f6e 650a 6170 7073 2f63 6f6d
2e61 6e64 726f 6964 2e63 7473 2e63 7473
7368 696d 2f5f 6d61 6e69 6665 7374 0000
0000 0000 0000 0000 0000 0000 0000 0000
0000 0000 0000 0000 0000 0000 0000 0000
0000 0000 0000 0000 0000 0000 0000 0000
0000 0000 0000 0000 0000 0000 3030 3036
3030 2000 3031 3735 3000 0000 3031 3735
3000 0000 3030 3030 3030 3034 3537 3600
3000 0000 0000 0000 0000 0000 3031 3430
3134 0020 3000 0000 0000 0000 0000 0000
```

**Saiba mais**

* [Extração de arquivos de backup | Android Backup Extractor](https://github.com/nelenkov/android-backup-extractor)
* [Análise de arquivos de backup no Android](https://digitalforensicforest.com/2016/01/28/android-backup-file-ab-analysis/)
* [Verificar um backup do Android (mensagens SMS) - Mobile Verification Toolkit](https://docs.mvt.re/en/latest/android/backup/) 

### files.json 

As informações deste arquivo são geradas pelo módulo [files.go](https://github.com/mvt-project/androidqf/blob/main/modules/files.go)

**Informações contidas**

Este arquivo está no formato *json* e contém o resultado da pesquisa de arquivos usando o comando *find.*

O comando completo *find* é `adb shell find ‘/’ -maxdepth 1 -printf ‘%T@ %m %s %u %g %p\n’ 2\> /dev/null` e é aplicado às seguintes pastas:

* /sdcard/
* /system/
* /system\_ext/
* /vendor/
* /cust/
* /product/
* /apex/
* /data/local/tmp/
* /data/media/0/
* /data/misc/radio/
* /data/vendor/secradio/
* /data/log/
* /tmp/
* /data/data/

Cada arquivo inclui metadados como: o caminho completo do arquivo, tamanho, marca de tempo (indica a última modificação do arquivo e o último acesso ao arquivo), permissões do arquivo, identificador do proprietário, mensagens de erro e hashes sha1, sha256, sha512, md5, se estiverem pré-calculados.

**Por que isso é importante?**

Este arquivo é relevante para identificar arquivos de interesse em uma investigação forense, incluindo arquivos potencialmente usados por invasores para comprometer um dispositivo e fazer as análises oportunas que permitam rastrear atividades maliciosas.

**Exemplo do conteúdo do arquivo**

```
{
"path": "/sdcard/Android/.Trash/com.sec.android.app.myfiles/.nomedia",
    	"size": 62,
    	"mode": "-rw-rw----",
    	"user_id": 10276,
    	"user_name": "",
    	"group_id": 1023,
    	"group_name": "",
    	"changed_time": 1722868692,
    	"modified_time": 1722868692,
    	"access_time": 1714937715,
    	"error": "",
    	"context": "u:object_r:fuse:s0",
    	"sha1": "",
    	"sha256": "",
    	"sha512": "",
    	"md5": ""
}
```


## Comentários

Tem comentários ou sugestões sobre este recurso? Você pode usar a função de comentários mostrada abaixo para deixar suas ideias ou observações. Por favor, certifique-se de seguir nosso [código de conduta](../../community/code-of-conduct). A função de comentários leva diretamente à seção de [Discussions do Github](https://github.com/Socialtic/forensics/discussions), onde você também pode participar das discussões de forma direta.


