# condominio-parti-comuni-assemblea-cc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con avvocato civilista / amministratore di condominio da completare)

Skill di **supporto documentale** al **condominio negli edifici**: parti comuni, innovazioni
(ordinarie/agevolate) e costituzione dell'assemblea con quorum e maggioranze delle deliberazioni,
secondo il **Codice civile, artt. 1117, 1120, 1136**.

**Non redige** verbali/delibere, **non valuta** validità/impugnazione (art. 1137), **non tratta** le
tabelle millesimali e **non sostituisce** l'amministratore, il legale o il giudice: inquadra parti
comuni, innovazioni e maggioranze.

## Target

Ingegneri e architetti (progettisti di interventi su parti comuni, amministratori, CTU condominiali).

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-parti-innovazione` | Individua se un bene è parte comune (art. 1117) e classifica l'innovazione ordinaria/agevolata con la maggioranza (art. 1120) |
| `verifica-quorum-assemblea` | Verifica i quorum costitutivi/deliberativi (1ª/2ª convocazione) e la maggioranza per la specifica delibera (art. 1136) |

Nucleo: **parti comuni** (art. 1117); **innovazioni** ordinarie (2/3 del valore) e agevolate (metà del
valore) (art. 1120); **assemblea** con quorum e maggioranze (art. 1136).

## Fonti consultate

- **Codice civile** (R.D. 262/1942) - artt. 1117, 1120, 1136 - testo vigente su Normattiva (indice
  pinnato a `!vig=2026-07-17`, codice 042U0262)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non redige** verbali/convocazioni né delibere; non compila le **tabelle millesimali**.
- **Non valuta** la **validità** o l'**impugnazione** della delibera (art. 1137) né la ripartizione
  delle spese (artt. 1123-1126).
- **Non risolve** il caso concreto (interpretazione del titolo, uso esclusivo, distacco impianti) né
  fornisce consulenza legale.
- **Non sostituisce** l'amministratore, il legale o il giudice.

**La skill è un supporto documentale: non sostituisce l'amministratore, il legale né il giudice, né la
lettura degli artt. 1117/1120/1136 del Codice civile.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
