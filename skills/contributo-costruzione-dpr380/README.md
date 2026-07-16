# contributo-costruzione-dpr380

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con funzionario SUE / esperto oneri edilizi da completare)

Skill di **supporto documentale** all'inquadramento del **contributo di costruzione** dovuto per
il **permesso di costruire** (e gli altri titoli edilizi onerosi): **oneri di urbanizzazione** +
**costo di costruzione**, riduzioni ed esoneri, convenzione-tipo, opere non residenziali, secondo
il **T.U. Edilizia (D.P.R. 380/2001), artt. 16-19**.

**Non calcola gli importi** (demandati a tabelle regionali e deliberazioni comunali) e **non
sostituisce** l'ufficio tecnico comunale: inquadra quadro, voci ed esoneri.

## Target

Ingegneri, architetti, geometri e uffici **SUE** che devono inquadrare l'onerosità di un titolo
edilizio.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-contributo` | Stabilisce se il contributo è dovuto e in che misura (oneri + costo di costruzione), con riduzioni ed esoneri |
| `gestisci-oneri-scomputo` | Imposta rateizzazione, scomputo con esecuzione diretta delle opere di urbanizzazione e tempi di corresponsione |

Nucleo: composizione del contributo (art. 16), rateizzazione/scomputo e tempi, riduzioni ed
esoneri (art. 17), convenzione-tipo (art. 18), opere non residenziali (art. 19).

## Fonti consultate

- **D.P.R. 6 giugno 2001, n. 380** (T.U. Edilizia) - artt. 16, 17, 18, 19 - testo vigente su
  Normattiva (indice pinnato a `!vig=2026-07-16`, codice 001G0429)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non calcola gli importi**: le tabelle degli oneri e i valori del costo di costruzione sono di
  **regioni e comuni** (deliberazioni comunali su tabelle regionali).
- **Non sostituisce** l'ufficio tecnico comunale (SUE) né il computo del contributo.
- **Non copre** la disciplina regionale/comunale di dettaglio (rateizzazione, garanzie,
  monetizzazioni, SCIA onerosa).

**La skill è un supporto documentale: non sostituisce l'ufficio tecnico comunale, il calcolo del
contributo né la lettura del D.P.R. 380/2001 e della normativa regionale/comunale applicabile.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
