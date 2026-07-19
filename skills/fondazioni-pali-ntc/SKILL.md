---
name: fondazioni-pali-ntc
description: "Supporto documentale al progettista strutturale e geotecnico per l'inquadramento delle verifiche delle fondazioni su pali e delle fondazioni miste a platea su pali secondo le NTC 2018 (DM 17 gennaio 2018), paragrafo 6.4.3. Aiuta a inquadrare l'impostazione del progetto con gli effetti di gruppo e l'attrito negativo (coefficienti M1 della Tabella 6.2.II) e il rinvio al paragrafo 7.11.5.3.2 per il sismico; le verifiche agli stati limite ultimi dei pali - GEO (carico limite assiale, carico limite trasversale, sfilamento in trazione, stabilita' globale) e STR - con la stabilita' globale in Approccio 1 Combinazione 2 (A2+M2+R2) e le rimanenti verifiche in Approccio 2 (A1+M1+R3); le resistenze a carico assiale con i coefficienti parziali della Tabella 6.4.II (base 1,15/1,35/1,3, laterale in compressione 1,15, totale 1,15/1,30/1,25, laterale in trazione 1,25 per pali infissi, trivellati e ad elica continua) e la determinazione della resistenza caratteristica con i fattori di correlazione delle Tabelle 6.4.III (prove statiche), 6.4.IV (verticali indagate) e 6.4.V (prove dinamiche); la resistenza della palificata con l'effetto di gruppo; i carichi trasversali con il coefficiente della Tabella 6.4.VI (1,3); le verifiche di esercizio su cedimenti e spostamenti; le fondazioni miste; i controlli d'integrita' (almeno il 5 per cento dei pali, minimo 2) e le prove di carico di progetto e in corso d'opera. Use when a structural or geotechnical designer must frame the limit-state verifications of pile foundations (and piled rafts) under the Italian NTC 2018 par. 6.4.3; it is a documentary aid and does NOT compute the resistances, the verifications or the coefficients, does NOT size the piles or the pile group, does NOT reproduce Tables 6.2.I/6.2.II/6.8.I or the 2019 Circular, does NOT cover the seismic case (par. 7.11.5.3.2), and does NOT replace the designer or the geotechnical report."
license: MIT
area: strutture-geotecnica
title: "Fondazioni su pali: verifiche SLU/SLE e coefficienti NTC 2018 (par. 6.4.3)"
summary: "Inquadra le verifiche delle fondazioni su pali (NTC 2018 par. 6.4.3): SLU GEO/STR con stabilita' globale in Approccio 1 (A2+M2+R2) e rimanenti in Approccio 2 (A1+M1+R3), Tab. 6.4.II e 6.4.VI, fattori di correlazione, fondazioni miste, controlli d'integrita' e prove di carico."
normative_refs:
  - "NTC 2018 (D.M. 17 gennaio 2018) - par. 6.4.3 Fondazioni su pali: verifiche SLU/SLE, Tab. 6.4.II (gamma_R), Tab. 6.4.III/IV/V (correlazione), Tab. 6.4.VI, controlli d'integrita' e prove di carico"
  - "Rinvio (non riprodotti): Tabelle 6.2.I/6.2.II (azioni e parametri), Tab. 6.8.I (stabilita' globale), Tab. 6.4.I, par. 6.4.2/6.8/7.11.5.3.2 (sismico) NTC 2018; Circolare 21/1/2019 n. 7"
version: 0.1.0-alpha
status: alpha
tags:
  - fondazioni-su-pali
  - pali-e-palificate
  - ntc-2018
  - stati-limite-geotecnici
  - coefficienti-parziali
---

# Fondazioni su pali: verifiche SLU/SLE e coefficienti NTC 2018 (par. 6.4.3)

## Quando usare questa skill

Usala quando un **progettista strutturale o geotecnico** deve **inquadrare** le **verifiche delle
fondazioni su pali** (e delle **fondazioni miste** a platea su pali) secondo le **NTC 2018** (DM 17
gennaio 2018), **paragrafo 6.4.3**:

- **impostazione** del progetto, effetti di gruppo e attrito negativo (§6.4.3);
- **verifiche SLU** dei pali (stati limite, approcci, coefficienti) (§6.4.3.1);
- **resistenza caratteristica** e fattori di correlazione (§6.4.3.1.1);
- **verifiche SLE**, **fondazioni miste**, **controlli d'integrità** e **prove di carico** (§6.4.3.2-7).

**Non è** uno strumento che calcola resistenze, verifiche o coefficienti, né dimensiona i pali: è un
**supporto documentale** che inquadra stati limite, approcci progettuali, coefficienti e fattori di
correlazione.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-verifiche-slu-sle-pali` | Stati limite, approcci e combinazioni per pali e fondazioni miste, con Tab. 6.4.II e Tab. 6.4.VI (§6.4.3.1-6.4.3.4) |
| `inquadra-resistenza-caratteristica-prove` | Resistenza caratteristica con i fattori di correlazione, controlli d'integrità e prove di carico (§6.4.3.1.1, 6.4.3.6, 6.4.3.7) |

## Punti chiave (verificati sul testo)

- **Impostazione** (§6.4.3): soli pali (§6.4.3.1-2) o fondazione mista (§6.4.3.3-4); tra le azioni
  permanenti **peso proprio del palo** e **attrito negativo** (γM del caso **M1**, Tab. 6.2.II); sisma
  §7.11.5.3.2.
- **SLU** (§6.4.3.1): **GEO** (carico limite assiale, carico limite trasversale, sfilamento in trazione,
  **stabilità globale**) e **STR**; **stabilità globale** → **Approccio 1, Comb. 2 (A2+M2+R2)**;
  **rimanenti** → **Approccio 2 (A1+M1+R3)**; nelle STR il γR **non** si porta in conto.
- **Tab. 6.4.II (γR, R3)**: base **1,15/1,35/1,3**, laterale in compressione **1,15**, totale
  **1,15/1,30/1,25**, laterale in trazione **1,25** (infissi/trivellati/elica).
- **Resistenza caratteristica** (§6.4.3.1.1): minore tra media e minimo con i **fattori di correlazione
  ξ** delle Tab. **6.4.III** (prove statiche), **6.4.IV** (verticali indagate), **6.4.V** (prove
  dinamiche). **Palificata**: somma con **effetto di gruppo**.
- **Carichi trasversali** (§6.4.3.1.2): **γT = 1,3** (Tab. 6.4.VI).
- **SLE** (§6.4.3.2): cedimenti/sollevamenti e spostamenti trasversali (combinazioni caratteristiche
  §2.5.3).
- **Controlli d'integrità** (§6.4.3.6): almeno **5% dei pali, minimo 2**; grande diametro (d ≥ 80 cm) con
  ≤ 4 pali → tutti. **Prove di carico** (§6.4.3.7): di progetto ≥ **2,5×** l'azione SLE; in corso d'opera
  **1,5×** (o **1,2×** se strumentati).

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 6.4.3** - testo del Supplemento Ordinario n. 8 alla G.U. n.
  42 del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e
  trascritto verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non calcola** resistenze, verifiche o coefficienti; **non dimensiona** i pali o la palificata.
- **Non riproduce** le **Tabelle 6.2.I/6.2.II/6.8.I** né la **Circolare 21/1/2019 n. 7**.
- **Non tratta** il caso **sismico** (§7.11.5.3.2) né le fondazioni superficiali (§6.4.2, skill
  `capacita-portante-fondazione-ntc`) se non nei richiami.

**La skill è un supporto documentale: non sostituisce il progettista strutturale/geotecnico o la
relazione geotecnica, né la lettura del par. 6.4.3 delle NTC 2018 e della Circolare applicativa.**
