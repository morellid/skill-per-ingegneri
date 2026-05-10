# CHANGELOG - dnsh-pnrr-checker

Tutte le modifiche significative alla skill sono documentate qui.

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
e questa skill aderisce a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### fix(source-grounding): remediation semantica (issue #99)

#### Fonti lette da PDF

- `circolare-rgs-22-2024-dnsh.pdf` (SHA256: 6f3f94e...81cb5, 3 pagine integrali) - letto 2026-05-10
- `guida-operativa-dnsh-terza-edizione.pdf` (SHA256: f924cb6...c29, pp. 1-23 introduzione metodologica completa) - letto 2026-05-10

Gli SHA256 erano gia' corretti in sources.yaml e corrispondono ai file in `not_in_repo/`. Questa remediation si concentra sul contenuto semantico.

#### Aggiunto

- `references/fonti/circolare-rgs-22-2024.md`: trascrizione integrale della circolare (3 pagine) con testo italiano originale, motivazione aggiornamento (CID n. 16051/23 del 8 dicembre 2023), novita' (Reg. Delegato (UE) 2023/2486, 3 fasi ReGiS, CAM art. 57 D.lgs. 36/2023).
- `references/fonti/guida-operativa-dnsh-2024.md`: trascrizione delle sezioni metodologiche della Guida (pp. 1-23): sei obiettivi ambientali, Regime 1 e 2 con condizioni di applicabilita' (tagging 100%), struttura schede (sezioni A-F), check list (SI/NO/Non applicabile + commento), conseguenza NO ex post (non conformita' al DNSH), tre fasi ReGiS, CAM, analisi rischio climatico (soglia 10 MLN euro), mappature 1 e 2.
- `md_path` aggiunto in `sources.yaml` per entrambe le fonti con binary.

#### Riscritto

- `references/estratti/guida-operativa-dnsh-2024.md`: completamente riscritto sulla base del testo letto. Aggiunto: condizioni per Regime 1 (tagging 100% climatico o ambientale, o autovalutazione esplicita); struttura schede tecniche (sezioni A-F); formato ufficiale check list (SI/NO/Non applicabile); conseguenza NO ex post (non conformita' formale); check list deve essere sottoscritte e datata; tre fasi ReGiS; CAM e relazione con Regime 1/2; soglia 10 MLN euro per analisi rischio climatico.
- `references/estratti/circolare-rgs-22-2024.md`: riscritto con citazioni dirette dal testo letto: CID n. 16051/23, Reg. Delegato (UE) 2023/2486, tre fasi ReGiS nominate esplicitamente, art. 57 D.lgs. 36/2023.

#### Corretto

- `tasks/verifica-checklist.md`: allineato al formato ufficiale SI/NO/Non applicabile della Guida RGS 2024 (p. 20-21). Aggiunto: significato preciso di ogni risposta per ex ante ed ex post; evidenziazione che NO ex post implica non conformita' al DNSH; obbligo di sottoscrivere e datare la check list; campo "fase attuativa ReGiS" negli input.
- `tasks/inquadra-misura-schede.md`: corretto il passo Regime DNSH con le tre condizioni di applicabilita' del Regime 1 tratte dalla Guida (p. 13), sostituendo la descrizione generica precedente.
- `tasks/piano-evidenze-report.md`: aggiunto piano per le tre fasi di attestazione ReGiS (selezione progetti, affidamento, rendicontazione), con contenuti specifici per ciascuna fase (Guida pp. 22-23); soglia 10 MLN euro per analisi rischio climatico; distinzione Consip vs Invitalia per fase 2.

#### Verificato invariato

- `references/estratti/reg-ue-2020-852-art-17.md`: contenuto confermato dalla Guida (che cita art. 17 e i sei obiettivi). Lasciato invariato.
- `references/estratti/reg-ue-2021-241-art-5-18.md`: contenuto confermato dalla Guida (che cita art. 18 e art. 5 RRF). Lasciato invariato.
- `references/estratti/dl-77-2021-art-14-pnc.md` e `ministero-salute-principio-dnsh-pnc.md`: fonti web di contesto per casi PNC; non modificati (non sono fonte operativa principale).

---

### Changed (precedente Unreleased)
- Reso esplicito che il supporto PNC e' solo condizionato a una fonte misura-specifica che richiami il DNSH
- Aggiornate regole operative, task e metadata per impedire l'uso automatico della Guida RGS 2024 su casi PNC privi di base documentale

### Added (precedente Unreleased)
- Fonti integrative per supporto PNC condizionato (`DL 77/2021 art. 14` e pagina istituzionale Ministero della Salute sul principio DNSH)
- Estratti operativi dedicati al perimetro PNC condizionato

## [0.1.0-alpha] - 2026-05-04

### Added
- Prima versione alpha della skill DNSH PNRR
- SKILL.md con frontmatter `license: MIT` e routing verso 3 task files
- agents/openai.yaml con metadata Codex
- 3 task files:
  - `inquadra-misura-schede.md`
  - `verifica-checklist.md`
  - `piano-evidenze-report.md`
- references/sources.yaml con fonti UE/RGS e hash SHA256 dei PDF RGS scaricati in `not_in_repo/`
- references/estratti/ con 4 estratti sintetici strutturati
- README.md e AGENTS.md di dominio

### Note di sviluppo
- Skill non ancora validata da dominio terzo (Livello 1)
- Da considerare draft finche' non passa validazione Livello 2
- Verificare periodicamente aggiornamenti sulla pagina ufficiale Italia Domani / RGS DNSH e template ReGiS
