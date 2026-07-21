# CHANGELOG - accessi-passi-carrabili-cds

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-17

### Added (closes #339)
- Prima versione della skill di supporto all'inquadramento di **accessi, diramazioni e passi
  carrabili** dalla strada ai fondi/fabbricati laterali, ai sensi dell'**art. 22 del D.Lgs. 30
  aprile 1992, n. 285** (Codice della Strada), nell'area `ambiente-territorio-mobilita`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.Lgs. 285/1992 (CdS)** - indice Normattiva pinnato `!vig=2026-07-17`
    SHA256: e541dc1a2a210a4ffbc9edb9fb8c5bb21ee41241638dffbb0cee783cadb84918
    (codice 092G0306). Art. 22 via `caricaArticolo` (versione 17, idGruppo 2, formato AKN).
  - Trascrizione verbatim in `references/fonti/cds-285-1992-art22.md`: art. 22 per intero (12 commi).
- Estratto operativo `references/estratti/accessi-passi-carrabili-checklist.md`.
- Due task: `inquadra-autorizzazione-accesso.md` e `verifica-divieti-sanzioni.md`.
- Due esempi: nuovo accesso carrabile a un fondo su strada provinciale; accesso a un insediamento
  senza autorizzazione e in posizione vietata (corsia di decelerazione).

### Contenuto ancorato al testo
- Preventiva autorizzazione dell'ente proprietario per nuovi accessi/diramazioni/innesti (c. 1);
  regolarizzazione degli esistenti (c. 2); passi carrabili con segnale previa autorizzazione (c. 3);
  divieto di trasformazioni/variazioni d'uso senza autorizzazione (c. 4); diniego rinviato al
  regolamento (c. 5); opere sui fossi e caratteristiche plano-altimetriche (c. 6); modalita'
  costruttive nel regolamento (c. 7); parcheggi per accessi a insediamenti (c. 8); opere particolari
  e consorzi obbligatori (c. 9); caratteristiche tecniche con decreto MIT e divieto di accessi su
  rampe/corsie di accelerazione-decelerazione (c. 10); sanzioni da 173 a 694 euro (c. 11) e da 42 a
  173 euro (c. 12).

### Scope e limiti
- Non rilascia l'autorizzazione, non redige l'istanza/progetto, non riproduce il Regolamento (DPR
  495/1992, artt. 44-46) ne' i decreti MIT sulle caratteristiche tecniche; non tratta titolo
  edilizio/SUE ne' il canone. Non sostituisce l'ente proprietario/gestore della strada.

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del CdS pinnato (nuovo hash) e verificare
  gli adeguamenti biennali delle sanzioni (art. 195, c. 3) segnalati dai doppi tondi `(( ))`.
- Validazione Livello 2 con esperto di polizia stradale / ente proprietario della strada.
