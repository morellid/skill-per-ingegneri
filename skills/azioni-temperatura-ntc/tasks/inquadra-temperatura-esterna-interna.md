# Task - Inquadra la temperatura esterna/interna e la distribuzione nella sezione (§3.5.2-3.5.4)

## Obiettivo

Inquadrare la **temperatura dell'aria esterna e interna** e la **distribuzione della temperatura** negli
elementi strutturali (componente uniforme e lineari), secondo le NTC 2018 §3.5.2-3.5.4.

## Input richiesti

- **zona** della temperatura (I-IV, dalla Fig. 3.5.1 in funzione della localizzazione) e **altitudine as [m]**;
- durata dell'eventuale **fase transitoria/costruzione** (per il periodo di ritorno);
- natura della superficie (riflettente/chiara/scura) ed esposizione (per l'irraggiamento).

## Procedura (ancorata al testo)

1. **Temperatura esterna** (§3.5.2). Assumere il **periodo di ritorno** (50 anni; TR ≥ 5 anni per fasi ≤ 3
   mesi, TR ≥ 10 anni per fasi 3 mesi–1 anno). Calcolare **Tmax/Tmin** con le formule della zona:
   - **Zona I**: Tmin = −15 − 4·as/1000 [3.5.1]; Tmax = 42 − 6·as/1000 [3.5.2];
   - **Zona II**: Tmin = −8 − 6·as/1000 [3.5.3]; Tmax = 42 − 2·as/1000 [3.5.4];
   - **Zona III**: Tmin = −8 − 7·as/1000 [3.5.5]; Tmax = 42 − 0,3·as/1000 [3.5.6];
   - **Zona IV**: Tmin = −2 − 9·as/1000 [3.5.7]; Tmax = 42 − 2·as/1000 [3.5.8].

2. **Temperatura interna** (§3.5.3). In mancanza di più precise valutazioni assumere **Tint = 20 °C**.

3. **Distribuzione nella sezione** (§3.5.4). Individuare la **componente uniforme ΔTu = T − T0** (con **T0 = 15
   °C**) e le **componenti lineari ΔTMy/ΔTMz**; per elevati gradienti considerare l'andamento non lineare. Per
   l'**irraggiamento solare** usare la **Tab. 3.5.I** (estate: riflettente 0/18, chiara 2/30, scura 4/42 °C per
   Nord-Est / Sud-Ovest-orizzontali; inverno 0/0).

## Output

Una nota che indichi: la **zona** e le **espressioni** di Tmax/Tmin per l'altitudine data, la **Tint**, la
**componente uniforme ΔTu = T − T0** con T0 = 15 °C e il contributo dell'**irraggiamento** (Tab. 3.5.I). **La
skill inquadra i valori di riferimento; non calcola gli effetti né studia la trasmissione del calore.**
