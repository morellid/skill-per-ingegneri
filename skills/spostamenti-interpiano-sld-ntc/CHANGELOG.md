# CHANGELOG - spostamenti-interpiano-sld-ntc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-21

### Added (closes #421)
- Prima versione della skill di supporto al **progettista strutturale** per l'**inquadramento della verifica di
  deformabilita' allo stato limite di danno (SLD)** - i limiti di spostamento di interpiano - degli elementi
  strutturali secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafi 7.3.6 e 7.3.6.1**, nell'area
  `strutture-geotecnica`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **NTC 2018 (DM 17 gennaio 2018)** - PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio
    2018 - SHA256: dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46 (doppio download
    riproducibile, stessa fonte delle altre skill NTC del repo).
  - Par. 7.3.6 e 7.3.6.1 estratti con `pdftotext -layout` (pp. GU 221-222) e trascritti verbatim in
    `references/fonti/ntc2018-par-7-3-6-1-sld.md`. I sei limiti [7.3.11a]-[7.3.15] e gli operatori relazionali
    (<= per a-d, < per e) verificati anche sull'immagine renderizzata della pagina PDF 226 (pdftoppm), perche'
    pdftotext restituisce il simbolo <= in modo non affidabile.
- Estratto operativo `references/estratti/spostamenti-interpiano-checklist.md`.
- Due task: `inquadra-limiti-spostamento-interpiano.md` e `inquadra-classe-uso-stato-limite.md`.
- Due esempi: telaio in c.a. con tamponature fragili in CU II (limite 0,0050 h); edificio strategico CU IV con
  tamponature duttili (SLO, 2/3 di 0,0075 h).

### Contenuto ancorato al testo
- Quadro (§7.3.6, Tab. 7.3.III): per gli elementi strutturali primari la verifica di rigidezza (RIG) si esegue
  allo SLD per le CU I e II e allo SLO per le CU III e IV. Limiti di spostamento di interpiano (§7.3.6.1), con
  q*dr rapportato all'altezza di piano h: q*dr <= 0,0050 h per tamponature fragili collegate rigidamente
  [7.3.11a]; <= 0,0075 h per tamponature duttili collegate rigidamente [7.3.11b]; <= drp e <= 0,0100 h per
  tamponature progettate per non subire danni [7.3.12]; <= 0,0020 h per muratura ordinaria [7.3.13]; <= 0,0030 h
  per muratura armata [7.3.14]; < 0,0025 h per muratura confinata [7.3.15]. dr = differenza tra gli spostamenti
  del solaio superiore e inferiore (analisi lineare §7.3.3.3 o non lineare §7.3.4), su modello non comprensivo
  delle tamponature; h = altezza di piano; q = fattore di comportamento. Regole: per le CU III e IV (SLO) i
  limiti sono i 2/3 di quelli indicati; in caso di coesistenza di tipi diversi nel medesimo piano si assume il
  limite piu' restrittivo; se dr > 0,005 h (caso b) le verifiche di capacita' di spostamento si estendono a
  tutte le tamponature, alle tramezzature interne e agli impianti.

### Scope e limiti
- Non calcola gli spostamenti ne' esegue l'analisi (§7.3.3.3/§7.3.4), non determina q, non tratta le verifiche
  di resistenza (RES) o duttilita' (DUT), gli elementi non strutturali (§7.3.6.2) ne' gli impianti (§7.3.6.3),
  non riproduce la Circolare 21/1/2019 n. 7. Non sostituisce il progettista.

### Note di sviluppo
- Complementa `regolarita-strutturale-sismica-ntc` (§7.2.1/7.3.1), `periodo-proprio-t1-ntc` (§7.3.3.2) e
  `spettro-risposta-ntc` (§3.2), condividendo la stessa fonte GU. Validazione Livello 2 con ingegnere
  strutturista.
