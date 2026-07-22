# CHANGELOG - criteri-modellazione-sismica-ntc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-21

### Added (closes #423)
- Prima versione della skill di supporto al **progettista strutturale** per l'**inquadramento dei criteri di
  modellazione della struttura e dell'azione sismica** ai fini della progettazione sismica secondo le **NTC 2018**
  (DM 17 gennaio 2018), **paragrafo 7.2.6**, nell'area `strutture-geotecnica`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **NTC 2018 (DM 17 gennaio 2018)** - PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio
    2018 - SHA256: dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46 (doppio download
    riproducibile, stessa fonte delle altre skill NTC del repo).
  - Par. 7.2.6 estratto con `pdftotext -layout` (pp. GU 214-215) e trascritto verbatim in
    `references/fonti/ntc2018-par-7-2-6.md`.
- Estratto operativo `references/estratti/modellazione-checklist.md`.
- Due task: `inquadra-modellazione-struttura.md` e `inquadra-modellazione-azione-sismica.md`.
- Due esempi: rigidezza fessurata (sino al 50%) e orizzontamenti rigidi (soletta c.a. 50 mm) di un telaio in c.a.;
  eccentricità accidentale (>= 0,05 della dimensione media) di un edificio rettangolare 24 x 15 m.

### Contenuto ancorato al testo
- Modellazione della struttura (§7.2.6): modello tridimensionale (attenzione alle forze d'inerzia verticali su
  travi di grande luce/sbalzi); leggi costitutive elastiche per comportamento non dissipativo o dissipativo con
  q; rigidezza flessionale e a taglio di elementi in muratura, c.a. e acciaio-cls riducibile sino al 50% di
  quella dei corrispondenti elementi non fessurati; orizzontamenti infinitamente rigidi nel piano se in c.a.,
  oppure latero-cemento con soletta c.a. di almeno 40 mm, o mista con soletta c.a. di almeno 50 mm con connettori
  a taglio; elementi non strutturali non collaboranti (tamponature, tramezzi) rappresentati solo in termini di
  massa (rigidezza/resistenza solo se effetti negativi sulla sicurezza). Modellazione dell'azione sismica
  (§7.2.6): forze statiche equivalenti, spettri di risposta o storie temporali; con risposta sismica locale /
  interazione terreno-struttura lo spettro (5% di smorzamento) deve essere >= 70% di quello per sottosuolo A e la
  risultante di taglio/normale alla fondazione >= 70% di quella a base fissa; divieto di storie temporali
  artificiali per tali analisi (§3.2.3.6); eccentricità accidentale del centro di massa >= 0,05 volte la
  dimensione media dell'edificio misurata perpendicolarmente alla direzione dell'azione sismica, costante per
  entità e direzione su tutti gli orizzontamenti.

### Scope e limiti
- Non costruisce il modello ne' esegue l'analisi (metodi al §7.3), non determina q, non tratta la risposta
  sismica locale (§3.2.3.6) ne' le fondazioni miste (§6.4.3), non riproduce la Circolare 21/1/2019 n. 7. Non
  sostituisce il progettista.

### Note di sviluppo
- Complementa `regolarita-strutturale-sismica-ntc` (§7.2.1), `spostamenti-interpiano-sld-ntc` (§7.3.6.1),
  `periodo-proprio-t1-ntc` (§7.3.3.2) e `spettro-risposta-ntc` (§3.2), condividendo la stessa fonte GU.
  Validazione Livello 2 con ingegnere strutturista.
