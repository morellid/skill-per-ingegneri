# CHANGELOG - azioni-temperatura-ntc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-20

### Added (closes #405)
- Prima versione della skill di supporto al **progettista strutturale** per l'**inquadramento delle azioni
  della temperatura** secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 3.5**, nell'area
  `strutture-geotecnica`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **NTC 2018 (DM 17 gennaio 2018)** - PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio
    2018 - SHA256: dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46 (doppio download
    riproducibile, stessa fonte delle altre skill NTC del repo).
  - Par. 3.5 estratto con `pdftotext -layout` (pp. 59-61) e trascritto verbatim in
    `references/fonti/ntc2018-par-3-5.md` (Tab. 3.5.I/II/III, formule [3.5.1]-[3.5.8]). **I segni "−" delle
    formule Tmin/Tmax sono stati verificati sull'immagine del PDF** (pdftoppm della pagina GU 60), perché
    pdftotext li rende come spazi.
- Estratto operativo `references/estratti/azioni-temperatura-checklist.md`.
- Due task: `inquadra-temperatura-esterna-interna.md` e `inquadra-azioni-termiche-edifici-effetti.md`.
- Due esempi: Tmax/Tmin dell'aria esterna in Zona I a as=300 m (−16,2 / 40,2 °C); ΔTu e dilatazione libera di
  un edificio in c.a. esposto (±15 °C, αT=10·10⁻⁶/°C, ΔL=1,5 mm per L=10 m).

### Contenuto ancorato al testo
- Temperatura esterna (§3.5.2): Tmax/Tmin con TR = 50 anni (5/10 anni per fasi transitorie); formule per zone
  I-IV in funzione dell'altitudine as: Zona I Tmin = −15 − 4·as/1000 [3.5.1] e Tmax = 42 − 6·as/1000 [3.5.2];
  Zona II −8 − 6 [3.5.3] e 42 − 2 [3.5.4]; Zona III −8 − 7 [3.5.5] e 42 − 0,3 [3.5.6]; Zona IV −2 − 9 [3.5.7]
  e 42 − 2 [3.5.8]. Temperatura interna Tint = 20 °C (§3.5.3). Distribuzione nella sezione (§3.5.4): componente
  uniforme ΔTu = T − T0 (T0 = 15 °C) e componenti lineari ΔTMy/ΔTMz; irraggiamento solare Tab. 3.5.I. Azioni
  termiche sugli edifici (§3.5.5): sola componente ΔTu dalla Tab. 3.5.II (c.a./c.a.p. esposte ±15, protette
  ±10; acciaio esposte ±25, protette ±15 °C). Effetti (§3.5.7): coefficienti di dilatazione αT Tab. 3.5.III
  (alluminio 24, acciaio 12, cls 10, miste 12, cls alleggerito 7, muratura 6÷10, legno ∥ 5, legno ⊥ 30÷70,
  in 10⁻⁶/°C).

### Scope e limiti
- Non calcola gli effetti né esegue le verifiche, non studia la trasmissione del calore, non riproduce la Fig.
  3.5.1 (zonazione, immagine), non tratta le azioni termiche sui ponti (§5.1.3.9 e Eurocodici) né sulle
  strutture speciali (§3.5.6), non riproduce la Circolare 21/1/2019 n. 7. Non sostituisce il progettista.

### Note di sviluppo
- Completa la famiglia delle azioni del Capitolo 3 delle skill NTC (§3.1, §3.2, §3.3-3.4, §3.6.1, §3.6.3),
  condividendo la stessa fonte GU. Validazione Livello 2 con ingegnere strutturista.
