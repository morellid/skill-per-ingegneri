---
name: contributo-costruzione-dpr380
description: "Supporto documentale all'inquadramento del contributo di costruzione dovuto per il rilascio del permesso di costruire (e per gli altri titoli edilizi onerosi), secondo il Testo Unico dell'edilizia (D.P.R. 6 giugno 2001, n. 380), artt. 16-19. Aiuta a stabilire se e in che misura e' dovuto il contributo, composto da oneri di urbanizzazione (primaria e secondaria) e costo di costruzione (art. 16), a gestire la rateizzazione e lo scomputo mediante esecuzione diretta delle opere di urbanizzazione (art. 16, c. 2), le modalita' e i tempi di corresponsione (oneri all'atto del rilascio; costo di costruzione in corso d'opera entro 60 giorni dall'ultimazione - art. 16, c. 3), il ruolo delle tabelle parametriche regionali e delle deliberazioni comunali (art. 16, cc. 4-6); a individuare i casi di riduzione (edilizia convenzionata, prima abitazione - art. 17, cc. 1-2) e di esonero (zone agricole, ristrutturazione e ampliamento entro il 20% di edifici unifamiliari, opere pubbliche o di interesse generale e di urbanizzazione, pubbliche calamita', fonti rinnovabili e risparmio energetico - art. 17, c. 3; immobili dello Stato e manutenzione straordinaria con aumento del carico urbanistico - art. 17, c. 4), la convenzione-tipo regionale (art. 18) e il contributo per opere o impianti non destinati alla residenza (industriali/artigianali; turistiche, commerciali e direzionali con quota non superiore al 10% del costo di costruzione - art. 19). Use when an engineer, architect, geometra, or SUE office must frame the building contribution (urbanization charges plus construction cost) for an Italian building permit, identify reductions and exemptions, or handle instalments and the direct execution of urbanization works under DPR 380/2001; it is a documentary aid and does NOT compute the amounts (which depend on regional parametric tables and municipal resolutions), does not replace the municipal technical office, and does not cover regional/municipal detail rules."
license: MIT
area: edilizia-urbanistica-catasto
title: "Contributo di costruzione: oneri e costo di costruzione (DPR 380/2001)"
summary: "Inquadra il contributo di costruzione del permesso di costruire (DPR 380/2001, artt. 16-19): oneri di urbanizzazione + costo di costruzione, rateizzazione e scomputo, riduzioni ed esoneri, convenzione-tipo, opere non residenziali. Non calcola gli importi (regionali/comunali)."
normative_refs:
  - "D.P.R. 6 giugno 2001, n. 380 (T.U. Edilizia) - artt. 16, 17, 18, 19"
version: 0.1.0-alpha
status: alpha
tags:
  - contributo-di-costruzione
  - oneri-di-urbanizzazione
  - costo-di-costruzione
  - dpr-380-2001
  - permesso-di-costruire
---

# Contributo di costruzione: oneri e costo di costruzione (DPR 380/2001)

## Quando usare questa skill

Usala quando un **ingegnere, architetto, geometra o ufficio SUE** deve **inquadrare il
contributo di costruzione** dovuto per il **permesso di costruire** (e per gli altri titoli
edilizi onerosi), secondo il **Testo Unico dell'edilizia (D.P.R. 380/2001)**, artt. 16-19:

- stabilire **se e in che misura** e' dovuto il contributo (oneri + costo di costruzione);
- gestire **rateizzazione**, **scomputo** e tempi di corresponsione;
- individuare **riduzioni** ed **esoneri**;
- applicare la **convenzione-tipo** e il contributo per le **opere non residenziali**.

Per determinare il **modulo edilizio** e il regime dell'intervento usa
`modulistica-edilizia-unificata`; per le **attivita' produttive** al SUAP usa
`regimi-suap-attivita-produttive-dlgs222`.

## Composizione del contributo (art. 16)

Il rilascio del permesso di costruire comporta un **contributo commisurato**:

- all'**incidenza degli oneri di urbanizzazione** (primaria e secondaria);
- al **costo di costruzione**.

**Oneri di urbanizzazione** (c. 2): corrisposti **all'atto del rilascio**, su richiesta
**rateizzabili**; il titolare puo' obbligarsi a **realizzare direttamente le opere** di
urbanizzazione a **scomputo** (totale/parziale), con modalita' e garanzie del comune e
acquisizione delle opere al patrimonio comunale.

**Costo di costruzione** (c. 3): **determinato all'atto del rilascio** e **corrisposto in
corso d'opera**, non oltre **60 giorni** dalla **ultimazione**.

**Incidenza e valori** (cc. 4-9): l'incidenza degli oneri e' stabilita con **deliberazione del
consiglio comunale** in base alle **tabelle parametriche regionali** (per classi di comuni:
demografia, geografia, destinazioni di zona, standard, incentivi alla ristrutturazione,
maggior valore da varianti). Il valore del **costo di costruzione** per la residenza e'
determinato ai sensi del **c. 9** (rinvio a DM/normativa e adeguamenti ISTAT).

## Riduzione ed esonero (art. 17)

- **Riduzione** - **edilizia convenzionata** (c. 1): contributo ridotto alla **sola quota degli
  oneri di urbanizzazione** (con convenzione ex art. 18); **prima abitazione** (c. 2): pari
  all'edilizia residenziale pubblica (se ne sussistono i requisiti).
- **Esonero** (c. 3): contributo **non dovuto** per: **zone agricole** (conduzione del fondo
  dell'imprenditore agricolo); **ristrutturazione e ampliamento <= 20%** di **edifici
  unifamiliari**; **opere pubbliche o di interesse generale** e opere di **urbanizzazione**;
  interventi per **pubbliche calamita'**; impianti/opere per **fonti rinnovabili, risparmio e
  uso razionale dell'energia**.
- **Casi particolari** (c. 4): immobili dello **Stato** e **manutenzione straordinaria** con
  aumento del **carico urbanistico** -> contributo commisurato alle **sole opere di
  urbanizzazione** (se aumenta la superficie calpestabile).

## Convenzione-tipo (art. 18)

Per l'edilizia convenzionata (art. 17, c. 1) la **regione** approva una **convenzione-tipo** con
criteri e parametri tabellari (caratteristiche degli alloggi, prezzi di cessione/canoni, ecc.),
a cui si uniformano le convenzioni e gli atti d'obbligo comunali.

## Opere non destinate alla residenza (art. 19)

- **Industriali/artigianali**: contributo pari all'incidenza delle **opere di urbanizzazione** +
  opere per **trattamento/smaltimento dei rifiuti** e **sistemazione dei luoghi** (parametri
  regionali per tipo di attivita').
- **Turistiche, commerciali e direzionali** o di servizi: incidenza delle **opere di
  urbanizzazione** (ex art. 16) + **quota <= 10%** del **costo documentato di costruzione**
  (deliberazione comunale per tipo di attivita').

## Cosa NON fa (limiti)

- **Non calcola gli importi**: le **tabelle** degli oneri e i **valori** del costo di costruzione
  sono di **regioni e comuni** (deliberazioni comunali su tabelle regionali).
- **Non sostituisce** l'ufficio tecnico comunale (SUE) ne' il computo del contributo nel caso
  concreto.
- **Non copre** la disciplina **regionale/comunale** di dettaglio (rateizzazione, garanzie,
  riduzioni ulteriori, SCIA onerosa, monetizzazioni), che va verificata.

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`inquadra-contributo`](tasks/inquadra-contributo.md) | Stabilisce se il contributo e' dovuto e in che misura (oneri + costo di costruzione), con riduzioni ed esoneri |
| [`gestisci-oneri-scomputo`](tasks/gestisci-oneri-scomputo.md) | Imposta rateizzazione, scomputo con esecuzione diretta delle opere di urbanizzazione e tempi di corresponsione |

## Riferimenti normativi

- **D.P.R. 6 giugno 2001, n. 380** (T.U. Edilizia) - **art. 16** (contributo: oneri di
  urbanizzazione e costo di costruzione; rateizzazione, scomputo, tabelle regionali), **art. 17**
  (riduzione ed esonero), **art. 18** (convenzione-tipo), **art. 19** (opere non destinate alla
  residenza).

Dettaglio in `references/sources.yaml`, `references/fonti/dpr-380-2001-artt16-19.md`,
`references/estratti/contributo-costruzione-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: la determinazione del contributo e la sua quantificazione
restano responsabilita' del professionista e dell'**ufficio tecnico comunale (SUE)**, sulle
tabelle regionali e le deliberazioni comunali vigenti. La skill **non sostituisce** l'ufficio tecnico comunale, il calcolo del contributo ne' la lettura del D.P.R. 380/2001 e della normativa regionale/comunale applicabile.
