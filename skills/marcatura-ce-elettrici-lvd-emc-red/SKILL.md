---
name: marcatura-ce-elettrici-lvd-emc-red
description: "Supporto documentale alla marcatura CE dei prodotti elettrici ed elettronici secondo le tre direttive di prodotto: bassa tensione (LVD 2014/35/UE), compatibilita' elettromagnetica (EMC 2014/30/UE) e apparecchiature radio (RED 2014/53/UE). Aiuta a individuare quale direttiva o combinazione di direttive si applica al prodotto (materiale elettrico 50-1000 V ca / 75-1500 V cc per la LVD; apparecchi con emissione/immunita' EMC; apparecchiature radio per la RED, che incorpora sicurezza LVD ed EMC), a scegliere la procedura di valutazione della conformita' e i moduli ammessi (Modulo A - controllo interno; esame UE del tipo B + conformita' al tipo C; garanzia di qualita' totale H) e a capire quando e' obbligatorio l'intervento di un organismo notificato (in particolare nella RED se non si applicano le norme armonizzate per i requisiti dell'art. 3.1), oltre a strutturare la documentazione tecnica, la dichiarazione UE di conformita' (anche semplificata per la RED) e l'apposizione della marcatura CE. Use when a manufacturer or electrical/electronic engineer must determine the applicable EU product directive(s), the conformity assessment route and the technical documentation for CE marking of an electrical, EMC-relevant or radio product; it is a documentary aid and does not identify the applicable harmonised standards, does not run the tests and does not draft the final declaration."
license: MIT
area: impianti-macchine-prodotti
title: "Marcatura CE prodotti elettrici - LVD 2014/35, EMC 2014/30, RED 2014/53"
summary: "Marcatura CE dei prodotti elettrici: quale direttiva si applica (LVD 2014/35 bassa tensione, EMC 2014/30, RED 2014/53 radio), procedura di conformita' e moduli (A; esame UE del tipo B+C; qualita' totale H), quando serve l'organismo notificato, documentazione e dichiarazione UE."
normative_refs:
  - "Direttiva 2014/35/UE (LVD - bassa tensione) - art. 1, all. I, III, IV"
  - "Direttiva 2014/30/UE (EMC) - all. I, art. 14, all. II-III"
  - "Direttiva 2014/53/UE (RED - apparecchiature radio) - art. 3, 17, all. II-VII"
version: 0.1.0-alpha
status: alpha
tags:
  - marcatura-ce
  - lvd-2014-35
  - emc-2014-30
  - red-2014-53
  - valutazione-conformita
---

# Marcatura CE prodotti elettrici - LVD 2014/35, EMC 2014/30, RED 2014/53

## Quando usare questa skill

Usala quando, per un **prodotto elettrico o elettronico**, devi impostare la
**marcatura CE** secondo le tre direttive di prodotto rilevanti:

- individuare **quale direttiva** (o combinazione) si applica: **LVD 2014/35/UE**
  (materiale elettrico 50-1000 V ca / 75-1500 V cc), **EMC 2014/30/UE**
  (compatibilita' elettromagnetica), **RED 2014/53/UE** (apparecchiature radio);
- scegliere la **procedura di valutazione della conformita'** e i **moduli**
  ammessi (Modulo **A** controllo interno; esame UE del tipo **B** + conformita'
  al tipo **C**; garanzia di qualita' totale **H**);
- capire **quando serve un organismo notificato** (in particolare nella RED se non
  si applicano le norme armonizzate per i requisiti dell'art. 3.1);
- strutturare la **documentazione tecnica**, la **dichiarazione UE di conformita'**
  (anche **semplificata** per la RED) e la **marcatura CE**.

**Non e' una skill di prova/progetto**: non individua le norme armonizzate
applicabili (EN a pagamento), non esegue le prove EMC/sicurezza/spettro e non
redige materialmente la documentazione.

## Cosa NON fa (limiti)

- Non individua le **norme armonizzate** applicabili (EN a pagamento): le cita.
- Non esegue ne' interpreta le **prove** (EMC, sicurezza elettrica, spettro radio).
- Non redige materialmente la **documentazione tecnica** ne' la **dichiarazione UE**:
  ne fornisce struttura e requisiti.
- Non copre altre direttive eventualmente applicabili (macchine 2023/1230, ATEX
  2014/34, ErP, RoHS): solo rinvio.

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`individua-direttive`](tasks/individua-direttive.md) | Dato il prodotto, determina quale/i direttiva/e si applica/applicano (LVD, EMC, RED) e come si combinano (la RED incorpora sicurezza LVD ed EMC) |
| [`scegli-procedura-conformita`](tasks/scegli-procedura-conformita.md) | Per ciascuna direttiva applicabile, individua la procedura di conformita' e i moduli ammessi, quando serve l'organismo notificato, e struttura documentazione, dichiarazione UE e marcatura CE |

## Riferimenti normativi

- **Direttiva 2014/35/UE (LVD)** - art. 1 (campo), all. I (obiettivi di sicurezza),
  all. III (Modulo A), all. IV (dichiarazione UE). Recepita in Italia dal D.Lgs.
  86/2016.
- **Direttiva 2014/30/UE (EMC)** - all. I (requisiti essenziali), art. 14
  (procedure), all. II-III (Moduli A; B+C). Recepita dal D.Lgs. 80/2016.
- **Direttiva 2014/53/UE (RED)** - art. 3 (requisiti essenziali), art. 17
  (procedure), all. II-IV (Moduli A; B+C; H), all. V-VII (documentazione tecnica,
  dichiarazioni UE). Recepita dal D.Lgs. 128/2016.

Dettaglio in `references/sources.yaml`, `references/fonti/`,
`references/estratti/marcatura-ce-elettrici-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: l'individuazione delle norme armonizzate
applicabili, l'esecuzione delle prove e la responsabilita' della conformita' e
della marcatura CE restano in capo al **fabbricante** (o al suo mandatario) e ai
laboratori/organismi competenti. La skill **non sostituisce** il fabbricante, il
laboratorio di prova ne' l'organismo notificato.
