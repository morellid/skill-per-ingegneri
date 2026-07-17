---
name: ponteggi-fissi-pimus-dlgs81
description: "Supporto documentale al tecnico (ingegnere/architetto/geometra), all'impresa/datore di lavoro e al preposto per i ponteggi fissi a elementi portanti prefabbricati e per il Pi.M.U.S. (piano di montaggio, uso e smontaggio), ai sensi del D.Lgs. 9 aprile 2008, n. 81 (Testo unico sicurezza), Titolo IV, Capo II, Sezione V, artt. 131-138. Aiuta a stabilire quando il ponteggio deve essere eretto in base a un progetto - altezza superiore a 20 metri, configurazioni non coperte dagli schemi-tipo dell'autorizzazione, o altre opere provvisionali di notevole importanza e complessita' - con calcolo di resistenza e stabilita' e disegno esecutivo firmati da un ingegnere o architetto abilitato (art. 133); a inquadrare l'esenzione dal calcolo per i montaggi entro schema-tipo e l'obbligo di riportare subito le modifiche sul disegno (artt. 132 c. 1 lett. g, 134 c. 2); la documentazione da tenere ed esibire in cantiere agli organi di vigilanza, cioe' l'autorizzazione ministeriale, il progetto e i disegni esecutivi e il Pi.M.U.S. per i lavori in quota, i cui contenuti sono nell'allegato XXII (artt. 133 c. 3, 134 c. 1); il Pi.M.U.S. redatto dal datore di lavoro a mezzo di persona competente, la sorveglianza del preposto sul montaggio/smontaggio/trasformazione conforme al piano e la formazione teorico-pratica degli addetti secondo l'allegato XXI (art. 136); l'autorizzazione ministeriale alla costruzione e all'impiego chiesta dal fabbricante con relazione tecnica e rinnovo decennale (artt. 131-132, 135); la manutenzione e revisione periodica del preposto e le norme particolari su parapetti, fermapiede e distacco delle tavole (artt. 137-138). Use when a designer, contractor, employer, or supervisor must frame scaffolding obligations, the need for a signed scaffold design, the on-site documentation, or the Pi.M.U.S. under D.Lgs. 81/2008; it is a documentary aid and does NOT draft the design, technical report, or Pi.M.U.S., does NOT perform the strength and stability calculation, does NOT issue the ministerial authorization, does NOT reproduce annexes XVIII/XIX/XXI/XXII or the UNI EN 12810/12811/74 standards, and does NOT replace the qualified engineer/architect, the employer, the competent supervisor, or the enforcement bodies."
license: MIT
area: sicurezza-lavoro-cantieri
title: "Ponteggi fissi: progetto, documentazione e Pi.M.U.S. (D.Lgs. 81/2008)"
summary: "Inquadra gli adempimenti sui ponteggi fissi (D.Lgs. 81/2008 artt. 131-138): quando serve il progetto firmato da ingegnere/architetto (>20 m o fuori schema-tipo, art. 133), la documentazione in cantiere e il Pi.M.U.S. con sorveglianza del preposto (art. 136). Non li redige."
normative_refs:
  - "D.Lgs. 9 aprile 2008, n. 81 (Testo unico sicurezza) - Titolo IV, Capo II, Sezione V (Ponteggi fissi), artt. 131-138: progetto firmato (art. 133), documentazione (art. 134), Pi.M.U.S. (art. 136)"
  - "Rinvio (non riprodotti): Allegati XVIII/XIX (ponteggi), XXI (formazione), XXII (contenuti Pi.M.U.S.); UNI EN 12810/12811/74; D.Lgs. 106/2009 (modifiche ad artt. 131, 136, 137, 138)"
version: 0.1.0-alpha
status: alpha
tags:
  - ponteggi-fissi
  - pimus
  - dlgs-81-2008
  - lavori-in-quota
  - sicurezza-cantieri
---

# Ponteggi fissi: progetto, documentazione e Pi.M.U.S. (D.Lgs. 81/2008 artt. 131-138)

## Quando usare questa skill

Usala quando un **tecnico** (ingegnere/architetto/geometra), un'**impresa/datore di lavoro** o un
**preposto** deve **inquadrare** gli adempimenti sui **ponteggi fissi** a elementi portanti
prefabbricati (metallici o non) e sul **Pi.M.U.S.** (piano di montaggio, uso e smontaggio), secondo il
**D.Lgs. 9 aprile 2008, n. 81** (Testo unico sicurezza), **Titolo IV, Capo II, Sezione V, artt.
131-138**:

- stabilire **quando serve il progetto** del ponteggio (calcolo di resistenza e stabilità + disegno
  esecutivo **firmati da un ingegnere o architetto abilitato**, art. 133);
- inquadrare l'**esenzione dal calcolo** per i montaggi **entro schema-tipo** dell'autorizzazione
  (artt. 132 c. 1 lett. g, 134 c. 2);
- sapere **quale documentazione tenere in cantiere** ed esibire agli organi di vigilanza (art. 134);
- inquadrare il **Pi.M.U.S.**, la **sorveglianza del preposto** e la **formazione** degli addetti
  (art. 136).

**Non è** uno strumento che redige il progetto/relazione/Pi.M.U.S., né esegue il calcolo di resistenza
e stabilità, né rilascia l'autorizzazione ministeriale: è un **supporto documentale** che inquadra
obblighi, soggetti e contenuti.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-progetto-documentazione` | Stabilisce se il ponteggio richiede il progetto firmato (art. 133) o rientra in schema-tipo, e quale documentazione va tenuta in cantiere (artt. 133 c. 3, 134) |
| `inquadra-pimus-montaggio` | Inquadra obbligo, redazione e contenuti del Pi.M.U.S., la sorveglianza del preposto e la formazione teorico-pratica degli addetti (art. 136) |

## Punti chiave (verificati sul testo)

- **Progetto** (art. 133): obbligatorio per ponteggi **> 20 m**, per configurazioni **fuori
  schema-tipo** e per **opere provvisionali di notevole importanza e complessità**; comprende
  **calcolo** e **disegno esecutivo**, **firmati da ingegnere/architetto abilitato**.
- **Documentazione in cantiere** (artt. 133 c. 3, 134 c. 1): autorizzazione ministeriale + istruzioni/
  schemi (art. 131 c. 6), progetto e disegni esecutivi (se dovuti), **Pi.M.U.S.** per lavori in quota
  (contenuti nell'**Allegato XXII**); da esibire agli organi di vigilanza. Modifiche **subito sul
  disegno**, entro lo schema-tipo (art. 134 c. 2).
- **Pi.M.U.S.** (art. 136): redatto dal **datore di lavoro a mezzo di persona competente**, in funzione
  della complessità; montaggio/smontaggio/trasformazione **sotto la diretta sorveglianza di un
  preposto**, conforme al piano, con lavoratori **formati** (teorico-pratica, Allegato XXI).
- **Autorizzazione ministeriale** (artt. 131-132, 135): chiesta dal **fabbricante** con **relazione
  tecnica**; **rinnovo ogni 10 anni**; marchio del fabbricante sugli elementi.
- **Manutenzione e norme particolari** (artt. 137-138): verifica periodica del **preposto**; distacco
  tavole dalla muratura **≤ 20 cm**; **parapetto ≥ 95 cm**, **fermapiede ≥ 15 cm**.

## Fonti

- **D.Lgs. 9 aprile 2008, n. 81** (Testo unico sicurezza) - Titolo IV, Capo II, Sezione V, **artt.
  131-138** - testo vigente su Normattiva (indice pinnato a `!vig=2026-07-17`, codice 008G0104,
  idGruppo 23). Artt. 131, 136, 137, 138 modificati dal D.Lgs. 106/2009.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non redige** il progetto, la relazione tecnica o il Pi.M.U.S.; **non esegue** il calcolo di
  resistenza e stabilità; **non rilascia** l'autorizzazione ministeriale.
- **Non riproduce** gli Allegati XVIII/XIX/XXI/XXII né le norme UNI EN 12810/12811/74.
- **Non tratta** i ponteggi in legno, i ponti su cavalletti e le altre opere provvisionali della
  Sezione IV se non nei richiami (artt. 125-126 per le deroghe dell'art. 138).

**La skill è un supporto documentale: non sostituisce l'ingegnere/architetto abilitato, il datore di
lavoro, il preposto competente o gli organi di vigilanza, né la lettura degli artt. 131-138 del D.Lgs.
81/2008 e dei relativi allegati.**
