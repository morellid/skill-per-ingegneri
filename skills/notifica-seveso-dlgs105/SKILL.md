---
name: notifica-seveso-dlgs105
description: "Supporto documentale agli obblighi di uno stabilimento a rischio di incidente rilevante (Seveso III, D.Lgs. 105/2015): aiuta a determinare se lo stabilimento e' soggetto al decreto (presenza di sostanze pericolose dell'allegato 1 sopra soglia, esclusioni dell'art. 2), a classificarlo come stabilimento di soglia inferiore o superiore (colonne 2 e 3 dell'allegato 1, regola della sommatoria nota 4), e a impostare gli adempimenti: notifica al CTR, Regione, MASE tramite ISPRA, Prefettura, Comune e VVF (art. 13, modulo allegato 5, termini 180/60 giorni o 1 anno), politica di prevenzione degli incidenti rilevanti e SGS (art. 14, per tutti), rapporto di sicurezza (art. 15, solo soglia superiore), con sanzioni penali e diffida/sospensione/chiusura (art. 28). Use when an operator or consultant must decide whether an Italian establishment falls under the Seveso III decree, its lower/upper tier and the resulting notification and documentary duties; it is a documentary aid and does not read the substance thresholds nor draft the safety report."
license: MIT
area: ambiente-territorio-mobilita
title: "Notifica e adempimenti Seveso III - D.Lgs. 105/2015"
summary: "Obblighi degli stabilimenti a rischio di incidente rilevante (Seveso III, D.Lgs. 105/2015): assoggettabilita' (art. 2), soglia inferiore/superiore (allegato 1), notifica (art. 13), PPIR/SGS (art. 14), rapporto di sicurezza soglia superiore (art. 15), sanzioni (art. 28)"
normative_refs:
  - "D.Lgs. 26/6/2015 n. 105 (testo vigente) - artt. 2, 3, 13, 14, 15, 28 (attuazione dir. 2012/18/UE Seveso III)"
version: 0.1.0-alpha
status: alpha
tags:
  - dlgs-105-2015
  - seveso-iii
  - incidente-rilevante
  - notifica
  - sostanze-pericolose
---

# Notifica e adempimenti Seveso III - D.Lgs. 105/2015

## Quando usare questa skill

Usala quando devi orientarti sugli obblighi di uno **stabilimento a rischio di
incidente rilevante** ai sensi del **D.Lgs. 105/2015** (Seveso III, attuazione
della direttiva 2012/18/UE):

- capire se uno stabilimento **e' soggetto** al decreto (presenza di sostanze
  pericolose dell'allegato 1 sopra soglia; esclusioni dell'art. 2);
- classificarlo come **stabilimento di soglia inferiore** o **superiore**
  (art. 3, colonne 2/3 dell'allegato 1, regola della sommatoria);
- impostare gli adempimenti: **notifica** (art. 13), **politica di prevenzione**
  degli incidenti rilevanti e SGS (art. 14), **rapporto di sicurezza** (art. 15);
- conoscere destinatari, termini e **sanzioni** (art. 28).

**Non e' una skill di calcolo**: non legge le soglie sostanza-specifiche
dell'allegato 1, non applica la regola della sommatoria, non redige il rapporto
di sicurezza ne' i piani di emergenza.

## Cosa NON fa (limiti)

- Non stabilisce le **soglie** dell'allegato 1 ne' esegue la **regola della
  sommatoria** (nota 4): rinvia all'allegato 1 e alla classificazione CLP
  (Reg. 1272/2008).
- Non redige **RdS**, **PPIR**, **SGS** ne' i piani di emergenza interna/esterna.
- Non copre l'istruttoria del RdS (art. 17), il nulla osta di fattibilita', la
  pianificazione territoriale (art. 22), l'informazione al pubblico (art. 23-24)
  se non nei richiami.
- Non sostituisce il gestore, il CTR, l'ISPRA ne' i tecnici incaricati.

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`verifica-assoggettabilita`](tasks/verifica-assoggettabilita.md) | Dato il profilo dello stabilimento (sostanze pericolose e quantita', attivita', esclusioni), determina se e' soggetto al decreto e se e' di soglia inferiore o superiore, rinviando all'allegato 1 per le soglie |
| [`checklist-adempimenti`](tasks/checklist-adempimenti.md) | Verifica la completezza degli adempimenti (notifica art. 13, PPIR/SGS art. 14, RdS art. 15) con destinatari, termini e sanzioni |

## Riferimenti normativi

- **D.Lgs. 26/6/2015 n. 105** (Seveso III), testo vigente su Normattiva:
  - art. 2 (ambito ed esclusioni), art. 3 (definizioni: soglia inferiore/
    superiore, gestore, sostanza pericolosa, incidente rilevante);
  - art. 13 (notifica), art. 14 (PPIR/SGS), art. 15 (rapporto di sicurezza);
  - art. 28 (sanzioni).

Dettaglio in `references/sources.yaml`, `references/fonti/dlgs-105-2015.md`,
`references/estratti/notifica-seveso-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: la determinazione delle soglie e della
classificazione richiede la lettura dell'allegato 1 e della classificazione CLP;
la valutazione finale spetta al gestore e alle autorita' competenti (CTR, ISPRA,
Regione).
