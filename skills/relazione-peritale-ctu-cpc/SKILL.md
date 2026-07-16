---
name: relazione-peritale-ctu-cpc
description: "Supporto alla strutturazione della relazione peritale e allo svolgimento delle operazioni del consulente tecnico d'ufficio (CTU) nel processo civile, ai sensi degli artt. 191-201 del codice di procedura civile. Aiuta a leggere e riformulare i quesiti del giudice (art. 191), a gestire accettazione/astensione e giuramento anche con dichiarazione a firma digitale (artt. 192-193), a condurre le operazioni peritali con l'intervento delle parti e dei consulenti di parte (art. 194), a redigere il processo verbale e la relazione con la corretta scansione dei termini fissati dal giudice - trasmissione della bozza alle parti, raccolta delle loro osservazioni, deposito della relazione con una sintetica valutazione delle osservazioni (art. 195), e a gestire esame contabile, tentativo di conciliazione, rinnovazione e sostituzione (artt. 196-200). Inquadra inoltre il CTU nell'albo (categorie e settori di specializzazione, requisiti di iscrizione) secondo il D.M. 109/2023. Use when an engineer serving as court-appointed expert (CTU) in Italian civil proceedings must structure the expert report and manage the peritale timeline and adversarial steps; it structures the report and procedure and does NOT provide the technical/merits content of the appraisal, does not replace the judge's directions and does not cover criminal-proceeding perizia (c.p.p.)."
license: MIT
area: forense
title: "Struttura della relazione peritale del CTU (c.p.c. artt. 191-201)"
summary: "Struttura della relazione peritale e delle operazioni del CTU nel processo civile (c.p.c. 191-201): quesiti, giuramento, verbale, trasmissione alle parti e osservazioni, deposito e termini. Inquadra il CTU nell'albo (categorie/settori, DM 109/2023). Non entra nel merito tecnico."
normative_refs:
  - "Codice di procedura civile (R.D. 1443/1940) - artt. 191-201 (del consulente tecnico)"
  - "D.M. Giustizia 4/8/2023 n. 109 (albo CTU: categorie, settori, requisiti di iscrizione)"
version: 0.1.0-alpha
status: alpha
tags:
  - ctu
  - relazione-peritale
  - codice-procedura-civile
  - ingegneria-forense
  - dm-109-2023
---

# Struttura della relazione peritale del CTU (c.p.c. artt. 191-201)

## Quando usare questa skill

Usala quando, come **ingegnere nominato consulente tecnico d'ufficio (CTU)** in un
**processo civile**, devi **strutturare la relazione peritale** e **gestire le
operazioni peritali** ai sensi degli **artt. 191-201 c.p.c.**:

- leggere e **riformulare i quesiti** posti dal giudice nell'ordinanza di nomina
  (art. 191);
- gestire **accettazione/astensione e ricusazione** e il **giuramento** (in udienza
  o con dichiarazione a **firma digitale**), con la contestuale **fissazione dei
  termini** dell'art. 195, terzo comma (artt. 192-193);
- condurre le **operazioni peritali** assicurando l'**intervento delle parti** e
  dei **consulenti di parte (CTP)** (art. 194);
- redigere il **processo verbale** e la **relazione** rispettando la scansione dei
  **termini** fissati dal giudice: **trasmissione della bozza alle parti**,
  **raccolta delle osservazioni**, **deposito** della relazione con una **sintetica
  valutazione** delle osservazioni (art. 195);
- gestire **esame contabile**, **tentativo di conciliazione**, **rinnovazione** e
  **sostituzione** del consulente (artt. 196-200);
- **inquadrare la propria posizione nell'albo CTU** (categoria e settore di
  specializzazione, requisiti di iscrizione) secondo il **D.M. 109/2023**.

## Cosa NON fa (limiti)

- **Non fornisce il contenuto tecnico/di merito** della perizia (rilievi, calcoli,
  valutazioni estimative): quello dipende dallo specifico quesito e dalla disciplina
  tecnica applicabile. La skill struttura **la relazione e la procedura**, non le
  conclusioni.
- **Non sostituisce le direttive del giudice**: quesiti, termini e modalita' sono
  fissati dall'ordinanza; in caso di dubbio si chiedono chiarimenti al magistrato.
- **Non copre la perizia penale** (c.p.p., artt. 220 e ss.) ne' l'ATP / consulenza
  ex art. 696-bis c.p.c. (solo cenni di rinvio).
- Non tratta la **liquidazione del compenso** del CTU: per quella vedi la skill
  `compensi-ctu-dpr115`.

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`struttura-relazione`](tasks/struttura-relazione.md) | Dall'ordinanza di nomina e dai quesiti, imposta l'indice della relazione peritale e la scansione dei termini dell'art. 195 (bozza alle parti, osservazioni, deposito con sintetica valutazione) |
| [`verbale-operazioni-peritali`](tasks/verbale-operazioni-peritali.md) | Struttura il processo verbale delle operazioni (inizio indagini, presenza delle parti/CTP, istanze e osservazioni, documenti) nel rispetto degli artt. 194-195 |

## Riferimenti normativi

- **Codice di procedura civile**, artt. **191-201** ("Del consulente tecnico"):
  nomina e quesiti (191), astensione/ricusazione (192), giuramento (193), attivita'
  del consulente (194), processo verbale e relazione (195), rinnovazione e
  sostituzione (196), assistenza all'udienza (197), esame contabile e conciliazione
  (198-199), mancata conciliazione (200), consulente tecnico di parte (201). Testo
  vigente aggiornato da D.Lgs. 149/2022 (riforma Cartabia) e D.Lgs. 164/2024.
- **D.M. Giustizia 4/8/2023 n. 109** - albo CTU: **categorie e settori di
  specializzazione** (art. 3 e Allegato A), **requisiti** e **domanda di iscrizione**
  (artt. 4-5), mantenimento e vigilanza (art. 6).

Dettaglio in `references/sources.yaml`,
`references/fonti/codice-procedura-civile-artt-191-201.md`,
`references/fonti/dm-109-2023.md`,
`references/estratti/struttura-relazione-checklist.md`.

## Avvertenza

Skill di **supporto alla struttura e alla procedura**: i quesiti, i termini e le
modalita' delle operazioni sono fissati dal **giudice**; il **contenuto tecnico** e
le **conclusioni** della perizia restano responsabilita' del CTU secondo la propria
disciplina e la propria competenza. La skill **non sostituisce** il giudice, il
difensore ne' il giudizio tecnico del consulente.
