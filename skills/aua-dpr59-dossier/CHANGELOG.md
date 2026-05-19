# CHANGELOG - aua-dpr59-dossier

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-05-19

### Added
- Prima versione alpha della skill AUA ex D.P.R. 59/2013.
- `SKILL.md` con 5 sotto-attivita': verifica applicabilita', mapping
  titoli art. 3, pianificazione termini, pianificazione rinnovo, triage
  modifica art. 6.
- Task files corrispondenti in `tasks/`.
- Fonte autoritativa: D.P.R. 13 marzo 2013, n. 59 da Normattiva (testo
  vigente al 2026-05-19, sha256
  `f566907ae45ddccd6f2300ad098779de6a3f13b1df2f072e986496bcca363823`).
- Trascrizione verbatim degli articoli 1-12 in
  `references/fonti/dpr-59-2013-articoli-1-12.md`.
- Estratto operativo in 10 sezioni in
  `references/estratti/dpr-59-2013-aua-perimetro.md`.
- Esempi: un caso conforme (PMI metalmeccanica con scarichi industriali
  e emissioni in atmosfera) + un caso problematico (impianto AIA per
  cui l'AUA non si applica).
- `AGENTS.md` di skill con convenzioni di dominio.
- `agents/openai.yaml` con metadata Codex.

### Note di sviluppo
- Skill **non ancora validata** da dominio terzo. Da considerare draft
  finche' non passa validazione Livello 2 (vedi
  `methodology/validazione.md`).
- Le discipline regionali AUA (art. 3 co. 2) non sono trattate: la
  skill copre il regolamento statale; rinvio a leggi e modulistica
  regionale.
- L'Allegato I (autorizzazioni di carattere generale) non e' trascritto
  verbatim per limiti del rendering Normattiva (tabelle in formato
  grafico nella GU n.124/2013 S.O. n.42).
