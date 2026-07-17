# AGENTS.md - contributo-costruzione-dpr380

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale all'inquadramento del **contributo di costruzione** dovuto per il
**permesso di costruire** (e gli altri titoli edilizi onerosi): oneri di urbanizzazione + costo
di costruzione, rateizzazione e scomputo, riduzioni ed esoneri, convenzione-tipo, opere non
residenziali. Fonte: **D.P.R. 380/2001 (T.U. Edilizia), artt. 16-19**. Target: ingegneri,
architetti, geometri, uffici SUE.

**E' una skill documentale**: inquadra quadro, voci ed esoneri; **non calcola gli importi**
(demandati a tabelle regionali e deliberazioni comunali) e non sostituisce l'ufficio tecnico
comunale.

## Nota sull'area e sulla complementarita'

Area **edilizia-urbanistica-catasto**. Complementare a `modulistica-edilizia-unificata` (quale
modulo/regime dell'intervento) e `regimi-suap-attivita-produttive-dlgs222`: questa copre
l'**onerosita'** del titolo edilizio (artt. 16-19 T.U.).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dpr-380-2001-contributo**: D.P.R. 6 giugno 2001, n. 380, indice Normattiva pinnato
  `!vig=2026-07-16` (hash `98a209da...`, codice 001G0429). Artt. 16-19 (testo vigente) via
  `caricaArticolo`, trascritti verbatim.

Trascrizione in `references/fonti/dpr-380-2001-artt16-19.md`; estratto in
`references/estratti/contributo-costruzione-checklist.md`.

## Punti chiave (verificati sul testo)

- **Art. 16**: contributo = **oneri di urbanizzazione** + **costo di costruzione**; oneri al
  rilascio (rateizzabili) o **scomputo** con esecuzione diretta delle opere; costo di costruzione
  **in corso d'opera** entro **60 gg** dall'ultimazione; **tabelle parametriche regionali** e
  deliberazione comunale (cc. 4-9).
- **Art. 17**: riduzione (convenzionata -> solo oneri; prima abitazione); **esonero** (agricole;
  ristrutturazione/ampliamento <= 20% di **unifamiliari**; opere pubbliche/di interesse generale;
  calamita'; fonti rinnovabili/risparmio energetico); immobili dello Stato / manutenzione
  straordinaria con aumento del carico urbanistico -> solo oneri.
- **Art. 18**: convenzione-tipo regionale.
- **Art. 19**: opere non residenziali (industriali/artigianali; turistiche/commerciali/direzionali
  con quota <= 10% del costo di costruzione).

## Convenzioni specifiche

### Cosa NON fare
- Non **calcolare gli importi** ne' riprodurre tabelle degli oneri/costo di costruzione: sono di
  regioni e comuni. Non inventare valori.
- Non trattare come esaustiva la disciplina: rateizzazione, garanzie, monetizzazioni e SCIA
  onerosa sono anche **regionali/comunali**.

### Cosa fare
- Inquadrare se/quanto e' dovuto (oneri e/o costo di costruzione), riduzioni/esoneri, e impostare
  rateizzazione/scomputo e tempi.

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.P.R. 380/2001 pinnato a nuovo `!vig=` (nuovo hash) e
rileggere gli artt. 16-19 (soggetti a modifiche frequenti), verificando le versioni vigenti.

## Validatori

- Non ancora assegnato (Livello 2 con funzionario SUE / esperto oneri edilizi).

## Stato attuale

- Versione: 0.1.0-alpha (closes #257)
- Task files: 2 (`inquadra-contributo.md`, `gestisci-oneri-scomputo.md`)
- Esempi: 2 (ampliamento <= 20% unifamiliare - esonero; capannone industriale - art. 19)
