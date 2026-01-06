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

translation-review-pending: true
---

# Dicionário de arquivos gerados pela ferramenta MVT-androidqf

Este documento contém informações sobre os arquivos gerados pelo MVT por meio do componente [mvt-check-androidqf.](https://github.com/mvt-project/mvt/tree/main/src/mvt/android/modules/androidqf). O objetivo desse dicionário é facilitar ao analista a busca por informações específicas e conhecer o formato em que as informações da análise forense são apresentadas.

Esse recurso é **parte de um repositório de documentação técnica** que visa estabelecer uma base de conhecimento testada, flexível e acessível para **promover a análise forense consensual em benefício da sociedade civil**. A [estrutura de documentação técnica Diataxis] (https://diataxis.fr/) é usada para organizar o conteúdo.

Esse recurso específico se enquadra na categoria de [referências] (https://diataxis.fr/reference) e contém informações sobre a análise da saída de aquisição gerada por dispositivos Android usando o comando ***mvt-android check-andoridqf*** durante o uso do MVT (*Mobile Verification Toolkit)*, desenvolvido e mantido pelo [Amnesty International Security Lab] (https://securitylab.amnesty.org/es/) e pertencente ao [MVT Project] (https://github.com/mvt-project/). Isso serve para que um analista **saiba quais arquivos são gerados, como usá-los, onde procurar informações específicas e em que formato encontrá-las.

MVT significa *Mobile Verification Toolkit* (Kit de ferramentas de verificação móvel). Trata-se de uma ferramenta desenvolvida, lançada e mantida pelo [Amnesty International Security Lab] (https://securitylab.amnesty.org/es/) como parte do [MVT Project] (https://github.com/mvt-project/).  A intenção desse kit de ferramentas é, em essência, facilitar a análise forense consensual de dispositivos Android e iOS com o objetivo de identificar traços de comprometimento.

Esse recurso foi atualizado pela última vez em 18 de novembro de 2025 e foi baseado no [*commit 339a1d0712c4cc051e880b8a777d2b8b6295e57b*](https://github.com/mvt-project/mvt/commit/339a1d0712c4cc051e880b8a777d2b8b6295e57b) para a coleta das informações.

As informações geradas pelo *mvt-androidqf* podem ser agrupadas em cinco categorias principais:

* Detalhes da aquisição
* Configuração do dispositivo
* Informações de registro e eventos do sistema
* Processos e aplicativos
* Arquivos de backup

Cada uma das categorias, por sua vez, contém arquivos específicos gerados pela ferramenta, que estão listados no **índice de conteúdo** abaixo:

- [Acquisition-details](#acquisition-details)
    - info.json](#info.json)
    - command.log](#command.log)
    - [timeline.csv](#timeline.csv)
- [device-configuration](#device-configuration)
    - [aqf_getprop.json](#aqf_getprop.json)
    - [aqf_settings.json](#aqf_settings.json)
    - mounts.json](#mounts.json)
- Processos e aplicativos](#processos-e-aplicativos)
    - [aqf_packages.json](#aqf_packages.json)
    - root_binaries.py](#root_binaries.py)
- backed-up_files](#backed-up_files)
    - [aqf_files.json](#aqf_files.json)

Durante a execução do comando ***mvt-android check-andoridqf***, o MVT também executa os módulos correspondentes a ***mvt-android check-bugreport*** e ***mvt-android check-backup***, desde que haja um arquivo bugreport.zip e um arquivo backup.ab dentro da pasta de entrada de uma extração androidqf.

No material de referência suplementar [sobre os arquivos gerados pela ferramenta mvt ao analisar um relatório de bug] (../02-reference-mvt-bugreport-dictionary/index.md), a saída do comando check-bugreport e os arquivos resultantes são descritos. A seguir, as **referências específicas de módulo para os módulos executados pelo comando check-androidqf para analisar o relatório de bug:**.

- device-configuration](../02-reference-mvt-bugreport-dictionary/index.md#device-configuration-device-configuration-device-configuration)
    - dumpsys_get_prop.json](../02-reference-mvt-bugreport-dictionary/index.md#getprop.json)
- dumpsys_get_prop.json](../02-reference-mvt-bugreport-dictionary/index.md#information-about-logs-and-system-events)
    - dumpsys_adb_state.json](../02-reference-mvt-bugreport-dictionary/index.md#dumpsys_adb_state.json)
    - bugreport_timestamps.json](../02-reference-mvt-bugreport-dictionary/index.md#bugreport_timestamps.json)
    - dbinfo.json](../02-reference-mvt-bugreport-dictionary/index.md#dbinfo.json)
    - dumpsys_receivers.json](../02-reference-mvt-bugreport-dictionary/index.md#receivers.json)
- processes-and-applications](../02-reference-mvt-bugreport-dictionary/index.md#processes-and-applications)
    - dumpsys_packages.json](../02-reference-mvt-bugreport-dictionary/index.md#packages.json)
    - dumpsys_activities.json](../02-reference-mvt-bugreport-dictionary/index.md#activities.json)
    - dumpsys_appops.json](../02-reference-mvt-bugreport-dictionary/index.md#appops.json)
    - dumpsys_accessibility.json](../02-reference-mvt-bugreport-dictionary/index.md#accessibility.json)
    - tombstones.json](../02-reference-mvt-bugreport-dictionary/index.md#tombstones.json)
    - dumpsys_battery_daily.json](../02-reference-mvt-bugreport-dictionary/index.md#battery_daily.json)
    - dumpsys_battery_history.json](../02-reference-mvt-bugreport-dictionary/index.md#battery_history.json)
    - [dumpsys_platform_compact.json](../02-reference-mvt-bugreport-dictionary/index.md#platform_compact.json)


Da mesma forma, também listamos os módulos executados pelo ***check-backup***, que estão detalhados no final deste recurso.  

- Informações sobre logs e eventos do sistema](#system-logs-and-events-information)
- sms.json](#sms.json)

##procurement-details {#procurement-details}(#sms.json)(#sms.json)

### info.json {#info.json}

**Informações contidas**

Esse arquivo está no formato *json* e contém informações relacionadas à análise realizada em uma extração concluída usando o AndroidQF. Ele contém as seguintes informações:

* Caminho do arquivo analisado.  
* Versão do MVT usada.  
* Data da análise.  
* Lista de arquivos de indicadores de compromisso.  
* Hash da pasta de saída analisada (SHA-256).

**Por que isso é importante?

Esse arquivo nos permite **validar a análise que foi realizada**, documentando que temos um registro do processo de aquisição e dos indicadores que foram considerados para fazer a comparação.

Essas informações nos permitem estabelecer uma referência do arquivo analisado e das ferramentas de indicadores usadas na análise, o que facilita o [processo de custódia de extração forense] (https://forensics.socialtic.org/explainers/01-explainer-introduccion-forense-digital/01-explainer-introduccion-forense-digital.html#cadena-de-custodia).

Estrutura do arquivo:** ** Estrutura do arquivo:** Estrutura do arquivo:** Estrutura do arquivo:** Estrutura do arquivo:** Estrutura do arquivo:** Estrutura do arquivo:** Estrutura do arquivo

```
{
	"target_path": "/path/file/path/acquisition-with-androidqf",
	"mvt_version": "2.6.1",
	"date": "YYYYY-MM-DD hh:mm:ss",
	"ioc_files": [
    	"/caminho/para/indicadores/pegasus.stix2",
    	"/path/to/indicators/predator.stix2",
    	"/path/to/indicators/rcs_lab.stix2",
    	"... mais indicadores usados ..."
	],
	"hashes": [
    	{
        	"file_path": "/path/from/file/acquisition-with-androidqf",
        	"sha256": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    	}
	]
}
```

### command.log {#command.log}

**informação contida** **informação contida** **informação contida** **informação contida** **informação contida** **informação contida

Esse arquivo está em texto simples com uma extensão *.log* e contém registros detalhados da execução do comando *mvt-android check-androidqf*.

Seu conteúdo lista a análise realizada em uma pasta de saída de uma extração de dados forenses realizada com o AndroidQF, incluindo a detecção de indicadores de comprometimento para identificar alertas de segurança relacionados a malware.

Os registros do arquivo são apresentados de forma estruturada com:

* Carimbos de data e hora
* Nomes de módulos em execução
* Tipo de mensagem (*INFO*, *DEBUG*, WARNING, *ERROR*)
* Ação do módulo correspondente (análise de arquivo, carregamento de IoCs, comparação e resultado da comparação).

Os tipos de mensagem correspondem ao seguinte:

*INFO*. As mensagens também são exibidas na tela durante a execução.  
*DEBUG*. Informações não exibidas na tela, mas associadas a uma ação executada durante a análise, por exemplo, o carregamento de um IoC ou a revisão de um hash.  
* WARNING* Corresponde a alertas de atividade ou informações suspeitas que um analista deve verificar.  
* ERRO: mensagens de erro sobre alguma ação realizada durante a análise, por exemplo, ao carregar um arquivo corrompido ou um problema com a execução do código correspondente.

**Por que isso é importante?

Permite gerar um registro das ações realizadas durante a análise. Por meio desse registro, é possível verificar o seguinte:

* Que a análise foi realizada corretamente
* Se houve coincidências com IoCs.
* Se foram identificadas informações ou atividades suspeitas.

Estrutura do arquivo:** ** Estrutura do arquivo:** Estrutura do arquivo:** Estrutura do arquivo:** Estrutura do arquivo:** Estrutura do arquivo:** Estrutura do arquivo:** Estrutura do arquivo

Este arquivo segue um formato de linha por linha com a seguinte estrutura.

```
TIMESTAMP] - [MODULE] - [LOG LEVEL] - [MESSAGE] - [MESSAGE] - [MESSAGE] - [MESSAGE] - [MESSAGE] - [MESSAGE] - [MESSAGE] - [MESSAGE] - [MESSAGE] - [MESSAGE] - [MESSAGE].
...
2025-01-17 17:06:14,035 - mvt.android.cmd_check_androidqf - INFO - Analisando o arquivo de indicadores STIX2 no caminho /home/user/.local/share/mvt/indicators/raw.githubusercontent.com_AmnestyTech_investigations_master_2021-07-18_nso_pegasus.stix2
2025-01-17 17:06:14,098 - mvt.android.cmd_check_androidqf - DEBUG - Extraiu 1549 indicadores para a coleção com o nome "Pegasus"
2025-01-17 17:06:14,812 - mvt.android.cmd_check_androidqf - DEBUG - Extraiu 245 indicadores para a coleção com o nome "mSpy"
```

**Saiba mais**

* [Introdução ao STIX](https://oasis-open.github.io/cti-documentation/stix/intro.html)

### timeline.csv {#timeline.csv}

**Informações contidas** **Informações contidas** **Informações contidas** **Informações contidas** **Informações contidas** **Informações contidas
Esse arquivo está no formato *csv* e armazena uma linha do tempo da atividade do dispositivo. Essa atividade é obtida a partir da execução dos módulos de análise do MVT e é classificada por tempo.

Cada linha do *csv* corresponde a:

* Timestamp (carimbo de data/hora local do dispositivo).  
* Módulo executado (Plugin).  
* Atividade identificada no dispositivo (Event).
* Descrição da atividade identificada no dispositivo (Description).

**Por que isso é importante?

Esse arquivo permite rastrear a atividade interna do dispositivo, podendo gerar uma ideia geral de como o dispositivo se comportou e identificar eventos relevantes.

**Estrutura do arquivo

Esse arquivo segue um formato de linha por linha com a seguinte estrutura.

```
UTC Timestamp", "Plugin", "Event", "Description", "2025-01-01 00:00:00", "Packages", "package_first_install", "Description"
"2025-01-01 00:00:00", "Packages", "package_first_install", "com.example.app (system: False, third party: True)"
"2025-01-01 00:00:00", "Packages", "package_last_update", "com.system.module (sistema: Verdadeiro, terceiros: Falso)"
"2025-01-01 00:00:00", "Packages", "package_install", "com.example.newapp (sistema: Falso, terceiros: Verdadeiro)"
```

## device-configuration {#device-configuration}

### aqf\_getprop.json {#aqf_getprop.json}

As informações nesse arquivo são geradas pelo módulo [aqf\_getprop](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/androidqf/aqf_getprop.py) e pelo artefato [getprop](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/artifacts/getprop.py).

**Informações contidas

Esse arquivo está no formato *json* e contém uma lista de propriedades do dispositivo que são extraídas do arquivo *getprop.tx*t gerado durante uma extração com o AndoridQF.

Essas propriedades do sistema são pares de chave-valor de cadeias de caracteres armazenadas no dicionário global [*build.prop*] (https://xdaforums.com/t/guide-build-prop-wiki.2056266/) ou em arquivos de descrição *.sysprop* e fornecem uma maneira conveniente de compartilhar configurações dentro do sistema.

As informações podem ser encontradas usando o seguinte formato:

```
[{prefix}.]{group}[.{subgroup}]*.{name}[.{type}]
```

Algumas propriedades são prefixadas com *ro*, indicando que são propriedades somente leitura ou que foram atribuídas após a reinicialização do dispositivo. As propriedades prefixadas com *persist* referem-se a configurações resistentes à reinicialização. Algumas propriedades não devem ter prefixo, portanto, começam diretamente com o grupo ao qual pertencem.

Os grupos mais comuns são:

*bluetooth*, relacionado ao Bluetooth.
*boot*, sysprops de linha de comando do kernel
*build*, sysprops que identificam uma compilação
*telefonia*, relacionado à telefonia
*audio*, relacionado a áudio
*graphics*, relacionado a gráficos
*vold*, relacionado ao vold, que gerencia a montagem de volumes físicos de armazenamento externo

Para obter mais detalhes, consulte a [lista de propriedades já definidas no código-fonte do Android] (https://android.googlesource.com/platform/system/sepolicy/+/refs/heads/main/private/property_contexts).

**Por que isso é importante?

As propriedades fornecem informações importantes sobre o hardware e o software do dispositivo, que podem ser alteradas por software mal-intencionado para ocultar sua presença ou para modificar inadvertidamente o comportamento do dispositivo.

Estrutura do arquivo:** ** Estrutura do arquivo:** Estrutura do arquivo:** Estrutura do arquivo:** Estrutura do arquivo:** Estrutura do arquivo:** Estrutura do arquivo:** Estrutura do arquivo

```
[
	{
    	"nome": "aaudio.hw_burst_min_usec",
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

As informações nesse arquivo são geradas pelo módulo [aqf\_settings](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/androidqf/aqf_settings.py) e pelo artefato [settings](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/artifacts/settings.py).

**Informações contidas

Esse arquivo está no formato *json* e contém informações sobre o status das configurações do dispositivo nos *namespaces* *system* (interface do usuário e comportamento geral, como brilho, matiz, rotação etc.), *secure* (configurações confidenciais que exigem permissões elevadas, como verificação de aplicativos, configurações de acessibilidade ou status do ADB) e *global* (parâmetros compartilhados entre usuários, como redes, localização, roaming, volumes globais etc.).

As informações são apresentadas em três blocos, primeiro Configurações do sistema, depois Configurações seguras e, por fim, Configurações globais. Cada configuração é apresentada como um par de valores-chave na estrutura:

````json
{setting}:{level}]
```

Os valores que têm cada configuração têm significados diferentes dependendo dessa configuração, mas geralmente são os seguintes:

* **0**geralmente significa desativado ou desligado.  
** **1** geralmente significa ativado ou ligado.  
* Números maiores** podem ser níveis, como o brilho da tela, por exemplo.  
* Alguns valores são **paths** ou caminhos do sistema que apontam para recursos.

Essas informações são extraídas diretamente dos arquivos settings\_global.txt, settings\_secure.txt e settings\_system.txt gerados durante uma extração com o AndoridQF.

**Por que isso é importante?

Permite identificar configurações anômalas que podem comprometer a segurança, a privacidade ou a funcionalidade do dispositivo. Configurações padrão incomuns podem sinalizar tentativas intencionais ou acidentais de modificar o comportamento do sistema.

Estrutura do arquivo:** ** Estrutura do arquivo:** Estrutura do arquivo:** Estrutura do arquivo:** Estrutura do arquivo:** Estrutura do arquivo:** Estrutura do arquivo:** Estrutura do arquivo

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
    	"accessibility_button_target_component": "accessibility_change_magnification_size": "3",
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
    	"contacts_move_simcontacts_not_now": "0",
    	"phenotype_boot_count": "131",
    	"phenotype_flags": "_boot_Phenotype_flags": "",
    	"activity_starts_starts_logging_enabled": "1",
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

**Saiba mais**

* [Lista completa de preferências do sistema](https://developer.android.com/reference/android/provider/Settings.System?hl=es-419)
* [Lista completa de preferências do sistema - Configurações seguras](https://developer.android.com/reference/android/provider/Settings.Secure?hl=es-419)
* [Lista completa de preferências do sistema \- Configurações globais](https://developer.android.com/reference/android/provider/Settings.Global?hl=es-419)

### mounts.json {#mounts.json}

As informações contidas nesse arquivo são geradas pelo módulo [mounts](https://github.com/mvt-project/androidqf/blob/main/modules/mounts.go) e pelo artefato [mounts](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/artifacts/mounts.py).

**Informações contidas

Este arquivo está no formato *json* e contém informações sobre as partições e os diretórios dos sistemas de arquivos montados em um dispositivo no espaço do usuário *e* no kernel do Linux Android extraído do arquivo *mounts.json* gerado durante uma extração com o AndoridQF.

O módulo se encarrega de identificar configurações suspeitas nos pontos de montagem /system, /vendor, /product e /system\_ext, como modo de acesso de leitura e gravação, carimbos de data e hora noatime ou nodiratime e, em seguida, se encarrega de formatar cada ponto de montagem da seguinte forma:

**device**: partição ou volume montado, no android os mais comuns são:
    * Partições de armazenamento físico
        /dev/block/sdX: dispositivo de armazenamento físico ([eMMC/UFS](https://new.c.mi.com/es/post/11738)) exposto como sd pelo kernel.
        /dev/block/mmcblk: dispositivo de armazenamento eMMC exposto como mmcblk.
        /dev/block/dm-X: dispositivo gerenciado pelo device-mapper (partições criptografadas, verity ou lógicas).
        /dev/block/by-name/: links simbólicos que apontam para partições reais por nome, por exemplo, sistema, fornecedor, userdata.
    * Volume virtual do kernel na RAM
        * proc: interface virtual para obter informações sobre o kernel e o processo.
        * sysfs: expõe informações sobre dispositivos, drivers e parâmetros do kernel.
        * selinuxfs: exibe políticas, estados e rótulos do SELinux.
        * tracefs: sistema virtual para ferramentas de rastreamento e depuração do kernel.
        * pstore: armazena registros persistentes de falhas do kernel.
        * bpf: expõe interfaces para programas [eBPF] (https://source.android.com/docs/core/architecture/kernel/bpf) carregados no kernel.
    * Espaço do usuário
        /dev/fuse: interface [FUSE](https://source.android.com/docs/core/storage/fuse-passthrough) usada pelo Android para montar o armazenamento.emulated p.j /storage/emulated.
    * Interfaces de controle interno do kernel
        * Nenhum: Identificador que indica que a montagem não vem de um dispositivo real.
        * binder: o [sistema IPC] interno do Android (https://source.android.com/docs/core/architecture/ipc/binder-overview) para comunicação entre processos.
    * Arquivos APEX montados como loopback
        /dev/block/loopX: dispositivos de loop usados para montar pacotes APEX como se fossem partições reais.

* Ponto de montagem**: caminho para a pasta raiz do armazenamento em que as informações são acessadas; no Android, geralmente são os seguintes:
    /system: contém o sistema operacional principal.
    /vendor: inclui componentes e drivers fornecidos pelo fabricante do hardware, como HALs, firmware e binários específicos do fornecedor.
    * product: armazena as personalizações do fabricante das funções do sistema e dos aplicativos específicos do dispositivo.
    /data: área para dados do usuário e armazenamento de aplicativos.
    /cache: espaço temporário usado para arquivos de atualização e dados transitórios do sistema.
    /metadata: contém informações críticas necessárias para [AVB](https://source.android.com/docs/security/features/verifiedboot/avb), criptografia e validações do sistema.
    /mnt/media_rw/: ponto de montagem para armazenamento removível ou adotado, por exemplo, cartão SD. Cartão SD.
    /storage/emulated: visualização emulada do armazenamento interno do usuário.
    /proc: sistema virtual que expõe o kernel e as informações do processo (não o armazenamento real).
    /sys: Sistema virtual que expõe informações sobre o dispositivo e o driver do kernel.
    /mnt/user/0/emulated: exibição específica do armazenamento emulado para o usuário 0.

** **filesystem_type**: tipo de sistema de arquivos, no android são os seguintes:
    * ext4: sistema de arquivos Linux usado em partições internas.
    * f2fs: sistema de arquivos otimizado para armazenamento flash.
    * erofs: sistema de arquivos otimizado somente para leitura.
    * vfat: sistema de arquivos FAT32 usado para cartões SD e armazenamento externo.
    * sdfat: implementação estendida do FAT/exFAT.
    * tmpfs: sistema de arquivos RAM temporário usado para diretórios voláteis, por exemplo, /dev, /run, /apex.
    * proc: sistema de arquivos virtual que expõe informações do kernel e do processo.
    * sysfs: sistema virtual que exibe informações de hardware, driver e driver do kernel.
    * selinuxfs: sistema virtual que expõe os parâmetros e o status do SELinux no dispositivo.
    * functionfs: sistema usado para interfaces [USB gadget] (https://source.android.com/docs/core/permissions/usb-hal) quando o Android atua como um dispositivo USB.
    * incremental-fs: sistema projetado para instalar ou executar aplicativos "sob demanda" enquanto eles ainda estão sendo baixados.
    * binder: sistema de comunicação IPC interno do Android.
    * cgroup: sistema virtual baseado em grupos de controle para gerenciar recursos por processo, por exemplo, CPU, memória. CPU, memória.
    * fuse: sistema de arquivos do espaço do usuário usado para armazenamento emulado.

* **mount_options**
    * Modos de acesso
        * ro: somente leitura
        * rw: leitura e gravação
    * Etiquetas de segurança
        * seclabel: ativa e aplica rótulos do SELinux ao sistema de arquivos.
        * nodev: impede que arquivos de dispositivos sejam usados nessa partição.
        * nosuid: bloqueia binários com [set-UID/set-GID] (https://www.cbtnuggets.com/blog/technology/system-admin/linux-file-permissions-understanding-setuid-setgid-and-the-sticky-bit) para evitar escalonamento.
        * noexec: impede a execução de arquivos dessa partição.
        * hidepid=invisible: oculta processos de outros usuários em * /proc *.
        * user_xattr: permite atributos estendidos definidos pelo usuário.
        * acl: permite listas de controle de acesso mais detalhadas do que *rwx*.
        * inlinecrypt: Usa a criptografia em linha compatível com o hardware/FS (Android).
        * usrquota: habilita cotas por usuário.
        * grpquota: habilita cotas por grupo.
    * Carimbos de data/hora
        * lazytime: adia a gravação de registros de data e hora no armazenamento para melhorar o desempenho.
        * relatime: atualiza os tempos de acesso somente se necessário.
        * noatitime: desativa a atualização do tempo de acesso.
    * Usuários ou grupos relacionados
        * uid=0: proprietário da montagem (raiz).
        * gid=1000: grupo base do Android (system ou media_rw).
        * user_id=0: usuário primário do sistema Android.
        * group_id=0: grupo primário do usuário root.

** **is_system_partition**: valor booleano que indica se a partição é /system ou /sys.
**is_read_write**: valor booleano que indica se a partição tem acesso de leitura e gravação.


**Por que isso é importante?

Os pontos de montagem permitem identificar as **áreas de armazenamento montadas no dispositivo**, sua origem e como estão configuradas. Com essas informaçõesn pode saber as permissões com as quais as partições foram montadas, os usuários associados e, em alguns casos, os rótulos de segurança SELinux aplicados. Isso é útil para **identificar montagens que possam ser suspeitas** de atividade mal-intencionada no dispositivo; por exemplo, uma partição do sistema, como as partições /system, /vendor, /product, cuja montagem geralmente é somente de leitura, é montada com permissões de gravação ou sem rótulos de segurança, ou uma partição como /data é montada com permissões de leitura em subpastas que contêm informações de aplicativos, o que pode indicar montagens fraudulentas não autorizadas, evidenciando um comportamento altamente suspeito.

Exemplo de conteúdo de arquivo** **Exemplo de conteúdo de arquivo** **Exemplo de conteúdo de arquivo** **Exemplo de conteúdo de arquivo

```
{
        "dispositivo":"/dev/block/mmcblk0p63",
        "mount_point": "/",
        "filesystem_type": "ext4",
        "mount_options": "ro,seclabel,relatime,discard",
        "options_list": [
            "ro",
            "seclabel",
            "relatime",
            "discard"
        ],
        "is_system_partition": falso,
        "is_read_write": false
    }
  {
        "device" (dispositivo): "tmpfs",
        "mount_point": "/dev",
        "filesystem_type": "tmpfs",
        "mount_options": "rw,seclabel,nosuid,relatime,size=1812632k,nr_inodes=453158,mode=755",
        "options_list": [
            }, "rw",
            "seclabel",
            "nosuid",
            "relatime",
            "size=1812632k",
            "nr_inodes=453158",
            "mode=755"
        ],
        "is_system_partition": falso,
        "is_read_write": true
    },
    {
        "device" (dispositivo): "devpts",
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
        "is_system_partition": falso,
        "is_read_write": true
    },
```

**Para saber mais:**

* [Visão geral do particionamento do Android](https://source.android.com/docs/core/architecture/partitions?hl=es-419)
* [Histórico e terminologia do particionamento dinâmico](https://source-android-com.translate.goog/docs/core/ota/virtual_ab?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=sge#background)
* Sistema de arquivos do Android](https://medium.com/@aditi.kale20/file-system-of-android-a89dcbb693f1)
* Compatibilidade do sistema de arquivos do kernel do Android](https://source-android-com.translate.goog/docs/core/architecture/android-kernel-file-system-support?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc)
* Compatibilidade com o SELinux](https://source.android.com/docs/security/features/selinux/compatibility)
* [Formato de arquivo APEX](https://source.android.com/docs/core/ota/apex)
* [Sistema de arquivos do Android](https://keepcoding.io/blog/sistema-de-ficheros-android/)

## Processos e aplicativos {#processos-e-aplicativos}

### aqf_packages.json {#aqf_packages.json}

As informações contidas nesse arquivo são geradas pelo módulo [aqf_packages] (https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/androidqf/aqf_packages.py).

**Informações contidas**.

Esse arquivo está no formato *json* e contém informações sobre os aplicativos instalados no dispositivo. Essas informações são extraídas do arquivo *packages.json* gerado durante a aquisição do AndroidQF.

As informações contidas nesse arquivo são apresentadas da seguinte forma:

**name**: Nome do pacote de aplicativos.  
**files**: Caminho do arquivo APK correspondente com seus respectivos hashes e informações de certificado.  
**installer**: a partir do qual o aplicativo foi instalado.  
** **uid**: O PID de execução associado.  
**disabled**: Indica se o aplicativo está desativado.  
** **system**: Indica se o pacote pertence ao sistema.  
**third party**: Indica se é um aplicativo de terceiros.

**Por que isso é importante?
O conteúdo desse arquivo inclui informações para identificar os aplicativos instalados e seu status no dispositivo. Isso ajuda os analistas a avaliar se existem aplicativos arriscados ou mal-intencionados, quais permissões eles têm e quais podem comprometer a segurança.

Estrutura do arquivo:** ** Estrutura do arquivo:** Estrutura do arquivo:** Estrutura do arquivo:** Estrutura do arquivo:** Estrutura do arquivo:** Estrutura do arquivo:** Estrutura do arquivo

```
{
        "nome": "com.samsung.android.arzone",
        "arquivos": [
            {
                "path": "/data/app/ARZone/ARZone.apk",
                "local_name": "",
                "md5": "947b59f40de694e2359c007abe0c0191",
                "sha1": "508d9207ca6218bf599171c13f8141c37e97f580",
                "sha256": "76f972c04be51d0cad7980df85f76219eebfc0f770001e8ef02b4fa9a180f9d4",
                "sha512": "3b34c13fb1150df1b347f0cc0913f55d17abe2be96354a64e2ed8369fdce5b2fb10c5748deb7a66409153b766d84039fa01b0a1ced1bf2ccb62ab5368b38599a",
                "erro": "",
                "verified_certificate": true,
                "certificate": {
                    "Md5": "d087e72912fba064cafa78dc34aea839",
                    "Sha1": "9ca5170f381919dfe0446fcdab18b19a143b3163",
                    "Sha256": "34df0e7a9f1cf1892e45c056b4973cd81ccf148a4050d11aea4ac5a65f900a42",
                    "ValidFrom": "2011-06-22T12:25:12Z",
                    "ValidTo": "2038-11-07T12:25:12Z",
                    "Emissor": "C=KR, ST=Coreia do Sul, L=Cidade de Suwon, O=Samsung Corporation, OU=DMC, CN=Samsung Cert",
                    "Subject": "C=KR, ST=Coreia do Sul, L=Cidade de Suwon, O=Samsung Corporation, OU=DMC, CN=Samsung Cert",
                    "SignatureAlgorithm": "SHA1-RSA",
                    "SerialNumber": 15134792569865480918
                },
                "certificate_error": "",
                "trusted_certificate": true
            }
        ],
        "installer" (instalador): "null" (nulo),
        "uid": 10295,
        "disabled": falso,
        "system": falso,
        "third_party": true
    }
```

### root_binaries.py {#root_binaries.py}

As informações contidas nesse arquivo são geradas pelo módulo [root_binaries](https://github.com/mvt-project/androidqf/blob/main/modules/root_binaries.go).

**Informações contidas**.

Esse arquivo está no formato *json* e contém uma lista de binários relacionados ao enraizamento no dispositivo, extraídos do arquivo r*oot_binaries.json* gerado durante uma extração com o AndoridQF.

Esse módulo é responsável por extrair os binários do arquivo de base para poder identificar os binários suspeitos de fazer o root e seus rastros. O formato aplicado é o seguinte:

* Caminho: Caminho para o binário de enraizamento encontrado.  
* binary\_name: Nome do binário, que pode ser o seguinte:  
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
* Descrição: Descrição do binário de root, que pode ser o seguinte:  
    * su: Binário do SuperUser
    * busybox: utilitários do BusyBox
    * supersu: gerenciamento de raiz do SuperSU
    * Superuser.apk: aplicativo Superuser
    * KingoUser.apk: aplicativo KingRoot
    * SuperSu.apk: aplicativo SuperSU
    * magisk: estrutura de raiz do Magisk
    * magiskhide: utilitário de ocultação do Magisk
    * magiskinit: binário de inicialização do Magisk
    * magiskpolicy: binário de política do Magisk

**Por que isso é importante?

Esse arquivo detecta ferramentas de root, o que pode ser uma indicação de acesso não autorizado e escalonamento de privilégios que pode expor uma vulnerabilidade.  Ele também permite que o analista identifique binários suspeitos que podem ter sido instalados sem o conhecimento do usuário e ajuda a determinar se o dispositivo foi adulterado.

**Exemplo de conteúdo de arquivo

```
    {
        "caminho": "/sistema/xbin/su",
        "binary_name": "su",
        "description": "SuperUser binary" (binário do superusuário)
    },
    {
        "path" (caminho): "/system/bin/su",
        "binary_name": "su",
        "description": "SuperUser binary" (binário do superusuário)
    },
    {
        "path": "/system/bin/busybox",
        "binary_name": "busybox",
        "description": "Utilitários do BusyBox"
    },
    {
        "path": "/data/local/tmp/magisk",
        "binary_name": "magisk",
        "description": "Magisk root framework" (Estrutura raiz do Magisk)
    }
```

## arquivos de backup {#backed-up-files}

### aqf_files.json {#aqf_files.json}

As informações contidas nesse arquivo são geradas pelo módulo [files](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/androidqf/files.py).  

**Informações contidas

Esse arquivo está no formato json e contém informações sobre os arquivos e seus metadados nos caminhos /sdcard/, /system, /data, etc., no dispositivo. Essas informações são extraídas do arquivo *files.json* gerado durante a aquisição do AndroidQF.

Cada entrada inclui um arquivo com seus metadados, como: o caminho completo do arquivo, o tamanho, o registro de data e hora (indica a última modificação do arquivo e o último acesso ao arquivo), as permissões do arquivo, o identificador do proprietário, as mensagens de erro e os hashes sha1, sha256, sha512, md5, se pré-computados.

As informações desse arquivo são apresentadas da seguinte forma:

**path**: Caminho do arquivo
**size**: Tamanho do arquivo em bytes
**mode**: Permissões do arquivo (leitura, gravação ou execução no formato unix)
**id_usuário**: Identificador do usuário proprietário
**Nome_do_usuário**: Nome do usuário proprietário
**group_id**: Identificador do grupo proprietário
**Nome_do_grupo**: Nome do proprietário do grupo
**changed_time**: Data e hora em que os metadados do arquivo foram modificados
**modified_time**: Data e hora em que o conteúdo do arquivo foi alterado
**Access_time**: Data e hora do último acesso ao arquivo.
* error**: Registro de erros durante a leitura do arquivo
**context**: tag de segurança do SELinux
** **Hashses:** Valores calculados dos hashes associados a cada arquivo

**Por que isso é importante?

Porque éEsse arquivo é relevante para identificar arquivos de interesse em uma investigação forense, incluindo possíveis arquivos usados por invasores para comprometer um dispositivo, e para análise oportuna para rastrear atividades mal-intencionadas.

**Estrutura do arquivo:

```
        "caminho":"/sdcard/Android/.Trash/com.sec.android.app.myfiles/.nomedia",
        "tamanho": 62,
        "mode":"-rw-rw----",
        "user_id": 10276,
        "nome_do_usuário": "",
        "group_id": 1023,
        "nome_do_grupo": "",
        "changed_time": "2025-07-28 03:46:55.000000",
        "modified_time": "2025-07-28 03:46:55.000000",
        "access_time": "2024-05-05 13:35:15.000000",
        "error": "",
        "contexto": "u:object_r:fuse:s0",
        "sha1": "",
        "sha256": "",
        "sha512": "",
        "md5": ""
    },
    {
        "path": "/sdcard/Android/.Trash/com.sec.android.app.myfiles/0d2b854e-bc86-4478-b0a9-6802f21ba015/1753640873997/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Images/.!%#@$/IMG-20250727-WA0000.jpg",
        "tamanho": "130802,
        "mode": "-rw-rw----",
        "user_id": 10276,
        "nome_do_usuário": "",
        "group_id": 1023,
        "nome_do_grupo": "",
        "changed_time": "2025-07-28 03:46:55.000000",
        "modified_time": "2025-07-27 12:06:02.000000",
        "access_time": "2025-07-27 12:06:02.000000",
        "error": "",
        "contexto": "u:object_r:fuse:s0",
        "sha1": "",
        "sha256": "",
        "sha512": "",
        "md5": ""
    }
```

### sms.json {#sms.json}

As informações nesse arquivo são geradas pelo módulo de backup [sms](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/backup/sms.py), pelo auxiliar de backup [helpers](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/backup/helpers.py) e pelo analisador [backup](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/parsers/backup.py).

**Informações contidas

O arquivo está no formato *json* e contém informações sobre mensagens SMS e MMS recebidas e armazenadas no dispositivo móvel.  Essas informações são extraídas do arquivo *backup.ab* gerado durante uma extração com o AndroidQF.

Em termos gerais, as informações das mensagens SMS e MMS de backup são pesquisadas e descriptografadas (se necessário) para descompactar esse backup, analisar datas, detectar links e homologar formatos.

As informações nesse arquivo são apresentadas da seguinte forma:

* **endereço**: Número de telefone ou endereço que enviou ou recebeu a mensagem.  
* body**: Conteúdo da mensagem em texto simples.
**date**: Carimbo de data/hora no formato Unix da hora do recebimento.  
* date_sent**: carimbo de data/hora Unix de quando a mensagem foi enviada. Se o valor for 0, significa que a mensagem foi recebida.  
* status**: código de status da mensagem:
    * 1: Desconhecido ou sem informações.
    * 0: Completa
    * 64: Envio pendente
    * 128: Rascunho
**type**: Tipo de mensagem
    * 1: Recebida
    * 2: Enviada
    * 3: Rascunho
    * 4: Saída
**recipients**: Lista de destinatários da mensagem.  
** **read**: Indicador se a mensagem foi lida (1) ou não lida (0).  
**isodate**: Data no formato ISO, para facilitar a compreensão.  
**direction**: Direção da mensagem (se ela foi enviada ou recebida).  
    * Enviado: Sent
    * received: Recebida
**links**: Lista de links identificados no corpo da mensagem.

**Por que isso é importante?

O conteúdo desse arquivo inclui informações que lhe permitem rastrear conversas e comunicações que indicam risco ou tentativas de ataques com conteúdo malicioso que indicam um vetor de ataque, como phishing.

Estrutura do arquivo:** **Estrutura do arquivo

```
[
	{
    	"address": "12345",
    	"body": "Reative seu aplicativo para continuar usando o serviço. Se tiver algum problema, solicitamos que você o reinstale em https://example.com/reactivacion",
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
    	"address" (endereço): "54321" (54321),
    	"body": "This is a sample message related to the verification of your account.", { "body": "This is a sample message related to the verification of your account.",
    	"date": "1601498392068",
    	"date_sent": "1601498390000",
    	"status": "-1",
    	"type": "1",
    	"destinatários": ["54321"],
    	"read": "0",
    	"isodate": "2025-01-01 00:00:00.000",
    	"direction": "sent" (direção)
	}
]
```

