# CHANGELOG - regolarita-strutturale-sismica-ntc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-21

### Added (closes #419)
- Prima versione della skill di supporto al **progettista strutturale** per l'**inquadramento della valutazione
  della regolarita' di una costruzione in pianta e in altezza** ai fini della progettazione sismica secondo le
  **NTC 2018** (DM 17 gennaio 2018), **paragrafo 7.2.1**, nell'area `strutture-geotecnica`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **NTC 2018 (DM 17 gennaio 2018)** - PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio
    2018 - SHA256: dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46 (doppio download
    riproducibile, stessa fonte delle altre skill NTC del repo).
  - Par. 7.2.1 (sezione REGOLARITA') estratto con `pdftotext -layout` (p. GU 208) e trascritto verbatim in
    `references/fonti/ntc2018-par-7-2-1-regolarita.md`, insieme ai richiami dei par. 7.3.1 (fattore KR) e
    7.3.3.1 (analisi lineare statica).
- Estratto operativo `references/estratti/regolarita-checklist.md`.
- Due task: `inquadra-regolarita-pianta-altezza.md` e `inquadra-conseguenze-regolarita.md`.
- Due esempi: verifica di regolarita' in pianta e in altezza con le soglie; conseguenze della non regolarita' in
  altezza su KR e sul metodo di analisi.

### Contenuto ancorato al testo
- Regolare in pianta (§7.2.1, tutte le a-c): (a) masse/rigidezze approssimativamente simmetriche su due direzioni
  ortogonali e forma compatta (contorno convesso; rientranze <= 5% dell'orizzontamento); (b) rapporto tra i lati
  del rettangolo circoscritto < 4; (c) orizzontamento rigido nel proprio piano (diaframma rigido). Regolare in
  altezza (§7.2.1, tutte le d-g): (d) sistemi resistenti estesi per tutta l'altezza; (e) massa e rigidezza
  costanti o graduali (variazioni di massa <= 25%, rigidezza che non si riduce piu' del 30% ne' aumenta piu' del
  10% da un piano al sovrastante; strutture con pareti/nuclei in c.a. o muratura o telai controventati in acciaio
  cui sia affidato almeno il 50% dell'azione sismica alla base considerate regolari); (f) rapporto
  capacita'/domanda allo SLV che non differisce piu' del 30% tra orizzontamenti adiacenti; (g) restringimenti con
  continuita' (rientro <= 10% della dimensione sottostante ne' > 30% della dimensione al primo orizzontamento).
  Casi particolari (§7.2.1): struttura scatolare rigida (controlli sulla sola struttura soprastante), ponti
  (§7.9.2.1). Conseguenze: §7.3.1 KR = 1 (regolare in altezza) / 0,8 (non regolare), q_lim = q0 x KR; §7.3.3.1
  analisi lineare statica ammessa solo se T1 <= 2,5 TC o TD e la costruzione e' regolare in altezza.

### Scope e limiti
- Non calcola la struttura ne' esegue l'analisi, non determina q0 (Tab. 7.3.II) ne' le classi di duttilita'
  (§7.2.2), non calcola T1 (§7.3.3.2, skill periodo-proprio-t1-ntc), non tratta la regolarita' dei ponti
  (§7.9.2.1), non riproduce la Circolare 21/1/2019 n. 7. Non sostituisce il progettista.

### Note di sviluppo
- Complementa `spettro-risposta-ntc` (§3.2), `periodo-proprio-t1-ntc` (§7.3.3.2) e `combinazioni-carico-ntc`
  (§2.5.3), condividendo la stessa fonte GU. Validazione Livello 2 con ingegnere strutturista.
