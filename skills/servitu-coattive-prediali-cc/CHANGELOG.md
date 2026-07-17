# CHANGELOG - servitu-coattive-prediali-cc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed
- Riformulazione dell'inquadramento per **centrare il ruolo dell'ingegnere/geometra/CTU** (area
  *CTU & ingegneria forense*): il fulcro e' il **compito tecnico** - verifica dell'interclusione,
  **localizzazione del tracciato** dell'accesso/conduttura coi criteri di legge e **base tecnica
  dell'indennita'**. Aggiornati `description`, `summary`, README e la riga del catalogo per
  esplicitare che la skill serve al tecnico e non da' consulenza legale. Contenuto normativo e
  fonte verbatim invariati.

## [0.1.0-alpha] - 2026-07-17

### Added (closes #321)
- Prima versione della skill di supporto documentale all'inquadramento delle servitù
  prediali coattive di interesse tecnico secondo il Codice civile (R.D. 262/1942), Libro
  III, Titolo VI.
- Fonte scaricata, hashata e letta (Regola zero):
  - Codice civile (R.D. 16/3/1942 n. 262) - testo su Normattiva, pagina indice pinnata
    `!vig=2026-07-17` SHA256:
    f817bc32707124081b048e6d34882a4256b7e107de3c4a018fcd83a936dce325
    (riproducibile, doppio download; codice redazionale 042U0262, stesso indice delle
    altre skill sul Codice civile). Articoli 1027 (nozione), 1031-1032 (costituzione),
    1033 (acquedotto coattivo), 1051-1053 e 1055 (passaggio coattivo e indennità), 1056
    (elettrodotto coattivo), 1057 (vie funicolari) letti via AJAX (caricaArticolo,
    idGruppo 125-131) e trascritti verbatim in
    `references/fonti/cc-servitu-coattive.md` (inclusa la nota Corte cost. 167/1999
    sull'art. 1052).
- Estratto operativo `references/estratti/servitu-coattive-checklist.md` con nozione,
  costituzione, passaggio coattivo (intercluso/non intercluso), indennità/cessazione,
  acquedotto ed elettrodotto coattivo.
- Due task: `inquadra-passaggio-coattivo.md` (presupposti, localizzazione, indennità,
  cessazione) e `inquadra-servitu-acque-elettrodotto.md` (acquedotto, elettrodotto, vie
  funicolari, costituzione).
- Due esempi: passaggio coattivo per fondo intercluso (artt. 1051-1053, 1055); acquedotto
  ed elettrodotto coattivo (artt. 1033, 1056, 1031-1032).

### Nota di source-grounding (#321)
La skill e' source-grounded sul **testo vigente del Codice civile letto da Normattiva**
(fonte ufficiale). Le **leggi speciali** richiamate "in conformità delle leggi in materia"
dagli artt. 1033/1056/1057 (T.U. acque R.D. 1775/1933, norme sugli elettrodotti) sono
**citate come rinvio e non riprodotte**. La **misura dell'indennità** (art. 1038,
richiamato dall'art. 1053) e' citata, non riprodotta. La servitù di elettrodotto
**amministrativa** (asservimento coattivo espropriativo, DPR 327/2001) e' esplicitamente
distinta e **fuori perimetro**.

### Note di sviluppo
- Testo multivigente: ad ogni aggiornamento ri-pinnare la URL Normattiva e rileggere gli
  articoli modificati.
- Validazione Livello 2 da effettuare con avvocato civilista/CTU.
- Possibili estensioni future: servitù volontarie (artt. 1058 ss.), estinzione delle
  servitù (artt. 1072 ss.) e raccordo con le distanze legali
  (`distanze-legali-costruzioni-cc`).
