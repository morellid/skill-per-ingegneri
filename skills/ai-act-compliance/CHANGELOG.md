# CHANGELOG - ai-act-compliance

Tutte le modifiche significative alla skill sono documentate qui.

Formato basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
versionamento [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Da fare
- Validazione Livello 1 con `scripts/validate.sh`
- Validazione Livello 2 da consulente legale specializzato in diritto digitale
- Test su caso reale di compliance AI Act (con consenso cliente)
- Catalogare linee guida Commissione su pratiche vietate (febbraio 2025) appena disponibili
- Catalogare linee guida Commissione su classificazione art. 6 (scadenza 02/02/2026)
- Aggiungere estratti di Allegato XI (doc tecnica GPAI) e XII (info per integratori) quando piu' rilevanti
- Aggiungere estratto di Allegato IV (documentazione tecnica art. 11) per provider high-risk
- Esempi aggiuntivi:
  - `provider-credit-scoring-gap/` per check-high-risk-provider
  - `deployer-pa-assistenza/` per check-deployer-obligations
  - `gpai-provider-llm-rischio-sistemico/` per check-gpai-provider
- Tracciare aggiornamenti norme armonizzate ETSI/CEN-CENELEC
- Tracciare Code of Practice GPAI quando definitivo

## [0.1.0-alpha] - 2026-04-25

### Added
- Scaffold completo via `scripts/new-skill.sh`
- `SKILL.md` con frontmatter, routing a 5 task files, disclaimer art. 99 sanzioni
- 6 estratti normativi:
  - `references/estratti/ai-act-art-5-pratiche-vietate.md` - 8 pratiche vietate + esempi tipici per ingegneri
  - `references/estratti/ai-act-art-6-9-classificazione-high-risk.md` - classificazione + sistema gestione rischi
  - `references/estratti/ai-act-allegato-iii.md` - 8 settori high-risk + mappa tipica per use case
  - `references/estratti/ai-act-art-26-27-deployer-fria.md` - obblighi deployer + FRIA
  - `references/estratti/ai-act-art-50-trasparenza.md` - 5 categorie trasparenza
  - `references/estratti/ai-act-art-51-55-gpai.md` - GPAI standard + rischio sistemico
- 5 task files operativi:
  - `tasks/classifica-sistema.md` - 9 step di classificazione + obblighi applicabili
  - `tasks/check-high-risk-provider.md` - checklist art. 8-22 + conformity assessment
  - `tasks/check-deployer-obligations.md` - obblighi art. 26 + FRIA art. 27
  - `tasks/check-gpai-provider.md` - obblighi art. 53 + 55
  - `tasks/check-trasparenza.md` - 5 categorie obblighi art. 50
- `references/sources.yaml` con hash SHA256 reale per AI Act italiano (a61b6170...)
- 2 esempi:
  - `examples/classifica-chatbot-cs/` - chatbot CS basato su GPT-4 = TRASPARENZA art. 50
  - `examples/classifica-hr-emozioni/` - video-interview HR con sentiment analysis = VIETATO art. 5 lett. f, con percorso di pivot a high-risk

### Note di sviluppo
- Skill considerata draft finche' non passa Livello 2 di validazione (consulente legale specializzato)
- Validatore di dominio target: avvocato diritto digitale UE / consulente AI compliance
- Skill commercialmente valida sia per uso open via repo (ingegneri italiani) sia per consulenza enterprise (vedi piano boutique business)
- Sinergica con skill `gdpr-registro-dpia` per casi che intersecano dati personali

### Date di applicazione AI Act (riferimento)
- 02/02/2025: pratiche vietate (art. 5) + AI literacy (art. 4)
- 02/08/2025: GPAI (art. 53-55) + governance + sanzioni
- 02/08/2026: high-risk Allegato III (maggior parte degli obblighi)
- 02/08/2027: high-risk Allegato I (componenti sicurezza prodotti)
