# CHANGELOG - azioni-traffico-ponti-ferroviari-ntc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-23

### Added (closes #448)
- Prima versione della skill di supporto al **progettista strutturale** per l'**inquadramento delle azioni da
  traffico sui ponti ferroviari** secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 5.2.2**, nell'area
  `strutture-geotecnica`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **NTC 2018 (DM 17 gennaio 2018)** - PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio
    2018 - SHA256: dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46 (doppio download
    riproducibile, stessa fonte delle altre skill NTC del repo).
  - Par. 5.2.2 (pagine PDF 167-174) estratto con `pdftotext -layout` e verificato sull'immagine (`pdftoppm -r
    150 -png`) delle pagine PDF 168 (LM71) e 171 (Φ) per i valori dei carichi e le formule; trascritto verbatim
    in `references/fonti/ntc2018-par-5-2.md`.
- Estratto operativo `references/estratti/azioni-ferroviari-checklist.md`.
- Due task: `inquadra-modelli-carico-verticali-ferroviari.md` e `inquadra-effetti-dinamici-azioni-orizzontali.md`.
- Due esempi: valori dei modelli LM71/SW con coefficiente di adattamento α; coefficiente dinamico Φ2/Φ3 per
  una trave semplicemente appoggiata data la lunghezza caratteristica L_φ.

### Contenuto ancorato al testo
- Modelli di carico verticali (§5.2.2.2.1): LM71 (4 assi da 250 kN a interasse 1,60 m + 80 kN/m; eccentricità
  s/18 con s=1435 mm; α=1,1); SW/0 (133 kN/m, a 15,0, c 5,3; α 1,1) e SW/2 (150 kN/m, a 25,0, c 7,0; α 1,0) -
  Tab. 5.2.I; treno scarico 10 kN/m; marciapiedi 10 kN/m². Effetti dinamici (§5.2.2.2.3): Φ2=1,44/(√L_φ−0,2)
  +0,82 con 1,00≤Φ2≤1,67 [5.2.6] (elevato standard manutentivo); Φ3=2,16/(√L_φ−0,2)+0,73 con 1,00≤Φ3≤2,00
  [5.2.7] (ridotto); L_φ lunghezza caratteristica (Tab. 5.2.II); Φ non su treno scarico/treni reali; per
  V>200 km/h o tipologie non convenzionali analisi dinamica con convogli reali. Azioni orizzontali (§5.2.2.3):
  forza centrifuga [5.2.9]/[5.2.10] (a 1,80 m sul P.F.); serpeggio Q_sk=100 kN; avviamento 33 kN/m·L≤1000 kN;
  frenatura 20 kN/m·L≤6000 kN (LM71/SW0), 35 kN/m·L (SW2); ×α, non ×Φ.

### Scope e limiti
- Non esegue le combinazioni delle azioni, l'analisi dinamica con treni reali (V>200 km/h o tipologie non
  convenzionali) né le verifiche (SLU/SLE, fatica, interazione statica binario-struttura); non riproduce la
  Tab. 5.2.II completa né i criteri progettuali/manutentivi (§5.2.1). Non sostituisce il progettista strutturale.

### Note di sviluppo
- Distinta da `azioni-traffico-ponti-stradali-ntc` (§5.1.3): modelli di carico, coefficienti e azioni sono
  completamente diversi. Condivide la fonte GU con le altre skill NTC. Validazione Livello 2 con ingegnere
  strutturista di ponti.
