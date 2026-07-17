# CHANGELOG - collaudo-verifica-conformita-dlgs36

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-17

### Added (closes #315)
- Prima versione della skill di supporto al **collaudo dei lavori** e alla **verifica di
  conformita'** di servizi e forniture nei contratti pubblici, ai sensi del **D.Lgs.
  36/2023, art. 116**, nell'area `appalti-opere-pubbliche`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.Lgs. 31/3/2023 n. 36** - indice Normattiva pinnato `!vig=2026-07-17`
    SHA256: 0e9a193836e379cb33cb6daf1a5a988c608eb9559d84b91a841d9ed9791a62af
    (codice 23G00044). Art. 116 versione 2, idGruppo 18, flagTipoArticolo 0, via
    `caricaArticolo`.
  - Trascrizione verbatim in `references/fonti/dlgs-36-2023-art-116.md`.
- Estratto operativo `references/estratti/collaudo-verifica-checklist.md`.
- Due task: `inquadra-collaudo-termini.md` e `verifica-collaudatori-incompatibilita.md`.
- Due esempi: termini e natura del certificato di collaudo (cc. 1-3, 7); nomina del
  collaudatore e incompatibilita' (cc. 4-6).

### Contenuto ancorato al testo
- Art. 116 c. 1 collaudo (lavori)/verifica di conformita' (servizi-forniture); c. 2
  termini 6 mesi/1 anno (all. II.14), certificato provvisorio->definitivo a 2 anni,
  approvazione tacita; c. 3 responsabilita' appaltatore per vizi/difformita' salvo art.
  1669 c.c.; cc. 4/4-bis/4-ter nomina 1-3 collaudatori (requisiti, indipendenza, PA/non
  PA), collaudatore statico, segreteria tecnica; c. 5 verifica di conformita' del
  RUP/direttore dell'esecuzione; c. 6 incompatibilita' (a-e); c. 7 rinvio all'allegato
  II.14 per modalita' e CRE; cc. 8-11 modalita'/tempi verifica, documenti finali (piano
  di manutenzione, BIM art. 43), accertamenti di laboratorio non soggetti a ribasso.

### Scope e limiti
- Non redige il certificato di collaudo/verifica ne' il CRE, non riproduce gli allegati
  II.14/II.15, non nomina i collaudatori ne' valuta requisiti/conflitto di interesse
  (art. 16), non tratta il collaudo statico (DPR 380 art. 67), non sostituisce la
  stazione appaltante, il RUP o l'organo di collaudo. Allegati II.14/II.15, artt. 16, 29,
  43, 45 e art. 1669 c.c. citati e non trascritti.

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del D.Lgs. 36/2023 pinnato
  (nuovo hash) e rileggere l'art. 116 (testo tra `(( ))`, es. correttivo D.Lgs. 209/2024).
- Validazione Livello 2 con RUP / collaudatore / esperto di contratti pubblici.
