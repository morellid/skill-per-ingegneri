---
name: scarichi-emissioni-dlgs152
description: "Supporto documentale alle autorizzazioni ambientali singole (residuali rispetto ad AUA e AIA) per lo scarico di acque reflue industriali (art. 124 D.Lgs. 152/2006) e per le emissioni in atmosfera degli stabilimenti (art. 269): aiuta a capire quando serve l'autorizzazione, chi la rilascia e a chi va la domanda (provincia o ente di governo dell'ambito per gli scarichi; autorita' competente per le emissioni), i contenuti della domanda (progetto e relazione tecnica per le emissioni), la durata e il rinnovo (scarichi 4 anni, rinnovo un anno prima; emissioni 15 anni, rinnovo un anno prima), i casi di nuova autorizzazione o comunicazione per trasferimento/ampliamento/modifica, e le sanzioni penali e amministrative (artt. 137 e 279). Use when an Italian operator or environmental consultant must handle a stand-alone discharge or air-emission authorization outside the single environmental authorization; it is a documentary aid and does not read the emission/discharge limit tables nor draft the application."
license: MIT
area: ambiente-territorio-mobilita
title: "Autorizzazione scarichi ed emissioni - D.Lgs. 152/2006 (artt. 124, 269)"
summary: "Autorizzazioni ambientali singole residuali rispetto ad AUA/AIA: scarico di acque reflue industriali (art. 124 D.Lgs. 152/2006, durata 4 anni) ed emissioni in atmosfera (art. 269, durata 15 anni), con nuova autorizzazione/comunicazione per modifiche e sanzioni (artt. 137, 279)"
normative_refs:
  - "D.Lgs. 3/4/2006 n. 152 (testo vigente) - artt. 124, 137 (Parte terza - scarichi) e 269, 279 (Parte quinta - emissioni)"
version: 0.1.0-alpha
status: alpha
tags:
  - dlgs-152-2006
  - scarichi-idrici
  - emissioni-atmosfera
  - autorizzazioni-ambientali
  - testo-unico-ambientale
---

# Autorizzazione scarichi ed emissioni - D.Lgs. 152/2006 (artt. 124, 269)

## Quando usare questa skill

Usala quando devi orientarti sulle **autorizzazioni ambientali singole** per:

- lo **scarico di acque reflue industriali** (art. 124, Parte terza);
- le **emissioni in atmosfera** di uno stabilimento (art. 269, Parte quinta);

nei casi **residuali** in cui non si applica l'**AUA** (DPR 59/2013) o l'**AIA**
(art. 29-quattuordecies), che altrimenti assorbono questi titoli.

Aiuta a determinare: quando serve l'autorizzazione, chi la rilascia e a chi va la
domanda, i contenuti della domanda, la **durata e il rinnovo**, i casi di **nuova
autorizzazione o comunicazione** per modifiche, e le **sanzioni**.

**Non e' una skill di calcolo**: non legge i valori limite (Allegato 5 parte
terza per gli scarichi; Allegati I-V parte quinta per le emissioni), non redige
le domande, non stabilisce se l'impianto rientri nell'AUA/AIA.

## Cosa NON fa (limiti)

- Non riproduce i **valori limite** di scarico/emissione: rinvia agli allegati.
- Non redige il progetto, la relazione tecnica o la domanda.
- Non decide l'inquadramento **AUA/AIA** dell'impianto.
- Non copre la disciplina degli scarichi urbani/domestici oltre ai richiami, ne'
  gli obblighi di autocontrollo di dettaglio.
- Non sostituisce l'autorita' competente (provincia, ente d'ambito, regione).

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`inquadra-autorizzazione`](tasks/inquadra-autorizzazione.md) | Dato l'impianto (tipo di scarico/emissione, destinazione, AUA/AIA), determina quale autorizzazione singola serve, l'autorita' competente, la durata e i casi di nuova autorizzazione o comunicazione |
| [`checklist-domanda-rinnovo`](tasks/checklist-domanda-rinnovo.md) | Verifica i contenuti della domanda, i termini di rilascio/rinnovo e le sanzioni applicabili (artt. 137, 279) |

## Riferimenti normativi

- **D.Lgs. 3/4/2006 n. 152** (TUA), testo vigente su Normattiva:
  - **art. 124** (criteri generali autorizzazione allo scarico) e **art. 137**
    (sanzioni penali scarichi) - Parte terza;
  - **art. 269** (autorizzazione alle emissioni in atmosfera) e **art. 279**
    (sanzioni emissioni) - Parte quinta.

Dettaglio in `references/sources.yaml`, `references/fonti/dlgs-152-2006.md`,
`references/estratti/scarichi-emissioni-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: i valori limite e l'inquadramento AUA/AIA
richiedono la lettura degli allegati e la valutazione del caso; la decisione
spetta all'autorita' competente.
