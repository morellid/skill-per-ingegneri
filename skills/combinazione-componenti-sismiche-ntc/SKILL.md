---
name: combinazione-componenti-sismiche-ntc
description: "Supporto documentale al progettista strutturale per l'inquadramento della combinazione delle componenti dell'azione sismica e della risposta alla variabilita' spaziale del moto secondo le NTC 2018 (DM 17 gennaio 2018), paragrafo 7.3.5. Aiuta a inquadrare la combinazione delle tre componenti dell'azione sismica nell'analisi dinamica o statica, lineare o non lineare (la risposta e' calcolata unitariamente applicando l'espressione 1,00 per Ex piu' 0,30 per Ey piu' 0,30 per Ez, formula 7.3.10; gli effetti piu' gravosi si ricavano dal confronto tra le tre combinazioni ottenute permutando circolarmente i coefficienti moltiplicativi, assegnando a turno il coefficiente unitario a ciascuna componente e 0,30 alle altre due); la considerazione della componente verticale unicamente nei casi previsti al paragrafo 7.2.2; la combinazione con gli effetti pseudo-statici indotti dagli spostamenti relativi prodotti dalla variabilita' spaziale del moto unicamente nei casi previsti al paragrafo 3.2.4.1, mediante la radice quadrata della somma dei quadrati (SRSS), salvo quanto indicato al paragrafo 7.2.2 per gli appoggi mobili; e l'analisi dinamica con integrazione al passo (applicazione simultanea delle due componenti orizzontali della storia temporale, e della verticale ove necessario; con almeno 3 storie temporali si utilizzano i valori piu' sfavorevoli, con almeno 7 diverse storie temporali gli effetti sono la media dei valori piu' sfavorevoli; per la variabilita' spaziale, storie temporali differenziate ma coerenti per ciascun vincolo oppure analisi con moto sincrono e effetti pseudo-statici del paragrafo 3.2.4). Use when a structural designer must frame the combination of the seismic action components (1,00 + 0,30 + 0,30 rule) and the response to the spatial variability of motion under the Italian NTC 2018 par. 7.3.5; it is a documentary aid and does NOT run the analysis nor compute the effects, does NOT generate the time histories, does NOT cover the cases requiring the vertical component (par. 7.2.2) nor the spatial variability of motion (par. 3.2.4), and does NOT replace the designer or the 2019 Circular."
license: MIT
area: strutture-geotecnica
title: "Combinazione delle componenti dell'azione sismica (NTC 2018 par. 7.3.5)"
summary: "Inquadra la combinazione delle componenti sismiche (NTC 2018 par. 7.3.5): 1,00 Ex + 0,30 Ey + 0,30 Ez [7.3.10] con permutazione circolare, componente verticale solo nei casi 7.2.2, SRSS per la variabilita' spaziale, storie temporali 3 (valori piu' sfavorevoli) o 7 (media)."
normative_refs:
  - "NTC 2018 (D.M. 17 gennaio 2018) - par. 7.3.5: combinazione 1,00 Ex + 0,30 Ey + 0,30 Ez [7.3.10], effetti piu' gravosi per permutazione circolare; componente verticale solo nei casi del par. 7.2.2"
  - "NTC 2018 - par. 7.3.5: variabilita' spaziale del moto con SRSS (casi par. 3.2.4.1); integrazione al passo con >= 3 storie temporali (valori piu' sfavorevoli) o >= 7 storie (media)"
version: 0.1.0-alpha
status: alpha
tags:
  - combinazione-sismica
  - componenti-azione-sismica
  - progettazione-sismica
  - ntc-2018
  - storie-temporali
---

# Combinazione delle componenti dell'azione sismica (NTC 2018 par. 7.3.5)

## Quando usare questa skill

Usala quando un **progettista strutturale** deve **combinare le componenti dell'azione sismica** e tener conto
della **variabilità spaziale del moto** secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 7.3.5**:

- **combinazione delle tre componenti** (analisi dinamica o statica, lineare o non lineare);
- **componente verticale** e **variabilità spaziale del moto**;
- **analisi dinamica con integrazione al passo** (numero di storie temporali).

**Non è** uno strumento che esegue l'analisi o calcola gli effetti: è un **supporto documentale** che inquadra la
regola di combinazione. Complementa `combinazioni-carico-ntc` (§2.5.3, combinazioni di carico e ψ),
`criteri-modellazione-sismica-ntc` (§7.2.6), `regolarita-strutturale-sismica-ntc` (§7.2.1),
`spostamenti-interpiano-sld-ntc` (§7.3.6.1) e `spettro-risposta-ntc` (§3.2).

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-combinazione-componenti` | Regola 1,00 Ex + 0,30 Ey + 0,30 Ez [7.3.10], le tre combinazioni per permutazione circolare, componente verticale solo nei casi §7.2.2 |
| `inquadra-analisi-integrazione-passo-variabilita` | Storie temporali (≥ 3 → valori più sfavorevoli, ≥ 7 → media) e variabilità spaziale del moto (SRSS nei casi §3.2.4.1, storie differenziate o moto sincrono) |

## Punti chiave (verificati sul testo)

- **Combinazione** (§7.3.5): la risposta è calcolata unitariamente per le tre componenti con **1,00·Ex + 0,30·Ey
  + 0,30·Ez** [7.3.10]; gli **effetti più gravosi** derivano dal confronto tra le **tre combinazioni** ottenute
  **permutando circolarmente** i coefficienti (1,00 a turno su ciascuna componente, 0,30 sulle altre due).
- **Componente verticale** (§7.3.5): tenuta in conto **solo nei casi previsti al §7.2.2**.
- **Variabilità spaziale del moto** (§7.3.5): combinazione con gli **effetti pseudo-statici** (spostamenti
  relativi) **solo nei casi del §3.2.4.1**, con **SRSS** (salvo §7.2.2 per gli appoggi mobili).
- **Integrazione al passo** (§7.3.5): due componenti orizzontali simultanee (+ verticale ove necessario); **≥ 3
  storie temporali → valori più sfavorevoli**; **≥ 7 storie temporali → media dei valori più sfavorevoli**;
  variabilità spaziale con storie differenziate coerenti per ciascun vincolo o moto sincrono (§3.2.4).

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 7.3.5** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e trascritto
  verbatim; la formula [7.3.10] verificata anche sull'immagine della pagina (i segni "+" sono persi da
  `pdftotext`).

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non esegue** l'analisi né **calcola** gli effetti; **non** genera/seleziona le storie temporali.
- **Non tratta** i casi che richiedono la **componente verticale** (§7.2.2) né la **variabilità spaziale del
  moto** (§3.2.4/§3.2.4.1); rinvio ai paragrafi.
- **Non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, né la lettura del par. 7.3.5 delle NTC 2018 e della Circolare applicativa.**
