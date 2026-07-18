# CHANGELOG - opere-sostegno-ntc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-18

### Added (closes #368)
- Prima versione della skill di supporto al **progettista strutturale e geotecnico** per
  l'**inquadramento delle verifiche delle opere di sostegno** - **muri**, **paratie** e **strutture
  miste** - secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 6.5**, nell'area
  `strutture-geotecnica`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **NTC 2018 (DM 17 gennaio 2018)** - PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20
    febbraio 2018 - SHA256:
    dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46 (doppio download riproducibile,
    stessa fonte delle altre skill NTC del repo).
  - Par. 6.5 estratto con `pdftotext -layout` (pp. 194-197) e trascritto verbatim in
    `references/fonti/ntc2018-par-6-5.md` (§6.5, 6.5.1, 6.5.2/6.5.2.1/6.5.2.2, 6.5.3/6.5.3.1/6.5.3.1.1
    con Tab. 6.5.I/6.5.3.1.2, 6.5.3.2), con i simboli greci resi in modo corretto (γR, δ, φ').
- Estratto operativo `references/estratti/opere-sostegno-checklist.md`.
- Due task: `inquadra-criteri-azioni-sostegno.md` e `inquadra-verifiche-slu-sostegno.md`.
- Due esempi: muro a mensola in c.a. (stati limite, approccio, coefficienti Tab. 6.5.I, resistenza
  passiva nello scorrimento); paratia con un ordine di tiranti (stati limite GEO/UPL/HYD/STR, approcci/
  combinazioni, stabilità globale e stati limite idraulici, non planarità con δ > φ'/2).

### Contenuto ancorato al testo
- Tipologie (muri/paratie/strutture miste) e rinvio al §7.11.6 per il sismico (§6.5). Criteri di
  progetto: riempimento e drenaggio a tergo dei muri, dispositivi complementari e monitoraggio, effetti
  sulle costruzioni preesistenti, indagini estese alla stabilità locale e globale (§6.5.1). Azioni e
  modello geometrico: sovraccarichi a tergo, riduzione della quota di valle (minore tra 10% dell'altezza,
  10% della differenza di quota, 0,5 m), livello di falda negli SLU per k < 10⁻⁶ m/s (§6.5.2). Muri -
  SLU GEO (scorrimento, carico limite, ribaltamento, stabilità globale) e STR, con stabilità globale in
  Approccio 1 Combinazione 2 (A2+M2+R2) e rimanenti verifiche in Approccio 2 (A1+M1+R3) e Tab. 6.5.I (γR:
  capacità portante 1,4; scorrimento 1,1; ribaltamento 1,15; resistenza a valle 1,4); resistenza passiva
  nello scorrimento in generale non considerata (al più 50%, giustificata) (§6.5.3.1.1). Paratie - SLU
  GEO/UPL/HYD/STR con stabilità globale in Approccio 1 Comb. 2, UPL/HYD come §6.2.4.2, rimanenti in
  Approccio 1 Comb. 1 (A1+M1+R1) e Comb. 2 (A2+M2+R1) con R1 = 1, non planarità delle superfici per
  δ > φ'/2 (§6.5.3.1.2). Verifiche di esercizio sugli spostamenti (§6.5.3.2).

### Scope e limiti
- Non calcola le spinte, le verifiche o i coefficienti, non dimensiona il muro o la paratia, non
  riproduce le Tabelle 6.2.I/6.2.II/6.8.I né la Circolare 21/1/2019 n. 7, non tratta il caso sismico
  (§7.11.6) né la stabilità dei pendii (§6.8) se non nei richiami. Non sostituisce il progettista
  strutturale/geotecnico né la relazione geotecnica.

### Note di sviluppo
- Complementare alle altre skill NTC del repo (capacita-portante-fondazione-ntc §6.4.2,
  cedimenti-edometrici-ntc, combinazioni-carico-ntc, carichi-atmosferici-ntc,
  costruzioni-esistenti-ntc-cap8), con cui condivide la fonte GU. Validazione Livello 2 con ingegnere
  strutturista/geotecnico.
