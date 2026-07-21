---
name: azioni-esplosione-eccezionali-ntc
description: "Supporto documentale al progettista strutturale per l'inquadramento delle azioni eccezionali da esplosione secondo le NTC 2018 (DM 17 gennaio 2018), paragrafo 3.6.2 (Esplosioni). Aiuta a inquadrare l'ambito (costruzioni con miscele esplosive di polveri o gas in aria o con materiali esplosivi; escluse le esplosioni esterne alla costruzione); la classificazione delle azioni (Tab. 3.6.I: categoria 1 effetti trascurabili, 2 localizzati, 3 generalizzati); e la modellazione come pressioni statiche equivalenti: per la Categoria 1 nessuna verifica; per la Categoria 2, ove siano presenti idonei pannelli di sfogo, la pressione statica equivalente nominale pd in kN/m quadro pari al valore maggiore fra pd uguale a 3 piu' pv [3.6.5a] e pd uguale a 3 piu' pv mezzi piu' 0,04 diviso il quadrato del rapporto Av su V [3.6.5b] (con pv pressione a cui cedono le aperture di sfogo, Av area delle aperture, V volume dell'ambiente), con il vincolo 0,05 minore o uguale ad Av su V minore o uguale a 0,15 al metro [3.6.6], valide per volume non superiore a 1000 metri cubi e con la pressione agente simultaneamente su tutte le pareti, mentre tutti gli elementi chiave e le loro connessioni devono essere progettati per pd uguale a 20 kN/m quadro da ogni direzione; per la Categoria 3 studi piu' approfonditi; e i criteri di progettazione (danneggiamenti localizzati accettabili, misure di protezione come superfici collassabili, giunti strutturali e prevenzione dei crolli). Use when a structural designer must frame the accidental explosion actions under the Italian NTC 2018 par. 3.6.2; it is a documentary aid and does NOT compute the internal forces nor size or verify the members, does NOT perform the pressure-wave theoretical models nor the Category 3 studies, does NOT cover external explosions, fire (par. 3.6.1) or impact (par. 3.6.3, dedicated skills), and does NOT replace the structural designer or the 2019 Circular."
license: MIT
area: strutture-geotecnica
title: "Azioni eccezionali da esplosione (NTC 2018 par. 3.6.2)"
summary: "Inquadra le azioni eccezionali da esplosione (NTC 2018 par. 3.6.2): classificazione (Tab. 3.6.I), Cat. 2 con pannelli di sfogo pd=max(3+pv; 3+pv/2+0,04/(Av/V)^2), vincolo 0,05<=Av/V<=0,15, elementi chiave 20 kN/m^2 e criteri di progettazione."
normative_refs:
  - "NTC 2018 (D.M. 17 gennaio 2018) - par. 3.6.2: Cat. 2 pd=max(3+pv [3.6.5a]; 3+pv/2+0,04/(Av/V)^2 [3.6.5b]), vincolo 0,05<=Av/V<=0,15 [3.6.6], V<=1000 m3, elementi chiave 20 kN/m2, classi Tab. 3.6.I"
  - "NTC 2018 - par. 3.6.2.4 criteri: danni localizzati accettabili; superfici collassabili, giunti strutturali, prevenzione crolli; rinvio par. 2.2.5 (robustezza) e 2.5.3 (comb. eccezionale)"
version: 0.1.0-alpha
status: alpha
tags:
  - azioni-da-esplosione
  - azioni-eccezionali
  - ntc-2018
  - robustezza
  - pannelli-di-sfogo
---

# Azioni eccezionali da esplosione (NTC 2018 par. 3.6.2)

## Quando usare questa skill

Usala quando un **progettista strutturale** deve **inquadrare le azioni eccezionali da esplosione** su strutture
in ambienti a rischio (miscele esplosive di polveri/gas o materiali esplosivi) secondo le **NTC 2018** (DM 17
gennaio 2018), **paragrafo 3.6.2 (Esplosioni)**:

- **classificazione** delle azioni (Tab. 3.6.I) (§3.6.2.2);
- **modellazione** come pressioni statiche equivalenti (§3.6.2.3);
- **criteri di progettazione** (§3.6.2.4).

**Non è** uno strumento che calcola le sollecitazioni o verifica gli elementi: è un **supporto documentale**
che inquadra categorie, pressioni equivalenti e criteri. Completa la famiglia delle **azioni eccezionali**
(§3.6) insieme a `resistenza-fuoco-strutture-ntc` (§3.6.1) e `azioni-urto-eccezionali-ntc` (§3.6.3).

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-classificazione-modellazione-esplosioni` | Classificazione (Tab. 3.6.I) e modellazione: Cat. 2 con pannelli di sfogo (pd = max di [3.6.5a]/[3.6.5b], vincolo [3.6.6], elementi chiave 20 kN/m²) (§3.6.2.2-3.6.2.3) |
| `inquadra-criteri-progettazione-esplosioni` | Criteri di progettazione: danni localizzati accettabili, misure di protezione (superfici collassabili, giunti, prevenzione crolli) (§3.6.2.4) |

## Punti chiave (verificati sul testo)

- **Ambito** (§3.6.2.1): miscele esplosive di polveri/gas o materiali esplosivi; **escluse** le esplosioni
  esterne.
- **Classificazione** (Tab. 3.6.I): categoria **1** trascurabili, **2** localizzati, **3** generalizzati.
- **Modellazione** (§3.6.2.3): onde di pressione → pressioni statiche equivalenti.
  - **Cat. 1**: nessuna verifica.
  - **Cat. 2** (con pannelli di sfogo): pd [kN/m²] = **max** fra **pd = 3 + pv** [3.6.5a] e **pd = 3 + pv/2 +
    0,04/(Av/V)²** [3.6.5b]; vincolo **0,05 m⁻¹ ≤ Av/V ≤ 0,15 m⁻¹** [3.6.6]; valide per **V ≤ 1.000 m³**;
    pressione su tutte le pareti. **Elementi chiave**: **pd = 20 kN/m²** da ogni direzione.
  - **Cat. 3**: studi più approfonditi.
- **Criteri** (§3.6.2.4): danni localizzati accettabili; **superfici collassabili**, **giunti strutturali**,
  **prevenzione di crolli** (robustezza §2.2.5).

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 3.6.2** - testo del Supplemento Ordinario n. 8 alla G.U. n. 42
  del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e trascritto
  verbatim (operatori delle formule verificati sull'immagine del PDF).

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non calcola** le sollecitazioni né **dimensiona/verifica** gli elementi o i sistemi di protezione; **non**
  sceglie la categoria di azione al posto del progettista.
- **Non svolge** i **modelli teorici** delle onde di pressione né gli **studi di Categoria 3**; **non** tratta
  le **esplosioni esterne**.
- **Non tratta** l'**incendio** (§3.6.1) né gli **urti** (§3.6.3, skill dedicate); **non riproduce** la
  **Circolare 21/1/2019 n. 7**.

**La skill è un supporto documentale: non sostituisce il progettista strutturale, né la lettura del par. 3.6.2 delle NTC 2018 e della Circolare applicativa.**
