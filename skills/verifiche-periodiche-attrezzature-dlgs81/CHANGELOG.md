# CHANGELOG - verifiche-periodiche-attrezzature-dlgs81

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-16

### Added (closes #266)
- Prima versione della skill di supporto al regime dei **controlli** e delle **verifiche
  periodiche** delle **attrezzature di lavoro**, ai sensi dell'**art. 71 e dell'Allegato VII
  del D.Lgs. 9 aprile 2008, n. 81**, nell'area `impianti-macchine-prodotti`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.Lgs. 9 aprile 2008, n. 81** - indice Normattiva pinnato `!vig=2026-07-16`
    SHA256: d89919850537a55286cc55ce7d2bff1aaa316b670d0072a475370176de830831
    (codice 008G0104). Art. 71 via `caricaArticolo` (versione 6, idGruppo 15).
  - Trascrizione verbatim in `references/fonti/dlgs-81-2008-art71-allegatoVII.md`: art. 71 per
    intero (commi 1-14) e la parte testuale disponibile dell'Allegato VII (nota di
    aggiornamento L. 34/2026).
- Estratto operativo `references/estratti/verifiche-attrezzature-checklist.md`.
- Due task: `inquadra-regime-attrezzatura.md` e `imposta-verifiche-periodiche.md`.
- Due esempi: gru a torre (verifiche periodiche Allegato VII); trapano da banco (soli controlli).

### Contenuto ancorato al testo
- Controlli iniziali/periodici/straordinari da persona competente, verbali conservati almeno
  tre anni (c. 8-10); verifiche periodiche delle attrezzature dell'Allegato VII (c. 11: prima
  verifica INAIL entro 45 giorni, successive ASL/ARPA o soggetti abilitati, oneri a carico del
  datore); soggetti privati abilitati incaricati di pubblico servizio (c. 12); rinvio al DM
  11/4/2011 (c. 13); VVF (c. 13-bis); aggiornamento dell'elenco (c. 14).

### Scope e limiti
- Non riproduce l'Allegato VII (elenco attrezzature e periodicita', in formato grafico su
  Normattiva): rinvio all'atto e al DM 11/4/2011. Non esegue le verifiche/controlli, non redige
  i verbali, non sostituisce INAIL/ASL/ARPA/soggetti abilitati ne' il datore di lavoro.

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del D.Lgs. 81/2008 pinnato (nuovo
  hash) e verificare le modifiche all'elenco dell'Allegato VII (aggiornato con decreto ex c.
  14; es. L. 34/2026).
- Validazione Livello 2 con esperto di sicurezza / verificatore abilitato.
