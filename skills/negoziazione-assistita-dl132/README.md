# negoziazione-assistita-dl132

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con avvocato civilista da completare)

Skill di **supporto documentale** al procedimento di **negoziazione assistita da
avvocati**: convenzione, condizione di procedibilità, invito e mancato accordo,
esecutività dell'accordo, secondo il **D.L. 132/2014 (conv. L. 162/2014), artt. 2-5**.

**Non redige** la convenzione/invito/accordo, **non fornisce** consulenza legale e
**non sostituisce** l'avvocato o il giudice: inquadra requisiti, casi di procedibilità
ed effetti.

## Target

Avvocati, ingegneri/tecnici parti di una controversia e CTU che devono inquadrare lo
strumento ADR.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `verifica-condizione-procedibilita` | Verifica se la controversia rientra tra i casi di condizione di procedibilità (art. 3), con esclusioni, effetti e rilievo |
| `inquadra-convenzione-accordo` | Inquadra i requisiti della convenzione (art. 2), l'invito e il mancato accordo (art. 4) e gli effetti dell'accordo (art. 5) |

Nucleo: **convenzione** (art. 2 - termine 1-3 mesi, forma scritta, un avvocato per
parte); **condizione di procedibilità** (art. 3 - danni da circolazione, pagamenti ≤
50.000 €); **invito/mancato accordo** (art. 4); **esecutività dell'accordo** (art. 5 -
titolo esecutivo).

## Fonti consultate

- **D.L. 12/9/2014 n. 132** (conv. **L. 162/2014**) - artt. 2, 3, 4, 5 - testo vigente
  su Normattiva (indice pinnato a `!vig=2026-07-17`, codice 14G00147)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non redige** la convenzione, l'invito, l'accordo né gli atti del procedimento.
- **Non valuta** la fondatezza della pretesa, la strategia processuale né
  l'ammissibilità del caso concreto.
- **Non tratta** la negoziazione assistita in materia di **famiglia** (art. 6) né gli
  obblighi antiriciclaggio/raccolta dati (artt. 9-11), né la **mediazione civile**
  (D.Lgs. 28/2010).
- **Non sostituisce** l'avvocato né il giudice.

**La skill è un supporto documentale: non sostituisce l'avvocato né il giudice, né la
lettura degli artt. 2-5 del D.L. 132/2014 (conv. L. 162/2014).**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
