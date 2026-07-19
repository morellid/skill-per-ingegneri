---
name: carichi-permanenti-sovraccarichi-ntc
description: "Supporto documentale al progettista strutturale per l'inquadramento dei carichi permanenti e dei sovraccarichi variabili per categoria d'uso delle costruzioni civili e industriali secondo le NTC 2018 (DM 17 gennaio 2018), paragrafo 3.1. Aiuta a inquadrare i pesi propri dei materiali strutturali con i pesi dell'unita' di volume della Tabella 3.1.I (calcestruzzo armato 25,0 kN/m3, acciaio 78,5, laterizio, legno, ecc.); i carichi permanenti non strutturali con la correlazione del carico equivalente distribuito g2 dei tramezzi al peso proprio lineare G2 delle partizioni (0,40, 0,80, 1,20, 1,60, 2,00 kN/m2 per G2 fino a cinque kN/m; oltre, posizionamento effettivo sul solaio); i sovraccarichi variabili qk distribuiti, Qk concentrati e Hk orizzontali per le categorie d'uso della Tabella 3.1.II (residenziale A, uffici B1/B2, ambienti suscettibili di affollamento C1-C5, commerciale D1/D2, magazzini e industriale E1/E2, rimesse e parcheggi F/G, coperture H/I/K, scale e balconi); le riduzioni dei sovraccarichi con il coefficiente per l'area di influenza e con il coefficiente per il numero di piani caricati, non combinabili tra loro; e le regole per i carichi concentrati e orizzontali nelle verifiche locali. Use when a structural designer must frame the permanent loads and the imposed (variable) loads by category of use of civil and industrial buildings under the Italian NTC 2018 par. 3.1; it is a documentary aid and does NOT compute the design loads or combine the actions, does NOT size the members, does NOT cover bridge traffic loads, the seismic action or wind and snow, and does NOT replace the structural designer or the 2019 Circular."
license: MIT
area: strutture-geotecnica
title: "Carichi permanenti e sovraccarichi variabili (NTC 2018 par. 3.1)"
summary: "Inquadra i carichi permanenti e i sovraccarichi variabili per categoria d'uso (NTC 2018 par. 3.1): pesi propri (Tab. 3.1.I), carico equivalente g2 dei divisori, sovraccarichi qk/Qk/Hk per categoria (Tab. 3.1.II), riduzioni per area di influenza e per numero di piani."
normative_refs:
  - "NTC 2018 (D.M. 17 gennaio 2018) - par. 3.1: pesi propri (Tab. 3.1.I), carichi permanenti non strutturali e g2, sovraccarichi per categoria d'uso (Tab. 3.1.II), riduzioni alpha_A/alpha_n, carichi Qk/Hk"
  - "Rinvio (non riprodotti): Tab. 2.5.I (coefficienti psi) NTC 2018; parr. 3.2 (sismica), 3.3/3.4 (vento/neve), cap. 5 (ponti); Circolare 21/1/2019 n. 7"
version: 0.1.0-alpha
status: alpha
tags:
  - carichi-permanenti
  - sovraccarichi-variabili
  - ntc-2018
  - categorie-uso
  - analisi-dei-carichi
---

# Carichi permanenti e sovraccarichi variabili per categoria d'uso (NTC 2018 par. 3.1)

## Quando usare questa skill

Usala quando un **progettista strutturale** deve **inquadrare** i **carichi permanenti** e i
**sovraccarichi variabili** (analisi dei carichi) per la **categoria d'uso** delle costruzioni civili e
industriali secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 3.1**:

- **pesi propri** dei materiali strutturali (Tab. 3.1.I) (§3.1.2);
- **carichi permanenti non strutturali** e il carico equivalente **g2** dei divisori (§3.1.3);
- **sovraccarichi** qk/Qk/Hk per categoria d'uso (Tab. 3.1.II) (§3.1.4);
- **riduzioni** dei sovraccarichi (area di influenza, numero di piani) e verifiche locali (§3.1.4.1-3).

**Non è** uno strumento che calcola i carichi di progetto o combina le azioni: è un **supporto
documentale** che fornisce i valori tabellari, il carico equivalente dei divisori e i coefficienti di
riduzione.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-sovraccarichi-categoria` | Sovraccarichi qk/Qk/Hk per categoria d'uso (Tab. 3.1.II) e verifiche locali (§3.1.4) |
| `inquadra-permanenti-riduzioni` | Pesi propri (Tab. 3.1.I), carico equivalente g2 dei divisori e riduzioni α_A/α_n (§3.1.2, 3.1.3, 3.1.4.1) |

## Punti chiave (verificati sul testo)

- **Pesi propri G1** (§3.1.2): dalla **Tab. 3.1.I** (c.a. **25,0 kN/m³**, acciaio **78,5**, laterizio
  18,0, legno 4,0÷8,0, ecc.).
- **Divisori g2** (§3.1.3): carico equivalente distribuito in funzione del peso lineare **G2**
  (≤1,00→0,40; 1-2→0,80; 2-3→1,20; 3-4→1,60; 4-5→2,00 kN/m²); **G2 > 5,00 kN/m** → posizionamento
  effettivo.
- **Sovraccarichi** (§3.1.4, **Tab. 3.1.II**): A residenziale **2,00**; B1/B2 uffici **2,00/3,00**;
  C1-C5 affollamento **3,00-5,00**; D1/D2 commerciale **4,00/5,00**; E1 magazzini **≥6,00**; F rimesse
  **2,50**; G **≥5,00**; H coperture **0,50**; scale/balconi **4,00** (o ≥4,00 secondo categoria); E2/K e
  carichi atipici **caso per caso**.
- **Riduzioni** (§3.1.4.1): **α_A = (5/7)·ψ0 + 10/A ≤ 1,0** (cat. A,B,C,D,H,I; per C,D **≥0,6**);
  **α_n = (2 + (n−2)·ψ0)/n** (cat. A÷D, edifici > 2 piani); **non combinabili**.
- **Verifiche locali**: **Qk** concentrati (impronta 50×50 mm; F 100×100 a 1,80 m; G 200×200 a 1,80 m) e
  **Hk** orizzontali (a **1,20 m** dal calpestio, parapetti al bordo superiore) - **non** contemporanei/
  combinati con le verifiche d'insieme (§3.1.4.2-3).

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 3.1** - testo del Supplemento Ordinario n. 8 alla G.U. n.
  42 del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e
  trascritto verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non calcola** i carichi di progetto né **combina** le azioni (skill `combinazioni-carico-ntc`);
  **non dimensiona** gli elementi.
- **Non tratta** i **carichi da ponte** (cap. 5), l'**azione sismica** (§3.2) né il **vento/neve**
  (§3.3/3.4, skill `carichi-atmosferici-ntc`).
- **Non riproduce** la **Tab. 2.5.I** (coefficienti ψ) né la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, né la lettura del par.
3.1 delle NTC 2018 e della Circolare applicativa.**
