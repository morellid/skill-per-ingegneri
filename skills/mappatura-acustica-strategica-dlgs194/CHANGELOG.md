# CHANGELOG - mappatura-acustica-strategica-dlgs194

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-14

### Added (closes #40)
- Prima versione della skill di supporto documentale agli obblighi di mappatura
  acustica strategica e piani d'azione contro il rumore ambientale (D.Lgs.
  194/2005, attuazione della direttiva 2002/49/CE).
- Fonte scaricata, hashata e letta (Regola zero):
  - D.Lgs. 19/8/2005 n. 194 - testo multivigente su Normattiva, pagina indice
    pinnata `!vig=2026-07-14` SHA256:
    02f5432f6230df6c97d71204746b4cc571c05c53da342f5920d83f86dfa88f98
    (riproducibile, doppio download; pattern della skill aua-dpr59-dossier).
    Articoli 1-11 letti via AJAX (caricaArticolo) e trascritti verbatim in
    `references/fonti/dlgs-194-2005.md`.
- Estratto operativo `references/estratti/mappatura-acustica-checklist.md` con
  soglie, soggetti, deliverable, scadenze quinquennali e sanzioni.
- Due task: `diagnosi-applicabilita.md` (soglie, soggetto, deliverable, scadenze)
  e `checklist-adempimenti.md` (completezza mappe/piani, informazione del pubblico).
- Due esempi: agglomerato di 150.000 abitanti (soggetto, con chiarimento sulla
  soglia 250k della sola prima tornata) e asse stradale con 2 milioni di
  veicoli/anno (sotto soglia, con rinvio alla L. 447/1995).

### Nota di source-grounding (#40)
La scheda citava il D.Lgs. 194/2005 (su bosettiegatti, host non ufficiale). La
skill e' source-grounded sul **testo vigente del D.Lgs. 194/2005 letto da
Normattiva** (fonte ufficiale), con la pagina indice pinnata a data di vigenza per
hash riproducibile e la trascrizione verbatim degli articoli 1-11. Gli allegati
tecnici 1-6 e i metodi comuni UE (CNOSSOS-EU, dir. (UE) 2015/996) sono citati come
riferimento, non riprodotti.

### Note di sviluppo
- Testo multivigente: ad ogni aggiornamento ri-pinnare la URL Normattiva e
  rileggere gli articoli modificati.
- Validazione Livello 2 da effettuare con tecnico acustico / ente competente.
- Possibili estensioni future: trascrizione mirata degli allegati (requisiti
  minimi di mappe e piani); raccordo con CNOSSOS-EU (dir. (UE) 2015/996);
  integrazione con la skill L. 447/1995.
