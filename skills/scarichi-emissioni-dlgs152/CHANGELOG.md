# CHANGELOG - scarichi-emissioni-dlgs152

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-14

### Added (closes #64)
- Prima versione della skill di supporto documentale alle autorizzazioni
  ambientali singole (residuali rispetto ad AUA e AIA) per lo scarico di acque
  reflue industriali (art. 124) e per le emissioni in atmosfera degli
  stabilimenti (art. 269) del D.Lgs. 152/2006 (Testo Unico Ambientale).
- Fonte scaricata, hashata e letta (Regola zero):
  - D.Lgs. 3/4/2006 n. 152 - testo multivigente su Normattiva, pagina indice
    pinnata `!vig=2026-07-14` SHA256:
    af54f5e0c6fa3d0a6d3dc5cf6d33ece0be7969be086dd93a24980e11b053b9fe
    (riproducibile, doppio download; pattern della skill aua-dpr59-dossier).
    Articoli 124 (v. 3, autorizzazione allo scarico), 137 (sanzioni scarichi),
    269 (v. 7, autorizzazione alle emissioni) e 279 (sanzioni emissioni) letti
    via AJAX (caricaArticolo) e trascritti verbatim in
    `references/fonti/dlgs-152-2006.md`.
- Estratto operativo `references/estratti/scarichi-emissioni-checklist.md` con
  obbligo, autorita', durata/rinnovo, modifiche e sanzioni.
- Due task: `inquadra-autorizzazione.md` (quale autorizzazione, autorita',
  durata) e `checklist-domanda-rinnovo.md` (contenuti, termini, sanzioni).
- Due esempi: nuovo scarico industriale (art. 124) e nuovo stabilimento con
  emissioni (art. 269).

### Nota di source-grounding (#64)
La scheda #64 (merge AM.7 + AM.12) citava gli artt. 124 e 269 tramite link
`gazzettaufficiale` all'atto originario 2006. La skill e' source-grounded sul
**testo vigente del D.Lgs. 152/2006 letto da Normattiva** (fonte ufficiale, TUA
fortemente emendato), con la pagina indice pinnata a data di vigenza per hash
riproducibile e la trascrizione verbatim degli artt. 124, 137, 269, 279 (versioni
vigenti). I **valori limite** (Allegato 5 parte terza; Allegati I-V parte quinta)
e l'inquadramento **AUA/AIA** non sono riprodotti: il perimetro distingue cio'
che e' negli articoli (obbligo, autorita', durata, sanzioni) da cio' che richiede
la lettura degli allegati o la valutazione del caso.

### Note di sviluppo
- Testo multivigente: ad ogni aggiornamento ri-pinnare la URL Normattiva e
  rileggere gli articoli modificati (usare le versioni piu' alte: art. 124 v. 3,
  art. 269 v. 7 al 2026-07-14).
- Validazione Livello 2 da effettuare con consulente ambientale.
- Possibili estensioni future: raccordo esplicito con la skill aua-dpr59-dossier
  (AUA) e con l'AIA; trascrizione mirata delle tabelle dei valori limite.
