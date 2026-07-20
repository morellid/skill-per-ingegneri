---
name: costruzioni-calcestruzzo-ntc
description: "Supporto documentale al progettista strutturale per l'inquadramento della progettazione delle costruzioni di calcestruzzo (cemento armato, cemento armato precompresso, non armato; caso non sismico) secondo le NTC 2018 (DM 17 gennaio 2018), paragrafo 4.1. Aiuta a inquadrare le classi di resistenza del calcestruzzo (Tab. 4.1.I, da C8/10 a C90/105) e i metodi di analisi (elastica lineare, plastica, non lineare) con il limite dell'asse neutro x/d non superiore a 0,45 per fck fino a 50 MPa e 0,35 oltre; le resistenze di progetto dei materiali: calcestruzzo a compressione fcd uguale a alpha_cc per fck diviso il coefficiente parziale gamma_c, con alpha_cc uguale a 0,85 e gamma_c uguale a 1,5 (riducibile a 1,4 per produzione continuativa controllata con coefficiente di variazione non superiore al 10 per cento, e ridotta a 0,80 fcd per elementi piani gettati in opera con spessore inferiore a 50 mm), calcestruzzo a trazione fctd uguale a fctk diviso gamma_c, e acciaio fyd uguale a fyk diviso gamma_s con gamma_s uguale a 1,15 sempre per tutti i tipi di acciaio; i diagrammi di calcolo tensione-deformazione (parabola-rettangolo, triangolo-rettangolo, rettangolo o stress block, con epsilon_c2 uguale a 0,20 per cento ed epsilon_cu uguale a 0,35 per cento per le classi fino a C50/60) e il modello del calcestruzzo confinato; le verifiche agli stati limite ultimi (pressoflessione, taglio con il modello a traliccio e inclinazione dei puntoni tra 1 e 2,5, torsione, punzonamento); e le verifiche agli stati limite di esercizio con la fessurazione (stati limite di decompressione, formazione e apertura delle fessure con i valori limite w1 uguale a 0,2 mm, w2 uguale a 0,3 mm, w3 uguale a 0,4 mm secondo le condizioni ambientali e la sensibilita' delle armature) e la limitazione delle tensioni (sigma_c non superiore a 0,60 fck in combinazione caratteristica e 0,45 fck in combinazione quasi permanente, sigma_s non superiore a 0,8 fyk). Use when a structural designer must frame the design of reinforced/prestressed concrete structures (non-seismic) under the Italian NTC 2018 par. 4.1; it is a documentary aid and does NOT compute the strengths or the verifications, does NOT size or reinforce the members, does NOT reproduce the material properties (fck, fctk, fyk) of par. 11.2/11.3 nor the Eurocodes (EN 1992), does NOT cover the seismic design (par. 7.4) nor special concretes, and does NOT replace the structural designer or the 2019 Circular. It complements the code-driven predimensionamento-flessione-ca-ntc skill (bending pre-sizing)."
license: MIT
area: strutture-geotecnica
title: "Costruzioni di calcestruzzo: materiali e verifiche (NTC 2018 par. 4.1)"
summary: "Inquadra la progettazione delle costruzioni di calcestruzzo (NTC 2018 par. 4.1): classi di resistenza, resistenze di progetto fcd=alpha_cc*fck/gamma_c e fyd=fyk/gamma_s (gamma_c=1,5, gamma_s=1,15), diagrammi di calcolo, verifiche SLU e SLE (fessurazione, tensioni)."
normative_refs:
  - "NTC 2018 (D.M. 17 gennaio 2018) - par. 4.1 Costruzioni di calcestruzzo: classi (Tab. 4.1.I), fcd=alpha_cc*fck/gamma_c, fyd=fyk/gamma_s (gamma_c=1,5, gamma_s=1,15), diagrammi, SLU e SLE"
  - "Rinvio (non riprodotti): par. 11.2/11.3 (materiali, fck/fyk), par. 7.4 (sismica), par. 4.1.12 (leggeri) e 11.2.12 (FRC), UNI EN 1992 (EC2); Circolare 21/1/2019 n. 7"
version: 0.1.0-alpha
status: alpha
tags:
  - costruzioni-di-calcestruzzo
  - cemento-armato
  - ntc-2018
  - resistenze-di-progetto
  - coefficienti-parziali
---

# Costruzioni di calcestruzzo: materiali, resistenze e verifiche (NTC 2018 par. 4.1)

## Quando usare questa skill

Usala quando un **progettista strutturale** deve **inquadrare** la **progettazione delle costruzioni di
calcestruzzo** (c.a., c.a.p., non armato; caso **non sismico**) secondo le **NTC 2018** (DM 17 gennaio 2018),
**paragrafo 4.1**:

- **classi di resistenza** (Tab. 4.1.I) e **metodi di analisi** (§4.1, 4.1.1);
- **resistenze di progetto** e coefficienti parziali γc, γs (§4.1.2.1.1);
- **diagrammi di calcolo** dei materiali (§4.1.2.1.2);
- **verifiche SLU** (pressoflessione, taglio, torsione) e **SLE** (fessurazione, tensioni) (§4.1.2.2-3).

**Non è** uno strumento che calcola resistenze o esegue verifiche, né dimensiona o arma gli elementi: è un
**supporto documentale** che inquadra classi, coefficienti, resistenze e criteri di verifica. È
complementare (documentale) al code-driven `predimensionamento-flessione-ca-ntc`.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-resistenze-progetto-ca` | Classi di resistenza (Tab. 4.1.I), coefficienti γc/γs e resistenze di progetto fcd/fctd/fyd con i diagrammi di calcolo (§4.1, 4.1.2.1) |
| `inquadra-verifiche-slu-sle-ca` | Verifiche SLU (pressoflessione, taglio, torsione, punzonamento) e SLE (fessurazione w1/w2/w3, limitazione tensioni) (§4.1.2.2-3) |

## Punti chiave (verificati sul testo)

- **Classi** (§4.1, Tab. 4.1.I): da **C8/10** a **C90/105**; proprietà del materiale al §11.2. Analisi con
  limite dell'asse neutro **x/d ≤ 0,45** (fck ≤ 50) / **0,35** (fck > 50).
- **Resistenze di progetto** (§4.1.2.1.1): **fcd = αcc·fck/γc** (**αcc = 0,85**, **γc = 1,5**, → 1,4 per
  produzione controllata; **0,80·fcd** per elementi piani < 50 mm); **fctd = fctk/γc**; **fyd = fyk/γs**
  (**γs = 1,15** sempre).
- **Diagrammi** (§4.1.2.1.2): parabola-rettangolo/triangolo-rettangolo/stress block; **εc2 = 0,20%**,
  **εcu = 0,35%** (≤ C50/60).
- **SLU** (§4.1.2.3): pressoflessione, **taglio** (traliccio, **1 ≤ ctgθ ≤ 2,5**), **torsione**,
  punzonamento.
- **SLE** (§4.1.2.2): **fessurazione** (decompressione/formazione/apertura, **w1 = 0,2 / w2 = 0,3 / w3 =
  0,4 mm**); **tensioni** (**σc ≤ 0,60·fck** rara, **σc ≤ 0,45·fck** quasi permanente, **σs ≤ 0,8·fyk**).

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 4.1** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e
  trascritto verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non calcola** le resistenze né esegue le verifiche; **non dimensiona** né **arma** gli elementi.
- **Non riproduce** le proprietà dei materiali (fck, fctk, fyk, moduli) dei **§11.2/11.3** né gli
  **Eurocodici** (UNI EN 1992).
- **Non tratta** la **progettazione sismica** (§7.4) né i **calcestruzzi speciali** (leggeri §4.1.12,
  fibrorinforzati §11.2.12); **non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, né la lettura del par. 4.1 delle NTC 2018 e della Circolare applicativa.**
