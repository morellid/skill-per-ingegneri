# CHANGELOG - istruzioni-uso-macchine-reg-1230

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-15

### Added (closes #56)
- Prima versione della skill di supporto documentale alla redazione e alla
  verifica di completezza delle istruzioni per l'uso (manuale di uso e
  manutenzione) di una macchina o prodotto correlato ai sensi dell'allegato III
  punto 1.7.4 del Reg. (UE) 2023/1230.
- Fonte letta e trascritta (Regola zero):
  - **Reg. (UE) 2023/1230** (Regolamento Macchine), testo su eur-lex
    (`CELEX:32023R1230`). Fonte **online-only** (`binary_path: null`, `sha256:
    null`): eur-lex non e' riproducibile con hash stabile e blocca gli IP
    datacenter di GitHub Actions (stesso approccio della skill ai-act-compliance).
    Il punto 1.7.4 dell'allegato III (1.7.4.1 principi generali; 1.7.4.2 contenuto
    a-u, incluse le informazioni sull'emissione di rumore aereo u.i-iii) e la
    deroga linguistica per la manutenzione sono trascritti verbatim in
    `references/fonti/reg-ue-2023-1230-istruzioni.md`.
- Estratto operativo `references/estratti/istruzioni-uso-checklist.md`.
- Due task: `redigi-istruzioni.md` e `verifica-completezza-istruzioni.md`.
- Due esempi: istruzioni per operatori non professionali; lingua della
  manutenzione (personale specializzato) e formato digitale/cartaceo.

### Note di source-grounding e scope
- La skill copre le **istruzioni per l'uso** (allegato III, 1.7.4). E'
  **complementare** alla skill `fascicolo-tecnico-macchine-reg-1230` (fascicolo
  tecnico, allegato IV; dichiarazioni UE, allegato V).
- Gli obblighi generali dell'**art. 10 §7-8** (lingua, formato digitale/cartaceo,
  accesso alla dichiarazione UE) sono citati come rinvio. Gli altri RES
  dell'allegato III e le **norme armonizzate** UNI/CEN (a pagamento) non sono
  riprodotti. La **valutazione dei rischi** e i valori (rumore, massa) sono a monte.

### Note di sviluppo
- Fonte eur-lex online-only: a ogni aggiornamento rileggere il punto 1.7.4 e l'art.
  10 del Reg. (UE) 2023/1230.
- Il regolamento si applica dal **14 gennaio 2027** (abroga la dir. 2006/42/CE).
- Validazione Livello 2 da effettuare con esperto marcatura CE macchine.
