# CHANGELOG - regimi-suap-attivita-produttive-dlgs222

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-16

### Added (closes #245)
- Prima versione della skill di supporto all'**individuazione del regime amministrativo**
  (comunicazione, SCIA, SCIA unica, SCIA condizionata, silenzio-assenso, autorizzazione)
  delle **attivita' private produttive/commerciali** presso il **SUAP**, ai sensi del
  **D.Lgs. 222/2016 ("SCIA 2")** e della sua **Tabella A**, nell'area
  `edilizia-urbanistica-catasto`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.Lgs. 25 novembre 2016, n. 222** - indice Normattiva pinnato `!vig=2026-07-16`
    SHA256: 7169e0b71d554d6aee1d2d7144dbc23570e671cf60a9ad96ddce3f40904b90a2
    (codice 16G00237). Articoli e Tabella A via `caricaArticolo`.
  - Trascrizione verbatim in `references/fonti/dlgs-222-2016.md`: art. 1 (oggetto), art. 2
    (regimi amministrativi; rinvio alla Tabella A), art. 5 (livelli ulteriori di
    semplificazione), legenda ed estratto rappresentativo della Tabella A.
- Estratto operativo `references/estratti/regimi-suap-checklist.md`.
- Due task: `individua-regime-attivita.md` e `gestisci-scia-unica-condizionata.md`.
- Due esempi: attivita' non elencata nella Tabella A (art. 2, c. 6); SCIA unica vs SCIA
  condizionata con prevenzione incendi (art. 19-bis, cc. 2 e 3 L. 241/1990).

### Contenuto ancorato al testo
- Art. 2, c. 1 (regime dalla Tabella A); c. 2 (comunicazione); c. 3 (SCIA/art. 19, SCIA
  unica/art. 19-bis c. 2, SCIA condizionata/art. 19-bis c. 3); c. 5 (autorizzazione/art.
  20); c. 6 (attivita' non elencate). Art. 5 (livelli ulteriori). Legenda Tabella A per
  effetti e tempi (controlli 60/30 gg; Conferenza di servizi entro 5 gg).

### Scope e limiti
- Non riproduce la Tabella A attivita' per attivita' (~245 KB): il regime esatto va letto
  sulla Tabella A dell'atto. Non sostituisce il SUAP. Non copre la parte edilizia
  (complementare a `modulistica-edilizia-unificata`).

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del D.Lgs. 222/2016 pinnato
  (nuovo hash) e verificare gli aggiornamenti periodici della Tabella A (art. 2, c. 7).
- Validazione Livello 2 con operatore SUAP / esperto semplificazione.
