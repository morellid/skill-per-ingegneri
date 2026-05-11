# CHANGELOG - valutazione-cem-srb-art-87-cce

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Fixed (source-grounding remediation)
- `references/fonti/dlgs-259-2003-cce-mimit.md`: creato con trascrizione dell'art. 87 commi 1-10
  e 3-bis letto tramite Normattiva (vigente 2014-01-01), corrispondente al contenuto del PDF MIMIT
  catalogato in sources.yaml (sha256: 476b36ff...). Aggiunto `md_path` in sources.yaml.
- `references/fonti/dpcm-8-7-2003-cem.md`: creato con trascrizione degli articoli 1-7 letti
  tramite endpoint HTML della Gazzetta Ufficiale (codice redazionale 03A09711, GU n. 199 del
  28/8/2003), corrispondente al PDF della GU catalogato in sources.yaml (sha256: 362144b3...).
  Le Tabelle 1, 2, 3 dell'Allegato B e le formule dell'Allegato C sono pubblicati come immagine
  nel PDF della GU e non sono riprodotti. Aggiunto `md_path` in sources.yaml.
- `references/fonti/legge-36-2001-quadro-cem.md`: creato con trascrizione degli articoli 1, 2,
  3, 4 c. 1 lett. a), 6 cc. 1-2 e 14 letti tramite Normattiva, corrispondente al PDF della GU n.
  55 del 7/3/2001 catalogato in sources.yaml (sha256: 7e705e7f...; il PDF della GU contiene il
  testo in forma di immagine non estraibile). Aggiunto `md_path` in sources.yaml.
- CI fix: le 3 violazioni "[skill/id] md_path mancante" del workflow source-grounding.yml
  (job validate-sources e check-md-fonti-present) risolte.

### Changed (post-review #86)
- `tasks/check-completezza-istanza.md`: chiarita la regola di pubblicizzazione dell'istanza (art. 87 c. 4) anche per il regime SCIA Modello B; allineata la terminologia "asseverazione" (SCIA, art. 19 L. 241/1990) vs. "documentazione tecnica firmata attestante" (regime ordinario, art. 87 c. 3); aggiunto item 9-bis sul catasto nazionale delle sorgenti elettromagnetiche.
- `examples/srb-lte-30w-conforme/expected-output.md`: stato dell'item co-siting da `OK (con caveat)` a `DA VERIFICARE` per coerenza con la grammatica della tabella; allineata la voce "asseverazione" Modello A.
- `AGENTS.md` di skill: documentata la scelta terminologica asseverazione vs. documentazione tecnica firmata.

### Da chiudere prima di v0.1.0 (uscita da alpha)
- Aggiungere nei task una nota strutturale sui regimi regionali speciali (DPCM art. 1 c. 5: regioni a statuto speciale e PA Trento/Bolzano; verifica leggi regionali per Sicilia, Sardegna, FVG, Valle d'Aosta).
- Distinguere nei task tra modifica sostanziale (riapre iter art. 87) e variazione non sostanziale (regime alleggerito secondo guida ARPA regionale).
- Verificare in validazione di Livello 2 la denominazione esatta della Guida CEI 211-7 per le SRB ("Guida CEI 211-7/E" vs. "Guida CEI 211-7 nelle Appendici dedicate alle SRB"): la norma e' a pagamento e non catalogabile in `references/sources.yaml`.
- Precisare in `tasks/mappa-iter-procedurale.md` il rapporto di lex specialis tra art. 87 c. 9 (90 gg) e disciplina generale SCIA dell'art. 19 L. 241/1990 (avvio attivita' immediato + controllo postumo 60 gg).
- `SKILL.md` riga 13: sostituire "consulente CEM ARPA-side" con "validatore ARPA" o "tecnico ARPA" (terminologia coerente con il resto del file).
- Eventuale rimozione dei `.gitkeep` orfani in `tasks/`, `examples/`, `references/estratti/` ora che le directory non sono piu' vuote (convenzione condivisa con altre skill: nessuna rimozione finche' la convenzione di repo non cambia).

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
