---
name: mog-231-sicurezza-lavoro
description: "Supporto documentale al Modello di Organizzazione e Gestione (MOG) 231 in materia di salute e sicurezza sul lavoro, cioe' il modello con efficacia esimente della responsabilita' amministrativa dell'ente per i reati di omicidio colposo e lesioni gravi o gravissime commessi con violazione delle norme antinfortunistiche. Aiuta a inquadrare i presupposti della responsabilita' dell'ente (reato commesso nel suo interesse o vantaggio da soggetti apicali o sottoposti - art. 5 D.Lgs 231/2001), le condizioni dell'esimente per gli apicali (adozione ed efficace attuazione di un modello idoneo, organismo di vigilanza con autonomi poteri, elusione fraudolenta, assenza di omessa vigilanza - art. 6) e per i sottoposti (art. 7), il reato presupposto (art. 25-septies, omicidio/lesioni colpose sul lavoro, con sanzioni pecuniarie in quote e interdittive) e soprattutto i requisiti del MOG di cui all'art. 30 del D.Lgs 81/2008: il sistema aziendale per l'adempimento degli obblighi giuridici (standard tecnico-strutturali, valutazione dei rischi, gestione emergenze/appalti/sorveglianza sanitaria/informazione-formazione, vigilanza, documentazioni obbligatorie, verifiche periodiche), i sistemi di registrazione, l'articolazione di funzioni e il sistema disciplinare, il controllo/riesame/aggiornamento del modello e la presunzione di conformita' per i modelli conformi alle Linee guida UNI-INAIL SGSL o alla UNI EN ISO 45001. Use when an engineer, RSPP, employer or consultant must set up or review the mapping of work-safety criminal risk and the structure of the safety MOG under art. 30 D.Lgs 81/2008; it is a documentary aid and does NOT draft the model, does not certify its adequacy (reserved to the judge) and does not cover other 231 predicate-offence families (e.g. environmental - see mog-231-reati-ambientali)."
license: MIT
area: sicurezza-lavoro-cantieri
title: "MOG 231 salute e sicurezza sul lavoro (art. 30 D.Lgs 81/2008 + art. 25-septies)"
summary: "MOG 231 per la sicurezza sul lavoro: responsabilita' dell'ente ed esimente (artt. 5-7 D.Lgs 231/2001), reato art. 25-septies (omicidio/lesioni colpose sul lavoro) e requisiti del modello esimente (art. 30 D.Lgs 81/2008). Non redige il modello ne' ne certifica l'idoneita'."
normative_refs:
  - "D.Lgs. 231/2001 artt. 5, 6, 7 (responsabilita' ed esimente) e 25-septies (reato presupposto)"
  - "D.Lgs. 81/2008 art. 30 (requisiti del MOG con efficacia esimente)"
version: 0.1.0-alpha
status: alpha
tags:
  - mog-231
  - sicurezza-lavoro
  - art-25-septies
  - art-30-dlgs81
  - responsabilita-enti
---

# MOG 231 salute e sicurezza sul lavoro (art. 30 D.Lgs 81/2008 + art. 25-septies)

## Quando usare questa skill

Usala quando, come **ingegnere, RSPP, datore di lavoro o consulente**, devi
**impostare o verificare** la mappatura del **rischio-reato in materia di sicurezza sul
lavoro** e la **struttura del MOG** (Modello di Organizzazione e Gestione) con
**efficacia esimente** della responsabilita' 231 dell'ente:

- inquadrare **quando l'ente risponde** (reato nel suo interesse/vantaggio, da apicali o
  sottoposti - art. 5 D.Lgs 231/2001);
- individuare le **condizioni dell'esimente** (modello idoneo ed efficacemente attuato,
  **organismo di vigilanza**, elusione fraudolenta, assenza di omessa vigilanza - artt.
  6-7);
- riconoscere il **reato presupposto** (art. 25-septies: omicidio colposo e lesioni
  gravi/gravissime con violazione delle norme antinfortunistiche - sanzioni in **quote** e
  **interdittive**);
- strutturare il **MOG** secondo i **requisiti dell'art. 30 D.Lgs 81/2008**.

## Reato presupposto (art. 25-septies)

- **Omicidio colposo** (art. 589 c.p.) e **lesioni gravi/gravissime** (art. 590 c.p.)
  commessi **con violazione delle norme sulla salute e sicurezza sul lavoro**.
- Sanzioni **pecuniarie** (in quote, fino a 1.000 quote nei casi piu' gravi) e
  **interdittive** (art. 9 c.2), secondo la gravita' del caso.

## Requisiti del MOG con efficacia esimente (art. 30 D.Lgs 81/2008)

Il modello deve assicurare un **sistema aziendale** per l'adempimento degli obblighi:

1. **standard tecnico-strutturali** (attrezzature, impianti, luoghi di lavoro, agenti);
2. **valutazione dei rischi** e misure di prevenzione/protezione;
3. **attivita' organizzative** (emergenze, primo soccorso, appalti, riunioni periodiche,
   consultazione RLS);
4. **sorveglianza sanitaria**; **informazione e formazione**; **vigilanza**;
5. **acquisizione documentazioni/certificazioni** obbligatorie; **verifiche periodiche**.

Inoltre: **sistemi di registrazione** dell'avvenuta effettuazione (c.2); **articolazione
di funzioni** con competenze/poteri e **sistema disciplinare** (c.3); **controllo,
riesame e aggiornamento** del modello (c.4); **presunzione di conformita'** per i modelli
definiti secondo le **Linee guida UNI-INAIL SGSL (2001)** o la **UNI EN ISO 45001** (c.5);
**procedure semplificate PMI** (c.5-bis) e **modelli semplificati** micro/PMI (c.5-ter).

## Cosa NON fa (limiti)

- **Non redige il modello** ne' i suoi protocolli: struttura la mappatura e i requisiti,
  non li scrive per l'azienda.
- **Non certifica l'idoneita'** del modello: il giudizio di idoneita'/efficace attuazione
  spetta in ultima analisi al **giudice** (l'esimente e' valutata nel processo).
- **Non copre gli altri reati presupposto 231** (es. ambientali - vedi
  `mog-231-reati-ambientali`; o la mappatura generale multi-reato).
- Non sostituisce il **DVR** ne' gli adempimenti del D.Lgs 81/2008 (il MOG li presuppone
  e li sistematizza).

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`mappa-rischio-reato`](tasks/mappa-rischio-reato.md) | Inquadra i presupposti della responsabilita' (art. 5), l'esimente (artt. 6-7) e il reato art. 25-septies, e mappa le attivita' aziendali a rischio di omicidio/lesioni colpose |
| [`struttura-mog-art30`](tasks/struttura-mog-art30.md) | Struttura i requisiti del MOG secondo l'art. 30 D.Lgs 81/2008 (obblighi a-h, registrazione, funzioni/sistema disciplinare, controllo/riesame, presunzione di conformita') |

## Riferimenti normativi

- **D.Lgs. 231/2001** - artt. **5** (responsabilita' dell'ente), **6-7** (modelli ed
  esimente per apicali/sottoposti), **25-septies** (omicidio/lesioni colpose sul lavoro).
- **D.Lgs. 81/2008** - **art. 30** (requisiti del MOG con efficacia esimente; presunzione
  di conformita' UNI-INAIL SGSL / UNI EN ISO 45001).

Dettaglio in `references/sources.yaml`,
`references/fonti/mog-231-sicurezza-lavoro.md`,
`references/estratti/mog-231-sicurezza-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: l'idoneita' e l'efficace attuazione del modello, e
quindi l'efficacia esimente, dipendono dall'organizzazione concreta e sono valutate dal
**giudice**. La skill **non sostituisce** il consulente legale, l'RSPP ne' l'organismo di
vigilanza, e non certifica il modello.
