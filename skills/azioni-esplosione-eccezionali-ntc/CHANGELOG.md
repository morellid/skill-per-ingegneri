# CHANGELOG - azioni-esplosione-eccezionali-ntc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-20

### Added (closes #407)
- Prima versione della skill di supporto al **progettista strutturale** per l'**inquadramento delle azioni
  eccezionali da esplosione** secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 3.6.2 (Esplosioni)**,
  nell'area `strutture-geotecnica`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **NTC 2018 (DM 17 gennaio 2018)** - PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio
    2018 - SHA256: dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46 (doppio download
    riproducibile, stessa fonte delle altre skill NTC del repo).
  - Par. 3.6.2 estratto con `pdftotext -layout` (pagina GU 65) e trascritto verbatim in
    `references/fonti/ntc2018-par-3-6-2.md` (Tab. 3.6.I, formule [3.6.5a]/[3.6.5b], [3.6.6]). **Gli operatori
    "+" delle formule [3.6.5a]/[3.6.5b] sono stati verificati sull'immagine del PDF** (pdftoppm della pagina),
    perché pdftotext li rende come spazi.
- Estratto operativo `references/estratti/azioni-esplosione-checklist.md`.
- Due task: `inquadra-classificazione-modellazione-esplosioni.md` e `inquadra-criteri-progettazione-esplosioni.md`.
- Due esempi: pressione statica equivalente in un ambiente con pannelli di sfogo (pv=3, Av/V=0,10, V=500 m³ →
  pd=8,5 kN/m²); pressione di 20 kN/m² sugli elementi chiave.

### Contenuto ancorato al testo
- Ambito (§3.6.2.1): miscele esplosive di polveri/gas in aria o materiali esplosivi; escluse le esplosioni
  esterne. Classificazione (§3.6.2.2, Tab. 3.6.I): categoria 1 effetti trascurabili, 2 localizzati, 3
  generalizzati. Modellazione (§3.6.2.3): onde di pressione ricondotte a pressioni statiche equivalenti; Cat. 1
  nessuna verifica; Cat. 2 con pannelli di sfogo pd = valore maggiore fra pd = 3 + pv [3.6.5a] e pd = 3 + pv/2 +
  0,04/(Av/V)² [3.6.5b] (pv, Av, V), vincolo 0,05 m⁻¹ ≤ Av/V ≤ 0,15 m⁻¹ [3.6.6], valide per V ≤ 1000 m³,
  pressione simultanea su tutte le pareti, elementi chiave e connessioni pd = 20 kN/m² da ogni direzione; Cat. 3
  studi più approfonditi. Criteri di progettazione (§3.6.2.4): danneggiamenti localizzati accettabili; misure
  (superfici collassabili, giunti strutturali, prevenzione di crolli significativi).

### Scope e limiti
- Non calcola le sollecitazioni né dimensiona/verifica gli elementi o i sistemi di protezione, non svolge i
  modelli teorici delle onde di pressione né gli studi di Categoria 3, non tratta le esplosioni esterne,
  l'incendio (§3.6.1) né gli urti (§3.6.3), non riproduce la Circolare 21/1/2019 n. 7. Non sostituisce il
  progettista strutturale.

### Note di sviluppo
- Completa la famiglia delle azioni eccezionali (§3.6) con `resistenza-fuoco-strutture-ntc` (§3.6.1) e
  `azioni-urto-eccezionali-ntc` (§3.6.3), condividendo la fonte GU. Validazione Livello 2 con ingegnere
  strutturista.
