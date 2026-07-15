# CHANGELOG - fascicolo-tecnico-dispositivi-medici-mdr

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-15

### Added (closes #47)
- Prima versione della skill di supporto documentale alla struttura del fascicolo
  tecnico e al percorso di valutazione della conformita' di un dispositivo medico
  di classe I o IIa ai sensi del Reg. (UE) 2017/745 (MDR).
- Fonte letta e trascritta (Regola zero):
  - **Reg. (UE) 2017/745 (MDR)**, testo consolidato su eur-lex
    (`CELEX:02017R0745-20240709`). Fonte **online-only** (`binary_path: null`,
    `sha256: null`): eur-lex non e' riproducibile con hash stabile e blocca gli IP
    datacenter di GitHub Actions (stesso approccio della skill ai-act-compliance).
    Struttura dell'allegato II (documentazione tecnica, 6 capitoli), allegato III
    (sorveglianza post-commercializzazione), art. 52 (procedure classi I e IIa,
    incluse Is/Im/Ir) e intestazione dell'allegato VIII trascritti verbatim in
    `references/fonti/reg-ue-2017-745-mdr.md`.
- Estratto operativo `references/estratti/fascicolo-tecnico-mdr-checklist.md`.
- Due task: `struttura-fascicolo-tecnico.md` e `scegli-percorso-conformita.md`.
- Due esempi: classe I sterile (Is) con organismo notificato limitato; classe IIa
  con scelta del percorso (allegato IX o XI).

### Note di source-grounding e scope
- La skill lavora sulla **struttura** del fascicolo (allegato II + III) e sul
  **percorso** (art. 52). Le **22 regole di classificazione** (allegato VIII) e i
  **requisiti generali di sicurezza e prestazione** (allegato I) sono citati come
  rinvio, non riprodotti integralmente. La **valutazione clinica**, le prove e le
  norme armonizzate (a pagamento) restano fuori scope.
- **Area di catalogo**: classificata in `impianti-macchine-prodotti` (compliance di
  prodotto) in assenza di un'area "biomedico" (le aree sono fisse in `areas.yaml`,
  promozione a nuova area con >= 3 skill).

### Note di sviluppo
- Fonte eur-lex online-only (testo consolidato): a ogni aggiornamento rileggere gli
  allegati II, III, VIII e l'art. 52 nella versione consolidata piu' recente.
- MDR pienamente applicabile dal 26 maggio 2021.
- Validazione Livello 2 da effettuare con esperto RA dispositivi medici.
