# AGENTS.md - regimi-suap-attivita-produttive-dlgs222

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale all'**individuazione del regime amministrativo** (comunicazione,
SCIA, SCIA unica, SCIA condizionata, silenzio-assenso, autorizzazione) applicabile alle
**attivita' private produttive/commerciali** presso il **SUAP**, sulla base del **D.Lgs.
222/2016 ("SCIA 2")** e della sua **Tabella A**. Target: ingegneri, geometri, consulenti,
operatori SUAP/SUE.

**E' una skill documentale**: inquadra il **metodo di lettura** della Tabella A e gli
effetti/tempi dei regimi; **non riproduce la Tabella A attivita' per attivita'** e non
sostituisce la valutazione del SUAP.

## Nota sull'area e sulla complementarita'

Area **edilizia-urbanistica-catasto**. Complementare a `modulistica-edilizia-unificata`
(che usa lo stesso D.Lgs. 222/2016 Tabella A ma per la **parte edilizia**, gli interventi
DPR 380/2001 e la modulistica unificata): questa skill copre la **parte attivita'
produttive/commerciali** dei regimi del SUAP.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-222-2016**: D.Lgs. 25 novembre 2016, n. 222, pagina indice Normattiva pinnata a
  `!vig=2026-07-16` (hash `7169e0b7...`; codice 16G00237). Articoli e Tabella A caricati
  via `caricaArticolo` (AJAX) e trascritti verbatim: art. 1 (oggetto), art. 2 (regimi
  amministrativi; rinvio alla Tabella A), art. 5 (livelli ulteriori), legenda ed estratto
  rappresentativo della Tabella A.

Trascrizione in `references/fonti/dlgs-222-2016.md`; estratto operativo in
`references/estratti/regimi-suap-checklist.md`.

## Punti chiave (verificati sul testo)

- **Art. 2, c. 1**: a ciascuna attivita' della Tabella A si applica il **regime ivi
  indicato**.
- **Comunicazione** (c. 2): effetto con la **presentazione** (anche comunicazione unica
  ex art. 19-bis).
- **SCIA** (c. 3 -> art. 19): avvio immediato, controlli **60 gg (30 edilizia)**.
- **SCIA unica** (art. 19-bis, c. 2): un'unica SCIA allo Sportello, che trasmette.
- **SCIA condizionata** (art. 19-bis, c. 3): Conferenza di servizi **entro 5 gg**, avvio
  **subordinato** al rilascio delle autorizzazioni.
- **Autorizzazione** (c. 5 -> art. 20): provvedimento espresso, salvo **silenzio-assenso**.
- **Attivita' non elencate** (c. 6): ricondotte alla corrispondente, **pubblicate sul
  sito** dell'ente.
- **Art. 5**: livelli ulteriori di semplificazione di regioni/enti locali.

## Convenzioni specifiche

### Cosa NON fare
- Non **riprodurre la Tabella A attivita' per attivita'** (~245 KB): il regime esatto va
  letto sulla Tabella A dell'atto.
- Non **classificare in modo definitivo** la singola attivita' al posto del SUAP.
- Non trattare la **parte edilizia** (rinvio a `modulistica-edilizia-unificata`).

### Cosa fare
- Impostare la **lettura della Tabella A** (art. 2, c. 1) e inquadrare effetti/tempi dei
  regimi; gestire attivita' non elencate (c. 6) e livelli ulteriori (art. 5).

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.Lgs. 222/2016 pinnato a nuovo `!vig=` (nuovo hash)
e rileggere artt. 1, 2, 5 e la Tabella A, verificando gli **aggiornamenti** della Tabella A
(art. 2, c. 7: integrazioni con decreti correttivi e aggiornamenti periodici).

## Validatori

- Non ancora assegnato (Livello 2 con operatore SUAP / esperto semplificazione).

## Stato attuale

- Versione: 0.1.0-alpha (closes #245)
- Task files: 2 (`individua-regime-attivita.md`, `gestisci-scia-unica-condizionata.md`)
- Esempi: 2 (attivita' non elencata; SCIA unica vs SCIA condizionata / prevenzione incendi)
