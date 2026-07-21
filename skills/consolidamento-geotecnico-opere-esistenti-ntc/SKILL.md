---
name: consolidamento-geotecnico-opere-esistenti-ntc
description: "Supporto documentale al progettista geotecnico e strutturale per l'inquadramento della progettazione degli interventi di consolidamento geotecnico di opere esistenti (sottofondazioni, rinforzo delle fondazioni, miglioramento del terreno di fondazione) secondo le NTC 2018 (DM 17 gennaio 2018), paragrafo 6.10. Aiuta a inquadrare l'ambito (provvedimenti tecnici sul sistema manufatto-terreno per eliminare o mitigare difetti di comportamento di un'opera esistente); i criteri generali di progetto (individuazione delle cause del comportamento anomalo - sovrastruttura, strutture di fondazione, terreno di fondazione; cause di anomali spostamenti del terreno da modifiche del manufatto, variazioni delle pressioni interstiziali, manufatti adiacenti, modifiche del profilo topografico o movimenti di massa, deterioramento dei materiali; progetto sviluppato unitariamente con quello strutturale e congiuntamente al risanamento della struttura in elevazione; modalita' esecutive e opere provvisionali parte integrante del progetto; metodo osservazionale ammesso quando la complessita' del sottosuolo e' documentata) (6.10.1); le indagini geotecniche e la caratterizzazione (indagini su terreno e fondazioni esistenti basate sulla documentazione disponibile, cautele per manufatti sensibili agli spostamenti, misura dei caratteri cinematici dei movimenti in atto e della variazione nel tempo di pressioni interstiziali e spostamenti nel volume significativo, misure protratte per fenomeni stagionali) (6.10.2); i tipi di consolidamento geotecnico (miglioramento/rinforzo dei terreni di fondazione, miglioramento/rinforzo dei materiali della fondazione, ampliamento della base della fondazione superficiale, trasferimento del carico a strati piu' profondi, introduzione di sostegni laterali, rettifica degli spostamenti del piano di posa; valutazione della ridistribuzione delle sollecitazioni a breve e lungo termine; particolari cautele per interventi con variazioni di volume come congelamento, iniezioni e gettiniezione) (6.10.3); e i controlli e il monitoraggio (controllo dell'efficacia obbligatorio quando l'intervento comporta una ridistribuzione delle sollecitazioni al contatto terreno-manufatto, ampiezza commisurata a importanza dell'opera, tipo di difetto e danni possibili; monitoraggio previsto in progetto con esiti come elemento di collaudo) (6.10.4). Use when a geotechnical or structural designer must frame the design of geotechnical consolidation (underpinning, foundation strengthening) of an existing structure under the Italian NTC 2018 par. 6.10; it is a documentary aid and does NOT compute or size the interventions, does NOT define the geotechnical model nor design the structural repair, does NOT cover general ground improvement (par. 6.9), the seismic assessment of existing buildings (Chap. 8) nor the seismic design, and does NOT replace the designer or the 2019 Circular."
license: MIT
area: strutture-geotecnica
title: "Consolidamento geotecnico di opere esistenti (NTC 2018 par. 6.10)"
summary: "Inquadra il consolidamento geotecnico di opere esistenti (sottofondazioni, rinforzo fondazioni) - NTC 2018 par. 6.10: cause, progetto unitario geotecnico-strutturale, sei tipi di consolidamento, cautele (iniezioni), controllo obbligatorio con ridistribuzione sollecitazioni."
normative_refs:
  - "NTC 2018 (D.M. 17 gennaio 2018) - par. 6.10: consolidamento geotecnico di opere esistenti; sei tipi (6.10.3), progetto unitario con lo strutturale (6.10.1), cautele per iniezioni e congelamento"
  - "NTC 2018 - par. 6.10.2/6.10.4: indagini su manufatto e terreno, grandezze cinematiche e pressioni interstiziali; controllo obbligatorio se ridistribuzione delle sollecitazioni terreno-manufatto"
version: 0.1.0-alpha
status: alpha
tags:
  - consolidamento-geotecnico
  - opere-esistenti
  - sottofondazioni
  - geotecnica
  - ntc-2018
---

# Consolidamento geotecnico di opere esistenti (NTC 2018 par. 6.10)

## Quando usare questa skill

Usala quando un **progettista geotecnico** o **strutturale** deve **inquadrare la progettazione degli interventi
di consolidamento geotecnico di un'opera esistente** (sottofondazioni, rinforzo delle fondazioni, miglioramento
del terreno di fondazione) secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 6.10**:

- **criteri generali di progetto** (§6.10.1);
- **indagini geotecniche e caratterizzazione** (§6.10.2);
- **tipi di consolidamento geotecnico** (§6.10.3);
- **controlli e monitoraggio** (§6.10.4).

**Non è** uno strumento che calcola o dimensiona gli interventi: è un **supporto documentale** che inquadra
criteri, indagini, tipi di consolidamento e controlli. Complementa `costruzioni-esistenti-ntc-cap8` (che
classifica strutturalmente l'esistente: LC/FC, adeguamento/miglioramento) e `relazione-geologica-geotecnica-ntc`
(che esclude i §6.3-6.12).

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-criteri-tipi-consolidamento` | Cause del comportamento anomalo, progetto unitario geotecnico-strutturale, i sei tipi di consolidamento e le cautele per gli interventi con variazioni di volume (§6.10.1, 6.10.3) |
| `inquadra-indagini-controlli-consolidamento` | Indagini su manufatto e terreno, grandezze cinematiche e pressioni interstiziali, controllo obbligatorio con ridistribuzione delle sollecitazioni, monitoraggio e collaudo (§6.10.2, 6.10.4) |

## Punti chiave (verificati sul testo)

- **Ambito** (§6.10): provvedimenti sul sistema manufatto-terreno per eliminare o mitigare difetti di
  comportamento di un'opera esistente.
- **Criteri generali** (§6.10.1): individuazione delle **cause** (sovrastruttura, fondazioni, terreno); progetto
  sviluppato **unitariamente con quello strutturale** e congiuntamente al risanamento della struttura in
  elevazione; modalità esecutive e opere provvisionali parte integrante; **metodo osservazionale** se la
  complessità è documentata.
- **Indagini** (§6.10.2): su terreno e fondazioni esistenti, dalla documentazione disponibile; cautele per
  manufatti sensibili; misura dei **caratteri cinematici**, delle **pressioni interstiziali** e degli
  **spostamenti** nel volume significativo, protratte per fenomeni stagionali.
- **Tipi di consolidamento** (§6.10.3): (1) miglioramento/rinforzo dei terreni di fondazione;
  (2) miglioramento/rinforzo dei materiali della fondazione; (3) ampliamento della base (se superficiale);
  (4) trasferimento del carico a strati più profondi; (5) sostegni laterali; (6) rettifica degli spostamenti del
  piano di posa. **Particolari cautele** per interventi con variazioni di volume (congelamento, iniezioni,
  gettiniezione).
- **Controlli/monitoraggio** (§6.10.4): controllo dell'efficacia **obbligatorio** quando l'intervento comporta
  una **ridistribuzione delle sollecitazioni al contatto terreno-manufatto**; monitoraggio previsto in progetto;
  esiti come **elemento di collaudo**.

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 6.10** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e trascritto
  verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non calcola** né **dimensiona** gli interventi di consolidamento; **non** definisce il modello geotecnico né
  **progetta** il risanamento strutturale.
- **Non tratta** il **miglioramento/rinforzo dei terreni** in generale (§6.9), la **classificazione sismica
  dell'esistente** (Cap. 8, skill `costruzioni-esistenti-ntc-cap8`) né la **progettazione sismica** (Cap. 7).
- **Non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista geotecnico/strutturale, né la lettura del par. 6.10 delle NTC 2018 e della Circolare applicativa.**
