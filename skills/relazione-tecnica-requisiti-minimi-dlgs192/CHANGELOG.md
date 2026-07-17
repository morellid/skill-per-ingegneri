# CHANGELOG - relazione-tecnica-requisiti-minimi-dlgs192

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-17

### Added (closes #346)
- Prima versione della skill di supporto al **tecnico** (progettista, direttore dei lavori) per la
  **relazione tecnica di progetto attestante la rispondenza ai requisiti minimi energetici** (la
  "relazione ex legge 10"), ai sensi del **D.Lgs. 19 agosto 2005, n. 192, art. 8** (con l'art. 15
  cc. 1, 3, 4), nell'area `energia-incentivi`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.Lgs. 192/2005** - indice Normattiva pinnato `!vig=2026-07-17`
    SHA256: bfaa533634a0bcd106b0a5d52d07b1a6f841b7c85960a8de069eeef0c952741d
    (codice 005G0219). Artt. 8 (versione 5, idGruppo 1) e 15 (versione 4, idGruppo 3) via
    `caricaArticolo` (formato AKN).
  - Trascrizione verbatim in `references/fonti/dlgs-192-2005-art8-15.md` (art. 8 per intero; art. 15
    cc. 1, 3, 4).
- Estratto operativo `references/estratti/relazione-tecnica-checklist.md`.
- Due task: `inquadra-relazione-deposito.md` e `inquadra-asseverazione-sanzioni.md`.
- Due esempi: relazione per nuova costruzione con sistemi alternativi ed esclusione PdC 12 kW; fine
  lavori senza asseverazione (inefficacia, sanzione al DL, controlli del Comune).

### Contenuto ancorato al testo
- Relazione redatta dai progettisti e depositata dal proprietario in doppia copia con la DIA/titolo
  abilitativo, con esclusioni (PdC <= 15 kW; sostituzione generatore sotto soglia DM 37/2008) - art.
  8 c. 1; valutazione di fattibilità dei sistemi alternativi ad alta efficienza per nuove
  costruzioni/ristrutturazioni importanti - c. 1-bis; asseverazione di conformità e AQE del direttore
  dei lavori a fine lavori, pena l'inefficacia della fine lavori - c. 2; conservazione, accertamenti
  e ispezioni del Comune in corso d'opera o entro 5 anni - cc. 3-5; dichiarazione sostitutiva di atto
  notorio - art. 15 c. 1; sanzione professionista 700-4200 euro - c. 3; sanzione direttore dei lavori
  1000-6000 euro - c. 4.

### Scope e limiti
- Non redige la relazione né esegue i calcoli/verifiche (rinvio a `trasmittanza-termica-opache-dm2015`
  e al DM 26/6/2015), non riproduce gli schemi di relazione del decreto MiSE, non copre l'APE (art. 6,
  skill `attestato-prestazione-energetica-dlgs192`) né i commi 2 e 5-10 dell'art. 15. Non sostituisce
  il progettista/direttore dei lavori.

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del D.Lgs. 192/2005 pinnato (nuovo hash) e
  verificare le modifiche (es. D.Lgs. 48/2020) e l'evoluzione del decreto attuativo MiSE.
- Validazione Livello 2 con termotecnico / certificatore energetico.
