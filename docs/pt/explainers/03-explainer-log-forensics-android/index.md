---
title: Explicador - Princípios para perícia forense baseada em logs em dispositivos Android 
summary: Documento introdutório com princípios para perícia forense baseada em logs em dispositivos Android
keywords: perícia forense, logs, android, androidqf
lang: pt-br
tags: [explainer, intro]
last_updated: 2025-09-05
some_url:
created: 2025-06-23
comments: true
authors:
    - Daniel Bedoya
    - MariaLab
    - Data Privacy Brasil

---

# Explicador: Princípios para perícia forense baseada em logs em dispositivos Android

Este documento faz **parte de um repositório de documentação técnica** que tem como objetivo estabelecer uma base de conhecimento comprovada, flexível e acessível para **impulsionar a análise forense consentida em benefício da sociedade civil**. Para organizar o conteúdo, é utilizado o [quadro de referência de documentação técnica Diataxis](https://diataxis.fr/).

Este recurso em particular se enquadra na categoria de materiais explicativos e apresenta os **fundamentos da perícia baseada em logs para dispositivos Android**, incluindo uma definição de perícia baseada em logs e uma comparação com outros tipos de análise, bem como casos de uso. Este é um **material introdutório que não requer conhecimentos prévios** e é complementado por outros [guias](../../how-tos/) de [extração forense](../01-explainer-introduction-digital-forensics/index.md#quais-sao-as-etapas-de-uma-investigacao-forense).


## O que é a análise forense baseada em logs e por que ela é útil?

A análise forense baseada em logs refere-se a um tipo de investigação que utiliza diferentes registros do sistema, como relatórios de erros, capturas de memória, arquivos de configuração, entre outros, para identificar e investigar vestígios e indicadores de potenciais ataques digitais (https://socialtic.org/wp-content/uploads/2020/11/Tipologia_AtaquesDigitales-2020-1.pdf).**

Para realizar uma análise forense baseada em logs, são percorridas [as diferentes etapas de uma investigação forense](../01-explainer-introduction-digital-forensics/index.md#quais-sao-as-etapas-de-uma-investigacao-forense), começando com a **identificação e coleta** de potenciais evidências. Ao coletar evidências, é importante obter um [consentimento informado](../../how-tos/01-how-to-obtain-informed-consent/), reduzir a quantidade de informações pessoais e manter processos adequados de verificação, preservação e proteção das informações.

No caso de dispositivos móveis, e em particular quando se suspeita de uma possível infecção avançada ou spyware, **a maior parte das análises** realizadas por organizações da sociedade civil como Amnesty Tech ou Citizen Lab **utilizam perícia baseada em logs**. A viabilidade de coletar dados relevantes e específicos (por exemplo, um relatório de erros do Android), **mesmo em situações de atendimento remoto**, torna esse tipo de análise comum na sociedade civil.

As evidências coletadas geralmente são **analisadas** posteriormente, idealmente em um ambiente de laboratório, em conformidade com as **boas práticas de [segurança operacional](https://en.wikipedia.org/wiki/Operations_security)**. Ferramentas como [MVT](https://github.com/mvt-project/mvt) ou [AndroidQF](https://github.com/mvt-project/androidqf/issues) facilitam diferentes ações durante a captura e análise de artefatos. De maneira geral, busca-se **testar a similaridade com [indicadores de comprometimento](https://www.cloudflare.com/pt-br/learning/security/what-are-indicators-of-compromise/)** (IoC, na sigla em inglês) de ataques previamente registrados e documentados; ou identificar e documentar anomalias ao comparar com uma linha de base estabelecida, que permita evidenciar comportamentos suspeitos ou vulnerabilidades que talvez não tenham sido relatadas. Devido à sua abordagem metodológica, as detecções positivas por meio de análise forense baseada em logs costumam ter um **alto nível de confiabilidade**.

É importante levar em consideração que **os logs e registros de um sistema** **mudam** constantemente ao longo do tempo e podem ser sobrescritos ou eliminados após um determinado período. Portanto, embora a análise forense baseada em logs possa ser aplicada posteriormente a um incidente de segurança, **a possibilidade de detectar alguma atividade maliciosa diminui se muito tempo tiver decorrido** entre a possível atividade e a aquisição de artefatos.

Embora os registros possam não ser úteis para ataques ocorridos anos atrás, **posteriormente podem ser descobertas novas vulnerabilidades**, metodologias ou indicadores de comprometimento para identificar ataques digitais que antes não eram detectáveis. Se você planeja armazenar registros para análises posteriores, é importante que exista uma carta ou formulário de consentimento documentado e que você reduza ou elimine qualquer informação pessoal que não seja relevante para a investigação forense.

A publicação “[Detecção e análise de spyware: metodologias, limitações e oportunidades](https://irl.works/blog/2025/03/19/spyware-detection-analysis.html)” **resume e apresenta diferentes metodologias em uso pela sociedade civil**, especificamente para a detecção de spyware. Além de investigações forenses de dispositivos, incluindo investigações baseadas em logs, são descritas **investigações a partir de sinais ou sistemas de monitoramento** instalados nos sistemas, onde um componente de software monitora em tempo real os processos e outras atividades para alertar sobre possíveis intrusões a partir de métodos determinísticos ou estatísticos. Além disso, é mencionada a **detecção de incidentes por meio da análise de tráfego de rede**, que busca detectar vestígios de um software malicioso investigando metadados das comunicações de rede dos dispositivos. 

Em resumo, algumas das **vantagens da perícia baseada em logs** são:

* Possibilidade de **atendimento remoto.** 
* Coleta **menos informações privadas**, especialmente se a coleta for pontual e os arquivos ou dados confidenciais forem eliminados.
* Permite obter **resultados com um** **alto nível de confiança**, especialmente quando é possível estabelecer uma correspondência com algum IoC conhecido.
* É útil para fazer **comparações a partir de uma linha de base conhecida** com a qual comparar.
* **É possível continuar avaliando os registros capturados** em relação a novos IoCs publicados após a coleta inicial.

E alguns dos **desafios de usar a perícia baseada em logs** são:

* Mesmo quando são feitas extrações direcionadas, **é possível que os arquivos incluam centenas de milhares de linhas**, de modo que a análise manual exige experiência técnica em filtragem, interpretação de dados e identificação. . 
* Alguns logs e registros podem não estar disponíveis no perfil do usuário ou **podem exigir permissões adicionais do sistema** (como, por exemplo, acesso super usuário no Android).
* Muitos arquivos de logs funcionam com **[buffers circulares](https://pt.wikipedia.org/wiki/Circular_buffer) que são sobrescritos** à medida que ficam cheios, de modo que as informações mais antigas são sobrescritas constantemente.
* Para extrair logs e registros, **é necessário ter um conhecimento básico do sistema** operacional, especialmente quando o armazenamento é particionado ou usa diferentes rotas para armazenar informações.

## Como iniciar uma análise forense baseada em logs em um dispositivo Android?

Para realizar uma análise forense baseada em logs, é necessário passar pelas etapas típicas de uma investigação forense, **começando com a captura dos registros-chave** do sistema que se deseja investigar. Para realizar a análise, também será necessário ter uma linha de referência, que nos permita entender qual é o comportamento esperado do dispositivo em situações normais. Como mencionado anteriormente, o **acesso a indicadores de comprometimento**, como os publicados pela [Amnesty International](https://github.com/mvt-project/mvt-indicators) ou pelo [Citizen Lab](https://github.com/citizenlab/malware-indicators), facilitam a identificação de ameaças e a triagem de possíveis incidentes, embora seja importante mencionar que eles podem perder a validade à medida que o invasor modifica sua infraestrutura, tecnologia ou vetores de ataque, devendo ser atualizados ou complementados com análises manuais.

Para extrair as informações essenciais de um dispositivo Android, é possível utilizar algumas **ferramentas que facilitam o empacotamento e a captura de registros**, como o relatório de erros do Google (bugreport) ou o shell do ADB, além de ferramentas desenvolvidas por terceiros, como o AndroidQF.

## Tipos de logs e ferramentas de empacotamento

No caso de dispositivos móveis com sistema operacional Android, devido à **diversidade de fabricantes e suas preferências particulares**, bem como ao ecossistema diversificado de desenvolvedores e componentes, existem diferentes abordagens para o registro de logs. Em geral, é utilizada uma combinação dos [seguintes padrões](https://source.android.com/docs/core/tests/debug/understanding-logging):

* [RCF 5424 (protocolo syslog)](https://datatracker.ietf.org/doc/html/rfc5424): Utilizado para registrar **eventos do kernel e de aplicativos do tipo UNIX**, como, por exemplo, serviços do sistema.
* [android.util.log](https://android.googlesource.com/platform/frameworks/base/+/master/core/java/android/util/Log.java) : Utilizado para registrar **eventos do Android e de aplicativos do sistema**
* [java.util.logging.level:](https://docs.oracle.com/javase/8/docs/api/java/util/logging/Level.html) É usado para **registro em aplicativos Java**, o que inclui muitos aplicativos de terceiros.

Cada um dos padrões possui uma construção semelhante, mas **níveis diferentes para registro** e alerta em situações de erro. Por exemplo, no **syslog existem 8 níveis**: desde logs de depuração até logs de emergência; enquanto no **android.util existem apenas 5 níveis**, que vão desde verboso até erros.

Embora compreender exatamente os níveis e a construção de cada um dos logs do Android esteja fora do escopo deste recurso, **é importante ter em mente a fragmentação do ecossistema**, pois isso também se refletirá nas diferenças para navegar pelas interfaces gráficas, acessar opções avançadas ou extrair informações.

Embora a diversidade do ecossistema impeça o estabelecimento de uma lista definitiva para todos os sistemas Android, a seguir estão detalhados alguns dos tipos de logs e registros mais comumente usados durante uma análise forense e que podem ser acessados sem a necessidade de privilégios de administração (ou seja, acesso root):

* **logs principais (main log):** Os logs principais registram mensagens gerais dos aplicativos e do sistema.
* **logs de pânico do kernel (kernel panic):** Os logs de pânico referem-se a registros criados quando o sistema operacional detecta um erro do qual não é possível recuperar, como uma violação de memória ou algum problema com uma chamada de sistema. Na maioria dos casos, a função do kernel do Linux [‘ramoops’](https://www.kernel.org/doc/html/v4.19/admin-guide/ramoops.html) é usada para gravar os logs antes que o sistema pare.
* **Relatórios de interrupções (crash reports) e tombstones:** Os logs de interrupções geralmente são registrados quando um aplicativo ou processo é interrompido inesperadamente. Por sua vez, os tombstones referem-se a relatórios detalhados de falhas para aplicativos nativos do Android.
* **Logs de rádio**: Os logs de rádio e componentes de rede capturam informações sobre a atividade que ocorre entre o celular e as torres de comunicação, relacionadas a dados móveis, chamadas de voz, SMS, entre outros.
* **logs de segurança**: Os logs de segurança referem-se a registros relacionados a configurações de segurança, como [SELinux](https://www.redhat.com/en/topics/linux/what-is-selinux) ou logs encontrados dentro do buffer de segurança.


Existem algumas ferramentas nativas que permitem extrair e empacotar os registros (logs, aplicativos, lista de processos, etc.) de forma simples e pontual. Algumas dessas ferramentas são:

* [**dumpsys**](https://developer.android.com/tools/dumpsys): É uma ferramenta nativa de linha de comando no Android, disponível a partir do shell de depuração do Android ou ADB. **Permite extrair informações detalhadas dos serviços do sistema**, como bateria, rede Wi-Fi, uso de memória, entre outros.
* **dumpstate**: É uma ferramenta nativa que **permite coletar informações do registro de erros** de um dispositivo. Está disponível através da ferramenta de criação de relatórios de erros ou bugreport.
* [**logcat**](https://developer.android.com/tools/logcat): É uma ferramenta nativa de linha de comando no Android, disponível a partir do shell de depuração do Android ou ADB. **Permite extrair mensagens ou logs do sistema,** incluindo muitos dos logs descritos anteriormente.
* [**bugreport**](https://developer.android.com/studio/debug/bug-report): É uma ferramenta nativa de linha de comando no Android, disponível a partir da interface gráfica ou do shell ADB. **Permite gerar um relatório de erros** que contém logs de diagnóstico, gerados a partir da chamada para logcat, dumsptate e dumpsys. É gerado dentro de um arquivo .zip e é composto por uma estrutura de pastas com informações sobre erros, uso de memória, chamadas ao sistema, informações de rede, informações do dispositivo, entre outros. 
* [**androidqf**](https://github.com/mvt-project/androidqf): É uma ferramenta desenvolvida inicialmente por Claudio Gurnieri e atualmente suportada pela equipe do [laboratório de segurança da Anistia Internacional.](https://securitylab.amnesty.org/latest/2024/12/tech-guide-detecting-novispy-spyware-with-androidqf-and-the-mobile-verification-toolkit-mvt/)
* [**Perfetto**](https://perfetto.dev/docs/)**:** É uma ferramenta de código aberto que permite realizar uma depuração avançada de aplicativos no sistema operacional Android e Linux. Ela coleta informações de memória, CPU, consumo de bateria, entre outros.

## Considerações adicionais sobre a perícia baseada em logs

Antes de iniciar uma análise forense baseada em logs, é importante levar em consideração os seguintes aspectos:

* **Proteção e minimização de dados sensíveis**: Ao contrário de [outras abordagens de perícia forense digital](../01-explainer-introduction-digital-forensics/index.md#onde-a-pericia-digital-e-utilizada), na sociedade civil, busca-se desenvolver investigações a partir de informações específicas e direcionadas, e **evitar a coleta excessiva de informações pessoais** não relevantes para a investigação. Se os pacotes de informações [incluírem informações confidenciais](../../how-tos/01-how-to-obtain-informed-consent/index.md#quais-informacoes-confidenciais-sao-coletadas-durante-uma-analise-forense), como, por exemplo, fotografias pessoais, é altamente recomendável aplicar procedimentos automatizados para manter apenas as informações relevantes. Esses procedimentos devem ser devidamente documentados e replicáveis para garantir sempre a integridade das informações.

* **Consentimento informado**: Antes de coletar logs ou registros de um dispositivo, é importante discutir e obter um consentimento informado. [Este recurso fornece orientação e diretrizes para gerar uma carta de consentimento](../../how-tos/01-how-to-obtain-informed-consent/) e acordar boas práticas com quem solicita a análise.

* **Funções, fases e etapas da análise forense baseada em logs:** A análise forense baseada em logs passa por uma [série de etapas](../01-explainer-introduction-digital-forensics/index.md#quais-sao-as-etapas-de-uma-investigacao-forense), começando pela **identificação e coleta** de informações essenciais. Durante essas etapas, é possível seguir guias práticos para executar procedimentos de coleta e empacotamento de informações que, em geral, **não exigem conhecimentos avançados em análise forense**. A triagem e análise das informações coletadas requerem conhecimentos adicionais, tanto no uso de ferramentas de análise quanto na aplicação e revisão manual. 

* **Gerenciamento de expectativas**: Ao realizar a revisão de um dispositivo, **é possível que não sejam encontrados vestígios de alguma ameaça**, quando comparado com ameaças conhecidas. Embora isso seja um sinal positivo, não é suficiente para afirmar que nenhuma ameaça existe. Mesmo após realizar uma análise manual, pode haver fatores que limitam o sucesso de uma análise forense baseada em logs. Caso haja fortes suspeitas de comprometimento (por exemplo, notificação de ameaças de plataformas), recomenda-se também considerar alguns dos métodos forenses mencionados anteriormente.

* **Revisão por pares e trabalho colaborativo**: Ao realizar investigações forenses de qualquer tipo, incluindo aquelas baseadas em logs, é importante verificar as descobertas com colegas de confiança que possam replicar de forma independente a metodologia para confirmar os resultados. É altamente recomendável realizar revisões por pares antes de publicar, especialmente se os resultados forem apresentados por meio de uma nova metodologia ou se se tratar de uma nova vulnerabilidade.

## Conclusão

A **investigação forense baseada em logs** utiliza registros importantes do dispositivo, como informações de processos, relatórios de erros ou logs do sistema, para identificar indicadores de comprometimento conhecidos ou destacar anomalias ao comparar com uma linha de base estabelecida. 

No caso do **sistema Android**, devido à diversidade de fabricantes e tecnologias envolvidas em sua criação e desenvolvimento, existe uma variedade de padrões e ferramentas com os quais é importante se familiarizar, incluindo syslog, dumpstate e ADB. Além disso, algumas ferramentas como AndroidQF são muito úteis durante a coleta de informações forenses no Android.

Grande parte dos relatórios publicados até agora pela sociedade civil utilizou a perícia baseada em logs para justificar e documentar suas descobertas, em parte porque permite realizar investigações remotamente, minimiza as informações pessoais a serem coletadas e fornece resultados com alto grau de confiabilidade.

Se você deseja contribuir com o desenvolvimento, tradução ou divulgação deste recurso, escreva para [seguridad@socialtic.org](mailto:seguridad@socialtic.org)


## Comentários

Tem comentários ou sugestões sobre este recurso? Você pode usar a função de comentários mostrada abaixo para deixar suas ideias ou observações. Por favor, certifique-se de seguir nosso [código de conduta](../../community/code-of-conduct/). A função de comentários leva diretamente à seção de [Discussions do Github](https://github.com/Socialtic/forensics/discussions), onde você também pode participar das discussões de forma direta.



