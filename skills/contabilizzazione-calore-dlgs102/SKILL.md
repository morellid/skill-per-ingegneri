---
name: contabilizzazione-calore-dlgs102
description: "Supporto documentale all'inquadramento degli obblighi di contabilizzazione del calore e di ripartizione delle spese negli edifici e condomini con impianto centralizzato o allacciamento a teleriscaldamento/teleraffrescamento, ai sensi del D.Lgs. 102/2014, art. 9, comma 5 (e commi 5-bis, 5-ter, 5-quater). Aiuta a individuare gli obblighi: contatore di fornitura in corrispondenza dello scambiatore/punto di fornitura dell'edificio (lett. a), sotto-contatori per ciascuna unita' immobiliare ove tecnicamente possibile ed efficiente in termini di costi con la metodologia UNI EN 15459, con esenzioni da riportare in relazione tecnica del progettista/tecnico abilitato (lett. b), in alternativa sistemi di termoregolazione e contabilizzazione del calore individuali (ripartitori) per corpo scaldante (lett. c), e la ripartizione delle spese attribuendo una quota di almeno il 50 per cento ai prelievi volontari e la quota residua per millesimi/superfici/volumi/potenze (UNI 10200) (lett. d); la lettura da remoto entro il 1 gennaio 2027 (comma 5-bis), il divieto di deroga per le nuove costruzioni (comma 5-ter) e la guida ENEA per differenze di fabbisogno superiori al 50 per cento (comma 5-quater). Use when a designer, thermotechnician or building manager must frame the heat-metering and cost-allocation obligations in a centralized/district-heating building under Italian law; it is a documentary aid, does not compute the thermal thousandths or the shares (UNI 10200/EN 15459), does not draft the exemption technical report or the allocation table and does not replace the designer, the thermotechnician or the building administrator."
license: MIT
area: energia-incentivi
title: "Contabilizzazione del calore e ripartizione delle spese - D.Lgs. 102/2014 art. 9"
summary: "Contabilizzazione del calore e ripartizione spese in condomini centralizzati/teleriscaldati (D.Lgs. 102/2014 art. 9 c. 5): contatore di fornitura, sotto-contatori (UNI EN 15459) o ripartitori, quota >= 50% ai prelievi volontari e residua UNI 10200; lettura da remoto."
normative_refs:
  - "D.Lgs. 4/7/2014 n. 102 - art. 9 c. 5 (contabilizzazione del calore e ripartizione delle spese)"
  - "D.Lgs. 4/7/2014 n. 102 - art. 9 cc. 5-bis, 5-ter, 5-quater (lettura da remoto, nuove costruzioni, guida ENEA)"
version: 0.1.0-alpha
status: alpha
tags:
  - dlgs-102-2014
  - contabilizzazione-calore
  - ripartizione-spese
  - condominio
  - efficienza-energetica
  - teleriscaldamento
---

# Contabilizzazione del calore e ripartizione delle spese - D.Lgs. 102/2014 art. 9

## Quando usare questa skill

Usala quando devi **inquadrare gli obblighi di contabilizzazione del calore** e di
**ripartizione delle spese** in un edificio o condominio con **impianto centralizzato**
o **allacciamento a teleriscaldamento/teleraffrescamento**, ancorandoli al **D.Lgs.
102/2014, art. 9, comma 5** (e commi 5-bis/5-ter/5-quater):

- **contatore di fornitura** (lett. a): allo **scambiatore** di collegamento alla rete
  o al **punto di fornitura** dell'edificio/condominio (obbligo dal 30/6/2017);
- **sotto-contatori** per **ciascuna unita' immobiliare** (lett. b): obbligatori ove
  **tecnicamente possibile** ed **efficiente in termini di costi** (metodologia **UNI
  EN 15459**); i casi di impossibilita'/inefficienza vanno motivati in **relazione
  tecnica** del progettista o tecnico abilitato;
- in **alternativa** (lett. c): **sistemi di termoregolazione e contabilizzazione del
  calore individuali** (ripartitori) per **corpo scaldante**, salvo inefficienza in
  termini di costi (UNI EN 15459);
- **ripartizione delle spese** (lett. d): quota di **almeno il 50%** ai **prelievi
  volontari** di energia termica; la **quota residua** per **millesimi, superfici,
  volumi o potenze installate** (norma **UNI 10200**); prima stagione termica possibile
  ai soli millesimi;
- **lettura da remoto** entro il **1 gennaio 2027** (c. 5-bis); **divieto di deroga**
  per **nuove costruzioni** (c. 5-ter); **guida ENEA** per differenze di fabbisogno
  termico **> 50%** (c. 5-quater).

**Non e' una skill di calcolo**: non determina i millesimi termici ne' le quote (UNI
10200/EN 15459), non redige la relazione tecnica di esenzione ne' la tabella di
ripartizione e non sostituisce il progettista/termotecnico o l'amministratore.

## Cosa NON fa (limiti)

- Non **calcola** i **millesimi termici**, le quote di ripartizione ne' la verifica di
  **efficienza in termini di costi** (UNI 10200, UNI EN 15459 - non riprodotte).
- Non **redige** la **relazione tecnica** di impossibilita'/inefficienza (lett. b/c)
  ne' la **tabella millesimale** di ripartizione.
- Non riproduce i **provvedimenti ARERA** (commi 1-4, sistemi di misurazione
  intelligenti) ne' le regole di **fatturazione** di dettaglio.
- Non tratta la **diagnosi energetica** (art. 8 - vedi `diagnosi-energetica-dlgs102`)
  ne' l'esercizio/manutenzione degli impianti termici (DPR 74/2013).

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`verifica-obbligo-contabilizzazione`](tasks/verifica-obbligo-contabilizzazione.md) | Individua gli obblighi applicabili (contatore di fornitura, sotto-contatori o ripartitori) e i presupposti di esenzione con relazione tecnica (art. 9 c. 5 a-c, 5-bis, 5-ter) |
| [`imposta-ripartizione-spese`](tasks/imposta-ripartizione-spese.md) | Imposta lo schema di ripartizione delle spese: quota >= 50% ai prelievi volontari e quota residua (millesimi/mq/mc/potenze, UNI 10200), con i casi particolari (art. 9 c. 5 d, 5-quater) |

## Riferimenti normativi

- **D.Lgs. 4/7/2014 n. 102** (efficienza energetica, dir. 2012/27/UE) - **art. 9,
  comma 5** (contabilizzazione del calore e ripartizione delle spese) e commi
  **5-bis** (lettura da remoto), **5-ter** (nuove costruzioni), **5-quater** (guida
  ENEA).

Dettaglio in `references/sources.yaml`,
`references/fonti/dlgs-102-2014-art-9.md`,
`references/estratti/contabilizzazione-calore-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: il calcolo dei millesimi termici e delle quote, la
verifica di efficienza in termini di costi, la stesura della relazione tecnica e della
tabella di ripartizione e ogni scelta sul caso concreto restano in capo al
**progettista/termotecnico** e all'**amministratore/condominio**, con le norme tecniche
(UNI 10200, UNI EN 15459). **Non sostituisce** il progettista, il termotecnico ne'
l'amministratore, ne' la lettura dell'art. 9 del D.Lgs. 102/2014.
