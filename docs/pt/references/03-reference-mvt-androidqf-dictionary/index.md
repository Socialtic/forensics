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

Este documento contém informações sobre os arquivos gerados pela MVT por meio do componente [mvt-check-androidqf.](https://github.com/mvt-project/mvt/tree/main/src/mvt/android/modules/androidqf) O objetivo deste dicionário é facilitar ao analista a busca por informações específicas e a compreensão do formato em que as informações da análise forense são apresentadas.

Este recurso faz **parte de um repositório de documentação técnica** que tem como objetivo estabelecer uma base de conhecimentos comprovados, flexíveis e acessíveis para **impulsionar a análise forense consensual em benefício da sociedade civil**. Para organizar o conteúdo, utiliza-se o [quadro de referência de documentação técnica Diataxis](https://diataxis.fr/).

Este recurso em particular se enquadra na categoria de [referências](https://diataxis.fr/reference) e contém informações sobre a análise dos dados de aquisição gerados por dispositivos Android por meio do comando ***mvt-android check-andoridqf***  durante o uso da ferramenta MVT (*Mobile Verification Toolkit)*, desenvolvida e mantida pelo [Laboratório de Segurança da Anistia Internacional](https://securitylab.amnesty.org/es/) e pertencente ao [Projeto MVT](https://github.com/mvt-project/). O objetivo é que um analista **conheça os arquivos gerados, saiba como utilizá-los, onde buscar informações específicas e em que formato as encontrará.**

MVT refere-se ao *Mobile Verification Toolkit*. Trata-se de uma ferramenta desenvolvida, lançada e mantida pelo [Laboratório de Segurança da Anistia Internacional](https://securitylab.amnesty.org/es/), pertencente ao [Projeto MVT](https://github.com/mvt-project/).  A intenção dessa ferramenta é, essencialmente, facilitar a análise forense consensual de dispositivos Android e iOS com o objetivo de identificar vestígios de invasão. 

Este recurso foi atualizado pela última vez em 18 de novembro de 2025 e, para a compilação das informações, tomou-se como base o [*commit 339a1d0712c4cc051e880b8a777d2b8b6295e57b*](https://github.com/mvt-project/mvt/commit/339a1d0712c4cc051e880b8a777d2b8b6295e57b). 

As informações geradas pelo *mvt-androidqf* podem ser agrupadas em 5 categorias principais:

* Detalhes da aquisição  
* Configuração do dispositivo  
* Informações sobre registros e eventos do sistema  
* Processos e aplicativos  
* Arquivos de backup

Por sua vez, cada uma das categorias contém arquivos específicos gerados pela ferramenta, os quais estão listados no **índice a seguir**:

- [Detalhes da aquisição](#detalhes-da-aquisição)
    - [info.json](#info.json)
    - [command.log](#command.log)
    - [timeline.csv](#timeline.csv)
- [Configuração do dispositivo](#configuração-do-dispositivo)
    - [aqf_getprop.json](#aqf_getprop.json)
    - [aqf_settings.json](#aqf_settings.json)
    - [mounts.json](#mounts.json)
- [Processos e aplicativos](#processos-e-aplicativos)
    - [aqf_packages.json](#aqf_packages.json)
    - [root_binaries.py](#root_binaries.py)
- [Arquivos de backup](#arquivos-de-backup)
    - [aqf_files.json](#aqf_files.json)

Durante a execução do comando ***mvt-android check-androidqf**,* o MVT também executa módulos correspondentes a  ***mvt-android check-bugreport*** e ***mvt-android check-backup***, desde que existam um arquivo bugreport.zip e um arquivo backup.ab dentro da pasta de entrada de uma extração com o androidqf.

No material de referência complementar [sobre arquivos gerados pela ferramenta mvt ao analisar um bugreport](../02-reference-mvt-bugreport-dictionary/index.md) é descrita a saída do comando check-bugreport e os arquivos resultantes. A seguir, são apresentadas **as referências específicas aos módulos executados pelo comando check-androidqf para analisar o bugreport:**

- [Configuração do dispositivo](../02-reference-mvt-bugreport-dictionary/index.md#configuracion-del-dispositivo-configuracion-del-dispositivo)
    - [dumpsys_get_prop.json](../02-reference-mvt-bugreport-dictionary/index.md#getprop.json)
- [Informações sobre registros e eventos do sistema](../02-reference-mvt-bugreport-dictionary/index.md#informação-sobre-registros-e-eventos-do-sistema)
    - [dumpsys_adb_state.json](../02-reference-mvt-bugreport-dictionary/index.md#dumpsys_adb_state.json)
    - [bugreport_timestamps.json](../02-reference-mvt-bugreport-dictionary/index.md#bugreport_timestamps.json)
    - [dbinfo.json](../02-reference-mvt-bugreport-dictionary/index.md#dbinfo.json)
    - [dumpsys_receivers.json](../02-reference-mvt-bugreport-dictionary/index.md#receivers.json)
- [Processos e aplicativos](../02-reference-mvt-bugreport-dictionary/index.md#processos-e-aplicativos)
    - [dumpsys_packages.json](../02-reference-mvt-bugreport-dictionary/index.md#packages.json)
    - [dumpsys_acactivities.json](../02-reference-mvt-bugreport-dictionary/index.md#activities.json)
    - [dumpsys_appops.json](../02-reference-mvt-bugreport-dictionary/index.md#appops.json)
    - [dumpsys_accessibility.json](../02-reference-mvt-bugreport-dictionary/index.md#accessibilityjson-accessibilityjson)
    - [tombstones.json](../02-reference-mvt-bugreport-dictionary/index.md#tombstones.json)
    - [dumpsys_battery_daily.json](../02-reference-mvt-bugreport-dictionary/index.md#battery_daily.json)
    - [dumpsys_battery_history.json](../02-reference-mvt-bugreport-dictionary/index.md#battery_history.json)
    - [dumpsys_platform_compact.json](../02-reference-mvt-bugreport-dictionary/index.md#platform_compact.json)


Da mesma forma, também listamos os módulos executados pelo ***check-backup***, os quais são detalhados no final deste recurso.  

- [Informações sobre registros e eventos do sistema](#informações-sobre-registros-e-eventos-do-sistema)  
- [sms.json](#sms.json)

## Detalhes da aquisição {#detalhes-da-aquisição}

### info.json {#info.json}

**Informações contidas**

Este arquivo está no formato *json* e contém informações relacionadas à análise realizada em uma extração concluída por meio do AndroidQF. Ele contém as seguintes informações:

* Caminho do arquivo analisado.  
* Versão utilizada do MVT.  
* Data da análise.  
* Lista de arquivos de indicadores de comprometimento.  
* Hash da pasta de saída analisada (SHA-256).

**Por que isso é importante?**

Este arquivo nos permite **validar a análise realizada**, documentando que há um registro do processo de aquisição e dos indicadores considerados para a comparação.

Essas informações permitem estabelecer uma referência do arquivo analisado e das ferramentas de indicadores utilizadas na análise, o que facilita o [processo de custódia da extração forense](https://forensics.socialtic.org/explainers/01-explainer-introduccion-forense-digital/01-explainer-introduccion-forense-digital.html#cadena-de-custodia). 

**Estrutura do arquivo:**

```
{
  "target_path": "/caminho/do/arquivo/acquision-with-androidqf",
  "mvt_version": "2.6.1",
  "date": "AAAA-MM-DD hh:mm:ss",
	"ioc_files": [
 "/caminho/para/indicadores/pegasus.stix2",
 "/caminho/para/indicadores/predator.stix2",
    	"/caminho/para/indicadores/rcs_lab.stix2",
 "... mais indicadores utilizados ..."
  ],
  "hashes": [
 {
        	"file_path": "/caminho/do/arquivo/acquision-with-androidqf",
 "sha256": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
 }
  ]
}
```

### command.log {#command.log}

**Informações contidas**

Este arquivo está em texto simples com a extensão *.log* e contém os registros detalhados da execução do comando *mvt-android check-androidqf*.

Seu conteúdo lista a análise realizada em uma pasta de saída de uma extração de informações forenses feita com o AndroidQF, incluindo a detecção de indicadores de comprometimento para identificar alertas de segurança relacionados a malware.

Os registros do arquivo são apresentados de forma estruturada com:

* Marcas de tempo  
* Nomes do módulo em execução  
* Tipo de mensagem (*INFO*, *DEBUG*, WARNING, *ERROR*)  
* Ação correspondente do módulo (análise do arquivo, carregamento de IoCs, comparação e resultado da comparação).

Os tipos de mensagem correspondem da seguinte forma:

* *INFO*. Mensagens exibidas também na tela durante a execução.  
* *DEBUG*. Informações não exibidas na tela, mas associadas a uma ação realizada durante a análise, por exemplo, o carregamento de um IoC ou a verificação de um hash.  
* *WARNING.* Corresponde a alertas de atividade ou informações suspeitas que um analista deve verificar.  
* *ERROR.* Mensagens de erro em alguma ação realizada durante a análise, por exemplo, ao carregar um arquivo corrompido ou um problema com a execução do código correspondente.

**Por que isso é importante?**

Permite gerar um registro das ações realizadas durante a análise. Por meio desse registro, é possível verificar o seguinte:

* Se a análise foi realizada corretamente  
* Se houve correspondências com IoCs  
* Se foram identificadas informações ou atividades suspeitas.

**Estrutura do arquivo:**

Este arquivo segue um formato linha por linha com a seguinte estrutura.

```
[TIMESTAMP] - [MÓDULO] - [NÍVEL DE LOG] - [MENSAGEM]  
...
2025-01-17 17:06:14,035 - mvt.android.cmd_check_androidqf - INFO - Analisando o arquivo de indicadores STIX2 no caminho /home/user/.local/share/mvt/indicators/raw.githubusercontent.com_AmnestyTech_investigations_master_2021-07-18_nso_pegasus.stix2  
17/01/2025 17:06:14,098 - mvt.android.cmd_check_androidqf - DEBUG - Extraídos 1.549 indicadores para a coleção com o nome “Pegasus”  
17/01/2025 17:06:14,812 - mvt.android.cmd_check_androidqf - DEBUG - Extraídos 245 indicadores para a coleção com o nome “mSpy”  
```

**Saiba mais**

* [Introdução ao STIX](https://oasis-open.github.io/cti-documentation/stix/intro.html)

### timeline.csv {#timeline.csv}

**Informações contidas**  
Este arquivo está no formato *csv* e armazena uma linha do tempo da atividade do dispositivo. Essa atividade é obtida a partir da execução dos módulos de análise do MVT e é ordenada por tempo.

Cada linha do *csv* corresponde a:

* Carimbo de data/hora (Device Local Timestamp).  
* Módulo executado (Plugin).  
* Atividade identificada no dispositivo (Event)  
* Descrição da atividade identificada no dispositivo (Description).

**Por que isso é importante?**

Este arquivo permite acompanhar a atividade interna do dispositivo, proporcionando uma visão abrangente de como o dispositivo se comportou e identificando eventos relevantes. 

**Estrutura do arquivo**

Este arquivo segue um formato linha por linha com a seguinte estrutura.

```
"UTC Timestamp","Plugin","Event","Description"
"2025-01-01 00:00:00","Packages","package_first_install","com.example.app (system: False, third party: True)"
"2025-01-01 00:00:00","Packages","package_last_update","com.system.module (system: True, third party: False)"
"2025-01-01 00:00:00","Pacotes","package_install","com.example.newapp (sistema: False, de terceiros: True)"
```

## Configuração do dispositivo {#configuração-do-dispositivo}

### aqf\_getprop.json {#aqf_getprop.json}

As informações deste arquivo são geradas pelo módulo [aqf\_getprop](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/androidqf/aqf_getprop.py) e pelo artefato [getprop](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/artifacts/getprop.py).

**Informações contidas**

Este arquivo está no formato *json* e contém uma lista das propriedades do dispositivo extraídas do arquivo *getprop.tx* gerado durante uma extração com o AndroidQF.

Essas propriedades do sistema são pares chave-valor de strings armazenados no dicionário global [*build.prop*](https://xdaforums.com/t/guide-build-prop-wiki.2056266/) ou em arquivos de descrição *.sysprop*, e oferecem uma maneira prática de compartilhar configurações dentro do sistema. 

As informações podem ser encontradas no seguinte formato:

```
[{prefixo}.]{grupo}[.{subgrupo}]*.{nome}[.{tipo}]
```

Algumas propriedades aparecem com o prefixo *ro*, o que indica que são de somente leitura ou que foram atribuídas após a reinicialização do dispositivo. As propriedades com o prefixo *persist* referem-se a configurações resistentes à reinicialização. Algumas propriedades não terão prefixo, portanto começam diretamente com o grupo ao qual pertencem. 

Os grupos mais comuns são:

* *bluetooth*, relacionado ao Bluetooth  
* *boot*, sysprops da linha de comando do kernel  
* *build*, sysprops que identificam uma compilação  
* *telephony*, relacionado à telefonia  
* *audio*, relacionado ao áudio  
* *graphics*, relacionado aos gráficos  
* *vold*, relacionado ao vold, que gerencia a montagem de volumes físicos de armazenamento externo

Para mais detalhes, consulte a [lista de propriedades já definidas no código-fonte do Android](https://android.googlesource.com/platform/system/sepolicy/+/refs/heads/main/private/property_contexts).

**Por que isso é importante?**

As propriedades fornecem informações importantes sobre o hardware e o software do dispositivo, as quais podem ser alteradas por software malicioso para ocultar sua presença ou para modificar o comportamento do dispositivo de forma imperceptível.

**Estrutura do arquivo:**

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

As informações deste arquivo são geradas pelo módulo [aqf\_settings](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/androidqf/aqf_settings.py) e pelo artefato [settings](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/artifacts/settings.py).

**Informações contidas**

Este arquivo está no formato *json* e contém informações sobre o estado das configurações do dispositivo nos *namespaces* *system* (interface do usuário e comportamento geral, como brilho, tom, rotação etc.), *secure* (configurações sensíveis que exigem permissões elevadas, como verificação de aplicativos, ajustes de acessibilidade ou status do ADB) e *global* (parâmetros compartilhados entre usuários, como redes, localização, roaming, volumes globais etc.). 

As informações são apresentadas em três blocos: primeiro aparecem as configurações do *system*, depois as do *secure* e, por fim, as do *global*. Cada configuração é apresentada como um par chave-valor na estrutura:

```json
[{setting}:{level}]
```

Os valores de cada configuração têm significados diferentes dependendo da configuração em questão, mas, em geral, tratam-se de:A seguir:

* **0** geralmente significa desativado ou desligado.  
* **1** geralmente significa ativado ou ligado.  
* **Números maiores** podem corresponder a níveis, como o brilho da tela, por exemplo.  
* Alguns valores são **paths** ou caminhos do sistema que apontam para recursos.

Essas informações são extraídas diretamente dos arquivos settings\_global.txt, settings\_secure.txt e settings\_system.txt gerados durante uma extração com o AndroidQF.

**Por que isso é importante?**

Permite identificar configurações anômalas que poderiam comprometer a segurança, a privacidade  ou a funcionalidade do dispositivo. Configurações padrão incomuns podem indicar tentativas de modificar o comportamento do sistema, sejam elas intencionais ou acidentais.

**Estrutura do arquivo:**

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
 "Contacts_move_simcontacts_not_now": "0",
 "Phenotype_boot_count": "131",
 "Phenotype_flags": "_boot_Phenotype_flags": "",
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

**Saiba mais**

* [Lista completa de preferências do sistema — Configurações do Sistema](https://developer.android.com/reference/android/provider/Settings.System?hl=es-419)  
* [Lista completa de preferências do sistema \- Configurações de Segurança](https://developer.android.com/reference/android/provider/Settings.Secure?hl=es-419)  
* [Lista completa de preferências do sistema \- Configurações globais](https://developer.android.com/reference/android/provider/Settings.Global?hl=es-419)

### mounts.json {#mounts.json}

As informações deste arquivo são geradas pelo módulo [mounts](https://github.com/mvt-project/androidqf/blob/main/modules/mounts.go) e pelo artefato [mounts](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/artifacts/mounts.py) 

**Informações contidas**

Este arquivo está no formato *json* e contém informações sobre as partições e diretórios de sistemas de arquivos montados em um dispositivo no espaço do usuário *e* no kernel Linux do Android, extraídas do arquivo *mounts.json* gerado durante uma extração com o AndroidQF.

O módulo se encarrega de identificar configurações suspeitas nos pontos de montagem /system, /vendor, /product e /system\_ext, como modo de acesso de leitura e gravação, marcas de tempo *notime* ou *nodiratime*, e, posteriormente, se encarrega de formatar cada ponto de montagem da seguinte maneira:

* **device**: Partição ou volume montado; no Android, os mais comuns são:
    * Partições de armazenamento físico
 * /dev/block/sdX: Dispositivo de armazenamento físico ([eMMC/UFS](https://new.c.mi.com/es/post/11738)) exposto como sd pelo kernel.
        * /dev/block/mmcblk: Dispositivo de armazenamento eMMC apresentado como mmcblk.
 * /dev/block/dm-X: Dispositivo gerenciado pelo device-mapper (criptografado, verity ou partições lógicas).
        * /dev/block/by-name/: Links simbólicos que apontam para as partições reais por nome, por exemplo, system, vendor, userdata.
    * Volume virtual do kernel na RAM
 * proc: Interface virtual para obter informações sobre o kernel e os processos.
        * sysfs: Exibe informações sobre dispositivos, drivers e parâmetros do kernel.
 * selinuxfs: Exibe políticas, estados e etiquetas do SELinux.
 * tracefs: Sistema virtual para ferramentas de rastreamento e depuração do kernel.
        * pstore: Armazena registros persistentes de falhas do kernel.
 * bpf: Exibe interfaces para programas [eBPF](https://source.android.com/docs/core/architecture/kernel/bpf) carregados no kernel.
    * Espaço do usuário
 * /dev/fuse: Interface [FUSE](https://source.android.com/docs/core/storage/fuse-passthrough) usada pelo Android paramontar o armazenamento emulado, por exemplo, /storage/emulated.
    * Interfaces internas de controle do kernel
 * none: Identificador que indica que a montagem não provém de um dispositivo real.
        * binder: [Sistema de IPC](https://source.android.com/docs/core/architecture/ipc/binder-overview) interno do Android para comunicação entre processos.
    * Arquivos APEX montados como loopback
 * /dev/block/loopX: Dispositivos de loopback usados para montar pacotes APEX como se fossem partições reais.

* **ponto de montagem**: Caminho da pasta raiz do armazenamento onde as informações são acessadas; no Android, geralmente são os seguintes:
    * /system: Contém o sistema operacional principal.
    * /vendor: Inclui componentes e drivers fornecidos pelo fabricante do hardware, como HALs, firmware e binários específicos do fornecedor.
    * /product: Armazena personalizações do fabricante relacionadas às funcionalidades do sistema e aplicativos específicos do dispositivo.
    * /data: Área de dados do usuário e armazenamento de aplicativos.
    * /cache: Espaço temporário usado para arquivos de atualização e dados transitórios do sistema.
    * /metadata: Contém informações críticas necessárias para [AVB](https://source.android.com/docs/security/features/verifiedboot/avb), criptografia e validações do sistema.
    * /mnt/media_rw/: Ponto de montagem para armazenamento removível ou emulado, por exemplo, cartão SD.
    * /storage/emulated: Visão emulada do armazenamento interno do usuário.
    * /proc: Sistema virtual que expõe informações do kernel e dos processos (não é armazenamento real).
    * /sys: Sistema virtual que expõe informações sobre dispositivos e controladores do kernel.
    * /mnt/user/0/emulated: Visão específica do armazenamento emulado para o usuário 0.

* **filesystem_type**: Tipo de sistema de arquivos; no Android, são os seguintes:
    * ext4: Sistema de arquivos do Linux usado em partições internas.
    * f2fs: Sistema de arquivos otimizado para armazenamento flash.
    * erofs: Sistema de arquivos otimizado somente para leitura.
    * vfat: Sistema de arquivos FAT32 usado para cartões SD e armazenamento externo.
    * sdfat: Implementação estendida do FAT/exFAT.
    * tmpfs: Sistema de arquivos temporário na RAM usado para diretórios voláteis, por exemplo, /dev, /run, /apex.
    * proc: Sistema de arquivos virtual que expõe informações do kernel e dos processos.
    * sysfs: Sistema virtual que exibe informações de hardware, drivers e controladores do kernel.
    * selinuxfs: Sistema virtual que expõe parâmetros e o estado do SELinux no dispositivo.
    * functionfs: Sistema usado para interfaces [USB gadget](https://source.android.com/docs/core/permissions/usb-hal) quando o Android atua como um dispositivo USB.
    * incremental-fs: Sistema projetado para instalar ou executar aplicativos “sob demanda” enquanto eles ainda estão sendo baixados.
    * binder: Sistema de comunicação interna IPC do Android.
    * cgroup: Sistema virtual baseado em grupos de controle para gerenciar recursos por processos, por exemplo, CPU e memória.
    * fuse: Sistema de arquivos no espaço do usuário utilizado para armazenamento emulado.

* **mount_options**
    * modos de acesso
 * ro: somente leitura
 * rw: leitura e gravação
    * rótulos de segurança
 * seclabel: habilita e aplica rótulos SELinux ao sistema de arquivos.
        * nodev: Impede o uso de arquivos de dispositivo nessa partição.
 * nosuid: Bloqueia binários com [set-UID/set-GID](https://www.cbtnuggets.com/blog/technology/system-admin/linux-file-permissions-understanding-setuid-setgid-and-the-sticky-bit) para evitar escalonamento de privilégios.
 * noexec: Impede a execução de arquivos nessa partição.
        * hidepid=invisible: Oculta processos de outros usuários em */proc*.
 * user_xattr: Permite atributos estendidos definidos pelo usuário.
 * acl: Permite listas de controle de acesso mais detalhadas do que *rwx*.
        * inlinecrypt: Utiliza criptografia em linha suportada por hardware/sistema de arquivos (Android).
 * usrquota: Habilita cotas por usuário.
 * grpquota: Habilita cotas por grupo.
    * carimbos de data/hora
 * lazytime: Adia a gravação dos carimbos de data/hora no armazenamento para melhorar o desempenho.
 * relatime: Atualiza os tempos de acesso somente se necessário.
 * noatime: Desativa a atualização do tempo de acesso.
    * usuários ou grupos relacionados
 * uid=0: Proprietário do montagem (root).
 * gid=1000: Grupo base do Android (system ou media_rw).
        * user_id=0: Usuário principal do sistema Android.
 * group_id=0: Grupo primário do usuário root.

* **is_system_partition**: Valor booleano que indica se a partição é /system ou /sys.
* **is_read_write**: Valor booleano que indica se a partição possui acesso de leitura e gravação.


**Por que isso é importante?**

Os pontos de montagem permitem identificar as **áreas de armazenamento montadas no dispositivo**, sua origem e como estão configuradas. CCom essas informações, é possível verificar as permissões com as quais as partições foram montadas, os usuários associados e, em alguns casos, as etiquetas de segurança do SELinux aplicadas. Isso é útil para a **identificação de montagens que possam ser suspeitas** de atividades maliciosas no dispositivo, por exemplo, uma partição do sistema como /system, /vendor, /product — partições cuja montagem geralmente é somente de leitura — que esteja montada com permissões de gravação ou sem etiquetas de segurança; ou uma partição como /data que esteja montada com permissões de leitura em subpastas que contêm informações de aplicativos — o que poderia indicar montagens fraudulentas e não autorizadas, evidenciando comportamentos altamente suspeitos.

**Exemplo do conteúdo do arquivo**

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

**Para saber mais:**

* [Visão geral das partições do Android](https://source.android.com/docs/core/architecture/partitions?hl=es-419)   
* [Contexto e terminologia das partições dinâmicas](https://source-android-com.translate.goog/docs/core/ota/virtual_ab?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=sge#background)  
* [Sistema de arquivos do Android](https://medium.com/@aditi.kale20/file-system-of-android-a89dcbb693f1)   
* [Compatibilidade com o sistema de arquivos do kernel do Android](https://source-android-com.translate.goog/docs/core/architecture/android-kernel-file-system-support?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc)  
* [Compatibilidade com o SELinux](https://source.android.com/docs/security/features/selinux/compatibility)  
* [Formato de arquivo APEX](https://source.android.com/docs/core/ota/apex)  
* [Sistema de arquivos do Android](https://keepcoding.io/blog/sistema-de-ficheros-android/) 

## Processos e aplicativos {#processos-e-aplicativos}

### aqf_packages.json {#aqf_packages.json}

As informações deste arquivo são geradas pelo módulo [aqf\_packages](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/androidqf/aqf_packages.py).

**Informações contidas**

Este arquivo está no formato *json* e contém informações sobre os aplicativos instalados no dispositivo. Essas informações são extraídas do arquivo *packages.json* gerado durante a aquisição do AndroidQF.

As informações deste arquivo são apresentadas da seguinte forma:

* **name**: Nome do pacote do aplicativo.  
* **files**: Caminho do arquivo APK correspondente, com seus respectivos hashes e informações do certificado.  
* **installer**: A partir de qual aplicativo foi instalado.  
* **uid**: O PID associado em execução.  
* **disabled**: Indica se o aplicativo está desativado.  
* **system**: Indica se o pacote pertence ao sistema.  
* **third\_party**: Indica se é um aplicativo de terceiros.

**Por que isso é importante?**  
O conteúdo desse arquivo inclui informações que permitem identificar os aplicativos instalados e qual é o status deles no dispositivo. Isso ajuda os analistas a avaliar se existem aplicativos de risco ou maliciosos, quais permissões eles possuem e quais podem comprometer a segurança.

**Estrutura do arquivo:**

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
 "c"certificado": {
 "Md5": "d087e72912fba064cafa78dc34aea839",
                    "Sha1": "9ca5170f381919dfe0446fcdab18b19a143b3163",
                    "Sha256": "34df0e7a9f1cf1892e45c056b4973cd81ccf148a4050d11aea4ac5a65f900a42",
                    "ValidFrom": "2011-06-22T12:25:12Z",
 "ValidTo": "2038-11-07T12:25:12Z",
                    "Issuer": "C=KR, ST=Coreia do Sul, L=Cidade de Suwon, O=Samsung Corporation, OU=DMC, CN=Samsung Cert",
 "Subject": "C=KR, ST=Coreia do Sul, L=Cidade de Suwon, O=Samsung Corporation, OU=DMC, CN=Samsung Cert",
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

As informações deste arquivo são geradas pelo módulo [root\_binaries](https://github.com/mvt-project/androidqf/blob/main/modules/root_binaries.go)

**Informações contidas**

Este arquivo está no formato *json* e contém uma lista de binários relacionados ao rooting no dispositivo, extraída do arquivo *root\_binaries.json* gerado durante uma extração com o AndroidQF.

Este módulo é responsável por extrair os binários do arquivo base para, posteriormente, identificar binários suspeitos de root e seus rastros. O formato aplicado é o seguinte:

* path: Caminho para o binário de root encontrado.  
* binary\_name: Nome do binário; pode ser um dos seguintes: 
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
* descrição: Descrição do binário de root, podendo ser uma das seguintes: 
 * su: Binário do SuperUser  
    * busybox: utilitários do BusyBox 
 * supersu: gerenciamento de root do SuperSU 
 * Superuser.apk: aplicativo Superuser 
 * KingoUser.apk: aplicativo KingRoot 
 * SuperSu.apk: aplicativo SuperSU  
    * magisk: estrutura de root do Magisk 
 * magiskhide: utilitário de ocultação do Magisk 
 * magiskinit: binário de inicialização do Magisk 
 * magiskpolicy: binário de política do Magisk

**Por que isso é importante?**

Este arquivo detecta ferramentas de root, o que pode indicar  acessos não autorizados e escalonamento de privilégios que possam expor alguma vulnerabilidade.  Além disso, permite que o analista identifique binários suspeitos que possam ter sido instalados sem o conhecimento do usuário e ajuda a determinar se o dispositivo foi manipulado.

**Exemplo do conteúdo do arquivo**

```
    {
 "path": "/system/xbin/su",
 "binary_name": "su",
        "description": "Binário do SuperUser"
    },
    {
 "path": "/system/bin/su",
 "binary_name": "su",
 "description": "Binário do SuperUser"
    },
    {
 "path": "/system/bin/busybox",
 "binary_name": "busybox",
 "description": "Utilitários do BusyBox"
    },
    {
 "path": "/data/local/tmp/magisk",
 "binary_name": "magisk",
 "description": "Estrutura de root do Magisk"
    }
```

## Arquivos de backup {#arquivos-de-backup}

### aqf_files.json {#aqf_files.json}

As informações deste arquivo são geradas pelo módulo [files](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/androidqf/files.py).  

**Informações contidas**

Este arquivo está no formato JSON e contém informações sobre os arquivos e seus metadados nos caminhos /sdcard/, /system, /data etc. no dispositivo. Essas informações são extraídas do arquivo *files.json* gerado durante a aquisição do AndroidQF.

Cada entrada inclui um arquivo com seus metadados, tais como: o caminho completo do arquivo, tamanho, carimbo de data/hora (indica a última modificação e o último acesso ao arquivo), permissões do arquivo, identificador do proprietário, mensagens de erro e hashes sha1, sha256, sha512 e md5, caso estejam pré-calculados.

As informações deste arquivo são apresentadas da seguinte maneira:

* **path**: Caminho do arquivo  
* **size**: Tamanho do arquivo em bytes  
* **mode**: Permissões do arquivo (leitura, gravação ou execução no formato Unix)  
* **user\_id**: Identificador do usuário proprietário  
* **user\_name**: Nome do usuário proprietário   
* **group\_id**: Identificador do grupo proprietário  
* **group\_name**: Nome do grupo proprietário  
* **changed\_time**: Data e hora em que os metadados do arquivo foram modificados   
* **modified\_time**: Data e hora em que o conteúdo do arquivo foi modificado  
* **access\_time**: Data e hora do último acesso ao arquivo  
* **error**: Registro de erros durante a leitura do arquivo  
* **context**: Etiqueta de segurança do SELinux  
* **Hashses:** Valores calculados dos hashes associados a cada arquivo

**Por que é importante?**

Este arquivo é relevante para identificar arquivos de interesse em uma investigação forense, incluindo possíveis arquivos utilizados por invasores para comprometer um dispositivo e realizar as análises necessárias que permitam rastrear atividades maliciosas. 

**Estrutura do arquivo**:

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
 "path": "/sdcard/Android/.Lixeira/com.sec.android.app.myfiles/0d2b854e-bc86-4478-b0a9-6802f21ba015/1753640873997/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Images/.!%#@$/IMG-20250727-WA0000.jpg",
 "size": 130802,
        "mode": "-rw-rw----",
 "user_id": 10276,
 "user_name": "",
 "group_id": 1023,
        "group_name": "",
 "changed_time": "28/07/2025 03:46:55.000000",
        "modified_time": "27/07/2025 12:06:02.000000",
        "access_time": "27/07/2025 12:06:02.000000",
 "error": "",
 "context": "u:object_r:fuse:s0",
        "sha1": "",
 "sha256": "",
 "sha512": "",
 "md5": ""
    }
```

### sms.json {#sms.json}

As informações deste arquivo são geradas pelo módulo de backup [sms](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/backup/sms.py) e pelo helper de backup [helpers](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/modules/backup/helpers.py) e o analisador [backup](https://github.com/mvt-project/mvt/blob/main/src/mvt/android/parsers/backup.py).

**Informações contidas**

O arquivo está no formato *json* e contém informações sobre as mensagens SMS e MMS recebidas e armazenadas no dispositivo móvel. Essas informações são extraídas do arquivo *backup.ab* gerado durante uma extração com o AndroidQF.

De modo geral, as informações do backup de mensagens SMS e MMS são buscadas e descriptografadas (se necessário) para que seja possível descompactar esse backup, analisar datas, detectar links e padronizar formatos.

As informações deste arquivo são apresentadas da seguinte maneira:

* **address**: Número de telefone ou endereço que enviou ou recebeu a mensagem.  
* **body**: Conteúdo da mensagem em texto simples  
* **date**: Carimbo de data/hora no formato Unix do momento da recepção.  
* **date\_sent**: Carimbo de data/hora no formato Unix de quando a mensagem foi enviada. Se o valor for 0, significa que a mensagem foi recebida.  
* **status**: Código de status da mensagem: 
 * \-1: Desconhecido ou sem informações 
 * 0: Completa 
 * 64: Aguardando envio  
    * 128: Rascunho  
* **type**: Tipo de mensagem 
 * 1: Recebida 
 * 2: Enviada 
 * 3: Rascunho 
 * 4: A enviar  
* **recipients**: Lista de destinatários da mensagem.  
* **read**: Indicador de se a mensagem foi lida (1) ou não lida (0).  
* **isodate**: Data no formato ISO, para facilitar a compreensão.  
* **direction**: Direção da mensagem (se foi enviada ou recebida). 
 * sent: Enviada 
 * received: Recebida  
* **links**: Lista de links identificados no corpo da mensagem.

**Por que isso é importante?**

O conteúdo desse arquivo inclui informações que permitem acompanhar conversas e comunicações que indiquem risco ou tentativas de ataques com conteúdos maliciosos, apontando um vetor de ataque como o phishing.

**Estrutura do arquivo:**

```
[
  {
 "address": "12345",
 "body": "Reative seu aplicativo para continuar aproveitando o serviço. Se tiver algum problema, pedimos que você o reinstale a partir de https://example.com/reactivacion",
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
 "body": "Esta é uma mensagem de exemplo relacionada à verificação da sua conta.",
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

