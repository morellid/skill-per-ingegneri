# CHANGELOG - autorizzazione-paesaggistica-semplificata-dpr31

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-16

### Added (closes #249)
- Prima versione della skill di supporto alla **qualificazione di un intervento in area a
  vincolo paesaggistico** rispetto all'**autorizzazione paesaggistica** (esclusa /
  semplificata / ordinaria), ai sensi del **D.P.R. 13 febbraio 2017, n. 31**, nell'area
  `edilizia-urbanistica-catasto`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.P.R. 13 febbraio 2017, n. 31** - indice Normattiva pinnato `!vig=2026-07-16`
    SHA256: e71de17b153daddcd22a4eacc47200d7bd7d22f9e8a278772f663d9fa3e7cc49
    (codice 17G00042). Articoli e Allegati via `caricaArticolo`.
  - Trascrizione verbatim in `references/fonti/dpr-31-2017.md`: art. 2 (interventi esclusi ->
    Allegato A), art. 3 (lieve entita' -> Allegato B), art. 4 (esonero), art. 7 (rinnovo),
    art. 9 (presentazione istanza), art. 11 (semplificazioni procedimentali), e per intero
    l'**Allegato A** (A.1-A.31) e l'**Allegato B** (B.1-B.42).
- Estratto operativo `references/estratti/autorizzazione-paesaggistica-checklist.md`.
- Due task: `qualifica-intervento-paesaggistico.md` e `imposta-procedimento-semplificato.md`.
- Due esempi: pannelli fotovoltaici esclusi (A.6); ampliamento di lieve entita' (B.1).

### Contenuto ancorato al testo
- Tre regimi: escluso (art. 2 + Allegato A), semplificato per interventi di lieve entita'
  (art. 3 + Allegato B, Capo II), ordinario (art. 146 del Codice). Esonero (art. 4).
  Presentazione a SUE/SUAP/amministrazione (art. 9). Verifica preliminare + conferenza di
  servizi con termini dimezzati (art. 11). Rinnovo semplificato (art. 7). Condizioni/limiti
  con richiami all'art. 136 del Codice.

### Scope e limiti
- Non riproduce la classificazione puntuale di ogni intervento (va letta sulle voci degli
  Allegati A e B dell'atto). Non rilascia l'autorizzazione, non redige la relazione
  paesaggistica, non tratta il titolo edilizio (DPR 380/2001 / D.Lgs. 222/2016) ne'
  l'accertamento di compatibilita' ex art. 167 del Codice.

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del D.P.R. 31/2017 pinnato (nuovo
  hash) e verificare le modifiche (es. DPR 73/2026, che ha modificato il DPR 31/2017).
- Validazione Livello 2 con esperto di tutela paesaggistica / funzionario di soprintendenza.
