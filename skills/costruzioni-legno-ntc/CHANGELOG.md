# CHANGELOG - costruzioni-legno-ntc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-19

### Added (closes #382)
- Prima versione della skill di supporto al **progettista strutturale** per l'**inquadramento della
  progettazione delle costruzioni di legno** (caso **non sismico**) secondo le **NTC 2018** (DM 17 gennaio
  2018), **paragrafo 4.4**, nell'area `strutture-geotecnica`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **NTC 2018 (DM 17 gennaio 2018)** - PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20
    febbraio 2018 - SHA256:
    dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46 (doppio download riproducibile,
    stessa fonte delle altre skill NTC del repo).
  - Par. 4.4 estratto con `pdftotext -layout` (pp. 132-141) e trascritto verbatim in
    `references/fonti/ntc2018-par-4-4.md` (§4.4.1-4.4.15 con Tab. 4.4.I-4.4.V), con i simboli resi in modo
    corretto (σ, γM, λ, λrel, τ, βc).
- Estratto operativo `references/estratti/costruzioni-legno-checklist.md`.
- Due task: `inquadra-resistenze-progetto-legno.md` e `inquadra-verifiche-slu-sle-legno.md`.
- Due esempi: kmod e γM per una trave di copertura in legno lamellare (classe di servizio 2, durata media);
  frecce limite SLE e kdef per un solaio in legno massiccio (classe di servizio 1, L/300 e L/200).

### Contenuto ancorato al testo
- Classi di durata del carico con la Tab. 4.4.I (permanente >10 anni, lunga 6 mesi-10 anni, media 1
  settimana-6 mesi, breve <1 settimana, istantaneo) e l'attribuzione tipica di peso proprio, variabili,
  neve, vento (§4.4.4). Classi di servizio 1/2/3 con la Tab. 4.4.II (§4.4.5). Resistenza di progetto
  Xd = kmod·Xk/γM con la Tab. 4.4.III del coefficiente γM (colonna A/B: legno massiccio 1,50/1,45,
  lamellare 1,45/1,35, CLT 1,45/1,35, particelle/fibre 1,50/1,40, LVL/compensato/OSB 1,40/1,30, unioni
  1,50/1,40, eccezionali 1,00) e la Tab. 4.4.IV del coefficiente kmod, con kmod di combinazione pari
  all'azione di minor durata (§4.4.6). Stati limite di esercizio con la Tab. 4.4.V del kdef, la
  deformazione a lungo termine con il fattore 1/(1+kdef) e le frecce limite (istantanea < L/300, finale
  < L/200) (§4.4.7). Stati limite ultimi con le verifiche di resistenza (trazione e compressione parallela
  e perpendicolare alla fibratura, flessione con km = 0,7 rettangolari / 1,0 altre, tenso/pressoflessione,
  taglio, torsione con ksh) e le verifiche di stabilità (kcrit,m per lo svergolamento con soglia
  λrel,m ≤ 0,75, kcrit,c per l'instabilità di colonna con soglia λrel,c ≤ 0,3 e βc = 0,2 massiccio / 0,1
  lamellare) (§4.4.8). Collegamenti (§4.4.9), elementi e sistemi strutturali (§4.4.10-4.4.11), robustezza
  (§4.4.12), durabilità (§4.4.13), resistenza al fuoco con rinvio a UNI EN 1995-1-2 e γM eccezionali
  (§4.4.14), regole per l'esecuzione con lo scostamento massimo 1/500 lamellare e 1/300 massiccio
  (§4.4.15).

### Scope e limiti
- Non calcola le resistenze né esegue le verifiche, non dimensiona elementi e collegamenti, non riproduce
  le proprietà dei materiali (fk, moduli elastici, kh) del §11.7 né gli Eurocodici (UNI EN 1995), non
  tratta la progettazione sismica (§7.7), non riproduce la Circolare 21/1/2019 n. 7. Non sostituisce il
  progettista strutturale.

### Note di sviluppo
- Complementare a `costruzioni-muratura-ntc` (§4.5) e alle altre skill NTC del repo (carichi, combinazioni,
  fondazioni, opere di sostegno), con cui condivide la fonte GU. Validazione Livello 2 con ingegnere
  strutturista.
