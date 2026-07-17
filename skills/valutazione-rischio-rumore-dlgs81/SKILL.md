---
name: valutazione-rischio-rumore-dlgs81
description: "Supporto documentale alla valutazione del rischio rumore negli ambienti di lavoro ai sensi del D.Lgs. 81/2008, Titolo VIII, Capo II (artt. 188-196). Aiuta a inquadrare le definizioni (pressione acustica di picco ppeak, livello di esposizione giornaliera LEX,8h e settimanale LEX,w; art. 188), a collocare l'esposizione rispetto ai valori limite di esposizione (LEX 87 dB(A) / ppeak 140 dB(C)), ai valori superiori di azione (85 dB(A) / 137 dB(C)) e ai valori inferiori di azione (80 dB(A) / 135 dB(C)) (art. 189), a impostare i contenuti della valutazione del rischio e l'obbligo di misurazione al superamento dei valori inferiori di azione (art. 190), a strutturare le misure di prevenzione e protezione, la segnaletica e la delimitazione delle aree (art. 192), a definire la messa a disposizione e l'obbligo d'uso dei DPI uditivi in funzione delle soglie (art. 193) e la sorveglianza sanitaria (art. 196). Use when an employer, RSPP, safety engineer or competent-in-acoustics technician must frame the workplace noise risk assessment, the action/limit values, the required measures, the hearing PPE and the health surveillance under the Italian Testo unico sicurezza; it is a documentary aid, does not measure or compute the exposure levels (LEX,8h), does not draft the noise risk assessment nor the acoustic report and does not replace the competent-in-acoustics technician, the competent doctor or the employer."
license: MIT
area: sicurezza-lavoro-cantieri
title: "Valutazione del rischio rumore sul lavoro - D.Lgs. 81/2008 Titolo VIII Capo II"
summary: "Rischio rumore sul lavoro (D.Lgs. 81/2008 Titolo VIII Capo II): definizioni (ppeak, LEX,8h), valori limite (87 dB(A)) e di azione superiori (85)/inferiori (80 dB(A)), valutazione e misurazione, misure di prevenzione, DPI uditivi e sorveglianza sanitaria (artt. 188-196)."
normative_refs:
  - "D.Lgs. 9/4/2008 n. 81 - artt. 188-189 (definizioni, valori limite e di azione del rumore)"
  - "D.Lgs. 9/4/2008 n. 81 - artt. 190, 192, 193, 196 (valutazione, misure, DPI uditivi, sorveglianza sanitaria)"
version: 0.1.0-alpha
status: alpha
tags:
  - dlgs-81-2008
  - sicurezza-lavoro
  - rischio-rumore
  - agenti-fisici
  - dpi-uditivi
  - sorveglianza-sanitaria
---

# Valutazione del rischio rumore sul lavoro - D.Lgs. 81/2008 Titolo VIII Capo II

## Quando usare questa skill

Usala quando devi **inquadrare la valutazione del rischio rumore** negli ambienti
di lavoro e ancorarla al **D.Lgs. 81/2008, Titolo VIII, Capo II** (artt. 188-196):

- **definizioni** rilevanti - **art. 188**: pressione acustica di picco (**ppeak**),
  livello di esposizione giornaliera (**LEX,8h**) e settimanale (**LEX,w**);
- collocare l'esposizione rispetto ai **valori** - **art. 189**: **valori limite di
  esposizione** (LEX **87 dB(A)** / ppeak **140 dB(C)**), **valori superiori di
  azione** (**85 dB(A)** / **137 dB(C)**), **valori inferiori di azione** (**80
  dB(A)** / **135 dB(C)**), con la possibilita' di usare il livello settimanale;
- impostare i **contenuti della valutazione del rischio** e l'**obbligo di
  misurazione** quando possono essere superati i valori inferiori di azione, con
  documentazione nel DVR - **art. 190**;
- strutturare le **misure di prevenzione e protezione**, la **segnaletica** e la
  **delimitazione** delle aree oltre i valori superiori di azione - **art. 192**;
- definire la **messa a disposizione** (oltre i valori inferiori) e l'**obbligo
  d'uso** (dai valori superiori) dei **DPI uditivi** - **art. 193**;
- la **sorveglianza sanitaria** (obbligatoria oltre i valori superiori di azione;
  su richiesta oltre gli inferiori) - **art. 196**.

**Non e' una skill di calcolo/misura**: non determina i livelli di esposizione
(LEX,8h), non redige il DVR-rumore ne' la relazione fonometrica e non sostituisce il
tecnico competente in acustica, il medico competente o il datore di lavoro.

## Cosa NON fa (limiti)

- Non **misura** ne' **calcola** i livelli di esposizione (LEX,8h, LEX,w, ppeak):
  le misurazioni ex art. 190 c. 2-4 spettano al tecnico con strumentazione idonea.
- Non **redige** il documento di valutazione del rischio rumore ne' la **relazione
  fonometrica**: fornisce lo schema di riferimento normativo.
- Non riproduce le **norme tecniche** (ISO 1999:1990, UNI) ne' le **banche dati**
  sul rumore richiamate (art. 190 c. 5-bis): sono citate.
- Non tratta gli altri agenti fisici del Titolo VIII (vibrazioni, campi
  elettromagnetici, radiazioni ottiche) ne' la valutazione generale ex art. 28.

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`classifica-esposizione-valori`](tasks/classifica-esposizione-valori.md) | Colloca un'esposizione rispetto ai valori inferiori/superiori di azione e al valore limite (art. 189) e individua i conseguenti obblighi (misurazione, misure, segnaletica, sorveglianza) |
| [`imposta-misure-dpi-sorveglianza`](tasks/imposta-misure-dpi-sorveglianza.md) | Struttura le misure di prevenzione (art. 192), la messa a disposizione/obbligo d'uso dei DPI uditivi (art. 193) e la sorveglianza sanitaria (art. 196) in funzione della fascia di esposizione |

## Riferimenti normativi

- **D.Lgs. 9/4/2008 n. 81** (Testo unico sicurezza) - **Titolo VIII, Capo II
  (Rumore)** - artt. **188** (definizioni), **189** (valori limite e di azione),
  **190** (valutazione del rischio), **192** (misure), **193** (DPI uditivi),
  **196** (sorveglianza sanitaria).

Dettaglio in `references/sources.yaml`,
`references/fonti/dlgs-81-2008-rumore.md`,
`references/estratti/rischio-rumore-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: la misura dei livelli di esposizione, la stesura
del DVR-rumore e della relazione fonometrica, la scelta dei DPI uditivi e i giudizi
di sorveglianza sanitaria restano in capo al **datore di lavoro**, al **tecnico
competente in acustica** e al **medico competente**, con le norme tecniche
applicabili. **Non sostituisce** il datore di lavoro, il tecnico competente in
acustica ne' il medico competente, ne' la lettura degli artt. 188-196 del D.Lgs.
81/2008.
