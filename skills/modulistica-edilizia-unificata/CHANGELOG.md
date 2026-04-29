# CHANGELOG - modulistica-edilizia-unificata

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Esempi aggiuntivi: ristrutturazione "pesante" con SCIA alternativa al PdC, intervento in zona vincolata paesaggistica con DPR 31/2017 All. B.
- Estensione con scheda specifica per **sanatoria a "doppia conformita' alleggerita"** (art. 36-bis) e differenze procedurali rispetto all'art. 36.
- Integrazione del **glossario opere di edilizia libera** (DM 2/3/2018) come tabella di lookup per le voci ricorrenti.

## [0.1.0-alpha] - 2026-04-29

### Added
- Prima versione alpha della skill Modulistica edilizia unificata + Salva Casa
- Task files: `determina-regime-edilizio.md`, `genera-elenco-allegati.md`, `verifica-salva-casa.md`
- Fonti normative consultate: DPR 380/2001 (Testo Unico Edilizia), D.Lgs. 222/2016 Tabella A sez. II Edilizia, DL 69/2024 conv. L. 105/2024 (Salva Casa), Modulistica unificata Conferenza Unificata 27/3/2025
- Estratti testuali strutturati: `dpr-380-2001-regimi-edilizi.md`, `dlgs-222-2016-tabella-a.md`, `dl-69-2024-salva-casa.md`, `modulistica-unificata-2025.md`
- Esempi: 1 caso CILA/SCIA borderline (manutenzione straordinaria con frazionamento) + 1 cambio destinazione d'uso post Salva Casa + 1 sanatoria semplificata art. 36-bis
- Documentazione dual-agent (Claude Code + OpenAI Codex)

### Note di sviluppo
- Skill non ancora validata da dominio terzo (Livello 1: autore-driven, fonti pubbliche).
- Da considerare draft finche' non passa validazione Livello 2 con un ingegnere edile / architetto / geometra esperto in pratiche edilizie post Salva Casa o un operatore SUE/SUAP comunale (vedi `methodology/validazione.md`). Validazione tipica prevista: 10 interventi reali, confronto modulo proposto vs scelta corretta dello sportello SUE.
- I PDF delle fonti (DPR 380/2001 consolidato, D.Lgs. 222/2016, DL 69/2024 conv., modulistica 2025) non sono stati scaricati automaticamente: i campi `sha256` in `sources.yaml` sono `null`. Per popolarli eseguire manualmente `scripts/fetch-sources.sh modulistica-edilizia-unificata` (richiede permessi di rete) e committare sources.yaml aggiornato.
- Issue di riferimento: GitHub issue #1 ([P1] CT.3 Modulistica edilizia unificata + Salva Casa DL 69/2024).
