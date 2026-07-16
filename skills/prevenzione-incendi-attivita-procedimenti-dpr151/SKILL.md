---
name: prevenzione-incendi-attivita-procedimenti-dpr151
description: "Supporto documentale per stabilire se un'attivita' e' soggetta ai controlli di prevenzione incendi e quale procedimento del Comando dei Vigili del fuoco si applica, secondo il D.P.R. 1 agosto 2011, n. 151 (regolamento di semplificazione dei procedimenti di prevenzione incendi). Aiuta a verificare se l'attivita' rientra nell'Allegato I e in quale categoria A, B o C (art. 2); a impostare la valutazione del progetto per le categorie B e C (art. 3, pronuncia del Comando entro 60 giorni); a gestire l'avvio dell'attivita' tramite segnalazione certificata di inizio attivita' (SCIA) prima dell'esercizio e i controlli con visite tecniche entro 60 giorni (art. 4), con il certificato di prevenzione incendi rilasciato entro 15 giorni per la categoria C e i provvedimenti in caso di carenza (conformazione entro 45 giorni); a programmare il rinnovo periodico di conformita' antincendio ogni 5 anni (10 anni per le attivita' 6, 7, 8, 64, 71, 72, 77 - art. 5); a rispettare gli obblighi in esercizio (art. 6) e a presentare l'istanza di deroga (art. 7). Use when an engineer, fire-prevention professional, or SUAP/VVF operator must determine whether an Italian activity is subject to fire-prevention controls, its category (A/B/C) and the applicable procedure (project assessment, SCIA, technical visits, CPI, periodic renewal, derogation) under DPR 151/2011; it is a documentary aid and does NOT reproduce the exact classification of every activity (the exact category must be read on Annex I of the decree), does not draft the fire-prevention project, the SCIA or the antincendio assessments, does not reproduce the technical fire-prevention rules (RTO/RTV, DM 3/8/2015) and does not replace the fire-prevention professional or the Fire Brigade Command."
license: MIT
area: sicurezza-lavoro-cantieri
title: "Attivita' e procedimenti di prevenzione incendi (DPR 151/2011)"
summary: "Stabilisce se un'attivita' e' soggetta ai controlli di prevenzione incendi e la categoria A/B/C (Allegato I) secondo il DPR 151/2011, e imposta l'iter VV.F.: valutazione progetto (B/C), SCIA, visite 60 gg, CPI (C), rinnovo, deroghe. Non classifica ogni attivita'."
normative_refs:
  - "D.P.R. 1 agosto 2011, n. 151 - artt. 2, 3, 4, 5, 6, 7 e Allegato I (categorie A/B/C)"
  - "D.Lgs. 139/2006 art. 16 + art. 49 DL 78/2010 (conv. L. 122/2010) (richiamati)"
version: 0.1.0-alpha
status: alpha
tags:
  - prevenzione-incendi
  - dpr-151-2011
  - scia-antincendio
  - certificato-prevenzione-incendi
  - vigili-del-fuoco
---

# Attivita' e procedimenti di prevenzione incendi (DPR 151/2011)

## Quando usare questa skill

Usala quando un **ingegnere, professionista antincendio o operatore SUAP/VV.F.** deve
stabilire se un'attivita' e' **soggetta ai controlli di prevenzione incendi** e quale
**procedimento** del **Comando dei Vigili del fuoco** si applica, secondo il **D.P.R. 1
agosto 2011, n. 151** (regolamento di semplificazione dei procedimenti di prevenzione
incendi):

- verificare se l'attivita' rientra nell'**Allegato I** e in quale **categoria A/B/C**;
- impostare la **valutazione del progetto** (B/C), la **SCIA** e i **controlli**;
- gestire il **certificato di prevenzione incendi (CPI)**, il **rinnovo periodico** e le **deroghe**.

Per la **gestione dell'emergenza** (piano di emergenza) usa `piano-emergenza-antincendio-dm2021`;
per la protezione dei lavoratori dalle **atmosfere esplosive** usa `atex-luoghi-lavoro-dlgs81`.

## Attivita' soggette e categorie (art. 2)

Sono soggette ai controlli le attivita' riportate nell'**Allegato I**, distinte in **tre
categorie**:

- **A**: attivita' a rischio contenuto, dotate di **regole tecniche** di riferimento;
- **B**: attivita' di media complessita' (comprende le A con soglie maggiori);
- **C**: attivita' a rischio piu' elevato o di maggiore complessita'.

La **categoria** dipende da dimensione dell'impresa, settore, esistenza di regole tecniche
ed esigenze di tutela della pubblica incolumita'. **La categoria esatta va letta sulla
tabella dell'Allegato I** (colonne A/B/C): la skill non la riproduce attivita' per attivita'.

## Valutazione del progetto (art. 3) - solo B e C

Le attivita' di **categoria B e C** devono richiedere al Comando l'**esame del progetto**
di nuovi impianti/costruzioni o di modifiche con **aggravio** delle condizioni di sicurezza.
Il Comando puo' chiedere integrazioni **entro 30 giorni** e si pronuncia sulla conformita'
**entro 60 giorni** dalla documentazione completa. La **categoria A** non richiede questa fase.

## Controlli e avvio dell'attivita' (art. 4) - SCIA

- **Prima dell'esercizio**, si presenta al Comando la **SCIA** (segnalazione certificata di
  inizio attivita') con la documentazione prevista; il Comando verifica la completezza
  formale e rilascia **ricevuta** (l'attivita' puo' avviarsi).
- **Categoria A e B**: **visite tecniche entro 60 giorni** (anche a campione); in caso di
  carenza, provvedimenti di divieto salvo **conformazione entro 45 giorni**.
- **Categoria C**: **visite tecniche entro 60 giorni** e, se l'esito e' positivo, rilascio
  del **certificato di prevenzione incendi (CPI) entro 15 giorni**.
- **Modifiche** (c. 6): nuove destinazioni, modifiche di lavorazione/strutture o variazioni
  delle sostanze pericolose che alterano le condizioni di sicurezza fanno **ripartire** le
  procedure (con la valutazione del progetto dell'art. 3 in caso di aggravio).

## Rinnovo periodico (art. 5)

Il titolare invia al Comando la **richiesta di rinnovo periodico di conformita' antincendio
ogni 5 anni** (dichiarazione di assenza di variazioni + documentazione). La cadenza e'
**elevata a 10 anni** per le attivita' n. **6, 7, 8, 64, 71, 72 e 77** dell'Allegato I.

## Esercizio e deroghe (artt. 6 e 7)

- **In esercizio** (art. 6): mantenere in efficienza sistemi, dispositivi, attrezzature e
  misure antincendio, effettuare verifiche/manutenzioni e informare sui rischi.
- **Deroga** (art. 7): se l'attivita' non consente l'integrale osservanza delle regole
  tecniche, si presenta **istanza di deroga** al Comando, che la trasmette con parere
  motivato **entro 30 giorni** alla **Direzione regionale** (decisione sentito il Comitato
  tecnico regionale).

## Cosa NON fa (limiti)

- **Non riproduce la classificazione puntuale** di ogni attivita': la **categoria esatta**
  (A/B/C) va **letta sull'Allegato I** dell'atto.
- **Non redige** il progetto antincendio, la SCIA ne' le asseverazioni/certificazioni.
- **Non riproduce le regole tecniche** (Codice di prevenzione incendi - DM 3/8/2015 e RTV):
  le richiama.
- **Non sostituisce** il professionista antincendio ne' il **Comando dei Vigili del fuoco**.

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`classifica-attivita-categoria`](tasks/classifica-attivita-categoria.md) | Verifica se l'attivita' e' nell'Allegato I e in quale categoria A/B/C, e i procedimenti conseguenti |
| [`imposta-procedimento-vvf`](tasks/imposta-procedimento-vvf.md) | Imposta il procedimento VV.F.: valutazione progetto (B/C), SCIA e controlli, CPI (C), rinnovo periodico e deroghe |

## Riferimenti normativi

- **D.P.R. 1 agosto 2011, n. 151** - **art. 2** (attivita' soggette, categorie A/B/C,
  Allegato I), **art. 3** (valutazione dei progetti), **art. 4** (SCIA e controlli, CPI),
  **art. 5** (rinnovo periodico), **art. 6** (obblighi in esercizio), **art. 7** (deroghe);
  **Allegato I** (elenco delle attivita').
- **D.Lgs. 8 marzo 2006, n. 139** (art. 16) e **art. 49 DL 78/2010** (conv. L. 122/2010) -
  basi normative (richiamati, non riprodotti).

Dettaglio in `references/sources.yaml`, `references/fonti/dpr-151-2011.md`,
`references/estratti/prevenzione-incendi-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: la classificazione dell'attivita', la valutazione del
progetto e la predisposizione delle pratiche antincendio restano responsabilita' del
professionista e del **Comando dei Vigili del fuoco**, sull'Allegato I vigente e sulle regole
tecniche applicabili. La skill **non sostituisce** il professionista antincendio, il Comando VV.F. ne' la lettura dell'Allegato I del D.P.R. 151/2011 e delle regole tecniche di prevenzione incendi.
