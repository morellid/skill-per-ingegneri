---
name: negoziazione-assistita-dl132
description: "Supporto documentale al procedimento di negoziazione assistita da avvocati ai sensi del D.L. 132/2014 (conv. L. 162/2014), artt. 2-5. Aiuta a inquadrare la convenzione di negoziazione assistita (cooperazione in buona fede, termine concordato non inferiore a un mese e non superiore a tre - prorogabile 30 giorni -, oggetto su diritti disponibili, forma scritta a pena di nullita', assistenza di almeno un avvocato per parte, certificazione delle firme; art. 2), i casi in cui il procedimento e' condizione di procedibilita' della domanda giudiziale (risarcimento del danno da circolazione di veicoli e natanti; domande di pagamento a qualsiasi titolo di somme non eccedenti cinquantamila euro) con le esclusioni e il rilievo dell'improcedibilita' entro la prima udienza (art. 3), la disciplina dell'invito, dell'avvertimento sulle spese e del mancato accordo (art. 4) e l'esecutivita' dell'accordo raggiunto (titolo esecutivo, iscrizione di ipoteca giudiziale, trascrizione, illecito deontologico per l'avvocato che impugna l'accordo; art. 5). Use when a lawyer, party or technician must frame the assisted-negotiation procedure, whether it is a condition of admissibility, the convention requirements and the effects of the agreement under Italian law; it is a documentary aid, does not draft the convention, the invitation or the agreement, does not give legal advice and does not replace the lawyer or the judge."
license: MIT
area: forense
title: "Negoziazione assistita da avvocati - D.L. 132/2014 (artt. 2-5)"
summary: "Negoziazione assistita da avvocati (D.L. 132/2014): convenzione - termine 1-3 mesi, forma scritta (art. 2), condizione di procedibilita' per danni da circolazione e pagamenti <= 50.000 euro (art. 3), invito e mancato accordo (art. 4), esecutivita' dell'accordo (art. 5)."
normative_refs:
  - "D.L. 12/9/2014 n. 132 (conv. L. 162/2014) - artt. 2 (convenzione) e 3 (condizione di procedibilita')"
  - "D.L. 12/9/2014 n. 132 (conv. L. 162/2014) - artt. 4 (invito e mancato accordo) e 5 (esecutivita' dell'accordo)"
version: 0.1.0-alpha
status: alpha
tags:
  - dl-132-2014
  - negoziazione-assistita
  - adr
  - condizione-procedibilita
  - avvocati
  - forense
---

# Negoziazione assistita da avvocati - D.L. 132/2014 (artt. 2-5)

## Quando usare questa skill

Usala quando devi **inquadrare il procedimento di negoziazione assistita da avvocati**
e ancorarlo al **D.L. 132/2014** (conv. L. 162/2014), **artt. 2-5**:

- la **convenzione di negoziazione assistita** - **art. 2**: cooperazione in **buona
  fede**, **termine** concordato **non inferiore a un mese e non superiore a tre**
  (prorogabile di 30 giorni), **oggetto** su **diritti disponibili**, **forma scritta
  a pena di nullita'**, assistenza di **almeno un avvocato per parte**, certificazione
  delle firme;
- i casi di **condizione di procedibilita'** - **art. 3**: **risarcimento del danno da
  circolazione di veicoli e natanti** e **domande di pagamento** a qualsiasi titolo di
  somme **non eccedenti 50.000 euro**, con le **esclusioni** (ingiunzione, ATP art.
  696-bis, esecuzione, camera di consiglio, azione civile nel processo penale,
  consumatori) e il **rilievo** dell'improcedibilita' non oltre la prima udienza;
- l'**invito**, l'**avvertimento sulle spese** (artt. 96 e 642 c.p.c.) e il **mancato
  accordo** - **art. 4**;
- l'**esecutivita' dell'accordo** - **art. 5**: **titolo esecutivo** e per
  l'**iscrizione di ipoteca giudiziale**, **trascrizione**, **illecito deontologico**
  per l'avvocato che impugna l'accordo.

**Non e' una skill che redige atti o da' consulenza legale**: non scrive la
convenzione, l'invito o l'accordo, non risolve il caso concreto e non sostituisce
l'avvocato o il giudice.

## Cosa NON fa (limiti)

- Non **redige** la convenzione, l'invito, l'accordo ne' gli atti del procedimento:
  fornisce lo schema di riferimento normativo.
- Non **valuta** la fondatezza della pretesa, la strategia processuale ne'
  l'ammissibilita' del caso concreto: e' materia dell'avvocato.
- Non tratta la **negoziazione assistita in materia di famiglia** (art. 6:
  separazione/divorzio consensuale) ne' gli obblighi antiriciclaggio/raccolta dati
  (artt. 9-11), citati come rinvio.
- Non tratta la **mediazione civile** (D.Lgs. 28/2010): strumento diverso, con altra
  disciplina e altro soggetto (organismo di mediazione).

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`verifica-condizione-procedibilita`](tasks/verifica-condizione-procedibilita.md) | Verifica se la controversia rientra tra i casi di condizione di procedibilita' (art. 3), con le esclusioni, gli effetti e il rilievo dell'improcedibilita' |
| [`inquadra-convenzione-accordo`](tasks/inquadra-convenzione-accordo.md) | Inquadra i requisiti della convenzione (art. 2), l'invito e il mancato accordo (art. 4) e gli effetti dell'accordo raggiunto (art. 5) |

## Riferimenti normativi

- **D.L. 12/9/2014 n. 132** (conv. **L. 162/2014**) - **artt. 2** (convenzione), **3**
  (improcedibilita' / condizione di procedibilita'), **4** (invito e mancato accordo),
  **5** (esecutivita' dell'accordo e trascrizione).

Dettaglio in `references/sources.yaml`,
`references/fonti/dl-132-2014-negoziazione.md`,
`references/estratti/negoziazione-assistita-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: la stesura della convenzione, dell'invito e
dell'accordo, la valutazione della pretesa e ogni scelta processuale restano in capo
all'**avvocato** e alle **parti**, con il vaglio del **giudice**. **Non sostituisce**
l'avvocato ne' il giudice, ne' la lettura degli artt. 2-5 del D.L. 132/2014 (conv. L.
162/2014).
