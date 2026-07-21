# Estratto operativo - Azioni della temperatura (NTC 2018 §3.5)

> Parafrasi ancorata a `references/fonti/ntc2018-par-3-5.md`. Ogni voce cita il paragrafo/tabella/formula NTC.
> La skill **inquadra** temperatura, componenti ed effetti; **non** calcola gli effetti né esegue le verifiche.
> I segni "−" delle formule sono verificati sull'immagine del PDF.

## 1. Temperatura dell'aria esterna (§3.5.2)

- **Tmax / Tmin** con **periodo di ritorno 50 anni**; per fasi transitorie: **TR ≥ 5 anni** (≤ 3 mesi), **TR ≥
  10 anni** (3 mesi – 1 anno).
- Formule in funzione dell'**altitudine as [m]** per **Zona I-IV** (Fig. 3.5.1, zonazione = immagine → l'utente
  identifica la zona):

| Zona | Regioni | Tmin [°C] | Tmax [°C] |
|---|---|---|---|
| **I** | VdA, Piemonte, Lombardia, Trentino-AA, Veneto, FVG, Emilia-Romagna | **−15 − 4·as/1000** [3.5.1] | **42 − 6·as/1000** [3.5.2] |
| **II** | Liguria, Toscana, Umbria, Lazio, Sardegna, Campania, Basilicata | **−8 − 6·as/1000** [3.5.3] | **42 − 2·as/1000** [3.5.4] |
| **III** | Marche, Abruzzo, Molise, Puglia | **−8 − 7·as/1000** [3.5.5] | **42 − 0,3·as/1000** [3.5.6] |
| **IV** | Calabria, Sicilia | **−2 − 9·as/1000** [3.5.7] | **42 − 2·as/1000** [3.5.8] |

## 2. Temperatura dell'aria interna (§3.5.3)

- **Tint = 20 °C** (in mancanza di più precise valutazioni).

## 3. Distribuzione nella sezione (§3.5.4)

- **Componente uniforme ΔTu = T − T0** (T = temperatura media attuale, T0 = iniziale); **T0 = 15 °C** in
  mancanza di determinazioni più precise.
- **Componenti lineari ΔTMy, ΔTMz** secondo gli assi principali; per elevati gradienti termici considerare
  l'andamento non lineare.
- **Irraggiamento solare** (Tab. 3.5.I, incremento di temperatura):

| Stagione | Superficie | Nord-Est | Sud-Ovest / orizzontali |
|---|---|---|---|
| Estate | riflettente | 0 °C | 18 °C |
| Estate | chiara | 2 °C | 30 °C |
| Estate | scura | 4 °C | 42 °C |
| Inverno | — | 0 °C | 0 °C |

## 4. Azioni termiche sugli edifici (§3.5.5)

- Se la temperatura **non** è azione fondamentale, per gli edifici si usa la **sola componente ΔTu** dalla Tab.
  3.5.II:

| Tipo di struttura | ΔTu |
|---|---|
| c.a. e c.a.p. **esposte** | **± 15 °C** |
| c.a. e c.a.p. **protette** | **± 10 °C** |
| acciaio **esposte** | **± 25 °C** |
| acciaio **protette** | **± 15 °C** |

- Se la temperatura **è** azione fondamentale, va studiata la trasmissione del calore.

## 5. Azioni termiche speciali (§3.5.6)

- Ciminiere, tubazioni, sili, serbatoi, torri di raffreddamento, ecc.: progettare per le distribuzioni di
  temperatura delle specifiche condizioni di servizio (fuori scope della skill).

## 6. Effetti delle azioni termiche (§3.5.7)

- **Coefficienti di dilatazione termica αT** (Tab. 3.5.III, ×10⁻⁶/°C):

| Materiale | αT | Materiale | αT |
|---|---|---|---|
| Alluminio | 24 | Calcestruzzo alleggerito | 7 |
| Acciaio da carpenteria | 12 | Muratura | 6 ÷ 10 |
| Calcestruzzo strutturale | 10 | Legno (∥ fibre) | 5 |
| Strutture miste acciaio-cls | 12 | Legno (⊥ fibre) | 30 ÷ 70 |

## Cosa la skill NON fa

- **Non calcola** gli effetti (dilatazioni, sollecitazioni indotte) né **esegue** le verifiche; **non** studia
  la trasmissione del calore.
- **Non riproduce** la **Fig. 3.5.1** (zonazione, immagine): l'utente identifica la zona; **non** tratta le
  azioni termiche sui **ponti** (§5.1.3.9 e Eurocodici) né sulle **strutture speciali** (§3.5.6).
- **Non sostituisce** il progettista strutturale né la lettura del §3.5 delle NTC 2018 e della Circolare
  applicativa.
