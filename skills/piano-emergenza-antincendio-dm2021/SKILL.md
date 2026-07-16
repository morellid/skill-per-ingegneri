---
name: piano-emergenza-antincendio-dm2021
description: "Supporto documentale all'obbligo e alla struttura del piano di emergenza ed evacuazione nei luoghi di lavoro, ai sensi dell'art. 46 del D.Lgs. 81/2008 e del D.M. 2 settembre 2021 (criteri per la gestione della sicurezza antincendio in esercizio ed in emergenza, attuativi dell'art. 46 c.3). Aiuta a stabilire quando il piano di emergenza e' obbligatorio (luoghi di lavoro con almeno dieci lavoratori; luoghi aperti al pubblico con presenza contemporanea di piu' di cinquanta persone; attivita' soggette a controllo dei Vigili del Fuoco ex Allegato I del DPR 151/2011 - art. 2 c.2 del D.M.) e cosa fare quando non lo e' (misure organizzative e gestionali nel DVR - art. 2 c.4), a inquadrare la gestione della sicurezza antincendio in esercizio ed in emergenza secondo gli allegati I e II, la designazione degli addetti al servizio antincendio all'esito della valutazione del rischio incendio (art. 4) e la loro formazione e aggiornamento (art. 5, allegato III), e a richiamare i contenuti del piano (misure di gestione dell'emergenza, nominativi degli addetti). Use when an employer/RSPP/technician must determine whether an emergency and evacuation plan is required and how to structure it under the Italian fire-safety-in-emergency decree; it is a documentary aid and does NOT replace the fire-risk assessment (valutazione del rischio incendio), does NOT reproduce the full annexes I-II-III content and does not certify the plan."
license: MIT
area: sicurezza-lavoro-cantieri
title: "Piano di emergenza ed evacuazione (art. 46 D.Lgs 81/2008 + DM 2/9/2021)"
summary: "Obbligo e struttura del piano di emergenza nei luoghi di lavoro (art. 46 D.Lgs 81/2008 + DM 2/9/2021): quando e' obbligatorio (>=10 lavoratori, >50 persone al pubblico, attivita' DPR 151/2011), designazione e formazione addetti. Non esegue la valutazione del rischio incendio."
normative_refs:
  - "D.Lgs. 81/2008 art. 46 (prevenzione incendi e gestione delle emergenze)"
  - "D.M. 2 settembre 2021 (gestione sicurezza antincendio in esercizio ed emergenza)"
version: 0.1.0-alpha
status: alpha
tags:
  - piano-emergenza
  - antincendio
  - dm-2-9-2021
  - art-46-dlgs81
  - sicurezza-lavoro
---

# Piano di emergenza ed evacuazione (art. 46 D.Lgs 81/2008 + DM 2/9/2021)

## Quando usare questa skill

Usala quando, come **datore di lavoro / RSPP / tecnico**, devi stabilire se e' **dovuto
il piano di emergenza ed evacuazione** e come strutturarlo, ai sensi dell'**art. 46 D.Lgs
81/2008** e del **D.M. 2 settembre 2021** (gestione della sicurezza antincendio in
esercizio ed in emergenza):

- **determinare l'obbligo** del piano di emergenza (art. 2 c.2 del D.M.);
- gestire il caso in cui **non e' obbligatorio** (misure nel DVR - art. 2 c.4);
- **designare** gli addetti al servizio antincendio (art. 4) e curarne **formazione e
  aggiornamento** (art. 5, allegato III);
- richiamare i **contenuti** del piano (misure di gestione dell'emergenza, nominativi
  degli addetti - art. 2 c.3).

## Quando il piano di emergenza e' OBBLIGATORIO (art. 2 c.2 DM 2/9/2021)

Il datore di lavoro **predispone il piano di emergenza** nei luoghi di lavoro:

- ove sono occupati **almeno 10 lavoratori**;
- **aperti al pubblico** con presenza contemporanea di **piu' di 50 persone**,
  indipendentemente dal numero di lavoratori;
- che rientrano nell'**Allegato I del DPR 151/2011** (attivita' soggette a controllo dei
  Vigili del Fuoco).

**Se non si rientra** in nessuno di questi casi (art. 2 c.4): **non** c'e' obbligo di
redigere il piano, ma restano dovute le **misure organizzative e gestionali** da attuare
in caso di incendio, riportate nel **DVR** (o nel documento con procedure standardizzate,
art. 29 c.5).

## Struttura e adempimenti

- **Gestione in esercizio ed in emergenza** (art. 2 c.1): secondo i criteri degli
  **allegati I e II** (parte integrante del decreto).
- **Contenuti del piano** (art. 2 c.3): misure di gestione dell'emergenza + **nominativi
  degli addetti** (o del datore di lavoro nei casi dell'art. 34 D.Lgs 81/2008).
- **Designazione addetti** (art. 4): all'esito della **valutazione del rischio incendio**
  e delle misure di gestione (incluso il piano, ove previsto).
- **Formazione e aggiornamento** (art. 5, allegato III): secondo l'art. 37 c.9 D.Lgs
  81/2008.
- **Base di legge** (art. 46 D.Lgs 81/2008): prevenzione incendi e delega ai decreti per
  i criteri di gestione delle emergenze e per il servizio antincendio.

## Cosa NON fa (limiti)

- **Non esegue la valutazione del rischio incendio** (presupposto del piano e della
  designazione): la skill inquadra l'obbligo e la struttura, non valuta il rischio.
- **Non riproduce integralmente gli allegati I-II-III** del D.M. (criteri operativi,
  livelli, contenuti di dettaglio): li richiama, rinviando al decreto.
- **Non certifica** il piano ne' sostituisce il progetto antincendio (mini-codice, DM
  3/9/2021) o le pratiche VV.F. (DPR 151/2011).

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`determina-obbligo-piano`](tasks/determina-obbligo-piano.md) | Stabilisce se il piano di emergenza e' obbligatorio (soglie art. 2 c.2) o se bastano le misure nel DVR (art. 2 c.4) |
| [`struttura-piano-e-addetti`](tasks/struttura-piano-e-addetti.md) | Imposta i contenuti del piano (misure di emergenza, nominativi) e la designazione/formazione degli addetti antincendio (artt. 2 c.3, 4, 5) |

## Riferimenti normativi

- **D.Lgs. 81/2008 art. 46** - prevenzione incendi e gestione delle emergenze (base e
  delega ai decreti).
- **D.M. 2 settembre 2021** - gestione della sicurezza antincendio in esercizio ed in
  emergenza (artt. 1-8; allegati I-II-III), attuativo dell'art. 46 c.3.

Dettaglio in `references/sources.yaml`, `references/fonti/piano-emergenza.md`,
`references/estratti/piano-emergenza-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: la valutazione del rischio incendio, la definizione
puntuale del piano e la designazione/formazione degli addetti dipendono dal caso concreto
e dalla responsabilita' del datore di lavoro e dell'RSPP/tecnico antincendio. La skill
**non sostituisce** il datore di lavoro, l'RSPP ne' il professionista antincendio.
