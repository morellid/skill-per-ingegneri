# CHANGELOG - pfte-allegato-i7-checker

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Esempi dedicati al task di verifica coerenza PFTE/esecutivo (`coerenza-nuova-costruzione/`, `coerenza-scostamenti/`).
- Estensione integrazione bandi-tipo ANAC (catalog PR.2).

## [0.1.1] - 2026-05-10

### fix(source-grounding)
- Scaricati i PDF ufficiali della GU (D.Lgs. 36/2023 GU n. 87 SO n. 14 e GU n. 77 SO n. 12/L;
  D.Lgs. 209/2024 GU n. 17 SO n. 3) e verificati via pdftotext.
- Creata `references/fonti/dlgs-36-2023-allegato-i7.md` con trascrizione verbatim di:
  art. 41 (tutti i commi), Allegato I.7 artt. 1-7, 19-22 (testi rilevanti per gli elaborati).
- Creata `references/fonti/dlgs-209-2024-correttivo.md` con trascrizione verbatim di:
  art. 14 (modifiche art. 41) e art. 78 (modifiche Allegato I.7) del D.Lgs. 209/2024.
- Aggiornato `references/sources.yaml` con SHA256 reali (calcolati dai PDF scaricati),
  `md_path` per le due fonti con PDF scaricati, aggiornamento URL correttivo (SO n. 3, non n. 4).
- **Corretti gli estratti** dopo lettura del testo normativo:
  - `allegato-i7-pfte.md`: rimossa affermazione errata che il "disciplinare descrittivo e
    prestazionale" (art. 14) sia elaborato obbligatorio dell'art. 21 co. 2 per appalto integrato
    (il testo normativo dell'art. 21 co. 2 non lo include); aggiornato elenco elaborati co. 7
    lett. p con la modifica del correttivo (ora limitata ad appalto integrato + BIM); aggiunta
    nota sul conteggio delle lettere (18, non un numero diverso).
  - `allegato-i7-esecutivo.md`: aggiornato con lettere p-bis e p-ter introdotte dal correttivo;
    nota su abrogazione co. 5; corrette le citazioni agli articoli di dettaglio.
  - `dlgs-36-art-41.md`: riscritto integralmente con citazioni precise a fonte verbatim.
  - `dlgs-209-2024-modifiche.md`: riscritto integralmente con citazioni precise a fonte verbatim.
- **Corretti i task files**:
  - `verifica-completezza-pfte.md`: corretto "16 elaborati" -> "18 elaborati" (art. 6 co. 7);
    aggiunta citazione alla fonte.
  - `genera-checklist-pfte.md`: rimossa "disciplinare descrittivo" dall'elenco obbligatorio per
    appalto integrato (non tracciabile in art. 21 co. 2); lista corretta con i 4 elaborati
    dell'art. 21 co. 2 (PSC, piano manutenzione, schema contratto, capitolato speciale).
  - `verifica-coerenza-esecutivo.md`: aggiunta citazione alla fonte per art. 22 co. 4.
- Closes #105.

## [0.1.0-alpha] - 2026-04-29

### Added
- Prima versione alpha della skill PFTE Allegato I.7 Checker
- Task files: `genera-checklist-pfte.md`, `verifica-completezza-pfte.md`, `verifica-coerenza-esecutivo.md`
- Fonti normative consultate: D.Lgs. 36/2023 (art. 41 + Allegato I.7) e D.Lgs. 209/2024 correttivo
- Estratti testuali strutturati: `dlgs-36-art-41.md`, `allegato-i7-pfte.md`, `allegato-i7-esecutivo.md`, `dlgs-209-2024-modifiche.md`
- Esempi: 1 conforme (nuova costruzione) + 1 incompleto (manutenzione straordinaria con elaborati mancanti)
- Documentazione dual-agent (Claude Code + OpenAI Codex)

### Note di sviluppo
- Skill non ancora validata da dominio terzo (Livello 1: autore-driven, fonti pubbliche).
- Da considerare draft finche' non passa validazione Livello 2 con un RUP / ingegnere civile esperto in procedure post D.Lgs. 36/2023 (vedi `methodology/validazione.md`).
- I PDF delle fonti (D.Lgs. 36/2023 e correttivo) non sono stati scaricati automaticamente: i campi `sha256` in `sources.yaml` sono `null`. Per popolarli eseguire manualmente `scripts/fetch-sources.sh pfte-allegato-i7-checker` (richiede permessi di rete) e committare sources.yaml aggiornato.
- Issue di riferimento: GitHub issue #3 ([P1] PR.1).
