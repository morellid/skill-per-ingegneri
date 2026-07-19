# offerte-anomale-congruita-dlgs36

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con RUP / esperto di contratti pubblici da completare)

Skill di **supporto documentale** al **RUP** e alla **commissione giudicatrice/seggio di gara** per
l'inquadramento della **verifica delle offerte anormalmente basse** (giudizio di congruità) e
dell'**esclusione automatica** delle offerte anomale nei contratti pubblici, ai sensi del **D.Lgs. 31
marzo 2023, n. 36 (Codice dei contratti pubblici), artt. 110 e 54** (con l'art. 108, comma 9).

**Non calcola** la soglia di anomalia né **applica** i metodi dell'Allegato II.2, **non redige** gli atti
e **non sostituisce** il RUP o la stazione appaltante: inquadra il procedimento, i termini e i casi di
esclusione.

## Target

RUP, commissioni giudicatrici, uffici gare e tecnici delle stazioni appaltanti che devono inquadrare la
verifica di congruità e l'esclusione automatica delle offerte anomale.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-verifica-congruita` | Presupposto, richiesta di spiegazioni, giustificazioni e casi di esclusione delle offerte anormalmente basse (art. 110) |
| `inquadra-esclusione-automatica-sottosoglia` | Presupposti e metodo (Allegato II.2) dell'esclusione automatica sotto soglia e distinzione dall'art. 110 (art. 54) |

Nucleo: **verifica di congruità** (art. 110) - presupposto, **spiegazioni** (termine 15 gg),
giustificazioni non ammesse, **esclusione**; **esclusione automatica** sotto soglia (art. 54, Allegato
II.2); **costi della manodopera** e **oneri di sicurezza** (art. 108, c. 9).

## Fonti consultate

- **D.Lgs. 31 marzo 2023, n. 36** - artt. 110, 54 e 108 c. 9 - testo vigente su Normattiva (indice pinnato
  a `!vig=2026-07-17`, codice 23G00044).

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non calcola** la **soglia di anomalia** né applica i **metodi dell'Allegato II.2**.
- **Non redige** la richiesta di spiegazioni né il **verbale di congruità**; **non valuta** nel merito le
  giustificazioni.
- **Non tratta** la valutazione dell'**offerta tecnica** (skill `oepv-valutatore-offerte-tecniche`) né il
  soccorso istruttorio, se non nei richiami.

**La skill è un supporto documentale: non sostituisce il RUP o la stazione appaltante, né la lettura degli
artt. 110, 54 e 108 del D.Lgs. 36/2023 e dell'Allegato II.2.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
