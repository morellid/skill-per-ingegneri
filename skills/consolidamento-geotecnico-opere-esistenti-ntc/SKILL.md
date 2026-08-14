---
name: consolidamento-geotecnico-opere-esistenti-ntc
description: "Supporto documentale al progettista geotecnico e strutturale per l'inquadramento della progettazione degli interventi di consolidamento geotecnico di opere esistenti (sottofondazioni, rinforzo delle fondazioni, miglioramento del terreno di fondazione) secondo le NTC 2018 (DM 17 gennaio 2018), paragrafo 6.10. Use when a geotechnical or structural designer must frame the design of geotechnical consolidation (underpinning, foundation strengthening) of an existing structure under the Italian NTC 2018 par. 6.10; it is a documentary aid and does NOT compute or size the interventions, does NOT define the geotechnical model nor design the structural repair, does NOT cover general ground improvement (par. 6.9), the seismic assessment of existing buildings (Chap. 8) nor the seismic design, and does NOT replace the designer or the 2019 Circular."
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
