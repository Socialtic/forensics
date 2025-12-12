---

title: Comunidad - Traducciones y localizaciones
summary: Consideraciones sobre traducciones y localizaciones
keywords: forense, comunidad, contribucion, traducción, traducir
lang: es
tags: [comunidad, intro, traducir]
last_updated: 2025-07-14
some_url:
author:
    name: Daniel
    url: https://socialtic.org/quienes-somos/
    description: SocialTIC
translation-review-pending: true
---

Na SocialTIC, entendemos a importância de manter **recursos que sejam acessíveis**, **fáceis de ler** e que possam ter impacto em **populações com diferentes capacidades técnicas e em várias regiões do mundo**. Devido à nossa experiência e localização geográfica, nossos recursos geralmente estarão **disponíveis primeiro em espanhol** e depois traduzidos para os outros idiomas disponíveis.

Para facilitar esse processo de tradução, foi desenvolvido um script que usa a API *deepl* para gerar traduções automáticas e integrá-las por meio de solicitações pull. Esse script está [descrito em detalhes na documentação correspondente] (https://github.com/socialtic/forensics/blob/main/scripts/translate-readme.md). Esse script automático requer revisões manuais, portanto, se você estiver interessado em **colaborar com a tradução de recursos do espanhol para o inglês**, ou vice-versa, escreva para [**seguridad@socialtic.org**](mailto:seguridad@socialtic.org).

Embora esse script de tradução automática facilite a localização de recursos, há algumas considerações importantes antes de iniciar uma tradução:

* Capacidade e sustentabilidade: a tradução e a localização de conteúdo é um **trabalho árduo**, e nós da **SocialTIC agradecemos qualquer esforço** que impulsione a análise forense consensual em populações vulneráveis, especialmente a maioria global. Entretanto, antes de iniciar uma tradução, recomendamos **avaliar a sustentabilidade do esforço** a médio e longo prazo.  
* Revisão de conteúdo: Em nossa experiência, o ideal é que, além da tradução inicial, **uma segunda pessoa faça uma revisão secundária**. Se estiver com dificuldades para identificar uma segunda pessoa para revisar uma tradução, informe-nos para que possamos ajudar na coordenação.   
* Atualização e manutenção: Nossa visão é que o **repositório estará em constante crescimento e atualização**. Esperamos que os **primeiros anos sejam os mais intensivos** na produção de conteúdo de triagem e aquisição e, em seguida, nos concentremos em conteúdo mais especializado.   
* Regras de estilo: sugerimos a geração de breves regras de estilo que considerem, por exemplo, o **uso de anglicismos, linguagem inclusiva, entre outros**.    
* Licença de uso: este repositório estende [a licença MVT] (https://docs.mvt.re/en/latest/license/) para incentivar a análise forense consensual.

### Organização do conteúdo

O repositório está **estruturado para aceitar traduções para novos idiomas**. O plug-in [mkdocs-static-i18n] (https://ultrabug.github.io/mkdocs-static-i18n/) é usado para lidar com as traduções.

A configuração da pasta é usada, portanto, em geral, o conteúdo em todos os idiomas **é estruturado da seguinte forma**, com os **nomes das pastas em inglês**. A estrutura para o idioma espanhol é mostrada abaixo:

```
docs/
  es/
    localized-assets/
      recurso 1/
        image1.png
    home/
      começando/
        index.md
      roadmap/
        index.md
    explicadores/
      explainer-topic-01/
        índice.md
      explicador-tópico-n/
        index.md
    how-tos/
      how-to-topic-01/
        index.md
      how-to-topic-n/
        index.md
    tutorials/
      tutorial-topic-01/
        index.md
      tutorial-topic-n/
        index.md
    referências/
      reference-topic-01/
        índice.md
      referência-topic-n/
        índice.md
    index.md

```

**Cada novo conteúdo terá sua própria pasta correspondente**, onde está hospedado o arquivo markdown denominado 'index.md' com o conteúdo. Por exemplo, o conteúdo *Explainer:* *Introdução à perícia digital consensual para a defesa dos direitos humanos* está organizado da seguinte forma nos idiomas inglês e espanhol:

```
en/
  explainers/
    01-explainer-introduction-digital-forensics/
      index.md

en/ en/
  explainers/
    01-explainer-introduction-digital-forensics/
      index.md
	
```

Como você pode ver, **não há diferença no nome dos arquivos ou pastas**, e a única diferença está na pasta em que a documentação é colocada.

Para fazer contribuições diretamente para o repositório em relação às traduções, é recomendável seguir as instruções na seção *pull requests* (../how-to-contribute/index.md#pull-requests).
