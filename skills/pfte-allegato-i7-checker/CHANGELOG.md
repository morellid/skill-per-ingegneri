# CHANGELOG - pfte-allegato-i7-checker

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Esempi dedicati al task di verifica coerenza PFTE/esecutivo (`coerenza-nuova-costruzione/`, `coerenza-scostamenti/`).

## [0.2.0] - 2026-05-18

### Added (issue #171)

- **Obbligo BIM aggiornato** (art. 43 D.Lgs. 36/2023 come modificato dal Correttivo D.Lgs. 209/2024):
  - Soglia aggiornata a > 2 milioni di euro (innalzata da 1M dal Correttivo, in vigore dal 1 gennaio 2025).
  - Regime transitorio (art. 225-bis c.2) esplicitato nella variabile #5 del task `genera-checklist-pfte.md`.
  - Esclusione manutenzione ordinaria/straordinaria (salvo opere precedentemente eseguite con GID).
  - Fonte: MIT Linee Guida GID 2026 (par. 1.2.2-1.2.4, pag. 8-13), SHA256 `7150201b23813c2b39c606e948751927ec75c6c526ad5bbe751ca0016783f7ab`.

- **Bando Tipo n. 2/2026 ANAC** (Delibera 153/2026, GU n. 111 del 15/05/2026, in vigore dal 30/05/2026):
  - Nota nella sezione "Non usare" di `SKILL.md`: per gare SIA sopra soglia il Bando Tipo n. 2/2026 codifica BIM come clausola strutturale; la skill gestisce il check sugli elaborati BIM del PFTE (g, p), la conformita' dell'intero set documentale di gara e' della skill `bandi-tipo-anac-checker`.
  - Nota sulla maggiorazione del compenso del 10% per gare SIA sopra soglia con lavori > 2M EUR (Allegato I.13, art. 2 c.5).
  - Nota sull'Offerta di Gestione Informativa (OGI) nella voce p della tabella elaborati.
  - Fonte: ANAC Bando Tipo n. 2/2026, SHA256 `3c39962bc041200fc03a2cc20c727c42b22e096e999cc9dcb3ccd28f786c2b49`.

- **Clausola AI obbligatoria** (art. 13 L. 132/2025, par. 15.1 Bando Tipo n. 2/2026):
  - Aggiunta variabile #9 "Gara SIA sopra soglia europea" in `genera-checklist-pfte.md` con spiegazione della clausola dichiarazione uso AI.
  - Aggiunta nota nel task `verifica-completezza-pfte.md` (caso "Gara SIA sopra soglia") che distingue tra clausola AI (attiene all'offerta di gara, non agli elaborati del PFTE) e completezza documentale del PFTE.
  - Aggiunta in "Elementi non valutabili automaticamente" la clausola AI e il regime transitorio BIM.

- **Elaborati BIM nel PFTE** (MIT LG GID 2026, Schema 2 - par. 3, pag. 48-52):
  - Voce g aggiornata con denominazione corretta "Modelli informativi + relazione specialistica sulla modellazione informativa" e riferimento a artt. 13 e 13-bis Allegato I.7 + MIT LG GID Schema 2.
  - Voce g in `verifica-completezza-pfte.md` aggiornata con denominazioni attese (Modelli IFC, Relazione specialistica, formati IFC/BCF/PDF-A).
  - Sezione "Gara SIA sopra soglia" in `verifica-completezza-pfte.md`: verifica conformita' modelli al Capitolato Informativo (All. I.7 art. 40 c.2 lett. i-bis e i-ter) e formati aperti richiesti.

- **Integrazione MIT LG GID 2026 con Allegato I.7**:
  - Estratto `references/estratti/mit-gid-2026-bim-pfte.md` con: art. 43 verbatim, soglie, regime transitorio, BIM roles lato SA, Schema 2 PFTE-GID, capitolato informativo, formati aperti.
  - Estratto `references/estratti/anac-bando-tipo-n2-2026-bim-ai.md` con: clausola BIM premesse verbatim, requisiti BIM par. 6.1, 10% compenso, clausola AI par. 15.1 verbatim, par. 16 OGI.
  - Fonti aggiunte in `references/sources.yaml`: `anac-bando-tipo-n2-2026-del-153-2026` e `mit-lg-gid-2026-02-20`.
  - Riferimenti ai nuovi estratti aggiunti in `SKILL.md`, `genera-checklist-pfte.md`, `verifica-completezza-pfte.md`.

- **Aggiornamento `last_verified`**: 2026-05-10 -> 2026-05-18.

- Closes #171.

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
