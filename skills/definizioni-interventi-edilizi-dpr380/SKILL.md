---
name: definizioni-interventi-edilizi-dpr380
description: "Supporto documentale alla qualificazione dell'intervento edilizio secondo le definizioni dell'art. 3 del D.P.R. 380/2001 (Testo unico edilizia). Aiuta a inquadrare un intervento in una delle categorie: manutenzione ordinaria (riparazione/rinnovamento/sostituzione delle finiture e degli impianti tecnologici; lett. a), manutenzione straordinaria (opere anche strutturali, servizi igienico-sanitari e tecnologici, frazionamento/accorpamento senza modifica della volumetria complessiva e dell'originaria destinazione d'uso, modifiche ai prospetti per l'agibilita'/accesso; lett. b), restauro e risanamento conservativo (conservazione dell'organismo edilizio nel rispetto degli elementi tipologici/formali/strutturali; lett. c), ristrutturazione edilizia (trasformazione, anche demolizione e ricostruzione con diversa sagoma/sedime salvo vincoli e zone A; lett. d), nuova costruzione (trasformazione del territorio non riconducibile alle altre categorie, con i sottocasi e.1-e.7: manufatti, urbanizzazioni, infrastrutture, torri/tralicci, manufatti leggeri/roulotte, pertinenze oltre il 20%, depositi; lett. e) e ristrutturazione urbanistica (sostituzione del tessuto urbanistico-edilizio; lett. f), con la prevalenza delle definizioni sugli strumenti urbanistici. Use when a designer, technician or applicant must classify a building intervention into the DPR 380 categories before choosing the title or filing; it is a documentary aid, does not select the building title (CILA/SCIA/permit), does not draft the application and does not replace the designer or the Municipality."
license: MIT
area: edilizia-urbanistica-catasto
title: "Definizioni degli interventi edilizi - DPR 380/2001 art. 3"
summary: "Qualificazione dell'intervento edilizio (art. 3 DPR 380/2001): manutenzione ordinaria (a) e straordinaria (b), restauro e risanamento conservativo (c), ristrutturazione edilizia (d, anche demo-ricostruzione), nuova costruzione (e, casi e.1-e.7) e ristrutturazione urbanistica (f)."
normative_refs:
  - "D.P.R. 6/6/2001 n. 380 - art. 3 (definizioni degli interventi edilizi, lett. a-f)"
  - "D.P.R. 6/6/2001 n. 380 - art. 3 c. 2 (prevalenza delle definizioni sugli strumenti urbanistici)"
version: 0.1.0-alpha
status: alpha
tags:
  - dpr-380-2001
  - testo-unico-edilizia
  - interventi-edilizi
  - ristrutturazione
  - manutenzione-straordinaria
  - nuova-costruzione
---

# Definizioni degli interventi edilizi - DPR 380/2001 art. 3

## Quando usare questa skill

Usala quando devi **qualificare un intervento edilizio** in una delle categorie
definite dall'**art. 3 del D.P.R. 380/2001** (Testo unico edilizia), prima di
scegliere il titolo o presentare la pratica:

- **manutenzione ordinaria** (lett. a): riparazione, rinnovamento e sostituzione
  delle **finiture** e opere per mantenere in efficienza gli **impianti tecnologici**
  esistenti;
- **manutenzione straordinaria** (lett. b): opere e modifiche anche **strutturali**,
  servizi igienico-sanitari e tecnologici, **frazionamento/accorpamento** di unita'
  immobiliari, **senza** alterare la **volumetria complessiva** e mantenendo
  l'**originaria destinazione d'uso**; modifiche ai **prospetti** per agibilita'/
  accesso a certe condizioni;
- **restauro e risanamento conservativo** (lett. c): conservazione dell'organismo
  edilizio nel rispetto degli **elementi tipologici, formali e strutturali**;
- **ristrutturazione edilizia** (lett. d): trasformazione, incluse **demolizione e
  ricostruzione** con diversi sagoma/prospetti/sedime (salvo **vincoli** ex D.Lgs.
  42/2004 e **zone A**, dove servono stessi sagoma/sedime e nessun incremento di
  volume); ripristino di edifici crollati/demoliti se ne e' accertabile la
  preesistente consistenza;
- **nuova costruzione** (lett. e): trasformazione del territorio **non** riconducibile
  alle altre categorie, con i **sottocasi e.1-e.7** (manufatti fuori terra/interrati o
  ampliamenti fuori sagoma; urbanizzazioni; infrastrutture/impianti; **torri e
  tralicci**; **manufatti leggeri/roulotte/case mobili** stabili; **pertinenze** oltre
  il **20%** del volume o qualificate dagli strumenti urbanistici; depositi/impianti
  produttivi all'aperto);
- **ristrutturazione urbanistica** (lett. f): sostituzione del **tessuto
  urbanistico-edilizio** esistente con altro diverso.

Le definizioni **prevalgono** sulle disposizioni degli strumenti urbanistici generali
e dei regolamenti edilizi (c. 2).

**Non e' una skill che sceglie il titolo o redige la pratica**: qualifica la categoria
dell'intervento; la scelta del titolo (CILA/SCIA/PdC) e l'istruttoria restano ad altre
skill / al Comune.

## Cosa NON fa (limiti)

- Non **sceglie il titolo edilizio** (edilizia libera / CILA / SCIA / SCIA alternativa
  / permesso di costruire): rinvio a `modulistica-edilizia-unificata`; per il regime
  del permesso vedi `permesso-costruire-dpr380`.
- Non **redige** la pratica, gli elaborati o l'asseverazione.
- Non **applica** le tolleranze/sanatorie del **Salva Casa** ne' valuta lo **stato
  legittimo** (art. 9-bis): fornisce solo le definizioni dell'art. 3.
- Non tratta il **mutamento di destinazione d'uso** (art. 23-ter) ne' i vincoli
  **paesaggistici/culturali** (D.Lgs. 42/2004): sono citati come rinvio.

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`qualifica-intervento`](tasks/qualifica-intervento.md) | Colloca un intervento in una categoria dell'art. 3 (a-f) applicando i criteri distintivi (volumetria, destinazione d'uso, elementi tipologici, sagoma/sedime, vincoli) |
| [`distingui-nuova-costruzione`](tasks/distingui-nuova-costruzione.md) | Verifica se un intervento ricade nella nuova costruzione (lett. e) applicando i sottocasi e.1-e.7 (manufatti, pertinenze oltre il 20%, manufatti leggeri, ecc.) |

## Riferimenti normativi

- **D.P.R. 6/6/2001 n. 380** (Testo unico edilizia) - **art. 3** (Definizioni degli
  interventi edilizi, lett. a-f; c. 2 prevalenza sugli strumenti urbanistici).

Dettaglio in `references/sources.yaml`,
`references/fonti/dpr-380-2001-art-3.md`,
`references/estratti/definizioni-interventi-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: la qualificazione definitiva dell'intervento, la
scelta del titolo, l'applicazione del Salva Casa e ogni determinazione sul caso
concreto restano in capo al **progettista** e al **Comune**, con le leggi regionali
applicabili. **Non sostituisce** il progettista ne' il Comune, ne' la lettura dell'art.
3 del D.P.R. 380/2001.
