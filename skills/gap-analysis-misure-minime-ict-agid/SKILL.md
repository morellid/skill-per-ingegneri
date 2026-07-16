---
name: gap-analysis-misure-minime-ict-agid
description: "Supporto alla gap analysis delle Misure Minime di Sicurezza ICT per le pubbliche amministrazioni (MMS-PA), basate sugli AgID Basic Security Control(s) (ABSC) di cui alla Circolare AgID 18/4/2017 n. 2/2017 (attuazione art. 14-bis C.A.D. e direttiva PCM 1/8/2015). Aiuta a inquadrare l'ambito soggettivo (le PA e i soggetti dell'art. 2 c.2 del C.A.D.), il responsabile dell'attuazione (art. 3), il modulo di implementazione da compilare, firmare digitalmente con marcatura temporale e conservare (art. 4, Allegato 2), i tempi (art. 5) e soprattutto la struttura degli otto gruppi di controlli ABSC (ABSC 1 inventario dispositivi, 2 inventario software, 3 protezione delle configurazioni, 4 valutazione e correzione delle vulnerabilita', 5 uso appropriato dei privilegi di amministratore, 8 difese contro i malware, 10 copie di sicurezza, 13 protezione dei dati) e i tre livelli di attuazione (Minimo, soglia obbligatoria sotto la quale nessuna amministrazione puo' scendere; Standard, base di riferimento; Alto, obiettivo a cui tendere). Guida a impostare la gap analysis controllo per controllo e la conseguente compilazione del modulo. Use when a public administration (or a supplier/consultant working for it) must assess its posture against the Italian minimum ICT security measures and fill in the AgID implementation module; it is a documentary/gap-analysis aid and does NOT reproduce the full per-control matrix (the exact Minimo/Standard/Alto flags per ABSC_ID are a graphic table in the cited PDF), does not perform the technical security assessment and does not replace the responsible officer's determinations or newer obligations (e.g. NIS2 - D.Lgs 138/2024)."
license: MIT
area: software-dati-cybersecurity
title: "Gap analysis Misure Minime ICT AgID (ABSC - Circ. 2/2017)"
summary: "Gap analysis delle Misure Minime ICT per le PA (ABSC, Circ. AgID 2/2017): ambito, responsabile, modulo di implementazione (artt. 2-4), 8 gruppi di controlli (ABSC 1,2,3,4,5,8,10,13) e 3 livelli (Minimo obbligatorio, Standard, Alto). Non riproduce la matrice grafica dei controlli."
normative_refs:
  - "Circolare AgID 18/4/2017 n. 2/2017 (Misure minime di sicurezza ICT per le PA - ABSC)"
  - "D.Lgs. 82/2005 (C.A.D.) art. 14-bis e art. 2 c.2 (ambito) + direttiva PCM 1/8/2015"
version: 0.1.0-alpha
status: alpha
tags:
  - abscagid
  - misure-minime-ict
  - cybersecurity-pa
  - circolare-agid-2-2017
  - gap-analysis
---

# Gap analysis Misure Minime ICT AgID (ABSC - Circ. 2/2017)

## Quando usare questa skill

Usala quando una **pubblica amministrazione** (o un fornitore/consulente che lavora
per essa) deve **valutare la propria posizione** rispetto alle **Misure Minime di
Sicurezza ICT** (MMS-PA) basate sugli **AgID Basic Security Control(s) (ABSC)** della
**Circolare AgID 2/2017**, e **compilare il modulo di implementazione**:

- inquadrare **chi e' destinatario** (i soggetti dell'art. 2 c.2 del C.A.D.) e **chi e'
  responsabile** dell'attuazione (art. 3);
- impostare la **gap analysis** controllo per controllo sugli **8 gruppi ABSC**;
- assegnare a ciascun controllo il **livello** (Minimo/Standard/Alto) e lo **stato di
  attuazione**;
- predisporre il **modulo di implementazione** (Allegato 2) da **firmare digitalmente
  con marcatura temporale** e **conservare** (da trasmettere al CERT-PA in caso di
  incidente) (art. 4).

## Gli 8 gruppi di controlli ABSC

| ABSC | Oggetto |
|---|---|
| **1** | Inventario dei dispositivi autorizzati e non autorizzati |
| **2** | Inventario dei software autorizzati e non autorizzati |
| **3** | Proteggere le configurazioni di hardware e software (dispositivi mobili, laptop, workstation, server) |
| **4** | Valutazione e correzione continua della vulnerabilita' |
| **5** | Uso appropriato dei privilegi di amministratore |
| **8** | Difese contro i malware |
| **10** | Copie di sicurezza |
| **13** | Protezione dei dati |

Ogni ABSC e' un **identificatore gerarchico a tre livelli `x.y.z`** (famiglia →
controllo → misura elementare), con una colonna **FNSC** che lo raccorda al Framework
Nazionale per la Cyber Security.

## I tre livelli di attuazione

- **Minimo**: la **soglia sotto la quale nessuna amministrazione puo' scendere**; i
  controlli cosi' marcati sono **obbligatori**.
- **Standard**: base di riferimento assumibile nella maggior parte dei casi.
- **Alto**: obiettivo a cui tendere (strutture complesse/eterogenee).

> Le amministrazioni NSC, per l'infrastruttura che gestisce dati NSC, dovrebbero
> collocarsi almeno a livello "standard".

## Cosa NON fa (limiti)

- **Non riproduce la matrice completa** dei singoli controlli con i flag esatti
  Minimo/Standard/Alto per ogni `ABSC_ID`: quella e' una **tabella in formato grafico**
  nel PDF ufficiale (pagg. ~68-73) e il livello esatto va **letto sul PDF citato**.
- **Non esegue l'assessment tecnico** (scansioni, inventari, test): la skill imposta la
  gap analysis, non la conduce sul campo.
- **Non sostituisce** le determinazioni del **responsabile** dell'attuazione (art. 3)
  ne' considera obblighi piu' recenti che si aggiungono per alcuni soggetti (es. **NIS2
  - D.Lgs 138/2024**, per cui vedi la skill `nis2-self-assessment`).

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`imposta-gap-analysis`](tasks/imposta-gap-analysis.md) | Per ciascun gruppo ABSC (1-13) imposta la valutazione controllo per controllo: livello (Minimo/Standard/Alto), stato di attuazione, evidenze e azioni |
| [`compila-modulo-implementazione`](tasks/compila-modulo-implementazione.md) | Struttura il modulo di implementazione (Allegato 2) con responsabile (art. 3), firma digitale e marcatura temporale, conservazione e trasmissione al CERT-PA (art. 4) |

## Riferimenti normativi

- **Circolare AgID 18/4/2017 n. 2/2017** - Misure minime di sicurezza ICT per le PA
  (Premessa, art. 1 Scopo, art. 2 destinatari, art. 3 responsabile, art. 4 modulo di
  implementazione, art. 5 tempi; Allegato 1 - ABSC; Allegato 2 - modulo).
- **D.Lgs. 82/2005 (C.A.D.)** - art. 14-bis (funzioni AgID) e art. 2 c.2 (ambito
  soggettivo); **direttiva PCM 1 agosto 2015**.

Dettaglio in `references/sources.yaml`,
`references/fonti/circolare-agid-2-2017.md`,
`references/estratti/absc-gap-analysis-checklist.md`.

## Avvertenza

Skill di **supporto documentale alla gap analysis**: l'individuazione dei controlli
applicabili, del livello adeguato e dello stato reale di attuazione richiede l'analisi
tecnica dei sistemi e la responsabilita' del soggetto designato (art. 3). La skill
**non sostituisce** l'assessment tecnico, il responsabile dell'attuazione ne' la lettura
delle tabelle ABSC nel PDF ufficiale.
