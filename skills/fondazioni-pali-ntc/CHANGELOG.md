# CHANGELOG - fondazioni-pali-ntc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-18

### Added (closes #372)
- Prima versione della skill di supporto al **progettista strutturale e geotecnico** per
  l'**inquadramento delle verifiche delle fondazioni su pali** (e delle **fondazioni miste** a platea su
  pali) secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 6.4.3**, nell'area
  `strutture-geotecnica`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **NTC 2018 (DM 17 gennaio 2018)** - PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20
    febbraio 2018 - SHA256:
    dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46 (doppio download riproducibile,
    stessa fonte delle altre skill NTC del repo).
  - Par. 6.4.3 estratto con `pdftotext -layout` (pp. 190-194) e trascritto verbatim in
    `references/fonti/ntc2018-par-6-4-3.md` (§6.4.3, 6.4.3.1/6.4.3.1.1/6.4.3.1.1.1/6.4.3.1.2, 6.4.3.2,
    6.4.3.3/6.4.3.4, 6.4.3.5/6.4.3.6/6.4.3.7), con i simboli greci resi in modo corretto (γR, γT, γM, ξ).
- Estratto operativo `references/estratti/fondazioni-pali-checklist.md`.
- Due task: `inquadra-verifiche-slu-sle-pali.md` e `inquadra-resistenza-caratteristica-prove.md`.
- Due esempi: palificata di pali trivellati sotto un plinto (stati limite, approccio, coefficienti Tab.
  6.4.II, effetto di gruppo, carichi trasversali Tab. 6.4.VI); resistenza caratteristica da prove
  (fattori di correlazione Tab. 6.4.III/IV/V, controlli d'integrità, prove di carico).

### Contenuto ancorato al testo
- Impostazione del progetto con effetti di gruppo e attrito negativo (γM del caso M1, Tab. 6.2.II) e
  rinvio al §7.11.5.3.2 per il sismico. Verifiche SLU (§6.4.3.1): GEO (carico limite assiale, carico
  limite trasversale, sfilamento in trazione, stabilità globale) e STR, con stabilità globale in Approccio
  1 Combinazione 2 (A2+M2+R2) e rimanenti verifiche in Approccio 2 (A1+M1+R3) e γR non portato in conto
  negli SLU strutturali. Resistenze a carico assiale (§6.4.3.1.1) con Tab. 6.4.II (γR base/laterale/
  totale/trazione per pali infissi/trivellati/a elica) e resistenza caratteristica dai fattori di
  correlazione delle Tab. 6.4.III (prove statiche), 6.4.IV (verticali indagate), 6.4.V (prove dinamiche);
  effetto di gruppo della palificata (§6.4.3.1.1.1); carichi trasversali con γT = 1,3 (Tab. 6.4.VI,
  §6.4.3.1.2). Verifiche SLE (§6.4.3.2). Fondazioni miste (§6.4.3.3-6.4.3.4). Controlli d'integrità su
  almeno il 5% dei pali con minimo 2, e su tutti i pali dei gruppi di grande diametro d≥80 cm se ≤4
  (§6.4.3.6). Prove di carico di progetto su pali pilota ≥2,5× l'azione SLE (resistenza al cedimento 10%
  del diametro, o ≥5% per d≥80 cm) e prove in corso d'opera a 1,5× (o 1,2× se strumentati) con numero
  minimo per numero di pali (§6.4.3.7).

### Scope e limiti
- Non calcola le resistenze, le verifiche o i coefficienti, non dimensiona i pali o la palificata, non
  riproduce le Tabelle 6.2.I/6.2.II/6.8.I né la Circolare 21/1/2019 n. 7, non tratta il caso sismico
  (§7.11.5.3.2) né le fondazioni superficiali (§6.4.2) se non nei richiami. Non sostituisce il progettista
  strutturale/geotecnico né la relazione geotecnica.

### Note di sviluppo
- Complementare alle altre skill NTC del repo (capacita-portante-fondazione-ntc §6.4.2, opere-sostegno-ntc
  §6.5, cedimenti-edometrici-ntc, combinazioni-carico-ntc, relazione-geologica-geotecnica-ntc), con cui
  condivide la fonte GU. Validazione Livello 2 con ingegnere strutturista/geotecnico.
