# AGENTS.md - classificazione-rifiuti-dlgs152

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **tecnico ambientale**, all'**RSGA** e al **produttore/detentore** per la
**classificazione dei rifiuti** (urbani/speciali, pericolosi/non pericolosi) e l'attribuzione dei
**codici EER**, ai sensi del **D.Lgs. 3 aprile 2006, n. 152, Parte IV, artt. 183 (definizioni) e 184
(classificazione)**. Target: tecnici ambientali, RSGA, produttori/detentori.

**E' una skill documentale per il tecnico**: inquadra definizioni e criteri; **non attribuisce** il
codice EER ne' la classe di pericolo del singolo rifiuto, **non redige** l'analisi di caratterizzazione
ne' compila registri/FIR/MUD.

## Nota sull'area e sulla complementarita'

Area **ambiente-territorio-mobilita**. Distinta da `sottoprodotti-end-of-waste-dlgs152` (artt.
184-bis/ter: quando un materiale **non e'** o **cessa** di essere rifiuto) e da `terre-rocce-scavo-dpr120`
(gestione delle terre): questa copre la **classificazione** del rifiuto (a monte della gestione).
Complementare, per la parte gestionale, al deposito temporaneo (art. 185-bis, rinvio) e agli obblighi di
tracciabilita' (registro, FIR, MUD - non trattati).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-152-2006-183-184**: D.Lgs. 152/2006, pagina indice Normattiva pinnata a `!vig=2026-07-17` (hash
  `c2175fe5...`; codice 006G0171, idGruppo 34, dataPubblicazioneGazzetta 2006-04-14). Artt. 183 (v17,
  solo lettere rilevanti) e 184 (v9, cc. 1-5) caricati via `caricaArticolo` (formato AKN) e trascritti
  verbatim.

Trascrizione in `references/fonti/dlgs-152-2006-183-184.md`; estratto operativo in
`references/estratti/classificazione-rifiuti-checklist.md`.

## Punti chiave (verificati sul testo)

- **Rifiuto** (art. 183, lett. a); **produttore** iniziale/nuovo (lett. f); **detentore** (lett. h);
  **deposito temporaneo prima della raccolta** (lett. bb, ex art. 185-bis).
- **Due assi** (art. 184, c. 1): **origine** (urbani/speciali) e **pericolosita'**.
- **Urbani** (c. 2; art. 183 lett. b-ter): domestici e **simili** (All. L-quater/L-quinquies).
  **Speciali** (c. 3): C&D e scavo, industriali, artigianali, commerciali, di servizio, fanghi, sanitari,
  veicoli fuori uso.
- **Pericolosi** (c. 4): caratteristiche **Allegato I** (HP 1-15); **elenco EER (Allegato D)**
  vincolante, **voci a specchio** (c. 5); **codice attribuito dal produttore** con **Linee guida SNPA**.

## Convenzioni specifiche

### Cosa NON fare
- Non **attribuire** il codice **EER** ne' la classe **HP** del singolo rifiuto; non **redigere**
  l'analisi di caratterizzazione ne' compilare **registro/FIR/MUD**.
- Non riprodurre gli **Allegati D/I/L-quater/L-quinquies** ne' le **Linee guida SNPA**: rinvio.
- Non trattare il **deposito temporaneo** (art. 185-bis), i **sottoprodotti/EoW** (184-bis/ter) ne' le
  **terre e rocce da scavo** (DPR 120/2017): rinvio alle skill/temi dedicati.

### Cosa fare
- Stabilire se e' rifiuto (183), classificarlo per origine (184 cc. 1-3) e pericolosita' (184 cc. 4-5),
  inquadrando l'elenco EER e il ruolo del produttore.

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.Lgs. 152/2006 pinnato a nuovo `!vig=` (nuovo hash) e rileggere gli
artt. 183-184, verificando le modifiche dei doppi tondi `(( ))` (es. D.Lgs. 116/2020, dir. 2018/851).

## Validatori

- Non ancora assegnato (Livello 2 con tecnico ambientale/chimico).

## Stato attuale

- Versione: 0.1.0-alpha (closes #360)
- Task files: 2 (`inquadra-origine-rifiuto.md`, `inquadra-pericolosita-codice.md`)
- Esempi: 2 (rifiuti da C&D e barattoli di vernice: origine e pericolosita'; rifiuti d'ufficio: urbani
  per similarita' vs speciali)
