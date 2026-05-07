# CHANGELOG - valutazione-cem-srb-art-87-cce

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-05-07

### Added
- Prima versione alpha della skill di supporto alla pratica art. 87 D.Lgs. 259/2003 (autorizzazione SRB / impianti radioelettrici) + valutazione predittiva CEM ai limiti del DPCM 8/7/2003.
- Tre task: `check-completezza-istanza.md` (regime ordinario Modello A vs. SCIA Modello B per impianti <= 20 W), `mappa-iter-procedurale.md` (timeline 30/15/30/30/90/12 mesi), `checklist-relazione-cem.md` (conformita' CEI 211-7, Tabelle 1/2/3 Allegato B, mediazione 6 min, esposizioni multiple).
- Fonti normative catalogate (`references/sources.yaml`): D.Lgs. 259/2003 (testo MIMIT 2013-2014), DPCM 8/7/2003 (GU n. 199 del 28/8/2003), L. 36/2001 (riferimento strutturale).
- Estratti testuali (`references/estratti/`): art. 87 commi 1-10 + 3-bis; DPCM 8/7/2003 art. 1-7 + rinvio strutturale ad Allegati A, B, C.
- Esempi: 1 conforme (`srb-lte-30w-conforme`, regime ordinario Modello A) + 1 problematico (`srb-5g-bozza-incompleta`, regime SCIA con sei BLOCCANTI tipici).

### Limiti noti
- **Tabelle 1, 2, 3 Allegato B DPCM 8/7/2003 NON riprodotte testualmente**: pubblicate come immagine nella GU n. 199 del 28/8/2003 e non estraibili come testo dal PDF di GU. La skill rinvia strutturalmente alle righe di tabella applicabili e demanda al professionista firmatario la verifica numerica direttamente sulla GU o sulla versione consolidata di Normattiva.
- **Fonte MIMIT del D.Lgs. 259/2003 datata 2013-2014**: NON riflette modifiche post-2014 (in particolare D.L. 76/2020 conv. L. 120/2020 e D.Lgs. 8 novembre 2021 n. 207). Il testo dei task e degli esempi richiama puntualmente l'obbligo per l'utente di consultare il testo vigente su Normattiva prima del deposito.
- **Calcolo numerico CEM** non eseguito dalla skill (richiede software CEI 211-7 dell'utente).
- **Regimi speciali fuori scope v0.1**: GSM-R ferroviario (art. 87 c. 3-bis), impianti radar / esposizioni pulsate, esposizioni professionali dei lavoratori (D.Lgs. 81/2008 Titolo VIII Capo IV).

### Note di sviluppo
- Validazione di Livello 1 (validate.sh + adversarial review automatica) effettuata.
- Validazione di Livello 2 (ingegnere CEM diverso dall'autore) NON ancora effettuata. La skill resta `0.1.0-alpha` finche' non passa validazione Livello 2 (vedi `methodology/validazione.md`).
