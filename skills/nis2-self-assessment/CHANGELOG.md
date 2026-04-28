# CHANGELOG - nis2-self-assessment

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-04-29

### Added
- Prima versione alpha della skill `nis2-self-assessment`
- 4 task files:
  - `valuta-perimetro` - classificazione essenziale/importante/fuori ambito (art. 3, 6 D.Lgs. 138/2024)
  - `gap-analysis-misure` - gap analysis sui 10 elementi art. 24 + sottocategorie Framework Nazionale Cybersecurity
  - `verifica-incidente-significativo` - art. 25 e soglie ACN
  - `check-obblighi-governance` - art. 23 obblighi del CdA
- 6 estratti normativi:
  - `dlgs-138-2024-perimetro.md` (art. 3, 6, 7)
  - `dlgs-138-2024-misure-art23.md` (art. 23 + art. 24, con i 10 elementi minimi)
  - `dlgs-138-2024-incident-art25.md` (art. 25 + tempistiche)
  - `dlgs-138-2024-allegati-i-iv.md` (settori e tipologie)
  - `acn-misure-base-essenziali.md` (Allegato 2 Det. 164179/2025 - struttura completa)
  - `acn-misure-base-importanti.md` (Allegato 1 - struttura)
  - `acn-incidenti-significativi.md` (categorie incidenti significativi di base)
  - `reg-ese-2024-2690-ambito.md` (ambito Reg. UE 2024/2690)
- Fonti primarie catalogate in `sources.yaml` con SHA256 per i binari scaricati:
  - D.Lgs. 138/2024 (PDF GU)
  - Det. ACN 164179/2025 Allegato 2 essenziali (PDF)
- Compatibilita' dual-agent: Claude Code (SKILL.md) + OpenAI Codex (`agents/openai.yaml`)
- AGENTS.md con convenzioni di dominio, citazioni di articoli e best practice

### Note di sviluppo
- Skill **non ancora validata da dominio terzo** (Livello 2). Profilo target validatore: CISO o consulente cybersecurity con esperienza diretta su mandati NIS2 attivi.
- Il testo della **Determinazione ACN 379907/2025** (sostitutiva di 164179/2025 dal 15/01/2026) non e' ancora analizzato in dettaglio. La struttura per funzioni/categorie/sottocategorie e' coerente, ma il dettaglio dei requisiti puo' differire. Da catalogare con SHA256 e estratti dedicati nelle iterazioni successive.
- Le **soglie quantitative** degli incidenti significativi di base (Allegati 3 e 4 Det. 379907/2025) sono fornite a livello di categoria; i valori puntuali richiedono lettura del testo della determinazione.
- Esempi `examples/` non ancora popolati.
- Da considerare draft fino a validazione Livello 2 (vedi `methodology/validazione.md`).

### Limiti noti per la versione 0.1.0-alpha
- La skill non gestisce il calcolo dimensionale per gruppi/imprese collegate (art. 6 par. 2 dell'Allegato Racc. 2003/361/CE) oltre il rinvio strutturale.
- Non integra la determina applicabile per i soggetti del **Perimetro di Sicurezza Nazionale Cibernetica** (DL 105/2019) oltre il richiamo all'unificazione di notifica.
- Non produce moduli di registrazione precompilati per la piattaforma ACN.
