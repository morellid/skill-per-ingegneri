# CHANGELOG - segnalazione-agibilita-dpr380

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-16

### Added (closes #281)
- Prima versione della skill di supporto alla **segnalazione certificata di agibilità (SCA)**, ai
  sensi dell'**art. 24 del D.P.R. 6 giugno 2001, n. 380** (art. 25 abrogato dal D.Lgs. 222/2016),
  nell'area `edilizia-urbanistica-catasto`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.P.R. 6 giugno 2001, n. 380** - indice Normattiva pinnato `!vig=2026-07-16`
    SHA256: 98a209dab2743964d5eddeca5321261f5b12225c140367e17c53705e5b95acb2
    (codice 001G0429). Art. 24 (versione 7, idGruppo 7) e art. 25 via `caricaArticolo`.
  - Trascrizione verbatim in `references/fonti/dpr-380-2001-art-24-25.md`: art. 24 per intero
    (testo vigente, con i blocchi (( )) dei provvedimenti successivi) e art. 25 (abrogato).
- Estratto operativo `references/estratti/agibilita-checklist.md`.
- Due task: `prepara-sca.md` e `verifica-agibilita-parziale.md`.
- Due esempi: agibilità di nuova costruzione (SCA, 15 gg, SUE, documentazione, utilizzo dalla
  presentazione); agibilità parziale di singola unità (c. 4) con deroga di altezza (c. 5-bis/ter).

### Contenuto ancorato al testo
- Art. 24: strumento SCA (c. 1); soggetto/termine 15 gg/SUE e interventi (c. 2); sanzione 77-464
  euro (c. 3); agibilità parziale (c. 4); documentazione allegata (c. 5); deroghe igienico-sanitarie
  asseverabili - altezza 2,40 m, monostanza 20/28 mq, adattabilità DM 236/1989 (c. 5-bis/ter/quater);
  utilizzo dalla presentazione e richiamo art. 19 c. 3/6-bis L. 241/1990 (c. 6); controlli anche a
  campione (c. 7); SCA in assenza di lavori (c. 7-bis). Art. 25 abrogato (D.Lgs. 222/2016).

### Scope e limiti
- Non redige/presenta la SCA né compila la modulistica regionale/comunale (cfr.
  `modulistica-edilizia-unificata`). Non esegue collaudo statico (art. 67 → `denuncia-opere-strutturali-l1086`)
  né certificazioni impianti (DM 37/2008)/accessibilità (DM 236/1989). Non sostituisce il DL né il
  professionista abilitato.

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del D.P.R. 380/2001 pinnato (nuovo hash) e
  verificare le modifiche all'art. 24 (testo tra `(( ))`).
- Validazione Livello 2 con tecnico abilitato / SUE.
