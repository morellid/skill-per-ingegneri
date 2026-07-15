# CHANGELOG - fattibilita-idraulica-toscana-lr41

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-14

### Added (closes #49)
- Prima versione della skill di supporto documentale alla fattibilita' delle
  trasformazioni nelle aree a pericolosita' per alluvioni in Toscana (L.R.
  41/2018).
- Fonte scaricata, hashata e letta (Regola zero):
  - L.R. Toscana 24/7/2018 n. 41 - testo vigente sulla Raccolta Normativa del
    Consiglio regionale (pagina a testo completo, URL con `pr=idx,0;artic,1`)
    SHA256: 4b75a5008ccef7ce46ad99e3638fdb2d2a588372deedfc753e03f232713ca481
    (riproducibile, doppio download; stesso host della skill
    pratiche-edilizie-lr65-2014-toscana). Articoli 1, 2 (magnitudo idraulica
    h1/h2/h3, battente, aree a pericolosita', opere), 7, 8 (opere per il rischio
    R2), 10 (limitazioni), 11 (nuova costruzione), 12 (esistente), 23, 25 letti e
    trascritti verbatim in `references/fonti/lr-toscana-41-2018.md`.
- Estratto operativo `references/estratti/fattibilita-idraulica-checklist.md` con
  magnitudo, opere, limitazioni e condizioni per tipo di intervento.
- Due task: `verifica-fattibilita.md` (ammissibilita' e opere) e
  `checklist-interventi.md` (limitazioni e condizioni).
- Due esempi: nuova costruzione in area a pericolosita' frequente (magnitudo molto
  severa) e lotto non a pericolosita' (fuori ambito).

### Nota di source-grounding e correzione della scheda (#49)
La scheda #49 chiedeva "calcolo volumi compensativi e classi pericolosita' per
relazione invarianza idraulica" citando come fonte il **DPGR Toscana 5/R/2020**.
Verificando la fonte (scaricata e letta), il DPGR 5/R/2020 disciplina in realta'
il **deposito e il controllo delle indagini geologiche, idrauliche e sismiche**
(attuazione art. 104 l.r. 65/2014) e **non** la fattibilita'/invarianza idraulica.
La disciplina della **fattibilita' delle trasformazioni nelle aree a pericolosita'
per alluvioni** (classi di magnitudo idraulica, opere di messa in sicurezza,
condizioni per nuova costruzione ed esistente) e' invece nella **L.R. 41/2018**,
adottata qui come fonte corretta e source-grounded. Il **calcolo dei volumi
compensativi/di laminazione** e' definito dalle **DGR/allegati tecnici** e dal
progettista: non riprodotto (esula dal testo di legge letto).

### Note di sviluppo
- Fonte regionale: ad ogni aggiornamento riscaricare la pagina a testo completo
  (nuovo hash) e rileggere gli articoli modificati (l'art. 11 c. 1 e' gia' stato
  sostituito dalla l.r. 7/2020).
- Validazione Livello 2 da effettuare con geologo/ingegnere idraulico toscano.
- Possibili estensioni future: raccordo con il DPGR 5/R/2020 (indagini) e con le
  DGR sui criteri di determinazione del battente e dei volumi.
