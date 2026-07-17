# deposito-classificazione-rifiuti-dlgs152

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con tecnico ambientale / consulente rifiuti da completare)

Skill di **supporto documentale** alla **classificazione dei rifiuti** e al **deposito temporaneo
prima della raccolta**: definizioni, classificazione (urbani/speciali, pericolosi/non pericolosi)
e condizioni/limiti del deposito temporaneo, secondo gli **artt. 183, 184, 185-bis del D.Lgs. 3
aprile 2006, n. 152** (Parte quarta).

**Non attribuisce i codici EER**, **non redige** registri/FIR e **non sostituisce** il
produttore/detentore né il consulente: inquadra classificazione e deposito.

## Target

Ingegneri, produttori di rifiuti e consulenti ambientali che devono classificare un rifiuto o
impostare il deposito temporaneo.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `classifica-rifiuto` | Classifica il rifiuto per origine (urbano/speciale) e pericolosità (pericoloso/non pericoloso), con il rinvio all'EER e alle linee guida |
| `imposta-deposito-temporaneo` | Imposta condizioni, limiti (30/10 mc, trimestrale, 1 anno) e modalità del deposito temporaneo prima della raccolta |

Nucleo: **definizioni** (art. 183), **classificazione** (art. 184: urbani/speciali, pericolosi/non
pericolosi, **EER allegato D** vincolante, codici a cura del produttore, divieto di
declassificazione), **deposito temporaneo** (art. 185-bis: luogo di produzione, avvio con
**cadenza trimestrale** o a **30 mc** di cui max **10 mc pericolosi**, durata max **1 anno**,
categorie omogenee, **senza autorizzazione**).

## Fonti consultate

- **D.Lgs. 3 aprile 2006, n. 152** (Parte quarta) - artt. 183, 184, 185-bis - testo vigente su
  Normattiva (indice pinnato a `!vig=2026-07-16`, codice 006G0171)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non attribuisce i codici EER** né esegue la caratterizzazione analitica: rinvio all'allegato
  D, all'allegato I (HP) e alle Linee guida SNPA.
- **Non redige** registri (art. 190), FIR (art. 193) né MUD: per il trasporto vedi
  `trasporto-rifiuti-fir-dlgs152`.
- **Non sostituisce** il produttore/detentore né il consulente; non tratta le autorizzazioni alla
  gestione (artt. 208 e ss.) se non come richiamo.

**La skill è un supporto documentale: non sostituisce il produttore/detentore né il consulente,
né la lettura degli artt. 183/184/185-bis del D.Lgs. 152/2006 e degli allegati richiamati.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
