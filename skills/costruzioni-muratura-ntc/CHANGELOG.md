# CHANGELOG - costruzioni-muratura-ntc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-19

### Added (closes #380)
- Prima versione della skill di supporto al **progettista strutturale** per l'**inquadramento della
  progettazione delle costruzioni in muratura** (caso **non sismico**) secondo le **NTC 2018** (DM 17
  gennaio 2018), **paragrafo 4.5**, nell'area `strutture-geotecnica`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **NTC 2018 (DM 17 gennaio 2018)** - PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20
    febbraio 2018 - SHA256:
    dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46 (doppio download riproducibile,
    stessa fonte delle altre skill NTC del repo).
  - Par. 4.5 estratto con `pdftotext -layout` (pp. 141-146) e trascritto verbatim in
    `references/fonti/ntc2018-par-4-5.md` (§4.5.1-4.5.7 con Tab. 4.5.Ia/Ib, 4.5.II, 4.5.III, 4.5.IV), con
    i simboli resi in modo corretto (γM, γs, λ, Π, Φ, ρ).
- Estratto operativo `references/estratti/costruzioni-muratura-checklist.md`.
- Due task: `inquadra-materiali-resistenze-muratura.md` e
  `inquadra-organizzazione-verifiche-muratura.md`.
- Due esempi: categoria dell'elemento e coefficiente γM per un muro portante (Tab. 4.5.Ia + Tab. 4.5.II);
  applicabilità delle verifiche semplificate a un edificio in muratura ordinaria (§4.5.6.4, γM = 4,2).

### Contenuto ancorato al testo
- Classificazione degli elementi resistenti in base alla percentuale di foratura Π con le Tab. 4.5.Ia
  (laterizio) e 4.5.Ib (calcestruzzo): pieni (Π ≤ 15%), semipieni (15% < Π ≤ 45%), forati (45% < Π ≤ 55%),
  categoria I/II (§4.5.2). Caratteristiche meccaniche fk/fvk0/E/G con il controllo sperimentale per
  fk ≥ 8 MPa (§4.5.3). Organizzazione strutturale con il comportamento scatolare, cordoli e incatenamenti,
  gli spessori minimi dei muri portanti (150/200/240 mm per gli elementi artificiali pieni/semipieni/forati
  e 240/400/500 mm per la pietra squadrata/listata/non squadrata) e la snellezza convenzionale
  λ = h0/t ≤ 20 (§4.5.4). Resistenze di progetto fd = fk/γM e fvd = fvk/γM con la Tab. 4.5.II del
  coefficiente γM (da 2,0 a 3,0 in funzione della categoria degli elementi I/II, del tipo di malta e della
  classe di esecuzione 1/2) (§4.5.6.1). Verifiche agli stati limite ultimi (pressoflessione fuori piano e
  nel piano, taglio, carichi concentrati) e metodo semplificato per i carichi laterali con
  fd,rid = Φ·fd (Tab. 4.5.III), h0 = ρ·h (Tab. 4.5.IV) e le eccentricità (e1, e2 ≤ 0,33 t) (§4.5.6.2).
  Verifiche semplificate per gli edifici semplici con γM = 4,2, i limiti (fino a 3 piani per la muratura
  ordinaria e 4 per l'armata, interpiano ≤ 3,5 m, snellezza ≤ 12, carico variabile ≤ 3,00 kN/m², rapporto
  fra i lati ≥ 1/3) e la verifica σ = N/(0,65 A) ≤ fk/γM (§4.5.6.4). Muratura armata con le armature minime
  (diametro ≥ 5 mm, percentuali di armatura), la malta ≥ 10 MPa, il conglomerato ≥ C12/15 e γs = 1,15
  (§4.5.7).

### Scope e limiti
- Non calcola le resistenze né esegue le verifiche, non dimensiona la muratura, non tratta la progettazione
  sismica (§7.8) né la Tab. 7.8.II, la resistenza al fuoco (§4.5.11), il cap. 11.10 (materiali) né gli
  Eurocodici (§4.6), non riproduce la Circolare 21/1/2019 n. 7. Non sostituisce il progettista strutturale.

### Note di sviluppo
- Complementare alle altre skill NTC del repo (carichi, combinazioni, fondazioni, opere di sostegno), con
  cui condivide la fonte GU. Validazione Livello 2 con ingegnere strutturista.
