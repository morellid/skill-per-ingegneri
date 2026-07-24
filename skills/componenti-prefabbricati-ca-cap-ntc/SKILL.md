---
name: componenti-prefabbricati-ca-cap-ntc
description: "Supporto documentale al progettista strutturale, al Direttore dei Lavori e ai produttori per la qualificazione, il controllo di produzione e l'accettazione dei componenti prefabbricati in c.a. e c.a.p. secondo le NTC 2018 (DM 17 gennaio 2018), paragrafo 11.8. Aiuta a inquadrare: le generalita' del par. 11.8.1 (processo industrializzato e sistema di controllo della produzione in stabilimento; per gli elementi qualificati ai punti A o C del par. 11.1 i requisiti procedurali del deposito ex art. 58 del DPR 380/2001 si considerano assolti; Metodi 1, 2 e 3 per la dichiarazione delle prestazioni); i requisiti degli stabilimenti del par. 11.8.2 (dosaggio a peso, sistema di controllo documentato); il controllo di produzione del par. 11.8.3 (sistema qualita' UNI EN ISO 9001; per il calcestruzzo controllo continuo secondo il par. 11.2 con apparecchiature tarate annualmente, registri conservati dieci anni, prove a 28 giorni, controllo di tipo B in stabilimento e di tipo A su 3 prelievi con almeno un prelievo ogni cinque giorni; per l'acciaio prova di piegatura su 3 campioni ogni 90 tonnellate e almeno una volta al mese, trazione su 3 campioni ogni 10 rotoli; marchiatura fissa e, per manufatti di peso oltre 8 kN, indicazione del peso); le procedure di qualificazione del par. 11.8.4 (Servizio Tecnico Centrale; serie dichiarata con attestato quinquennale, serie controllata con Certificato di Valutazione Tecnica quinquennale e prove a rottura su prototipo); e i documenti di accompagnamento del par. 11.8.5 (il Direttore dei Lavori rifiuta le forniture non conformi; certificato di origine, istruzioni di montaggio, verifica della marchiatura). Use when a structural engineer, works supervisor or precast producer must frame the qualification, factory production control and site acceptance of precast concrete/prestressed components under the Italian NTC 2018 par. 11.8; it is a documentary aid, does NOT design the components, and does NOT replace the designer or the works supervisor. It is distinct from the concrete/steel acceptance skill (par. 11.2/11.3) and the concrete design skill (par. 4.1)."
license: MIT
area: strutture-geotecnica
title: "Prefabbricati c.a./c.a.p.: qualificazione e accettazione (NTC 2018 par. 11.8)"
summary: "Inquadra qualificazione, controllo di produzione e accettazione dei prefabbricati in c.a./c.a.p. (NTC 2018 par. 11.8): metodi 1/2/3 (11.8.1), controllo cls/acciaio e marchiatura >8 kN (11.8.3), serie dichiarata/controllata quinquennale (11.8.4), documenti e accettazione (11.8.5)."
normative_refs:
  - "NTC 2018 - par. 11.8: metodi 1/2/3 (11.8.1); controllo produzione cls e acciaio, marchiatura >8 kN (11.8.3); serie dichiarata/controllata quinquennale (11.8.4); documenti e accettazione (11.8.5)"
  - "Rinvio (fuori scope): progetto/verifiche par. 4.1; accettazione generale cls/acciaio par. 11.2/11.3; denuncia/collaudo statico DPR 380 (skill dedicate)"
version: 0.1.0-alpha
status: alpha
tags:
  - prefabbricati
  - calcestruzzo
  - ntc-2018
  - qualificazione
  - accettazione
---

# Componenti prefabbricati c.a./c.a.p.: qualificazione e accettazione (NTC 2018 par. 11.8)

## Quando usare questa skill

Usala quando un **progettista strutturale**, un **Direttore dei Lavori** o un **produttore** deve inquadrare la
**qualificazione**, il **controllo di produzione** e l'**accettazione** dei componenti prefabbricati in c.a. e
c.a.p. secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 11.8** (Cap. 11):

- **generalità** e metodi di dichiarazione delle prestazioni (§11.8.1);
- **requisiti degli stabilimenti** (§11.8.2);
- **controllo di produzione** e sui materiali di serie, **marchiatura** (§11.8.3);
- **procedure di qualificazione** serie dichiarata/controllata (§11.8.4);
- **documenti di accompagnamento** e accettazione in cantiere (§11.8.5).

È un **supporto documentale**: inquadra qualificazione, controllo e accettazione; **non** esegue il progetto degli
elementi prefabbricati né le verifiche. È **distinta** da `controlli-accettazione-cls-acciaio-ntc` (§11.2/§11.3,
accettazione **generale** di cls/acciaio) e da `costruzioni-calcestruzzo-ntc` (§4.1, **progetto**).

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-qualificazione-e-controllo-produzione` | Generalità/metodi 1-2-3 (§11.8.1), requisiti stabilimenti (§11.8.2), controllo di produzione e materiali di serie (§11.8.3), procedure di qualificazione (§11.8.4) |
| `verifica-marchiatura-e-documenti-accettazione` | Marchiatura (§11.8.3.4) e documenti di accompagnamento/accettazione del Direttore dei Lavori (§11.8.5) |

## Punti chiave (verificati sul testo/immagine)

- **Generalità** (§11.8.1): processo industrializzato + controllo di produzione in stabilimento; per elementi
  qualificati ai **punti A/C del §11.1** deposito **art. 58 DPR 380/2001** assolto; **Metodi 1/2/3** di dichiarazione.
- **Controllo di produzione** (§11.8.3): sistema qualità **UNI EN ISO 9001**. **Cls**: controllo continuo (§11.2),
  apparecchiature **tarate annualmente**, registri **10 anni**, prove a **28 giorni**, resistenza caratteristica
  **controllo tipo B** in stabilimento, controlli esterni **≥ 1 prelievo/5 giorni** con **controllo tipo A** su
  **3 prelievi**. **Acciaio**: **piegatura 3 campioni/90 t** (min mensile, UNI EN ISO 15630-1), **trazione 3
  campioni/10 rotoli**; solo per prodotti **privi di marcatura CE**.
- **Marchiatura** (§11.8.3.4): **fissa/indelebile** per rintracciabilità; per manufatti **> 8 kN** indicare il **peso**.
- **Qualificazione** (§11.8.4): **STC** (art. 58 DPR 380); **serie dichiarata** (§4.1.10.2.1) → **attestato
  quinquennale**; **serie controllata** (§4.1.10.2.2) → **Certificato di Valutazione Tecnica quinquennale** + prove
  a rottura su prototipo; sospensioni/revoche.
- **Documenti** (§11.8.5): il **Direttore dei Lavori** rifiuta le forniture non conformi; istruzioni trasporto/
  montaggio, **certificato d'origine**, prove a compressione, verifica della **marchiatura** prima dell'accettazione.

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 11.8** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e verificato
  sull'immagine delle pagine PDF 355-357 (frequenze prove, registri, marchiatura, validità quinquennali).

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non esegue** il **progetto** degli elementi prefabbricati né le **verifiche** (serie dichiarata/controllata,
  §4.1.10).
- **Non tratta** i **controlli di accettazione generali** di cls/acciaio (§§11.2/11.3, → skill
  `controlli-accettazione-cls-acciaio-ntc`) né la **denuncia/collaudo statico** (DPR 380, → skill dedicata).
- **Non** sostituisce il progettista né il Direttore dei Lavori.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, il Direttore dei Lavori né la lettura del par. 11.8 delle NTC 2018 e della relativa Circolare applicativa.**
