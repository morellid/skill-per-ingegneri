# CHANGELOG - carichi-permanenti-sovraccarichi-ntc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-18

### Added (closes #378)
- Prima versione della skill di supporto al **progettista strutturale** per l'**analisi dei carichi** -
  **carichi permanenti** e **sovraccarichi variabili** per **categoria d'uso** delle costruzioni civili e
  industriali - secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 3.1**, nell'area
  `strutture-geotecnica`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **NTC 2018 (DM 17 gennaio 2018)** - PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20
    febbraio 2018 - SHA256:
    dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46 (doppio download riproducibile,
    stessa fonte delle altre skill NTC del repo).
  - Par. 3.1 estratto con `pdftotext -layout` (pp. 41-44) e trascritto verbatim in
    `references/fonti/ntc2018-par-3-1.md` (§3.1.1-3.1.4.3 con Tab. 3.1.I e Tab. 3.1.II), con i simboli
    resi in modo corretto (α_A, α_n, ψ0).
- Estratto operativo `references/estratti/carichi-sovraccarichi-checklist.md`.
- Due task: `inquadra-sovraccarichi-categoria.md` e `inquadra-permanenti-riduzioni.md`.
- Due esempi: edificio a uso misto residenziale/uffici/negozio (sovraccarichi per categoria d'uso e
  parapetti); carico dei tramezzi come g2 e riduzioni α_A/α_n su trave e pilastro.

### Contenuto ancorato al testo
- Pesi propri dei materiali strutturali con la Tab. 3.1.I dei pesi dell'unità di volume (calcestruzzo
  armato 25,0 kN/m³, acciaio 78,5, ecc.) (§3.1.2). Carichi permanenti non strutturali con la correlazione
  del carico equivalente distribuito g2 dei tramezzi al peso proprio lineare G2 (0,40/0,80/1,20/1,60/2,00
  kN/m² per G2 fino a 5,00 kN/m; oltre, posizionamento effettivo) (§3.1.3). Sovraccarichi qk/Qk/Hk con la
  Tab. 3.1.II dei valori per le categorie d'uso A-K (residenziale, uffici B1/B2, affollamento C1-C5,
  commerciale D1/D2, magazzini/industriale E1/E2, rimesse/parcheggi F/G, coperture H/I/K, scale e balconi)
  e i carichi atipici da valutare caso per caso (§3.1.4). Riduzioni dei sovraccarichi con α_A per l'area di
  influenza ((5/7)·ψ0 + 10/A ≤ 1,0, non minore di 0,6 per C e D) e α_n per il numero di piani caricati ((2
  + (n−2)·ψ0)/n), non combinabili (§3.1.4.1). Sovraccarichi concentrati Qk per verifiche locali con le
  impronte di carico (§3.1.4.2) e orizzontali lineari Hk applicati a 1,20 m e ai parapetti al bordo
  superiore (§3.1.4.3).

### Scope e limiti
- Non calcola i carichi di progetto né combina le azioni, non dimensiona gli elementi, non tratta i
  carichi da ponte (cap. 5), l'azione sismica (§3.2) né il vento/neve (§3.3/3.4), non riproduce la Tab.
  2.5.I dei coefficienti ψ né la Circolare 21/1/2019 n. 7. Non sostituisce il progettista strutturale.

### Note di sviluppo
- Complementare a `combinazioni-carico-ntc` (combinazioni delle azioni) e `carichi-atmosferici-ntc`
  (vento/neve), con cui condivide la fonte GU. Validazione Livello 2 con ingegnere strutturista.
