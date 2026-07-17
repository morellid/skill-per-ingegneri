---
name: responsabilita-appaltatore-rovina-cc
description: "Supporto documentale alla responsabilità dell'appaltatore per difformità e vizi dell'opera e per la rovina e i gravi difetti degli edifici, secondo il Codice civile, artt. 1667, 1668, 1669. Aiuta a inquadrare la garanzia per difformità e vizi dell'opera e la sua esclusione quando il committente ha accettato l'opera e i vizi erano conosciuti o riconoscibili, salvo che siano stati taciuti in mala fede, con la denuncia a pena di decadenza entro sessanta giorni dalla scoperta (non necessaria se i vizi sono riconosciuti od occultati) e la prescrizione dell'azione in due anni dalla consegna, oltre all'eccezione del committente convenuto per il pagamento (art. 1667), il contenuto della garanzia con la scelta tra eliminazione dei vizi a spese dell'appaltatore o riduzione proporzionale del prezzo, salvo il risarcimento del danno in caso di colpa, e la risoluzione del contratto se l'opera è del tutto inadatta alla destinazione (art. 1668) e la responsabilità per rovina e gravi difetti di edifici o altre cose immobili destinate a lunga durata, per la quale l'appaltatore risponde per dieci anni dal compimento verso il committente e i suoi aventi causa quando l'opera, per vizio del suolo o difetto di costruzione, rovina in tutto o in parte o presenta evidente pericolo di rovina o gravi difetti, con denuncia entro un anno dalla scoperta e prescrizione in un anno dalla denuncia (art. 1669). Use when an engineer, works director, or CTU must frame the contractor's liability for defects of the work or for the ruin and serious defects of a building, its terms and remedies, under Italian Civil Code arts. 1667-1669; it is a documentary aid and does NOT ascertain the defects, the causal link, or the quantum, does NOT give case-law interpretation, and does NOT replace the lawyer, the court-appointed expert, or the judge."
license: MIT
area: forense
title: "Responsabilità dell'appaltatore: vizi e rovina d'edificio (c.c. 1667-1669)"
summary: "Responsabilità dell'appaltatore: garanzia per difformità e vizi, denuncia entro 60 giorni e prescrizione biennale (art. 1667), rimedi e risoluzione (art. 1668), rovina e gravi difetti di edifici con responsabilità decennale, denuncia e prescrizione annuale (art. 1669)."
normative_refs:
  - "Codice civile (R.D. 262/1942) - artt. 1667, 1668, 1669 (appalto)"
  - "Richiamati (non trascritti): artt. 1655, 1660-1666, 1670-1676; interpretazione giurisprudenziale dell'art. 1669"
version: 0.1.0-alpha
status: alpha
tags:
  - responsabilita-appaltatore
  - rovina-edificio
  - vizi-opera
  - codice-civile
  - forense
---

# Responsabilità dell'appaltatore: vizi e rovina d'edificio (c.c. 1667-1669)

## Quando usare questa skill

Usala quando un **ingegnere, direttore dei lavori o CTU** deve inquadrare la **responsabilità
dell'appaltatore** per i difetti dell'opera o per la **rovina e i gravi difetti** di un edificio,
secondo il **Codice civile, artt. 1667, 1668, 1669**:

- distinguere la **garanzia per vizi** (art. 1667-1668) dalla **responsabilità per rovina/gravi
  difetti** degli immobili (art. 1669);
- individuare i **termini** (denuncia, decadenza, prescrizione) applicabili;
- inquadrare i **rimedi** esperibili dal committente.

Per la **relazione del CTU** vedi `relazione-peritale-ctu-cpc`; per l'**ATP/CTP preventiva** vedi
`accertamento-tecnico-preventivo-cpc` (se in catalogo). Questa copre il **regime sostanziale** della
responsabilità dell'appaltatore.

## Garanzia per difformità e vizi (art. 1667)

L'appaltatore è tenuto alla **garanzia** per **difformità** e **vizi** dell'opera. La garanzia **non
è dovuta** se il committente ha **accettato** l'opera e i vizi erano **conosciuti** o **riconoscibili**
(salvo che siano stati **taciuti in mala fede**). Il committente deve **denunziare** i vizi **a pena
di decadenza entro 60 giorni** dalla scoperta (denuncia **non necessaria** se l'appaltatore li ha
**riconosciuti** od **occultati**). L'azione **si prescrive in 2 anni** dalla **consegna**. Il
committente **convenuto per il pagamento** può **sempre** far valere la garanzia in **eccezione**,
purché i vizi siano stati denunziati nei 60 giorni e prima dei 2 anni.

## Contenuto della garanzia (art. 1668)

Il committente può chiedere, a scelta: l'**eliminazione** dei vizi **a spese dell'appaltatore** o la
**riduzione proporzionale del prezzo**, **salvo** il **risarcimento del danno** in caso di **colpa**
dell'appaltatore. Se i vizi rendono l'opera **del tutto inadatta** alla destinazione, il committente
può chiedere la **risoluzione del contratto**.

## Rovina e gravi difetti di immobili (art. 1669)

Per **edifici** o altre **cose immobili** destinate **a lunga durata**: se, nel corso di **10 anni
dal compimento**, l'opera — **per vizio del suolo** o **difetto della costruzione** — **rovina** in
tutto o in parte, ovvero presenta **evidente pericolo di rovina** o **gravi difetti**, l'appaltatore è
**responsabile** verso il **committente** e i suoi **aventi causa**, purché la **denuncia** sia fatta
**entro 1 anno** dalla **scoperta**. Il diritto del committente **si prescrive in 1 anno** dalla
**denuncia**.

> L'art. 1669 configura, secondo la **giurisprudenza**, una responsabilità di **ordine pubblico**
> (con applicazioni anche a interventi su edifici esistenti e a soggetti diversi dal solo
> appaltatore): profili da valutare con il legale, non riprodotti dalla skill.

## Cosa NON fa (limiti)

- **Non accerta** i **vizi**/la **rovina**, il **nesso causale** o il **quantum** del danno.
- **Non fornisce** l'**interpretazione giurisprudenziale** dell'art. 1669 (ambito, natura, soggetti
  responsabili) né la strategia processuale.
- **Non sostituisce** il **legale**, il **CTU** o il **giudice**; non tratta gli altri articoli del
  Capo VII (nozione, variazioni, verifica/accettazione) se non come richiamo.

## Sotto-attività

| Task | Descrizione |
|---|---|
| [`inquadra-garanzia-vizi`](tasks/inquadra-garanzia-vizi.md) | Inquadra la garanzia per difformità/vizi (art. 1667), i termini (60 gg, 2 anni) e i rimedi (art. 1668) |
| [`inquadra-rovina-1669`](tasks/inquadra-rovina-1669.md) | Verifica i presupposti e i termini della responsabilità per rovina e gravi difetti (art. 1669) |

## Riferimenti normativi

- **Codice civile** (R.D. 262/1942), Capo VII (appalto) - **art. 1667** (difformità e vizi:
  garanzia, denuncia 60 gg, prescrizione 2 anni), **art. 1668** (contenuto della garanzia:
  eliminazione/riduzione/risarcimento/risoluzione), **art. 1669** (rovina e gravi difetti di
  immobili: responsabilità decennale, denuncia e prescrizione annuale).
- **Richiamati** (non trascritti): artt. **1655** (nozione), **1660-1666** (variazioni, verifica,
  accettazione), **1670-1676**; **interpretazione giurisprudenziale** dell'art. 1669.

Dettaglio in `references/sources.yaml`, `references/fonti/cc-artt-1667-1668-1669.md`,
`references/estratti/responsabilita-appaltatore-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: l'**accertamento tecnico** dei vizi/della rovina, la valutazione
del **nesso causale** e del **quantum**, l'**interpretazione** dell'art. 1669 e la strategia
processuale restano responsabilità del **legale**, del **CTU** e del **giudice**, sul testo vigente
del Codice civile e sulla giurisprudenza.
La skill **non sostituisce** tali soggetti né la lettura degli articoli richiamati.
