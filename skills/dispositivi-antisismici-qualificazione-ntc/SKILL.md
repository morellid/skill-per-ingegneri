---
name: dispositivi-antisismici-qualificazione-ntc
description: "Supporto documentale al progettista strutturale, al Direttore dei Lavori e al collaudatore per la qualificazione e i controlli di accettazione in cantiere dei dispositivi antisismici e di controllo delle vibrazioni (isolatori elastomerici e a scorrimento, dissipatori lineari/non lineari/viscosi, dispositivi di vincolo a fusibile/provvisori) secondo le NTC 2018 (DM 17 gennaio 2018), paragrafo 11.9. Aiuta a inquadrare: i requisiti generali (vita di servizio superiore a 10 anni; campo di temperatura di riferimento, in assenza di indicazioni almeno da -15 C a +45 C; piani di manutenzione e sostituzione; dbd come spostamento allo SLV e gamma_x per dbd allo SLC nella UNI EN 15129); le tipologie del par. 11.9.1; la procedura di qualificazione del par. 11.9.2 (per i dispositivi del punto A del par. 11.1 conformita' alla UNI EN 15129 e Marcatura CE con sistema di valutazione e verifica della costanza della prestazione per applicazioni critiche; altrimenti caso C del par. 11.1; manuale di posa e manutenzione); la procedura di accettazione del par. 11.9.3 (obbligatoria per tutte le tipologie e demandata al Direttore dei Lavori, che campiona i dispositivi sui lotti del cantiere, verifica la documentazione e le tolleranze, rifiuta le forniture non conformi; prove certificate da laboratorio ex art. 59 DPR 380/2001); e le prove di accettazione e i limiti prestazionali per tipo dei par. 11.9.4-11.9.10 (almeno il 20% dei dispositivi e comunque non meno di 4; Tab. 11.9.I-IV; prova quasi statica con almeno 5 cicli ad ampiezza piu o meno d2). Use when a structural engineer, works supervisor or tester must frame the qualification and site acceptance of anti-seismic devices (isolators, dampers) under the Italian NTC 2018 par. 11.9; it is a documentary aid, does NOT design the isolation system nor size the devices (par. 7.10), and does NOT replace the designer or the works supervisor."
license: MIT
area: strutture-geotecnica
title: "Dispositivi antisismici: qualificazione e accettazione (NTC 2018 par. 11.9)"
summary: "Inquadra qualificazione e accettazione dei dispositivi antisismici (isolatori, dissipatori) secondo le NTC 2018 par. 11.9: UNI EN 15129 + CE (11.9.2), accettazione del Direttore dei Lavori con prove art. 59 (11.9.3), prove per tipo >=20% e >=4 e limiti Tab. 11.9.I-IV (11.9.4-10)."
normative_refs:
  - "NTC 2018 - par. 11.9: vita servizio >10 anni, temperatura -15/+45 C (11.9); UNI EN 15129 + CE o caso C par. 11.1 (11.9.2); accettazione del Direttore dei Lavori, laboratorio art. 59 DPR 380 (11.9.3)"
  - "NTC 2018 - par. 11.9.4-11.9.10: prove accettazione >=20% e >=4 per tipo; limiti Tab. 11.9.I-IV; isolatori, dissipatori viscosi (gamma_v), fusibile, vincolo provvisorio (corsa >=+/-50/25 mm)"
version: 0.1.0-alpha
status: alpha
tags:
  - dispositivi-antisismici
  - isolatori
  - dissipatori
  - ntc-2018
  - accettazione
---

# Dispositivi antisismici: qualificazione e accettazione (NTC 2018 par. 11.9)

## Quando usare questa skill

Usala quando un **progettista strutturale**, un **Direttore dei Lavori** o un **collaudatore** deve inquadrare la
**qualificazione** e i **controlli di accettazione in cantiere** dei **dispositivi antisismici e di controllo delle
vibrazioni** (isolatori elastomerici e a scorrimento, dissipatori lineari/non lineari/viscosi, dispositivi di vincolo
a fusibile/provvisori) secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 11.9** (Cap. 11):

- **requisiti generali** (vita di servizio, campo di temperatura, UNI EN 15129) e **tipologie** (§11.9-11.9.1);
- **procedura di qualificazione** (UNI EN 15129 + Marcatura CE / caso C del §11.1) (§11.9.2);
- **procedura di accettazione** demandata al Direttore dei Lavori (§11.9.3);
- **prove di accettazione** e **limiti prestazionali per tipo** (§11.9.4-11.9.10).

È un **supporto documentale**: inquadra qualificazione e accettazione; **non** esegue il **progetto** delle costruzioni
isolate né **dimensiona** i dispositivi. È **distinta** da `isolamento-sismico-ntc` (§7.10, progetto), che rinvia
esplicitamente al §11.9 come fuori scope.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-tipologie-e-qualificazione` | Requisiti generali (vita servizio, temperatura, UNI EN 15129) e tipologie (§11.9-11.9.1); procedura di qualificazione (UNI EN 15129 + CE per applicazioni critiche / caso C del §11.1) (§11.9.2) |
| `imposta-accettazione-e-prove-per-tipo` | Procedura di accettazione del Direttore dei Lavori (§11.9.3) e prove/limiti per tipo (§11.9.4-11.9.10): numerosità ≥ 20% e ≥ 4, Tab. 11.9.I-IV, prova quasi statica |

## Punti chiave (verificati sul testo/immagine)

- **Generalità** (§11.9): **vita di servizio > 10 anni**; campo di temperatura in assenza di indicazioni **almeno
  −15 °C ÷ +45 °C**; piani di manutenzione/sostituzione; in UNI EN 15129 **dbd = SLV**, **γx·dbd = SLC**.
- **Qualificazione** (§11.9.2): dispositivi del **punto A del §11.1** → **UNI EN 15129 + Marcatura CE**, sistema
  **VVCP per applicazioni critiche**; non ricadenti → **caso C del §11.1**; **manuale** di posa/manutenzione.
- **Accettazione** (§11.9.3): **obbligatoria per tutte le tipologie**, **demandata al Direttore dei Lavori** (che
  **campiona sui lotti del cantiere**, verifica documentazione/tolleranze, **rifiuta i non conformi**); prove
  **certificate da laboratorio ex art. 59 DPR 380/2001** (FPC tests).
- **Prove per tipo** (§11.9.4-11.9.10): **≥ 20% dei dispositivi, comunque ≥ 4**; prova **«quasi statica»** su ≥ 1
  dispositivo con **≥ 5 cicli** ±d2 (lineari/non lineari); limiti in **Tab. 11.9.I-IV**.
- **Dettagli per tipo**: lineari **ξe < 15%**, **|Ke−Kin|/Kin < 20%**; viscosi **γv = (1+td)·(1,5)^α**, rotazione
  **≥ 2°**; elastomerici piastre **18%**, **2/20 mm**; scorrimento attrito **≤ 25%**, **1,25 d2**; fusibile **±10%**,
  **3 cicli**, forza di rilascio **±15%**; provvisori corsa **≥ ±50 mm ponti / ±25 mm edifici**, FS **1,5** (o **1,1**).

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 11.9** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e con **tutti i
  valori numerici verificati sull'immagine** delle pagine PDF 358-364 (tabelle, formule, numerosità delle prove).

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non esegue** il **progetto** delle costruzioni con isolamento/dissipazione né **dimensiona** i dispositivi
  (§7.10, → skill `isolamento-sismico-ntc`).
- **Non tratta** la qualificazione dei **materiali** del Cap. 11 (cls/acciaio §§11.2/11.3, → skill dedicate).
- **Non** sostituisce il progettista, il Direttore dei Lavori né il laboratorio ex art. 59.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, il Direttore dei Lavori né la lettura del par. 11.9 delle NTC 2018, della UNI EN 15129 e della relativa Circolare applicativa.**
