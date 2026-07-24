---
name: muratura-portante-materiali-ntc
description: "Supporto documentale al progettista strutturale e al Direttore dei Lavori per la qualificazione dei materiali e la determinazione dei parametri meccanici della muratura portante secondo le NTC 2018 (DM 17 gennaio 2018), paragrafo 11.10. Aiuta a inquadrare: gli elementi per muratura del par. 11.10.1 (conformita' alla serie UNI EN 771 e Marcatura CE; Tab. 11.10.I con Categoria I al sistema 2+ e Categoria II al sistema 4; gli elementi di Categoria I hanno probabilita' di insuccesso non oltre il 5 per cento; coefficiente di sicurezza gamma_M secondo la categoria, par. 4.5.6); le prove di accettazione del par. 11.10.1.1 (laboratorio di cui all'art. 59 del DPR 380/2001; un campione ogni 350 mc per la Categoria II e 650 mc per la Categoria I; n elementi con n non inferiore a 6; media almeno pari a fbm e f1 almeno 0,80 fbm, oppure f1 almeno pari a fbk); le malte del par. 11.10.2 (classe M con fm in N/mm2 dalla Tab. 11.10.II M2,5-M20; per la muratura portante non ammesse malte con fm inferiore a 2,5; a prestazione garantita, a composizione prescritta con Tab. 11.10.V, o prodotte in cantiere; accettazione con 3 provini 40x40x160 ogni 350 o 700 mc); e la determinazione dei parametri meccanici del par. 11.10.3 (resistenza a compressione fk sperimentale su n muretti oppure stimata dalle Tab. 11.10.VI e 11.10.VII con fbk pari a 0,8 fbm per elementi artificiali e 0,75 fbm per elementi naturali, valida per giunti di spessore 5-15 mm; resistenza caratteristica a taglio fvk0 dalla Tab. 11.10.VIII). Use when a structural engineer or works supervisor must qualify masonry materials and determine the mechanical parameters (fk, fvk0) under the Italian NTC 2018 par. 11.10; it is a documentary aid, does NOT run the design verifications (fd = fk/gamma_M), and does NOT replace the designer or the works supervisor. It is distinct from the masonry design skill (par. 4.5), the seismic masonry skill (par. 7.8.1) and the concrete/steel acceptance skill (par. 11.2 and 11.3)."
license: MIT
area: strutture-geotecnica
title: "Muratura portante: qualificazione materiali e parametri (NTC 2018 par. 11.10)"
summary: "Inquadra la qualificazione dei materiali e i parametri meccanici della muratura portante (NTC 2018 par. 11.10): elementi Cat. I/II e accettazione (11.10.1), malte classi M2,5-M20 (11.10.2), fk (Tab. 11.10.VI-VII, fbk=0,8/0,75 fbm) e fvk0 (Tab. 11.10.VIII) (11.10.3)."
normative_refs:
  - "NTC 2018 - par. 11.10: elementi Cat. I (2+)/II (4), accettazione 350/650 mc (11.10.1); malte M2,5-M20, fm>=2,5 (11.10.2); fk Tab. 11.10.VI-VII (fbk=0,8/0,75 fbm) e fvk0 Tab. 11.10.VIII (11.10.3)"
  - "Rinvio (fuori scope): resistenze di progetto fd=fk/gamma_M e verifiche par. 4.5; muratura sismica par. 7.8; accettazione cls/acciaio par. 11.2/11.3 (skill dedicate)"
version: 0.1.0-alpha
status: alpha
tags:
  - muratura-portante
  - materiali
  - ntc-2018
  - accettazione
  - prove-cantiere
---

# Muratura portante: qualificazione materiali e parametri (NTC 2018 par. 11.10)

## Quando usare questa skill

Usala quando un **progettista strutturale** o un **Direttore dei Lavori** deve **qualificare i materiali** della
muratura portante e **determinarne i parametri meccanici** secondo le **NTC 2018** (DM 17 gennaio 2018),
**paragrafo 11.10** (Cap. 11 «Materiali e prodotti per uso strutturale»):

- **elementi** per muratura e categorie I/II (§11.10.1);
- **prove di accettazione** in cantiere degli elementi (§11.10.1.1);
- **malte** (classi, tipi, prove) (§11.10.2);
- **determinazione dei parametri meccanici** fk e fvk0 (§11.10.3).

È un **supporto documentale**: inquadra la qualificazione e la stima dei parametri; **non** esegue le verifiche di
progetto (fd = fk/γM) né dimensiona la muratura. È **distinta** da `costruzioni-muratura-ntc` (§4.5, progetto/
verifiche), `costruzioni-muratura-zona-sismica-ntc` (§7.8.1) e `controlli-accettazione-cls-acciaio-ntc`
(§11.2/§11.3, cls e acciaio).

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-elementi-e-malte` | Elementi Cat. I/II e prove di accettazione (§11.10.1) e malte, classi e prove (§11.10.2) |
| `determina-fk-e-fvk0` | Determinazione di fk (sperimentale/stima, Tab. 11.10.VI-VII) e fvk0 (Tab. 11.10.VIII) (§11.10.3) |

## Punti chiave (verificati sul testo/immagine)

- **Elementi** (§11.10.1): conformi **UNI EN 771** + Marcatura CE; Tab. 11.10.I **Categoria I → 2+**, **Categoria
  II → 4**; Cat. I con **probabilità di insuccesso ≤ 5%**; γM secondo categoria (§4.5.6).
- **Accettazione elementi** (§11.10.1.1): laboratorio **art. 59 DPR 380/2001**; **1 campione ogni 350 m³** (Cat.
  II) / **650 m³** (Cat. I); **n ≥ 6**; **media ≥ fbm** [11.10.1] e **f1 ≥ 0,80·fbm** [11.10.2]; oppure **f1 ≥ fbk**.
- **Malte** (§11.10.2): classe **M** = fm in N/mm² (Tab. 11.10.II, M2,5-M20/Md); **non ammesse malte con fm < 2,5**;
  a prestazione garantita / a composizione prescritta (Tab. 11.10.V) / in cantiere; accettazione **3 provini
  40×40×160 ogni 350 m³** (o 700 m³ per prestazione garantita).
- **Parametri meccanici** (§11.10.3): fk **sperimentale** su **n muretti (n ≥ 6)** o **stimata** da **Tab.
  11.10.VI** (artificiali) / **VII** (naturali), con **fbk = 0,8·fbm** (artificiali) o **0,75·fbm** (naturali),
  validità **giunti 5-15 mm**, interpolazione lineare (no estrapolazione); **fvk0** da **Tab. 11.10.VIII**
  (laterizio 0,30/0,20/0,10; silicato di calcio e cls 0,20/0,15/0,10).

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 11.10** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e verificato
  sull'immagine delle pagine PDF 365-368 (Tab. 11.10.I/II/V/VI/VII/VIII e formule di accettazione).

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non esegue** le **verifiche di progetto** né calcola le **resistenze di progetto** (fd = fk/γM); non
  dimensiona la muratura.
- **Non tratta** la resistenza a taglio **fvk con tensioni normali** (§11.10.3.3) né i **moduli di elasticità**
  (§11.10.3.5).
- **Non tratta** il **progetto/verifiche** (§4.5, → skill `costruzioni-muratura-ntc`), i requisiti **sismici**
  (§7.8, → skill `costruzioni-muratura-zona-sismica-ntc`) né l'accettazione di **cls/acciaio** (§11.2/§11.3, →
  skill dedicata); **non** sostituisce il progettista né il Direttore dei Lavori.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, il Direttore dei Lavori né la lettura del par. 11.10 delle NTC 2018 e della relativa Circolare applicativa.**
