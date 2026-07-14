# CHANGELOG - verifiche-messa-a-terra-dpr462

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-14

### Added (closes #59)
- Prima versione della skill di supporto documentale agli adempimenti del DPR
  462/2001 (denuncia e verifiche periodiche di impianti di messa a terra,
  protezione scariche atmosferiche e impianti in luoghi con pericolo di
  esplosione nei luoghi di lavoro).
- Fonte scaricata, hashata e letta (Regola zero):
  - D.P.R. 22/10/2001 n. 462 - testo multivigente su Normattiva, pagina indice
    pinnata `!vig=2026-07-14` SHA256:
    08a5a8c683081472f94f24a3f7fe63d57b904bbc8e011df28182d10f529c8810
    (riproducibile, doppio download; pattern della skill aua-dpr59-dossier).
    Articoli 1-10 letti via AJAX (caricaArticolo) e trascritti verbatim in
    `references/fonti/dpr-462-2001.md` (art. 7-bis in vigore dal 1-3-2020).
- Estratto operativo `references/estratti/verifiche-messa-a-terra-checklist.md`
  con la regola di periodicita' e la catena degli adempimenti.
- Due task: `diagnosi-adempimenti.md` (periodicita', soggetti, adempimenti per un
  impianto) e `checklist-adempimenti.md` (completezza degli adempimenti).
- Due esempi: impianto di messa a terra in ambiente a maggior rischio in caso di
  incendio (periodicita' biennale, non quinquennale) e impianto in luogo con
  pericolo di esplosione (artt. 5-6, omologazione ASL/ARPA).

### Nota di source-grounding (#59)
La scheda citava DPR 462/2001 (Normattiva) e le guide INAIL. La skill e'
source-grounded esclusivamente sul **testo vigente del DPR 462/2001 letto da
Normattiva** (fonte ufficiale), con la pagina indice pinnata a data di vigenza
per hash riproducibile e la trascrizione verbatim degli articoli. Le guide INAIL
e le norme tecniche UNI CEI (a pagamento) non sono riprodotte; l'aggiornamento
istituzionale ISPESL -> INAIL (DL 78/2010) e' segnalato nel testo.

### Note di sviluppo
- Testo multivigente: ad ogni aggiornamento ri-pinnare la URL Normattiva e
  rileggere gli articoli modificati.
- Validazione Livello 2 da effettuare con perito elettrotecnico / RSPP.
- Possibili estensioni future: tariffe (decreto ISPESL 7/7/2005, con
  trascrizione); coordinamento con D.Lgs. 81/2008; modulistica INAIL.
