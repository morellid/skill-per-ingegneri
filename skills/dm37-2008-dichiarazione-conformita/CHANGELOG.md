# CHANGELOG - dm37-2008-dichiarazione-conformita

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.2-alpha] - 2026-05-10

### Aggiunto

- `secondary_sources_to_evaluate`: aggiunto DM 192/2022 (modifica DM 37/2008 per infrastrutture
  digitali cat. b) e Art. 5-bis) come fonte da leggere nella prossima versione della skill.
  Nota: numero e data del decreto non ancora verificati da fonte primaria letta; da confermare
  su Normattiva o GU prima di integrare contenuto nella skill.

## [0.1.1-alpha] - 2026-05-10

### fix(source-grounding)

- Scaricato PDF originale DM 37/2008 da MIMIT.gov.it (SHA256 verificato:
  86afc81c9e942c893052a8b2988f9f3b71fdc6f6779325dcae895fd694654fc1)
- Creato `references/fonti/dm37-2008-mimit.md` con trascrizione letterale dei paragrafi
  rilevanti (Art. 1, 2, 3, 4, 5, 6, 7, 8, 11, 15 e nota allegati)
- Riscritto `references/estratti/dm37-2008-artt-1-7-allegato-i.md` citando il MD di fonte;
  rimossa avvertenza "parafrasi operativa" e sostituita con citazioni precise
- Aggiornato `references/sources.yaml`: aggiunto id `dm37-2008-mimit` con SHA256 reale e
  md_path; rimossa fonte GU (URL non piu' funzionante); annotata Normattiva come HTML non
  scaricabile (sha256: null coerente con binary_path: null)

Correzioni semantiche agli estratti (discrepanze rispetto al testo reale del PDF):

- **CRITICO - Art. 5 co. 2 lett. a)**: soglia superficie unita' abitativa residenziale corretta
  da **200 mq a 400 mq** (il vecchio estratto aveva 200 mq - valore errato, da training data)
- **Art. 5 co. 2 lett. a)**: rimossa soglia "16 unita' immobiliari" per condomini - il testo dice
  "per tutte le utenze condominiali" senza soglia numerica
- **Art. 5 co. 2 lett. c)**: chiarita distinzione tra residenziale (400 mq) e
  non-residenziale/commerciale (200 mq); corretta struttura dei tre sottocasi (lett. a, c, d)
- **Art. 5 co. 2 lett. f)**: corretta cat. c) riscaldamento: nessuna soglia kW generica per
  portata termica; criteri sono canne fumarie collettive ramificate o >= 40.000 frigorie/ora
- **Art. 5 co. 2 cat. d) idrico-sanitario**: rimossi i falsi threshold (16 unita' abitative,
  1000 mq) che non compaiono nel testo originale 2008; chiarito che per cat. d) Art. 5 co. 2
  non elenca casi con obbligo di professionista
- **Art. 5 co. 2 lett. h) antincendio**: aggiunta corretta condizione: CPI, o >= 4 idranti,
  o >= 10 rilevatori (non "progetto sempre obbligatorio" senza condizioni)
- **Art. 4**: corretti i requisiti del responsabile tecnico; il vecchio estratto conflava opzione
  a) (laurea) con b) (diploma + 2 anni); ora le 4 opzioni sono correttamente separate
- **Allegato I**: aggiunta nota esplicita che Allegato I e II sono stati sostituiti dal Decreto
  19 maggio 2010 (non incluso nel PDF letto)

Correzioni ai task:

- `identifica-allegati-obbligatori.md`: tabelle soglie riscritte con i valori corretti
  tracciabili al PDF MIMIT; rimossa frase "verificare testo vigente" usata come placeholder
  per valori incerti; aggiunta citazione Art. 5 co. 2 per ogni categoria
- `verifica-completezza-ddc.md`: aggiornata nota sulle fonti e sui limiti della verifica

## [0.1.0-alpha] - 2026-05-02

### Added
- SKILL.md con routing verso 2 task files e 7 categorie impianti (a-g)
- AGENTS.md con convenzioni di dominio e articoli chiave DM 37/2008 corretti
- Task `verifica-completezza-ddc.md`: verifica tutti i campi obbligatori del modello Allegato I
- Task `identifica-allegati-obbligatori.md`: determina allegati richiesti per categoria e soglie Art. 5 (progetto da professionista) e Art. 7 (schema sempre necessario)
- `references/sources.yaml` con fonti DM 37/2008 (Normattiva + GU originale)
- `references/estratti/dm37-2008-artt-1-7-allegato-i.md`: parafasi operativa Art. 1, 3, 4, 5, 7 e struttura Allegato I
- Esempio conforme: impianto elettrico residenziale 85 mq, 3 kW, con schema impianto
- Esempio problematico: impianto elettrico ufficio 350 mq, 15 kW, senza progetto professionale

### Fixed (post adversarial review Codex)
- Corretti numeri articoli: progettazione e' Art. 5 (non Art. 6); abilitazioni sono Art. 3 e 4 (non Art. 5)
- Rimosso riferimento a "categoria h" inesistente: categorie sono a-g (Art. 1 DM 37/2008)
- Aggiunto obbligo schema elaborato tecnico in tutti i casi (non solo sopra-soglia)
- Aggiunta distinzione "progetto da professionista" (sopra soglia Art. 5) vs "schema del responsabile tecnico" (sotto soglia, ma sempre necessario)
- Corrette soglie per cat. e) gas: 50 kW (non 35 kW) - da verificare su Normattiva

### Note di sviluppo
- Skill non ancora validata da dominio terzo (Livello 2)
- Da considerare draft finche' non passa validazione (vedi methodology/validazione.md)
- Fonti: testo DM 37/2008 da Normattiva (testo consolidato vigente) e GU originale
- Soglie Art. 5 nell'estratto sono parafrasi operative: richiedono verifica su Normattiva prima di v1.0
