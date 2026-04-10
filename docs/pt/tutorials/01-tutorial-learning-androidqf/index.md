---

title: Tutorial - Explorando AndroidQF para la adquisición de información en Android
summary: Explorando AndroidQF para la adquisición de información en Android
keywords: triage, android, bugreport, 
lang: es
tags: [how-to, intro]
last_updated: 2025-08-18
some_url:
created: 2025-08-18
comments: true
name: jose

translation-review-pending: true
---

# Tutorial - Explorando o AndroidQF para aquisição de informações no Android

Este documento é **parte de um repositório de documentação técnica** que visa estabelecer uma base de conhecimento comprovada, flexível e acessível para **promover a análise forense consensual em benefício da sociedade civil**. Para organizar o conteúdo, é usada a [estrutura de referência da documentação técnica Diataxis](../../references/00-glossary/index.md#diataxis).

Esse recurso específico se enquadra na categoria [tutoriais](https://diataxis.fr/tutorials/) e contém atividades práticas guiadas para se familiarizar com uma extração forense por meio da ferramenta [AndroidQF](https://github.com/mvt-project/androidqf).

Este tutorial tem como objetivo ensinar de forma prática, clara e acessível como usar o AndroidQF** para realizar extrações forenses em dispositivos Android, destacando sua utilidade em contextos de análise de ameaças e incidentes que afetam defensores de direitos humanos, jornalistas e organizações da sociedade civil.


!!! dica "Como seguir este tutorial?"

    Este tutorial foi concebido para ser um **recurso de aprendizado**, portanto, alguns conceitos são explorados em profundidade, mostrando também alternativas e possibilidades. Se estiver procurando um guia conciso, com instruções passo a passo para concluir uma extração, consulte nosso [guia para aquisição com androidqf.](../../how-tos/04-how-to-extract-with-androidqf/)
    
    Recomenda-se que você reserve pelo menos **90 minutos para a varredura inicial**, especialmente se você não tiver experiência anterior com a ferramenta.

## Requisitos para seguir este tutorial

Para concluir este tutorial, é **indispensável** ter os seguintes itens:

* Um **dispositivo Android**. O dispositivo deve estar funcionando e você deve saber a senha, o PIN ou o padrão de desbloqueio; ele deve ter a **depuração USB ativa**.

    !!! pergunta "Como ativar a depuração USB".

        Se o dispositivo não tiver essa configuração ativa, você precisará primeiro seguir as etapas em [How to enable developer options on different Android devices](../../how-tos/02-how-to-enable-developer-options/) e, em seguida, seguir as etapas em [How to enable ADB (debugging over USB) on different Android devices](../../how-tos/03-how-to-enable-adb/).

* Um **computador** com um sistema operacional Windows, Linux ou macOS recente.

* Cabo USB para **transferência de dados** em boas condições.

    !!! informação "Nem todos os cabos USB são iguais".

        Alguns cabos USB não têm as conexões necessárias para transferir dados entre o dispositivo móvel e o computador. Esses cabos são úteis para carregar o dispositivo, mas não funcionam para a transferência de dados. Para remoção, certifique-se de usar um cabo que possa transferir dados. É [difícil distinguir à primeira vista] (https://support.konnected.io/how-to-tell-a-usb-charge-only-cable-from-a-usb-data-cable), mas geralmente os cabos de carregamento rápido ou aqueles incluídos nos dispositivos são cabos de dados.

## Sobre o AndroidQF

O [AndroidQF](https://github.com/mvt-project/androidqf) é uma ferramenta de software gratuita e de código aberto **focada na extração forense de dispositivos Android**. Faz parte do [MVT Project](https://github.com/mvt-project/), inicialmente desenvolvido por [Claudio Guarnieri](https://nex.sx/) e atualmente mantido pelo [Amnesty International Security Lab](https://securitylab.amnesty.org/es/).

Seu nome vem de *Android Quick Forensics*, e seu projeto e desenvolvimento se concentram em **facilitar a aquisição de informações para análise forense consensual** em um contexto de sociedade civil.

O AndroidQF é destacado nos grupos técnicos que realizam extrações como uma **[ferramenta portátil] fácil de usar(../../references/00-glossary/index.md#portable-tool], pois pode ser executado no Windows, Linux e macOS** por meio de binários pré-compilados.

### O que o AndroidQF faz em nível técnico?

Tecnicamente, o AndroidQF é um [wrapper](https://developer.mozilla.org/en-US/docs/Glossary/Wrapper) forense no [ADB](../../references/00-glossary/index.md#adb), o que significa que ele automatiza os comandos do ADB empacotados em [modules](https://github.com/mvt-project/androidqf/tree/main/modules) que executam operações específicas e seguem um fluxo específico.

Alguns dos componentes gerais do AndroidQF são:

* **Interface de execução ** Exibe uma interface de linha de comando com a qual a pessoa interage e gera o registro de todas as atividades durante a execução.  
* Gerenciamento de módulos** Trata do fluxo de execução específico de cada módulo.  
* Extração forense ** Realiza a aquisição de dados forenses usando uma interface de linha de comando.adb.

### Por que ele é útil para a análise forense na sociedade civil?

Seu design permite **extrações rápidas e seguras de dispositivos Android**, sem a necessidade de ferramentas comerciais ou configurações avançadas.

Isso o torna uma ferramenta acessível e confiável para investigadores, defensores de direitos humanos, jornalistas e laboratórios de análise forense digital, especialmente porque:

* Pode ser usado de forma portátil** sem a necessidade de instalação complexa.  
* O **controle das informações forenses é local** e nenhum dado é compartilhado por meio de um serviço da Web ou de nuvem.
* Sua modularidade **permite que você decida exatamente quais dados obter**, dependendo do nível de risco de uma pessoa.  
* A ferramenta e sua documentação se enquadram na categoria de **software livre e de código aberto**, portanto, seu código-fonte é transparente e pode ser pesquisado por qualquer pessoa interessada em saber como a ferramenta funciona.

A facilidade de saber quais informações forenses foram extraídas e qual foi o processo permite maior transparência e confiança no processo, reduzindo assim os riscos técnicos e éticos da análise forense consensual.

Como complemento a este tutorial, este repositório contém um [Dicionário de arquivos gerados pela ferramenta androidqf](../../references/01-reference-androidqf-dictionary/index.md), um material de referência que contém **informações sobre os arquivos gerados**, como usá-los, onde procurar informações específicas e em que formato você as encontrará.

## Revisão das configurações no dispositivo Android

Para iniciar este tutorial, é importante **confirmar as configurações necessárias no dispositivo Android e no computador**, isso garantirá que haja uma boa transmissão de informações entre os dispositivos ao realizar a extração forense.

Com a depuração USB ativada, é hora de **conectar o dispositivo móvel ao computador** por meio do cabo de transferência de arquivos. Ao conectar o telefone, selecione **permitir** quando o dispositivo Android **pedir permissão para acessar os dados do dispositivo**.

Captura de tela do dispositivo móvel Android Samsung solicitando permissões de acesso aos dados](../../../../../assets/01-tutorial/01-capture-android-data-permissions.png "image 1")
/// legenda
**Imagem 1**. Captura de tela do dispositivo móvel Samsung Android solicitando permissão de acesso a dados.
///
    
Em seguida, verifique no painel de notificações se o dispositivo está conectado no modo **USB para transferir arquivos** (veja a imagem 2). Para isso, clique na notificação do sistema Android e selecione *USB para transferir arquivos/Android Auto* (veja a imagem 3). Se nenhuma notificação for exibida, você poderá verificar as **configurações de USB** no menu de configurações do dispositivo, verificando se a opção _Transferência de arquivos_ está ativada.

Captura de tela do painel de notificações no dispositivo móvel Android](../../../../../assets/01-tutorial/02-capture-android-notifications-panel.png "image 1")
/// legenda
**Imagem 2**. Captura de tela do painel de notificações no dispositivo móvel Android.
///

Captura de tela do dispositivo móvel Android com configurações para usar USB para transferir arquivos](../../../assets/01-tutorial/03-capture-android-settings-usb.png "image 1")
/// legenda
**Imagem 3**. Captura de tela do dispositivo móvel Android com configurações para usar o USB para transferir arquivos.
///

## Obtendo o AndroidQF

Esta seção detalha **como fazer o download do binário e preparar o seu computador** para executar o AndroidQF. Além disso, para se aprofundar no ajuste do binário e **explorar uma alternativa**, são mostradas as etapas para compilar seu próprio binário em um sistema Linux.

### Baixe e instale o AndroidQF de seu repositório oficial.

Para começar, você precisa baixar o [binário] do AndroidQF(../../references/00-glossary/index.md#binary) de seu [repositório oficial do GitHub] (https://github.com/mvt-project/androidqf/releases/).

É importante observar que o download correto do binário **depende da arquitetura do seu processador e do sistema operacional**. Aqui estão os detalhes para os sistemas operacionais Windows e Linux/MacOS.


!!! informações "Disponibilidade do Windows".

    O repositório oficial do AndroidQF só tem o binário do Windows para uma arquitetura amd64, portanto, se a sua **arquitetura do Windows for arm, você não poderá continuar com este tutorial**, a menos que tenha um sistema operacional **Linux ou macOS** particionado ou virtualizado em seu computador.


=== "Linux e MacOS"

    No Linux e no macOS: abra o terminal e digite *uname \-m*. A saída desse comando informará a arquitetura do seu processador (x86 ou arm64). A Figura 4 mostra um exemplo em um sistema Linux..

    Captura de tela do terminal Linux com a saída do comando *uname command-m.*](../../../assets/01-tutorial/04-capture-linux-command-uname.png "image 1")
    /// legenda
    **Imagem 4**. Captura de tela do terminal Linux com a saída do comando *uname.
    ///

    Dependendo dessa saída, baixe o binário correspondente da lista de downloads do [repositório oficial do AndroidQF] (https://github.com/mvt-project/androidqf/releases/). A Figura 5 mostra a lista de downloads.

    Captura de tela da lista de downloads do androidqf no repositório oficial do github](../../../../../assets/01-tutorial/05-screenshot-repository-downloads-androidqf.png "image 1")
    /// legenda
    **Imagem 5**. Captura de tela da lista de downloads do androidqf no repositório oficial do github.
    ///

    A imagem 6 mostra o arquivo baixado, neste caso específico, a versão 1.7.0. A versão pode variar à medida que forem feitas atualizações na ferramenta.

    Imagem de referência do download do binário do AndroidQF versão 1.7.0 para o sistema Linux amd64](../../../../../assets/01-tutorial/06-capture-screenshot-download-binary-androidqf.png "image 1")
    /// legenda
    **Imagem 6**. Imagem de referência do download do binário do AndroidQF versão 1.7.0 para o sistema Linux amd64.
    ///

    Opcionalmente, você pode mover o binário baixado para uma pasta dedicada à ferramenta ou para uma pasta onde você realiza extrações forenses, embora possa manter o binário na pasta de download.   

    Captura de tela do terminal do Linux com a execução do comando *mv* para mover o binário baixado](../../../../assets/01-tutorial/07-capture-linux-command-mv.png "image 1")
    /// legenda
    **Imagem 7**. Captura de tela do terminal do Linux com a execução do comando *mv* para mover o binário baixado
    ///

    Depois de ter o binário na pasta de sua escolha, você precisa atribuir permissões de execução ao AndroidQF, usando o comando mostrado na imagem 8:

    ````shell
    chmod +x ./androidqf-XXX
    ```

    captura de tela do terminal Linux com a execução do comando *chmod +x* para adicionar permissões de execução ao binário](../../../../../assets/01-tutorial/08-capture-linux-permissions-execution-andoridqf.png "image 1")
    /// legenda
    **Imagem 8**. Captura de tela do terminal do Linux com a execução do comando *chmod \+x* para adicionar permissões de execução ao binário
    ///


=== "Windows"

    Conforme mencionado acima, para os sistemas operacionais Windows **apenas um binário está disponível**, que terá um nome semelhante a _androidqf_v1.7.0_windows_amd64_signed.exe_. Para obter o AndroidQF, você deve fazer o download desse arquivo. A Figura 9 mostra uma pasta com o binário baixado (arquivo _.exe_).
    

    Captura de tela do explorador de arquivos do Windows com a pasta binária na pasta onde a extração forense será salva](../../../assets/01-tutorial/09-capture-windows-explorer-binary-andoridqf.png "image 1")
    /// legenda
    **Imagem 9**. Captura de tela do explorador de arquivos do Windows com a pasta binary na pasta em que a extração forense será salva.
    ///

    Opcionalmente, você pode mover o binário baixado para uma pasta dedicada à ferramenta ou para uma pasta onde você realiza extrações forenses, embora possa manter o binário na pasta de download.

!!! falha "Conflitos com antivírus".

    Caso seu computador Windows ou macOS tenha algum **antivírus** instalado, é possível que esse software impeça e interrompa o download e a execução do AndroidQF. Portanto, caso você tenha problemas com o download ou a execução, recomendamos que você **desabilite-o temporariamente**. Alguns softwares antivírus podem identificar o binário do AndroidQF como uma ameaça e aplicar regras de segurança em sua execução.
    
    Se você tiver o **Windows Defender, não precisará desativá-lo**.

### Alternativa: compilação do binário do AndroidQF para Linux

Além disso, neste tutorial, apresentamos a alternativa de **compilar o binário do AndroidQF** para Linux. Essa opção lhe dá a possibilidade de gerar o binário diretamente em seu sistema e evitar depender apenas dos binários publicados nas versões oficiais. Essa **não é uma etapa obrigatória**, mas permite que você entenda como usar o repositório de código para gerar o arquivo executável passo a passo.

Se não quiser explorar a compilação ou se estiver usando uma máquina Windows, continue o tutorial na seção [explore-and-run-androidQF](#explore-and-run-androidqf).

!!! Dica "Integridade binária do AndroidQF".

    A compilação do projeto a partir do código-fonte também lhe dá a vantagem de verificar a integridade do software, tendo o binário construído a partir do zero e o binário construído a partir do zero.Verifique as atualizações mais recentes do código-fonte da ferramenta e certifique-se de que o binário esteja adaptado ao seu próprio ambiente de trabalho.

**Etapa 1 - Atualizar o sistema

Use o gerenciador de pacotes para garantir que tudo esteja atualizado.

````shell
sudo apt update && sudo apt upgrade -y
```

**Etapa 2 - Instalar as dependências necessárias

Go 1.23, make, git, unzip e wget. É importante não usar a versão do Go incluída nos repositórios, pois ela é antiga.

Se você tiver uma instalação anterior, remova-a com:

````shell
sudo apt remove --purge -y golang-go golang
sudo rm -rf /usr/local/go
```

Agora, baixe e instale a versão oficial do Go. Neste exemplo, estamos usando a versão 1.23, mas você precisa **baixar a versão mais recente**.

````shell
cd /tmp
wget https://go.dev/dl/go1.23.1.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.23.1.linux-amd64.tar.gz
```

Adicione o Go ao PATH para que o sistema o reconheça:

````shell
export PATH=/usr/local/go/bin:$PATH
```

Depois de fazer isso, é recomendável confirmar a versão do Go instalada

````shell
versão do go
```

**Etapa 3 - Clonar o repositório

Com o ambiente pronto, o repositório oficial do AndroidQF é clonado do GitHub e inserido na pasta de download.

````shell
cd ~
git clone https://github.com/mvt-project/androidqf.git
cd androidqf
```

**Etapa 4 - Compilar o binário

Dentro do projeto, a primeira coisa a fazer é compilar o módulo coletor, que é responsável pela execução em dispositivos Android durante a extração.

````shell
make collector
```

Aguarde até que a construção do coletor seja concluída, conforme mostrado na figura 10.

Captura de tela do terminal Linux com a execução do comando build collector](.../.../.../assets/01-tutorial/10-capture-linux-make-collector.png "image 1")
/// legenda
**Imagem 10**. Captura de tela do terminal do Linux com a execução do comando *build collector.*.
///

A versão Linux do AndroidQF é então compilada usando a instrução, conforme mostrado na Figura 11.

````shell
make linux
```

captura de tela do terminal Linux com execução do comando *make linux.*](../../../../../assets/01-tutorial/11-captura-linux-builder-done.png "image 1")
/// legenda
**Imagem 11**. Captura de tela do terminal do Linux com a execução do comando *make linux.*.
///

Quando a compilação é concluída, os binários são gerados dentro da pasta *build*. Você pode listar a pasta e confirmar a compilação dos binários com o seguinte comando, conforme mostrado na figura 12:

````shell
ls build/
```

Captura de tela do terminal Linux com a execução do comando ls build/.](../../../assets/01-tutorial/12-captura-linux-ls-build.png "image 1")
/// legenda
**Imagem 12**. Captura de tela do terminal do Linux com a execução do comando *ls build/.*.
///

Para verificar se tudo correu bem, você pode passar para a próxima seção, que abordará a exploração dessas ferramentas.

### Criptografia de extrações (opcional)

Ao realizar uma extração de dados forenses de um dispositivo, são coletadas informações privadas, pois o AndoridQF pode gerar backups de mensagens SMS, listar os aplicativos instalados em um dispositivo ou mostrar os caminhos em que a extração foi realizada, revelando o nome ou o pseudônimo da pessoa que realizou o procedimento, Por isso, o envio dessas informações sem criptografia pode expor a pessoa que está sendo acompanhada no processo de extração, bem como o acompanhante, o que, em alguns contextos, pode comprometer a segurança digital ou física de uma pessoa.

Nesses cenários, o AndroidQF oferece uma alternativa de criptografia automática usando [chaves de criptografia AGE] (https://github.com/FiloSottile/age) em uma extração a ser realizada.

Usando essa alternativa de criptografia, o AndroidQF pode detectar uma chave pública com a qual ele primeiro comprime a extração para .zip, depois criptografa o arquivo com *AGE* e remove a extração não criptografada, resultando em um arquivo no formato: **.zip.age**.

Se você for uma pessoa que vai realizar uma extração em nome de uma organização ou de outro analista e vai usar a chave dele para criptografar extrações, siga estas etapas:** **.

* Solicite a chave pública correspondente do analista ou usuário que planeja descriptografar essas informações.  
    * Verifique se a chave começa com *age1...*.

* Crie um arquivo *.txt* chamado **key** no diretório em que o binário do AndroidQF está localizado.
    * Coloque a chave pública nesse arquivo e salve as alterações.

É importante mencionar que, depois que as informações dessa extração forem criptografadas, somente a pessoa que tiver a chave privada poderá descriptografar essas informações.

**Se você for um analista ou a pessoa que receberá as informações das extrações**, como primeira etapa, deverá fazer o download e instalar o *age*, a [documentação oficial] (https://github.com/FiloSottile/age) menciona o cocomandos necessários para diferentes sistemas operacionais e manipuladores de pacotes, como *apt*, por exemplo:

````shell
apt install age
```

Além disso, essa mesma documentação menciona o uso de binários pré-compilados e a funcionalidade completa dessa ferramenta de criptografia.

Para os fins deste tutorial, você só precisa gerar um par de chaves, uma chave pública (aquela com a qual você compartilha e criptografa os dados) e uma chave privada (aquela com a qual você descriptografa os dados), usando o seguinte comando:

````shell
age-keygen -o my-key.txt
```

A saída criará o arquivo *my-key.txt*, que conterá o registro de data e hora da criação da chave, a chave pública e a chave privada.

Para criptografar as extrações, você precisa seguir as etapas abaixo:

* Crie um arquivo *.txt* chamado **key** no diretório em que o binário do AndroidQF está localizado e mantenha-o aberto.
* Abra o arquivo *my-key.txt* e copie a chave pública que começa com: *age1...*.
* Cole a chave no arquivo *key.txt* e salve as alterações feitas
* Compartilhe essa chave com qualquer pessoa que precise criptografar extrações ou use-a ao gerar extrações com o AndroidQF.

**Se for você quem descriptografa as informações**, siga as etapas abaixo:

* Crie um arquivo *.txt* chamado **private.key** no diretório em que o binário do AndroidQF está localizado e mantenha-o aberto.
* Abra o arquivo *my-key.txt* e copie a chave privada que começa com: *AGE-SECRET-KEY-...*...*.
* Cole a chave no arquivo *private-key.txt* e salve as alterações feitas
* Execute o seguinte comando para descriptografar as informações:

    ````shell
    $ age --decrypt -i ~/path/to/privatekey.txt -o <UUID>.zip <UUID>.zip.age
    ```
Embora esse processo de criptografia seja opcional, recomenda-se que ele seja considerado para reduzir os [riscos potenciais](../../explainers/02-explainer-risks-threats/index.md).

## Verificação e execução do AndroidQF

### Verificação do AndroidQF

Nesta seção, vamos explorar o AndroidQF para conhecer os parâmetros de execução que a ferramenta possui. **Compreendê-los permitirá que você controle e personalize o tipo de extração forense que deseja realizar**, esses parâmetros fazem parte dos comandos que orientam a ferramenta a funcionar corretamente.

O AndroidQF integra uma lista completa de parâmetros disponíveis por meio de seu parâmetro *help* (ou sua forma abreviada *h*). Isso funciona no Linux, macOS e Windows usando o seguinte comando:

````shell

./androidqf_vXXX_ --help
```

=== "Comando de ajuda no Linux/MacOS"

    Exemplo do Linux:

    ![ captura de tela do terminal linux com execução do parâmetro *-help*](../../../assets/01-tutorial/13-capture-androidqf-help.png "image 1")
    /// legenda
    **Imagem 13**. Captura de tela do terminal Linux com execução do parâmetro *-help*.
    ///

=== "Comando de ajuda do Windows

    Exemplo no Windows:

    Na pasta em que você salvou o binário do AndroidQF, clique com o botão direito do mouse e selecione a opção Abrir no terminal, conforme mostrado na imagem 14:

    ![ Captura de tela da pasta do Windows com o menu direito ativo e a opção *abrir no terminal* identificada](../../../../assets/01-tutorial/14-capture-windows-open-terminal.png "image 1")
    /// legenda
    **Imagem 14**. Captura de tela da pasta Windows com o menu direito ativo e a opção *abrir no terminal* identificada.
    ///

    Uma vez no terminal, você pode executar o comando com o parâmetro *-help*, conforme mostrado na imagem 15.

    Captura de tela do terminal do Windows Powershell com o parâmetro *-help* executado](../../../../../assets/01-tutorial/15-captura-windows-androidqf-help.png "image 1")
    /// legenda
    **Imagem 15**. Captura de tela do terminal do Windows Powershell com o parâmetro *-help* executado.
    ///

Isso mostra um menu de ajuda no terminal com todos os parâmetros disponíveis. Os mais importantes ao realizar uma extração forense são os seguintes:

* *\-s*: Se você tiver vários dispositivos conectados, poderá usar esse parâmetro para especificar o dispositivo a ser analisado.

=== "Identify devices in Linux/MacOS" (Identificar dispositivos no Linux/MacOS).

    No macOS e no Linux, você pode listar os dispositivos com o adb. Deixamos este guia sobre [How to install ADB on macOS and Linux] (https://www-xda--developers-com.translate.goog/install-adb-windows-macos-linux/?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc).
	  
	O comando para listar os dispositivos no macOS e no Linux é:

    ````shell
    dispositivos adb
    ```

    O resultado é mostrado na Figura 16.

    Captura de tela do terminal Linux com execução do comando *adb devices](../../../../../assets/01-tutorial/16-capture-linux-adb-devices.png "image 1")
    /// legenda
    **Imagem 16**. Captura de tela do terminal Linux com execução do comando *adb devices.*.
    ///

=== "Identificar dispositivos no Windows

    No caso do Windows, quando você executa o comando bNo diretório AndroidQF pela primeira vez, o executável ADB é criado e pode ser usado para listar os dispositivos:

    ````shell
    .\adb.exe devices
    ```
    
    O resultado é mostrado na Figura 17.

    Captura de tela do terminal do Windows PowerShell com a execução do executável *adb* e do parâmetro *devices.*](../../../assets/01-tutorial/17-capture-windows-adb-devices.png "image 1")
    /// legenda
    **Imagem 17**. Captura de tela do terminal do Windows PowerShell com a execução do executável *adb* e o parâmetro *devices.*.
    ///


    Depois que os dispositivos conectados são identificados, é possível adicionar o número de série usando o parâmetro -s, conforme mostrado na imagem 18.

    ````shell
    ./androidqf -s número-de-série
    ```

    Captura de tela do terminal Linux com integração do parâmetro *\-s*.](../../../../../assets/01-tutorial/18-capture-androidqf-serial-number.png "image 1")
    /// legenda
    **Imagem 18**.  Captura de tela do terminal Linux com integração do *s-parameter*.
    ///


\-o: permite especificar uma saída ou pasta de saída onde os arquivos extraídos serão salvos.  

    Se nenhuma pasta de saída ou de saída for especificada, o AndroidQF identificará o dispositivo assim que ativar a depuração USB e gerará uma pasta com um identificador exclusivo (UUID). Essa pasta armazenará a extração. O nome dessas pastas sendo um UUID geralmente tem nomes como 0caba18f-20a7-48d0-b9ba-724fdaa3ff85 ou a577ae94-0a47-479c-82c5-c8017bfb7175.

    Como exemplo neste tutorial, o parâmetro *\-o* é usado para definir a pasta de saída da extração em vez de permitir que o AndroidQF gere um UUID. Dessa forma, o comando criará uma pasta com um nome mais legível, que combina a data no formato ano-mês-dia com um texto de identificação adicional, que neste exemplo chamaremos de *acquisition01*.

    ````shell
    ./androidqf -s numero-serial -o "$(date +%Y-%m-%d)"-identifier
    ```

    Captura de tela do terminal Linux com integração do parâmetro *\-o*.](../../../../../assets/01-tutorial/19-capture-andoridqf-output.png "image 1")
    /// legenda
    **Imagem 19**.  Captura de tela do terminal Linux com integração do parâmetro *\-o*.
    ///


* * "verbose" ou "v": opcionalmente, você pode ativar o modo detalhado. O terminal exibirá informações em tempo real sobre o processo, úteis para depuração. Essas informações são as mesmas armazenadas no arquivo [*command.log*] (https://forensics.socialtic.org/references/01-reference-diccionario-androidqf/01-reference-diccionario-androidqf.html#commandlog) gerado automaticamente após cada execução.

    ````shell
    ./androidqf -s serial-number -o "$(date +%Y-%m-%d)"-complement-optional -v
    ```

    captura de tela do terminal Linux com integração do parâmetro *\-o*](../../../../../assets/01-tutorial/20-capture-androidqf-verbose.png "image 1")
    /// legenda
    **Imagem 20**.  Captura de tela do terminal Linux com integração do parâmetro *\-v*.
    ///



### Executando o AndroidQF

Antes de executar o binário do AndoridQF, ligue e desbloqueie o dispositivo móvel que você já conectou ao computador.

Primeiro, caso você use [encryption] (#encryption-of-extractions-optional), certifique-se de que a chave de criptografia esteja na pasta correspondente ao lado do binário do AndoridQF.

Além disso, independentemente do sistema operacional usado no computador, primeiro você precisa identificar os parâmetros do comando de execução do AndroidQF de acordo com as necessidades da sua análise. Para este exemplo, usamos o seguinte comando:

!!! nota "Nota sobre o exemplo".

    Para este tutorial, será abordado o comando que identifica o dispositivo pelo número de série e com saída de pasta com data e identificador. A versão detalhada será omitida para facilitar a leitura.

````shell
./androidqf -s serial-number -o /path/output/"$(date +%Y-%m-%d)"-complement # (1)!
```

Usamos os parâmetros **-s** para indicar o número de série e **-o** para especificar o caminho de saída. Também usamos o comando **date** para incluir automaticamente a data no nome da pasta.

=== "Execução no Linux/MacOS"

    Para executar o AndroidQF em um sistema Linux/MacOS, devemos abrir um terminal no local em que armazenamos o binário e executar o comando apresentado acima.  

    ````shell
    ./androidqf -s serial-number -o /path/output/"$(date +%Y-%m-%d)"-acquisition01
    ```

    A Figura 21 mostra um exemplo de saída em um sistema Linux.

    Captura de tela do terminal Linux com execução de comando pronta](../../../../../assets/01-tutorial/21-capture-linux-execution-andoridqf.png "image 1")
    /// legenda
    **Imagem 21**.  Captura de tela do terminal Linux com o comando run pronto.
    ///

=== "ExecuteWindows'.

    Para iniciar a execução no Windows, é possível usar o terminal ou o explorador de arquivos.

    === "Terminal

        Com o terminal aberto na pasta em que o binário do AndoridQF está localizado, execute o binário usando o comando com os parâmetros necessários de acordo com sua análise (semelhante ao caso do Linux e do macOS)

        ````shell
        ./androidqf.exe -s numero-serial -o "$(Get-Date -Format 'yyyy-MM-dd')-acquisition01
        ```

        Captura de tela do terminal do Windows PowerShell com o comando de execução pronto](../../../../assets/01-tutorial/22-capture-windows-ejecuion-androidqf-terminal.png "image 1")
        /// legenda
        **Imagem 22**. Captura de tela do terminal do Windows PowerShell com o comando run pronto.
        ///

    === "File Explorer

        Na pasta em que o binário foi salvo, o binário pode ser executado com um clique duplo.

        Captura de tela do explorador de arquivos com a pasta de download do binário androidqf](../../../../assets/01-tutorial/23-capture-windows-ejecuion-androidqf-interface.png "image 1")
        /// legenda
        **Imagem 23**. Captura de tela do explorador de arquivos com a pasta de download do binário androidqf.
        ///
    
    
    Depois de executar o binário, você receberá uma mensagem de **proteção do Windows** informando que o sistema evitou executar o aplicativo para evitar riscos; no entanto, como o AndroidQF é uma ferramenta gratuita e de código aberto com melhorias constantes, não há distribuição comercial.

    Para isso, clique em **"Mais informações "**.

    Captura de tela da janela pop-up de proteção do Windows](../../../assets/01-tutorial/24-capture-windows-protection.png "image 1")
    /// legenda
    **Imagem 24**. Captura de tela da janela pop-up de proteção do Windows.
    ///

    Selecione **"Run anyway "**.

    Captura de tela da janela pop-up de proteção do Windows com a seleção de *Executar mesmo assim*.](../../../../../assets/01-tutorial/25-capture-windows-run.png "image 25")
    /// legenda
    **imagem 25**. Captura de tela da janela pop-up de proteção do Windows com a seleção *Executar mesmo assim*.
    ///

### Considerações durante a execução

!!! info "Etapas equivalentes para todos os sistemas".

    As próximas etapas serão aplicadas da **mesma forma** nos 3 sistemas operacionais considerados neste tutorial: **Linux, Windows e macOS.**.

Esta seção aborda as ações e considerações **após o início da execução**, ou seja, assim que executarmos o comando mostrado na seção anterior.

Quando a execução é iniciada, é necessário realizar algumas configurações no terminal e outras no dispositivo Android. Essas configurações são sequenciais, portanto, é **recomendável estar ciente do processo de execução da extração**; essas configurações são mencionadas explicitamente abaixo:

1. **:material-cellphone-basic: - no telefone:** Quando a mensagem ***Enable USB debugging?*** aparecer, clique em ***"Always allow from this computer "*** e depois em ***"OK "*** ou ***"Allow "***.  

    Captura de tela do dispositivo móvel Samsung Android solicitando depuração e permissão de confiança para o computador transferir arquivos](../../../../assets/01-tutorial/26-captura-android-permiso-depuracion.png "imagen 1")
    /// legenda
    **Imagem 26**. Captura de tela do dispositivo móvel Android Samsung solicitando permissão de depuração e confiança do computador para transferir arquivos.
    ///


2. **:octicons-terminal-16: - no terminal:** O AndroidQF solicitará o tipo de backup que a ferramenta executará:

    ** **Only** **SMS**: Executa um backup limitado que inclui apenas mensagens SMS e MMS.  
    ** **Everything**: Executa um backup completo do dispositivo por meio do backup adb.  
    ** **No** **Backup**: Ignora completamente a geração de backup; extrai apenas outros artefatos via ADB.
	  
    !!! nota "Nota"

        No exemplo, usamos a opção **Only-SMS** para limitar a extração apenas a mensagens, reduzindo a exposição de dados pessoais desnecessários. Se o contexto do caso for considerado de alto risco ou envolver uma investigação mais sofisticada, é recomendável verificar a opção **Everything**, embora a opção **Only-SMS** na maioria dos casos ainda seja suficiente para procurar tentativas de phishing por SMS.

    Captura de tela do terminal Linux com o menu de backup do AndroidQF e a opção *Only-SMS* selecionada](../../../../assets/01-tutorial/27-captura-linux-only-sms.png "image 1")
    /// legenda
    **Imagem 27**. Captura de tela do terminal Linux com o menu de backup do AndroidQF e a opção *Only-SMS* selecionada.
    ///


3. **:material-cellphone-basic: - noQuando você selecionar o tipo de backup, o telefone solicitará que você use uma senha de criptografia temporária para o backup. Em nosso exemplo, usamos **a senha "sd "** para segurança digital em espanhol,**** conforme mostrado na Figura 28.

    !!! observe "Sobre a definição de senhas para o backup" !!! observe "Sobre a definição de senhas para o backup".

        Nesta etapa, a ferramenta solicita uma senha para a criptografia do backup. Para este exemplo, usaremos a senha "sd" para segurança digital.

        Dependendo do contexto e do caso, você pode escolher a senha apropriada, embora, se realizar extrações contínuas, possa usar a mesma senha como prática interna do seu computador.

        Embora a reutilização de senhas não seja uma prática de segurança digital recomendada, é importante considerar o contexto e lembrar que essa senha protegerá apenas um dos arquivos incluídos na extração forense. No entanto, os outros arquivos coletados não serão criptografados, portanto, independentemente da senha usada, devemos tratar a pasta de extração como informação confidencial e armazená-la somente em mídia com medidas e padrões de proteção adicionais, de acordo com nossa política interna de manuseio e proteção de informações.

    Captura de tela do dispositivo móvel Samsung Android solicitando a senha de backup temporário "sd"](../../../../../assets/01-tutorial/28-capture-android-password.png "image 1")
    /// legenda
    **Imagem 28**. Captura de tela do dispositivo móvel Samsung Android solicitando a senha temporária de backup.
    ///


4. **:material-cellphone-basic: - no telefone:** Em seguida, selecione o botão**: "Backup my data "**.

    Captura de tela do dispositivo móvel Samsung Android com a opção "Backup my data" selecionada](../../../../../assets/01-tutorial/29-capture-android-backup-data.png "image 1")
    /// legenda
    **Imagem 29**. Captura de tela do dispositivo móvel Samsung Android com a opção "Backup my data" selecionada.
    ///

    No :octicons-terminal-16:: Neste momento, o AndroidQF estará realizando o backup e coletando as informações do backup e as informações dos aplicativos (pacotes) instalados no dispositivo.

    !!! aviso "Path errors".

        Em algumas ocasiões, costumam aparecer erros sobre a pesquisa dos caminhos onde os pacotes estão localizados, por isso é comum ver algumas dessas marcas de erro, no entanto, **essas marcas de erro não afetam a extração de dados forenses no dispositivo.***.

    captura de tela do terminal Linux mostrando o AndroidQF coletando informações do pacote do aplicativo](../../../../../assets/01-tutorial/30-capture-linux-package-collection.png "image 1")
    /// legenda
    **Imagem 30**. Captura de tela do terminal Linux mostrando o AndroidQF coletando informações do pacote do aplicativo.
    ///

5. **:octicons-terminal-16: - no terminal:** Quando o AndoridQF encontrar todos os pacotes instalados no dispositivo, ele perguntará que tipo de cópia dos aplicativos você deseja fazer; há 3 opções:

    * **All**: Baixe os APKs de todos os aplicativos, inclusive os do sistema.
    Only** **Only** **non-system** **packages**: Baixar somente os APKs dos aplicativos instalados pelo usuário.
    Do** ** **not** ** **download** **any**: ignora completamente o download de APKs do dispositivo.

	  
	A recomendação, neste momento, é que os analistas baixem somente os pacotes que não sejam do sistema para permitir uma análise mais aprofundada de comportamento malicioso, modificações, rastreadores etc.

    Observação: "Qual opção é a ideal?"

        Embora nossa recomendação seja selecionar "Only non-system packages", a seleção depende de sua abordagem de análise e investigação, portanto, em casos com suspeita de ataques sofisticados, a opção "All" pode ser usada.* !!!!

    Captura de tela do terminal Linux com o menu de cópia de pacotes do aplicativo AndroidQF e a opção "*Only non-system packages "* selecionada](../../../assets/01-tutorial/31-capture-linux-copy-packages.png "image 1")
    /// legenda
    **Imagem 31**. Captura de tela do terminal Linux com o menu de cópia de pacotes do aplicativo AndroidQF e a opção "*Only non-system packages "* selecionada.
    ///


6. **:octicons-terminal-16: - no terminal:** Quando a opção de cópia de downloads de pacotes for selecionada, o AndroidQF perguntará sobre a remoção de APKs assinados por desenvolvedores ou entidades confiáveis (como o Google ou o fabricante do dispositivo), a fim de reduzir o tamanho da pasta de extração.

	  
	Responda "Yes" (Sim) para que, ao revisar as informações, você possa focar aA análise de pacotes potencialmente suspeitos também economizará tempo e espaço de armazenamento.

    !!! nota "Qual é a opção ideal?"

        Embora nossa recomendação seja selecionar "Yes", a seleção depende de sua abordagem de análise e investigação, portanto, em casos com suspeita de ataques sofisticados, a opção "No" pode ser usada.
    
    Captura de tela do terminal Linux com o menu que copia os pacotes de aplicativos do AndroidQF e a opção "*Only non-system packages "* selecionada](../../../assets/01-tutorial/32-capture-linux-omission-applications.png "image 1")
    /// caption
    **Imagem 32** Captura de tela do terminal Linux com o menu padrão de aplicativos de certificado confiável do AndroidQF e a opção Yes selecionada.
    ///

    Nesse ponto, várias tarefas de aquisição serão executadas, como a coleta de propriedades do dispositivo, logs do sistema, processos em execução, configurações, arquivos temporários etc., que explicaremos uma a uma na próxima seção.

    !!! info "Process duration" (Duração do processo)
    
        **Esta etapa pode levar vários minutos**, dependendo do modelo do telefone e da quantidade de dados armazenados. O progresso é exibido linha por linha no terminal e não requer nenhuma outra intervenção, exceto no final, onde você deve pressionar Enter para concluir.

    Captura de tela do terminal Linux com o menu que copia os pacotes de aplicativos do AndroidQF e a opção "*Only non-system packages "* selecionada](../../../assets/01-tutorial/33-screenshot-running-correct.png "image 1")
    /// legenda
    **Imagem 33** Captura de tela do terminal Linux com informações da execução bem-sucedida da extração forense com o AndroidQF e solicitação para pressionar *"Enter "* para concluir.
    ///

Quando o processo de aquisição estiver concluído, a ferramenta terá capturado os principais arquivos e informações necessários para uma [triagem](../../references/00-glossary/index.md#triage).

### Folha de dicas: comandos ADB usados para obter informações forenses

Durante uma aquisição forense com o AndroidQF, vários módulos são executados para coletar informações do sistema, processos, configurações, registros e artefatos do dispositivo.

Abaixo está uma **cheatsheet** com os comandos *adb* equivalentes para entender as ações que o AndroidQF executa em segundo plano por meio de comandos.

Essa tabela serve como uma referência rápida para entender quais informações cada módulo obtém, como elas podem ser verificadas manualmente e qual é o comando adb básico que permite observar dados equivalentes em uma análise forense de consenso. Se quiser se aprofundar na construção e na estrutura de cada módulo, consulte o [dicionário de arquivos gerados pelo AndroidQF](../../references/01-reference-androidqf-dictionary/index.md).

| Módulo | Comando adb | Função |
| ----- | ----- | :---: |
| | **informações e configuração do dispositivo** | | | | | |
| | **getprop** | `adb shell getprop` | | Exibe as propriedades do sistema/dispositivo
| | | **selinux** | `adb shell getenforce` | | Retorna o status do SELinux | | |
| **settings** | <pre><code> adb shell cmd settings list system</code><br><br><code>adb shell cmd settings list secure</code><br><code>adb shell cmd settings list global</code></pre> | Extrai configurações de sistema, rede, segurança e acessibilidade. |
| **env** | `adb shell env` | Lista as variáveis de ambiente ativas e os caminhos do sistema. |
| **mounts** | <pre><code>adb shell "mount"</code><br><br><code>adb shell "cat /proc/mounts"</code></pre> | Exibe os pontos de montagem ativos e os tipos de sistema de arquivos. |
| | **relatórios de dispositivos** | | | | |
| **logcat** | <pre><code>adb shell logcat -d -b all "&#42;:V"</code><br><br><code>adb shell logcat -L -b all "&#42;:V"</code></pre> | Captura os registros da reinicialização atual e da última. |
| **dumpsys** | `adb shell dumpsys ` | Exibe informações de diagnóstico sobre todos os serviços ativos. |
| **bugreport** | `adb bugreport bugreport.zip` | Gera um relatório completo do sistema com configurações e registros. |
| **logs** | <pre><code>adb shell "ls -R /data/anr/"</code><br><code>adb shell "ls -R /data/log/"</code><br><code>adb shell "ls -R /sdcard/log/"</code><br><code>adb pull /data/system/uiderrors.txt</code><br><br><code>adb pull /proc/kmsg</code><br><code><br><code>adb pull /proc/last_kmsg</code><br><code><br><code>adb pull /sys/fs/pstore/console-ramoops</code><br><code>adb pull /data/anr/</code><br><code>adb pull /data/log/</code><br><code>adb pull /sdcard/log/</code></code></pre> | Listar e fazer download de arquivos de log e erros do sistema. |
** Informações de backup** | | | | |
| **backup somente de SMS** | <pre><code>adb backup</code><br><br><code>com.Android.providers.telephony</code></pre> | Cria backups de SMS
| **backup all** | `adb backup -all` | Cria backups de todo o sistema. |
| | **files** | <pre><codeprintf '%T@ %m %s %u %g %p\n' 2>/dev/null"</code><br><code>adb shell "find /vendor/ -printf '%T@ %m %s %u %g %p\n' 2>/dev/null"</code><br><code><br><br><code>adb shell "find /cust/ -printf '%T@ %m %s %u %g %p\n' 2>/dev/null"</code><br><br><code>adb shell "find /product/ -printf '%T@ %m %s %u %g %p\n' 2>/dev/null"</code><br><code><code>adb shell "find /apex/ -printf '%T@ %m %s %u %g %p\n' 2>/dev/null"</code><br><br><code>adb shell "find /data/local/tmp/ -printf '%T@ %m %s %u %u %g %p\n' 2>/dev/null"</code><br><code><br><code>adb shell "find /data/media/0/ -printf '%T@ %m %s %u %g %p\n' 2>/dev/null"</code><br><br><code>adb shell "find /data/misc/radio/ -printf '%T@ %m %s %u %g %p\n' 2>/dev/null"</code><br><br><br><code>adb shell "find /data/vendor/secradio/ -printf '%T@ %m %s %u %g %p\n' 2>/dev/null"</code><br><code><br><code>adb shell "find /data/log/ -printf '%T@ %m %s %u %g %p\n' 2>/dev/null"</code><br><br><code>adb shell "find /tmp/ -printf '%T@ %m %s %u %g %p\n' 2>/dev/null"</code><br><br><code><br><code>adb shell "find / -maxdepth 1 -printf '%T@ %m %s %u %g %p\n' 2>/dev/null"</code><br><br><code>adb shell "find /data/data/ -printf '%T@ %m %s %u %g %p\n' 2>/dev/null"</code></pre> | Exibe arquivos e metadados do sistema. |
| **tmp** | <pre><code>adb shell ls -R /data/local/tmp/</code><br><code>adb pull /data/local/tmp/ &lt;path-local&gt;</code></pre> | Lista e extrai arquivos do diretório temporário do dispositivo. |
| | **Processos e aplicativos** | | | | | | |
| | | **Lista de pacotes** | `adb shell pm list packages -f` | Lista os aplicativos instalados e permite extrair seus APKs. |
| | | | **packages download** | `adb pull <path_apk> <path_local>` | | Extrai APKs. |
| **processos** | `adb shell ps -A` | Lista os processos em execução no dispositivo. |
| | **services** | `adb shell service list` | Exibe os serviços ativos.
| **root\_binaries** | <pre><code>adb shell "which -a su"</code><br><code>adb shell "which -a busybox"</code><br><code><br><code>adb shell "which -a supersu"</code><br><code>adb shell "which -a Superuser.apk"</code><br><code><br><code>adb shell "which -a KingoUser.apk"</code><br><code>adb shell "which -a SuperSu.apk"</code><br><br><code>adb shell "which -a magisk"</code><br><code>adb shell "which -a magiskhide"</code><br><code><br><code>adb shell "which -a magiskinit"</code><br><code>adb shell "which -a magiskpolicy"</code></pre> | Procure vestígios de enraizamento ou binários com permissões elevadas. |

## Verificação da extração

Quando o AndroidQF terminar de ser executado, é importante validar se a aquisição foi concluída corretamente. Para fazer isso, execute as etapas a seguir:

1. se você recebeu uma extração criptografada, é necessário descriptografar essas informações primeiro; consulte a seção sobre [criptografar extrações] (#encrypting-extractions-optional).

2 Analise o arquivo *command.log*.

    Abra o arquivo *command.log* com um editor de texto e procure as palavras *WARNING* e *ERROR* para encontrar alertas durante a extração. Se houver correspondências na pesquisa, verifique se elas correspondem a falhas críticas ou eventos não relevantes.


	=== "No Linux/MacOS"
        
        Você pode usar o comando *grep* para fazer uma pesquisa dentro da pasta de aquisição:

        ````shell
        grep -i "AVISO\|ERRO" command.log
        ```

        A saída será em texto simples:

        ````shell
        2025-07-28T13:05:36-06:00 [ERRO] Falha ao obter caminhos de arquivo para o pacote com.adobe.reader: status de saída 1:
        2025-07-28T13:05:55-06:00 [ERROR] Falha ao obter caminhos de arquivo para o pacote com.whova.event: status de saída 1:
        2025-07-28T13:07:27-06:00 [ERRO] Falha ao obter caminhos de arquivo para o pacote im.vector.app: status de saída 1:
        2025-07-28T13:10:09-06:00 [ERRO] Falha ao obter caminhos de arquivo para o pacote sh.file.opener.shell.editor.app: status de saída 1:
        2025-07-28T13:29:51-06:00 [DEBUG] De: /data/system/uiderrors.txt
        2025-07-28T13:29:51-06:00 [DEBUG] To: /home/lightyear/Documentos/ST/ST2025/extracciones qf/a7de07b3-36d8-4589-9854-1bc666c2c873/logs/data/system/uiderrors.txt
        2025-07-28T13:29:51-06:00 [ERROR] Falha ao extrair o arquivo de registro /data/system/uiderrors.txt:
        2025-07-28T13:29:29:51-06:00 [ERROR] Failed to pull log file /proc/kmsg:
        2025-07-28T13:29:29:51-06:00 [ERROR] Failed to pull log file /proc/last_kmsg:
        2025-07-28T13:29:29:51-06:00 [ERROR] Failed to pull log file /sys/fs/pstore/console-ramoops:
        2025-07-28T13:29:29:51-06:00 [ERROR] Failed to pull log file /data/anr/:
        2025-07-28T13:29:29:51-06:00 [ERROR] Failed to pull log file /data/anr/anr_2025-07-23-03-47-27-988:
        2025-07-28T13:29:52-06:00 [ERROR] Failed to pull log file /data/log/:
        2025-07-28T13:30:00-06:00 [ERROR] Failed to pull log file /data/log/settingsprovider.txt:
        2025-07-28T13:30:30:00-06:00 [ERRO] Falha ao puxar o arquivo de registro /data/log/dark_mode_log0.txt.lck:
        2025-07-28T13:30:00-06:00 [ERROR] Falha ao extrair o arquivo de registro /data/log/dark_mode_log0.txt:
        2025-07-28T13:30:30:00-06:00 [ERROR] Failed to pull log file /data/log/knoxsdk.log.0.lck:
        2025-07-28T13:30:30:00-06:00 [ERRO] Falha ao puxar o arquivo de registro /data/log/knoxsdk.log.0:
        2025-07-28T13:30:30:00-06:00 [ERROR] Failed to pull log file /data/log/LockSettingsLog_Enroll.log:
        2025-07-28T13:30:30:01-06:00 [ERROR] Failed to pull log file /data/log/setupwizard.txt:
        2025-07-28T13:30:30:01-06:00 [ERRO] Falha ao puxar o arquivo de registro /data/log/appwidget_history_log0.txt.lck:
        2025-07-28T13:30:01-06:00 [ERRO] Falha ao puxar o arquivo de registro /data/log/appwidget_history_log0.txt:
        2025-07-28T13:30:01-06:00 [ERROR] Failed to pull log file
        ```

        A Figura 34 mostra a saída da pesquisa de erros em um sistema Linux.

        Captura de tela do terminal Linux com o comando *grep* para procurar erros no arquivo command.log gerado pelo AndoridQF](../../../assets/01-tutorial/34-screenshot-terminal-linux-errors.png "image 1")
        /// legenda
        **Imagem 34** Captura de tela do terminal Linux com o comando *grep* para procurar erros no arquivo command.log gerado pelo AndoridQF.
        ///

	=== "No Windows"

        Abra o arquivo com o *Notepad*. Se estiver usando o Windows em espanhol, pressione a combinação de teclas **ctrl+b** e, se estiver usando o Windows em inglês ou português, use **ctrl+f**.

        A Figura 35 mostra a saída de uma pesquisa de erros do Windows. Nesse caso, não foram encontrados erros relacionados ao processo de extração forense.

        Captura de tela do Bloco de Notas do Windows com a pesquisa de erros no arquivo command.log gerado pelo AndoridQF](../../../../assets/01-tutorial/35-screenshot-windows-errors.png "image 1")
        /// legenda
        **Imagem 35** Captura de tela do Windows Notepad com a pesquisa de erro no arquivo command.log gerado pelo AndoridQF.
        ///



Verifique a existência do arquivo *acquisition.json* e abra-o.

	Esse arquivo resume os detalhes da extração. Sua criação implica que o AndroidQF concluiu com êxito a extração forense do dispositivo.

    Exemplo da saída do arquivo *acquisition.json*:

    ```
    {
    "uuid": "a7de07b3-36d8-4589-9854-1bc666c2c873",
    "androidqf_version": "f77a04f",
    "storage_path": "/home/user/acquisition/folder qf/a7de07b3-36d8-4589-9854-1bc666c2c873",
    "started": "2025-07-28T19:02:46.15453512Z",
    "completed": "2025-07-28T19:30:22.947074074Z",
    "collector" (coletor): {
    "ExePath":"/data/local/tmp/collector",
    "installed": falso,
    "Adb": {
    "ExePath":"/usr/bin/adb",
    "Serial": ""
    },
    "Arquitetura": "arm64-v8a"
    },
    "tmp_dir":"/data/local/tmp/",
    "sdcard": "/sdcard/",
    "cpu": "arm64-v8a"
    }
    ```

3. Verifique a criação de arquivos e pastas de saída.

Certifique-se de que os seguintes arquivos e pastas tenham sido gerados:

* files
  * acquisition.json
  * backup.ab
  * bugreport.zip
  * command.log
  * dumpsys.txt
  * env.txt
  * files.json
  * getprop.txt
  * hashes.csv
  * logcat.txt
  * packages.json
  * processos.txt
  * root\_binaries.json
  * selinux.txt
  * serviços.txt
  * settings_global.txt
  * settings_secure.txt
  * settings\_system.txt
* Pastas de saída
  * apks/
  * logs/
  * tmp/

	  
Isso significa que os módulos foram executados corretamente.

Captura de tela dos arquivos do aplicativo no PopOS! mostrando a pasta de saída dos arquivos e diretórios gerados com a extração forense com o AndroidQF](../../../assets/01-tutorial/36-screenshot-files-output.png "image 1")
/// legenda
**Imagem 36** Captura de tela do aplicativo de arquivos no PopOS! mostrando a pasta de saída dos arquivos e diretórios gerados com a extração forense do AndroidQF.
///

Identificar que uma extração foi bem-sucedida envolve um processo de análise, habilidade e instinto para ler linhas com diferentes formatos e identificar todos os nomes dos arquivos de saída. Todo o seu esforço ajuda a comunidade a fortalecer essas ferramentas para torná-las melhores na sociedade civil.

## Conclusão

Parabéns! Você concluiu com êxito o processo de aquisição forense com o AndroidQF. Executar uma extração de dados forenses não é uma tarefa fácil, mas agora você dominou as etapas essenciais para realizar extrações seguras, documentadas e consentidas. O AndroidQF permitirá que você, como analista, dê suporte a investigações de seu laboratório, organização ou causa, se você for um analista independente em vigilância, ameaças digitais e documentação de incidentes ou ataques digitais. Suas novas habilidades são cruciais para fortalecer o uso dessas ferramentas para o benefício de muitas empresas.unidade e sociedade civil.

Agora que você tem a extração, a próxima etapa é interpretar as informações obtidas, pois, uma vez que a extração tenha sido realizada com sucesso, é necessário iniciar um processo de análise das informações contidas nessa extração.

Para ajudá-lo nessa análise, este repositório inclui um recurso de referência importante: o [AndroidQF-generated file dictionary](../../references/01-reference-androidqf-dictionary/). Com esse recurso, você será capaz de:

* Identificar o conteúdo de cada arquivo de saída.  
* Entender por que essas informações são importantes e como usá-las em uma análise forense.  
* Compreender o formato em que as informações são fornecidas e como visualizá-las.

A próxima etapa é realizar uma análise mais aprofundada das informações adquiridas. Para isso, recomendamos que você explore nossos materiais sobre o MVT, incluindo o [dicionário de arquivos gerados pelo MVT ao analisar capturas de tela com o AndroidQF](../../references/03-reference-mvt-androidqf-dictionary/index.md).

