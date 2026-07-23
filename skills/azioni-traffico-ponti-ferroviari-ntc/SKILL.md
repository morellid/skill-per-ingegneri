---
name: azioni-traffico-ponti-ferroviari-ntc
description: "Supporto documentale al progettista strutturale per inquadrare le azioni da traffico sui ponti ferroviari secondo le NTC 2018 (DM 17 gennaio 2018), paragrafo 5.2.2. Aiuta a inquadrare: i modelli di carico verticali, cioe' il modello LM 71 (quattro assi da 250 kN a interasse di 1,60 m piu' un carico distribuito di 80 kN/m), i modelli SW/0 (carico distribuito 133 kN/m, a 15,0 m, c 5,3 m) ed SW/2 (150 kN/m, a 25,0 m, c 7,0 m) della Tab. 5.2.I, il treno scarico (10 kN/m) e i carichi sui marciapiedi (10 kN/m quadro), tutti da moltiplicare per il coefficiente di adattamento alpha (pari a 1,1 per LM71 e SW/0 e a 1,0 per SW/2 nelle ferrovie ordinarie); gli effetti dinamici mediante i coefficienti di incremento dinamico Phi2 uguale a 1,44 diviso la radice di L_phi meno 0,2, piu' 0,82 (con 1,00 minore o uguale a Phi2 minore o uguale a 1,67) per linee con elevato standard manutentivo e Phi3 uguale a 2,16 diviso la radice di L_phi meno 0,2, piu' 0,73 (con 1,00 minore o uguale a Phi3 minore o uguale a 2,00) per ridotto standard, con L_phi lunghezza caratteristica della Tab. 5.2.II e Phi non applicato al treno scarico e ai treni reali; e le azioni orizzontali, cioe' la forza centrifuga (formule 5.2.9 e 5.2.10), il serpeggio (forza concentrata di 100 kN) e le forze di avviamento (33 kN/m per L, non oltre 1000 kN) e di frenatura (20 kN/m per L, non oltre 6000 kN, e 35 kN/m per L per SW/2). Use when a structural engineer must frame the railway-bridge traffic actions under the Italian NTC 2018 par. 5.2.2; it is a documentary aid, does NOT run the load combinations, the dynamic analysis with real trains (speed above 200 km/h or non-conventional bridges) nor the verifications, and does NOT replace the structural designer. It is distinct from the road-bridge traffic-actions skill (par. 5.1.3)."
license: MIT
area: strutture-geotecnica
title: "Azioni da traffico sui ponti ferroviari (NTC 2018 par. 5.2.2)"
summary: "Inquadra le azioni da traffico sui ponti ferroviari (NTC 2018 par. 5.2.2): modelli di carico verticali (LM71, SW/0, SW/2, treno scarico), coeff. di adattamento alpha, effetti dinamici Phi2/Phi3 (con L_phi) e azioni orizzontali (centrifuga, serpeggio, avviamento/frenatura)."
normative_refs:
  - "NTC 2018 - par. 5.2.2: LM71 (4x250 kN + 80 kN/m), SW/0 133/SW2 150 kN/m, treno scarico 10 kN/m, alpha; dinamici Phi2/Phi3 (con Lphi); orizzontali: centrifuga, serpeggio 100 kN, avviamento/frenatura"
  - "Rinvio (fuori scope): §5.2.1 criteri progettuali; combinazioni; analisi dinamica con treni reali (V>200 km/h); Tab. 5.2.II completa (Lphi); verifiche SLU/SLE, fatica, interazione binario-struttura"
version: 0.1.0-alpha
status: alpha
tags:
  - ponti-ferroviari
  - azioni-da-traffico
  - ntc-2018
  - lm71-sw
  - coefficiente-dinamico
---

# Azioni da traffico sui ponti ferroviari (NTC 2018 par. 5.2.2)

## Quando usare questa skill

Usala quando un **progettista strutturale** deve **inquadrare le azioni da traffico** di un **ponte
ferroviario** secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 5.2.2** (par. 5.2 «Ponti ferroviari»):

- **modelli di carico verticali** (LM71, SW/0, SW/2, treno scarico, marciapiedi) e **coefficiente di
  adattamento α** (§5.2.2.2);
- **effetti dinamici** (coefficienti Φ2/Φ3, lunghezza caratteristica L_φ) (§5.2.2.2.3);
- **azioni orizzontali** (forza centrifuga, serpeggio, avviamento/frenatura) (§5.2.2.3).

È un **supporto documentale**: inquadra i modelli di carico, i coefficienti e le azioni; **non** esegue le
combinazioni, l'analisi dinamica con treni reali né le verifiche. È **distinta** da
`azioni-traffico-ponti-stradali-ntc` (§5.1.3, ponti stradali): modelli e coefficienti sono diversi.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-modelli-carico-verticali-ferroviari` | Modelli di carico verticali LM71, SW/0, SW/2, treno scarico, marciapiedi e coefficiente di adattamento α (§5.2.2.2.1-5.2.2.2.2) |
| `inquadra-effetti-dinamici-azioni-orizzontali` | Effetti dinamici (Φ2/Φ3, L_φ) e azioni orizzontali: centrifuga, serpeggio, avviamento/frenatura (§5.2.2.2.3, §5.2.2.3) |

## Punti chiave (verificati sul testo/immagine)

- **LM 71** (§5.2.2.2.1.1): **4 assi da 250 kN** a interasse **1,60 m** + **80 kN/m** distribuito; eccentricità
  da Q_V2/Q_V1 = 1,25 [5.2.1] (s/18, s = 1435 mm); **α = 1,1**.
- **SW/0 e SW/2** (Tab. 5.2.I): SW/0 **q_vk 133 kN/m**, a 15,0 m, c 5,3 m (**α = 1,1**); SW/2 **q_vk 150 kN/m**,
  a 25,0 m, c 7,0 m (**α = 1,0**). **Treno scarico** 10 kN/m; **marciapiedi** 10 kN/m².
- **Effetti dinamici** (§5.2.2.2.3): per **V ≤ 200 km/h** e frequenza nel fuso (Fig. 5.2.7) si usano Φ;
  **Φ2 = 1,44/(√L_φ − 0,2) + 0,82** (1,00 ≤ Φ2 ≤ 1,67) [5.2.6] e **Φ3 = 2,16/(√L_φ − 0,2) + 0,73**
  (1,00 ≤ Φ3 ≤ 2,00) [5.2.7], con **L_φ** da Tab. 5.2.II. Φ **non** su treno scarico/treni reali; per
  V > 200 km/h o tipologie non convenzionali → **analisi dinamica con convogli reali**.
- **Azioni orizzontali** (§5.2.2.3): **forza centrifuga** [5.2.9]-[5.2.10] (a 1,80 m sul P.F.; non ×Φ);
  **serpeggio** Q_sk = 100 kN; **avviamento** 33 kN/m·L ≤ 1000 kN; **frenatura** 20 kN/m·L ≤ 6000 kN (LM71/SW0),
  35 kN/m·L (SW/2). Serpeggio, avviamento e frenatura ×α ma non ×Φ.

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 5.2.2** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e verificato
  sull'immagine delle pagine PDF 168 (LM71) e 171 (Φ).

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non esegue** le **combinazioni** delle azioni, l'**analisi dinamica** con treni reali (V > 200 km/h o
  tipologie non convenzionali) né le **verifiche** (SLU/SLE, fatica, interazione statica binario-struttura).
- **Non riproduce** la **Tab. 5.2.II** completa (L_φ per ciascun elemento) né i criteri progettuali/manutentivi
  (§5.2.1); **non** tratta le azioni ambientali/eccezionali sui ponti.
- **Non** riguarda i **ponti stradali** (→ skill `azioni-traffico-ponti-stradali-ntc`, §5.1.3).

**La skill è un supporto documentale: non sostituisce il progettista strutturale né la lettura del par. 5.2.2 delle NTC 2018 e delle relative specifiche tecniche ferroviarie.**
