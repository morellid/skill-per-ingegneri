---
name: valutazione-rischio-vibrazioni-dlgs81
description: "Supporto documentale alla valutazione del rischio da vibrazioni meccaniche negli ambienti di lavoro ai sensi del D.Lgs. 81/2008, Titolo VIII, Capo III (artt. 200-205). Aiuta a inquadrare le definizioni (vibrazioni trasmesse al sistema mano-braccio e al corpo intero, esposizione giornaliera A(8); art. 200), a collocare l'esposizione rispetto ai valori limite di esposizione e ai valori d'azione (mano-braccio: limite 5 m/s2 - su periodi brevi 20 - e azione 2,5 m/s2; corpo intero: limite 1,0 m/s2 - su periodi brevi 1,5 - e azione 0,5 m/s2; art. 201), a impostare i contenuti della valutazione dei rischi e la valutazione/misurazione con l'allegato XXXV (art. 202), a strutturare le misure di prevenzione e protezione e il programma oltre i valori d'azione, con l'obbligo di riportare l'esposizione sotto il valore limite se superato (art. 203), la sorveglianza sanitaria (art. 204) e le deroghe per navigazione marittima/aerea ed esposizioni occasionali (art. 205). Use when an employer, RSPP, safety engineer or competent technician must frame the mechanical vibration (hand-arm and whole-body) risk assessment, the action/limit values, the required measures, the health surveillance and the derogations under the Italian Testo unico sicurezza; it is a documentary aid, does not measure or compute the exposure levels A(8), does not draft the vibration risk assessment nor the technical report and does not replace the competent technician, the competent doctor or the employer."
license: MIT
area: sicurezza-lavoro-cantieri
title: "Rischio vibrazioni sul lavoro - D.Lgs. 81/2008 Titolo VIII Capo III"
summary: "Rischio vibrazioni meccaniche sul lavoro (D.Lgs. 81/2008 Titolo VIII Capo III): definizioni A(8) (art. 200), valori limite/azione mano-braccio 5/2,5 e corpo intero 1,0/0,5 m/s2 (art. 201), valutazione (art. 202), misure (art. 203), sorveglianza (art. 204), deroghe (art. 205)."
normative_refs:
  - "D.Lgs. 9/4/2008 n. 81 - artt. 200-201 (definizioni, valori limite e d'azione delle vibrazioni)"
  - "D.Lgs. 9/4/2008 n. 81 - artt. 202, 203, 204, 205 (valutazione, misure, sorveglianza sanitaria, deroghe)"
version: 0.1.0-alpha
status: alpha
tags:
  - dlgs-81-2008
  - sicurezza-lavoro
  - rischio-vibrazioni
  - agenti-fisici
  - mano-braccio
  - corpo-intero
---

# Rischio vibrazioni sul lavoro - D.Lgs. 81/2008 Titolo VIII Capo III

## Quando usare questa skill

Usala quando devi **inquadrare la valutazione del rischio da vibrazioni meccaniche**
(mano-braccio e corpo intero) negli ambienti di lavoro e ancorarla al **D.Lgs.
81/2008, Titolo VIII, Capo III** (artt. 200-205):

- **definizioni** - **art. 200**: vibrazioni trasmesse al **sistema mano-braccio** e
  al **corpo intero**; esposizione giornaliera **A(8)** [m/s²];
- collocare l'esposizione rispetto ai **valori** - **art. 201**:
  - **mano-braccio**: valore **limite** di esposizione **5 m/s²** (su periodi brevi
    20 m/s²) e valore **d'azione 2,5 m/s²**;
  - **corpo intero**: valore **limite 1,0 m/s²** (su periodi brevi 1,5 m/s²) e valore
    **d'azione 0,5 m/s²**;
- impostare i **contenuti della valutazione dei rischi** e la **valutazione/
  misurazione** con l'**allegato XXXV** (parti A e B) - **art. 202**;
- strutturare le **misure di prevenzione e protezione** e il **programma** oltre i
  valori d'azione, con l'obbligo di **riportare l'esposizione sotto il valore limite**
  se superato - **art. 203**;
- la **sorveglianza sanitaria** (oltre i valori d'azione o secondo il medico) - **art.
  204** - e le **deroghe** (navigazione marittima/aerea; esposizioni occasionali) -
  **art. 205**.

**Non e' una skill di calcolo/misura**: non determina i livelli di esposizione A(8),
non redige il DVR-vibrazioni ne' la relazione tecnica e non sostituisce il tecnico
competente, il medico competente o il datore di lavoro.

## Cosa NON fa (limiti)

- Non **misura** ne' **calcola** i livelli di esposizione **A(8)** (mano-braccio /
  corpo intero): la valutazione/misurazione ex art. 202 e allegato XXXV spetta al
  tecnico con metodologia e strumentazione idonee.
- Non **redige** il documento di valutazione del rischio vibrazioni ne' la relazione
  tecnica: fornisce lo schema di riferimento normativo.
- Non riproduce l'**allegato XXXV** ne' le **norme tecniche** (UNI, ISO): sono citate.
- Non tratta gli altri agenti fisici del Titolo VIII (rumore - vedi
  `valutazione-rischio-rumore-dlgs81` -, CEM, radiazioni ottiche) ne' la valutazione
  generale ex art. 28.

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`classifica-esposizione-vibrazioni`](tasks/classifica-esposizione-vibrazioni.md) | Colloca un'esposizione mano-braccio/corpo intero rispetto ai valori d'azione e limite (art. 201) e individua gli obblighi (valutazione/misura, misure, sorveglianza) |
| [`imposta-misure-sorveglianza-deroghe`](tasks/imposta-misure-sorveglianza-deroghe.md) | Struttura le misure di prevenzione e il programma (art. 203), la sorveglianza sanitaria (art. 204) e verifica i presupposti delle deroghe (art. 205) |

## Riferimenti normativi

- **D.Lgs. 9/4/2008 n. 81** (Testo unico sicurezza) - **Titolo VIII, Capo III
  (Vibrazioni)** - artt. **200** (definizioni), **201** (valori limite e d'azione),
  **202** (valutazione dei rischi), **203** (misure), **204** (sorveglianza
  sanitaria), **205** (deroghe).

Dettaglio in `references/sources.yaml`,
`references/fonti/dlgs-81-2008-vibrazioni.md`,
`references/estratti/rischio-vibrazioni-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: la misura dei livelli di esposizione, la stesura
del DVR-vibrazioni e della relazione tecnica, la scelta delle misure/attrezzature e i
giudizi di sorveglianza sanitaria restano in capo al **datore di lavoro**, al
**tecnico competente** e al **medico competente**, con le norme tecniche applicabili
e l'allegato XXXV. **Non sostituisce** il datore di lavoro, il tecnico competente ne'
il medico competente, ne' la lettura degli artt. 200-205 del D.Lgs. 81/2008.
