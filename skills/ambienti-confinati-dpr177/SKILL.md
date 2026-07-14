---
name: ambienti-confinati-dpr177
description: "Supporto documentale alla qualificazione delle imprese e dei lavoratori autonomi e alle procedure di sicurezza per i lavori in ambienti sospetti di inquinamento o confinati ai sensi del DPR 177/2011 (testo vigente, artt. 1-4) e in raccordo con il D.Lgs. 81/2008 (artt. 26, 66, 121, allegato IV punto 3). Copre i requisiti di qualificazione dell'impresa (art. 2: almeno il 30% della forza lavoro con esperienza triennale, preposti esperti, formazione con verifica di apprendimento, DPI e addestramento, DURC, CCNL, divieto di subappalto non autorizzato) e le procedure operative in caso di appalto (art. 3: informazione preventiva del committente di almeno un giorno, individuazione del rappresentante del committente, procedura di lavoro specifica con fase di soccorso e coordinamento con SSN e Vigili del Fuoco). Use when an Italian employer, contractor or safety consultant needs the DPR 177/2011 qualification requirements and confined-space entry procedures; it is a documentary aid and does not replace the risk assessment nor the involved parties."
license: MIT
area: sicurezza-lavoro-cantieri
title: "Ambienti confinati - qualificazione e procedure DPR 177/2011"
summary: "Qualificazione imprese/autonomi e procedure di sicurezza per ambienti confinati (DPR 177/2011, artt. 1-4): requisiti art. 2 (30% esperti, formazione, DPI, DURC, no subappalto non autorizzato), procedure art. 3 in appalto (informazione >=1 gg, rappresentante, soccorso/VVF)"
normative_refs:
  - "D.P.R. 14/9/2011 n. 177 (testo vigente) - artt. 1-4"
  - "D.Lgs. 81/2008 artt. 26, 66, 121 + Allegato IV punto 3 (richiamati)"
version: 0.1.0-alpha
status: alpha
tags:
  - dpr-177-2011
  - ambienti-confinati
  - sicurezza-lavoro
  - qualificazione-imprese
  - dlgs-81-2008
---

# Ambienti confinati - qualificazione e procedure DPR 177/2011

## Quando usare questa skill

Usala quando devi orientarti sugli obblighi del **DPR 177/2011** per i lavori in
**ambienti sospetti di inquinamento o confinati** (pozzi, fogne, serbatoi, silos,
vasche, cunicoli, ecc.):

- **requisiti di qualificazione** dell'impresa o del lavoratore autonomo (art. 2);
- **procedure di sicurezza in caso di appalto** (art. 3): informazione
  preventiva, rappresentante del committente, procedura di lavoro con soccorso;
- inquadramento dell'ambito rispetto al **D.Lgs. 81/2008** (artt. 66, 121,
  allegato IV punto 3).

Target: datori di lavoro committenti e appaltatori, RSPP, coordinatori della
sicurezza, consulenti, imprese del settore.

## Avvertenza

Questa skill e' un **supporto documentale** basato sul testo vigente del DPR
177/2011. **Non riproduce** il testo del D.Lgs. 81/2008 (citato come
riferimento), **non definisce** le regole tecniche di dettaglio (misurazione
dell'atmosfera, scelta dei DPI, procedure operative puntuali), **non redige** la
valutazione dei rischi, il POS o il DUVRI e **non sostituisce** il datore di
lavoro committente, l'impresa appaltatrice, i rappresentanti e i soggetti del
soccorso.

## Sotto-attivita' disponibili

- **Verifica di qualificazione dell'impresa**: controlla il possesso dei
  requisiti dell'art. 2 -> `tasks/verifica-qualificazione.md`
- **Checklist delle procedure di appalto**: verifica gli adempimenti dell'art. 3
  in caso di affidamento in appalto -> `tasks/checklist-procedure-appalto.md`

Se la richiesta non e' chiara, chiedi all'utente quale sotto-attivita' desidera.

## Processo generale

1. Identifica la sotto-attivita'.
2. Carica il file `tasks/<task-scelto>.md`.
3. Richiedi gli input (ruolo: committente/appaltatore; dati su personale,
   formazione, DPI, appalto/subappalto).
4. Applica la checklist **citando l'articolo preciso** (artt. 1-4) e i richiami
   al D.Lgs. 81/2008.
5. Chiudi con il rinvio alla valutazione dei rischi e ai soggetti responsabili.

## Fonti normative

Riferimenti completi in `references/sources.yaml`. Trascrizione verificata in
`references/fonti/dpr-177-2011.md` (testo vigente da Normattiva, pagina indice
pinnata `!vig=2026-07-14`), estratto operativo in
`references/estratti/ambienti-confinati-checklist.md`.

## Limiti

Cosa questa skill NON fa:
- non riproduce il testo del D.Lgs. 81/2008 (artt. 26, 66, 121, allegato IV punto
  3): citati come riferimento;
- non definisce le regole tecniche (atmosfera, DPI, procedure operative
  puntuali): rinvio al manuale del Ministero del lavoro e alle buone prassi;
- non redige POS/DUVRI/valutazione dei rischi;
- non tratta il regime sanzionatorio penale del D.Lgs. 81/2008 oltre alla
  sanzione qualificatoria dell'art. 3 c. 4.
