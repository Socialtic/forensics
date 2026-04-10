---

title: ¿Cómo habilitar las opciones de desarrollador en diferentes dispositivos Android?
summary: Cómo habilitar las opciones de desarrollador en diferentes dispositivos Android.
keywords: triage, android, developer options
lang: es
tags: [how-to, intro]
last_updated: 2025-07-28
some_url:
created: 2025-07-28
comments: true
author:
    name: Daniel
    url: https://socialtic.org/quienes-somos/
    description: SocialTIC

translation-review-pending: true
---

# Guia: Como ativar as opções de desenvolvedor em diferentes dispositivos Android?


Este recurso se enquadra na categoria de **guias de instruções** e mostra as etapas a serem seguidas para **ativar o menu de opções do desenvolvedor em diferentes dispositivos Android**, bem como uma breve explicação sobre **o que são as opções do desenvolvedor** e **por que elas são úteis** ao fazer perícia digital. Este é um material **introdutório**, complementar a outros recursos, como o [explicador forense baseado em registro para dispositivos Android](../../explainers/03-explainer-log-forensics-android/), e **faz parte das etapas a serem seguidas para realizar a triagem inicial**.   

Somos gratos pela **colaboração** do [Reporters Without Borders security lab] (https://rsf.org/en/digital-security-lab), que forneceu a contribuição inicial necessária para a produção deste guia.

## O que são e por que são úteis?

As [**opções do desenvolvedor**](https://developer.android.com/studio/debug/dev-options) referem-se a um **menu oculto** do sistema operacional **Android** que permite configurar algumas **funções adicionais**, especialmente destinadas a apoiar o processo de [depuração](https://es.wikipedia.org/wiki/Depuraci%C3%B3n_de_programas) durante a **criação de novos aplicativos ou alterações no sistema**. Entre as opções do desenvolvedor, algumas **configurações avançadas** também são frequentemente colocadas, como o ajuste das preferências do driver gráfico ou configurações avançadas de rede e até mesmo **opções experimentais** que ainda estão em teste ou desenvolvimento.

Do ponto de vista da **forense digital** e, em particular, ao fazer [investigações baseadas em logs](../../explainers/03-explainer-log-forensics-android/) usando ferramentas como MVT e AndroidQF, as opções do desenvolvedor **permitem ativar os principais recursos**, como **[depuração USB](../../references/00-glossary/index.md#adb)**, o **consolo do ADB** ou a **geração de relatórios de erros***. É por isso que, em muitos casos, a **primeira etapa** será ativar o menu de opções do desenvolvedor.

## Por que há diferentes maneiras de ativá-las?

O sistema operacional Android é baseado no projeto de código aberto [*Android Open Source Project*](https://source.android.com/)*.* No entanto, [a maioria dos fabricantes usa uma versão proprietária do Google](https://www.makeuseof.com/tag/android-really-open-source-matter/), sobre a qual são adicionadas camadas de personalização adicionais, que, na maioria dos casos, também são proprietárias. Há algumas alternativas, como [LineageOS](https://lineageos.org/), [Graphene OS](https://grapheneos.org/) ou [CalyxOS](https://calyxos.org/), que se baseiam inteiramente em princípios de **fonte aberto** e buscam se afastar dos ecossistemas proprietários.

O resultado desses desenvolvimentos adicionais sobre o projeto básico significa que há uma **grande variedade de interfaces gráficas** para o sistema operacional. Os exemplos incluem:

* [Pixel UI] (https://en.wikipedia.org/wiki/Google_Pixel): interface de usuário desenvolvida pelo **Google** para dispositivos Pixel. Ela é semelhante à versão básica do Android, mas inclui [personalizações adicionais e proprietárias desenvolvidas pelo Google] (https://www.howtogeek.com/google-pixel-devices-stock-android/).   
* One UI](https://es.wikipedia.org/wiki/One_UI): interface de usuário desenvolvida pela **Samsung** para dispositivos inteligentes, incluindo dispositivos móveis Android desde 2017. Há versões da One UI para telefones, tablets, smartwatches e computadores.  
* HyperOS](https://es.wikipedia.org/wiki/Xiaomi_HyperOS): interface de usuário desenvolvida pela **Xiaomi**, lançada em 2023, substituindo a interface de usuário anterior conhecida como [MIUI](https://es.wikipedia.org/wiki/MIUI).   
* ColorOS](https://es.wikipedia.org/wiki/ColorOS): o ColorOS é um sistema operacional móvel e uma interface de usuário criada pela **Oppo Electronics**.
* Realme UI](https://en.wikipedia.org/wiki/Realme): interface de usuário desenvolvida pela **Realme**, que, por sua vez, é uma subsidiária da [Oppo Electronics](https://en.wikipedia.org/wiki/Oppo), que também é proprietária da marca **OnePlus**.   
* Oxygen OS](https://en.wikipedia.org/wiki/OxygenOS): sistema operacional desenvolvido pela **OnePlus** exclusivamente para telefones celulares.    
* Harmony OS](https://en.wikipedia.org/wiki/HarmonyOS): sistema operacional desenvolvido pela **Huawei**. Embora às vezes seja posicionado como um sistema operacional diferente, ele é baseado no Android e na camada de personalização anterior, conhecida como [EMUI](https://en.wikipedia.org/wiki/EMUI).  
* Hello UI] (https://beebom.com/motorola-hello-ui-review/): interface desenvolvida pela **Motorola**, parte da **Lenovo**. [Este vídeo](https://www.google.com/url?q=https://www.youtube.com/watch?v%3Di3ZU9-TGJlE&sa=D&source=docs&ust=1753486266796661&usg=AOvVaw14C09MkoaBDTU4pbef9Aqq) mostra aspectos relevantes da interface.    
* Xperia UI](https://en.wikipedia.org/wiki/Sony_Xperia): interface de usuário desenvolvida pela **Sony** para dispositivos [Xperia](https://en.wikipedia.org/wiki/Sony_Xperia).   
* Magic OS](https://en.wikipedia.org/wiki/Honor_(brand)#MagicOS): sistema operacional desenvolvido pelo fabricante [**Honor](https://en.wikipedia.org/wiki/Honor_), anteriormente uma subsidiária da **Huawei**.

## Lista de instruções passo a passo

Abaixo estão os **passos a serem seguidos** para ativar o menu de opções do desenvolvedor em **diferentes dispositivos**, bem como uma captura de tela dos menus a serem seguidos para exibir esse menu.



### Google (Pixel OS)

Para habilitar as opções de desenvolvedor em dispositivos **Google** que usam **Pixel OS**, você pode seguir as seguintes etapas, também exemplificadas na **imagem 1.**.

1. abra o menu **Configurações** ⚙️
Navegue até a última opção **Sobre o telefone** 📱 3.
3. Localize as informações sobre o **Build number** 🔢
4. Pressione **7 vezes** no número de compilação, até ver uma mensagem de confirmação. 👆

![Etapas para ativar as opções de desenvolvedor em um dispositivo Google Pixel com Android 13](.../../../../../assets/02-how-to/enable-dev-options-Google.gif "image 1"){ loading=lazy }
/// legenda
**Imagem 1**. Etapas para ativar as opções de desenvolvedor em um dispositivo Google Pixel com Android 13.
///

As opções do desenvolvedor aparecerão como um novo submenu em **Sistema** e permanecerão **habilitadas** até serem desativadas (no menu de opções do desenvolvedor).   

### Honor (Magic OS)

Para ativar as opções de desenvolvedor nos dispositivos **Honor** que usam a versão **Magic OS** do Android, você pode seguir as etapas abaixo, também mostradas na **imagem 2**.

1. abra o menu **Configurações** ⚙️
Navegue até a última opção **Sobre o telefone** 📱 3.
3. Localize as informações sobre o **Número de compilação** 🔢
4. Pressione **7 vezes** no número de compilação, até ver uma mensagem de confirmação. 👆

As opções do desenvolvedor aparecerão como um novo submenu em **Sistema** e permanecerão **habilitadas** até serem desabilitadas (no menu de opções do desenvolvedor).   

Etapas para ativar as opções de desenvolvedor em um dispositivo Honor Magic Lite com Magic OS 7.1 no Android 13](.../../../../assets/02-how-to/02-like-enable-dev-options/developer-options/assets/enable-dev-options-Honor.gif "image 2"){ loading=lazy }
/// legenda
**imagem 2**. Etapas para ativar as opções de desenvolvedor em um dispositivo Honor Magic Lite com Magic OS 7.1 no Android 13.
///

### Motorola (Hello UI)

Para ativar as opções de desenvolvedor em dispositivos **Motorola** que usam a versão 13 do Android, você pode seguir as etapas abaixo, também exemplificadas na **imagem 3.

1. abra o menu **Configurações** ⚙️
Navegue até a última opção **Sobre o telefone** 📱 3.
3. Localize as informações sobre o **Build number** 🔢
4. Pressione **7 vezes** no número de compilação, até ver uma mensagem de confirmação. 👆

![Etapas para ativar as opções de desenvolvedor em um dispositivo Motorola Edge Neo 40 usando o Hi OS no Android 13](.../../../../assets/02-how-to/02-like-enable-dev-options-developer-options/assets/enable-dev-options-Motorola.gif "image 4"){ loading=lazy }
/// legenda
**imagem 3**. Etapas para ativar as opções do desenvolvedor em um dispositivo Motorola Edge Neo 40 usando o Hi OS no Android 13.
///


### Nokia

Para ativar as opções de desenvolvedor em dispositivos **Nokia** que usam a versão 13 ou superior do Android, você pode seguir as etapas abaixo, também mostradas na **imagem 4.

1. abra o menu **Configurações** ⚙️
Navegue até a última opção **Sobre o telefone** 📱 3.
3. Localize as informações sobre o **Número de compilação** 🔢
4. Pressione **7 vezes** no número de compilação, até ver uma mensagem de confirmação. 👆

As opções do desenvolvedor aparecerão como um novo submenu em **Sistema** e permanecerão **habilitadas** até serem desabilitadas (no menu de opções do desenvolvedor).

Etapas para ativar as opções do desenvolvedor em um dispositivo Nokia G42 5G usando o Android 13](.../../../../assets/02-how-to/02-como-ativar-opções-do-desenvolvedor/assets/enable-dev-options-Nokia.gif "image 4"){ loading=lazy }
/// legenda
**imagem 4**. Etapas para habilitar as opções de desenvolvedor em um dispositivo Nokia G42 5G usando o Android 13.
///

### Oppo Reno 10 (Color OS)

Para ativar as opções de desenvolvedor em um dispositivo Nokia G42 5G usando o Android 13.Se você **OPPO** estiver usando o Android versão 13 ou superior, poderá seguir as etapas a seguir, também exemplificadas na **imagem 5.

1. abra o menu **Configurações** ⚙️
Navegue até a última opção **Sobre o telefone** 📱 3.
3. Localize as informações sobre o **Número da versão** 🔢 4.
4. Pressione **7 vezes** no número da versão, até ver uma mensagem de confirmação. 👆

As opções do desenvolvedor aparecerão como um novo submenu em **Sistema** e permanecerão **habilitadas** até serem desabilitadas (no menu de opções do desenvolvedor).

Etapas para ativar as opções de desenvolvedor em um dispositivo Oppo Android 13](.../../../../assets/02-how-to/02-like-enable-dev-options/dev-options/assets/enable-dev-options-oppo.gif "image 5"){: style="height:480x;width:216px"}
/// legenda
**Imagem 5**. Etapas para ativar as opções de desenvolvedor em um dispositivo Oppo.
///

### Realme (Realme UI)

Para ativar as opções de desenvolvedor em dispositivos **Realme** usando a camada de personalização da Realme UI, você pode seguir as etapas abaixo, também exemplificadas na **imagem 6.

1. abra o menu **Configurações** ⚙️
Navegue até a última opção **Sobre o dispositivo** 📱 3.
3. Entre no menu **versão** 📝 4.
4. Localize as informações do **Build Number** 🔢 🔢 5.
5. Pressione **7 vezes** no número de compilação até ver uma mensagem de confirmação. 👆

![Etapas para ativar as opções de desenvolvedor em um dispositivo Realme GT2 Pro com RealMe UI 4.0 usando o Android 13](../../../../assets/02-how-to/02-like-enable-dev-options/developer-options/assets/enable-dev-options-Realme.gif "image 6"){ loading=lazy }
/// legenda
**imagem 6**. Etapas para ativar as opções de desenvolvedor em um dispositivo Realme GT2 Pro com RealMe UI 4.0 usando o Android 13
///

### Samsung (One UI)

Para ativar as opções de desenvolvedor em dispositivos **Samsung** usando a camada de personalização One UI, você pode seguir as etapas abaixo, também exemplificadas na **imagem 7.

1. abra o menu **Configurações ⚙️** 2.
Navegue até a última opção **Sobre o telefone** 📱 3.
3. Entre no menu **Informações de software** 📝 4.
4. Localize as informações do **Build Number** 🔢 🔢 5.
5. Pressione **7 vezes** no número de compilação até ver uma mensagem de confirmação. 👆

Etapas para ativar as opções de desenvolvedor em um dispositivo Samsung Galaxy A54 com One UI em um dispositivo com Android 13](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExdnB4bTJ0dWpnaWVsY2s0aWVnYTZyejN3a3N1bnhwZnV2NW10cGN2eSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ctCvv5Is6UZ6CEhQ4D/giphy.gif "image 7"){ loading=lazy }
/// legenda
**Imagem 7**. Etapas para ativar as opções de desenvolvedor em um dispositivo Samsung Galaxy A54 com One UI em um dispositivo com Android 13
///

### Sony (Xperia UI)

Para ativar as opções de desenvolvedor em dispositivos **Xperia** usando a camada de personalização da Xperia UI, você pode seguir as etapas abaixo, também exemplificadas na **imagem 8.

1. abra o menu **Configurações** ⚙️
Navegue até a última opção **Sobre o telefone** 📱 3.
3. Localize as informações sobre o **Número de compilação** 🔢
4. Pressione **7 vezes** no número de compilação até ver uma mensagem de confirmação. 👆

![Etapas para ativar as opções de desenvolvedor em um dispositivo Sony Xperia 10V com Xperia UI 4.0 usando o Android 14](../../../assets/02-how-to/02-like-enable-dev-options/assets/enable-dev-options-Sony.gif "image 8"){ loading=lazy }
/// legenda
**imagem 8**. Etapas para habilitar as opções de desenvolvedor em um dispositivo Sony Xperia 10V com Xperia UI 4.0 usando o Android 14.0.
///


### Techno (Hi OS)

Para ativar as opções de desenvolvedor nos dispositivos **Tecno Spark** que usam a camada de personalização Hi OS, você pode seguir as etapas abaixo, também exemplificadas na **imagem 9.

1. abra o menu **Settings** (Configurações) ⚙️
Navegue até a opção **My Phone** 📱 3.
3. Localize a informação **Compilation number** 🔢 🔢 4.
4. Pressione **7 vezes** no número de compilação até ver uma mensagem de confirmação. 👆

Etapas para ativar as opções de desenvolvedor em um dispositivo Tecno Spark Go com Hi OS usando o Android 13](../../../../../assets/02-how-to/02-as-enable-dev-options-developer-options/assets/enable-dev-options-Tecno.gif "image 9"){ loading=lazy }
/// legenda
**imagem 9**. Etapas para ativar as opções de desenvolvedor em um dispositivo Tecno Spark Go com Hi OS usando o Android 13.
///

### Xiaomi (Hyper OS)

Para ativar as opções de desenvolvedor em dispositivos **Xiaomi** que usam a camada de personalização do Hyper OS, você pode seguir as etapas abaixo, também exemplificadas na **imagem 10.**.

1. abra o menu **Configurações** ⚙️
2. vá para a opção **About** (Sobre). do telefone** 📱
3. Localize as informações da **Versão do sistema operacional** 🔢 🔢 4.
4. Pressione **7 vezes** no número de compilação até ver uma mensagem de confirmação. 👆

![Etapas para ativar as opções de desenvolvedor em um dispositivo Xiamoi](.../../../../assets/02-how-to/02-like-enable-dev-options/assets/enable-dev-options-Xiaomi.gif "image 10"){ loading=lazy }
/// legenda
**imagem 10**. Etapas para habilitar as opções de desenvolvedor em um dispositivo Xiamoi.
///

As opções do desenvolvedor aparecerão como um novo submenu em **Opções avançadas** e permanecerão **habilitadas** até serem desativadas (no menu de opções do desenvolvedor).

## Conclusão

A interface gráfica dos dispositivos Android varia entre os fabricantes que usam o [Android Open Source Project (AOSP)] (https://source.android.com/?hl=es-419) como base. Cada fabricante constrói seus próprios desenvolvimentos sobre essa camada de base, com diferentes níveis de personalização, resultando em interfaces com **aparência, menus e opções diferentes**.

O menu **developer options** é um menu oculto, que é ativado por meio de um procedimento simples na GUI, e é necessário para modificar **as principais opções necessárias durante um processo de extração forense**, como o console ADB ou um relatório de bug. Esse recurso compila **capturas de tela de diferentes fabricantes** e interfaces, com a intenção de **facilitar aos analistas da sociedade civil a ativação das opções do desenvolvedor**.

Se **você tem acesso a uma GUI que não é mostrada na lista** e gostaria de incorporar a captura de tela correspondente a esse recurso, escreva para nós por meio de um *[issue](../../community/how-to-contribute/index.md#proposals-for-improvements-or-corrections-through-issues)* ou, se você estiver familiarizado com markdown, pode enviar uma solicitação de integração por meio de um *[pull request](../../community/how-to-contribute/index.md#requests-for-integration-through-pull-request)*.


## Comentários

Você tem **comentários ou sugestões** sobre este recurso? Você pode usar a função **comentário abaixo** para nos deixar suas ideias ou comentários. Certifique-se de seguir nosso [código de conduta](../../community/code-of-conduct/). A função de comentário está vinculada diretamente à seção [_Discussions_ do Github] (https://github.com/Socialtic/forensics/discussions), onde você também pode **participar diretamente das discussões**, se preferir.   


