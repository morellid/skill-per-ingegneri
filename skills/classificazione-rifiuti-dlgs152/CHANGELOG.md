# CHANGELOG - classificazione-rifiuti-dlgs152

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-17

### Added (closes #360)
- Prima versione della skill di supporto al **tecnico ambientale**, all'**RSGA** e al **produttore/
  detentore** per la **classificazione dei rifiuti**, ai sensi del **D.Lgs. 3 aprile 2006, n. 152,
  Parte IV, artt. 183 e 184**, nell'area `ambiente-territorio-mobilita`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.Lgs. 152/2006** - indice Normattiva pinnato `!vig=2026-07-17` SHA256:
    c2175fe5c9313db1087d444b07e71d727154140d579ffcf6357ababa5d57b45c (codice 006G0171, idGruppo 34).
    Artt. 183 (v17) e 184 (v9) via `caricaArticolo` (formato AKN).
  - Trascrizione verbatim in `references/fonti/dlgs-152-2006-183-184.md` (art. 183 lettere rilevanti;
    art. 184 cc. 1-5).
- Estratto operativo `references/estratti/classificazione-rifiuti-checklist.md`.
- Due task: `inquadra-origine-rifiuto.md` e `inquadra-pericolosita-codice.md`.
- Due esempi: rifiuti da C&D e barattoli di vernice (origine e pericolosita', voci a specchio); rifiuti
  d'ufficio (urbani per similarita' vs speciali, superamento della nozione di "assimilati").

### Contenuto ancorato al testo
- Definizioni essenziali - rifiuto, produttore iniziale/nuovo, detentore, deposito temporaneo prima
  della raccolta (rinvio art. 185-bis) (183); classificazione secondo l'origine in urbani (domestici e
  simili - All. L-quater/L-quinquies) e speciali (C&D e scavo, industriali, artigianali, commerciali, di
  servizio, fanghi, sanitari, veicoli fuori uso) e secondo la pericolosita' (caratteristiche Allegato I),
  elenco europeo dei rifiuti (Allegato D) vincolante per i pericolosi, attribuzione dei codici e delle
  caratteristiche di pericolo a cura del produttore sulla base delle Linee guida SNPA (184).

### Scope e limiti
- Non attribuisce il codice EER ne' la classe di pericolo del singolo rifiuto, non redige l'analisi di
  caratterizzazione ne' compila registri/FIR/MUD, non riproduce gli Allegati D/I/L-quater/L-quinquies ne'
  le Linee guida SNPA. Non sostituisce il produttore, il tecnico ambientale ne' il laboratorio.

### Note di sviluppo
- Distinta da `sottoprodotti-end-of-waste-dlgs152` (184-bis/ter) e `terre-rocce-scavo-dpr120`. Deposito
  temporaneo (art. 185-bis) trattato solo come rinvio.
- Artt. 183-184 aggiornati dal D.Lgs. 116/2020 (recepimento dir. 2018/851). Validazione Livello 2 con
  tecnico ambientale/chimico.
