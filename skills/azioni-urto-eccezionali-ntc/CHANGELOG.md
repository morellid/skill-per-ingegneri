# CHANGELOG - azioni-urto-eccezionali-ntc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-20

### Added (closes #403)
- Prima versione della skill di supporto al **progettista strutturale** per l'**inquadramento delle azioni
  eccezionali da urto** secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 3.6.3 (Urti)**, nell'area
  `strutture-geotecnica`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **NTC 2018 (DM 17 gennaio 2018)** - PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio
    2018 - SHA256: dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46 (doppio download
    riproducibile, stessa fonte delle altre skill NTC del repo).
  - Par. 3.6.3 estratto con `pdftotext -layout` (pp. 65-66) e trascritto verbatim in
    `references/fonti/ntc2018-par-3-6-3.md` (Tab. 3.6.II/III, formule [3.6.7]-[3.6.9]).
- Estratto operativo `references/estratti/azioni-urto-checklist.md`.
- Due task: `inquadra-urti-traffico-veicolare.md` e `inquadra-urti-ferroviario-altri.md`.
- Due esempi: forza d'urto su un piedritto di cavalcavia autostradale (Fd,x=1000 kN, Fd,y=500 kN, a 1,25 m);
  forza d'urto su un elemento orizzontale con sottovia h=5,5 m (F=r·Fd,x, r=0,5, F=250 kN).

### Contenuto ancorato al testo
- Classificazione (§3.6.3.2, Tab. 3.6.II): categoria 1 effetti trascurabili, 2 localizzati, 3 generalizzati;
  applicazione per categoria 2 e 3. Urti da traffico veicolare sotto ponti (§3.6.3.3.1): Fd,y = 0,50·Fd,x
  [3.6.7] (non simultanee); forze statiche equivalenti Tab. 3.6.III (autostrade/extraurbane 1000 kN, strade
  locali 750, urbane 500, parcheggi automobili 50, veicoli merci > 3,5 t 150); punti di applicazione 0,5 m
  (automobili) o 1,25 m sopra la superficie di marcia; elementi orizzontali F = r·Fd,x [3.6.8] con r = 1,0
  fino a 5 m, decrescente da 1,0 a 0 tra 5 e 6 m, 0 oltre 6 m (intradosso a 10° verso l'alto, area 0,25×0,25
  m); carrelli elevatori F = 5·W [3.6.9] a 0,75 m dal piano di calpestio. Sopra i ponti (§3.6.3.3.2): forza
  orizzontale equivalente 100 kN sugli elementi di sicurezza (rinvio §5.1.3.10 per l'impalcato). Urti da
  traffico ferroviario (§3.6.3.4): analisi di rischio; in mancanza, azioni statiche equivalenti per distanza d
  (d ≤ 5 m: 4000/1500 kN; 5 < d ≤ 15 m: 2000/750 kN; d > 15 m: 0), a 1,80 m dal piano del ferro, non
  simultanee. Imbarcazioni/aeromobili (§3.6.3.5): rinvio ai documenti del Cap. 12.

### Scope e limiti
- Non calcola le sollecitazioni né dimensiona/verifica gli elementi o i sistemi di protezione, non riproduce le
  analisi di rischio (ferrovia) né le procedure per imbarcazioni/aeromobili, non tratta le esplosioni (§3.6.2)
  né l'incendio (§3.6.1), non riproduce la Circolare 21/1/2019 n. 7. Non sostituisce il progettista strutturale.

### Note di sviluppo
- Completa la famiglia delle azioni eccezionali (§3.6) con `resistenza-fuoco-strutture-ntc` (§3.6.1); distinta
  dalle azioni da traffico dei ponti (§5.1.3). Validazione Livello 2 con ingegnere strutturista.
