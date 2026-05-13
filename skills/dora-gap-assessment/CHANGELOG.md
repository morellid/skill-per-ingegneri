# CHANGELOG - dora-gap-assessment

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-05-13

### Added
- Prima versione alpha della skill di gap assessment DORA (Reg. UE 2022/2554).
- 5 task files, uno per pillar:
  - `tasks/check-pillar-1-ict-risk-mgmt.md` (artt. 5-16, 58 voci incl. quadro semplificato).
  - `tasks/check-pillar-2-incidents.md` (artt. 17-23, 20 voci).
  - `tasks/check-pillar-3-testing.md` (artt. 24-27, 22 voci).
  - `tasks/check-pillar-4-third-party.md` (artt. 28-30, 42 voci).
  - `tasks/check-pillar-5-info-sharing.md` (art. 45, 10 voci).
- Fonte primaria registrata in `references/sources.yaml` con SHA256 verificato: Regolamento (UE) 2022/2554 (DORA), versione PE-CONS 41/22 (testo trilogue-finale identico in contenuto a GU UE L 333 del 27/12/2022).
- Trascrizione integrale degli artt. 1-30, 45, 64 in `references/fonti/reg-ue-2022-2554-dora.md`.
- Estratti curati per pillar in `references/estratti/reg-ue-2022-2554-dora.md`.
- 2 esempi: 1 conforme + 1 problematico (vedi `examples/`).
- Frontmatter dual-agent: `SKILL.md` (Claude Code) + `agents/openai.yaml` (Codex).

### Note di sviluppo
- Skill non ancora validata da dominio terzo: status "alpha".
- Skill copre solo gli obblighi **lato entita' finanziaria** (artt. 1-30, 45, 64): fuori scope Capo V Sez. II (artt. 31-44, sorveglianza fornitori critici lato autorita'), Capo VII (artt. 46-56), Capo VIII salvo art. 64.
- Skill non valuta gli RTS/ITS DORA di secondo livello.
- Da considerare draft finche' non passa validazione Livello 2 (CISO/compliance di entita' diversa dall'autore - vedi `methodology/validazione.md`).
