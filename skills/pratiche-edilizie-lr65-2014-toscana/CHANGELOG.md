# CHANGELOG - pratiche-edilizie-lr65-2014-toscana

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-05-02

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

### Note di sviluppo
- Skill non ancora validata da tecnico abilitato toscano o tecnico SUE
- La numerazione degli articoli della LR 65/2014 e' indicativa: verificare sul portale normativo regionale
- Non copre: sanatorie (usare skill modulistica-edilizia-unificata), recupero sottotetti LR 5/2010,
  varianti in corso d'opera, concessioni convenzionate
- Non integra le specificita' Salva Casa (DL 69/2024) per la Toscana: rinviare a skill modulistica-edilizia-unificata
- Classificazione sismica per Comune non embedata: va sempre verificata esternamente (INGV / Regione Toscana)
- Closes GitHub issue #8
