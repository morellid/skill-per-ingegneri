# CHANGELOG - condominio-parti-comuni-assemblea-cc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-17

### Added (closes #297)
- Prima versione della skill di supporto al **condominio negli edifici** (parti comuni, innovazioni,
  assemblea), ai sensi del **Codice civile, artt. 1117, 1120, 1136**, nell'area `forense`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **Codice civile (R.D. 262/1942)** - indice Normattiva pinnato `!vig=2026-07-17`
    SHA256: f817bc32707124081b048e6d34882a4256b7e107de3c4a018fcd83a936dce325
    (codice 042U0262). Artt. 1117 (v2), 1120 (v4), 1136 (v4), idGruppo 140, flagTipoArticolo 2, via
    `caricaArticolo`.
  - Trascrizione verbatim in `references/fonti/cc-artt-1117-1120-1136.md`.
- Estratto operativo `references/estratti/condominio-checklist.md`.
- Due task: `inquadra-parti-innovazione.md` e `verifica-quorum-assemblea.md`.
- Due esempi: quorum per la nomina dell'amministratore (art. 1136); innovazioni agevolate
  cappotto/fotovoltaico (art. 1120).

### Contenuto ancorato al testo
- Art. 1117 parti comuni (strutture/facciate/scale/cortili; parcheggi/locali servizi; impianti
  centralizzati fino al punto di diramazione/utenza; salvo titolo contrario); art. 1120 innovazioni
  ordinarie (2/3 del valore) e agevolate (metà del valore) con convocazione entro 30 gg su richiesta di
  un condomino e divieti (stabilità/sicurezza/decoro/inservibilità); art. 1136 costituzione
  dell'assemblea e validità delle deliberazioni (quorum 1ª/2ª convocazione, maggioranze qualificate del
  2° comma per nomina/revoca amministratore, liti, ricostruzione, innovazioni; convocazione di tutti gli
  aventi diritto; verbale).

### Scope e limiti
- Non redige verbali/delibere né compila le tabelle millesimali, non valuta validità/impugnazione (art.
  1137) né la ripartizione delle spese (artt. 1123-1126), non sostituisce l'amministratore, il legale o
  il giudice. Artt. 1118, 1122-bis/ter, 1130-1135 citati e non trascritti.

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del Codice civile pinnato (nuovo hash) e
  rileggere gli artt. 1117, 1120, 1136 (riforma L. 220/2012, testo tra `(( ))`).
- Validazione Livello 2 con avvocato civilista/amministratore di condominio.
