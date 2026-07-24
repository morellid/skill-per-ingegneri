# CHANGELOG - costruzioni-legno-zona-sismica-ntc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-24

### Added (closes #456)
- Prima versione della skill di supporto al **progettista strutturale** per l'**inquadramento delle regole
  generali** delle **costruzioni di legno in zona sismica** secondo le **NTC 2018** (DM 17 gennaio 2018),
  **paragrafo 7.7**, nell'area `strutture-geotecnica`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **NTC 2018 (DM 17 gennaio 2018)** - PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio
    2018 - SHA256 dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46 (doppio download
    riproducibile, stessa fonte delle altre skill NTC del repo).
  - Par. 7.7 (pagine PDF 258-260) estratto con `pdftotext -layout` e verificato sull'immagine (`pdftoppm -r
    150 -png`) per gli spessori dei pannelli, i rapporti di duttilità, i mezzi di unione e i coefficienti;
    trascritto verbatim in `references/fonti/ntc2018-par-7-7.md`.
- Estratto operativo `references/estratti/legno-sismica-checklist.md`.
- Due task: `inquadra-comportamento-materiali-fattore-q.md` e `verifica-requisiti-duttilita-dettagli.md`.
- Due esempi: requisiti dei materiali/pannelli e comportamento dissipativo per una parete a telaio; requisiti di
  duttilità dei mezzi di unione di un collegamento legno-acciaio (Tab. non applicabile: regole §7.7.3.1).

### Contenuto ancorato al testo
- Aspetti concettuali (§7.7.1): comportamento dissipativo → CD"A"/CD"B" o non dissipativo (→ §4.4); zone
  dissipative nei collegamenti, membrature lignee elastiche; sovraresistenza ηRd (Tab. 7.2.I), comunque ≥ 1,3
  (CD"A") / ≥ 1,1 (CD"B"). Materiali (§7.7.2): rinvio §4.4; unioni incollate non dissipative; pannelli di
  rivestimento particelle ≥ 13 mm, compensato ≥ 9 mm, OSB ≥ 12 mm (coppia) / ≥ 15 mm (singoli); connettori
  §11.7.8. Fattori di comportamento (§7.7.3): q0 da Tab. 7.3.II, giustificato dal Progettista. Precisazioni
  (§7.7.3.1): ≥ 3 cicli, duttilità statica ≥ 4 (CD"B") / ≥ 6 (CD"A"), riduzione ≤ 20%; d ≤ 12 mm & membrature
  ≥ 10d; chiodi d ≤ 3,1 mm & rivestimento ≥ 4d; alternative 8d/3d → CD"B". Verifiche/dettagli (§§7.7.5-7.7.7):
  vincoli impalcato-pareti bilateri; giunti di carpenteria con coefficiente parziale aggiuntivo 1,3; RES §7.3.6.1
  con resistenza ridotta del 20%; perni/bulloni d > 16 mm non usati nei collegamenti legno-legno/legno-acciaio.

### Scope e limiti
- Non esegue le verifiche di resistenza/duttilità di elementi e collegamenti né calcola q0 numerico (Tab. 7.3.II);
  non progetta i collegamenti (§7.7.7); non tratta i requisiti statici (§4.4) né il fattore q generale (§7.3.1).
  Non sostituisce il progettista.

### Note di sviluppo
- Distinta da `costruzioni-legno-ntc` (§4.4, statica) e `fattore-comportamento-q-sismica-ntc` (§7.3.1).
  Condivide la fonte GU con le altre skill NTC. Validazione Livello 2 con ingegnere strutturista esperto di
  strutture di legno.
