# Changelog - relazione-cam-dm256-2022

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
