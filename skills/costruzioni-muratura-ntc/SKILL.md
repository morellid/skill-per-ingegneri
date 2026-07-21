---
name: costruzioni-muratura-ntc
description: "Supporto documentale al progettista strutturale per l'inquadramento della progettazione delle costruzioni in muratura (caso non sismico) secondo le NTC 2018 (DM 17 gennaio 2018), paragrafo 4.5. Aiuta a inquadrare la classificazione degli elementi resistenti in base alla percentuale di foratura (elementi pieni, semipieni e forati delle Tabelle 4.5.Ia e 4.5.Ib) e la categoria degli elementi; le caratteristiche meccaniche della muratura (resistenza caratteristica a compressione fk e a taglio fvk, moduli di elasticita', con controllo sperimentale per fk maggiore o uguale a 8 MPa); l'organizzazione strutturale con il comportamento scatolare, i cordoli e gli incatenamenti, gli spessori minimi dei muri portanti (150, 200, 240 mm per gli elementi artificiali pieni, semipieni e forati; 240, 400, 500 mm per la pietra squadrata, listata e non squadrata) e la snellezza convenzionale non superiore a 20; le resistenze di progetto fd uguale a fk diviso il coefficiente parziale gamma_M e fvd uguale a fvk diviso gamma_M, con la Tabella 4.5.II che fornisce gamma_M da 2,0 a 3,0 in funzione della classe di esecuzione 1 o 2 e della categoria degli elementi I o II; le verifiche agli stati limite ultimi (pressoflessione fuori piano e nel piano, taglio, carichi concentrati) con il metodo semplificato per i carichi laterali; le verifiche semplificate per gli edifici semplici con gamma_M uguale a 4,2 e i relativi limiti; e la muratura armata. Use when a structural designer must frame the design of masonry buildings (non-seismic) under the Italian NTC 2018 par. 4.5; it is a documentary aid and does NOT compute the strengths or the verifications, does NOT size the masonry, does NOT cover the seismic design (par. 7.8), the fire resistance or the material chapter 11.10, and does NOT replace the structural designer or the 2019 Circular."
license: MIT
area: strutture-geotecnica
title: "Costruzioni in muratura: materiali, verifiche e coefficienti (NTC 2018 par. 4.5)"
summary: "Inquadra la progettazione delle costruzioni in muratura (NTC 2018 par. 4.5): categorie degli elementi (Tab. 4.5.I), spessori minimi e snellezza, resistenze di progetto fd=fk/gamma_M (Tab. 4.5.II), verifiche SLU, verifiche semplificate (gamma_M=4,2) e muratura armata."
normative_refs:
  - "NTC 2018 (D.M. 17 gennaio 2018) - par. 4.5 Costruzioni di muratura: materiali/categorie (Tab. 4.5.I), snellezza, resistenze di progetto e Tab. 4.5.II (gamma_M), verifiche SLU e semplificate"
  - "Rinvio (non riprodotti): par. 7.8 (sismica) e Tab. 7.8.II, par. 4.5.11 (fuoco), cap. 11.10 (materiali), par. 4.6 (Eurocodici) NTC 2018; Circolare 21/1/2019 n. 7"
version: 0.1.0-alpha
status: alpha
tags:
  - costruzioni-in-muratura
  - muratura-portante
  - ntc-2018
  - resistenze-di-progetto
  - coefficienti-parziali
---

# Costruzioni in muratura: materiali, verifiche e coefficienti (NTC 2018 par. 4.5)

## Quando usare questa skill

Usala quando un **progettista strutturale** deve **inquadrare** la **progettazione delle costruzioni in
muratura** (caso **non sismico**) secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 4.5**:

- **materiali** e **categorie** degli elementi resistenti (§4.5.2);
- **organizzazione strutturale**, spessori minimi e **snellezza** (§4.5.4);
- **resistenze di progetto** e coefficiente **γM** (Tab. 4.5.II) (§4.5.6.1);
- **verifiche SLU**, **verifiche semplificate** e **muratura armata** (§4.5.6-4.5.7).

**Non è** uno strumento che calcola resistenze o esegue verifiche, né dimensiona la muratura: è un
**supporto documentale** che inquadra materiali, categorie, criteri, verifiche e coefficienti.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-materiali-resistenze-muratura` | Classificazione elementi (Tab. 4.5.I), caratteristiche meccaniche e resistenze di progetto con γM (Tab. 4.5.II) (§4.5.2, 4.5.3, 4.5.6.1) |
| `inquadra-organizzazione-verifiche-muratura` | Organizzazione strutturale, spessori e snellezza, verifiche SLU e verifiche semplificate (§4.5.4, 4.5.6.2, 4.5.6.4) |

## Punti chiave (verificati sul testo)

- **Elementi** (§4.5.2): classificati per **foratura Π** (Tab. 4.5.Ia/Ib): **pieni** (≤15%), **semipieni**
  (15-45%), **forati** (45-55%); **categoria I o II** (§11.10.1).
- **Meccanica** (§4.5.3): **fk**, **fvk0**, **E**, **G**; controllo sperimentale se **fk ≥ 8 MPa**.
- **Organizzazione** (§4.5.4): comportamento **scatolare**; **spessori minimi** 150/200/240 (artificiali)
  e 240/400/500 (pietra) mm; **snellezza λ = h0/t ≤ 20**.
- **Resistenze di progetto** (§4.5.6.1): **fd = fk/γM**, **fvd = fvk/γM**; **Tab. 4.5.II** γM = 2,0/2,2/2,5
  (classe 1) e 2,5/2,7/3,0 (classe 2) secondo categoria e malta.
- **SLU** (§4.5.6.2): pressoflessione fuori/nel piano, taglio, carichi concentrati; metodo semplificato
  **fd,rid = Φ·fd** (Tab. 4.5.III), h0 = ρ·h (Tab. 4.5.IV), eccentricità **e ≤ 0,33 t**.
- **Verifiche semplificate** (§4.5.6.4): **γM = 4,2**; ≤ 3 piani (ordinaria)/4 (armata); interpiano ≤ 3,5
  m; **snellezza ≤ 12**; carico variabile ≤ 3 kN/m²; **σ = N/(0,65 A) ≤ fk/γM**.
- **Muratura armata** (§4.5.7): barre ≥ 5 mm; percentuali di armatura; malta ≥ 10 MPa, cls ≥ C12/15; **γs =
  1,15**.

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 4.5** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e
  trascritto verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non calcola** le resistenze né esegue le verifiche; **non dimensiona** la muratura.
- **Non tratta** la **progettazione sismica** (§7.8), la **resistenza al fuoco** (§4.5.11), il **cap.
  11.10** (materiali) né gli **Eurocodici** (§4.6).
- **Non riproduce** le tabelle dei materiali (§11.10) né la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, né la lettura del par.
4.5 delle NTC 2018 e della Circolare applicativa.**
