---
name: opere-sostegno-ntc
description: "Supporto documentale al progettista strutturale e geotecnico per l'inquadramento delle verifiche delle opere di sostegno - muri di sostegno, paratie e strutture miste - secondo le NTC 2018 (DM 17 gennaio 2018), paragrafo 6.5. Aiuta a inquadrare le tipologie di opere di sostegno e il rinvio al paragrafo 7.11.6 per le azioni sismiche; i criteri generali di progetto, con il drenaggio e il riempimento a tergo dei muri, i dispositivi complementari, gli effetti sulle costruzioni preesistenti e le indagini geotecniche estese alla stabilita' locale e globale del complesso opera-terreno; le azioni e il modello geometrico di riferimento, con la riduzione della quota di valle pari al minore tra il dieci per cento dell'altezza, il dieci per cento della differenza di quota e cinquanta centimetri, e l'ipotesi sul livello di falda negli stati limite ultimi; le verifiche agli stati limite ultimi dei muri (scorrimento, carico limite, ribaltamento, stabilita' globale e stati limite strutturali) con la stabilita' globale in Approccio 1 Combinazione 2 (A2+M2+R2) e le rimanenti verifiche in Approccio 2 (A1+M1+R3) e i coefficienti parziali della Tabella 6.5.I (capacita' portante 1,4, scorrimento 1,1, ribaltamento 1,15, resistenza a valle 1,4); le verifiche agli stati limite ultimi delle paratie (geotecnici, idraulici e strutturali) con l'Approccio 1; e le verifiche di esercizio sugli spostamenti. Use when a structural or geotechnical designer must frame the limit-state verifications of retaining structures (walls and embedded walls) under the Italian NTC 2018 par. 6.5; it is a documentary aid and does NOT compute the earth pressures, the verifications, or the coefficients, does NOT size the wall or the embedded wall, does NOT reproduce Tables 6.2.I/6.2.II/6.8.I or the 2019 Circular, does NOT cover the seismic case (par. 7.11.6), and does NOT replace the designer or the geotechnical report."
license: MIT
area: strutture-geotecnica
title: "Opere di sostegno: muri e paratie - verifiche NTC 2018 (par. 6.5)"
summary: "Inquadra le verifiche delle opere di sostegno (NTC 2018 par. 6.5): tipologie e criteri (6.5.1), azioni e modello geometrico (6.5.2), verifiche SLU dei muri con Approccio 2 (A1+M1+R3) e Tab. 6.5.I e stabilita' globale con Approccio 1 (A2+M2+R2), paratie e SLE (6.5.3)."
normative_refs:
  - "NTC 2018 (D.M. 17 gennaio 2018) - par. 6.5 Opere di sostegno: criteri di progetto (6.5.1), azioni e modello geometrico (6.5.2), verifiche SLU/SLE di muri e paratie e Tab. 6.5.I (6.5.3)"
  - "Rinvio (non riprodotti): Tabelle 6.2.I/6.2.II (azioni e parametri), Tab. 6.8.I (stabilita' globale), par. 6.2.4.2, 6.8 e 7.11.6 (sismico) NTC 2018; Circolare 21/1/2019 n. 7"
version: 0.1.0-alpha
status: alpha
tags:
  - opere-di-sostegno
  - muri-e-paratie
  - ntc-2018
  - stati-limite-geotecnici
  - coefficienti-parziali
---

# Opere di sostegno: muri e paratie - verifiche NTC 2018 (par. 6.5)

## Quando usare questa skill

Usala quando un **progettista strutturale o geotecnico** deve **inquadrare** le **verifiche delle opere
di sostegno** (muri, paratie, strutture miste) secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo
6.5**:

- **tipologie** di opere di sostegno e criteri di progetto (§6.5, §6.5.1);
- **azioni** e **modello geometrico** di riferimento (§6.5.2);
- **verifiche SLU** dei **muri** (approcci e Tab. 6.5.I) e delle **paratie** (§6.5.3.1);
- **verifiche di esercizio (SLE)** (§6.5.3.2).

**Non è** uno strumento che calcola spinte, verifiche o coefficienti, né dimensiona l'opera: è un
**supporto documentale** che inquadra tipologie, azioni, stati limite, approcci progettuali e
coefficienti parziali.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-criteri-azioni-sostegno` | Inquadra tipologie e criteri di progetto (§6.5, 6.5.1) e le azioni e il modello geometrico di riferimento (§6.5.2) |
| `inquadra-verifiche-slu-sostegno` | Inquadra le verifiche SLU/SLE di muri e paratie, gli approcci progettuali e i coefficienti della Tab. 6.5.I (§6.5.3) |

## Punti chiave (verificati sul testo)

- **Tipologie** (§6.5): **muri** (peso proprio), **paratie** (resistenza a valle + ancoraggi/puntoni),
  **strutture miste**; sismico al **§7.11.6**.
- **Modello geometrico** (§6.5.2.2): **riduzione della quota di valle** = minore tra **10%** dell'altezza,
  **10%** della differenza di quota, **0,5 m**; falda negli SLU **non inferiore** al livello dei terreni a
  bassa permeabilità (**k < 10⁻⁶ m/s**).
- **Muri - SLU** (§6.5.3.1.1): GEO (scorrimento, carico limite, ribaltamento, **stabilità globale**) e
  STR; **stabilità globale** → **Approccio 1, Comb. 2 (A2+M2+R2)**; **rimanenti** → **Approccio 2
  (A1+M1+R3)** con **Tab. 6.5.I** (γR: capacità portante **1,4**, scorrimento **1,1**, ribaltamento
  **1,15**, resistenza a valle **1,4**). Nello scorrimento in generale **non** si considera la resistenza
  passiva a valle (al più 50%, se giustificata).
- **Paratie - SLU** (§6.5.3.1.2): GEO/UPL/HYD e STR; **stabilità globale** → Approccio 1 Comb. 2; **altre**
  → **Approccio 1**, Comb. 1 **(A1+M1+R1)** e Comb. 2 **(A2+M2+R1)** con **R1 = 1**.
- **SLE** (§6.5.3.2): valutare gli **spostamenti** compatibili con funzionalità e con i manufatti
  adiacenti.

## Fonti

- **NTC 2018 (D.M. 17 gennaio 2018)** - **par. 6.5** - testo del Supplemento Ordinario n. 8 alla G.U. n.
  42 del 20 febbraio 2018 (PDF Gazzetta Ufficiale, SHA256 `dda1e397...`), estratto con `pdftotext` e
  trascritto verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non calcola** spinte, verifiche o coefficienti; **non dimensiona** il muro o la paratia.
- **Non riproduce** le **Tabelle 6.2.I/6.2.II/6.8.I** né la **Circolare 21/1/2019 n. 7**.
- **Non tratta** il caso **sismico** (§7.11.6) né la stabilità dei pendii (§6.8) se non nei richiami.

**La skill è un supporto documentale: non sostituisce il progettista strutturale/geotecnico o la
relazione geotecnica, né la lettura del par. 6.5 delle NTC 2018 e della Circolare applicativa.**
