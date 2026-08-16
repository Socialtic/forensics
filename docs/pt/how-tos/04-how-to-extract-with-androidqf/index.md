---

title: Adquisición y extracción de dispositivos Android mediante AndroidQF
summary: Adquisición y extracción de dispositivos Android mediante AndroidQF 
keywords: android, adquisicion, extraccion, androidqf
authors: 
tags: [androidqf, extraction, acquisition, adquisicion, extraccion]
last_updated: 2025-12-09
some_url:
created: 2025-08-01
comments: true
name: jose
translation-review-pending: true
---

# Guia: Como realizar uma aquisição e extração usando o AndroidQF?

Este documento faz parte de um **repositório de documentação técnica** que visa estabelecer uma base de conhecimento comprovada, flexível e acessível para **promover a análise forense consensual em benefício da sociedade civil**. Para organizar o conteúdo, é usada a [estrutura de referência de documentação técnica Diataxis](../../references/00-glossary/index.md#ditaxis).

Esse recurso se enquadra na categoria [Guide, how-to](../) e contém instruções para realizar uma extração forense com a ferramenta [AndroidQF](../../references/00-glossary/index.md#androidqf).

## O que é o AndroidQF?

O [AndroidQF] (https://github.com/mvt-project/androidqf) é uma ferramenta de software gratuita e de código aberto **focada na extração forense de dispositivos Android**. Atualmente é mantida pelo [Amnesty International Security Lab](https://securitylab.amnesty.org/es/).

Seu foco é especificamente para jornalistas, ativistas, defensores dos direitos humanos e os **laboratórios técnicos que acompanham casos de vigilância digital e ameaças de spyware**.

O AndroidQF funciona como um [wrapper] forense (https://developer.mozilla.org/en-US/docs/Glossary/Wrapper) no [ADB](.../../references/00-glossary/index.md#adb), automatizando comandos comuns por meio de módulos que **permitem extrações rápidas, seguras e locais de qualquer sistema operacional (Linux, Windows ou macOS)**, sem depender de serviços em nuvem ou instalações complexas.

Sua utilidade em contextos da sociedade civil está em sua **[portabilidade](../../references/00-glossary/index.md#portable-tool), facilidade de uso e execução local.

Este guia é complementado por outros materiais, como o [dicionário de arquivos gerados pelo AndroidQF](../../references/01-reference-androidqf-dictionary/), seus formatos e recomendações de uso ou o [explicador sobre análise forense baseada em registros para dispositivos Android](../../explainers/03-explainer-log-forensics-android/).

## Pré-requisitos para realizar a extração forense

Para poder realizar uma extração com o AndroidQF, é **necessário**:

* O **dispositivo Android a ser analisado**: habilitar o **[modo de desenvolvedor](../../references/00-glossary/index.md#developer-mode)** e **[habilitar a depuração USB](../../references/00-glossary/index.md#adb)**. Se necessário, consulte nossos [guias sobre como ativar as opções do desenvolvedor](../02-how-to-enable-developer-options/) ou [guia sobre como ativar o ADB](../03-how-to-enable-adb/).
* Computador Windows, Linux ou Mac**: será usado para realizar a extração. Você precisa saber qual é o chip [chip incorporado do computador] (https://servernet.com.ar/como-saber-si-mi-procesador-es-amd-o-arm/)
* Tenha um **cabo de transferência de arquivos** para o telefone-computador.

### Criptografia das extrações

Esse procedimento permite a criptografia automática das extrações geradas pelo AndroidQF usando uma chave pública *AGE*. É recomendado quando a extração é feita remotamente, quando você precisa enviar ou compartilhar informações por meio de mídia virtual, quando há risco de exposição ou quando você segue alguma política de privacidade.

Para isso, siga as etapas abaixo:

* Se for você quem estiver descriptografando as informações, deverá criar uma chave pública e uma chave privada seguindo a [documentação oficial] (https://github.com/FiloSottile/age).  
Se você for um cifrador em nome de uma organização ou de outro analista, peça à pessoa a chave pública [*AGE*](https://github.com/FiloSottile/age) **.** **.
* No mesmo diretório em que o binário do AndroidQF está localizado, crie um arquivo chamado: *key.txt*.
* Abra o *key.txt*, cole a chave pública completa em uma única linha e salve as alterações.

Para descriptografar o *.zip*, tudo o que você precisa fazer é o seguinte:

* Crie um arquivo *.txt* chamado **private.key** no diretório em que o binário andoridqf está localizado, abra-o e cole a chave privada que começa com: *AGE-SECRET-KEY-...*.
    
* Execute o seguinte comando para descriptografar as informações:

````shell
$ age --decrypt -i ~/path/to/privatekey.txt -o <UUID>.zip <UUID>.zip.age
```

!!! observe "Verificar o par de chaves".
        
    Certifique-se de que a chave privada seja o par de chaves públicas.  


## Etapas para obter uma extração forense com o AndroidQF

Abaixo estão as etapas detalhadas para realizar a extração forense:

### :material-numeric-1-box: Faça o download do binário no AndroidQF

* **Baixe** a versão mais recente do [binário](../../references/00-glossary/index.md#binary), e que **corresponda à arquitetura do computador** onde ele será executado. O download é feito a partir das versões do repositório: [https://github.com/mvt-project/androidqf/releases/](https://github.com/mvt-project/androidqf/releases/)

    !!! pergunta "Como identificar a arquitetura?"
        
        Se não tiver certeza de qual é a arquitetura do equipamento que está usando, consulte este [recurso para descobrir qual chip está incorporado no dispositivo] (https://servernet.com.ar/como-saber-si-mi-procesador-es-amd-o-arm/).

* Crie uma nova pasta** para armazenar o download do dispositivo. Mova o binário recém-baixado para essa pasta.

### :material-numeric-2-box: Atribua permissões de execução ao binário baixado (**Linux e macOS somente**)

* Se estiver usando uma máquina **Linux ou macOS** para a extração, será necessário atribuir permissão de execução ao arquivo antes de poder executá-lo. Para fazer isso, **abra um terminal e navegue até a pasta onde o binário está localizado** e, em seguida, execute:


    !!! Aviso "Complete o nome"

        Ao executar o comando, **certifique-se de completar o nome** *androidqf_* com o nome completo do binário baixado na etapa 1. O comando resultante será semelhante a:

        ```
        chmod +x ./androidqf_v1.7.1_linux_amd64
        ```


    **No linux:**

    ```
    chmod +x ./androidqf_
    ```

    **No macOS:**

    ```
    chmod +x ./androidqf_
    ```


### :material-numeric-3-box: Conectando o telefone

* **Conecte** o dispositivo desbloqueado ao computador usando um cabo de dados USB.

    !!! falha "Nem todos os cabos USB são iguais".

        Alguns cabos USB não têm as conexões necessárias para transferir dados entre o dispositivo móvel e o computador. Certifique-se de usar um cabo que possa transferir dados. É [difícil distinguir à primeira vista] (https://support.konnected.io/how-to-tell-a-usb-charge-only-cable-from-a-usb-data-cable), mas geralmente os cabos de carregamento rápido ou aqueles incluídos nos dispositivos são cabos de dados.  

* Quando o telefone estiver conectado, uma nova mensagem será exibida. Selecione **permitir** quando o dispositivo Android **solicitar permissão para acessar dados no dispositivo**, conforme mostrado na imagem 1.

    !!! falha "Nenhuma mensagem aparece".

        Se você não receber nenhuma mensagem sobre permissões ao conectar o dispositivo ao computador, verifique o seguinte:

        * Certifique-se de que [a depuração USB esteja ativada](../03-how-to-enable-adb/).
        * Verifique as **configurações USB** e certifique-se de que a opção _transferência de arquivos_ esteja ativada.
        * Certifique-se de que o cabo USB seja um **cabo de dados**.

    Captura de tela do dispositivo móvel Samsung Android solicitando permissões de acesso a dados](.../../../../assets/04-how-to/01-capture-android-data-permissions.png "image 1")
    /// legenda
    **Imagem 1**. Captura de tela do dispositivo móvel Samsung Android solicitando permissão de acesso a dados.
    ///

* Verifique se o arquivo key.txt está na mesma pasta que o binário andoridqf se você quiser criptografar a extração.


### Material-numeric-4-box: execute o AndroidQF

Neste ponto, é possível executar o androidQF seguindo estas instruções:

=== "Linux e MacOS"

    Execute com o **seguinte comando**. **Certifique-se de preencher **androidqf_* com o nome completo do binário baixado.
    
    ```
    ./androidqf-linux-v?
    ./androidqf-macos-v?
    ```

    ![Captura de tela do terminal Linux com binário em execução para inicialização da extração](../../../../../assets/04-how-to/02-capture-terminal-linux-running.png "image 2")
    /// legenda
    **Imagem 2**. Captura de tela do terminal Linux com binário em execução para inicialização da extração
    ///

=== "Windows" === "Windows" === "Windows" === "Windows" === "Windows" === "Windows" === "Windows

    * Vá para a pasta em que o binário baixado na etapa 1 foi salvo e **clique duas vezes no arquivo** Uma janela de proteção do Windows será exibida; clique em **"More information "**.

    Captura de tela da janela pop-up de proteção do Windows](../../../../assets/04-how-to/03-capture-terminal-windows-run.png "image 3")
    /// legenda
    **Imagem 3**. Captura de tela da janela pop-up de proteção do Windows.
    ///

    * Selecione **"Executar mesmo assim "**.

    Captura de tela da janela pop-up de proteção do Windows com a seleção de executar mesmo assim...](../../../../../assets/04-how-to/04-capture-screenshot-protection-windows.png "image 4")
    /// legenda
    **Imagem 4**. Captura de tela do pop-up de proteção do Windows com a opção de executar de qualquer forma.
    ///



### :material-numeric-5-box: Confirmar e configurar a extração

As próximas etapas serão aplicadas da **mesma forma** nos 3 sistemas operacionais considerados neste tutorial: **Linux, Windows e macOS**.

**O AndroidQF identificará automaticamente o dispositivo quando ele permitir a depuração USB** e gerará uma pasta com um identificador exclusivo (UUID). A extração será armazenada nessa pasta.

    !!! pergunta O que é um UUID?  

        É um número gerado aleatoriamente, expresso por 32 dígitos hexadecimais divididos em cinco grupos separados por hífens no formato 8-4-4-4-4-12 para um total de 36 caracteres (32 dígitos e 4 hífens), por exemplo, ```0caba18f-20a7-48d0-b9ba-724fdaa3ff85````.

* Em seguida, o **AndroidQF solicitará o tipo de backup** a ser realizado pela ferramenta:

    ** **Only** **SMS**: Executa um backup limitado que inclui apenas mensagens SMS e MMS.
    **Everything**: Executa um backup completo do dispositivo usando o adb backup.
    ** **No** **Backup**: Ignora completamente a geração de backup; extrai apenas outros artefatos via ADB.


    !!! aviso "Alternativa"

        No exemplo, usamos a opção **Only-SMS** para limitar a extração apenas a mensagens, reduzindo a exposição de dados pessoais desnecessários. Se o **contexto do caso for considerado de alto risco** ou envolver uma investigação mais sofisticada, é recomendável verificar a opção **Everything**, embora a opção **Only-SMS** na maioria dos casos ainda seja suficiente para pesquisar tentativas de phishing por SMS.


    Captura de tela do terminal Linux com o menu de backup do AndroidQF e a opção Somente SMS selecionada](.../../../../assets/04-how-to/06-captura-linux-only-sms.png "image 7")
    /// legenda
    **Imagem 6**. Captura de tela do terminal Linux com o menu de backup do AndroidQF e a opção Somente SMS selecionada.
    ///

* Ao selecionar o tipo de backup, o telefone solicitará o uso de uma **senha de criptografia temporária** para criptografar o [backup gerado pelo ADB](.../../references/00-glossary/index.md#backup-generated-by-adb). Em nosso exemplo, usamos **a senha "sd "** para segurança digital em espanhol, conforme mostrado na imagem 7.

    !!! aviso "Alternativa"

        Essa senha permite criptografar o backup gerado ao executar o androidqf. Caso você gere **senhas aleatórias**, certifique-se de usar um **gerenciador com boas práticas de backup**. Caso contrário, e se não for um risco, defina uma senha simples e equivalente para todas as suas extrações.
   
    Captura de tela do dispositivo móvel Samsung Android solicitando senha temporária para backup do sd](.../../../../../assets/04-how-to/07-capture-android-password.png "image 7")
    /// legenda
    **Imagem 7**. Captura de tela do dispositivo móvel Samsung Android solicitando a senha de backup temporário "sd".
    ///

* Selecione: **"Backup my data" **.

    Captura de tela do dispositivo móvel Samsung Android com a opção "Backup my data" selecionada](../../../../../assets/04-how-to/08-capture-android-backup-data.png "image 8")
    /// legenda
    **Imagem 8**. Captura de tela do dispositivo móvel Samsung Android com a opção "Backup my data" selecionada.
    ///

    !!! falha "Mensagens de erro esperadas".

        Ocasionalmente, erros sobre como encontrar os caminhos onde os pacotes estão localizados são encontrados com frequência, portanto, é comum ver algumas dessas marcas de erro; no entanto, **essas marcas de erro não afetam a extração de dados forenses no dispositivo.

    captura de tela do terminal Linux indicando a coleção de informações do pacote de aplicativos do AndroidQF](../../../../../assets/04-how-to/09-capture-linux-collection.png "image 9")
    /// legenda
    **Imagem 9**. Captura de tela do terminal Linux indicando a coleta de informações do pacote de aplicativos pelo AndroidQF.
    ///

* Quando o AndoridQF encontrar todos os pacotes instalados no dispositivo, ele perguntará que **tipo de cópias de aplicativos você deseja baixar; há três opções**:

    * **All**: Baixe o [APK](../../references/00-glossary/index.md#apk) de todos os aplicativos, inclusive os aplicativos do sistema.  
    ** **Only** **non-system** **packages**: Baixe apenas os APKs dos aplicativos instalados pelo usuário.  
    **Do** **not** **download** **any**: ignora completamente o download de APKs do dispositivo.


    !!! aviso "Alternativa"

        Embora nossa recomendação seja selecionar "Only non-system packages" (Somente pacotes que não sejam do sistema), a seleção depende de sua abordagem de análise e investigação, portanto, em casos com suspeita de ataques sofisticados, a opção "All" (Todos) pode ser usada.


    captura de tela do terminal Linux com o menu de cópia de pacotes do aplicativo AndroidQF e a opção Only non-system packages selecionada](../../../assets/04-how-to/10-capture-linux-copy-packages.png "image 10")
    /// legenda
    **Imagem 10**. Captura de tela do terminal Linux com o menu de cópia de pacotes de aplicativos do AndroidQF e a opção Only non-system packages selecionada.
    ///

* Quando a opção de baixar cópias de pacotes for selecionada, o **AndroidQF perguntará sobre a remoção da opção de cópias de pacotes.ar [APKs](../../references/00-glossary/index.md#apk)** assinados por desenvolvedores ou entidades confiáveis (como o Google ou o fabricante do dispositivo), a fim de reduzir o tamanho da pasta de extração.

    * Responda **"Yes "** para que, ao revisar as informações, você possa **focar a análise em pacotes potencialmente suspeitos** e economizar tempo e espaço de armazenamento.


    !!! aviso "Alternativa"

        Embora nossa recomendação seja selecionar "Yes", a seleção depende de sua abordagem de análise e investigação, portanto, em casos com suspeita de ataques sofisticados, a opção "No" pode ser usada.


    Captura de tela do terminal Linux com o menu de desvio do aplicativo de certificado confiável AndroidQF e a opção Sim selecionada](../../../assets/04-how-to/11-capture-linux-omission-applications.png "image 11")
    /// legenda
    **Imagem 11**. Captura de tela do terminal Linux com o menu padrão de aplicativos com o certificado confiável AndroidQF e a opção Yes selecionada.
    ///

**Aguarde** que todos os módulos do AndroidQF sejam executados de acordo com sua programação.

    !!! info "Process duration" (Duração do processo)
    
        **Esta etapa pode levar vários minutos**, dependendo do modelo do telefone e da quantidade de dados armazenados. O progresso é exibido linha por linha no terminal e não requer nenhuma outra intervenção, exceto no final, onde você deve pressionar Enter para concluir.

    ![Captura de tela do terminal Linux com o menu padrão do aplicativo AndroidQF trusted-certificate e a opção Yes selecionada](../../../assets/04-how-to/12-capture-screenshot-execute-correct.png "image 12")
    /// legenda
    **imagem 12**. Captura de tela do terminal Linux com informações da execução bem-sucedida da extração forense com o AndroidQF e solicitação para pressionar enter para concluir.
    ///


### :material-numeric-6-box: Verificando a extração

Depois que o AndroidQF terminar de ser executado, é importante **validar se a aquisição foi concluída corretamente**. Para fazer isso, execute as seguintes etapas:

* Se você recebeu uma extração criptografada, é necessário descriptografar essas informações primeiro. Consulte a seção sobre [criptografia de extração] (#extraction-encryption).


* Abra o arquivo command.log com um editor de texto e **procure as palavras warning ou error**. Se elas aparecerem, verifique se correspondem a falhas críticas ou eventos não relevantes.


=== "Linux / MacOS"

    Você pode usar o seguinte comando dentro da pasta de aquisição:

    ```
    grep -i "AVISO\|ERRO" command.log
    ```

    ![Captura de tela do terminal Linux com o comando grep para procurar erros no arquivo command.log gerado pelo AndoridQF.](../../../assets/04-how-to/13-screenshot-linux-terminal-linux-errors.png "image 12")
    /// legenda
    **Imagem 13**. Captura de tela do terminal Linux com o comando grep para procurar erros no arquivo command.log gerado pelo AndoridQF.
    ///
    

=== "Windows" === "Windows" === "Windows" === "Windows" === "Windows" === "Windows" === "Windows

    Abra o arquivo com o "*Notepad "*, selecione a combinação de teclas **ctrl+b** e digite ***WARNING*** ou ***ERROR*****.**

    Captura de tela do terminal Linux com o comando grep para procurar erros no arquivo command.log gerado pelo AndoridQF](../../../assets/04-how-to/14-screenshot-windows-errors.png "image 14")
    /// legenda
    **Imagem 14**. Captura de tela do Windows Notepad com a pesquisa de erros no arquivo command.log gerado pelo AndoridQF.
    ///

* Verifique a **existência do arquivo *acquisition.json*** e se seu conteúdo parece apropriado.

    Captura de tela do Sublime Text com a saída do arquivo acquisition.json gerado pelo AndoridQF](../../../../../assets/04-how-to/15-screenshot-acquisition.png "image 15")
    /// legenda
    **Imagem 15**. Captura de tela do Sublime Text com a saída do arquivo acquisition.json gerado pelo AndoridQF.
    ///

* Verifique a criação de arquivos e pastas de saída. **Certifique-se de que os seguintes arquivos e pastas tenham sido gerados:** **/// **Imagem 15**.

    ```
    ├── apks/
    ├─── logs/
    ├──── tmp/
    .json
    ├─── backup.ab
    Relatório de erros.zip
    command.log
    dumpsys.txt
    ├──── env.txt
    ├─── files.json
    getprop.txt ├───── getprop.txt
    ├─── hashes.csv
    ├─── logcat.txt
    ├─── packages.json
    ├─── processes.txt
    root_binaries.json ├─── raiz_binários.json
    selinux.txt
    ├─── services.txt
    ├─── settings_global.txt
    Configurações_seguras.txt
    └└─── settings_system.txt
    ```

    Captura de tela dos arquivos de aplicativos no PopOS! mostrando a pasta de saída dos arquivos e diretórios gerados com a extração forense com o AndroidQF.](../../../assets/04-how-to/16-screenshot-files-output.png "image 15")
    /// legenda
    **imagem 16**. Captura de tela do aplicativomostrando a pasta de saída dos arquivos e diretórios gerados pela extração forense com o AndroidQF.
    ///

## Conclusão

O AndroidQF permite que você adquira e extraia evidências forenses de dispositivos Android. É uma **ferramenta amplamente utilizada por laboratórios da sociedade civil**, devido à sua praticidade, simplicidade e portabilidade. Neste guia, detalhamos o passo a passo a ser seguido para realizar extrações usando Windows, MacOS ou Linux.

A extração de possíveis evidências é uma das **[primeiras etapas de uma investigação forense](../../explainers/01-explainer-introduction-digital-forensics/index.md#what-are-the-stages-of-a-forensic-investigation)** e é fundamental para iniciar uma triagem. A partir dessas informações extraídas, é possível iniciar um estágio de análise, seja manualmente ([você pode consultar o dicionário de arquivos aqui](../../references/01-reference-androidqf-dictionary/) ou usando uma ferramenta como o [MVT](https://docs.mvt.re/en/latest/).

Se quiser contribuir para o desenvolvimento, a tradução ou a disseminação desse recurso ou de outros recursos, **consulte nossa [seção da comunidade](../../community/)** para obter mais informações.


## Comentários

Você tem **comentários ou sugestões** sobre este recurso? Você pode usar a função **comentário abaixo** para nos deixar suas ideias ou comentários. Certifique-se de seguir nosso [código de conduta](../../community/code-of-conduct/). A função de comentário está vinculada diretamente à seção [_Discussions_ do Github] (https://github.com/Socialtic/forensics/discussions), onde você também pode **participar diretamente das discussões**, se preferir.   


