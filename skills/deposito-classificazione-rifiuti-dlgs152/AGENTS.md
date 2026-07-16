# AGENTS.md - deposito-classificazione-rifiuti-dlgs152

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale alla **classificazione dei rifiuti** e al **deposito temporaneo prima della
raccolta**: definizioni, classificazione (urbani/speciali, pericolosi/non pericolosi) e condizioni/
limiti del deposito temporaneo, secondo gli **artt. 183, 184, 185-bis del D.Lgs. 3 aprile 2006, n.
152** (Parte quarta). Target: ingegneri, produttori di rifiuti, consulenti ambientali.

**E' una skill documentale**: inquadra classificazione e deposito; **non attribuisce** i codici
EER, **non redige** registri/FIR, non sostituisce produttore/detentore ne' consulente.

## Nota sull'area e sulla complementarita'

Area **ambiente-territorio-mobilita**. Complementare e distinta da `trasporto-rifiuti-fir-dlgs152`
(FIR/trasporto), `terre-rocce-scavo-dpr120` (terre da scavo) e `bonifica-siti-contaminati-dlgs152`
(bonifica): questa copre **classificazione** e **deposito temporaneo**.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-152-2006-artt-183-184-185bis**: D.Lgs. 3 aprile 2006, n. 152, pagina indice Normattiva
  pinnata a `!vig=2026-07-16` (hash `fac1fb98...`; codice 006G0171). Artt. 183 (v17), 184 (v9),
  185-bis (idSottoArticolo 2, v2), idGruppo 34, caricati via `caricaArticolo` e trascritti verbatim.

Trascrizione in `references/fonti/dlgs-152-2006-artt-183-184-185bis.md`; estratto operativo in
`references/estratti/rifiuti-checklist.md`.

## Punti chiave (verificati sul testo)

- **Classificazione** (art. 184): **urbani/speciali** (origine) e **pericolosi/non pericolosi**
  (allegato I); **EER allegato D** vincolante per i pericolosi; **codici a cura del produttore**
  (Linee guida SNPA); **divieto di declassificazione** per diluizione/miscelazione (c. 5-ter).
- **Deposito temporaneo** (art. 185-bis): nel **luogo di produzione**; avvio a recupero/smaltimento
  con **cadenza trimestrale** oppure a **30 mc (max 10 mc pericolosi)**; se sotto il limite/anno
  durata **max 1 anno**; **categorie omogenee**; **non necessita di autorizzazione** (c. 3).

## Convenzioni specifiche

### Cosa NON fare
- Non **attribuire i codici EER** ne' riprodurre l'allegato D / l'allegato I: rinviarvi.
- Non **redigere** registri (art. 190), FIR (art. 193), MUD: rinviare a `trasporto-rifiuti-fir-dlgs152`.
- Non inventare **limiti** (usare 30/10 mc, trimestrale, 1 anno come da testo).

### Cosa fare
- **Classificare** il rifiuto (origine + pericolosita') con rinvio all'EER; **impostare** le
  condizioni e i limiti del deposito temporaneo.

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.Lgs. 152/2006 pinnato a nuovo `!vig=` (nuovo hash) e
rileggere artt. 183/184/185-bis, verificando le modifiche (es. D.Lgs. 116/2020 nozione di rifiuto
urbano; testo tra `(( ))`).

## Validatori

- Non ancora assegnato (Livello 2 con tecnico ambientale / consulente rifiuti).

## Stato attuale

- Versione: 0.1.0-alpha (closes #278)
- Task files: 2 (`classifica-rifiuto.md`, `imposta-deposito-temporaneo.md`)
- Esempi: 2 (rifiuti da costruzione e demolizione: speciali; deposito temporaneo di rifiuti pericolosi)
