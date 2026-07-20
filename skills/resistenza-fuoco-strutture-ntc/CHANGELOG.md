# CHANGELOG - resistenza-fuoco-strutture-ntc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-20

### Added (closes #401)
- Prima versione della skill di supporto al **progettista strutturale** per l'**inquadramento della resistenza
  al fuoco delle strutture** secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 3.6.1 (Incendio)**,
  nell'area `strutture-geotecnica`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **NTC 2018 (DM 17 gennaio 2018)** - PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio
    2018 - SHA256: dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46 (doppio download
    riproducibile, stessa fonte delle altre skill NTC del repo).
  - Par. 3.6.1 estratto con `pdftotext -layout` (pp. 62-64) e trascritto verbatim in
    `references/fonti/ntc2018-par-3-6-1.md` (Tab. 3.5.IV, formule [3.6.1]-[3.6.4]).
- Estratto operativo `references/estratti/resistenza-fuoco-checklist.md`.
- Due task: `inquadra-prestazioni-classi-fuoco.md` e `inquadra-analisi-verifica-fuoco.md`.
- Due esempi: temperatura dei gas con la curva nominale standard a t=30/60 min per una classe R60;
  associazione obiettivo → livello di prestazione II e classe per un'attività soggetta a VVF.

### Contenuto ancorato al testo
- Definizioni (§3.6.1.1): capacità portante (R), tenuta (E), isolamento (I); resistenza al fuoco;
  compartimento; carico d'incendio specifico di progetto qf,d = qf·δq1·δq2·δn [3.6.1] con δq1 ≥ 1,00, δq2 ≥
  0,80 e δn ≥ 0,20 (dettaglio dei fattori nel DM 9 marzo 2007). Richieste di prestazione (§3.6.1.2, Tab.
  3.5.IV): Livelli I-V; per attività VVF classi da D.Lgs 139/2006. Classi di resistenza al fuoco (§3.6.1.3):
  15, 20, 30, 45, 60, 90, 120, 180, 240, 360 minuti. Procedura di analisi (§3.6.1.5): incendio di progetto con
  curva nominale/naturale, curva nominale standard θg = 20 + 345·log10(8t+1) [3.6.2], curva idrocarburi
  [3.6.3], curva esterna [3.6.4]; evoluzione della temperatura (§3.6.1.5.2); comportamento meccanico in
  combinazione eccezionale (§3.6.1.5.3); verifiche di sicurezza sul tempo pari alla classe (§3.6.1.5.4).

### Scope e limiti
- Non calcola il carico d'incendio (i fattori δni sono nel DM 9/3/2007) né esegue le analisi termiche/meccaniche,
  non fornisce le proprietà dei materiali ad alta temperatura (Eurocodici parte 1-2), non stabilisce le
  classi/livelli specifici delle regole tecniche VVF (D.Lgs 139/2006, DM 3/8/2015), non tratta i procedimenti
  antincendio (DPR 151/2011), non riproduce la Circolare 21/1/2019 n. 7. Non sostituisce il progettista né il
  professionista antincendio.

### Note di sviluppo
- Distinta da `prevenzione-incendi-attivita-procedimenti-dpr151` (procedimenti VVF); condivide la fonte GU con
  le altre skill NTC. Validazione Livello 2 con ingegnere strutturista/professionista antincendio.
