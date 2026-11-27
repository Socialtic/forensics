---
title: "[2026-11] Technical triage on Android with MVT"
summary: Four new materials on technical triage of Android devices using MVT
keywords: changelog, triage, android, mvt
lang: en
tags: [changelog, android, mvt]
last_updated: 2026-11-27
some_url:
icon: material/android
created: 2026-11-27
comments: true
author:
    name: Daniel
    url: https://socialtic.org/quienes-somos/
    description: SocialTIC
auto-translate: false
---

# [2026-11] Technical triage on Android with MVT

## TL;DR

In November 2026 we published **four new materials available in Spanish and English**, all **related to the process of technical triage of Android devices** using the MVT tool. These materials aim to **support you throughout this process**, from understanding key concepts and how the tool works, to interpreting MVT's outputs.

## Description of the new materials

In the context of this repository, we define **technical triage** as *the bounded, hypothesis-driven review of readily available device artifacts (bugreport, AndroidQF extraction, intrusion logs, etc.) to identify [indicators of compromise](../../../references/00-glossary/index.md#indicator-of-compromise-ioc) or [TTPs](../../../references/00-glossary/index.md#ttp) consistent with known attack vectors.*

To support this review process, we are making the following new materials available:

| Material | What is it for? |
| ----- | ----- |
| [Explainer: Introduction to technical triage of Android devices](../../../explainers/04-explainer-introduction-android-triage/index.md) | **Learning material** that explores key concepts and considerations when approaching a triage process, including **formulating hypotheses** and how to approach an **initial interview** with the person requesting support. |
| [Explainer: Exploring MVT for technical triage on Android](../../../explainers/05-explainer-mvt-android-triage/index.md) | **Learning material** that explores how the **MVT tool** works, including its Android modules, and the **mental model for triaging** with this tool. |
| [Tutorial: Using MVT for technical triage on Android](../../../tutorials/02-tutorial-mvt-android-triage/index.md) | **Learning material** with a **guided exercise** based on a hypothetical case, using a **test extraction** generated with AndroidQF to reach initial conclusions from the analysis of MVT's output. |
| [How-to: Technical triage of Android devices using MVT](../../../how-tos/06-how-to-triage-android-mvt/index.md) | Material for **use during case handling and execution**, including the **commands** and steps to follow, for **people already familiar** with the tools. |

## How to approach these new materials?

If this is your first time approaching technical triage on Android with MVT, we recommend the following reading order:

1. Start with the [*Explainer: Introduction to technical triage of Android devices*](../../../explainers/04-explainer-introduction-android-triage/index.md) to understand the key concepts and the triage process.
2. Continue with the [*Explainer: Exploring MVT for technical triage on Android*](../../../explainers/05-explainer-mvt-android-triage/index.md) to learn more about the MVT tool and how it works.
3. Put what you learned to the test by following the [*Tutorial: Using MVT for technical triage on Android*](../../../tutorials/02-tutorial-mvt-android-triage/index.md).
4. Keep the [*How-to: Technical triage of Android devices using MVT*](../../../how-tos/06-how-to-triage-android-mvt/index.md) as a reference for future cases.

## Acknowledgements

**We thank the 0xCHE team for their reviews and suggestions.** We also recognize the **effort and leadership of Amnesty International's Security Lab in developing the MVT tool**, as well as their work strengthening the consensual forensics community around the world through their [Digital Forensics Fellowship](https://securitylab.amnesty.org/digital-forensics-fellowship/) program. These materials aim to be compatible with and complementary to these technological and methodological efforts.

Any errors or omissions are the responsibility of SocialTIC.

## Feedback

We'd love to hear how you use these materials and what we can improve. You can leave a comment below or check [how to collaborate with this repository](../../how-to-contribute/index.md).
