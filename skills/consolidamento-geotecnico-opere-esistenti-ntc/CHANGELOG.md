# CHANGELOG - consolidamento-geotecnico-opere-esistenti-ntc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-21

### Added (closes #417)
- Prima versione della skill di supporto al **progettista geotecnico e strutturale** per l'**inquadramento della
  progettazione degli interventi di consolidamento geotecnico di opere esistenti** (sottofondazioni, rinforzo
  delle fondazioni, miglioramento del terreno di fondazione) secondo le **NTC 2018** (DM 17 gennaio 2018),
  **paragrafo 6.10**, nell'area `strutture-geotecnica`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **NTC 2018 (DM 17 gennaio 2018)** - PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio
    2018 - SHA256: dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46 (doppio download
    riproducibile, stessa fonte delle altre skill NTC del repo).
  - Par. 6.10 estratto con `pdftotext -layout` (pp. GU 203-204) e trascritto verbatim in
    `references/fonti/ntc2018-par-6-10.md`.
- Estratto operativo `references/estratti/consolidamento-geotecnico-checklist.md`.
- Due task: `inquadra-criteri-tipi-consolidamento.md` e `inquadra-indagini-controlli-consolidamento.md`.
- Due esempi: i sei tipi di consolidamento geotecnico e le cautele per gli interventi con variazioni di volume;
  obbligo di controllo dell'efficacia e progetto unitario geotecnico-strutturale.

### Contenuto ancorato al testo
- Ambito (§6.10): provvedimenti sul sistema manufatto-terreno per eliminare o mitigare difetti di comportamento
  di un'opera esistente. Criteri generali (§6.10.1): individuazione delle cause (sovrastruttura, fondazioni,
  terreno; anomali spostamenti del terreno; deterioramento dei materiali); progetto sviluppato unitariamente con
  quello strutturale; modalita' esecutive e opere provvisionali parte integrante; metodo osservazionale se la
  complessita' e' documentata. Indagini (§6.10.2): su terreno e fondazioni esistenti dalla documentazione
  disponibile; cautele per manufatti sensibili; misura dei caratteri cinematici, delle pressioni interstiziali e
  degli spostamenti nel volume significativo, protratte per fenomeni stagionali. Tipi di consolidamento
  (§6.10.3): miglioramento/rinforzo dei terreni di fondazione; miglioramento/rinforzo dei materiali della
  fondazione; ampliamento della base (se superficiale); trasferimento del carico a strati piu' profondi;
  sostegni laterali; rettifica degli spostamenti del piano di posa; particolari cautele per interventi con
  variazioni di volume (congelamento, iniezioni, gettiniezione). Controlli e monitoraggio (§6.10.4): controllo
  dell'efficacia obbligatorio quando l'intervento comporta una ridistribuzione delle sollecitazioni al contatto
  terreno-manufatto; monitoraggio previsto in progetto; esiti come elemento di collaudo.

### Scope e limiti
- Non calcola ne' dimensiona gli interventi, non definisce il modello geotecnico ne' progetta il risanamento
  strutturale, non tratta il miglioramento/rinforzo dei terreni in generale (§6.9), la classificazione sismica
  dell'esistente (Cap. 8) ne' la progettazione sismica (Cap. 7), non riproduce la Circolare 21/1/2019 n. 7. Non
  sostituisce il progettista.

### Note di sviluppo
- Complementa `costruzioni-esistenti-ntc-cap8` (Cap. 8) e `relazione-geologica-geotecnica-ntc`, condividendo la
  stessa fonte GU. Validazione Livello 2 con ingegnere geotecnico/strutturista.
