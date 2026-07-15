# CHANGELOG - scheda-dati-sicurezza-sds-reg878

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-15

### Added (closes #35)
- Prima versione della skill di supporto documentale alla compilazione e alla
  verifica di completezza della Scheda di Dati di Sicurezza (SDS) secondo
  l'allegato II del REACH quale sostituito dal Reg. (UE) 2020/878.
- Fonte letta e trascritta (Regola zero):
  - **Reg. (UE) 2020/878** (sostituisce l'allegato II REACH), testo su eur-lex
    (`CELEX:32020R0878`). Fonte **online-only** (`binary_path: null`, `sha256:
    null`): eur-lex non e' riproducibile con hash stabile e blocca gli IP
    datacenter di GitHub Actions (stesso approccio della skill ai-act-compliance).
    Parte A (prescrizioni generali 0.2-0.3) e struttura completa delle 16 sezioni
    con le sotto-sezioni trascritte verbatim in
    `references/fonti/reg-ue-2020-878-sds.md`.
- Estratto operativo `references/estratti/sds-16-sezioni-checklist.md`.
- Due task: `compila-sds.md` e `verifica-completezza-sds.md`.
- Due esempi: sezione 3 per una miscela; revisione e datazione della SDS.

### Note di source-grounding e scope
- La skill copre la **struttura** e le **prescrizioni generali** dell'allegato II.
  L'**obbligo** e le condizioni di fornitura della SDS sono nell'**art. 31 REACH**
  (citato, non riprodotto). La **classificazione CLP** (Reg. 1272/2008) e la
  **valutazione della sicurezza chimica** sono a monte e non sono svolte.
- I sistemi di trasporto (ADR/RID/IMDG/IATA) e la dir. 98/24/CE richiamati sono
  citati, non riprodotti.

### Note di sviluppo
- Fonte eur-lex online-only: a ogni aggiornamento rileggere il testo del Reg. (UE)
  2020/878 ed eventuali modifiche successive dell'allegato II REACH.
- Validazione Livello 2 da effettuare con esperto REACH/CLP.
