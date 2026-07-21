# azioni-temperatura-ntc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con ingegnere strutturista da completare)

Skill di **supporto documentale** al **progettista strutturale** per l'**inquadramento delle azioni della
temperatura** secondo le **NTC 2018** (D.M. 17 gennaio 2018), **paragrafo 3.5**: temperatura esterna/interna,
distribuzione nella sezione, azioni termiche sugli edifici ed effetti (dilatazione).

**Non calcola** gli effetti né **esegue** le verifiche e **non sostituisce** il progettista: fornisce i valori
di riferimento (Tmax/Tmin per zone, Tint, componente uniforme ΔTu, coefficienti di dilatazione αT) e i criteri.

## Target

Ingegneri strutturisti che devono definire le azioni della temperatura per il progetto strutturale secondo le
NTC 2018 par. 3.5.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-temperatura-esterna-interna` | Tmax/Tmin (zone I-IV, [3.5.1]-[3.5.8]), Tint=20°, componente uniforme ΔTu=T-T0 (T0=15°) e irraggiamento (Tab. 3.5.I) (§3.5.2-3.5.4) |
| `inquadra-azioni-termiche-edifici-effetti` | ΔTu per edifici (Tab. 3.5.II) e coefficienti di dilatazione αT (Tab. 3.5.III) (§3.5.5, 3.5.7) |

Nucleo: **temperatura esterna** Tmax/Tmin (zone I-IV), **interna** Tint=20 °C, **componente uniforme** ΔTu =
T − T0 (T0=15 °C), **ΔTu edifici** (Tab. 3.5.II: c.a. ±15, acciaio ±25) e **coefficienti di dilatazione** αT
(Tab. 3.5.III) (§3.5).

## Relazione con altre skill

- Completa la famiglia delle **azioni** del Capitolo 3 con `carichi-permanenti-sovraccarichi-ntc` (§3.1),
  `spettro-risposta-ntc`/`periodo-proprio-t1-ntc` (§3.2), `carichi-atmosferici-ntc` (§3.3-3.4),
  `resistenza-fuoco-strutture-ntc` (§3.6.1) e `azioni-urto-eccezionali-ntc` (§3.6.3). Condivide la fonte GU con
  le altre skill NTC.

## Fonti consultate

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 3.5** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e trascritto
  verbatim (segni delle formule verificati sull'immagine del PDF).

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non calcola** gli effetti (dilatazioni, sollecitazioni indotte) né **esegue** le verifiche; **non** studia
  la trasmissione del calore.
- **Non riproduce** la **Fig. 3.5.1** (zonazione, immagine): l'utente identifica la zona; **non** tratta le
  azioni termiche sui **ponti** (§5.1.3.9 e Eurocodici) né sulle **strutture speciali** (§3.5.6).
- **Non sostituisce** il progettista strutturale.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, né la lettura del par. 3.5 delle NTC 2018 e della Circolare applicativa.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
