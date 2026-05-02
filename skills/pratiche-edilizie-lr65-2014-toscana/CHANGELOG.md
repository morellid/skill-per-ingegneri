# CHANGELOG - pratiche-edilizie-lr65-2014-toscana

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-05-02 (rev 2 - post Codex adversarial review)

### Added
- SKILL.md: entry point con routing verso due sotto-attivita' (determina-tipo-pratica, checklist-documenti)
- AGENTS.md: convenzioni di dominio, articoli chiave DPR 380/2001 e LR 65/2014, anti-pattern
- tasks/determina-tipo-pratica.md: albero decisionale per CILA/SCIA/PdC con verifica zona sismica e vincoli
- tasks/checklist-documenti.md: checklist documenti per CILA, SCIA, PdC con documenti obbligatori e condizionali
- references/sources.yaml: LR 65/2014, DPR 380/2001, DPGR 64/R/2018, D.Lgs. 42/2004, DM 28/7/2021, NTC 2018, DM 37/2008
- references/estratti/lr-65-2014-titoli-abilitativi.md: sintesi dei titoli abilitativi e specificita' toscane
- references/estratti/dpr-380-2001-artt-zona-sismica.md: artt. 65, 83, 93, 94 DPR 380/2001 (zone sismiche)
- examples/cila-manutenzione-straordinaria/: rifacimento impianti senza struttura, Livorno zona 3, nessun vincolo
- examples/scia-ristrutturazione-strutturale/: ristrutturazione con muro portante, zona 3, vincolo paesaggistico
- agents/openai.yaml: metadata Codex (display_name, short_description, default_prompt)
- README.md: documentazione utente con installazione e limiti noti

### Fixed (post Codex adversarial review)
- Rimossi tutti i numeri di articolo specifici della LR 65/2014 dalle tabelle operative (SKILL.md, tasks): la numerazione non e' verificata sul testo consolidato vigente; aggiunta avvertenza critica esplicita
- Aggiunta avvertenza critica che la CILA e' solo per interventi NON strutturali; rimossa erronea voce "Comunicazione al Genio Civile" dalla checklist CILA (se ci sono parti strutturali il titolo e' SCIA)
- Corretta fonte sismica: sostituito DM 28/7/2021 con DGRT 421/2014 (Regione Toscana) come fonte corretta per la classificazione sismica in Toscana
- Aggiunto DPGR 1/R/2022 (procedura regionale toscana Genio Civile) in sources.yaml e nelle note
- Corretta fonte paesaggistica semplificata: sostituito "DPCM 13/9/2017" con DPR 13 febbraio 2017 n. 31
- Chiariti i tempi di inizio lavori per SCIA (distinzione SCIA ordinaria / SCIA in zona vincolata / SCIA alternativa al PdC)
- Rimossi esempi comunali di zone sismiche specifiche (Livorno, Castiglione della Pescaia) che non erano verificati; aggiunta nota di rinvio al portale Regione Toscana
- Aggiornato AGENTS.md con anti-pattern su classificazione sismica e numeri articoli LR 65/2014

### Note di sviluppo
- Skill non ancora validata da tecnico abilitato toscano o tecnico SUE
- La numerazione degli articoli della LR 65/2014 e' indicativa: verificare sul portale normativo regionale
- Non copre: sanatorie (usare skill modulistica-edilizia-unificata), recupero sottotetti LR 5/2010,
  varianti in corso d'opera, concessioni convenzionate
- Non integra le specificita' Salva Casa (DL 69/2024) per la Toscana: rinviare a skill modulistica-edilizia-unificata
- Classificazione sismica per Comune non embedata: va sempre verificata esternamente (INGV / Regione Toscana)
- Closes GitHub issue #8
