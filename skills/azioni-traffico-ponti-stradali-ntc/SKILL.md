---
name: azioni-traffico-ponti-stradali-ntc
description: "Supporto documentale al progettista strutturale per l'inquadramento della definizione delle azioni da traffico (e delle altre azioni) sui ponti stradali secondo le NTC 2018 (DM 17 gennaio 2018), paragrafo 5.1.3. Aiuta a inquadrare la suddivisione della superficie carrabile in corsie convenzionali (Tab. 5.1.I: per w minore di 5,40 m una corsia da 3,00 m, per 5,4 fino a 6,0 m due corsie da w mezzi, per w da 6,0 m in su un numero di corsie pari alla parte intera di w diviso 3, ciascuna da 3,00 m); gli Schemi di Carico da 1 a 5 (Schema 1 tandem a due assi piu' carico distribuito per verifiche globali e locali, Schema 2 asse singolo, Schemi 3 e 4 carichi isolati sui marciapiedi, Schema 5 folla compatta 5,0 kN/m con valore di combinazione 2,5 kN/m) e gli Schemi 6.a/b/c per luci oltre 300 m; le intensita' Qik e qik per corsia (Tab. 5.1.II: corsia 1 con 300 kN e 9,00 kN/m, corsia 2 con 200 kN e 2,50 kN/m, corsia 3 con 100 kN e 2,50 kN/m, altre corsie 0 e 2,50 kN/m); le categorie stradali (ponti a carichi interi e ponti pedonali con il solo Schema 5); l'azione di frenamento q3 pari a 0,6 per 2 Q1k piu' 0,10 q1k w1 L, compresa fra 180 e 900 kN; la forza centrifuga q4 in funzione del raggio (Tab. 5.1.III); le altre azioni (neve e vento q5, temperatura q7, urto e parapetti q8 con parapetti alti almeno 1,10 m e azione orizzontale 1,5 kN/m); e i gruppi di azioni e i coefficienti parziali e di combinazione (Tab. 5.1.IV, 5.1.V, 5.1.VI). Use when a bridge structural designer must frame the traffic actions on road bridges under the Italian NTC 2018 par. 5.1.3; it is a documentary aid and does NOT compute the internal forces or the verifications, does NOT find the most unfavourable load arrangement nor size the deck, does NOT reproduce the figures (Fig. 5.1.1/5.1.2/5.1.3), does NOT cover railway bridges (par. 5.2), fatigue (par. 5.1.4) nor the seismic design of bridges (par. 7.9), and does NOT replace the structural designer or the 2019 Circular."
license: MIT
area: strutture-geotecnica
title: "Azioni da traffico sui ponti stradali (NTC 2018 par. 5.1.3)"
summary: "Inquadra le azioni da traffico sui ponti stradali (NTC 2018 par. 5.1.3): corsie convenzionali (Tab. 5.1.I), Schemi di Carico 1-5, intensita' Qik/qik (Tab. 5.1.II), frenamento q3 [5.1.4] e centrifuga q4, con i gruppi di azioni e i coefficienti delle combinazioni."
normative_refs:
  - "NTC 2018 (D.M. 17 gennaio 2018) - par. 5.1.3: corsie convenzionali (Tab. 5.1.I), Schemi di Carico 1-5 e Qik/qik (Tab. 5.1.II), frenamento q3 [5.1.4], centrifuga q4, combinazioni (Tab. 5.1.IV/V/VI)"
  - "Rinvio (non riprodotti): Fig. 5.1.1/5.1.2/5.1.3 (geometrie), par. 5.2 (ponti ferroviari), par. 5.1.4 (fatica), par. 7.9 (sismica ponti), UNI EN 1991-2 (EC1); Circolare 21/1/2019 n. 7"
version: 0.1.0-alpha
status: alpha
tags:
  - ponti-stradali
  - azioni-da-traffico
  - ntc-2018
  - schemi-di-carico
  - corsie-convenzionali
---

# Azioni da traffico sui ponti stradali (NTC 2018 par. 5.1.3)

## Quando usare questa skill

Usala quando un **progettista strutturale di ponti** deve **inquadrare la definizione delle azioni da
traffico** (e delle altre azioni) su un **ponte stradale** secondo le **NTC 2018** (DM 17 gennaio 2018),
**paragrafo 5.1.3**:

- **corsie convenzionali** e loro numero/larghezza (§5.1.3.3.2, Tab. 5.1.I);
- **Schemi di Carico 1-5** e **intensità Qik/qik** (§5.1.3.3.3, Tab. 5.1.II);
- **categorie stradali** (carichi interi / ponti pedonali) (§5.1.3.3.4);
- **frenamento q3** e **forza centrifuga q4** (§5.1.3.5-5.1.3.6);
- **altre azioni** (neve/vento, temperatura, parapetti/urto) e **combinazioni** (§5.1.3.7-5.1.3.14).

**Non è** uno strumento che calcola le sollecitazioni o esegue le verifiche, né individua la disposizione più
gravosa dei carichi o dimensiona l'impalcato: è un **supporto documentale** che inquadra corsie, schemi,
intensità, formule e coefficienti. Apre il **Capitolo 5 (ponti)** delle skill NTC, lato azioni da traffico.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-corsie-schemi-carico` | Corsie convenzionali (Tab. 5.1.I), Schemi di Carico 1-5, categorie stradali e intensità Qik/qik (Tab. 5.1.II) (§5.1.3.3) |
| `inquadra-azioni-derivate-combinazioni` | Frenamento q3 [5.1.4], centrifuga q4 (Tab. 5.1.III), altre azioni e coefficienti delle combinazioni (Tab. 5.1.IV/V/VI) (§5.1.3.4-5.1.3.14) |

## Punti chiave (verificati sul testo)

- **Corsie** (§5.1.3.3.2, Tab. 5.1.I): **w < 5,40 → nl = 1** (3,00 m); **5,4 ≤ w < 6,0 → nl = 2** (w/2);
  **6,0 ≤ w → nl = Int(w/3)** (3,00 m). Ingombro convenzionale 3,00 m; **min 2 corsie** (salvo w < 5,40 m).
- **Schemi di Carico** (§5.1.3.3.3): **1** (tandem + distribuito, globali/locali), **2** (asse singolo,
  locali), **3** (150 kN) e **4** (10 kN, marciapiedi), **5** (folla **5,0 kN/m²**, combinazione **2,5**);
  **6.a/b/c** per luce > 300 m ([5.1.1]-[5.1.3]).
- **Intensità** (Tab. 5.1.II): corsia 1 **300 kN / 9,00 kN/m²**; corsia 2 **200 / 2,50**; corsia 3
  **100 / 2,50**; altre **0 / 2,50**.
- **Frenamento q3** (§5.1.3.5, [5.1.4]): **180 kN ≤ q3 = 0,6·(2·Q1k) + 0,10·q1k·w1·L ≤ 900 kN**.
- **Centrifuga q4** (§5.1.3.6, Tab. 5.1.III): **R < 200 → 0,2·Qv**; **200 ≤ R ≤ 1500 → 40·Qv/R**;
  **R ≥ 1500 → 0**.
- **Parapetti/urto q8** (§5.1.3.10): parapetti **h ≥ 1,10 m**, azione orizzontale **1,5 kN/m**; forze da urto
  ×**1,50** per l'impalcato; γ **unitario** per l'urto.
- **Combinazioni** (§5.1.3.14): gruppi di azioni (Tab. 5.1.IV), γ parziali SLU (Tab. 5.1.V, EQU/A1/A2:
  traffico γQ **1,35/1,35/1,15**) e ψ (Tab. 5.1.VI).

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 5.1** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e trascritto
  verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non calcola** le sollecitazioni né esegue le verifiche; **non individua** la disposizione più gravosa dei
  carichi mobili; **non dimensiona** l'impalcato, le pile o gli appoggi.
- **Non riproduce** le **Fig. 5.1.1/5.1.2/5.1.3** (numerazione corsie, geometrie/interassi degli Schemi e
  delle impronte, diffusione dei carichi): rinvio al testo NTC e all'**EC1 (UNI EN 1991-2)**.
- **Non tratta** i **ponti ferroviari** (§5.2), la **fatica** e le verifiche di dettaglio (§5.1.4), né la
  **progettazione sismica dei ponti** (§7.9); **non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, né la lettura del par. 5.1 delle NTC 2018 e della Circolare applicativa.**
