---
name: vita-nominale-classi-uso-ntc
description: "Supporto documentale al progettista per l'inquadramento della vita nominale di progetto (VN), delle classi d'uso (CU) e del periodo di riferimento per l'azione sismica (VR) secondo le NTC 2018 (DM 17 gennaio 2018), paragrafo 2.4. Aiuta a fissare i tre parametri di base di ogni progetto strutturale: la vita nominale di progetto VN (numero di anni in cui l'opera, soggetta a manutenzione, mantiene i livelli prestazionali; valori minimi della Tab. 2.4.I: 10 anni per le costruzioni temporanee e provvisorie, 50 anni per i livelli di prestazioni ordinari, 100 anni per i livelli di prestazioni elevati; per la fase di costruzione di durata PN la VN e' non inferiore a PN e comunque non inferiore a 5 anni; le verifiche sismiche di opere temporanee o in fase di costruzione possono omettersi se la condizione permane per meno di 2 anni); la classe d'uso (Classe I presenza occasionale ed edifici agricoli, Classe II normali affollamenti, Classe III affollamenti significativi, Classe IV funzioni pubbliche o strategiche importanti); e il periodo di riferimento per l'azione sismica VR uguale al prodotto tra la vita nominale VN e il coefficiente d'uso CU, formula 2.4.1, con coefficiente d'uso CU della Tab. 2.4.II pari a 0,7 per la Classe I, 1,0 per la Classe II, 1,5 per la Classe III e 2,0 per la Classe IV (anche superiore a 2 per attivita' a rischio di incidente rilevante). Use when a designer must set the nominal design working life VN, the use class CU and the seismic reference period VR under the Italian NTC 2018 par. 2.4; it is a documentary aid and does NOT define the response spectrum nor the return periods TR of the limit states (par. 3.2), and does NOT replace the designer or the 2019 Circular."
license: MIT
area: strutture-geotecnica
title: "Vita nominale, classi d'uso e periodo di riferimento (NTC 2018 par. 2.4)"
summary: "Inquadra i tre parametri di base di ogni progetto strutturale (NTC 2018 par. 2.4): vita nominale VN (Tab. 2.4.I: 10/50/100 anni), classi d'uso I-IV, periodo di riferimento sismico VR = VN*CU [2.4.1] con CU (Tab. 2.4.II) = 0,7/1,0/1,5/2,0."
normative_refs:
  - "NTC 2018 (D.M. 17 gennaio 2018) - par. 2.4.1: vita nominale di progetto VN, valori minimi Tab. 2.4.I (10 anni temporanee, 50 ordinarie, 100 elevate); fase di costruzione VN >= PN e >= 5 anni"
  - "NTC 2018 - par. 2.4.2: classi d'uso I-IV (presenza occasionale / normali affollamenti / affollamenti significativi / funzioni pubbliche o strategiche)"
  - "NTC 2018 - par. 2.4.3: periodo di riferimento VR = VN*CU [2.4.1]; coefficiente d'uso CU Tab. 2.4.II = 0,7/1,0/1,5/2,0 (I/II/III/IV), >2 per rischio incidente rilevante"
version: 0.1.0-alpha
status: alpha
tags:
  - vita-nominale
  - classi-uso
  - periodo-riferimento
  - azione-sismica
  - ntc-2018
---

# Vita nominale, classi d'uso e periodo di riferimento (NTC 2018 par. 2.4)

## Quando usare questa skill

Usala quando un **progettista** deve **fissare i tre parametri di base** che governano la definizione dell'azione
sismica (e delle azioni dipendenti dal tempo) all'**avvio di ogni progetto strutturale**, secondo le **NTC 2018**
(DM 17 gennaio 2018), **paragrafo 2.4**:

- **vita nominale di progetto V_N** (§2.4.1);
- **classe d'uso** e coefficiente d'uso **C_U** (§2.4.2);
- **periodo di riferimento per l'azione sismica V_R** (§2.4.3).

**Non è** uno strumento che definisce lo spettro di risposta o i periodi di ritorno degli stati limite: è un
**supporto documentale** che inquadra la scelta e richiama i valori tabellari. A valle, per lo spettro e i periodi
di ritorno T_R, usa `spettro-risposta-ntc` (§3.2).

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-vita-nominale-classe-uso` | Fissa V_N (Tab. 2.4.I: 10/50/100 anni, fase di costruzione >= P_N e >= 5 anni) e la classe d'uso I-IV (§2.4.1, §2.4.2) |
| `inquadra-periodo-riferimento-vr` | Ricava il periodo di riferimento V_R = V_N·C_U [2.4.1] con C_U (Tab. 2.4.II: 0,7/1,0/1,5/2,0) e ne indica l'uso a valle verso il §3.2 (§2.4.3) |

## Punti chiave (verificati sul testo)

- **Vita nominale V_N** (§2.4.1): numero di anni in cui l'opera, soggetta alla **necessaria manutenzione**,
  mantiene i livelli prestazionali. Valori **minimi** (Tab. 2.4.I): **10** anni (temporanee e provvisorie), **50**
  anni (prestazioni ordinarie), **100** anni (prestazioni elevate). Per la **fase di costruzione** di durata P_N:
  V_N **≥ P_N** e comunque **≥ 5 anni**; verifiche sismiche omettibili se la condizione dura **< 2 anni**.
- **Classi d'uso** (§2.4.2): in base alle conseguenze di interruzione di operatività/collasso — **I** (presenza
  occasionale, edifici agricoli), **II** (normali affollamenti), **III** (affollamenti significativi), **IV**
  (funzioni pubbliche o strategiche importanti).
- **Periodo di riferimento V_R** (§2.4.3): **V_R = V_N · C_U** [2.4.1], con coefficiente d'uso **C_U** (Tab.
  2.4.II) = **0,7 / 1,0 / 1,5 / 2,0** per le classi **I / II / III / IV** (**> 2** per attività a rischio di
  incidente rilevante). V_R è il periodo da cui, tramite le probabilità di superamento di ciascuno stato limite,
  si ricavano i periodi di ritorno T_R dell'azione sismica (§3.2).

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 2.4.1-2.4.3** - testo del Supplemento Ordinario n. 8 alla G.U. n.
  42 del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e trascritto
  verbatim; la formula [2.4.1] e le Tab. 2.4.I/2.4.II verificate anche sull'immagine della pagina.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non definisce** lo **spettro di risposta** né i **periodi di ritorno T_R** / le probabilità di superamento
  degli stati limite (§3.2): a valle usa `spettro-risposta-ntc`.
- **Non tratta** la valutazione delle **opere esistenti** né le **combinazioni delle azioni** (§2.5).
- **Non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista, né la lettura diretta del par. 2.4 delle NTC 2018 e della Circolare applicativa.**
