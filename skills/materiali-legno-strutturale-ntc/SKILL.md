---
name: materiali-legno-strutturale-ntc
description: "Supporto documentale al progettista strutturale e al Direttore dei Lavori per la qualificazione e le proprieta' dei materiali e prodotti a base di legno per uso strutturale secondo le NTC 2018 (DM 17 gennaio 2018), paragrafo 11.7. Aiuta a inquadrare: le generalita' del par. 11.7.1 (qualificazione secondo il par. 11.1 nei casi A marcatura CE, B qualificazione, C Linee Guida del Consiglio Superiore dei Lavori Pubblici; sistema di qualita' e rintracciabilita'; il Direttore dei Lavori rifiuta le forniture non conformi ed effettua i controlli di accettazione; laboratori art. 59 del DPR 380/2001 o notificati); le proprieta' dei materiali del par. 11.7.1.1 (valori caratteristici come frattile 5 per cento, prove di durata 300 secondi a 20 gradi e umidita' relativa 65 per cento; profilo resistente Tab. 11.7.I con fm,k, ft,0,k, fc,0,k, fv,k, E0,mean, E0,05, Gmean e massa volumica; coefficiente kh per il legno massiccio pari a min tra (150/h) elevato a 0,2 e 1,3, e per il legno lamellare min tra (600/h) elevato a 0,1 e 1,1); e i tipi di prodotto dei par. 11.7.2-11.7.6 (legno massiccio UNI EN 14081-1 con classi UNI EN 338; giunti a dita; legno lamellare incollato UNI EN 14080, con classi delle tavole superiori a C30 solo per classificazione a macchina; pannelli a base di legno UNI EN 13986) con l'accettazione in cantiere del par. 11.7.10. Use when a structural engineer or works supervisor must qualify structural timber products and frame their mechanical properties (resistance profile, kh) under the Italian NTC 2018 par. 11.7; it is a documentary aid, does NOT run the design verifications (fd = kmod fk/gamma_M), and does NOT replace the designer or the works supervisor. It is distinct from the timber design skill (par. 4.4), the seismic timber skill (par. 7.7) and the masonry/concrete/steel material skills (par. 11.10, 11.2, 11.3)."
license: MIT
area: strutture-geotecnica
title: "Legno strutturale: qualificazione materiali e proprieta' (NTC 2018 par. 11.7)"
summary: "Inquadra la qualificazione e le proprieta' del legno strutturale (NTC 2018 par. 11.7): generalita' e casi A/B/C (11.7.1), profilo resistente Tab. 11.7.I e kh (11.7.1.1), tipi di prodotto e norme CE UNI EN 14081/14080/13986/338 (11.7.2-11.7.6)."
normative_refs:
  - "NTC 2018 - par. 11.7: qualificazione casi A/B/C (11.7.1); profilo resistente Tab. 11.7.I e kh=min[(150/h)^0,2;1,3]/min[(600/h)^0,1;1,1] (11.7.1.1); UNI EN 14081/14080/13986/338 (11.7.2-11.7.6)"
  - "Rinvio (fuori scope): adesivi/collegamenti/durabilita' (11.7.7-11.7.9); verifiche par. 4.4, sismica par. 7.7, accettazione muratura/cls/acciaio par. 11.10/11.2/11.3 (skill dedicate)"
version: 0.1.0-alpha
status: alpha
tags:
  - legno-strutturale
  - materiali
  - ntc-2018
  - qualificazione
  - profilo-resistente
---

# Legno strutturale: qualificazione materiali e proprietà (NTC 2018 par. 11.7)

## Quando usare questa skill

Usala quando un **progettista strutturale** o un **Direttore dei Lavori** deve **qualificare** i materiali e
prodotti a base di legno per uso strutturale e **inquadrarne le proprietà** secondo le **NTC 2018** (DM 17 gennaio
2018), **paragrafo 11.7** (Cap. 11 «Materiali e prodotti per uso strutturale»):

- **generalità** e casi di qualificazione (§11.7.1);
- **proprietà dei materiali**, profilo resistente e coefficiente kh (§11.7.1.1);
- **tipi di prodotto** (massiccio, giunti a dita, lamellare, pannelli) e norme di riferimento (§11.7.2-11.7.6);
- **identificazione, qualificazione e accettazione** in cantiere (§11.7.10).

È un **supporto documentale**: inquadra la qualificazione e le proprietà; **non** esegue le verifiche di progetto
(fd = kmod·fk/γM). È **distinta** da `costruzioni-legno-ntc` (§4.4, progetto), `costruzioni-legno-zona-sismica-ntc`
(§7.7) e dalle skill materiali su `muratura-portante-materiali-ntc` (§11.10) e `controlli-accettazione-cls-acciaio-ntc`
(§11.2/§11.3).

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-proprieta-e-profilo-resistente` | Generalità/qualificazione (§11.7.1), valori caratteristici, profilo resistente Tab. 11.7.I e coefficiente kh (§11.7.1.1) |
| `qualifica-prodotti-e-accettazione` | Tipi di prodotto e norme di riferimento (§11.7.2-11.7.6) e accettazione in cantiere (§11.7.10) |

## Punti chiave (verificati sul testo/immagine)

- **Generalità** (§11.7.1): qualificazione secondo il §11.1 (**caso A** Marcatura CE / **B** qualificazione / **C**
  Linee Guida CSLP); sistema qualità e rintracciabilità; il **Direttore dei Lavori** rifiuta le forniture non
  conformi ed effettua i controlli di accettazione; laboratori **art. 59 DPR 380/2001** o notificati.
- **Proprietà** (§11.7.1.1): valori caratteristici = **frattile 5%**; prove **300 s** a **20 ± 2 °C** e **UR 65 ± 5%**;
  **profilo resistente** (Tab. 11.7.I: fm,k, ft,0,k, ft,90,k, fc,0,k, fc,90,k, fv,k; E0,mean, E0,05, E90,mean, Gmean;
  ρk, ρmean). **kh**: legno **massiccio** (150 mm) **kh = min[(150/h)^0,2 ; 1,3]** [11.7.1]; legno **lamellare** (600
  mm) **kh = min[(600/h)^0,1 ; 1,1]** [11.7.2].
- **Tipi di prodotto** (§11.7.2-11.7.6): legno massiccio **UNI EN 14081-1** + CE, classi **UNI EN 338**; giunti a
  dita (caso C); lamellare/massiccio incollato **UNI EN 14080** (classi tavole **> C30** solo classificazione a
  macchina); pannelli **UNI EN 13986** (valori UNI EN 12369); altri derivati (caso C).
- **Accettazione** (§11.7.10): identificazione/rintracciabilità e **controlli di accettazione in cantiere** a cura
  del Direttore dei Lavori, verificando la corrispondenza con quanto qualificato/marcato CE e indicato in progetto.

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 11.7** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e verificato
  sull'immagine delle pagine PDF 349-350 (Tab. 11.7.I, formule di kh, condizioni di prova).

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non esegue** le **verifiche di progetto** né calcola le **resistenze di progetto** (fd = kmod·fk/γM).
- **Non tratta** in dettaglio gli **adesivi** (§11.7.7), gli **elementi meccanici di collegamento** (§11.7.8) né la
  **durabilità** (§11.7.9).
- **Non tratta** il **progetto/verifiche** (§4.4, → skill `costruzioni-legno-ntc`), i requisiti **sismici** (§7.7, →
  skill `costruzioni-legno-zona-sismica-ntc`) né l'accettazione di **muratura/cls/acciaio** (§§11.10/11.2/11.3, →
  skill dedicate); **non** sostituisce il progettista né il Direttore dei Lavori.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, il Direttore dei Lavori né la lettura del par. 11.7 delle NTC 2018 e della relativa Circolare applicativa.**
