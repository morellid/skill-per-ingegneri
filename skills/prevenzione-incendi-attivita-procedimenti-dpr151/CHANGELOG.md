# CHANGELOG - prevenzione-incendi-attivita-procedimenti-dpr151

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-16

### Added (closes #251)
- Prima versione della skill di supporto per stabilire se un'attivita' e' **soggetta ai
  controlli di prevenzione incendi** e in quale **categoria (A/B/C)** dell'Allegato I, e per
  impostare i **procedimenti VV.F.**, ai sensi del **D.P.R. 1 agosto 2011, n. 151**, nell'area
  `sicurezza-lavoro-cantieri`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.P.R. 1 agosto 2011, n. 151** - indice Normattiva pinnato `!vig=2026-07-16`
    SHA256: a254e20396c8b21a044979fc70fec7280421d5596418f99dc0a7acb37b23f0a6
    (codice 011G0193). Articoli e Allegato I via `caricaArticolo`.
  - Trascrizione verbatim in `references/fonti/dpr-151-2011.md`: art. 2 (attivita' soggette,
    categorie A/B/C), art. 3 (valutazione progetti B/C), art. 4 (SCIA e controlli, CPI), art.
    5 (rinnovo periodico), art. 6 (obblighi in esercizio), art. 7 (deroghe); Allegato I
    (intestazione/legenda + estratto rappresentativo).
- Estratto operativo `references/estratti/prevenzione-incendi-checklist.md`.
- Due task: `classifica-attivita-categoria.md` e `imposta-procedimento-vvf.md`.
- Due esempi: autorimessa (categoria e procedimento); rinnovo quinquennale e deroga.

### Contenuto ancorato al testo
- Categorie A/B/C (art. 2 + Allegato I); valutazione del progetto per B/C con pronuncia
  entro 60 gg (art. 3); SCIA prima dell'esercizio, visite tecniche entro 60 gg (anche a
  campione), conformazione entro 45 gg, CPI entro 15 gg per la categoria C (art. 4); rinnovo
  periodico ogni 5 anni, 10 per le attivita' 6/7/8/64/71/72/77 (art. 5); obblighi in
  esercizio (art. 6); deroga con parere del Comando entro 30 gg -> Direzione regionale (art. 7).

### Scope e limiti
- Non riproduce la classificazione puntuale di ogni attivita' (categoria A/B/C da leggere
  sull'Allegato I, tabella grafica). Non redige progetto/SCIA/asseverazioni, non riproduce le
  regole tecniche (DM 3/8/2015 - Codice di prevenzione incendi, RTV), non sostituisce il
  Comando VV.F. Complementare a `piano-emergenza-antincendio-dm2021`.

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del D.P.R. 151/2011 pinnato (nuovo
  hash) e verificare eventuali modifiche dell'Allegato I.
- Validazione Livello 2 con professionista antincendio / funzionario VV.F.
