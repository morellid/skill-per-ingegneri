# CHANGELOG - costruzioni-calcestruzzo-ntc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-20

### Added (closes #390)
- Prima versione della skill di supporto al **progettista strutturale** per l'**inquadramento della
  progettazione delle costruzioni di calcestruzzo** (c.a., c.a.p., non armato; caso **non sismico**)
  secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 4.1**, nell'area `strutture-geotecnica`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **NTC 2018 (DM 17 gennaio 2018)** - PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20
    febbraio 2018 - SHA256:
    dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46 (doppio download riproducibile,
    stessa fonte delle altre skill NTC del repo).
  - Par. 4.1 estratto con `pdftotext -layout` (pp. 71-90) e trascritto verbatim in
    `references/fonti/ntc2018-par-4-1.md` (§4.1-4.1.2 con Tab. 4.1.I e le formule [4.1.3]-[4.1.17]), con i
    simboli resi in modo corretto (γc, γs, αcc, σc, σs, εc2, εcu).
- Estratto operativo `references/estratti/costruzioni-calcestruzzo-checklist.md`.
- Due task: `inquadra-resistenze-progetto-ca.md` e `inquadra-verifiche-slu-sle-ca.md`.
- Due esempi: resistenze di progetto e coefficienti per una trave C25/30 con acciaio B450C (fcd, fyd,
  diagramma con εc2/εcu); verifiche SLE di limitazione delle tensioni (0,60/0,45 fck, 0,8 fyk) e di
  fessurazione (w1/w2/w3).

### Contenuto ancorato al testo
- Classi di resistenza (Tab. 4.1.I, da C8/10 a C90/105) e metodi di analisi (elastica lineare, plastica,
  non lineare) con il limite dell'asse neutro x/d <= 0,45 per fck <= 50 MPa e <= 0,35 per fck > 50 MPa
  (§4.1, 4.1.1). Resistenze di progetto dei materiali: calcestruzzo a compressione fcd = αcc·fck/γc con
  αcc = 0,85 e γc = 1,5 (riducibile a 1,4 per produzione continuativa controllata con CoV <= 10%; ridotta a
  0,80·fcd per elementi piani gettati in opera con spessore < 50 mm) [4.1.3], a trazione fctd = fctk/γc
  [4.1.4], acciaio fyd = fyk/γs con γs = 1,15 sempre [4.1.5] (§4.1.2.1.1). Diagrammi di calcolo del
  calcestruzzo (parabola-rettangolo, triangolo-rettangolo, rettangolo/stress block; εc2 = 0,20%,
  εcu = 0,35% per classi <= C50/60) e del calcestruzzo confinato (§4.1.2.1.2). Stati limite di esercizio con
  la fessurazione (stati limite di decompressione, formazione e apertura delle fessure con i valori limite
  w1 = 0,2 mm, w2 = 0,3 mm, w3 = 0,4 mm secondo condizioni ambientali e sensibilità delle armature) e la
  limitazione delle tensioni (σc <= 0,60·fck in combinazione caratteristica [4.1.15], σc <= 0,45·fck in
  combinazione quasi permanente [4.1.16], σs <= 0,8·fyk [4.1.17]) (§4.1.2.2). Stati limite ultimi di
  pressoflessione, taglio (traliccio con 1 <= ctgθ <= 2,5 [4.1.25]), torsione [4.1.38] e punzonamento
  (§4.1.2.3).

### Scope e limiti
- Non calcola le resistenze né esegue le verifiche, non dimensiona né arma gli elementi, non riproduce le
  proprietà dei materiali (fck, fctk, fyk, moduli) dei §11.2/11.3 né gli Eurocodici (UNI EN 1992), non
  tratta la progettazione sismica (§7.4) né i calcestruzzi speciali (leggeri §4.1.12, fibrorinforzati
  §11.2.12), non riproduce la Circolare 21/1/2019 n. 7. Non sostituisce il progettista strutturale.

### Note di sviluppo
- Completa la famiglia "costruzioni di X" con acciaio (§4.2), legno (§4.4) e muratura (§4.5), con cui
  condivide la fonte GU. Complementare al code-driven `predimensionamento-flessione-ca-ntc`. Validazione
  Livello 2 con ingegnere strutturista.
