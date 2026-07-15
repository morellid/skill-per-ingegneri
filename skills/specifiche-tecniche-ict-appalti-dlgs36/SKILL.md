---
name: specifiche-tecniche-ict-appalti-dlgs36
description: "Supporto documentale alla redazione delle specifiche tecniche di una procedura d'appalto ICT della pubblica amministrazione ai sensi del D.Lgs. 36/2023 (Codice dei contratti pubblici) e del CAD. Aiuta a impostare la fase preliminare di analisi comparativa delle soluzioni software (software ad hoc, riuso, open source, cloud, proprietario; art. 68 CAD) e i relativi criteri (costo complessivo, formati/standard aperti e interoperabilita', sicurezza e protezione dati; art. 68 c. 1-bis), a presidiare il riuso e la titolarita' dei diritti sul codice nel capitolato (art. 69 CAD), e a formulare le specifiche tecniche secondo le modalita' ammesse (prestazioni/requisiti funzionali, riferimento a norme con clausola 'o equivalente', divieto di marchi/brevetti) e le etichettature (art. 79-80 e allegato II.5 del Codice). Use when a RUP, technical officer or ICT engineer in an Italian public administration must set up the technical specifications of an ICT tender or the pre-purchase comparative analysis; it is a documentary aid and does not draft the full tender, does not choose the solution, does not evaluate the bids and does not compute the base price."
license: MIT
area: appalti-opere-pubbliche
title: "Specifiche tecniche ed acquisizione ICT negli appalti PA - D.Lgs. 36/2023 + CAD"
summary: "Specifiche tecniche ed etichettature negli appalti ICT della PA (art. 79-80 e all. II.5 D.Lgs. 36/2023): modalita' di formulazione, clausola 'o equivalente', divieto di marchi; analisi comparativa delle soluzioni software e riuso/titolarita' del codice (artt. 68-69 CAD)."
normative_refs:
  - "D.Lgs. 31/3/2023 n. 36 - artt. 79, 80 e allegato II.5 (specifiche tecniche ed etichettature)"
  - "D.Lgs. 7/3/2005 n. 82 (CAD) - artt. 68 (analisi comparativa) e 69 (riuso e standard aperti)"
version: 0.1.0-alpha
status: alpha
tags:
  - dlgs-36-2023
  - codice-contratti-pubblici
  - cad-dlgs-82-2005
  - specifiche-tecniche
  - appalti-ict
  - riuso-software
---

# Specifiche tecniche ed acquisizione ICT negli appalti PA - D.Lgs. 36/2023 + CAD

## Quando usare questa skill

Usala quando, in una **pubblica amministrazione**, devi impostare le **specifiche
tecniche** di una procedura d'appalto **ICT** (o l'**acquisizione di software**) e
vuoi ancorare le scelte al **Codice dei contratti pubblici** (D.Lgs. 36/2023) e al
**Codice dell'amministrazione digitale** (CAD, D.Lgs. 82/2005):

- impostare la **analisi comparativa delle soluzioni** prima dell'acquisto di
  software (software ad hoc, riuso, open source, cloud, proprietario, misto) e i
  relativi **criteri** (costo complessivo; formati/interfacce aperti e standard di
  interoperabilita'; sicurezza e protezione dati) - **art. 68 CAD**;
- presidiare **riuso** e **titolarita' dei diritti** sul codice sorgente nel
  **capitolato / specifiche di progetto** - **art. 69 CAD**;
- **formulare le specifiche tecniche** secondo le modalita' ammesse (prestazioni/
  requisiti funzionali; riferimento a norme con la clausola **"o equivalente"**;
  divieto di **marchi/brevetti**) e le **etichettature** - **art. 79-80 e
  allegato II.5** del Codice.

**Non e' una skill di calcolo e non redige la gara**: non sceglie la soluzione,
non scrive il capitolato/disciplinare completo, non valuta le offerte e non
calcola importi/basi d'asta.

## Cosa NON fa (limiti)

- Non **sceglie la soluzione** ne' effettua materialmente la valutazione
  comparativa: fornisce lo schema di criteri (art. 68 CAD), la decisione e la
  motivazione spettano alla PA/RUP.
- Non definisce i **criteri di aggiudicazione / OEPV** (art. 108 del Codice):
  rinvio alla skill `oepv-valutatore-offerte-tecniche`.
- Non riproduce le **Linee guida AgID** (analisi comparativa, riuso,
  publiccode.yml) ne' le norme tecniche citate (a pagamento): sono richiamate.
- Non calcola **importi, base d'asta, soglie** ne' redige il capitolato completo.

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`analisi-comparativa-soluzioni`](tasks/analisi-comparativa-soluzioni.md) | Imposta la valutazione comparativa tecnico-economica delle soluzioni software ex art. 68 CAD (soluzioni a-f, criteri c. 1-bis) e le condizioni per il ricorso al proprietario (c. 1-ter) e il riuso/titolarita' del codice (art. 69) |
| [`formula-specifiche-tecniche`](tasks/formula-specifiche-tecniche.md) | Verifica che le specifiche tecniche siano formulate secondo una modalita' ammessa (all. II.5, A, punto 5), con la clausola "o equivalente" e senza riferimenti a marchi/brevetti, e imposta le eventuali etichettature (B) |

## Riferimenti normativi

- **D.Lgs. 31/3/2023 n. 36** (Codice dei contratti pubblici) - **artt. 79, 80** e
  **allegato II.5** (specifiche tecniche ed etichettature; operativo art. 70 c. 3).
- **D.Lgs. 7/3/2005 n. 82 (CAD)** - **artt. 68** (analisi comparativa delle
  soluzioni) e **69** (riuso delle soluzioni e standard aperti).

Dettaglio in `references/sources.yaml`, `references/fonti/dlgs-36-2023.md`,
`references/fonti/dlgs-82-2005-cad.md`,
`references/estratti/specifiche-tecniche-ict-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: la scelta della soluzione, la stesura del
capitolato/disciplinare, la motivazione della valutazione comparativa e la
determinazione degli importi restano in capo al **RUP / stazione appaltante**, con
le **Linee guida AgID** e il parere degli uffici competenti. **Non sostituisce** il
RUP, il progettista del capitolato ne' le Linee guida AgID/ANAC.
