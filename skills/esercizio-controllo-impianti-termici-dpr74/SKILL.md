---
name: esercizio-controllo-impianti-termici-dpr74
description: "Supporto documentale ai criteri di esercizio, conduzione, controllo e manutenzione degli impianti termici per la climatizzazione invernale ed estiva, secondo il D.P.R. 16 aprile 2013, n. 74 (regolamento attuativo dell'art. 4 del D.Lgs. 192/2005). Aiuta a rispettare i valori massimi di temperatura ambiente (18 C + 2 C di tolleranza per gli edifici industriali/artigianali, 20 C + 2 C per gli altri edifici in regime invernale; non meno di 26 C - 2 C in regime estivo - art. 3), i limiti di esercizio per zona climatica (periodi e ore giornaliere di accensione per le zone A-F e le deroghe con ordinanza del sindaco - artt. 4-5), a individuare i soggetti responsabili (responsabile dell'impianto e terzo responsabile, con i limiti alla delega per le unita' residenziali senza locale tecnico dedicato - art. 6), a impostare il controllo e la manutenzione da parte di ditte abilitate ai sensi del DM 37/2008 secondo le istruzioni dell'installatore o del fabbricante (art. 7) e il controllo di efficienza energetica con il relativo rapporto (RCEE) per gli impianti invernali oltre 10 kW ed estivi oltre 12 kW (art. 8), e a tenere la documentazione (libretto di impianto ex DM 10/2/2014). Use when an engineer, plant manager, maintenance firm, or building administrator must comply with the operation, control and maintenance rules for Italian thermal (heating/cooling) plants under DPR 74/2013 - temperature limits, heating-season windows by climate zone, plant responsible/third-party responsible, energy-efficiency control and the RCEE report; it is a documentary aid and does NOT reproduce the RCEE form fields (Annex A, in tabular form) or the plant logbook model (DM 10/2/2014), does not perform the control/maintenance or draft the RCEE, and does not replace the qualified maintainer or the competent authority's inspection, nor the regional rules (plant registry, sticker)."
license: MIT
area: energia-incentivi
title: "Esercizio, controllo e manutenzione degli impianti termici (DPR 74/2013)"
summary: "Applica i criteri del DPR 74/2013 per esercizio, controllo e manutenzione degli impianti termici: temperature massime (20/18 C +2), periodi e orari per zona climatica A-F, responsabile/terzo responsabile, controllo di efficienza energetica e RCEE (>10/12 kW). Non redige il RCEE."
normative_refs:
  - "D.P.R. 16 aprile 2013, n. 74 - artt. 3, 4, 5, 6, 7, 8 e Allegato A"
  - "D.Lgs. 192/2005 (attuazione dir. 2002/91/CE) + DM 10 febbraio 2014 (libretto di impianto) - richiamati"
version: 0.1.0-alpha
status: alpha
tags:
  - impianti-termici
  - dpr-74-2013
  - efficienza-energetica
  - terzo-responsabile
  - rcee
---

# Esercizio, controllo e manutenzione degli impianti termici (DPR 74/2013)

## Quando usare questa skill

Usala quando un **ingegnere, responsabile di impianto, ditta di manutenzione o amministratore**
deve rispettare i criteri di **esercizio, conduzione, controllo e manutenzione** degli
**impianti termici per la climatizzazione** (invernale ed estiva), secondo il **D.P.R. 16
aprile 2013, n. 74** (attuativo dell'art. 4 del **D.Lgs. 192/2005**):

- rispettare i **valori massimi di temperatura** e i **limiti di esercizio** per zona climatica;
- individuare i **soggetti responsabili** (responsabile e terzo responsabile);
- impostare **controllo/manutenzione** e il **controllo di efficienza energetica** (RCEE).

Per il calcolo della **trasmittanza** dell'involucro usa `trasmittanza-termica-opache-dm2015`;
per la **diagnosi energetica** delle imprese usa `diagnosi-energetica-dlgs102`.

## Valori massimi di temperatura (art. 3)

- **Climatizzazione invernale** - la media ponderata delle temperature dell'aria non deve
  superare: **18 C + 2 C** di tolleranza per gli edifici **industriali/artigianali** e
  assimilabili; **20 C + 2 C** di tolleranza per **tutti gli altri** edifici.
- **Climatizzazione estiva** - la media ponderata non deve essere **inferiore a 26 C - 2 C**
  di tolleranza per tutti gli edifici.

## Limiti di esercizio per zona climatica (artt. 4-5)

In regime invernale l'esercizio e' consentito nei seguenti **periodi** e con la **durata
giornaliera** (anche in due o piu' sezioni):

- **Zona A**: 6 ore/giorno dal 1 dicembre al 15 marzo;
- **Zona B**: 8 ore/giorno dal 1 dicembre al 31 marzo;
- **Zona C**: 10 ore/giorno dal 15 novembre al 31 marzo;
- **Zona D**: 12 ore/giorno dal 1 novembre al 15 aprile;
- **Zona E**: 14 ore/giorno dal 15 ottobre al 15 aprile;
- **Zona F**: nessuna limitazione.

Al di fuori dei periodi l'attivazione e' consentita **solo** in presenza di situazioni
climatiche che la giustificano. I **sindaci** possono, con **ordinanza** (art. 5), ampliare o
ridurre periodi/orari e stabilire riduzioni della temperatura massima.

## Soggetti responsabili (art. 6)

Esercizio, conduzione, controllo, manutenzione ed efficienza energetica sono affidati al
**responsabile dell'impianto**, che puo' delegare un **terzo responsabile**. La **delega non
e' consentita** per le **singole unita' immobiliari residenziali** con generatore **non**
installato in **locale tecnico dedicato**. Per gli impianti **non conformi**, la delega non
puo' essere rilasciata salvo che nell'atto sia conferito l'incarico di **messa a norma**.

## Controllo, manutenzione ed efficienza energetica (artt. 7-8)

- **Controllo e manutenzione** (art. 7): eseguiti da **ditte abilitate** ai sensi del **DM
  37/2008**, con le **prescrizioni e la periodicita'** delle **istruzioni dell'installatore**;
  in mancanza, del **fabbricante**.
- **Controllo di efficienza energetica** (art. 8): in occasione del controllo/manutenzione, per
  impianti **invernali > 10 kW** ed **estivi > 12 kW**, riguarda il sottosistema di
  **generazione**, i sistemi di **regolazione** della temperatura e di **trattamento acqua**.
  Si redige il **rapporto di controllo di efficienza energetica (RCEE)** secondo i **modelli
  dell'Allegato A**. Va effettuato anche alla **prima messa in esercizio** (installatore), alla
  **sostituzione del generatore** e per interventi che modificano l'efficienza.
- **Documentazione**: **libretto di impianto** (modello del **DM 10 febbraio 2014**) e
  conservazione dei **RCEE**; trasmissione secondo le modalita' regionali (catasto impianti,
  bollino) ove previste.

## Cosa NON fa (limiti)

- **Non riproduce i campi dei modelli RCEE** (Allegato A, in formato tabellare) ne' il **modello
  di libretto** (DM 10/2/2014): rinvia agli atti.
- **Non esegue** il controllo/manutenzione ne' redige il RCEE; **non sostituisce** il
  manutentore abilitato ne' l'ispezione dell'autorita' competente.
- **Non copre** la disciplina **regionale** di dettaglio (periodicita', catasto impianti,
  bollino), che va verificata caso per caso.

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`verifica-limiti-esercizio`](tasks/verifica-limiti-esercizio.md) | Verifica i valori massimi di temperatura e i limiti di esercizio per zona climatica (periodi/orari, deroghe comunali) |
| [`imposta-controllo-manutenzione`](tasks/imposta-controllo-manutenzione.md) | Imposta responsabile/terzo responsabile, controllo e manutenzione (DM 37/2008) e il controllo di efficienza energetica con RCEE |

## Riferimenti normativi

- **D.P.R. 16 aprile 2013, n. 74** - **art. 3** (temperature), **art. 4** (limiti di esercizio
  per zona), **art. 5** (ordinanze del sindaco), **art. 6** (responsabile e terzo responsabile),
  **art. 7** (controllo e manutenzione), **art. 8** (controllo di efficienza energetica, RCEE);
  **Allegato A** (modelli RCEE).
- **D.Lgs. 19 agosto 2005, n. 192** (attuazione dir. 2002/91/CE) - base del regolamento;
  **DM 22 gennaio 2008, n. 37** (ditte abilitate); **DM 10 febbraio 2014** (libretto di impianto
  e modelli RCEE) - richiamati, non riprodotti.

Dettaglio in `references/sources.yaml`, `references/fonti/dpr-74-2013.md`,
`references/estratti/impianti-termici-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: l'esercizio, il controllo, la manutenzione e la redazione
del RCEE restano responsabilita' del **responsabile dell'impianto** e del **manutentore
abilitato**, sulle prescrizioni vigenti (incluse quelle regionali). La skill **non sostituisce** il manutentore abilitato, l'autorita' competente per le ispezioni ne' la lettura del D.P.R. 74/2013 (Allegato A) e del DM 10/2/2014.
