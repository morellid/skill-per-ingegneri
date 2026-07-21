# CHANGELOG - tiranti-ancoraggio-ntc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-20

### Added (closes #399)
- Prima versione della skill di supporto al **progettista geotecnico e strutturale** per l'**inquadramento del
  progetto e della verifica dei tiranti di ancoraggio** secondo le **NTC 2018** (DM 17 gennaio 2018),
  **paragrafo 6.6**, nell'area `strutture-geotecnica`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **NTC 2018 (DM 17 gennaio 2018)** - PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio
    2018 - SHA256: dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46 (doppio download
    riproducibile, stessa fonte delle altre skill NTC del repo).
  - Par. 6.6 estratto con `pdftotext -layout` (pp. 197-199) e trascritto verbatim in
    `references/fonti/ntc2018-par-6-6.md` (Tab. 6.6.I/II/III, formule [6.6.1]-[6.6.2]).
- Estratto operativo `references/estratti/tiranti-ancoraggio-checklist.md`.
- Due task: `inquadra-verifica-sfilamento-tiranti.md` e `inquadra-criteri-prove-tiranti.md`.
- Due esempi: verifica a sfilamento di un tirante permanente con Rak da prove su 3 ancoraggi; numero di prove
  di progetto per 120 ancoraggi e prova in corso d'opera a 1,2·Pd.

### Contenuto ancorato al testo
- Definizione dei tiranti (§6.6) e criteri di progetto (§6.6.1): ancoraggi provvisori/permanenti, attivi
  (presollecitati)/passivi; indicazione di orientazione, lunghezza, numero, Rad, tesatura; conferma
  sperimentale con prove sempre necessaria. Verifica SLU a sfilamento (§6.6.2): condizione [6.2.1] Ed ≤ Rad,
  combinazione A1+M1+R3, Rad = Rak/γR con Tab. 6.6.I (γR = 1,1 temporanei, 1,2 permanenti). Rak da prove
  [6.6.1] con ξa1/ξa2 (Tab. 6.6.II: 1,5/1,4/1,3 e 1,5/1,3/1,2) o da calcolo [6.6.2] con ξa3/ξa4 (Tab. 6.6.III:
  1,80/1,75/1,70/1,65/1,60 e 1,80/1,70/1,65/1,60/1,55); nel calcolo analitico non si applicano γ ai parametri
  (M1). Aspetti costruttivi (§6.6.3): sistemi qualificati (§11.5.2), fori ≥ nominale, tesatura dopo presa.
  Prove di carico (§6.6.4): di progetto su ancoraggi preliminari (1/2/3/7/8/10 per <30/31-50/51-100/101-200/
  201-500/>500 ancoraggi); in corso d'opera su tutti gli ancoraggi a 1,2·Pd (azione SLE).

### Scope e limiti
- Non calcola la resistenza allo sfilamento né dimensiona il tirante o l'armatura, non esegue né interpreta le
  prove di carico, non riproduce i sistemi di ancoraggio come prodotti (§11.5.2), non tratta le paratie/muri
  (§6.5) né la progettazione sismica (Cap. 7), non riproduce la Circolare 21/1/2019 n. 7. Non sostituisce il
  progettista.

### Note di sviluppo
- Complementa `opere-sostegno-ntc` (§6.5), condividendo la stessa fonte GU. Validazione Livello 2 con ingegnere
  geotecnico/strutturista.
