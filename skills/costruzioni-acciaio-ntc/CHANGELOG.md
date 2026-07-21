# CHANGELOG - costruzioni-acciaio-ntc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-19

### Added (closes #384)
- Prima versione della skill di supporto al **progettista strutturale** per l'**inquadramento della
  progettazione delle costruzioni di acciaio** (caso **non sismico**) secondo le **NTC 2018** (DM 17
  gennaio 2018), **paragrafo 4.2**, nell'area `strutture-geotecnica`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **NTC 2018 (DM 17 gennaio 2018)** - PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20
    febbraio 2018 - SHA256:
    dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46 (doppio download riproducibile,
    stessa fonte delle altre skill NTC del repo).
  - Par. 4.2 estratto con `pdftotext -layout` (pp. 91-103) e trascritto verbatim in
    `references/fonti/ntc2018-par-4-2.md` (§4.2.1-4.2.4 con Tab. 4.2.I, 4.2.II, 4.2.VI, 4.2.VII, 4.2.IX),
    con i simboli resi in modo corretto (γM, σ, τ, χ, λ, λ̄, Φ, α).
- Estratto operativo `references/estratti/costruzioni-acciaio-checklist.md`.
- Due task: `inquadra-classe-sezione-resistenze-acciaio.md` e `inquadra-stabilita-analisi-acciaio.md`.
- Due esempi: materiale, classe e Mc,Rd per una trave inflessa in S275 (classe 1, metodo plastico);
  resistenza a trazione con fori (γM2) e stabilità di un'asta compressa (χ, λ̄, limiti 200/250).

### Contenuto ancorato al testo
- Materiali con i gradi da S235 a S460 e le tensioni caratteristiche fyk/ftk delle Tab. 4.2.I (profili a
  sezione aperta) e 4.2.II (sezione cava) (§4.2.1). Classificazione delle sezioni nelle classi 1 duttili
  (Cθ ≥ 3), 2 compatte (Cθ ≥ 1,5), 3 semi-compatte e 4 snelle con sezione efficace, i metodi di calcolo
  della capacità (elastico/plastico/elasto-plastico) e di analisi globale (Tab. 4.2.VI) e gli effetti del
  secondo ordine (α_cr ≥ 10 elastica / ≥ 15 plastica) e delle imperfezioni (§4.2.3). Verifiche agli stati
  limite ultimi con Rd = Rk/γM e la Tab. 4.2.VII (γM0 = 1,05 resistenza sezioni, γM1 = 1,05 stabilità /
  1,10 ponti, γM2 = 1,25 frattura sezioni tese forate), le resistenze di progetto a trazione (Npl,Rd =
  A·fyk/γM0, Nu,Rd = 0,9·Anet·ftk/γM2), compressione (Nc,Rd), flessione (Mc,Rd con Wpl/Wel/Weff per classe
  1-2/3/4) e taglio (Vc,Rd = Av·fyk/(√3·γM0)), le verifiche di stabilità delle membrature (aste compresse
  Nb,Rd = χ·A·fyk/γM1 con χ da [4.2.44] e snellezza normalizzata, instabilità trascurabile per λ̄ < 0,2 o
  NEd < 0,04·Ncr, snellezza limite 200 principali / 250 secondarie; travi inflesse con χLT e le curve αLT
  0,21/0,34/0,49/0,76) e lo stato limite di fatica (§4.2.4).

### Scope e limiti
- Non calcola le resistenze né esegue le verifiche, non dimensiona membrature e collegamenti, non riproduce
  le tabelle b/t di classificazione (Tab. 4.2.III-V) né le curve di instabilità (Tab. 4.2.VIII), che nel
  PDF sono figure e vanno lette sulla norma/EC3, non riproduce i materiali del §11.3.4 né gli Eurocodici
  (UNI EN 1993), non tratta la progettazione sismica (§7.5), non riproduce la Circolare 21/1/2019 n. 7. Non
  sostituisce il progettista strutturale.

### Note di sviluppo
- Completa la famiglia "costruzioni di X" con `costruzioni-muratura-ntc` (§4.5) e `costruzioni-legno-ntc`
  (§4.4), con cui condivide la fonte GU. Validazione Livello 2 con ingegnere strutturista.
