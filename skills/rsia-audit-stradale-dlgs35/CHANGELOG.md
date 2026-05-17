# CHANGELOG - rsia-audit-stradale-dlgs35

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-05-15

### Added
- Prima versione alpha della skill, copertura delle quattro procedure del D.Lgs 35/2011 modificato dal D.Lgs 213/2021.
- `SKILL.md` con frontmatter dual-agent (Claude Code + Codex), descrizione, disclaimer, processo generale e rinvii a `tasks/`.
- Cinque task files: `check-ambito-applicazione.md`, `draft-viss.md`, `draft-rsa.md`, `draft-nsa.md`, `verifica-requisiti-controllore.md`.
- Fonti normative: `references/sources.yaml` (D.Lgs 35/2011, D.Lgs 213/2021, Dir. 2008/96/CE - tre fonti scaricate e verificate via SHA256; Dir. (UE) 2019/1936 come riferimento strutturale).
- Estratti testuali per articolo, comma e allegato in `references/estratti/dlgs-35-2011.md`, `references/estratti/dlgs-213-2021.md`, `references/estratti/dir-2008-96-ce.md`.
- Esempi: `01-rsa-pfte-conforme` (caso conforme: autostrada TEN-T 18 km, controllore qualificato, galleria correttamente esclusa) e `02-rsa-controllore-non-idoneo` (caso problematico: incompatibilita' del controllore per partecipazione pregressa alla progettazione preliminare, mancanza dei requisiti formali, regime transitorio non applicabile).
- `AGENTS.md` di skill con convenzioni di dominio (articoli chiave, anti-pattern: niente citazione del vecchio art. 5 o vecchio Allegato III sostituiti dal D.Lgs 213/2021).

### Note di sviluppo
- Skill non ancora validata da dominio terzo. Validazione di Livello 1 effettuata dall'autore (Claude Opus 4.7).
- Da considerare draft finche' non passa validazione di Livello 2 (vedi `methodology/validazione.md`).
- Validatore di Livello 2 da identificare: controllore della sicurezza stradale iscritto all'elenco MIMS.
- Direttiva (UE) 2019/1936 inserita come riferimento strutturale solo: i contenuti sostanziali sono applicati attraverso il D.Lgs 213/2021 di recepimento, che e' la fonte vincolante nell'ordinamento italiano.
