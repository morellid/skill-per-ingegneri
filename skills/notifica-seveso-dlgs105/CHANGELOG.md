# CHANGELOG - notifica-seveso-dlgs105

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-14

### Added (closes #39)
- Prima versione della skill di supporto documentale agli obblighi degli
  stabilimenti a rischio di incidente rilevante (Seveso III, D.Lgs. 105/2015,
  attuazione della direttiva 2012/18/UE).
- Fonte scaricata, hashata e letta (Regola zero):
  - D.Lgs. 26/6/2015 n. 105 - testo multivigente su Normattiva, pagina indice
    pinnata `!vig=2026-07-14` SHA256:
    f117b2995baaace98640eff3e6cf59463875b19bf18646ce6f5b853184ca2406
    (riproducibile, doppio download; pattern della skill aua-dpr59-dossier).
    Articoli 2 (ambito), 3 (definizioni), 13 (notifica), 14 (PPIR/SGS), 15
    (rapporto di sicurezza) e 28 (sanzioni) letti via AJAX (caricaArticolo) e
    trascritti verbatim in `references/fonti/dlgs-105-2015.md`.
- Estratto operativo `references/estratti/notifica-seveso-checklist.md` con
  assoggettabilita', classificazione soglia inferiore/superiore, notifica,
  PPIR/SGS, RdS e sanzioni.
- Due task: `verifica-assoggettabilita.md` (assoggettabilita' e classificazione)
  e `checklist-adempimenti.md` (completezza degli adempimenti).
- Due esempi: deposito di soglia superiore soggetto (nuovo stabilimento) e
  officina sotto soglia (non soggetta).

### Nota di source-grounding (#39)
La scheda citava il D.Lgs. 105/2015 tramite `bosettiegatti` (host non ufficiale)
e ISPRA. La skill e' source-grounded sul **testo vigente del D.Lgs. 105/2015
letto da Normattiva** (fonte ufficiale), con la pagina indice pinnata a data di
vigenza per hash riproducibile e la trascrizione verbatim degli artt. 2, 3, 13,
14, 15, 28. Le **soglie** dell'allegato 1 e la **regola della sommatoria** (nota
4) non sono riprodotte (il perimetro distingue cio' che e' negli articoli -
obblighi, soggetti, termini, sanzioni - da cio' che richiede la lettura
dell'allegato 1 e della classificazione CLP, Reg. 1272/2008).

### Note di sviluppo
- Testo multivigente: ad ogni aggiornamento ri-pinnare la URL Normattiva e
  rileggere gli articoli modificati.
- Validazione Livello 2 da effettuare con esperto RIR / sicurezza di processo.
- Possibili estensioni future: trascrizione mirata dell'allegato 1 (soglie e
  sommatoria) e raccordo con l'istruttoria del RdS (art. 17) e la pianificazione
  territoriale (art. 22).
