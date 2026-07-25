---
name: valutazione-rischio-cem-dlgs81
description: "Supporto documentale per la valutazione del rischio da esposizione dei lavoratori ai campi elettromagnetici (CEM) ai sensi del D.Lgs 81/2008, Titolo VIII Capo IV (artt. 206-212 e Allegato XXXVI). Aiuta RSPP, datore di lavoro e tecnico competente in agenti fisici a: inquadrare la valutazione del rischio CEM nell'ambito del DVR e stabilire quando misura o calcolo dei livelli sono necessari e quando no (art. 209, casi dei luoghi accessibili al pubblico gia' valutati e delle attrezzature conformi a norme di prodotto); distinguere gli effetti biofisici diretti (termici e non termici) dagli effetti indiretti (interferenza con dispositivi medici e stimolatori cardiaci, oggetti ferromagnetici, detonatori, incendi, correnti di contatto) ex art. 207; usare il quadro dei valori limite di esposizione VLE (effetti sanitari ed effetti sensoriali) e dei valori di azione VA (inferiori e superiori) rinviando all'Allegato XXXVI parti I, II e III (art. 208); impostare le misure per eliminare o ridurre il rischio quando i VA sono superati (programma d'azione, schermature, limitazione di durata e intensita', DPI, segnaletica e accesso limitato alle aree oltre i VA) ex art. 210; gestire i gruppi particolarmente sensibili (portatori di dispositivi medici impiantati e lavoratrici in gravidanza), l'informazione e formazione (art. 210-bis), la sorveglianza sanitaria (art. 211) e le deroghe ministeriali ai VLE (art. 212). Use when an RSPP/employer/physical-agents technician must frame the occupational EMF risk assessment, decide whether measurement or calculation is needed, apply the VLE/VA framework or set the risk-reduction measures under Title VIII Chapter IV; it is a documentary aid, does NOT reproduce the numeric VLE/VA values of Annex XXXVI, does NOT perform measurements and does NOT replace the physical-agents technician or the occupational physician."
license: MIT
area: sicurezza-lavoro-cantieri
title: "Rischio campi elettromagnetici (CEM) - D.Lgs 81/2008 Titolo VIII Capo IV"
summary: "Valutazione del rischio da campi elettromagnetici dei lavoratori (D.Lgs 81/2008 Titolo VIII Capo IV, artt. 206-212): quadro VLE/VA (Allegato XXXVI), quando misura/calcolo, effetti diretti/indiretti, gruppi sensibili, misure, sorveglianza sanitaria. Non riproduce i valori."
normative_refs:
  - "D.Lgs. 9/4/2008 n. 81 - artt. 206-208 (campo di applicazione, definizioni, VLE e valori d'azione CEM)"
  - "D.Lgs. 9/4/2008 n. 81 - artt. 209-212 e Allegato XXXVI (valutazione, misure, sorveglianza sanitaria, deroghe)"
version: 0.1.0-alpha
status: alpha
tags:
  - dlgs-81-2008
  - sicurezza-lavoro
  - rischio-cem
  - campi-elettromagnetici
  - agenti-fisici
  - vle-va
---

# Rischio campi elettromagnetici (CEM) sul lavoro — D.Lgs 81/2008 Titolo VIII Capo IV

Supporto documentale per la **valutazione del rischio da esposizione dei lavoratori ai campi elettromagnetici (CEM)**
ai sensi del **D.Lgs 81/2008, Titolo VIII Capo IV (artt. 206-212 e Allegato XXXVI)**. Completa la serie "agenti fisici"
del Titolo VIII (rumore Capo II, vibrazioni Capo III).

**La skill è un supporto documentale: non riproduce i valori numerici VLE/VA dell'Allegato XXXVI, non esegue misure e non sostituisce il tecnico competente in agenti fisici né il medico competente.**

## A chi serve

RSPP, datore di lavoro, tecnico competente in agenti fisici, medico competente: chiunque debba impostare o verificare la
valutazione del rischio CEM di un luogo di lavoro (es. saldatura, riscaldamento a induzione, elettrolisi, apparati RF,
risonanza magnetica).

## Cosa fa

1. **Inquadra la valutazione del rischio CEM** nel DVR e chiarisce **quando misura/calcolo** sono necessari e quando no
   (art. 209).
2. **Distingue effetti diretti** (termici/non termici) e **indiretti** (dispositivi medici/pacemaker, oggetti
   ferromagnetici, detonatori, incendi, correnti di contatto) — art. 207.
3. **Usa il quadro VLE/VA** (effetti sanitari/sensoriali; VA inferiori/superiori) rinviando all'Allegato XXXVI (art.
   208).
4. **Imposta le misure** quando i VA sono superati e gestisce **gruppi sensibili**, informazione/formazione,
   sorveglianza sanitaria e deroghe (artt. 210, 210-bis, 211, 212).

## Sotto-attività

- [`inquadra-valutazione-e-vle`](tasks/inquadra-valutazione-e-vle.md) — imposta la valutazione del rischio CEM
  (quando misura/calcolo, casi esclusi, elementi di attenzione) e il quadro VLE/VA (artt. 208-209 + Allegato XXXVI).
- [`misure-e-gruppi-sensibili`](tasks/misure-e-gruppi-sensibili.md) — imposta le misure di riduzione (art. 210),
  la gestione dei gruppi particolarmente sensibili, l'informazione/formazione, la sorveglianza sanitaria e le deroghe.

## Fonte (Regola zero)

D.Lgs 81/2008, Testo coordinato INL gennaio 2025, artt. 206-212 e Allegato XXXVI; testo trascritto in
[`references/fonti/dlgs-81-2008-titolo-viii-capo-iv.md`](references/fonti/dlgs-81-2008-titolo-viii-capo-iv.md), hash
SHA256 in [`references/sources.yaml`](references/sources.yaml). Checklist in
[`references/estratti/valutazione-cem-checklist.md`](references/estratti/valutazione-cem-checklist.md).

## Limiti

- Non riproduce i **valori numerici VLE/VA** (Allegato XXXVI, tabelle frequenza-dipendenti): il tecnico li legge
  dall'allegato.
- Non è la valutazione di **rumore** (Capo II), **vibrazioni** (Capo III) o **ROA** (Capo V), né l'esposizione della
  **popolazione** ai CEM (DPCM 2003 / art. 87 CCE): temi con skill/norme dedicate.
- Non esegue **misure strumentali** né sostituisce il tecnico competente in agenti fisici o il medico competente.
