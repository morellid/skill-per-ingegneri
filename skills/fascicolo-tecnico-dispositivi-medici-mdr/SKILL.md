---
name: fascicolo-tecnico-dispositivi-medici-mdr
description: "Supporto documentale alla struttura del fascicolo tecnico (documentazione tecnica) di un dispositivo medico di classe I o IIa e all'individuazione del percorso di valutazione della conformita' ai sensi del Regolamento (UE) 2017/745 (MDR). Aiuta a comporre i sei capitoli della documentazione tecnica dell'allegato II (descrizione e specifiche del dispositivo con classe di rischio e giustificazione; informazioni fornite dal fabbricante - etichetta e istruzioni; informazioni di progettazione e fabbricazione; requisiti generali di sicurezza e prestazione dell'allegato I; analisi rischi/benefici e gestione del rischio; verifica e convalida del prodotto inclusa la valutazione clinica), la documentazione sulla sorveglianza post-commercializzazione dell'allegato III (piano PMS, rapporto sulla sicurezza o PSUR) e a scegliere il percorso di conformita' dell'art. 52 (classe I in autodichiarazione con dichiarazione UE ex art. 19; classe I sterile/con funzione di misura/strumenti chirurgici riutilizzabili con intervento limitato dell'organismo notificato; classe IIa con allegato IX capi I e III oppure documentazione tecnica con allegato XI). Use when a biomedical engineer or manufacturer must structure the technical documentation and choose the conformity assessment route for a Class I or IIa medical device under the EU MDR; it is a documentary aid and does not classify the device, does not write the clinical evaluation and does not identify the applicable harmonised standards."
license: MIT
area: impianti-macchine-prodotti
title: "Fascicolo tecnico dispositivi medici (MDR Reg. UE 2017/745) - Classe I/IIa"
summary: "Struttura del fascicolo tecnico (allegato II + PMS allegato III) di un dispositivo medico di classe I o IIa e percorso di valutazione della conformita' (art. 52: classe I autodichiarazione; Is/Im/Ir; classe IIa allegato IX o XI) - Reg. (UE) 2017/745 (MDR)."
normative_refs:
  - "Regolamento (UE) 2017/745 (MDR) - art. 52, allegati II, III, VIII (classi I e IIa)"
version: 0.1.0-alpha
status: alpha
tags:
  - reg-ue-2017-745
  - mdr
  - dispositivi-medici
  - fascicolo-tecnico
  - marcatura-ce
---

# Fascicolo tecnico dispositivi medici (MDR Reg. UE 2017/745) - Classe I/IIa

## Quando usare questa skill

Usala quando, per un **dispositivo medico di classe I o IIa**, devi **strutturare
il fascicolo tecnico** (documentazione tecnica) e individuare il **percorso di
valutazione della conformita'** ai sensi del **Reg. (UE) 2017/745 (MDR)**:

- comporre i **sei capitoli** della documentazione tecnica dell'**allegato II**
  (descrizione e specifiche; informazioni fornite dal fabbricante; progettazione e
  fabbricazione; requisiti generali di sicurezza e prestazione - allegato I;
  analisi rischi/benefici e gestione del rischio; verifica e convalida, inclusa la
  valutazione clinica);
- comporre la documentazione sulla **sorveglianza post-commercializzazione**
  (**allegato III**: piano PMS, rapporto sulla sicurezza o PSUR);
- scegliere il percorso dell'**art. 52** (classe I in **autodichiarazione**;
  classe I **sterile/con funzione di misura/strumenti chirurgici riutilizzabili**
  con organismo notificato limitato; classe IIa con **allegato IX** o **XI**).

**Non e' una skill di classificazione ne' di merito clinico**: non applica le
regole dell'allegato VIII (la classe e' un input), non redige la valutazione
clinica ne' individua le norme armonizzate.

## Cosa NON fa (limiti)

- Non **classifica** il dispositivo (regole allegato VIII): la classe I/IIa e' un
  **input**.
- Non redige il **contenuto tecnico/clinico** (valutazione clinica, prove, gestione
  del rischio): ne struttura le sezioni.
- Non individua le **norme armonizzate** (a pagamento) ne' gli **MDCG guidance**.
- Non copre **IVDR** (Reg. 2017/746), dispositivi su misura, indagini cliniche,
  EUDAMED, classi IIb/III se non nel rinvio.

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`struttura-fascicolo-tecnico`](tasks/struttura-fascicolo-tecnico.md) | Compone i sei capitoli della documentazione tecnica (allegato II) e la documentazione PMS (allegato III) per il dispositivo |
| [`scegli-percorso-conformita`](tasks/scegli-percorso-conformita.md) | Data la classe (I, Is/Im/Ir, IIa), individua il percorso di valutazione della conformita' (art. 52) e il ruolo dell'organismo notificato |

## Riferimenti normativi

- **Regolamento (UE) 2017/745 (MDR)** - **allegato II** (documentazione tecnica),
  **allegato III** (documentazione tecnica sulla sorveglianza
  post-commercializzazione), **art. 52** (procedure di valutazione della
  conformita'), **allegato VIII** (regole di classificazione - citato).

Dettaglio in `references/sources.yaml`, `references/fonti/reg-ue-2017-745-mdr.md`,
`references/estratti/fascicolo-tecnico-mdr-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: la classificazione del dispositivo, la
valutazione clinica, la gestione del rischio, le prove e la responsabilita' della
conformita' e della marcatura CE restano in capo al **fabbricante** e ai
professionisti competenti (e all'organismo notificato ove richiesto). La skill
**non sostituisce** il fabbricante, il valutatore clinico ne' l'organismo
notificato.

> Nota sull'area di catalogo: il dispositivo medico e' un prodotto immesso sul
> mercato con documentazione tecnica e marcatura CE; la skill e' classificata in
> `impianti-macchine-prodotti` (compliance di prodotto), coerentemente con le
> altre skill di conformita' di prodotto del catalogo.
