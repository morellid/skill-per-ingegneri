---
name: garanzie-appalti-pubblici-dlgs36
description: "Supporto documentale all'inquadramento delle garanzie negli appalti pubblici ai sensi del D.Lgs. 36/2023 (Codice dei contratti pubblici). Aiuta a distinguere la garanzia provvisoria per la partecipazione alla procedura (art. 106: 2% del valore, riducibile all'1% o incrementabile al 4%; forme cauzione/fideiussione; requisiti di rinuncia alla preventiva escussione ed all'eccezione ex art. 1957 c.c., operativita' 15 giorni, efficacia >= 180 giorni; cosa copre; riduzioni per qualita', PMI, fideiussione digitale e certificazioni; svincolo automatico) dalla garanzia definitiva (art. 117: 10% dell'importo contrattuale, maggiorazione per ribassi > 10%/20%, oggetto e durata fino al collaudo/CRE, svincolo progressivo fino all'80%, sostituzione con ritenuta nei lavori, escussione, coperture assicurative CAR e RCT, polizza decennale postuma e schemi tipo). Use when a RUP, tender officer or economic operator must frame which guarantee applies, its amount, reductions, insurance covers and release in an Italian public contract; it is a documentary aid, does not compute the amounts of the specific case, does not draft the fideiussioni/polizze nor the schemi tipo and does not replace the contracting authority, the RUP, the guarantor or the economic operator."
license: MIT
area: appalti-opere-pubbliche
title: "Garanzie negli appalti pubblici: provvisoria e definitiva - D.Lgs. 36/2023"
summary: "Garanzia provvisoria (art. 106: 2%, riducibile all'1% o al 4%; forme, requisiti, riduzioni, svincolo) e garanzia definitiva (art. 117: 10%, maggiorazione per ribassi, svincolo progressivo all'80%, polizze CAR/RCT/decennale) negli appalti pubblici, D.Lgs. 36/2023."
normative_refs:
  - "D.Lgs. 31/3/2023 n. 36 - art. 106 (garanzia provvisoria - garanzie per la partecipazione alla procedura)"
  - "D.Lgs. 31/3/2023 n. 36 - art. 117 (garanzie definitive e coperture assicurative)"
version: 0.1.0-alpha
status: alpha
tags:
  - dlgs-36-2023
  - codice-contratti-pubblici
  - garanzia-provvisoria
  - garanzia-definitiva
  - fideiussione
  - polizze-assicurative
---

# Garanzie negli appalti pubblici: provvisoria e definitiva - D.Lgs. 36/2023

## Quando usare questa skill

Usala quando, in una procedura o in un contratto d'appalto pubblico, devi
**inquadrare quale garanzia si applica**, il suo **importo**, le **riduzioni**, le
**coperture assicurative** e lo **svincolo**, ancorando tutto al **Codice dei
contratti pubblici** (D.Lgs. 36/2023), **artt. 106 e 117**:

- **garanzia provvisoria** a corredo dell'offerta - **art. 106**: **2%** del
  valore complessivo della procedura (motivatamente riducibile fino all'**1%** o
  incrementabile fino al **4%**), forme (**cauzione** o **fideiussione**),
  requisiti (rinuncia alla **preventiva escussione** ed all'eccezione ex **art.
  1957, 2° comma, c.c.**, operativita' entro **15 giorni**, efficacia almeno
  **180 giorni**), cosa copre, **riduzioni** (30% qualita' ISO 9000; 50% PMI; 10%
  fideiussione digitale su registri distribuiti; fino al 20% certificazioni
  all. II.13) e **svincolo** (automatico alla firma; per i non aggiudicatari alla
  comunicazione e comunque a 30 giorni dall'aggiudicazione);
- **garanzia definitiva** per la sottoscrizione del contratto - **art. 117**:
  **10%** dell'importo contrattuale, **maggiorazione** per ribassi **> 10%** (un
  punto per punto) e **> 20%** (due punti per punto), **oggetto** (adempimento e
  risarcimento) e **durata** (fino al **collaudo/CRE**), **svincolo progressivo**
  fino all'**80%**, **sostituzione** con ritenuta del 10% sugli stati di
  avanzamento (lavori), **escussione**, e le **coperture assicurative** (polizza
  **CAR** e **RCT** con massimale, polizza **decennale postuma**, cauzione per la
  **rata di saldo**) e gli **schemi tipo** (c. 12).

**Non e' una skill di calcolo e non redige gli atti di garanzia**: non determina
gli importi del caso concreto, non scrive le fideiussioni/polizze ne' gli schemi
tipo (DM) e non sostituisce la stazione appaltante, il RUP o il garante.

## Cosa NON fa (limiti)

- Non **calcola** gli importi del caso concreto (valore della procedura, importo
  contrattuale, maggiorazione da ribasso, massimali): fornisce le percentuali e le
  regole di legge, il computo resta all'utente/stazione appaltante.
- Non **redige** le fideiussioni, le cauzioni o le polizze assicurative ne' gli
  **schemi tipo** (approvati con DM ex art. 117 c. 12): sono citati, non prodotti.
- Non **valuta** l'escussione, la decadenza o il contenzioso del caso concreto ne'
  fornisce consulenza legale/assicurativa.
- Non tratta le altre garanzie di sistema (anticipazione, garanzia per la
  progettazione ex art. 41, garanzie nei settori speciali/concessioni) se non nei
  richiami degli artt. 106 e 117.

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`inquadra-garanzia-provvisoria`](tasks/inquadra-garanzia-provvisoria.md) | Individua l'importo base (2%) e l'eventuale modulazione (1%-4%), la forma, i requisiti, le riduzioni cumulabili e lo svincolo della garanzia provvisoria ex art. 106 |
| [`inquadra-garanzia-definitiva`](tasks/inquadra-garanzia-definitiva.md) | Individua l'importo (10%) e la maggiorazione per ribasso, l'oggetto e la durata, lo svincolo progressivo (80%), la sostituzione e le coperture assicurative ex art. 117 |

## Riferimenti normativi

- **D.Lgs. 31/3/2023 n. 36** (Codice dei contratti pubblici) - **art. 106**
  (Garanzie per la partecipazione alla procedura - garanzia provvisoria).
- **D.Lgs. 31/3/2023 n. 36** - **art. 117** (Garanzie definitive e coperture
  assicurative).

Dettaglio in `references/sources.yaml`,
`references/fonti/dlgs-36-2023-artt-106-117.md`,
`references/estratti/garanzie-appalti-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: la determinazione degli importi, la scelta e la
stesura delle garanzie e delle polizze, la valutazione dell'escussione e ogni
decisione sul caso concreto restano in capo alla **stazione appaltante / RUP**,
all'**operatore economico** e al **garante**, con gli **schemi tipo** di legge e il
parere degli uffici competenti. **Non sostituisce** la stazione appaltante, il RUP,
il garante ne' l'operatore economico, ne' la lettura degli artt. 106 e 117 del
D.Lgs. 36/2023.
