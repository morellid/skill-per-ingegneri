# Changelog - relazione-cam-dm-24-11-2025 (gia' relazione-cam-dm256-2022)

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.0-alpha] - 2026-07-12

### Aggiornamento normativo maggiore (closes #195)

**Trigger**: il DM MASE 24 novembre 2025 (GU n. 281 del 3/12/2025, in vigore dal 2/2/2026) ha abrogato e sostituito il DM 23/6/2022 n. 256 e il correttivo DM 5/8/2024 (art. 4). Skill rinominata da `relazione-cam-dm256-2022` a `relazione-cam-dm-24-11-2025`.

### Added
- Nuove fonti scaricate, hashate e trascritte (Regola zero):
  - GU n. 281/2025 con articolato DM 24/11/2025 SHA256: d7372a1e2e6e06c5418fcbfc5251dbd64f0b63e82216b15fbbb9366434aeecad -> `references/fonti/dm-cam-24-11-2025-articolato.md` (artt. 1-4 integrali + avvertenza)
  - Allegato 1 (PDF MASE, 123 pp.) SHA256: 24b50d2b277d55afb75b10564c80fbeedd82b0f0c29742775110c50622a6265c -> `references/fonti/dm-cam-24-11-2025-allegato-1.md` (criteri 2.1.1 e 3.1.1 integrali, par. 1.3.5, intestazioni capitoli con regole di applicabilita', elenco completo criteri)
  - Circolare MASE 10/4/2026 SHA256: ef651b7a38083e35ccdcf05492af9aa96dbc92daa39967dde17e83e1b837bff5 -> `references/fonti/circolare-mase-10-04-2026.md` (trascrizione parr. A-C)
  - Modello MASE Relazione CAM vers. 02/02/2026 SHA256: 405a928522ee75ce0f535070aa5d978f285fa2f0cb2fd05bb65f9396299c2d11 -> `references/fonti/modello-relazione-cam-2026.md`
- Nuovi estratti: `dm-cam-2025-ambito-transitorio.md` (entrata in vigore, ambito, transitorio art. 2 + circolare), `dm-cam-2025-relazione-cam-struttura.md` (criterio 2.1.1, modello MASE, applicabilita' per capitolo/criterio)

### Changed
- SKILL.md riscritto sul DM 24/11/2025: nuovo name/title/summary/normative_refs; routing e processo aggiornati (verifica del regime come primo passo)
- `tasks/identifica-criteri-applicabili.md`: eliminata la classificazione NC/R1/R2/MS (non esiste piu' nel nuovo DM); nuovo flusso regime -> tipologia ex art. 3 DPR 380/2001 -> applicabilita' per capitolo -> applicabilita' per criterio -> Tabella 1 del modello MASE
- `tasks/draft-relazione-cam.md`: riscritto sulla struttura del modello MASE (normativa/progetto/allegati, strategia ambientale con LCA e GWPtotal, Tabella 1, Scheda Tipo per criterio)
- `tasks/check-relazione-cam.md`: riscritto (verifica del regime, check strutturale contro il modello, criteri, ammissibilita' dei mezzi di prova con divieto "certificati CAM" ex par. 1.3.5)
- Esempi riscritti sul nuovo DM (conforme: appalto integrato nuova costruzione; non conforme: relazione generica con mezzo di prova vietato)
- Estratti e fonte del DM 256/2022 marcati [STORICO - REGIME TRANSITORIO], mantenuti per il transitorio art. 2
- `sources.yaml`: nuove fonti primarie con hash reali; voci DM 256/2022 marcate ABROGATO; `last_verified: 2026-07-12`
- AGENTS.md, README.md, agents/openai.yaml aggiornati

### Nota di conformita' (Regola zero)
Tutto il contenuto normativo e' stato riscritto dopo la lettura dei PDF scaricati; i requisiti prestazionali puntuali dei singoli criteri NON sono riprodotti nella skill (non trascritti): i task rinviano esplicitamente al testo integrale del criterio nel PDF ufficiale con segnaposto, senza inventare soglie.

## [0.1.2-alpha] - 2026-05-11

### Fixed
- fix(source-grounding): aggiunto `references/fonti/dm-256-2022-allegato.md` da lettura
  diretta del PDF (SHA256: 5b1dd184996add6ba529e360ac868a3a73023576feca5764a106d6e7f11e92a5);
  trascrizione fedele di tutti i paragrafi rilevanti (sezioni 2.2.1-2.7.4, 3.1-3.2, 4.1-4.3.8)
  con indicazione della pagina della GU n. 183 del 06/08/2022 (chiude #109)
- fix(sources.yaml): aggiunto campo `md_path: references/fonti/dm-256-2022-allegato.md`
  alla entry `dm-256-2022-allegato`
- fix(estratti/dm-256-2022-allegato-criteri-2x.md): corretto criterio 2.3.2
  (Permeabilita' della superficie territoriale): l'estratto riportava solo la definizione
  di superficie permeabile (deflusso < 0,50) omettendo la soglia minima del 60% di
  superficie territoriale permeabile richiesta per la NC; riscritta la voce con entrambe
  le informazioni e citazione del paragrafo/pagina GU

## [0.1.1-alpha] - 2026-05-01

### Fixed - Riscrittura completa contenuto normativo (criteri tutti errati)

Riscrittura integrale di tutti i file che contenevano numeri di criterio e struttura normativa,
basata sulla lettura diretta del PDF ufficiale dell'Allegato al DM 23/06/2022 n. 256
(SHA256: 5b1dd184996add6ba529e360ac868a3a73023576feca5764a106d6e7f11e92a5).

**Errori strutturali corretti:**

- La struttura originale (2.1 suolo, 2.2 durabilita', 2.3 materiali, 2.4 acqua, 2.5 energia,
  2.6 verde, 2.7 rifiuti, 2.8 cantiere, 2.9 ISO 14001) era completamente inventata e non
  corrispondeva ad alcuna sezione del DM 256/2022.
- La struttura reale del DM e' organizzata per tipo di affidamento:
  - Sezione 2 = criteri per servizio di PROGETTAZIONE (2.3-2.6 obbligatori, 2.7 premianti)
  - Sezione 3 = criteri per LAVORI (3.1 obbligatori, 3.2 premianti)
  - Sezione 4 = criteri per affidamento CONGIUNTO (4.1 rinvia a 2.3-2.6, 4.2 rinvia a 3.1, 4.3 premianti)
- I criteri obbligatori della sezione 2 sono: 2.3 (territoriali-urbanistici), 2.4 (edifici),
  2.5 (prodotti da costruzione), 2.6 (cantiere)

**Errori specifici corretti file per file:**

- `dm-256-2022-allegato-criteri-2x.md`: riscritto con criteri 2.3.x, 2.4.x, 2.5.x, 2.6.x corretti
- `dm-256-2022-allegato-criteri-premianti.md`: riscritto con 2.7.x, 3.2.x, 4.3.x corretti
- `dm-256-2022-articoli-chiave.md`: corretto entrata in vigore (centoventi giorni = 4/12/2022,
  non sessantesimo giorno); rimossi articoli inesistenti
- `dlgs-36-2023-art57.md`: rimossa soglia 100%/50% che era del D.Lgs. 50/2016 (abrogato),
  non dell'art. 57 D.Lgs. 36/2023
- `sources.yaml`: aggiornato con SHA256 PDF Allegato; corretta struttura DM nel campo notes;
  rimossa soglia percentuale errata; corretto URL PDF Allegato (bosettiegatti.eu)
- `tasks/identifica-criteri-applicabili.md`: riscritto con struttura criteri corretta;
  rimossa richiesta importo lavori per ISO 14001; aggiunto tipo affidamento
- `tasks/draft-relazione-cam.md`: riscritto con numeri criterio corretti (2.3.x/2.4.x/2.5.x/2.6.x);
  corretta data entrata in vigore; aggiunto riferimento a criterio 2.2.1 come base relazione
- `tasks/check-relazione-cam.md`: riscritto con numeri criterio corretti; rimossa richiesta
  importo lavori per criterio 2.9
- `examples/conforme-uffici-nuova-costruzione/input.md`: rimossa soglia comunitaria per ISO14001;
  corretto lana di roccia da 12% a 20% (>=15% obbligatorio); rimossa guaina bituminosa (criterio
  inesistente); gres cambiato a Decisione 2021/476 Ecolabel UE (non percentuale riciclato)
- `examples/conforme-uffici-nuova-costruzione/expected-output.md`: riscritto con criteri
  2.3.1-2.3.9, 2.4.1-2.4.14, 2.5.x, 2.6.x, premianti 3.2.1/4.3.3/4.3.6 corretti
- `examples/conforme-uffici-nuova-costruzione/note.md`: aggiornato con numeri criterio corretti
- `examples/non-conforme-criteri-mancanti/input.md`: rimossa soglia comunitaria; aggiunto tipo
  affidamento "solo lavori"
- `examples/non-conforme-criteri-mancanti/expected-output.md`: riscritto; aggiunta nota che 2.3.x
  non si applica a R1 retrofit energetico; criteri mancanti corretti (2.4.1/2.4.5/2.4.9/2.6.2)
- `examples/non-conforme-criteri-mancanti/note.md`: aggiornato con criteri mancanti corretti;
  aggiunta spiegazione 2.3.x non applicabili a R1; aggiunta nota differenza DM vecchio/nuovo

## [0.1.0-alpha] - 2026-05-01

### Added
- SKILL.md: entry point con routing ai 3 task, avvertenza vigenza normativa, limiti
- Task `identifica-criteri-applicabili.md`: classificazione NC/R1/R2/MS e tabella criteri applicabili
- Task `draft-relazione-cam.md`: guida dialogica per la redazione criterio per criterio
- Task `check-relazione-cam.md`: verifica completezza e conformita' al DM 256/2022
- `references/sources.yaml`: 3 fonti (DM 256/2022, Allegato, D.Lgs. 36/2023 art. 57)
- Estratti testuali: criteri di base, criteri premianti, artt. chiave DM, art. 57
- Esempio conforme: nuova costruzione uffici (tutti criteri applicabili NC)
- Esempio non conforme: ristrutturazione R1 con relazione lacunosa (criteri mancanti e generici)
- README.md, AGENTS.md, agents/openai.yaml

### Known issues / TODO v0.2
- SHA256 decreto principale non popolato (GU download restituisce HTML, non PDF)
- Aggiungere esempio MS (manutenzione straordinaria)
- Validazione Livello 2 da effettuare con professionista esperto appalti PA
