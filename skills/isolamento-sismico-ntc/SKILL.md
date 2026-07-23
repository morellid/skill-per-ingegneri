---
name: isolamento-sismico-ntc
description: "Supporto documentale al progettista strutturale per l'inquadramento delle costruzioni con isolamento e/o dissipazione sismica secondo le NTC 2018 (DM 17 gennaio 2018), paragrafo 7.10. Aiuta a inquadrare lo scopo e le strategie dell'isolamento sismico alla base (allungare il periodo fondamentale per portarlo nel campo delle minori accelerazioni, oppure limitare la massima forza orizzontale trasmessa, con eventuale dissipazione di energia); i requisiti generali (sovrastruttura e sottostruttura in campo sostanzialmente elastico con i particolari costruttivi delle costruzioni con accelerazione al suolo agS non superiore a 0,075g; affidabilita' superiore del sistema di isolamento; dispositivi conformi al par. 11.9); le indicazioni progettuali (ispezionabilita' e sostituibilita' dei dispositivi, ricentraggio, carico verticale sul singolo isolatore di compressione o al piu' nullo con trazione in modulo inferiore al minore tra due volte il modulo di taglio e 1 MPa negli elastomerici, diaframma rigido sopra e sotto il sistema di isolamento, spazio libero attorno alla sovrastruttura); la modellazione e l'analisi (sovrastruttura e sottostruttura elastiche lineari, sistema di isolamento visco-elastico lineare o non lineare, deformabilita' verticale se il rapporto tra rigidezza verticale e orizzontale equivalente e' inferiore a 800, condizioni per il modello lineare equivalente, esclusione dell'analisi statica non lineare, requisiti dell'analisi statica lineare con periodo equivalente compreso tra tre volte il periodo a base fissa e 3 secondi); e le verifiche agli stati limite (SLD della sovrastruttura con spostamenti d'interpiano inferiori ai due terzi dei limiti del par. 7.3.6.1, SLV con fattore di comportamento non superiore a 1,50 per gli edifici e pari a 1 per i ponti e coefficiente di sicurezza almeno 1,5 per le parti non dissipative, SLC con i dispositivi che sostengono senza rotture gli spostamenti allo SLC). Use when a structural designer must frame the design of base-isolated buildings or bridges (isolation and energy dissipation) under the Italian NTC 2018 par. 7.10; it is a documentary aid and does NOT run the analysis or checks, does NOT design or qualify the isolation devices (par. 11.9), and does NOT replace the designer or the 2019 Circular."
license: MIT
area: strutture-geotecnica
title: "Costruzioni con isolamento sismico (NTC 2018 par. 7.10)"
summary: "Inquadra il progetto delle costruzioni con isolamento sismico (NTC 2018 par. 7.10): scopo e strategie, requisiti, dispositivi (par. 11.9), modellazione e analisi (modello lineare equivalente, statica lineare, no push-over) e verifiche SLD/SLV/SLC (q<=1,50 edifici, q=1 ponti)."
normative_refs:
  - "NTC 2018 (D.M. 17 gennaio 2018) - par. 7.10.1-7.10.4: isolamento alla base (allungare il periodo o limitare la forza); sovra/sottostruttura in campo elastico; dispositivi conformi al par. 11.9"
  - "NTC 2018 - par. 7.10.5: modellazione/analisi; deformabilita' verticale se KV/Kesi<800; modello lineare equivalente; no push-over; statica lineare se Tis in [3*Tbf, 3s], KV>=800*Kesi, TV<0,1s"
  - "NTC 2018 - par. 7.10.6: verifiche; SLD sovrastruttura interpiano < 2/3 dei limiti par. 7.3.6.1; SLV q<=1,50 (edifici)/q=1 (ponti), coeff. sicurezza >=1,5; SLC dispositivi che sostengono d2"
version: 0.1.0-alpha
status: alpha
tags:
  - isolamento-sismico
  - dissipazione-energia
  - progettazione-sismica
  - isolatori
  - ntc-2018
---

# Costruzioni con isolamento sismico (NTC 2018 par. 7.10)

## Quando usare questa skill

Usala quando un **progettista strutturale** deve **inquadrare** il progetto di **edifici o ponti con isolamento
sismico alla base** (costruzioni nuove o adeguamento di esistenti) secondo le **NTC 2018** (DM 17 gennaio 2018),
**paragrafo 7.10**:

- **scopo, strategie e requisiti** dell'isolamento (§7.10.1-7.10.3);
- **indicazioni progettuali** e dispositivi (§7.10.4);
- **modellazione, analisi e verifiche** SLE/SLV/SLC (§7.10.5-7.10.6).

**Non è** uno strumento che esegue l'analisi/verifiche o progetta i dispositivi: è un **supporto documentale** che
inquadra il framework. La qualificazione e le prove dei dispositivi sono trattate al **§11.9** (fuori scope).
Complementa `spettro-risposta-ntc` (§3.2), `combinazione-componenti-sismiche-ntc` (§7.3.5),
`fattore-comportamento-q-sismica-ntc` (§7.2.2-7.3.1) e `spostamenti-interpiano-sld-ntc` (§7.3.6.1).

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-scopo-requisiti-dispositivi` | Scopo e strategie, requisiti generali (campo elastico, agS≤0,075g, §11.9) e indicazioni progettuali dei dispositivi (V≥0, diaframma rigido) (§7.10.1-7.10.4) |
| `inquadra-modellazione-analisi-verifiche` | Modellazione, condizioni del modello lineare equivalente, applicabilità dell'analisi statica/dinamica lineare e verifiche SLD/SLV/SLC (§7.10.5-7.10.8) |

## Punti chiave (verificati sul testo/immagine)

- **Scopo** (§7.10.1): isolamento **sotto la costruzione**; (a) **allungare il periodo** (minori accelerazioni),
  (b) **limitare la forza** orizzontale; eventuale **dissipazione**.
- **Requisiti** (§7.10.2-7.10.3): sovra/sottostruttura in **campo sostanzialmente elastico** (particolari come per
  **agS ≤ 0,075g**); **affidabilità superiore** del sistema; dispositivi **conformi al §11.9**.
- **Indicazioni progettuali** (§7.10.4): ispezionabilità/sostituibilità e ricentraggio; **V ≥ 0** (se V<0, trazione
  **< min(2G, 1 MPa)** elastomerici); **diaframma rigido sopra e sotto**; spazio libero attorno.
- **Modellazione/analisi** (§7.10.5): sovra/sottostruttura **elastiche lineari**; sistema **visco-elastico lineare
  o non lineare**; deformabilità verticale se **KV/Kesi < 800**; modello lineare equivalente se rigidezza **≥ 50%**,
  smorzamento **< 30%**, variazione forza-spostamento **< 10%**, incremento forza **≥ 2,5%** del peso; **no
  push-over**; **analisi statica lineare** se **Tis ∈ [3·Tbf, 3,0 s]**, **KV ≥ 800·Kesi**, **TV < 0,1 s**, no
  trazione (edifici **≤ 20 m e ≤ 5 piani**).
- **Verifiche** (§7.10.6): **SLD sovrastruttura** interpiano **< 2/3** dei limiti §7.3.6.1; **SLV** con **q ≤ 1,50**
  (edifici) / **q = 1** (ponti), parti non dissipative con **coeff. sicurezza ≥ 1,5**; **SLC** i dispositivi
  sostengono senza rotture gli **spostamenti d2** (azione SLC).

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 7.10** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42 del
  20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e trascritto verbatim;
  le soglie (800, 50%/30%/10%/2,5%, 3·Tbf, TV<0,1 s, q≤1,50, ≥1,5) verificate anche sull'immagine delle pagine.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non esegue** l'analisi né le verifiche; **non calcola** forze/spostamenti (formule [7.10.1]-[7.10.5]).
- **Non progetta** né qualifica i **dispositivi** di isolamento/dissipazione (§11.9).
- **Non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, né la lettura del par. 7.10 delle NTC 2018 e della Circolare applicativa.**
