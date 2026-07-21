---
name: azioni-temperatura-ntc
description: "Supporto documentale al progettista strutturale per l'inquadramento delle azioni della temperatura secondo le NTC 2018 (DM 17 gennaio 2018), paragrafo 3.5. Aiuta a inquadrare la temperatura dell'aria esterna Test (valori massimo estivo Tmax e minimo invernale Tmin con periodo di ritorno di 50 anni, ridotto a 5 anni per fasi fino a tre mesi e a 10 anni per fasi tra tre mesi e un anno; formule per le zone da I a IV in funzione dell'altitudine as in metri: Zona I Tmin uguale a meno 15 meno 4 as diviso 1000 e Tmax uguale a 42 meno 6 as diviso 1000; Zona II meno 8 meno 6 e 42 meno 2; Zona III meno 8 meno 7 e 42 meno 0,3; Zona IV meno 2 meno 9 e 42 meno 2; la zonazione della Fig. 3.5.1 e' un'immagine e l'utente identifica la zona); la temperatura dell'aria interna Tint pari a 20 gradi; la distribuzione della temperatura nella sezione con la componente uniforme Delta_Tu uguale a T meno T0 (temperatura iniziale T0 pari a 15 gradi) e le componenti lineari, con il contributo dell'irraggiamento solare della Tab. 3.5.I; le azioni termiche sugli edifici con la sola componente Delta_Tu della Tab. 3.5.II (piu' o meno 15 gradi per le strutture in cemento armato e cemento armato precompresso esposte, piu' o meno 10 se protette, piu' o meno 25 per l'acciaio esposto, piu' o meno 15 se protetto); e gli effetti con i coefficienti di dilatazione termica alpha_T della Tab. 3.5.III (acciaio 12, calcestruzzo 10, alluminio 24, legno 5, ecc., in dieci alla meno sei per grado). Use when a structural designer must frame the thermal actions under the Italian NTC 2018 par. 3.5; it is a documentary aid and does NOT compute the effects nor run the verifications, does NOT reproduce the Fig. 3.5.1 zoning (image), does NOT study heat transmission, does NOT cover the thermal actions on bridges (par. 5.1.3.9 and Eurocodes) nor on special structures, and does NOT replace the structural designer or the 2019 Circular."
license: MIT
area: strutture-geotecnica
title: "Azioni della temperatura (NTC 2018 par. 3.5)"
summary: "Inquadra le azioni della temperatura (NTC 2018 par. 3.5): Tmax/Tmin esterna per zone I-IV, Tint=20 gradi, componente uniforme Delta_Tu=T-T0 (T0=15 gradi), Delta_Tu edifici (Tab. 3.5.II: c.a. +-15, acciaio +-25) e coefficienti di dilatazione alpha_T (Tab. 3.5.III)."
normative_refs:
  - "NTC 2018 (D.M. 17 gennaio 2018) - par. 3.5: Tmax/Tmin esterna per zone I-IV [3.5.1]-[3.5.8] (TR 50/10/5 anni), Tint=20 gradi, Delta_Tu=T-T0 (T0=15 gradi), irraggiamento Tab. 3.5.I"
  - "NTC 2018 - par. 3.5.5 Delta_Tu edifici Tab. 3.5.II (c.a. +-15/+-10, acciaio +-25/+-15 gradi); par. 3.5.7 coefficienti di dilatazione termica alpha_T Tab. 3.5.III (acciaio 12, cls 10, in 10^-6/grado)"
version: 0.1.0-alpha
status: alpha
tags:
  - azioni-della-temperatura
  - variazioni-termiche
  - ntc-2018
  - dilatazione-termica
  - azioni
---

# Azioni della temperatura (NTC 2018 par. 3.5)

## Quando usare questa skill

Usala quando un **progettista strutturale** deve **inquadrare le azioni della temperatura** (variazioni
termiche) per il progetto strutturale secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 3.5**:

- **temperatura dell'aria esterna** Tmax/Tmin (zone I-IV) (§3.5.2);
- **temperatura dell'aria interna** Tint (§3.5.3);
- **distribuzione nella sezione** (componente uniforme e lineari) (§3.5.4);
- **azioni termiche sugli edifici** ed **effetti** (dilatazione) (§3.5.5, 3.5.7).

**Non è** uno strumento che calcola gli effetti o esegue le verifiche: è un **supporto documentale** che
inquadra i valori di riferimento (Tmax/Tmin, Tint, ΔTu, αT) e i criteri. Completa la famiglia delle **azioni**
del Capitolo 3 (permanenti §3.1, sismica §3.2, vento/neve §3.3-3.4, eccezionali §3.6).

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-temperatura-esterna-interna` | Tmax/Tmin (zone I-IV, [3.5.1]-[3.5.8]), Tint=20°, componente uniforme ΔTu=T-T0 (T0=15°) e irraggiamento (Tab. 3.5.I) (§3.5.2-3.5.4) |
| `inquadra-azioni-termiche-edifici-effetti` | ΔTu per edifici (Tab. 3.5.II) e coefficienti di dilatazione αT (Tab. 3.5.III) (§3.5.5, 3.5.7) |

## Punti chiave (verificati sul testo)

- **Temperatura esterna** (§3.5.2): Tmax/Tmin con **TR = 50 anni** (5/10 anni per fasi transitorie); formule per
  altitudine as [m]:

| Zona | Tmin [°C] | Tmax [°C] |
|---|---|---|
| **I** (VdA, Piemonte, Lombardia, Trentino-AA, Veneto, FVG, E-R) | −15 − 4·as/1000 | 42 − 6·as/1000 |
| **II** (Liguria, Toscana, Umbria, Lazio, Sardegna, Campania, Basilicata) | −8 − 6·as/1000 | 42 − 2·as/1000 |
| **III** (Marche, Abruzzo, Molise, Puglia) | −8 − 7·as/1000 | 42 − 0,3·as/1000 |
| **IV** (Calabria, Sicilia) | −2 − 9·as/1000 | 42 − 2·as/1000 |

- **Temperatura interna** (§3.5.3): **Tint = 20 °C**.
- **Distribuzione** (§3.5.4): componente uniforme **ΔTu = T − T0** (**T0 = 15 °C**) e lineari ΔTMy/ΔTMz;
  irraggiamento Tab. 3.5.I.
- **Edifici** (§3.5.5, Tab. 3.5.II): ΔTu = **±15 °C** (c.a./c.a.p. esposte), **±10** (protette), **±25**
  (acciaio esposte), **±15** (acciaio protette).
- **Effetti** (§3.5.7, Tab. 3.5.III): αT [10⁻⁶/°C] = acciaio 12, cls 10, alluminio 24, miste 12, cls
  alleggerito 7, muratura 6÷10, legno ∥ 5, legno ⊥ 30÷70.

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 3.5** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e trascritto
  verbatim (segni delle formule verificati sull'immagine del PDF).

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non calcola** gli effetti (dilatazioni, sollecitazioni indotte) né **esegue** le verifiche; **non** studia
  la trasmissione del calore.
- **Non riproduce** la **Fig. 3.5.1** (zonazione, immagine): l'utente identifica la zona; **non** tratta le
  azioni termiche sui **ponti** (§5.1.3.9 e Eurocodici) né sulle **strutture speciali** (§3.5.6).
- **Non riproduce** la **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, né la lettura del par. 3.5 delle NTC 2018 e della Circolare applicativa.**
