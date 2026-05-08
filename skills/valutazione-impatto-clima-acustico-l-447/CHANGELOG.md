# CHANGELOG - valutazione-impatto-clima-acustico-l-447

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-05-08

### Added

- Prima versione alpha della skill (Livello 1).
- `SKILL.md` con frontmatter dual-agent (`license: MIT`) e
  disclaimer professionale.
- `agents/openai.yaml` con `display_name`, `short_description` e
  `default_prompt`.
- 4 task files in `tasks/`:
  - `mappa-applicabilita-art-8.md` (c. 2 / c. 3 / c. 4 / c. 6 della
    L. 447/1995 art. 8)
  - `check-completezza-impatto-acustico.md`
  - `check-completezza-clima-acustico.md`
  - `checklist-relazione-previsionale.md`
- 3 estratti normativi in `references/estratti/`:
  - `legge-447-1995-art-8.md` (art. 8 cc. 1-6, art. 4 c. 1 lett. l,
    art. 6 c. 1 lett. d, art. 2 definizioni)
  - `dpcm-14-11-1997-valori-limite.md` (art. 1-8 + Tabelle A, B, C, D)
  - `dm-16-03-1998-tecniche-misurazione.md` (art. 1-2 + allegati A,
    B, C, D)
- 4 fonti registrate in `references/sources.yaml` (L. 447/1995 PDF
  MASE, DPCM 14/11/1997 HTML aggregato GU, DM 16/3/1998 HTML aggregato
  GU, L. 447/1995 Normattiva reference-only).
- 2 esempi in `examples/`:
  - `palestra-classe-iv-conforme/` (caso conforme con dettagli sul
    passaggio dal periodo diurno al notturno e sul differenziale)
  - `scuola-prossima-strada-incompleta/` (caso problematico:
    valutazione di clima acustico priva di firma TCAA, di misure e
    di rinvio al DPR 142/2004)
- `AGENTS.md` di skill con convenzioni di dominio specifiche.
- `README.md` di skill con target, sotto-attivita', fonti, limiti.

### Note di sviluppo

- Skill non ancora validata da dominio terzo.
- Da considerare draft finche' non passa validazione Livello 2 (vedi
  `methodology/validazione.md`).
- Rinvii strutturali a DPR 459/1998 (ferroviario) e DPR 142/2004
  (stradale) senza quotarne i numeri; valutare in v0.2 se aggiungere
  estratti dedicati di queste due fonti.
- Rinvio sempre alla **legge regionale** (art. 4 c. 1 lett. l) L.
  447/1995) e al **regolamento comunale** (art. 6 c. 2 L. 447/1995):
  la skill non quota i contenuti regionali/comunali.
