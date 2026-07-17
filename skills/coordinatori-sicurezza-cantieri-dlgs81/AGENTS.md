# AGENTS.md - coordinatori-sicurezza-cantieri-dlgs81

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al regime dei **cantieri temporanei o mobili** (Titolo IV): definizioni,
obblighi del **committente/responsabile dei lavori**, obblighi del **coordinatore per la
progettazione (CSP)** e del **coordinatore per l'esecuzione (CSE)**, secondo gli **artt. 89-92
del D.Lgs. 9 aprile 2008, n. 81**. Target: ingegneri, committenti, responsabili dei lavori,
coordinatori per la sicurezza.

**E' una skill documentale**: inquadra ruoli/nomine/obblighi; **non nomina** i coordinatori,
**non redige** PSC/POS/fascicolo, non sostituisce committente/CSP/CSE ne' organo di vigilanza.

## Nota sull'area e sulla complementarita'

Area **sicurezza-lavoro-cantieri**. Complementare e distinta da `pos-allegato-xv-checker` (POS,
art. 96 + Allegato XV) e `duvri-interferenze-dlgs81` (appalti NON Titolo IV, art. 26): questa
copre la **gestione del cantiere Titolo IV** (committente, CSP, CSE, PSC/fascicolo).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-81-2008-titolo4-artt-89-92**: D.Lgs. 9 aprile 2008, n. 81, pagina indice Normattiva
  pinnata a `!vig=2026-07-16` (hash `d8991985...`; codice 008G0104). Artt. 89 (v2), 90 (v5), 91
  (v5), 92 (v2), idGruppo 18, caricati via `caricaArticolo` e trascritti verbatim.

Trascrizione in `references/fonti/dlgs-81-2008-titolo4-artt-89-92.md`; estratto operativo in
`references/estratti/coordinatori-cantieri-checklist.md`.

## Punti chiave (verificati sul testo)

- **Definizioni** (art. 89): cantiere (allegato X), committente, responsabile dei lavori, CSP,
  CSE (incompatibilita': non datore/dipendente/RSPP delle esecutrici), imprese affidataria/
  esecutrice, uomini-giorno, POS.
- **Committente** (art. 90): **CSP** contestuale alla progettazione e **CSE** prima
  dell'affidamento quando **piu' imprese** (anche non contemporanee); verifica idoneita'
  (all. XVII), DURC, patente (art. 27); notifica preliminare (art. 99); **sospensione del titolo**
  in assenza di PSC/fascicolo/notifica/DURC (c. 10); esonero lavori privati < 100.000 euro (c. 11).
- **CSP** (art. 91): **PSC** (art. 100/all. XV) + **fascicolo** (all. XVI).
- **CSE** (art. 92): verifica PSC/POS, coordinamento, contestazione e proposta di sospensione,
  **sospensione diretta** in pericolo grave e imminente.

## Convenzioni specifiche

### Cosa NON fare
- Non **nominare** i coordinatori ne' verificarne i requisiti (art. 98).
- Non **redigere** PSC/POS/fascicolo ne' riprodurre gli allegati (X, XV, XVI, XVII): rinviare a
  `pos-allegato-xv-checker` e agli atti.
- Non inventare **soglie** (usare 200 uomini-giorno e 100.000 euro come da testo).

### Cosa fare
- Stabilire **quando** nominare CSP/CSE, impostare le **verifiche del committente** e i casi di
  **sospensione del titolo**, e inquadrare gli obblighi di **CSP** e **CSE**.

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.Lgs. 81/2008 pinnato a nuovo `!vig=` (nuovo hash) e
rileggere artt. 89-92, verificando le modifiche (es. patente a crediti art. 27 DL 146/2021;
testo tra `(( ))`).

## Validatori

- Non ancora assegnato (Livello 2 con CSP/CSE esperto / RSPP di settore edile).

## Stato attuale

- Versione: 0.1.0-alpha (closes #277)
- Task files: 2 (`verifica-obbligo-coordinatori.md`, `obblighi-committente-cantiere.md`)
- Esempi: 2 (ristrutturazione con due imprese -> CSP/CSE; piccolo lavoro privato < 100.000 euro)
