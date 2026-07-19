---
name: costruzioni-acciaio-ntc
description: "Supporto documentale al progettista strutturale per l'inquadramento della progettazione delle costruzioni di acciaio (caso non sismico) secondo le NTC 2018 (DM 17 gennaio 2018), paragrafo 4.2. Aiuta a inquadrare la scelta dei materiali (gradi da S235 a S460, con le tensioni caratteristiche di snervamento fyk e di rottura ftk delle Tabelle 4.2.I per i profili a sezione aperta e 4.2.II per quelli a sezione cava); la classificazione delle sezioni trasversali nelle classi 1 duttili (capacita' rotazionale Ctheta maggiore o uguale a 3), 2 compatte (Ctheta maggiore o uguale a 1,5), 3 semi-compatte e 4 snelle (con sezione efficace), e i metodi di calcolo della capacita' resistente (elastico, plastico, elasto-plastico) e di analisi globale ammessi per ciascuna classe; gli effetti del secondo ordine (analisi del primo ordine ammessa se alpha_cr maggiore o uguale a 10 in campo elastico e 15 in campo plastico) e delle imperfezioni; le verifiche agli stati limite ultimi con la resistenza di progetto Rd uguale a Rk diviso il coefficiente parziale gamma_M e la Tabella 4.2.VII (gamma_M0 uguale a 1,05 per la resistenza delle sezioni, gamma_M1 uguale a 1,05 e 1,10 per i ponti per la stabilita', gamma_M2 uguale a 1,25 per la frattura delle sezioni tese indebolite dai fori), le resistenze di progetto a trazione (resistenza plastica della sezione lorda A per fyk diviso gamma_M0 e resistenza a rottura della sezione netta 0,9 per Anet per ftk diviso gamma_M2), compressione, flessione (con il modulo plastico, elastico o efficace secondo la classe) e taglio (Av per fyk diviso radice di 3 per gamma_M0); le verifiche di stabilita' delle membrature (aste compresse con Nb,Rd uguale a chi per A per fyk diviso gamma_M1 e la snellezza normalizzata, con instabilita' trascurabile per snellezza normalizzata minore di 0,2, e la limitazione della snellezza a 200 per le membrature principali e 250 per le secondarie; travi inflesse con la verifica a svergolamento chi_LT); e lo stato limite di fatica. Use when a structural designer must frame the design of steel structures (non-seismic) under the Italian NTC 2018 par. 4.2; it is a documentary aid and does NOT compute the strengths or the verifications, does NOT size the members or the connections, does NOT reproduce the width-to-thickness classification tables (Tab. 4.2.III-V) nor the buckling curves (Tab. 4.2.VIII) which are figures in the PDF, does NOT reproduce the material properties of par. 11.3.4 nor the Eurocodes (EN 1993), does NOT cover the seismic design (par. 7.5), and does NOT replace the structural designer or the 2019 Circular."
license: MIT
area: strutture-geotecnica
title: "Costruzioni di acciaio: materiali, classi e verifiche (NTC 2018 par. 4.2)"
summary: "Inquadra la progettazione delle costruzioni di acciaio (NTC 2018 par. 4.2): materiali S235-S460 (fyk/ftk, Tab. 4.2.I/II), classi di sezione 1-4, coefficienti gamma_M (Tab. 4.2.VII: 1,05/1,05/1,25), resistenze di progetto Rd=Rk/gamma_M e verifiche di stabilita' (Nb,Rd, chi)."
normative_refs:
  - "NTC 2018 (D.M. 17 gennaio 2018) - par. 4.2 Costruzioni di acciaio: materiali S235-S460 (Tab. 4.2.I/II), classi di sezione 1-4, gamma_M (Tab. 4.2.VII), Rd=Rk/gamma_M, resistenze SLU e stabilita'"
  - "Rinvio (non riprodotti): par. 11.3.4 (materiali, bulloni), par. 7.5 (sismica), Tab. 4.2.III-V (b/t) e 4.2.VIII (curve) come figure, UNI EN 1993 (EC3) e 1090-2; Circolare 21/1/2019 n. 7"
version: 0.1.0-alpha
status: alpha
tags:
  - costruzioni-di-acciaio
  - carpenteria-metallica
  - ntc-2018
  - classi-di-sezione
  - coefficienti-parziali
---

# Costruzioni di acciaio: materiali, classi di sezione e verifiche (NTC 2018 par. 4.2)

## Quando usare questa skill

Usala quando un **progettista strutturale** deve **inquadrare** la **progettazione delle costruzioni di
acciaio** (caso **non sismico**) secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 4.2**:

- **materiali** (gradi S235-S460, fyk/ftk - Tab. 4.2.I/II) (§4.2.1);
- **classificazione delle sezioni** (classi 1-4) e metodi di calcolo (§4.2.3);
- **resistenze di progetto** SLU e coefficiente **γM** (Tab. 4.2.VII) (§4.2.4.1.1-2);
- **verifiche di stabilità** delle membrature (aste compresse, travi inflesse) (§4.2.4.1.3).

**Non è** uno strumento che calcola resistenze o esegue verifiche, né dimensiona membrature e collegamenti:
è un **supporto documentale** che inquadra materiali, classi, coefficienti, resistenze e criteri di
verifica.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-classe-sezione-resistenze-acciaio` | Materiali (S235-S460, Tab. 4.2.I/II), classe di sezione (1-4), γM (Tab. 4.2.VII) e resistenze di progetto SLU (§4.2.1, 4.2.3.1, 4.2.4.1) |
| `inquadra-stabilita-analisi-acciaio` | Metodo di analisi (α_cr) e verifiche di stabilità delle membrature (Nb,Rd, χ, λ̄, svergolamento) (§4.2.3, 4.2.4.1.3) |

## Punti chiave (verificati sul testo)

- **Materiali** (§4.2.1): gradi **S235-S460**; fyk/ftk dalle Tab. 4.2.I (sezione aperta) e 4.2.II (cava);
  esecuzione UNI EN 1090-2.
- **Classi di sezione** (§4.2.3.1): **1 duttili** (Cθ ≥ 3), **2 compatte** (Cθ ≥ 1,5), **3 semi-compatte**,
  **4 snelle** (sezione efficace); classe composta = valore più alto.
- **Analisi** (§4.2.3): metodi E/P/EP; primo ordine ammesso se **α_cr ≥ 10** (elastica) / **≥ 15**
  (plastica).
- **Coefficienti** (§4.2.4.1.1, Tab. 4.2.VII): **Rd = Rk/γM**; **γM0 = 1,05** (sezioni), **γM1 = 1,05**
  (stabilità; 1,10 ponti), **γM2 = 1,25** (frattura sezioni tese forate).
- **Resistenze SLU** (§4.2.4.1.2): trazione min(**A·fyk/γM0**, **0,9·Anet·ftk/γM2**); compressione
  **A·fyk/γM0**; flessione **Wpl/Wel/Weff·fyk/γM0** (classe 1-2/3/4); taglio **Av·fyk/(√3·γM0)**.
- **Stabilità** (§4.2.4.1.3): **Nb,Rd = χ·A·fyk/γM1**; χ da [4.2.44]; instabilità trascurabile se **λ̄ <
  0,2**; snellezza **λ ≤ 200** (principali) / **250** (secondarie); svergolamento **χLT** (αLT
  0,21/0,34/0,49/0,76).

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 4.2** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e
  trascritto verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non calcola** le resistenze né esegue le verifiche; **non dimensiona** membrature e collegamenti.
- **Non riproduce** le **Tab. 4.2.III-V** (b/t) né la **Tab. 4.2.VIII** (curve di instabilità), che nel PDF
  sono figure: vanno lette sulla norma o su **UNI EN 1993** (EC3).
- **Non riproduce** i materiali del **§11.3.4** né gli Eurocodici; **non tratta** la **progettazione
  sismica** (§7.5); **non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, né la lettura del par.
4.2 delle NTC 2018 e della Circolare applicativa.**
