---
name: autorizzazione-scarico-acque-reflue-dlgs152
description: "Supporto documentale al tecnico ambientale e degli impianti e al titolare dello scarico per l'autorizzazione allo scarico di acque reflue e per la domanda di autorizzazione degli scarichi industriali, ai sensi del D.Lgs. 3 aprile 2006, n. 152 (Codice dell'ambiente), Parte III, artt. 124 e 125. Aiuta a inquadrare i criteri generali: l'obbligo di autorizzazione preventiva di tutti gli scarichi, il rilascio al titolare dell'attivita' o al titolare dello scarico finale o al consorzio, il regime delle acque reflue domestiche e delle reti fognarie e di quelle termali definito dalle regioni, l'autorizzazione provvisoria degli impianti di depurazione, la competenza della provincia o dell'ente di governo dell'ambito se lo scarico e' in pubblica fognatura con il termine di novanta giorni, la validita' di quattro anni e il rinnovo da chiedere un anno prima con mantenimento provvisorio dello scarico se la domanda e' tempestiva e con rinnovo espresso entro sei mesi per le sostanze pericolose dell'articolo 108, le prescrizioni tecniche in relazione alla localizzazione e all'ambiente, le spese di istruttoria a carico del richiedente e i casi di nuova autorizzazione per trasferimento, cambio d'uso, ampliamento o ristrutturazione con scarico diverso (art. 124); e il contenuto della domanda per gli scarichi industriali, cioe' le caratteristiche quantitative e qualitative, il volume annuo, il ricettore, il punto di prelievo di controllo, il sistema di scarico e le operazioni connesse, il sistema di misurazione del flusso, le apparecchiature e i sistemi di depurazione, con le indicazioni aggiuntive per le sostanze della tabella 3/A dell'Allegato 5 (art. 125). Use when an environmental or plant technician, or the holder of a discharge, must frame the authorization of wastewater discharges and the application for industrial discharges under D.Lgs. 152/2006; it is a documentary aid and does NOT draft the application, does NOT design the treatment plant, does NOT apply the emission limit values of Annex 5, does NOT handle the AUA/AIA procedures, and does NOT replace the technician, the water service operator, or the competent authority."
license: MIT
area: ambiente-territorio-mobilita
title: "Autorizzazione allo scarico di acque reflue (D.Lgs. 152/2006 artt. 124-125)"
summary: "Inquadra l'autorizzazione allo scarico di acque reflue (D.Lgs. 152/2006 artt. 124-125): obbligo preventivo e titolare, competenza e 90 giorni, validita' 4 anni e rinnovo, prescrizioni e spese (124), contenuto della domanda per gli scarichi industriali (125)."
normative_refs:
  - "D.Lgs. 3 aprile 2006, n. 152 (Codice dell'ambiente) - Parte III, artt. 124 (criteri generali) e 125 (domanda di autorizzazione agli scarichi di acque reflue industriali)"
  - "Rinvio (non riprodotti): Allegato 5 Parte III (valori limite di emissione, Tab. 1/2/3/3-A/4), artt. 74 (definizioni), 101 e 108 D.Lgs. 152/2006; AUA (DPR 59/2013); AIA"
version: 0.1.0-alpha
status: alpha
tags:
  - scarichi-idrici
  - acque-reflue
  - autorizzazione-allo-scarico
  - dlgs-152-2006
  - tutela-acque
---

# Autorizzazione allo scarico di acque reflue (D.Lgs. 152/2006 artt. 124-125)

## Quando usare questa skill

Usala quando un **tecnico ambientale/degli impianti** o il **titolare dello scarico** deve **inquadrare**
l'**autorizzazione allo scarico di acque reflue** e la **domanda** per gli **scarichi industriali**,
secondo il **D.Lgs. 3 aprile 2006, n. 152** (Codice dell'ambiente), **Parte III, artt. 124 e 125**:

- **obbligo** di autorizzazione preventiva e **titolare** (art. 124, cc. 1-2);
- **regimi** delle reflue domestiche/fognarie e termali, **autorizzazione provvisoria** (cc. 3-6);
- **competenza** e **termine** di 90 giorni (c. 7); **validità 4 anni** e **rinnovo** (c. 8);
- **prescrizioni tecniche**, **spese** e **modifiche** (cc. 9-12);
- **contenuto della domanda** per gli scarichi industriali (art. 125).

**Non è** uno strumento che redige la domanda o progetta l'impianto di depurazione, né applica i valori
limite di emissione: è un **supporto documentale** che inquadra obblighi, competenze, termini e
contenuti.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-autorizzazione-scarico` | Inquadra obbligo, titolare, regimi, competenza, termini, validità/rinnovo, prescrizioni e spese (art. 124) |
| `inquadra-domanda-scarico-industriale` | Inquadra il contenuto della domanda per gli scarichi industriali e le indicazioni per la Tabella 3/A (art. 125) |

## Punti chiave (verificati sul testo)

- **Obbligo** (art. 124, c. 1): **tutti gli scarichi preventivamente autorizzati**. **Titolare** (c. 2):
  attività / scarico finale / consorzio, con responsabilità del gestore dell'impianto di depurazione.
- **Regimi** (cc. 3-6): domestiche/fognarie e termali definiti dalle **regioni**; domestiche in
  fognatura **sempre ammesse** (regolamenti del gestore SII); **autorizzazione provvisoria** dei
  depuratori.
- **Competenza e termine** (c. 7): **provincia** o **ente di governo dell'ambito** (pubblica fognatura);
  provvedimento in **90 giorni**.
- **Validità/rinnovo** (c. 8): **4 anni**; rinnovo **1 anno prima**; proroga provvisoria se domanda
  tempestiva; **sostanze pericolose (art. 108)** → rinnovo **espresso entro 6 mesi**.
- **Prescrizioni/spese/modifiche** (cc. 10-12): prescrizioni per localizzazione e ambiente; **spese di
  istruttoria a carico del richiedente**; **nuova autorizzazione** se lo scarico cambia
  qualità/quantità.
- **Domanda industriale** (art. 125): caratteristiche **quali/quantitative**, volume annuo, ricettore,
  **punto di prelievo**, sistema di scarico, misurazione del flusso, **apparecchiature e sistemi di
  depurazione**; per la **Tab. 3/A**, capacità di produzione e fabbisogno orario d'acqua.

## Fonti

- **D.Lgs. 3 aprile 2006, n. 152** (Codice dell'ambiente) - Parte III, **artt. 124-125** - testo
  vigente su Normattiva (indice pinnato a `!vig=2026-07-17`, codice 006G0171, idGruppo 25).

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non redige** la domanda né **progetta** l'impianto di depurazione o lo scarico.
- **Non applica** i **valori limite di emissione** dell'**Allegato 5 alla Parte III** (Tab. 1/2/3/3-A/4).
- **Non tratta** l'**AUA** (DPR 59/2013) né l'**AIA** (skill `autorizzazione-integrata-ambientale-dlgs152`)
  come procedure, né le definizioni di scarico dell'art. 74, se non nei richiami.

**La skill è un supporto documentale: non sostituisce il tecnico, il gestore del servizio idrico
integrato o l'autorità competente, né la lettura degli artt. 124-125 del D.Lgs. 152/2006 e dell'Allegato
5.**
