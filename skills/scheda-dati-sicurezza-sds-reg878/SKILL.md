---
name: scheda-dati-sicurezza-sds-reg878
description: "Supporto documentale alla compilazione e alla verifica di completezza della Scheda di Dati di Sicurezza (SDS) secondo l'allegato II del regolamento REACH quale sostituito dal regolamento (UE) 2020/878 (formato a 16 sezioni). Aiuta a strutturare le 16 sezioni obbligatorie (identificazione, identificazione dei pericoli, composizione, primo soccorso, lotta antincendio, rilascio accidentale, manipolazione e immagazzinamento, controlli dell'esposizione/DPI, proprieta' fisiche e chimiche, stabilita' e reattivita', informazioni tossicologiche ed ecologiche, smaltimento, trasporto, regolamentazione, altre informazioni) con le rispettive sotto-sezioni, e a verificare le prescrizioni generali della Parte A (compilazione da persona competente, divieto di indicazioni minimizzanti non coerenti con la classificazione, datazione e gestione delle revisioni). Use when a chemical/safety engineer or regulatory officer must draft or check the completeness of a safety data sheet for a substance or mixture; it is a documentary aid and does not classify the substance under CLP, does not perform the chemical safety assessment and does not derive exposure/toxicological/transport values."
license: MIT
area: impianti-macchine-prodotti
title: "Scheda di Dati di Sicurezza (SDS) - allegato II REACH / Reg. (UE) 2020/878"
summary: "Compilazione e verifica di completezza della Scheda di Dati di Sicurezza (SDS) secondo l'allegato II REACH sostituito dal Reg. (UE) 2020/878: le 16 sezioni obbligatorie con le sotto-sezioni e le prescrizioni generali della Parte A (persona competente, datazione/revisioni)."
normative_refs:
  - "Regolamento (UE) 2020/878 - allegato II REACH (formato SDS a 16 sezioni)"
  - "Reg. (CE) 1907/2006 (REACH) art. 31 (obbligo SDS - citato) e Reg. (CE) 1272/2008 (CLP - citato)"
version: 0.1.0-alpha
status: alpha
tags:
  - reg-ue-2020-878
  - sds
  - scheda-dati-sicurezza
  - reach
  - clp
---

# Scheda di Dati di Sicurezza (SDS) - allegato II REACH / Reg. (UE) 2020/878

## Quando usare questa skill

Usala quando devi **compilare** o **verificare la completezza** di una **Scheda di
Dati di Sicurezza (SDS)** di una sostanza o miscela, secondo l'**allegato II del
REACH** quale sostituito dal **Reg. (UE) 2020/878** (formato a 16 sezioni):

- strutturare le **16 sezioni obbligatorie** e le rispettive **sotto-sezioni**
  nell'ordine e con la numerazione previsti;
- controllare le **prescrizioni generali** della Parte A (compilazione da persona
  competente; linguaggio chiaro; **divieto di indicazioni minimizzanti** non
  coerenti con la classificazione; **datazione** e gestione delle **revisioni**).

**Non e' una skill di classificazione**: non classifica la sostanza/miscela ai
sensi del **CLP**, non compie la **valutazione della sicurezza chimica** e non
ricava i valori (limiti di esposizione, dati tossicologici/ecologici, classi di
trasporto).

## Cosa NON fa (limiti)

- Non **classifica** ai sensi del **CLP** (Reg. 1272/2008) ne' redige gli
  **scenari d'esposizione** / la valutazione della sicurezza chimica.
- Non stabilisce **quando** la SDS e' obbligatoria: e' l'**art. 31 REACH**
  (rinvio, non riprodotto).
- Non fornisce i **dati** di sezione (limiti, tossicita', ecotossicita',
  classificazione ADR/RID/IMDG/IATA): sono del fornitore o delle prove.

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`compila-sds`](tasks/compila-sds.md) | Struttura le 16 sezioni e le sotto-sezioni della SDS secondo l'allegato II, con le prescrizioni generali della Parte A |
| [`verifica-completezza-sds`](tasks/verifica-completezza-sds.md) | Verifica la completezza e la conformita' formale di una SDS esistente (sezioni/sotto-sezioni presenti, datazione/revisione, assenza di indicazioni minimizzanti) |

## Riferimenti normativi

- **Regolamento (UE) 2020/878** della Commissione del 18 giugno 2020 - sostituisce
  l'**allegato II del REACH** (Reg. CE 1907/2006): prescrizioni generali (Parte A)
  e struttura delle 16 sezioni (Parte B).
- **Reg. (CE) 1907/2006 (REACH) art. 31** (obbligo e condizioni di fornitura della
  SDS - **citato**, non riprodotto) e **Reg. (CE) 1272/2008 (CLP)** (classificazione
  - citato).

Dettaglio in `references/sources.yaml`, `references/fonti/reg-ue-2020-878-sds.md`,
`references/estratti/sds-16-sezioni-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: la classificazione CLP, i valori tossicologici/
ecologici, i limiti di esposizione, la classificazione di trasporto e la
valutazione della sicurezza chimica richiedono dati e competenze specialistiche e
restano in capo al fornitore e alla persona competente che redige la SDS.
La skill **non sostituisce** la persona competente, il classificatore CLP ne' la
valutazione della sicurezza chimica.
