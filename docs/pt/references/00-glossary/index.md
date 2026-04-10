---

title: Glosario 
summary: Glosario 
keywords: glosario
lang: es
tags: [glossary, glosario, reference]
last_updated: 2025-08-04
some_url:
created: 2025-08-04
author:
    name: Daniel
    url: https://socialtic.org/quienes-somos/
    description: SocialTIC
alternate: 
    en: en/references/00-glossary.html
translation-review-pending: true
---

# Glossário

Este documento é **parte de um repositório de documentação técnica** que visa estabelecer uma base de conhecimento comprovada, flexível e acessível para **promover a análise forense consensual em benefício da sociedade civil**.

Este recurso específico é um glossário de termos que inclui **conceitos, abreviações e outros termos** que são considerados relevantes para a compreensão do conteúdo. Eles estão organizados em ordem alfabética.

## Termos

### ADB

ADB significa *Android Debug Bridge*, ou Ponte de depuração do Android. O ADB é uma **ferramenta de linha de comando** **que permite que você se comunique diretamente via USB com um dispositivo Android** e inicie diferentes ações e comandos.  

Do ponto de vista da **forense digital** e, em particular, ao fazer [investigações baseadas em logs](../../explainers/03-explainer-log-forensics-android/) usando ferramentas como o AndroidQF, o **ADB permite estabelecer comunicação direta com um dispositivo**. Ele é útil em situações em que **você tem acesso físico ao dispositivo** e quando deseja obter informações diretamente do dispositivo por meio de **comandos nativos**, sem usar ferramentas adicionais.


### Aquisição

Refere-se a um estágio da investigação forense, em que o analista forense deve determinar a melhor maneira de coletar evidências forenses e aplicar os procedimentos necessários para extrair artefatos forenses.


### Análise de risco

Os riscos específicos que uma organização ou indivíduo enfrenta **dependem do contexto e do trabalho específico**. O processo de identificação de vulnerabilidades, riscos e ameaças em um determinado momento é conhecido como análise de risco.

### AndroidQF

O [AndroidQF] (https://github.com/mvt-project/androidqf) é uma ferramenta de software gratuita e de código aberto **focada na extração forense de dispositivos Android**. Atualmente é mantida pelo [Amnesty International Security Lab](https://securitylab.amnesty.org/es/).

Seu foco é especificamente para jornalistas, ativistas, defensores dos direitos humanos e os **laboratórios técnicos que acompanham casos de vigilância digital e ameaças de spyware**.

### APK

De acordo com a Wikipedia, um [APK](https://es.wikipedia.org/wiki/APK_(format)) é um arquivo com extensão .apk (Android Application Package) é um pacote para o sistema operacional Android. Esse formato é uma variante do formato Java JAR e é usado para distribuir e instalar componentes empacotados para a plataforma Android para smartphones e tablets.

### Artefato forense

Um artefato forense refere-se à evidência ou aos dados recuperados durante a análise forense digital, incluindo arquivos, registros de processos, registros, metadados etc.

### Binário

Binários de software referem-se a arquivos que contêm apenas código binário pré-compilado, ou seja, instruções que são apenas legíveis por máquina e **prontas para serem executadas.** Exemplos incluem arquivos com a extensão ``.bin``, ``.exe`` ou ``.app``.

### Bugreport

Esta é uma ferramenta de linha de comando nativa do Android, disponível na GUI ou no shell ADB. Ela permite gerar um relatório de bug contendo registros de diagnóstico, gerados a partir da chamada de logcat, dumsptate e dumpsys. Ele é gerado em um arquivo .zip e é composto por uma estrutura de pastas com informações sobre erros, uso de memória, chamadas do sistema, informações de rede, informações do dispositivo, entre outras.

### Cadeia de custódia

O processo de documentar claramente quem e como as evidências são manipuladas é conhecido como **cadeia de custódia**. A evidência forense pode ser adulterada ou destruída durante o processo forense, portanto, o analista deve ser capaz de demonstrar a [integridade da evidência] (https://www.ibm.com/es-es/topics/data-integrity).  Se essa demonstração não for possível ou suficientemente robusta, a evidência pode não ser **admissível em processos judiciais** ou pode ser refutada e descartada por outros especialistas.

### Consentimento informado

Consent](https://es.wikipedia.org/wiki/Consentimiento) é um princípio que se refere à externalização da vontade entre duas ou mais pessoas de aceitar direitos e obrigações. No contexto da análise forense digital para o benefício de indivíduos da sociedade civil, o consentimento informado refere-se à **concordância e aprovação de ações para facilitar a coleta, a análise, a apresentação e a preservação de evidências digitais**.

Um aspecto fundamental de qualquer acordo de consentimento é a capacidade do consentidor de tomar uma **decisão informada** sobre o curso da investigação, incluindo a capacidade de recusar assistência. Na práticaNa prática forense, isso significa fornecer todas as informações necessárias para que a pessoa que solicita a análise compreenda as ações, os riscos, os direitos e as obrigações envolvidos no processo investigativo. É importante que o **analista se comunique de forma clara e transparente** e respeite os desejos da pessoa que está solicitando apoio.

### Copiar pouco a pouco

A cópia bit a bit, DD ou duplicação de disco refere-se ao processo de criação de uma réplica exata de um meio eletrônico. Elas permitem que a evidência original seja protegida de forma a salvaguardar sua integridade e preservá-la de acordo com as práticas recomendadas.

### CVE

Um programa para relatar, classificar e publicar vulnerabilidades de segurança. Registros CVE exclusivos são estabelecidos para cada vulnerabilidade, como ```CVE-2014-0160``.

###taxis

(https://diataxis.fr/start-here/) é uma estrutura para escrever e organizar a documentação técnica. Como princípio fundamental, ele tenta agrupar a documentação em quatro categorias diferentes:  **Explicadores**, **Guias de instruções**, **Tutoriais** e **Referências**; que, por sua vez, respondem a necessidades específicas do leitor. Cada tipo de material tem uma finalidade e um estilo diferentes.

### DFIR (Digital Forensics and Incident Response)

DFIR refere-se à combinação e à unificação dos procedimentos de resposta a incidentes e de análise forense. O objetivo é que, durante a resposta a um incidente, sejam consideradas as práticas recomendadas para a coleta e a preservação de evidências, e que as descobertas da análise forense sejam usadas para conter e erradicar ameaças e, por fim, evitar futuros incidentes.

### Exploração

[Exploit (https://es.wikipedia.org/wiki/Exploit) é um termo da ciência da computação que significa explorar ou explorar, que é um software, um dado ou uma sequência de comandos ou ações, usado para explorar uma vulnerabilidade de segurança em um sistema de informações para obter um comportamento indesejado do sistema.


### Forense digital

A perícia digital é o processo usado para a coleta, preservação, análise e apresentação de evidências digitais derivadas de mídias e dispositivos eletrônicos, usando **técnicas de investigação e métodos científicos** que sejam confiáveis, precisos e repetíveis, de modo que os resultados possam ser usados em **processos judiciais**.[1](https://csrc.nist.gov/glossary/term/digital_forensics)

A perícia digital é usada para descobrir e examinar dados de dispositivos eletrônicos com o objetivo de **identificar, recuperar, documentar e interpretar informações digitais** e sua conexão com [ataques digitais](https://protege.la/ataques/). O uso de procedimentos padrão, de acordo com as práticas recomendadas, **permite a geração de evidências úteis** para impulsionar ações de **responsabilidade**, o que pode reduzir a impunidade com que os ataques digitais são executados.


### Google Takeout

É uma função para contas on-line do Google que permite extrair informações de diferentes aplicativos, logs de acesso, logs de segurança, e-mail, entre outros. O processo leva alguns dias para ser concluído.

 [Siga este link para acessar o recurso e iniciar uma solicitação de retirada] (https://takeout.google.com/?pli=1).  


### Lawfare

Lawfare refere-se ao uso do sistema jurídico ou de instituições para prejudicar, desacreditar ou afetar indivíduos ou organizações. Por exemplo, em relação ao processo judicial dos EUA entre a NSO e o WhatsApp, o Citizen Lab enfrentou uma série de desafios legais e aplicativos que buscavam desmantelar seu trabalho e acessar informações confidenciais, incluindo a lista de vítimas. Em outro exemplo, em 2018, a empresa canadense Sandvine ameaçou o Citizen Lab com um processo de difamação após sua publicação sobre o uso de equipamentos da Sandvine para a implantação de spyware.  

### Hash

[Hash](https://es.wikipedia.org/wiki/Funci%C3%B3n_hash) são funções criptográficas que permitem a produção de um único valor para um determinado conjunto de dados. Os exemplos incluem MD5, SHA1.

### Ferramenta portátil

Refere-se a uma ferramenta de software que não requer instalação para ser executada. A ferramenta não modifica nem adiciona arquivos ao sistema, mas inclui todos os arquivos de que precisa para ser executada em sua própria pasta ou binário de tempo de execução.

Uma das vantagens desse tipo de programa é que ele deixa menos rastros de sua execução, em comparação com os programas que precisam ser instalados.

### Identificação

Refere-se a um estágio da investigação forense, em que o analista determina **quais dispositivos, contas ou sistemas podem conter informações relevantes para a investigação**. Exemplos de dispositivos incluem telefones celulares, computadores, contas on-line, mídia de armazenamento, hardware e software de computador.re outros. Idealmente, para determinar quais evidências coletar, o analista deve entrar em contato com a pessoa afetada para entender o que aconteceu, quais ações foram tomadas até o momento e quais evidências podem estar disponíveis.

### Indicador de compromisso (IOC)

[Um indicador de comprometimento (IoC) (https://es.wikipedia.org/wiki/Indicador_de_compromiso) é uma informação relevante que descreve qualquer incidente de segurança cibernética, atividade e/ou artefato malicioso por meio da análise de seus padrões de comportamento.[1] A intenção de um indicador de comprometimento é delinear as informações recebidas ou extraídas durante a análise de um incidente de forma que possam ser reutilizadas por outros investigadores ou partes afetadas para descobrir as mesmas evidências em seus sistemas e determinar se eles foram ou não comprometidos, seja do ponto de vista do monitoramento de ameaças ou da análise forense. 2] Por exemplo, arquivos criados, entradas de registro modificadas, novos processos ou serviços são identificados. A ideia subjacente é que, se você escanear um sistema e encontrar os detalhes contidos em um determinado indicador de comprometimento, estará lidando com uma infecção causada pelo programa malicioso (malware) ao qual o indicador de comprometimento se refere.[3] Os indicadores de comprometimento permitem uma troca simples e prática de informações para fins de detecção de intrusão a partir de análise forense, resposta a incidentes ou análise de malware.

### Integridade da informação

A integridade das informações, juntamente com a confidencialidade e a disponibilidade, está entre os princípios fundamentais da proteção das informações.  A integridade busca garantir que os dados sejam precisos e confiáveis e **que não tenham sido acidentalmente ou intencionalmente modificados por terceiros não autorizados**, seja em repouso, em uso ou em movimento.

### Inteligência contra ameaças

De acordo com a [wikipedia](https://es.wikipedia.org/wiki/Inteligencia_de_Ciberamenazas), a inteligência sobre ameaças cibernéticas (CTI), também conhecida como inteligência sobre ameaças cibernéticas, é a atividade de coleta de informações com base em conhecimento, habilidade e experiência sobre a ocorrência e a avaliação de ameaças cibernéticas e físicas, bem como sobre os agentes de ameaças, com a intenção e o objetivo de ajudar a mitigar possíveis ataques e eventos prejudiciais que ocorrem no espaço cibernético.

Esse conceito surgiu para combater a grande variedade de ameaças que estão ocorrendo, bem como para ajudar os profissionais de segurança a reconhecer indicadores de ataques cibernéticos, extrair informações sobre os métodos de ataques e, consequentemente, responder a eles de forma adequada e precisa.

A inteligência sobre ameaças cibernéticas busca gerar conhecimento sobre o inimigo a fim de reduzir o risco para qualquer instituição. Trata-se de uma estratégia que sempre buscará antecipar e neutralizar os ataques, analisando a ameaça como um todo para detectar os principais dados que ajudam a identificar o autor do ataque, o criminoso cibernético. Seu objetivo final é fornecer a capacidade de perceber, reconhecer, raciocinar, aprender e agir de forma inteligente e oportuna sobre os indicadores de cenários de ataque e ataques cibernéticos avançados, ou seja, tomar as ações defensivas inteligentes correspondentes.

### Registro

Os logs, também conhecidos como registros ou logs, são arquivos que documentam as atividades que ocorrem em um sistema de computador, rede ou aplicativo. Esses logs podem conter informações sobre o acesso do usuário, alterações no sistema, erros e outras atividades relevantes para uma investigação forense.

Neste recurso, detalhamos considerações importantes para [investigações forenses baseadas em logs em dispositivos Android](../../explainers/03-explainer-log-forensics-android/).

### Malware

Malware, traduzido como programa malicioso, programa malicioso, programa malicioso ou código malicioso, é qualquer tipo de software que executa ações prejudiciais em um sistema de computador intencionalmente (em oposição a malware) e sem o conhecimento do usuário (em oposição a software potencialmente indesejado).

### Modo de desenvolvedor

As [**opções do desenvolvedor**] (https://developer.android.com/studio/debug/dev-options) referem-se a um **menu oculto** do sistema operacional **Android** que permite configurar algumas **funções adicionais**, especialmente destinadas a apoiar o processo de [depuração] (https://es.wikipedia.org/wiki/Depuraci%C3%B3n_de_programas) durante a **criação de novos aplicativos ou alterações no sistema**. Entre as opções de desenvolvedor, também é comum colocar algumasalgumas **configurações avançadas**, como o ajuste das preferências do driver gráfico ou das configurações avançadas de rede e até mesmo **opções experimentais** que ainda estão sendo testadas ou desenvolvidas.


### MVT

O MVT é uma ferramenta para facilitar a análise forense consensual de dispositivos pertencentes a pessoas que podem ser alvo de ataques avançados de spyware e, especificamente, pessoas da sociedade civil e comunidades em risco.

Ela é indicada em seu [site](../../community/license/):

_O Mobile Verification Toolkit (MVT) é uma ferramenta para facilitar a análise forense consensual de dispositivos Android e iOS, com o objetivo de identificar traços de comprometimento.

Ele foi desenvolvido e lançado pelo Laboratório de Segurança da Anistia Internacional em julho de 2021 no contexto do Projeto Pegasus, juntamente com uma metodologia técnica forense. Ele continua a ser mantido pela Anistia Internacional e por outros colaboradores.

Nesta documentação, você encontrará instruções sobre como instalar e executar os comandos mvt-ios e mvt-android e orientações sobre como interpretar os resultados extraídos.

### Notificação de ameaça

As notificações de ameaças referem-se a mensagens enviadas por plataformas e fabricantes para pessoas que podem ter sido

De acordo com a Apple, as notificações de ameaças informam e ajudam as pessoas que usam dispositivos que podem ter sido alvo de ataques mercenários de spyware. A Apple envia essas notificações por e-mail e iMessage para os endereços e números de telefone registrados em todos os dispositivos associados à conta Apple de uma pessoa. A notificação também é exibida na parte superior da página depois que a pessoa faz login em account.apple.com.

### n-day

n-day refere-se a um tipo de [vulnerabilidade](#vulnerabilidade) que já é conhecida, mas ainda não foi resolvida em todos os sistemas afetados. Em alguns casos, podem existir patches de segurança ou atenuações oficiais, mas ainda não foram aplicados aos computadores afetados.  

### Pessoa especializada (expert)

De acordo com a [wikipedia](https://es.wikipedia.org/wiki/Perito), um especialista (feminino, perita ou experta)[1] é uma pessoa reconhecida como fonte confiável em um determinado assunto, técnica ou habilidade, cuja capacidade de julgar ou decidir de forma correta, equilibrada e inteligente confere autoridade e status por seus pares ou pelo público em um assunto específico.

No contexto das investigações forenses, um especialista é uma pessoa que tem conhecimento reconhecido (por exemplo, por meio de certificação) e que, por meio de seu conhecimento, pode analisar, avaliar e fazer julgamentos sobre as evidências coletadas.

### Phishing

Phishing é uma técnica baseada na personificação ou falsificação de informações para induzir uma pessoa a realizar uma ação, como clicar em um link, abrir um arquivo infectado, conectar-se a uma rede ou sistema falso ou inserir informações em sites falsos. Geralmente, com o objetivo de roubar informações, infectar um computador ou sistema de informações.

* Por exemplo, e-mails ou SMS suspeitos pedindo para clicar em links.
* Por exemplo, e-mails ou SMS suspeitos solicitando o envio ou a resposta de informações privadas, confidenciais ou financeiras.
* Por exemplo, e-mails suspeitos solicitando a abertura de anexos.

### Provedor de serviços de Internet (ISP)

Refere-se à empresa que fornece serviço de Internet ao usuário. Eles geralmente fornecem conexão de última milha,

### Resposta a incidentes de segurança

Resposta a incidentes](https://www.ibm.com/es-es/topics/incident-response) concentra-se em **detectar e responder a eventos de segurança**. Por meio de procedimentos de resposta, ela visa minimizar o impacto e conter as consequências dos incidentes. Para uma resposta eficaz, é importante identificar a causa raiz das intrusões para que a ameaça possa ser erradicada e a recuperação em tempo hábil possa ser obtida.

### Backup gerado pelo ADB

Um dos comandos da ferramenta de console [ADB](#adb) permite gerar um backup completo do dispositivo, incluindo aplicativos e algumas configurações. Geralmente, ele é acessado no ADB por meio do comando ``adb backup`` ou usado por meio de ferramentas como o AndroidQF. Quando executado, o dispositivo solicita uma senha para criptografar os dados.  

### SocialTIC

A [SocialTIC] (https://socialtic.org) é uma organização da sociedade civil sediada no México. Sua missão é SocialTIC **capacitar com segurança os atores da mudança na América Latina**, fortalecendo suas ações de análise, comunicação social e defesa de direitos por meio do uso estratégico de tecnologias e dados digitais.

### Spyware

Um tipo de malware que coleta informações de um computador ou dispositivo móvel e, em seguida, transmite essas informações para uma entidade externa sem o conhecimento ou o consentimento do proprietário do computador.dor. As funcionalidades desse tipo de ferramenta são variadas, mas, em geral, permitem acessar e extrair informações armazenadas e em trânsito, além de manipular os sensores do dispositivo (câmera, microfone etc.).  

### Stalkerware

Stalkerware é um spyware usado em pequena escala, principalmente em círculos íntimos, como casais, familiares ou amigos.

Eles geralmente são instalados por meio de acesso físico ao dispositivo e buscam coletar o máximo de informações possível. O invasor pode ter acesso a um painel de controle onde pode visualizar todas as informações.

Esses tipos de ferramentas geralmente são vendidos como opções de proteção familiar para evitar o uso mal-intencionado do dispositivo ou para evitar roubos; no entanto, suas funções e recursos permitem que sejam usados como ferramentas de monitoramento doméstico e espionagem.


### TTP

TTP significa _Techniques, Tactics and Procedures_ (técnicas, táticas e procedimentos) e refere-se a uma lista de técnicas, táticas e comportamentos usados por agentes de ameaças. A estrutura de TTP mais conhecida é a do [MITRE ATT&CK] (https://attack.mitre.org/), que também inclui um registro histórico de [TTPs associados a determinados agentes de ameaças] (https://attack.mitre.org/groups/).

### Triagem

A triagem de incidentes de segurança refere-se ao processo de avaliação inicial e classificação de incidentes de segurança com base em vários fatores, como gravidade, urgência e impacto potencial. Seu principal objetivo é alocar recursos e prioridades de forma eficaz, permitindo que as equipes de resposta a incidentes se concentrem nas ameaças mais críticas e reduzam o risco para a organização. Esse processo, fundamental para o gerenciamento de incidentes, é semelhante à triagem médica, em que os pacientes são classificados de acordo com a gravidade de sua condição para determinar a ordem de atendimento.


### Volatilidade

A volatilidade das evidências digitais refere-se ao fato de que algumas informações disponíveis nos sistemas são destruídas ou alteradas com o tempo.

Por exemplo, alguns arquivos de registro são sobrescritos quando atingem um determinado limite, de modo que algumas dessas evidências podem não existir permanentemente ao longo do tempo.

### Vulnerabilidade

Por outro lado, uma vulnerabilidade refere-se a uma deficiência ou fraqueza em processos, sistemas, práticas ou hábitos que podem levar a ameaças ou aumentar o impacto e as consequências de um incidente.

### Clique zero

Refere-se a um tipo de ataque no qual **nenhuma intervenção do usuário é necessária para a implantação do malware**. Normalmente, esse tipo de ataque é muito sofisticado e caro, e requer várias vulnerabilidades encadeadas para ser bem-sucedido.


### Dia zero

Refere-se a um tipo de ataque que explora uma [vulnerabilidade](#vulnerabilidade) que não é conhecida, nem mesmo pelo fabricante do dispositivo. Portanto, não há patches ou correções que possam ser aplicados.

Você pode consultar aqui a [página da wikipedia para "Zero-day attack"](https://es.wikipedia.org/wiki/Ataque_de_d%C3%ADa_cero).
