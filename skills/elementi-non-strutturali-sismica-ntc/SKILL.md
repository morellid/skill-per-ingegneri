---
name: elementi-non-strutturali-sismica-ntc
description: "Supporto documentale al progettista strutturale per l'inquadramento della progettazione sismica degli elementi strutturali secondari, degli elementi costruttivi non strutturali (tamponature, controsoffitti, parapetti, rivestimenti) e degli impianti secondo le NTC 2018 (DM 17 gennaio 2018), paragrafi 7.2.3 e 7.2.4. Aiuta a inquadrare gli elementi strutturali secondari (rigidezza e resistenza alle azioni orizzontali trascurabili nell'analisi; progettati per i soli carichi verticali e per seguire gli spostamenti allo SLC; la scelta non puo' trasformare una struttura irregolare in regolare e il loro contributo totale a rigidezza e resistenza orizzontale non puo' superare il 15% dell'analogo contributo degli elementi primari); gli elementi costruttivi non strutturali (capacita' maggiore della domanda sismica per ogni stato limite; ripartizione delle responsabilita' tra progettista della struttura, direttore dei lavori e fornitore/installatore per elementi costruiti o assemblati in cantiere; se la distribuzione e' fortemente irregolare in pianta si incrementa di un fattore 2 l'eccentricita' accidentale, se in altezza si incrementa di un fattore 1,4 la domanda sismica sugli elementi verticali dei livelli con riduzione; la forza sismica orizzontale Fa uguale al prodotto tra l'accelerazione adimensionalizzata Sa e il peso Wa dell'elemento diviso il fattore di comportamento qa dell'elemento, formula 7.2.1, con Sa e qa da documenti di comprovata validita'); e gli impianti (capacita' maggiore della domanda sismica; responsabilita' di produttore, installatore e progettista strutturale; richiedono uno studio specifico gli impianti che eccedano il 30% del carico permanente del campo di solaio o del pannello a cui sono appesi o il 10% del carico permanente totale della struttura). Use when a structural designer must frame the seismic design of secondary structural elements, non-structural elements (infill walls, ceilings, parapets) and building services under the Italian NTC 2018 par. 7.2.3-7.2.4; it is a documentary aid and does NOT compute Fa nor run the checks, does NOT determine Sa and qa, does NOT compute the demand/displacements (par. 7.3), and does NOT replace the designer or the 2019 Circular."
license: MIT
area: strutture-geotecnica
title: "Elementi non strutturali e impianti in zona sismica (NTC 2018 par. 7.2.3-7.2.4)"
summary: "Inquadra la progettazione sismica di elementi secondari, elementi non strutturali e impianti (NTC 2018 par. 7.2.3-7.2.4): forza Fa = Sa*Wa/qa [7.2.1], limite 15% per gli elementi secondari, incrementi 2 (pianta) e 1,4 (altezza), soglie impianti 30%/10% per lo studio specifico."
normative_refs:
  - "NTC 2018 (D.M. 17 gennaio 2018) - par. 7.2.3: elementi secondari (contributo <= 15% dei primari, SLC); elementi non strutturali Fa = Sa*Wa/qa [7.2.1]; irregolarita' in pianta x2, in altezza x1,4"
  - "NTC 2018 - par. 7.2.4: impianti, capacita' > domanda sismica (7.3.6); responsabilita' produttore/installatore/progettista; studio specifico se impianto > 30% del solaio o > 10% della struttura"
version: 0.1.0-alpha
status: alpha
tags:
  - elementi-non-strutturali
  - impianti-sismica
  - progettazione-sismica
  - ntc-2018
  - elementi-secondari
---

# Elementi non strutturali e impianti in zona sismica (NTC 2018 par. 7.2.3-7.2.4)

## Quando usare questa skill

Usala quando un **progettista strutturale** deve **inquadrare la progettazione sismica** di **elementi strutturali
secondari**, **elementi costruttivi non strutturali** (tamponature, controsoffitti, parapetti, rivestimenti) e
**impianti** secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafi 7.2.3 e 7.2.4**:

- **elementi strutturali secondari** (§7.2.3);
- **elementi costruttivi non strutturali** e forza **Fa** (§7.2.3);
- **impianti** (§7.2.4).

**Non è** uno strumento che calcola Fa o esegue le verifiche: è un **supporto documentale** che inquadra criteri e
formula. Complementa `criteri-modellazione-sismica-ntc` (§7.2.6), `regolarita-strutturale-sismica-ntc` (§7.2.1),
`spostamenti-interpiano-sld-ntc` (§7.3.6.1) e `spettro-risposta-ntc` (§3.2).

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-forza-elementi-non-strutturali` | Elementi costruttivi non strutturali: definizione, capacità > domanda, responsabilità, incrementi per irregolarità (2 in pianta, 1,4 in altezza) e forza Fa = Sa·Wa/qa [7.2.1] (§7.2.3) |
| `inquadra-elementi-secondari-impianti` | Elementi strutturali secondari (limite 15%, SLC) e impianti (capacità > domanda, responsabilità, soglie 30%/10% per lo studio specifico) (§7.2.3, 7.2.4) |

## Punti chiave (verificati sul testo)

- **Elementi secondari** (§7.2.3): rigidezza/resistenza orizzontale **trascurate** nell'analisi; progettati per i
  **soli carichi verticali** e per **seguire gli spostamenti** allo **SLC** (§7.3.3.3/§7.3.4); la scelta **non**
  può trasformare irregolare in regolare (§7.2.1); contributo totale a rigidezza/resistenza orizzontale **≤ 15%**
  degli elementi primari.
- **Elementi non strutturali** (§7.2.3): capacità **> domanda** per ogni SL (§7.3.6); responsabilità
  progettista/DL/fornitore-installatore; irregolarità **in pianta** → eccentricità accidentale **×2** (§7.2.6);
  **in altezza** → domanda sugli elementi verticali **×1,4**; forza **Fa = (Sa·Wa)/qa** [7.2.1] (Sa
  adimensionalizzata §3.2.1, Wa peso, qa fattore di comportamento dell'elemento; Sa e qa da documenti di
  comprovata validità).
- **Impianti** (§7.2.4): capacità **> domanda** (§7.3.6); responsabilità produttore/installatore/progettista
  strutturale; **studio specifico** se l'impianto eccede il **30%** del carico permanente del campo di solaio (o
  del pannello a cui è appeso) o il **10%** del carico permanente totale della struttura.

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 7.2.3-7.2.4** - testo del Supplemento Ordinario n. 8 alla G.U. n.
  42 del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e trascritto
  verbatim; la formula [7.2.1] e le costanti (15%, 2, 1,4, 30%, 10%) verificate anche sull'immagine della pagina.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non calcola** Fa né **esegue** le verifiche; **non** determina **Sa** e **qa** (documenti di comprovata
  validità).
- **Non calcola** la domanda/gli spostamenti (§7.3.3.3/§7.3.4/§7.3.6) né lo spettro (§3.2).
- **Non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, né la lettura dei par. 7.2.3-7.2.4 delle NTC 2018 e della Circolare applicativa.**
