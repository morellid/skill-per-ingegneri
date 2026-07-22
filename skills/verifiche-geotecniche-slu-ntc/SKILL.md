---
name: verifiche-geotecniche-slu-ntc
description: "Supporto documentale al progettista geotecnico o strutturista per l'inquadramento del framework semiprobabilistico delle verifiche geotecniche agli stati limite ultimi - approcci progettuali e coefficienti parziali - secondo le NTC 2018 (DM 17 gennaio 2018), paragrafo 6.2.4 (con il valore caratteristico del par. 6.2.2). Aiuta a impostare le verifiche SLU: stati limite di perdita di equilibrio EQU (azione instabilizzante non maggiore di quella stabilizzante), di resistenza dell'elemento strutturale STR e di resistenza del terreno GEO (effetto delle azioni di progetto non maggiore della resistenza di progetto, formula 6.2.1); i due approcci progettuali alternativi (Approccio 1 con due combinazioni di gruppi di coefficienti, Approccio 2 con un'unica combinazione), con la regola di default per gli stati limite non trattati nei paragrafi 6.3-6.11 (Approccio 1 con le combinazioni A1+M1+R1 e A2+M2+R2, coefficienti del gruppo R1 sempre unitari e del gruppo R2 maggiori o uguali all'unita'); i coefficienti parziali sulle azioni A1 e A2 (Tabella 6.2.I, con carichi permanenti G1 sfavorevoli 1,3 in A1 e 1,0 in A2, G2 sfavorevoli 1,5 e 1,3, azioni variabili 1,5 e 1,3) e sui parametri geotecnici M1 e M2 (Tabella 6.2.II: tangente dell'angolo di resistenza al taglio e coesione efficace con coefficiente 1,0 in M1 e 1,25 in M2, resistenza non drenata 1,0 e 1,4, peso dell'unita' di volume 1,0); e la definizione di valore caratteristico come stima ragionata e cautelativa del parametro per ogni stato limite (par. 6.2.2). Use when a geotechnical or structural designer must frame the ultimate limit state geotechnical verifications (design approaches, A/M/R partial factors) under the Italian NTC 2018 par. 6.2.4; it is a documentary aid and does NOT run the verifications, does NOT reproduce the resistance factors R specific to each work (par. 6.3-6.11), and does NOT replace the designer or the 2019 Circular."
license: MIT
area: strutture-geotecnica
title: "Verifiche geotecniche SLU: approcci e coefficienti (NTC 2018 par. 6.2.4)"
summary: "Inquadra il framework delle verifiche geotecniche agli SLU (NTC 2018 par. 6.2.4): SLU EQU/STR/GEO, approcci progettuali 1 e 2, default (A1+M1+R1)+(A2+M2+R2), coefficienti azioni Tab. 6.2.I e parametri M1/M2 Tab. 6.2.II (tan phi'/c' 1,25, cu 1,4)."
normative_refs:
  - "NTC 2018 (D.M. 17 gennaio 2018) - par. 6.2.4.1: SLU geotecnici EQU (Einst<=Estb), STR/GEO (Ed<=Rd [6.2.1]); approcci 1 e 2; default Approccio 1 con (A1+M1+R1) e (A2+M2+R2), R1 unitari, R2>=1"
  - "NTC 2018 - par. 6.2.4.1.1 Tab. 6.2.I: coefficienti parziali azioni EQU/A1/A2 (G1 sfav 1,1/1,3/1,0; G2 sfav 1,5/1,5/1,3; Q sfav 1,5/1,5/1,3)"
  - "NTC 2018 - par. 6.2.4.1.2 Tab. 6.2.II (M1/M2): tan phi' 1,0/1,25; c' 1,0/1,25; cu 1,0/1,4; peso 1,0/1,0; valore caratteristico par. 6.2.2 (stima ragionata e cautelativa)"
version: 0.1.0-alpha
status: alpha
tags:
  - verifiche-geotecniche
  - approcci-progettuali
  - coefficienti-parziali
  - stati-limite-ultimi
  - ntc-2018
---

# Verifiche geotecniche SLU: approcci e coefficienti (NTC 2018 par. 6.2.4)

## Quando usare questa skill

Usala quando un **progettista geotecnico o strutturista** deve **impostare le verifiche geotecniche agli stati
limite ultimi** — scegliere l'**approccio progettuale** e applicare i **coefficienti parziali** su azioni,
parametri del terreno e resistenze — secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 6.2.4** (con il
valore caratteristico del §6.2.2):

- **stati limite ultimi geotecnici** EQU, STR, GEO (§6.2.4.1);
- **approcci progettuali** 1 e 2 e **coefficienti** A/M/R (§6.2.4);
- **valore caratteristico** dei parametri geotecnici (§6.2.2).

**Non è** uno strumento che esegue le verifiche: è un **supporto documentale** che inquadra il framework generale.
I **coefficienti R** specifici di ciascuna opera stanno nelle skill d'opera (`opere-sostegno-ntc`,
`capacita-portante-fondazione-ntc`, `fondazioni-pali-ntc`, `stabilita-pendii-naturali-ntc`,
`opere-materiali-sciolti-scavi-ntc`, `opere-sotterraneo-gallerie-ntc`, `tiranti-ancoraggio-ntc`, §6.3-6.11).

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-approcci-progettuali-slu` | SLU EQU/STR/GEO, approcci 1 e 2, default (A1+M1+R1)+(A2+M2+R2), coefficienti sulle azioni Tab. 6.2.I (§6.2.4.1, 6.2.4.1.1) |
| `inquadra-coefficienti-parametri-geotecnici` | Coefficienti M1/M2 sui parametri del terreno (Tab. 6.2.II), resistenza di progetto Rd e valore caratteristico (§6.2.4.1.2, 6.2.2) |

## Punti chiave (verificati sul testo)

- **SLU geotecnici** (§6.2.4.1): **EQU** (perdita di equilibrio) → **Einst,d ≤ Estb,d** (colonna EQU Tab. 6.2.I);
  **STR** (resistenza elemento strutturale) e **GEO** (resistenza del terreno) → **Ed ≤ Rd** [6.2.1].
- **Approcci progettuali** (§6.2.4): **Approccio 1** = due combinazioni; **Approccio 2** = una combinazione. Per
  gli SLU **non trattati** nei §6.3-6.11 si usa l'**Approccio 1** con **(A1+M1+R1)** e **(A2+M2+R2)**; **R1 sempre
  unitari**, **R2 ≥ 1**. Gruppi: azioni **A1/A2**, parametri **M1/M2**, resistenze **R1/R2/R3**.
- **Coefficienti azioni** (Tab. 6.2.I, EQU/A1/A2): G1 sfav **1,1/1,3/1,0**; G2 sfav **1,5/1,5/1,3**; Q sfav
  **1,5/1,5/1,3** (favorevoli: G1 0,9/1,0/1,0, G2 0,8/0,8/0,8, Q 0,0). Terreno e acqua sono carichi permanenti
  (strutturali); per la spinta delle terre si usano i γG1.
- **Coefficienti parametri** (Tab. 6.2.II, M1/M2): **tan φ'k** 1,0/**1,25**; **c'k** 1,0/**1,25**; **cuk**
  1,0/**1,4**; **γ** 1,0/1,0. La resistenza **Rd** si ottiene dai valori caratteristici **/γM** con i **γR** di
  ciascuna opera.
- **Valore caratteristico** (§6.2.2): **stima ragionata e cautelativa** del parametro per **ogni stato limite**.

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 6.2.2 e 6.2.4** - testo del Supplemento Ordinario n. 8 alla G.U. n.
  42 del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e trascritto
  verbatim; le Tab. 6.2.I e 6.2.II verificate anche sull'immagine della pagina.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non esegue** le verifiche né calcola **Ed / Rd**, la spinta o le resistenze.
- **Non riproduce** i coefficienti **γR** (gruppi R1/R2/R3) specifici di ciascuna opera (§6.3-6.11): quelli stanno
  nelle skill d'opera.
- **Non tratta** in dettaglio le **verifiche SLE** geotecniche (§6.2.4.2).
- **Non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista geotecnico/strutturista, né la lettura dei par. 6.2.2-6.2.4 delle NTC 2018 e della Circolare applicativa.**
