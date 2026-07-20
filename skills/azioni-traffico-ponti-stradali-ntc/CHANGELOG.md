# CHANGELOG - azioni-traffico-ponti-stradali-ntc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-20

### Added (closes #394)
- Prima versione della skill di supporto al **progettista strutturale di ponti** per l'**inquadramento della
  definizione delle azioni da traffico** (e delle altre azioni) sui **ponti stradali** secondo le **NTC
  2018** (DM 17 gennaio 2018), **paragrafo 5.1.3**, nell'area `strutture-geotecnica`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **NTC 2018 (DM 17 gennaio 2018)** - PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio
    2018 - SHA256: dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46 (doppio download
    riproducibile, stessa fonte delle altre skill NTC del repo).
  - Par. 5.1 estratto con `pdftotext -layout` (pp. 150-157) e trascritto verbatim in
    `references/fonti/ntc2018-par-5-1.md` (§5.1.1-5.1.4 con le Tab. 5.1.I-VI e le formule [5.1.1]-[5.1.4]),
    con i simboli resi in modo corretto (γ, ψ, ε, Q, q).
- Estratto operativo `references/estratti/azioni-traffico-ponti-checklist.md`.
- Due task: `inquadra-corsie-schemi-carico.md` e `inquadra-azioni-derivate-combinazioni.md`.
- Due esempi: numero/larghezza delle corsie convenzionali e Schemi di Carico per una superficie carrabile di
  10,50 m; azione di frenamento q3 sulla corsia 1 con la formula [5.1.4].

### Contenuto ancorato al testo
- Inquadramento dei ponti (§5.1.1), prescrizioni generali (altezza libera ≥ 5 m, compatibilità idraulica
  Tr = 200 anni, franco ≥ 1,50 m; §5.1.2), elenco delle azioni e permanenti g1/g2/g3, distorsioni ε1-ε4
  (§5.1.3.1-5.1.3.2). Carichi verticali da traffico: corsie convenzionali (Tab. 5.1.I: w<5,40→nl=1;
  5,4≤w<6,0→nl=2; 6,0≤w→nl=Int(w/3)), Schemi di Carico 1-5 e 6.a/b/c ([5.1.1]-[5.1.3]), categorie stradali,
  intensità Qik/qik (Tab. 5.1.II: corsia 1 300/9,00; corsia 2 200/2,50; corsia 3 100/2,50; altre 0/2,50),
  diffusione a 45° (§5.1.3.3). Incremento dinamico q2 (§5.1.3.4); frenamento q3 = 0,6·(2·Q1k) + 0,10·q1k·w1·L
  fra 180 e 900 kN [5.1.4] (§5.1.3.5); centrifuga q4 (Tab. 5.1.III: R<200→0,2·Qv; 200≤R≤1500→40·Qv/R;
  R≥1500→0) (§5.1.3.6). Altre azioni: neve/vento q5 (parete 3 m; neve non concomitante col traffico salvo
  ponti coperti), temperatura q7, parapetti/urto q8 (parapetti h≥1,10 m, 1,5 kN/m; forze ×1,50; γ unitario),
  resistenze passive q9, sismiche (ψ2j=0,0 di regola, 0,2 zona urbana), eccezionali (§5.1.3.7-5.1.3.13).
  Combinazioni: gruppi di azioni (Tab. 5.1.IV), γ parziali SLU (Tab. 5.1.V, EQU/A1/A2) e ψ (Tab. 5.1.VI)
  (§5.1.3.14).

### Scope e limiti
- Non calcola le sollecitazioni né esegue le verifiche, non individua la disposizione più gravosa dei
  carichi mobili, non dimensiona l'impalcato/pile/appoggi, non riproduce le figure (Fig. 5.1.1/5.1.2/5.1.3),
  non tratta i ponti ferroviari (§5.2), la fatica (§5.1.4) né la sismica dei ponti (§7.9), non riproduce la
  Circolare 21/1/2019 n. 7. Non sostituisce il progettista strutturale.

### Note di sviluppo
- Apre il Capitolo 5 (ponti) delle skill NTC, condividendo con le altre la stessa fonte GU. Validazione
  Livello 2 con ingegnere strutturista/progettista di ponti.
