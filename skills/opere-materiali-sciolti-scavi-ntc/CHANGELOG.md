# CHANGELOG - opere-materiali-sciolti-scavi-ntc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-21

### Added (closes #411)
- Prima versione della skill di supporto al **progettista geotecnico** per l'**inquadramento della progettazione
  e della verifica delle opere di materiali sciolti** (rilevati, argini, terrapieni, colmate, rinterri) e dei
  **fronti di scavo** secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 6.8**, nell'area
  `strutture-geotecnica`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **NTC 2018 (DM 17 gennaio 2018)** - PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio
    2018 - SHA256: dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46 (doppio download
    riproducibile, stessa fonte delle altre skill NTC del repo).
  - Par. 6.8 estratto con `pdftotext -layout` (pp. GU 201-202) e trascritto verbatim in
    `references/fonti/ntc2018-par-6-8.md`. Tab. 6.8.I (gamma_R = 1,1) e la soglia dei 2 m per i fronti di scavo
    verticali verificate anche sull'immagine renderizzata della pagina PDF 206 (pdftoppm).
- Estratto operativo `references/estratti/materiali-sciolti-scavi-checklist.md`.
- Due task: `inquadra-verifica-materiali-sciolti.md` e `inquadra-fronti-scavo.md`.
- Due esempi: verifica di un rilevato stradale (Combinazione 2 A2+M2+R2, Tab. 6.8.I gamma_R = 1,1, stabilita'
  globale nelle diverse fasi); fronte di scavo in trincea con la soglia dei 2 m per la struttura di sostegno.

### Contenuto ancorato al testo
- Ambito (§6.8): manufatti di materiali sciolti (rilevati, argini di difesa, rinfianchi, rinterri, terrapieni,
  colmate, scavi per piazzali/trincee) e opere con funzioni di drenaggio/filtro/transizione/fondazione/tenuta/
  protezione; esclusi gli sbarramenti di ritenuta idraulica. Criteri generali (§6.8.1): requisiti prestazionali,
  scelta e qualificazione dei materiali, posa in opera. Verifiche SLU (§6.8.2): condizione [6.2.1], Combinazione
  2 (A2+M2+R2) dell'Approccio 1, coefficienti Tab. 6.2.I/6.2.II/6.8.I (gamma_R = 1,1 per R2); stabilita' globale
  manufatto-terreno nelle diverse fasi costruttive, a fine costruzione e in esercizio; verifiche locali sugli
  elementi di rinforzo; opere di ritenuta idraulica con attenzione a sifonamento ed erosione. Verifiche SLE
  (§6.8.3): spostamenti. Aspetti costruttivi (§6.8.4): posa in strati, geosintetici certificati. Controlli e
  monitoraggio (§6.8.5). Fronti di scavo (§6.8.6): indagini geotecniche (§6.8.6.1); criteri e verifiche
  (§6.8.6.2) con struttura di sostegno per scavi in trincea a fronte verticale > 2 m con permanenza di personale
  o in prossimita' di manufatti (verifiche SLU e SLE), azioni nelle condizioni piu' sfavorevoli.

### Scope e limiti
- Non calcola le verifiche né dimensiona il manufatto/fronte o la struttura di sostegno, non definisce il modello
  geotecnico, non tratta gli sbarramenti di ritenuta idraulica (dighe in terra), la sicurezza dei lavoratori
  negli scavi (D.Lgs 81/2008 Titolo IV), le terre e rocce da scavo come sottoprodotti (DPR 120/2017) né la
  progettazione sismica (Cap. 7), non riproduce la Circolare 21/1/2019 n. 7. Non sostituisce il progettista.

### Note di sviluppo
- Complementa `opere-sostegno-ntc` (§6.5), `stabilita-pendii-naturali-ntc` (§6.3) e
  `relazione-geologica-geotecnica-ntc`, ed e' distinta e complementare a `sicurezza-scavi-fondazioni-dlgs81`
  (D.Lgs 81 Titolo IV) e `terre-rocce-scavo-dpr120` (DPR 120/2017). Validazione Livello 2 con ingegnere
  geotecnico.
