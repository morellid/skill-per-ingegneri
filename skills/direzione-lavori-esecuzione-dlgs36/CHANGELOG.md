# CHANGELOG - direzione-lavori-esecuzione-dlgs36

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-17

### Added (closes #334)
- Prima versione della skill di supporto all'**inquadramento della direzione dei lavori (DL) e
  della direzione dell'esecuzione del contratto (DEC)** nella fase esecutiva dei **contratti
  pubblici**, ai sensi dell'**art. 114 del D.Lgs. 31 marzo 2023, n. 36** (Codice dei contratti
  pubblici), nell'area `appalti-opere-pubbliche`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.Lgs. 31 marzo 2023, n. 36** - indice Normattiva pinnato `!vig=2026-07-17`
    SHA256: 0e9a193836e379cb33cb6daf1a5a988c608eb9559d84b91a841d9ed9791a62af
    (codice 23G00044). Art. 114 via `caricaArticolo` (versione 2, idGruppo 18).
  - Trascrizione verbatim in `references/fonti/dlgs-36-2023-art114.md`: art. 114 per intero
    (commi 1-10).
- Estratto operativo `references/estratti/direzione-lavori-checklist.md`.
- Due task: `inquadra-direzione-lavori.md` e `inquadra-direzione-esecuzione.md`.
- Due esempi: nomina del DL e DL come coordinatore sicurezza in esecuzione per lavori <= 1
  milione; DEC di norma dal RUP nei servizi e casi di DEC diverso dal RUP.

### Contenuto ancorato al testo
- Esecuzione diretta dal RUP che si avvale di DEC/DL, coordinatore sicurezza e collaudatore/
  verificatore (c. 1); per i lavori: nomina prima dell'avvio della procedura su proposta del RUP
  e ufficio di direzione lavori (c. 2), controllo tecnico/contabile/amministrativo (c. 3), DL
  come CSE per contratti <= 1 milione senza lavori complessi/interferenze (c. 4), affidamento a
  dipendenti PA o esterno (c. 6); per servizi e forniture: DEC di norma dal RUP (c. 7), allegato
  II.14 per i contratti con DEC diverso dal RUP (c. 8), assistenti (c. 10); rinvii agli allegati
  II.14 e I.9 (c. 5, con periodo soppresso dal D.Lgs. 209/2024) e al comma 6 (c. 9).

### Scope e limiti
- Non nomina il DL/DEC, non redige gli atti della direzione lavori/esecuzione, non sostituisce
  la stazione appaltante ne' il RUP. Non riproduce gli allegati II.14 e I.9 ne' gli articoli
  richiamati (art. 15 RUP, art. 116 collaudo, D.Lgs. 81/2008, art. 15 L. 241/1990, art. 30
  D.Lgs. 267/2000).

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del D.Lgs. 36/2023 pinnato (nuovo
  hash) e verificare le modifiche dei decreti correttivi (es. D.Lgs. 209/2024) segnalate dai
  doppi tondi `(( ))` e dall'indicazione del periodo soppresso.
- Validazione Livello 2 con esperto di contrattualistica pubblica / RUP.
