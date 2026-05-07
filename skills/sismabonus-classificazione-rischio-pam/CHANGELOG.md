# CHANGELOG - sismabonus-classificazione-rischio-pam

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-05-07

### Added
- Prima versione alpha della skill (issue #12 del repo).
- Modulo di calcolo Python `tasks/lib/sismabonus.py` con:
  - costruzione Curva di Individuazione (5 punti SLID/SLO/SLD/SLV/SLC + termine SLR)
  - calcolo PAM con formula trapezoidale a 4 termini + coda lambda(SLC)*CR(SLR), DM 58/2017 Allegato A punto 2.1
  - calcolo IS-V = PGA_C(SLV)/PGA_D(SLV), Allegato A punto 2.2
  - attribuzione classe PAM (8 classi A+..G) e IS-V (7 classi A+..F) per le tabelle Allegato A punto 2.3
  - regola classe finale = peggiore tra le due
  - calcolo salto classi tra fatto e progetto (Allegato A punto 3)
  - segnalazione `monotona: false` su curve non monotone
  - validazione input hardening (NaN/inf/string/bool/negativi) + RFC 8259 su JSON
  - CLI `--input-json` con error handling friendly
- Test suite `tasks/lib/test_sismabonus.py`: 48 test su consistenza interna (formula PAM, bordi tabelle classi, salto classi, validazione input, CLI, anti-drift fixture-based).
- Task files: `calcola-classificazione.md`, `valida-input.md`, `run-test-suite.md`.
- Estratti normativi in `references/estratti/`: art. 3 DM 58, Allegato A punto 2.1 (PAM), 2.2 (IS-V), 2.3 (tabelle classi), 3 (salto classi).
- Fonti catalogate in `references/sources.yaml` (DM 58/2017 + DM 65/2017 + DM 24/2020 + DM 329/2020 + NTC 2018 + Circ. 7/2019).
- Esempi: `caso-conforme-fittizio` (smoke test, salto classi B->A), `caso-non-monotono` (caso patologico con warning).
- AGENTS.md con convenzioni di dominio per agent.

### Note di sviluppo
- Skill non ancora validata da dominio terzo (Livello 2). Test interni: 48/48 OK.
- **Validazione di campo (Livello 2)** richiesta prima del release stabile: confronto numerico vs software certificati (ClaSS S.I.S., CDM Win STS, EdiSis Newsoft, MasterSap-SismiClass AMV) su almeno 10 edifici reali. Piano dettagliato in `tasks/run-test-suite.md`.
- Metodo SEMPLIFICATO per edifici in muratura (Allegato A punto 3, tabella tipologie x numero piani) **fuori scope** della v0.1.0-alpha. Richiede tabelle aggiuntive e logica condizionale; pianificato per v0.2.0.
- Generazione Allegato B / B-bis (asseverazione tecnica) **fuori scope** della skill: la skill produce numeri, l'asseverazione formale e' a cura del professionista firmatario.
- Aliquote di detrazione fiscale sismabonus (50/70/75/80/85/super-110%) **fuori scope** della skill: dipendono da legge finanziaria vigente, demandate al commercialista.

### Hash sorgenti
Da calcolare al primo fetch effettivo (`./scripts/fetch-sources.sh`); placeholder `REPLACE_WITH_ACTUAL_HASH` in `references/sources.yaml`.
