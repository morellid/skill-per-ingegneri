# CHANGELOG - atex-luoghi-lavoro-dlgs81

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-14

### Added (closes #57)
- Prima versione della skill di supporto documentale alla protezione dei
  lavoratori dai rischi da atmosfere esplosive (ATEX luoghi di lavoro, Titolo XI
  del D.Lgs. 81/2008, recepimento dir. 1999/92/CE).
- Fonte scaricata, hashata e letta (Regola zero):
  - D.Lgs. 9/4/2008 n. 81 - testo multivigente su Normattiva, pagina indice
    pinnata `!vig=2026-07-14` SHA256:
    0664b393a7d1debc136cc11ebf837b3eda18d5394d6573b8a9dd739094b493e2
    (riproducibile, doppio download; pattern della skill aua-dpr59-dossier).
    Articoli 287 (ambito), 288 (definizioni), 289 (prevenzione/protezione), 290
    (valutazione), 293 (zone), 294 (DPCE), 296 (verifiche) e 297 (sanzioni)
    letti via AJAX (caricaArticolo) e trascritti verbatim in
    `references/fonti/dlgs-81-2008.md`.
- Estratto operativo `references/estratti/atex-checklist.md` con ambito,
  obblighi, valutazione, zone, DPCE, verifiche e sanzioni.
- Due task: `applicabilita-e-obblighi.md` (applicabilita' e sequenza obblighi) e
  `checklist-dpce.md` (contenuti del DPCE e sanzioni).
- Due esempi: reparto con polveri combustibili (soggetto, zone 20/21/22) e
  deposito di esplosivi (escluso, art. 287 c. 3 lett. c).

### Nota di source-grounding (#57)
La scheda #57 (ME.2 ATEX) citava la direttiva prodotti 2014/34/UE (eur-lex,
bloccato in questo ambiente) e il D.Lgs. 81/08 Titolo XI. La skill e'
source-grounded sul **testo vigente del D.Lgs. 81/2008 Titolo XI letto da
Normattiva** (fonte ufficiale), che recepisce la dir. **1999/92/CE** relativa
alla **protezione dei lavoratori** dalle atmosfere esplosive. La **marcatura ATEX
degli apparecchi** (dir. prodotti 2014/34/UE) e' esplicitamente **fuori
perimetro**: il decreto vigente disciplina gli obblighi del datore di lavoro, non
la certificazione dei prodotti. Gli allegati XLIX (zone), L (prescrizioni minime)
e LI (segnaletica) e le norme tecniche (CEI EN 60079) sono citati, non riprodotti.

### Note di sviluppo
- Testo multivigente: ad ogni aggiornamento ri-pinnare la URL Normattiva e
  rileggere gli articoli modificati.
- Validazione Livello 2 da effettuare con RSPP/esperto di sicurezza di processo.
- Possibili estensioni future: raccordo con il DPR 462/2001 (skill
  verifiche-messa-a-terra-dpr462) e trascrizione mirata dell'allegato XLIX
  (criteri di classificazione delle zone).
