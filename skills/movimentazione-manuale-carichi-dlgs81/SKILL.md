---
name: movimentazione-manuale-carichi-dlgs81
description: "Supporto documentale all'inquadramento degli obblighi in materia di movimentazione manuale dei carichi (MMC) ai sensi del D.Lgs. 81/2008, Titolo VI (artt. 167-169). Aiuta a stabilire il campo di applicazione e le definizioni (MMC come operazioni di trasporto o sostegno di un carico - sollevare, deporre, spingere, tirare, portare, spostare - con rischi di patologie da sovraccarico biomeccanico, in particolare dorso-lombari; art. 167), gli obblighi del datore di lavoro (evitare la MMC ricorrendo ad attrezzature meccaniche; se non evitabile, adottare misure organizzative e mezzi adeguati tenendo conto dell'allegato XXXIII: organizzazione dei posti di lavoro, valutazione anche in fase di progettazione, riduzione dei rischi in base ai fattori individuali/ambiente/esigenze, sorveglianza sanitaria ex art. 41; le norme tecniche come criteri di riferimento; art. 168) e l'informazione, la formazione e l'addestramento dei lavoratori sul peso e le caratteristiche del carico e sulle corrette manovre (art. 169). Use when an employer, RSPP, safety engineer or competent doctor must frame the manual-handling-of-loads obligations under the Italian Testo unico sicurezza; it is a documentary aid, does not compute the lifting index or the reference mass (Annex XXXIII, ISO 11228), does not draft the manual-handling risk assessment and does not replace the employer, the RSPP or the competent doctor."
license: MIT
area: sicurezza-lavoro-cantieri
title: "Movimentazione manuale dei carichi (MMC) - D.Lgs. 81/2008 Titolo VI"
summary: "Obblighi sulla movimentazione manuale dei carichi (D.Lgs. 81/2008 Titolo VI, artt. 167-169): campo e definizioni (art. 167), obblighi del datore - evitare/ridurre, valutazione, sorveglianza sanitaria (art. 168), informazione/formazione/addestramento (art. 169)."
normative_refs:
  - "D.Lgs. 9/4/2008 n. 81 - artt. 167 (campo di applicazione e definizioni) e 168 (obblighi del datore di lavoro)"
  - "D.Lgs. 9/4/2008 n. 81 - art. 169 (informazione, formazione e addestramento) + Allegato XXXIII (rinvio)"
version: 0.1.0-alpha
status: alpha
tags:
  - dlgs-81-2008
  - sicurezza-lavoro
  - movimentazione-manuale-carichi
  - sovraccarico-biomeccanico
  - sorveglianza-sanitaria
  - ergonomia
---

# Movimentazione manuale dei carichi (MMC) - D.Lgs. 81/2008 Titolo VI

## Quando usare questa skill

Usala quando devi **inquadrare gli obblighi** in materia di **movimentazione manuale
dei carichi (MMC)** e ancorarli al **D.Lgs. 81/2008, Titolo VI** (artt. 167-169):

- **campo di applicazione e definizioni** - **art. 167**: la MMC comprende le
  operazioni di **trasporto o sostegno** di un carico (**sollevare, deporre, spingere,
  tirare, portare, spostare**) che comportano rischi di **patologie da sovraccarico
  biomeccanico**, in particolare **dorso-lombari** (patologie osteoarticolari,
  muscolo-tendinee e nervo-vascolari);
- **obblighi del datore di lavoro** - **art. 168**: **evitare** la MMC ricorrendo ad
  **attrezzature meccaniche**; se non evitabile, adottare **misure organizzative** e
  **mezzi adeguati** tenendo conto dell'**allegato XXXIII** - organizzazione dei posti
  di lavoro, **valutazione** (anche in fase di **progettazione**), riduzione dei rischi
  in base ai **fattori individuali**, all'ambiente e alle esigenze, e **sorveglianza
  sanitaria** ex **art. 41**; le **norme tecniche** costituiscono criteri di
  riferimento;
- **informazione, formazione e addestramento** - **art. 169**: informazioni su **peso**
  e caratteristiche del carico, **formazione** sui rischi e sull'esecuzione corretta, e
  **addestramento** sulle corrette manovre e procedure.

**Non e' una skill di calcolo**: non determina l'**indice di sollevamento** (NIOSH) ne'
la **massa di riferimento**, non redige il DVR-MMC e non sostituisce il datore di
lavoro, l'RSPP o il medico competente.

## Cosa NON fa (limiti)

- Non **calcola** l'**indice di sollevamento** ne' la **massa di riferimento**/i
  moltiplicatori: i criteri numerici sono nell'**Allegato XXXIII** e nelle **norme
  tecniche ISO 11228-1/2/3** (rinvio degli artt. 168-169), **non riprodotti**.
- Non **redige** il documento di valutazione del rischio MMC ne' la relazione
  ergonomica: fornisce lo schema di riferimento normativo.
- Non esprime **giudizi di sorveglianza sanitaria** (art. 41): sono del medico
  competente.
- Non tratta i rischi da **movimenti ripetitivi** degli arti superiori (altro
  contenuto dell'allegato XXXIII / ISO 11228-3) se non nel richiamo generale al
  sovraccarico biomeccanico.

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`inquadra-obblighi-mmc`](tasks/inquadra-obblighi-mmc.md) | Verifica se l'attivita' rientra nella MMC (art. 167) e ricostruisce gli obblighi del datore di lavoro: evitare/ridurre, valutazione, misure e sorveglianza sanitaria (art. 168) |
| [`imposta-informazione-formazione`](tasks/imposta-informazione-formazione.md) | Imposta l'informazione, la formazione e l'addestramento dei lavoratori sulla MMC (art. 169), distinguendo i tre livelli |

## Riferimenti normativi

- **D.Lgs. 9/4/2008 n. 81** (Testo unico sicurezza) - **Titolo VI (Movimentazione
  manuale dei carichi)** - artt. **167** (campo di applicazione e definizioni),
  **168** (obblighi del datore di lavoro), **169** (informazione, formazione e
  addestramento); **Allegato XXXIII** (rinvio).

Dettaglio in `references/sources.yaml`,
`references/fonti/dlgs-81-2008-mmc.md`,
`references/estratti/mmc-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: la valutazione del rischio MMC (indice di
sollevamento, massa di riferimento), la stesura del DVR-MMC e della relazione
ergonomica, la scelta delle misure/attrezzature e i giudizi di sorveglianza sanitaria
restano in capo al **datore di lavoro**, all'**RSPP** e al **medico competente**, con
l'**Allegato XXXIII** e le **norme tecniche** (ISO 11228). **Non sostituisce** il
datore di lavoro, l'RSPP ne' il medico competente, ne' la lettura degli artt. 167-169
del D.Lgs. 81/2008.
