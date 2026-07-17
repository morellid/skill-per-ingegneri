# CHANGELOG - garanzie-appalti-pubblici-dlgs36

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-17

### Added (closes #298)
- Prima versione della skill di supporto all'inquadramento delle **garanzie negli
  appalti pubblici** (garanzia provvisoria e definitiva con coperture assicurative),
  ai sensi del **D.Lgs. 36/2023, artt. 106 e 117**, nell'area `appalti-opere-pubbliche`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.Lgs. 31/3/2023 n. 36** - indice Normattiva pinnato `!vig=2026-07-17`
    SHA256: 0e9a193836e379cb33cb6daf1a5a988c608eb9559d84b91a841d9ed9791a62af
    (codice 23G00044). Artt. 106 (v2, idGruppo 16), 117 (v1, idGruppo 18),
    flagTipoArticolo 2, via `caricaArticolo`.
  - Trascrizione verbatim in `references/fonti/dlgs-36-2023-artt-106-117.md`.
- Estratto operativo `references/estratti/garanzie-appalti-checklist.md`.
- Due task: `inquadra-garanzia-provvisoria.md` e `inquadra-garanzia-definitiva.md`.
- Due esempi: garanzia provvisoria con riduzioni cumulate (art. 106); garanzia
  definitiva con maggiorazione per ribasso e svincolo (art. 117).

### Contenuto ancorato al testo
- Art. 106 garanzia provvisoria: 2% (riducibile all'1%, incrementabile al 4%),
  cauzione/fideiussione, requisiti (rinuncia preventiva escussione + art. 1957 c.c. +
  operativita' 15 gg + efficacia >= 180 gg), copertura, riduzioni 30%/50%/10%/fino
  20% con cumulabilita', svincolo automatico (30 gg per i non aggiudicatari),
  esclusione progettazione/PSC/supporto RUP.
- Art. 117 garanzia definitiva: 10%, maggiorazione per ribasso > 10%/20%, oggetto e
  durata (collaudo/CRE), svincolo progressivo 80%, sostituzione con ritenuta,
  escussione, mancata costituzione, polizze CAR/RCT (massimale 5%, min 500k/max 5M),
  decennale postuma (20-40%), schemi tipo, RTI, esonero.

### Scope e limiti
- Non calcola gli importi del caso concreto, non redige fideiussioni/polizze ne' gli
  schemi tipo (DM), non valuta escussione/decadenza/contenzioso, non sostituisce la
  stazione appaltante, il RUP, il garante o l'operatore economico. Allegato II.13,
  schemi tipo (DM c. 12), art. 1957 c.c. e codice antimafia citati e non trascritti.

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del D.Lgs. 36/2023 pinnato
  (nuovo hash) e rileggere gli artt. 106, 117 (testo tra `(( ))`, es. correttivo
  D.Lgs. 209/2024).
- Validazione Livello 2 con esperto di contratti pubblici / RUP.
