---
name: controlli-accettazione-cls-acciaio-ntc
description: "Supporto documentale al Direttore dei Lavori e al collaudatore per l'inquadramento dei controlli di accettazione in cantiere del calcestruzzo (paragrafi 11.2.4-11.2.5) e dell'acciaio da cemento armato (paragrafo 11.3.2.12) secondo le NTC 2018 (DM 17 gennaio 2018), Capitolo 11. Aiuta a inquadrare, per il calcestruzzo, il prelievo, la scelta fra controllo di tipo A e controllo di tipo B statistico e i criteri di accettazione della Tab. 11.2.I, con le prescrizioni comuni. Use when a site director or tester must frame the on-site acceptance controls of concrete and reinforcing steel under the Italian NTC 2018; it is a documentary aid and does NOT run the tests nor assess the strength (which belong to the art. 59 DPR 380/2001 laboratory), does NOT replace the site director or tester, and does NOT cover the factory/qualification controls (par. 11.3.2.10-11), the core drilling and in-situ strength (par. 11.2.6-11.2.7) nor the other materials."
license: MIT
area: strutture-geotecnica
title: "Controlli di accettazione in cantiere: cls e acciaio (NTC 2018)"
summary: "Inquadra i controlli di accettazione in cantiere del calcestruzzo (prelievo, tipo A/B, Tab. 11.2.I: Rcm28 >= Rck+3,5 / Rck+1,48s, Rc,min >= Rck-3,5) e dell'acciaio da c.a. (3 campioni ogni 30 t, Tab. 11.3.VII: fy 425-572 N/mm2) secondo le NTC 2018 par. 11.2.5 e 11.3.2.12."
normative_refs:
  - "NTC 2018 (D.M. 17 gennaio 2018) - par. 11.2.4-11.2.5 (prelievo, controllo tipo A/B, Tab. 11.2.I: Rcm28 >= Rck+3,5 o Rck+1,48s; Rc,min >= Rck-3,5; A <= 300 m3, B > 1500 m3)"
  - "NTC 2018 - par. 11.3.2.12 acciaio da c.a. (3 campioni/30 t, entro 30 gg, laboratorio art. 59 DPR 380/2001; Tab. 11.3.VII: fy 425-572 N/mm2, Agt, ft/fy, non conformita' 6->25 campioni)"
version: 0.1.0-alpha
status: alpha
tags:
  - controlli-accettazione
  - calcestruzzo
  - acciaio-cemento-armato
  - ntc-2018
  - direttore-lavori
---

# Controlli di accettazione in cantiere: calcestruzzo e acciaio (NTC 2018 Cap. 11)

## Quando usare questa skill

Usala quando un **Direttore dei Lavori** (o il **collaudatore**) deve **inquadrare i controlli di accettazione
in cantiere** dei materiali strutturali secondo le **NTC 2018** (DM 17 gennaio 2018), **Capitolo 11**:

- **calcestruzzo** (§11.2.4-11.2.5): prelievo, controllo di tipo A / tipo B, criteri di accettazione (Tab.
  11.2.I);
- **acciaio da cemento armato** (§11.3.2.12): numerosità dei campioni, valori di accettazione (Tab. 11.3.VII
  a/b), non conformità.

**Non è** uno strumento che esegue le prove o valuta la resistenza (compito del **laboratorio ex art. 59 DPR
380/2001**), né sostituisce il Direttore dei Lavori: è un **supporto documentale** che inquadra prelievi,
numero minimo e criteri. Copre il compito di cantiere/collaudo che le skill "costruzioni di X" (§4.1/4.2)
rinviano esplicitamente al §11.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-controllo-accettazione-calcestruzzo` | Prelievo (§11.2.4), tipo A/B e criteri di accettazione (Tab. 11.2.I) del calcestruzzo (§11.2.5) |
| `inquadra-accettazione-acciaio-ca` | Numerosità (3 campioni/30 t), valori di accettazione (Tab. 11.3.VII a/b) e non conformità dell'acciaio da c.a. (§11.3.2.12) |

## Punti chiave (verificati sul testo)

- **Prelievo cls** (§11.2.4): **2 provini**; resistenza di prelievo = **media**; non accettato se scarto tra i
  due **> 20%** del minore.
- **Tipo A** (§11.2.5.1): **≤ 300 m³**, **3 prelievi** (≤ 100 m³ ciascuno), ≥ 1 prelievo/giorno.
- **Tipo B** (§11.2.5.2): obbligatorio **> 1500 m³**; ≥ 1 controllo/1500 m³; **≥ 15 prelievi**; coeff. di
  variazione **≤ 0,3**.
- **Accettazione cls** (Tab. 11.2.I): tipo A **Rcm28 ≥ Rck + 3,5** e **Rc,min ≥ Rck − 3,5**; tipo B
  **Rcm28 ≥ Rck + 1,48·s** e **Rc,min ≥ Rck − 3,5**.
- **Acciaio da c.a.** (§11.3.2.12): controlli **entro 30 gg**, laboratorio ex art. 59 DPR 380/2001; **3
  campioni ogni 30 t** (stessa classe/stabilimento).
- **Accettazione acciaio** (Tab. 11.3.VII a/b): **fy 425-572 N/mm²**; **Agt ≥ 6,0%** (B450C) / **≥ 2,0%**
  (B450A); **1,13 ≤ ft/fy ≤ 1,37** (B450C) / **≥ 1,03** (B450A); piegamento senza cricche.
- **Non conformità acciaio**: ripetizione su **6 campioni** → estensione a **25 campioni** → inidoneità della
  partita.

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **Cap. 11** (§11.2.4-11.2.5, §11.3.2.12) - testo del Supplemento
  Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto
  con `pdftotext` e trascritto verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non esegue** le prove né **valuta** la resistenza: le prove spettano al **laboratorio ex art. 59 DPR
  380/2001**; **non sostituisce** il Direttore dei Lavori né il collaudatore.
- **Non copre** i **controlli in stabilimento/qualificazione** (§11.3.2.10-11), il **controllo della
  resistenza in opera / carotaggi** (§11.2.6-11.2.7), gli **aggregati**, l'**acciaio da carpenteria**
  (§11.3.4), il **legno** (§11.7) né la **muratura** (§11.10).

**La skill è un supporto documentale: non sostituisce il Direttore dei Lavori, il collaudatore o il laboratorio, né la lettura del Cap. 11 delle NTC 2018.**
