# CHANGELOG - costruzioni-calcestruzzo-zona-sismica-ntc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-25

### Added (closes #474)
- Prima versione della skill di supporto al **progettista strutturale** per la **progettazione sismica delle
  costruzioni di calcestruzzo armato** secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 7.4** (Cap. 7),
  nell'area `strutture-geotecnica`. Completa la serie sismica per materiale (§7.5 acciaio, §7.6 composte, §7.7 legno,
  §7.8 muratura, §7.9 ponti) con il tassello del c.a.
- Fonte scaricata, hashata e letta (Regola zero):
  - **NTC 2018 (DM 17 gennaio 2018)** - PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio
    2018 - SHA256 dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46 (doppio download
    riproducibile, stessa fonte delle altre skill NTC del repo).
  - Par. 7.4 (pagine PDF 227-236 = GU 223-232) estratto con `pdftotext -layout`; i valori numerici e le formule
    (tipologie, αu/α1, 55%/65%, [7.4.1]-[7.4.4]) verificati sull'immagine (`pdftoppm -r 150 -png`) delle pagine PDF
    228/229/230 e trascritti in `references/fonti/ntc2018-par-7-4.md`.
- Estratto operativo `references/estratti/ca-sismica-checklist.md`.
- Due task: `inquadra-tipologie-e-fattore-comportamento.md` e `applica-gerarchia-delle-resistenze.md`.
- Due esempi: scelta di tipologia e fattore di comportamento per un edificio a telaio; gerarchia delle resistenze al
  nodo trave-pilastro.

### Contenuto ancorato al testo
- Materiali (§7.4.2): acciaio B450C; B450A solo diametri 5-10 mm per reti/tralicci o armatura trasversale se
  plasticizzazione impedita/secondari/non dissipativo. Tipologie (§7.4.3.1): telaio e pareti con taglio alla base ≥
  65%, miste (> 50% ai telai → equiv. telai), pendolo inverso (≥ 50% massa terzo superiore), monopiano (N ≤ 30%
  resistenza cls), deformabili torsionalmente (r²/ls² ≥ 1, ls² = (L²+B²)/12), pareti estese debolmente armate (periodo
  ≤ TC, solo CD"B"). Fattori (§7.4.3.2): q per §7.3.1/Tab. 7.3.II; pareti accoppiate se momento base equilibrato ≥ 20%;
  αu/α1 telai 1,1/1,2/1,3, pareti 1,0/1,1/1,2; travi a spessore → CD"B"; q > 1,5 per altre tipologie → analisi non
  lineari. Gerarchia delle resistenze (§7.4.4): γRd da Tab. 7.2.I; verifiche RES + DUT (§7.3.6.1); travi taglio da
  equilibrio della trave incernierata con capacità flessionale amplificata di γRd, CD"A" ctgθ=1 e VR1 [7.4.1] con
  armature ±45° VEd,max ≤ As·fyd/√2 [7.4.2], duttilità μφ [7.4.3] e μφ = 2μd − 1; pilastri pressoflessione N ≤ 55%
  (CD"A") / 65% (CD"B") della capacità a compressione del solo cls; nodo pilastro forte-trave debole ΣMc,Rd ≥
  γRd·ΣMb,Rd [7.4.4] (escluso sommità ultimo orizzontamento).

### Scope e limiti
- Non esegue il progetto né le verifiche di dettaglio (RES/DUT complete, dettagli costruttivi §7.4.6); non tratta il
  progetto ordinario non sismico (§4.1) né la macchina generale del q (§7.3.1). Non sostituisce il progettista né la
  Circolare 2019.

### Note di sviluppo
- Distinta da `costruzioni-calcestruzzo-ntc` (§4.1), `fattore-comportamento-q-sismica-ntc` (§7.3.1) e dalle altre skill
  sismiche per materiale (§7.5-7.10). Condivide la fonte GU con le altre skill NTC. Validazione Livello 2 con ingegnere
  strutturista esperto di progettazione sismica del c.a.
