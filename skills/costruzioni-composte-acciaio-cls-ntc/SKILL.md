---
name: costruzioni-composte-acciaio-cls-ntc
description: "Supporto documentale al progettista strutturale per l'inquadramento della progettazione delle costruzioni composte di acciaio-calcestruzzo (travi con soletta collaborante, colonne composte; caso non sismico) secondo le NTC 2018 (DM 17 gennaio 2018), paragrafo 4.3. Aiuta a inquadrare gli stati limite aggiuntivi della connessione (resistenza allo SLU ed esercizio allo SLE) e le fasi costruttive; la classificazione delle sezioni composte secondo lo schema delle sezioni in acciaio (par. 4.2.3, con distribuzioni di tensioni plastiche o elastiche per le classi 1 e 2 ed elastiche per le classi 3 e 4) e l'analisi con l'omogeneizzazione per la viscosita' e l'analisi fessurata; le resistenze di progetto fd uguale a fk diviso il coefficiente parziale gamma_M con gamma_C uguale a 1,5 per il calcestruzzo, gamma_A uguale a 1,05 per l'acciaio da carpenteria, gamma_S uguale a 1,15 per l'acciaio da armatura e gamma_V uguale a 1,25 per le connessioni allo stato limite ultimo (gamma_M uguale a 1 allo stato limite di esercizio e nelle situazioni eccezionali), con la classe del calcestruzzo compresa tra C20/25 e C60/75; la resistenza a flessione delle travi con soletta collaborante con il metodo elastico, plastico (compressione del calcestruzzo pari a 0,85 fcd) ed elasto-plastico e la resistenza a taglio verticale affidata alla trave metallica; il sistema di connessione a taglio con il grado di connessione K uguale a N diviso Nf e la resistenza dei pioli con testa pari al minore fra PRd,a uguale a 0,8 per ftk per pi greco d al quadrato diviso 4, il tutto diviso gamma_V, e PRd,c uguale a 0,29 per alpha per d al quadrato per la radice del prodotto fck per Ecm, diviso gamma_V (con ftk non superiore a 500 MPa, diametro d tra 16 e 25 mm, alpha uguale a 0,2 per hsc su d piu' 1 per hsc su d tra 3 e 4 e 1,0 oltre), con le riduzioni per lamiera grecata; e le colonne composte. Use when a structural designer must frame the design of steel-concrete composite structures (non-seismic) under the Italian NTC 2018 par. 4.3; it is a documentary aid and does NOT compute the strengths or the verifications, does NOT size the section or the shear connection, does NOT reproduce the figures/tables (Fig. 4.3.3/4.3.4, Tab. 4.3.II) nor the material properties of par. 11.2/11.3 nor the Eurocodes (EN 1994), does NOT cover the seismic design (par. 7.6), and does NOT replace the structural designer or the 2019 Circular."
license: MIT
area: strutture-geotecnica
title: "Costruzioni composte acciaio-cls: connettori e verifiche (NTC 2018 par. 4.3)"
summary: "Inquadra la progettazione delle costruzioni composte acciaio-calcestruzzo (NTC 2018 par. 4.3): coefficienti fd=fk/gamma_M (gamma_C=1,5, gamma_A=1,05, gamma_S=1,15, gamma_V=1,25), classi delle sezioni, resistenza a flessione e connessione a taglio (pioli PRd,a/PRd,c)."
normative_refs:
  - "NTC 2018 (D.M. 17 gennaio 2018) - par. 4.3 Costruzioni composte acciaio-cls: fd=fk/gamma_M (gamma_C=1,5, gamma_A=1,05, gamma_S=1,15, gamma_V=1,25), sezioni, connettori a piolo PRd,a/PRd,c"
  - "Rinvio (non riprodotti): par. 4.1/4.2 e 11.2/11.3, par. 7.6 (sismica), Fig. 4.3.3/4.3.4 e Tab. 4.3.II (figure), UNI EN 1994 (EC4); Circolare 21/1/2019 n. 7"
version: 0.1.0-alpha
status: alpha
tags:
  - costruzioni-composte
  - acciaio-calcestruzzo
  - ntc-2018
  - connettori-a-taglio
  - coefficienti-parziali
---

# Costruzioni composte acciaio-calcestruzzo: materiali, connettori e verifiche (NTC 2018 par. 4.3)

## Quando usare questa skill

Usala quando un **progettista strutturale** deve **inquadrare** la **progettazione delle costruzioni
composte di acciaio-calcestruzzo** (travi con soletta collaborante, colonne composte; caso **non sismico**)
secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 4.3**:

- **materiali** e **coefficienti parziali** (§4.3.3);
- **classificazione** delle sezioni composte e **analisi** (§4.3.2);
- **resistenza** delle travi con soletta collaborante (§4.3.4);
- **sistema di connessione** a taglio e **colonne composte** (§4.3.4.3, 4.3.5).

**Non è** uno strumento che calcola resistenze o esegue verifiche, né dimensiona la sezione o la connessione:
è un **supporto documentale** che inquadra materiali, coefficienti, criteri e formule. Completa la famiglia
"costruzioni di X" con c.a. (§4.1), acciaio (§4.2), legno (§4.4) e muratura (§4.5).

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-materiali-sezioni-composte` | Coefficienti (γC/γA/γS/γV), classificazione delle sezioni e resistenza a flessione (elastico/plastico/elasto-plastico) (§4.3.2-4.3.4.2) |
| `inquadra-connessione-taglio-composte` | Grado di connessione K e resistenza dei pioli (PRd,a/PRd,c), con riduzioni per lamiera grecata (§4.3.4.3) |

## Punti chiave (verificati sul testo)

- **Ambito** (§4.3): acciaio + c.a. resi collaboranti da un sistema di connessione; rinvio a §4.1 e §4.2.
- **Coefficienti** (§4.3.3): **fd = fk/γM**; SLU **γC = 1,5**, **γA = 1,05**, **γS = 1,15**, **γV = 1,25**;
  SLE/eccezionali γM = 1. Classe cls **C20/25-C60/75**.
- **Sezioni** (§4.3.2.1): classificate come per l'acciaio (§4.2.3); classi 1-2 plastiche/elastiche, classi
  3-4 elastiche; armatura B450C in classe 1-2.
- **Flessione** (§4.3.4.2): momento resistente **elastico** (fcd/fyd/fsd), **plastico** (cls 0,85·fcd),
  **elasto-plastico**; taglio verticale alla trave metallica.
- **Connessione** (§4.3.4.3): **K = N/Nf**; pioli con testa **PRd = min(PRd,a; PRd,c)** con
  **PRd,a = 0,8·ftk·(π·d²/4)/γV** e **PRd,c = 0,29·α·d²·√(fck·Ecm)/γV** (ftk ≤ 500 MPa, d 16-25 mm,
  α = 0,2·(hsc/d+1) o 1,0); riduzioni lamiera grecata (kl, kt).

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 4.3** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e
  trascritto verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non calcola** le resistenze né esegue le verifiche; **non dimensiona** la sezione né la connessione.
- **Non riproduce** le **Fig. 4.3.3/4.3.4** né la **Tab. 4.3.II** (figure/tabella figurata → norma/EC4) né i
  materiali dei **§11.2/11.3** né gli **Eurocodici** (UNI EN 1994).
- **Non tratta** la **progettazione sismica** (§7.6); **non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, né la lettura del par. 4.3 delle NTC 2018 e della Circolare applicativa.**
