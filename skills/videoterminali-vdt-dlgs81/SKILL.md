---
name: videoterminali-vdt-dlgs81
description: "Supporto documentale agli obblighi in materia di uso di attrezzature munite di videoterminali (VDT) ai sensi del D.Lgs. 81/2008, Titolo VII (artt. 172-177). Aiuta a stabilire il campo di applicazione e le esclusioni (posti di guida, sistemi a bordo di mezzi, uso prioritario del pubblico, calcolatrici/registratori di cassa, videoscrittura senza schermo separato; art. 172), le definizioni - videoterminale, posto di lavoro e in particolare il lavoratore (videoterminalista) come chi utilizza il VDT in modo sistematico o abituale per venti ore settimanali dedotte le interruzioni (art. 173), gli obblighi del datore di lavoro (analisi dei posti per rischi vista/occhi, postura e affaticamento, ergonomia e igiene ambientale; misure; requisiti minimi dell'allegato XXXIV; art. 174), lo svolgimento quotidiano con le pause (in assenza di contrattazione, quindici minuti ogni centoventi minuti di applicazione continuativa; non cumulabili a inizio/fine turno; la pausa e' parte dell'orario; art. 175), la sorveglianza sanitaria per i rischi alla vista/occhi e all'apparato muscolo-scheletrico con periodicita' biennale o quinquennale e i dispositivi di correzione visiva a carico del datore (art. 176) e l'informazione e formazione (art. 177). Use when an employer, RSPP, safety engineer or competent doctor must frame the display-screen-equipment (VDT) obligations under the Italian Testo unico sicurezza; it is a documentary aid, does not draft the VDT risk assessment, does not reproduce Annex XXXIV and does not replace the employer, the RSPP or the competent doctor."
license: MIT
area: sicurezza-lavoro-cantieri
title: "Uso di videoterminali (VDT) - D.Lgs. 81/2008 Titolo VII (artt. 172-177)"
summary: "Obblighi sull'uso di videoterminali - VDT (D.Lgs. 81/2008 Titolo VII): campo ed esclusioni (172), videoterminalista 20 ore/settimana (173), obblighi del datore e allegato XXXIV (174), pause 15 min/120 (175), sorveglianza sanitaria (176), informazione e formazione (177)."
normative_refs:
  - "D.Lgs. 9/4/2008 n. 81 - artt. 172-174 (campo, definizioni, obblighi del datore, allegato XXXIV)"
  - "D.Lgs. 9/4/2008 n. 81 - artt. 175-177 (pause, sorveglianza sanitaria, informazione e formazione)"
version: 0.1.0-alpha
status: alpha
tags:
  - dlgs-81-2008
  - sicurezza-lavoro
  - videoterminali
  - videoterminalista
  - sorveglianza-sanitaria
  - ergonomia
---

# Uso di videoterminali (VDT) - D.Lgs. 81/2008 Titolo VII (artt. 172-177)

## Quando usare questa skill

Usala quando devi **inquadrare gli obblighi** in materia di **uso di attrezzature munite
di videoterminali (VDT)** e ancorarli al **D.Lgs. 81/2008, Titolo VII** (artt. 172-177):

- **campo di applicazione ed esclusioni** - **art. 172**: si applica alle attivita' con
  uso di VDT, **escluse** guida di veicoli/macchine, sistemi a bordo di mezzi, sistemi a
  **uso prioritario del pubblico**, calcolatrici/registratori di cassa, videoscrittura
  **senza schermo separato**;
- **definizioni** - **art. 173**: **videoterminale**, **posto di lavoro** e in
  particolare il **lavoratore (videoterminalista)** = chi utilizza il VDT **in modo
  sistematico o abituale per 20 ore settimanali**, dedotte le interruzioni (art. 175);
- **obblighi del datore di lavoro** - **art. 174**: **analisi dei posti** (rischi
  **vista/occhi**, **postura/affaticamento** fisico o mentale, **ergonomia/igiene**),
  misure appropriate e organizzazione dei posti secondo i **requisiti minimi
  dell'allegato XXXIV**;
- **svolgimento quotidiano e pause** - **art. 175**: diritto a interruzione; in assenza
  di contrattazione, **pausa di 15 minuti ogni 120 minuti** di applicazione continuativa;
  **non cumulabile** a inizio/fine turno; la **pausa e' parte dell'orario** di lavoro;
- **sorveglianza sanitaria** - **art. 176**: ex art. 41, per rischi **vista/occhi** e
  **muscolo-scheletrico**; periodicita' **biennale** (idonei con prescrizioni/limitazioni
  o over 50) o **quinquennale**; **dispositivi speciali di correzione visiva** a carico
  del datore;
- **informazione e formazione** - **art. 177**.

**Non e' una skill di calcolo/redazione**: non redige il DVR-VDT, non riproduce
l'allegato XXXIV e non sostituisce il datore di lavoro, l'RSPP o il medico competente.

## Cosa NON fa (limiti)

- Non **redige** il documento di valutazione del rischio VDT ne' la relazione ergonomica.
- Non riproduce l'**allegato XXXIV** (requisiti minimi tecnici: schermo, tastiera, piano
  di lavoro, sedile, ambiente, interfaccia): e' citato come rinvio.
- Non esprime **giudizi di idoneita'/sorveglianza sanitaria** (art. 41): sono del medico
  competente.
- Non valuta in concreto se un lavoratore superi le **20 ore settimanali** (dato di
  fatto da verificare): fornisce la definizione.

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`inquadra-videoterminalista-obblighi`](tasks/inquadra-videoterminalista-obblighi.md) | Verifica l'applicabilita' del Titolo VII (art. 172), qualifica il lavoratore come videoterminalista (art. 173, 20 ore) e imposta gli obblighi del datore e le pause (artt. 174-175) |
| [`imposta-sorveglianza-formazione`](tasks/imposta-sorveglianza-formazione.md) | Imposta la sorveglianza sanitaria (art. 176, rischi e periodicita') e l'informazione/formazione (art. 177) |

## Riferimenti normativi

- **D.Lgs. 9/4/2008 n. 81** (Testo unico sicurezza) - **Titolo VII (Attrezzature munite
  di videoterminali)** - artt. **172** (campo), **173** (definizioni), **174** (obblighi
  del datore), **175** (pause), **176** (sorveglianza sanitaria), **177** (informazione e
  formazione); **Allegato XXXIV** (rinvio).

Dettaglio in `references/sources.yaml`,
`references/fonti/dlgs-81-2008-vdt.md`,
`references/estratti/vdt-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: la valutazione del rischio VDT, la stesura del
DVR-VDT e della relazione ergonomica, l'organizzazione dei posti secondo l'allegato
XXXIV e i giudizi di sorveglianza sanitaria restano in capo al **datore di lavoro**,
all'**RSPP** e al **medico competente**. **Non sostituisce** il datore di lavoro,
l'RSPP ne' il medico competente, ne' la lettura degli artt. 172-177 del D.Lgs. 81/2008.
