# CHANGELOG - costruzioni-composte-acciaio-cls-ntc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-20

### Added (closes #392)
- Prima versione della skill di supporto al **progettista strutturale** per l'**inquadramento della
  progettazione delle costruzioni composte di acciaio-calcestruzzo** (travi con soletta collaborante,
  colonne composte; caso **non sismico**) secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 4.3**,
  nell'area `strutture-geotecnica`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **NTC 2018 (DM 17 gennaio 2018)** - PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20
    febbraio 2018 - SHA256:
    dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46 (doppio download riproducibile,
    stessa fonte delle altre skill NTC del repo).
  - Par. 4.3 estratto con `pdftotext -layout` (pp. 114-127) e trascritto verbatim in
    `references/fonti/ntc2018-par-4-3.md` (§4.3.1-4.3.5 con le formule [4.3.6]-[4.3.14]), con i simboli resi
    in modo corretto (γM, γC, γA, γS, γV, α, Ecm, ftk, fck).
- Estratto operativo `references/estratti/costruzioni-composte-checklist.md`.
- Due task: `inquadra-materiali-sezioni-composte.md` e `inquadra-connessione-taglio-composte.md`.
- Due esempi: coefficienti e metodo di calcolo del momento resistente per una trave composta S355/C25/30 di
  classe 2; resistenza di progetto di un piolo con testa (PRd,a/PRd,c, α, γV).

### Contenuto ancorato al testo
- Stati limite aggiuntivi della connessione acciaio-calcestruzzo (resistenza allo SLU, esercizio allo SLE) e
  fasi costruttive (§4.3.1). Analisi con la classificazione delle sezioni composte secondo lo schema
  dell'acciaio (§4.2.3, distribuzioni plastiche/elastiche per classi 1-2 ed elastiche per 3-4), l'armatura
  B450C in classe 1-2 con la condizione [4.3.1], l'omogeneizzazione per la viscosità e l'analisi fessurata
  (EJ1/EJ2), la larghezza collaborante bei = min(Le/8, bi) (§4.3.2). Resistenze di progetto fd = fk/γM
  [4.3.6] con γC = 1,5, γA = 1,05, γS = 1,15 e γV = 1,25 allo SLU (γM = 1 allo SLE e nelle situazioni
  eccezionali) e la classe del calcestruzzo tra C20/25 e C60/75 (§4.3.3). Travi con soletta collaborante con
  il momento resistente elastico (limiti fcd/fyd/fsd), plastico (compressione del calcestruzzo 0,85·fcd) ed
  elasto-plastico, la resistenza a taglio verticale affidata alla trave metallica, e il sistema di
  connessione a taglio con il grado di connessione K = N/Nf e la resistenza dei pioli con testa pari al
  minore fra PRd,a = 0,8·ftk·(π·d²/4)/γV [4.3.9] e PRd,c = 0,29·α·d²·√(fck·Ecm)/γV [4.3.10] (ftk ≤ 500 MPa,
  d tra 16 e 25 mm, α = 0,2·(hsc/d+1) per 3 ≤ hsc/d ≤ 4 e 1,0 per hsc/d > 4), con le riduzioni per lamiera
  grecata kl [4.3.13] e kt [4.3.14] (§4.3.4). Le colonne composte (§4.3.5).

### Scope e limiti
- Non calcola le resistenze né esegue le verifiche, non dimensiona la sezione né la connessione, non
  riproduce le figure/tabelle-immagine (Fig. 4.3.3/4.3.4, Tab. 4.3.II) né i materiali dei §11.2/11.3 né gli
  Eurocodici (UNI EN 1994), non tratta la progettazione sismica (§7.6), non riproduce la Circolare 21/1/2019
  n. 7. Non sostituisce il progettista strutturale.

### Note di sviluppo
- Completa la famiglia "costruzioni di X" con calcestruzzo (§4.1), acciaio (§4.2), legno (§4.4) e muratura
  (§4.5), con cui condivide la fonte GU. Validazione Livello 2 con ingegnere strutturista.
