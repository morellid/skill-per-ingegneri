---
name: categorie-sottosuolo-topografiche-ntc
description: "Supporto documentale al geologo, geotecnico o strutturista per l'inquadramento della classificazione sismica del sito - categorie di sottosuolo e condizioni topografiche - secondo le NTC 2018 (DM 17 gennaio 2018), paragrafo 3.2.2. Aiuta a classificare la categoria di sottosuolo con l'approccio semplificato basato sulla velocita' equivalente di propagazione delle onde di taglio Vs,eq uguale al rapporto tra la profondita' del substrato H e la somma degli spessori di ciascuno strato divisi la relativa velocita' delle onde di taglio (formula 3.2.1), con il substrato definito da Vs almeno pari a 800 m/s e, per profondita' del substrato superiore a 30 m, la velocita' Vs,30 ottenuta ponendo H uguale a 30 m; le cinque categorie della Tabella 3.2.II (A ammassi rocciosi con Vs superiore a 800 m/s, B velocita' equivalente tra 360 e 800 m/s, C tra 180 e 360 m/s con substrato oltre 30 m, D tra 100 e 180 m/s con substrato oltre 30 m, E riconducibile a C o D con substrato non oltre 30 m); e a classificare la categoria topografica della Tabella 3.2.III (T1 superficie pianeggiante o pendii con inclinazione media non oltre 15 gradi, T2 pendii con inclinazione oltre 15 gradi, T3 rilievi con cresta stretta e inclinazione tra 15 e 30 gradi, T4 rilievi con cresta stretta e inclinazione oltre 30 gradi), da considerare per altezze superiori a 30 m. Use when a geologist or structural engineer must classify the subsoil category (A-E via Vs,eq) and the topographic category (T1-T4) of a site under the Italian NTC 2018 par. 3.2.2; it is a documentary aid and does NOT compute the response spectrum nor the amplification coefficients (par. 3.2.3), does NOT run site-specific seismic response analyses (par. 7.11.3), and does NOT replace the designer or the 2019 Circular."
license: MIT
area: strutture-geotecnica
title: "Categorie di sottosuolo e condizioni topografiche (NTC 2018 par. 3.2.2)"
summary: "Inquadra la classificazione sismica del sito (NTC 2018 par. 3.2.2): categorie di sottosuolo A-E (Tab. 3.2.II) via Vs,eq = H/somma(hi/Vs,i) [3.2.1] (substrato Vs>=800, regola dei 30 m) e categorie topografiche T1-T4 (Tab. 3.2.III) per altezze > 30 m."
normative_refs:
  - "NTC 2018 (D.M. 17 gennaio 2018) - par. 3.2.2: categorie di sottosuolo A-E (Tab. 3.2.II) con approccio semplificato su Vs,eq = H/somma(hi/Vs,i) [3.2.1]; substrato Vs>=800 m/s; regola dei 30 m (Vs,30)"
  - "NTC 2018 - par. 3.2.2: piani di riferimento del substrato (fondazioni superficiali/pali/opere di sostegno); sottosuoli non classificabili -> analisi di risposta locale (par. 7.11.3)"
  - "NTC 2018 - par. 3.2.2 Tab. 3.2.III: categorie topografiche T1 (i<=15°), T2 (i>15°), T3 (15°<=i<=30°), T4 (i>30°), da considerare se altezza > 30 m"
version: 0.1.0-alpha
status: alpha
tags:
  - categorie-sottosuolo
  - categorie-topografiche
  - vs30
  - azione-sismica
  - ntc-2018
---

# Categorie di sottosuolo e condizioni topografiche (NTC 2018 par. 3.2.2)

## Quando usare questa skill

Usala quando un **geologo, geotecnico o strutturista** deve **classificare il sito** ai fini della definizione
dell'azione sismica, secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 3.2.2**:

- **categoria di sottosuolo** A-E (approccio semplificato su Vs,eq);
- **categoria topografica** T1-T4.

**Non è** uno strumento che calcola lo spettro o i coefficienti di amplificazione: è un **supporto documentale**
che inquadra i **criteri di classificazione**. A valle, per lo spettro (che usa i coefficienti SS/CC/ST derivati
dalla categoria) usa `spettro-risposta-ntc` (§3.2.3).

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `classifica-categoria-sottosuolo` | Categoria di sottosuolo A-E (Tab. 3.2.II) con l'approccio semplificato su Vs,eq = H/Σ(hi/Vs,i) [3.2.1], substrato Vs≥800, regola dei 30 m, piani di riferimento (§3.2.2) |
| `classifica-categoria-topografica` | Categoria topografica T1-T4 (Tab. 3.2.III) in funzione dell'inclinazione media e della forma del rilievo, per altezze > 30 m (§3.2.2) |

## Punti chiave (verificati sul testo)

- **Approccio semplificato** (§3.2.2): la risposta sismica locale si valuta con analisi specifiche (§7.11.3) o, se
  le condizioni sono riconducibili alla Tab. 3.2.II, classificando il sottosuolo sulle onde di taglio **VS** (dati
  parte della **caratterizzazione geotecnica**, §6.2.2).
- **Velocità equivalente** (§3.2.2): **Vs,eq = H / Σ(hi/Vs,i)** [3.2.1]; il **substrato** ha **VS ≥ 800 m/s**; per
  **H > 30 m** si usa **VS,30** (H = 30 m). I piani di riferimento del substrato: fondazioni superficiali → piano
  di imposta; pali → testa pali; opere di sostegno di terreni naturali → testa opera; muri di terrapieni → piano
  di imposta fondazione.
- **Categorie di sottosuolo** (Tab. 3.2.II): **A** VS > 800 (copertura scadente ≤ 3 m); **B** 360-800; **C**
  180-360 (substrato > 30 m); **D** 100-180 (substrato > 30 m); **E** riconducibile a C/D con substrato ≤ 30 m.
  Sottosuoli non classificabili → **analisi di risposta locale**.
- **Categorie topografiche** (Tab. 3.2.III): **T1** i ≤ 15°; **T2** i > 15°; **T3** rilievi (cresta stretta)
  15° ≤ i ≤ 30°; **T4** rilievi (cresta stretta) i > 30°; da considerare (configurazioni 2D) se **altezza > 30 m**.

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 3.2.2** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42 del
  20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e trascritto verbatim;
  la formula [3.2.1] e le Tab. 3.2.II/3.2.III verificate anche sull'immagine delle pagine.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non calcola** lo **spettro** né i **coefficienti di amplificazione** stratigrafica SS/CC e topografica ST
  (§3.2.3.2): a valle usa `spettro-risposta-ntc`.
- **Non esegue** le **analisi di risposta sismica locale** (§7.11.3) né la **caratterizzazione geotecnica** del
  volume significativo (§6.2.2); non determina i valori di VS al posto del geologo/geotecnico.
- **Non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il geologo/geotecnico né il progettista, né la lettura diretta del par. 3.2.2 delle NTC 2018 e della Circolare applicativa.**
