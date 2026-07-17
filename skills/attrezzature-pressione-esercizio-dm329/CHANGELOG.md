# CHANGELOG - attrezzature-pressione-esercizio-dm329

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-16

### Added (closes #283)
- Prima versione della skill di supporto alla **messa in servizio** e alle **verifiche** delle
  **attrezzature e insiemi a pressione in esercizio** (fase post-marcatura CE), ai sensi del **D.M.
  1 dicembre 2004, n. 329** (artt. 1, 4, 5, 6, 10, 11, 13), nell'area `impianti-macchine-prodotti`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.M. 1 dicembre 2004, n. 329** - indice Normattiva pinnato `!vig=2026-07-16`
    SHA256: 5ee937bbc215f3a35f6e585e8eff0aad8d0dd1790adae26bc979a860542c93eb
    (codice 005G0017). Artt. 1, 4, 5, 6, 10, 11, 13 via `caricaArticolo` (idGruppo 0).
  - Trascrizione verbatim in `references/fonti/dm-329-2004-artt-1-4-5-6-10-11-13.md`.
- Estratto operativo `references/estratti/attrezzature-pressione-checklist.md`.
- Due task: `imposta-messa-in-servizio.md` e `imposta-riqualificazione-periodica.md`.
- Due esempi: messa in servizio di un serbatoio GPL (verifica art. 4 + dichiarazione art. 6 con
  cumulativa per serie); esenzione dalla riqualificazione periodica (art. 11, calcolo PS/PS·V).

### Contenuto ancorato al testo
- Art. 1 campo di applicazione e tipi di verifica; art. 4 verifica di primo impianto/messa in
  servizio (installazione dall'utilizzatore, attestazione, divieto se esito negativo); art. 5
  esclusioni; art. 6 dichiarazione di messa in servizio a ISPESL(INAIL)+ASL con contenuti a-e e
  cumulativa per serie GPL ≤ 13 m³ / criogenici ≤ 35 m³; art. 10 riqualificazione periodica
  (integrità + funzionamento, periodicità allegati A/B, deroghe ministeriali); art. 11 esenzioni
  (soglie PS/PS·V); art. 13 verifica di funzionamento (accessori di sicurezza, taratura valvole).

### Scope e limiti
- Non esegue le verifiche né rilascia attestazioni/verbali (INAIL/ASL/soggetti abilitati). Non
  redige la dichiarazione di messa in servizio. Non riproduce le tabelle degli allegati A e B né
  gli articoli non trascritti (artt. 2, 3, 12). Distinta dalla marcatura CE (D.Lgs. 93/2000 →
  `ped-classificazione-conformita`) e dalle verifiche periodiche ex art. 71 D.Lgs. 81/2008 (→
  `verifiche-periodiche-attrezzature-dlgs81`). ISPESL soppresso, funzioni all'INAIL (D.L. 78/2010).

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del D.M. 329/2004 pinnato (nuovo hash) e
  rileggere gli articoli.
- Validazione Livello 2 con tecnico della sicurezza / verificatore INAIL-ASL.
