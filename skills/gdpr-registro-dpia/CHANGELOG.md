# CHANGELOG - gdpr-registro-dpia

Tutte le modifiche significative alla skill sono documentate qui.

Formato basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
versionamento [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Da fare
- Validazione Livello 1 con `scripts/validate.sh`
- Validazione Livello 2 da DPO esterno o ingegnere informazione/cybersecurity
- Test su Registro reale di una PMI italiana (con consenso titolare)
- Aggiungere esempio "registro-incompleto" per check
- Catalogare e citare il Codice di Deontologia sistemi informativi creditizi (Allegato A.5 Cod. Privacy) per casi fintech
- Aggiungere riferimenti a linee guida EDPB tematiche (videosorveglianza, AI, biometria, lavoro)

### Note tecniche
- Ricalcolare hash WP248 (download da identificare URL stabile EDPB)
- Aggiungere fetch script per WP248 quando URL e' stabile

## [0.1.0-alpha] - 2026-04-25

### Added
- Scaffold completo della skill via `scripts/new-skill.sh`
- `SKILL.md` con frontmatter, routing a 4 task files (draft+check registro, valuta soglia DPIA, draft DPIA), disclaimer art. 83 GDPR
- 4 task files operativi:
  - `tasks/draft-registro-trattamenti.md` - stesura Registro guidata, 7 voci titolare / 4 responsabile
  - `tasks/check-registro-trattamenti.md` - verifica completezza con pattern di problemi comuni
  - `tasks/valuta-soglia-dpia.md` - 12 tipologie Garante + 9 criteri WP248 + art. 35 par. 3
  - `tasks/draft-dpia.md` - stesura DPIA con 4 contenuti minimi par. 7 e tabella rischi-misure
- 3 estratti normativi:
  - `references/estratti/gdpr-art-30.md` - testo art. 30 + sintesi 7 contenuti minimi
  - `references/estratti/gdpr-art-35-36.md` - testo art. 35-36 + 9 criteri WP248
  - `references/estratti/garante-allegato1-prov467-2018.md` - 12 tipologie italiane
- `references/sources.yaml` con hash SHA256 reali per:
  - GDPR italiano consolidato Garante (16c0bb35...)
  - Garante Allegato 1 Provv. 467/2018 (6ece43c2...)
- 2 esempi:
  - `examples/registro-pmi-base/` - PMI 50 dipendenti, 6 trattamenti tipici (HR, CRM, fornitori, marketing, videosorveglianza, sito web). Expected: CONFORME CON NOTE MINORI con T5 da chiarire e T2 da documentare.
  - `examples/dpia-soglia-app-scoring/` - sistema scoring credito con decisioni automatizzate. Expected: DPIA OBBLIGATORIA con 4 tipologie + 7 criteri attivati + lista 9 punti attenzione per la DPIA.

### Note di sviluppo
- Skill considerata draft finche' non passa Livello 1 di validazione (vedi `methodology/validazione.md`)
- Validatore di dominio target: DPO esperto o ingegnere informazione con esperienza compliance privacy
- Settori di applicazione tipici: SaaS B2B, fintech, app mobile, IoT, AI/ML systems
