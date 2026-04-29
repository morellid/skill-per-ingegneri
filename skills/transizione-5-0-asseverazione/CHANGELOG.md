# CHANGELOG - transizione-5-0-asseverazione

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-04-29

### Added
- Prima versione alpha della skill di asseverazione tecnica del Piano Transizione 5.0
- SKILL.md con frontmatter `license: MIT` e routing verso 4 task files
- agents/openai.yaml con metadata Codex
- 4 task files: `verifica-ammissibilita.md`, `calcola-riduzione-consumi.md`, `struttura-certificazione-ex-ante.md`, `struttura-certificazione-ex-post.md`
- references/sources.yaml con 11 fonti primarie e 3 fonti secondarie da valutare
- references/estratti/ con 5 estratti testuali strutturati:
  - `dl-19-2024-art-38.md`
  - `dm-24-07-2024-articoli-chiave.md`
  - `circolare-mimit-criteri-risparmio.md`
  - `circolare-mimit-modelli-certificazioni.md`
  - `faq-mimit-soggetti-certificatori.md`
  - `circolare-mise-2014-tep.md`
- 2 esempi (1 conforme manifatturiero meccanico 3,2 mln EUR + 1 non conforme cogenerazione gas naturale per violazione DNSH)
- AGENTS.md di dominio con convenzioni specifiche per la materia

### Note di sviluppo
- Skill non ancora validata da dominio terzo (Livello 1)
- Da considerare draft finche' non passa validazione Livello 2 (vedi methodology/validazione.md)
- Validatore di Livello 2 da identificare: profilo EGE/ESCo con esperienza in asseverazioni T5.0 gia' presentate al GSE
- Verificare al prossimo aggiornamento: modifiche L. 207/2024 (Bilancio 2025) art. 1 co. 427-429, eventuali DM correttivi al DM 24/7/2024, FAQ MIMIT successive al 10/4/2025
- Hash SHA256 dei PDF normativi non popolati (campo `sha256: null` in sources.yaml): da popolare manualmente eseguendo `curl + shasum` come indicato nelle note di sources.yaml
