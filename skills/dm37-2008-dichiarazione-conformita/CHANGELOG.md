# CHANGELOG - dm37-2008-dichiarazione-conformita

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-05-02

### Added
- SKILL.md con routing verso 2 task files
- AGENTS.md con convenzioni di dominio, articoli chiave DM 37/2008
- Task `verifica-completezza-ddc.md`: verifica tutti i campi obbligatori del modello Allegato I
- Task `identifica-allegati-obbligatori.md`: determina allegati richiesti per categoria e soglie Art. 6
- `references/sources.yaml` con fonti DM 37/2008 (Normattiva + GU originale)
- `references/estratti/dm37-2008-artt-1-7-allegato-i.md`: estratto Art. 1, 5, 6, 7 e Allegato I
- Esempio conforme: impianto elettrico residenziale < 200 mq
- Esempio problematico: impianto elettrico commerciale > 200 mq senza schema impianto

### Note di sviluppo
- Skill non ancora validata da dominio terzo (Livello 2)
- Da considerare draft finche' non passa validazione (vedi methodology/validazione.md)
- Fonti: testo DM 37/2008 da Normattiva (testo consolidato vigente) e GU originale
