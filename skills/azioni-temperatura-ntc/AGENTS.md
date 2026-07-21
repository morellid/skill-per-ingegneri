# AGENTS.md - azioni-temperatura-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **progettista strutturale** per l'**inquadramento delle azioni della temperatura**
secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 3.5**: temperatura esterna/interna, distribuzione
nella sezione, azioni termiche sugli edifici ed effetti (dilatazione). Target: ingegneri strutturisti.

**E' una skill documentale per il tecnico**: fornisce i valori di riferimento (Tmax/Tmin per zone, Tint,
componente uniforme ΔTu, coefficienti αT) e i criteri; **non calcola** gli effetti e **non esegue** le
verifiche.

## Nota sull'area e sulla complementarita'

Area **strutture-geotecnica**. Completa la famiglia delle **azioni** del Capitolo 3 delle skill NTC insieme a
`carichi-permanenti-sovraccarichi-ntc` (§3.1), `spettro-risposta-ntc`/`periodo-proprio-t1-ntc` (§3.2),
`carichi-atmosferici-ntc` (§3.3-3.4), `resistenza-fuoco-strutture-ntc` (§3.6.1) e `azioni-urto-eccezionali-ntc`
(§3.6.3). Condivide con le altre skill NTC la stessa fonte (PDF GU del S.O. n. 8 alla G.U. n. 42/2018). Restano
fuori scope: il calcolo degli effetti e le verifiche, lo studio della trasmissione del calore, le azioni
termiche sui ponti (§5.1.3.9 e Eurocodici) e sulle strutture speciali (§3.5.6).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **ntc2018-par-3-5**: PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (DM 17 gennaio
  2018, NTC 2018), SHA256 `dda1e397...` (doppio download riproducibile, stessa fonte delle altre skill NTC).
  Par. 3.5 estratto con `pdftotext -layout` (pp. 59-61) e trascritto verbatim; **i segni "−" delle formule
  Tmin/Tmax sono stati verificati sull'immagine del PDF** (pdftoppm), perché pdftotext li rende come spazi.

Trascrizione in `references/fonti/ntc2018-par-3-5.md`; estratto operativo in
`references/estratti/azioni-temperatura-checklist.md`.

## Punti chiave (verificati sul testo)

- **Esterna** (§3.5.2): TR 50 anni (5/10 anni fasi transitorie); Zona I Tmin=−15−4·as/1000, Tmax=42−6·as/1000;
  Zona II −8−6 / 42−2; Zona III −8−7 / 42−0,3; Zona IV −2−9 / 42−2.
- **Interna** (§3.5.3): Tint = 20 °C.
- **Distribuzione** (§3.5.4): ΔTu = T − T0 (T0 = 15 °C); ΔTMy/ΔTMz; irraggiamento Tab. 3.5.I.
- **Edifici** (§3.5.5, Tab. 3.5.II): ±15/±10 (c.a.), ±25/±15 (acciaio) [esposte/protette].
- **Effetti** (§3.5.7, Tab. 3.5.III): αT acciaio 12, cls 10, alluminio 24, legno ∥ 5, ecc. [10⁻⁶/°C].

## Convenzioni specifiche

### Cosa NON fare
- Non **calcolare** gli effetti (dilatazioni, sollecitazioni) né **eseguire** le verifiche; non **studiare** la
  trasmissione del calore.
- Non **riprodurre** la **Fig. 3.5.1** (zonazione, immagine): l'utente identifica la zona; non **trattare** le
  azioni termiche sui ponti (§5.1.3.9) né sulle strutture speciali (§3.5.6).
- **ATTENZIONE ai segni**: pdftotext perde i segni "−"; verificare sempre sull'immagine del PDF prima di
  scrivere le formule Tmin/Tmax.

### Cosa fare
- Fornire Tmax/Tmin (per zona/altitudine), Tint, ΔTu (uniforme) e i coefficienti αT, sempre con rinvio al
  paragrafo/tabella/formula NTC.

## Aggiornamento delle fonti

NTC: se il PDF GU cambia (nuova edizione/errata) riscaricare, ricalcolare l'hash con doppio download e
riestrarre/ritrascrivere il par. 3.5. Riverificare i segni delle formule [3.5.1]-[3.5.8] sull'immagine, le ΔTu
(Tab. 3.5.II) e i coefficienti αT (Tab. 3.5.III).

## Validatori

- Non ancora assegnato (Livello 2 con ingegnere strutturista).

## Stato attuale

- Versione: 0.1.0-alpha (closes #405)
- Task files: 2 (`inquadra-temperatura-esterna-interna.md`, `inquadra-azioni-termiche-edifici-effetti.md`)
- Esempi: 2 (Tmax/Tmin in Zona I a as=300 m; ΔTu e dilatazione di un edificio in c.a. esposto)
