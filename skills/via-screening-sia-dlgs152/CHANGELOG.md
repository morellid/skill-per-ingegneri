# CHANGELOG - via-screening-sia-dlgs152

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-14

### Added (closes #36)
- Prima versione della skill di supporto documentale alla VIA (Parte Seconda
  D.Lgs. 152/2006 + DM 30/03/2015), che unisce le fasi AM.5 (screening) e AM.6
  (SIA) della scheda #36.
- Fonti scaricate, hashate e lette (Regola zero):
  - D.Lgs. 152/2006 Parte Seconda - testo multivigente su Normattiva, pagina
    indice pinnata `!vig=2026-07-14` SHA256:
    af54f5e0c6fa3d0a6d3dc5cf6d33ece0be7969be086dd93a24980e11b053b9fe
    (riproducibile, doppio download; pattern della skill aua-dpr59-dossier).
    Testo di art. 19 (in vigore dal 17-12-2024), Allegato IV-bis, Allegato V,
    Allegato VII letto via AJAX (caricaArticolo) e trascritto verbatim in
    `references/fonti/dlgs-152-2006-via.md`.
  - DM 30/03/2015 (GU n. 84/2015) SHA256:
    a315fb08a203de3f5b4c0391f561d77e65bdfb9c7bb289ef9bc137a5807345e1
    (riproducibile) -> trascrizione di scopo e meccanismi di adeguamento
    regionale in `references/fonti/dm-30-03-2015-via.md`.
- Estratto operativo `references/estratti/via-screening-sia-checklist.md` con
  procedura, timeline, criteri (All. V) e checklist (All. IV-bis, All. VII).
- Due task: `screening-verifica-assoggettabilita.md` (procedura art. 19 +
  verifica Studio Preliminare Ambientale) e `checklist-sia.md` (12 punti All.
  VII).
- Due esempi: cronoprogramma dello screening per progetto di competenza
  regionale (termini art. 19 + adeguamento soglie DM 30/03/2015) e verifica di
  completezza di un SIA con individuazione dei contenuti obbligatori mancanti
  (alternative con alternativa zero; vulnerabilita' a incidenti/calamita').

### Nota di source-grounding (#36)
La scheda citava come fonti le "Indicazioni operative MASE" (va.mite.gov.it) e
gli allegati D.Lgs. 152/06 su bosettiegatti (host non ufficiale). La skill e'
invece source-grounded su:
- il testo vigente del D.Lgs. 152/2006 letto direttamente da **Normattiva**
  (fonte ufficiale), con la pagina indice pinnata a data di vigenza per hash
  riproducibile e la trascrizione verbatim degli articoli/allegati;
- il **DM 30/03/2015** scaricato dalla **Gazzetta Ufficiale** (host ufficiale).
Gli elenchi dei progetti con soglie (allegati II-bis e IV) non sono trascritti
integralmente: sono citati come riferimento.

### Note di sviluppo
- Il testo del D.Lgs. 152/2006 e' multivigente: l'art. 19 e' frequentemente
  modificato (versione corrente in vigore dal 17-12-2024). Ad ogni aggiornamento
  ri-pinnare la URL Normattiva e rileggere gli articoli modificati.
- Validazione Livello 2 da effettuare con esperto VIA / valutatore.
- Possibili estensioni future: elenchi dei progetti (all. II-bis/IV) con soglie;
  procedura di VIA (artt. 23-27) e PAUR (art. 27-bis); VAS.
