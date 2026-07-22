# CHANGELOG - elementi-non-strutturali-sismica-ntc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-22

### Added (closes #427)
- Prima versione della skill di supporto al **progettista strutturale** per l'**inquadramento della progettazione
  sismica degli elementi strutturali secondari, degli elementi costruttivi non strutturali e degli impianti**
  secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafi 7.2.3 e 7.2.4**, nell'area `strutture-geotecnica`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **NTC 2018 (DM 17 gennaio 2018)** - PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio
    2018 - SHA256: dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46 (doppio download
    riproducibile, stessa fonte delle altre skill NTC del repo).
  - Par. 7.2.3-7.2.4 estratti con `pdftotext -layout` (p. GU 212) e trascritti verbatim in
    `references/fonti/ntc2018-par-7-2-3-7-2-4.md`. La formula [7.2.1] e le costanti (15%, 2, 1,4, 30%, 10%) sono
    state verificate sull'immagine renderizzata della pagina PDF 216 (pdftoppm), perche' pdftotext perde gli
    operatori =, x, /.
- Estratto operativo `references/estratti/elementi-non-strutturali-checklist.md`.
- Due task: `inquadra-forza-elementi-non-strutturali.md` e `inquadra-elementi-secondari-impianti.md`.
- Due esempi: forza Fa su una tamponatura (con irregolarita' in pianta -> eccentricita' x2); elementi secondari
  con il limite del 15% e un impianto pesante oltre la soglia del 30%.

### Contenuto ancorato al testo
- Elementi secondari (§7.2.3): rigidezza/resistenza alle azioni orizzontali trascurabili; progettati per i soli
  carichi verticali e per seguire gli spostamenti allo SLC (§7.3.3.3/§7.3.4); la scelta non puo' trasformare una
  struttura irregolare in regolare (§7.2.1); contributo totale a rigidezza/resistenza orizzontale <= 15%
  dell'analogo contributo degli elementi primari. Elementi costruttivi non strutturali (§7.2.3): capacita' >
  domanda sismica per ogni SL (§7.3.6); responsabilita' progettista struttura/DL/fornitore-installatore;
  irregolarita' in pianta -> eccentricita' accidentale x2 (§7.2.6); in altezza -> domanda sugli elementi
  verticali x1,4; forza Fa = (Sa x Wa)/qa [7.2.1] (Sa adimensionalizzata §3.2.1, Wa peso, qa fattore di
  comportamento; Sa e qa da documenti di comprovata validita'). Impianti (§7.2.4): capacita' > domanda (§7.3.6);
  responsabilita' produttore/installatore/progettista strutturale; studio specifico se l'impianto eccede il 30%
  del carico permanente del campo di solaio (o del pannello) o il 10% del carico permanente totale della
  struttura.

### Scope e limiti
- Non calcola Fa ne' esegue le verifiche, non determina Sa e qa, non calcola la domanda/gli spostamenti (§7.3) ne'
  lo spettro (§3.2), non riproduce la Circolare 21/1/2019 n. 7. Non sostituisce il progettista.

### Note di sviluppo
- Complementa `criteri-modellazione-sismica-ntc` (§7.2.6), `regolarita-strutturale-sismica-ntc` (§7.2.1),
  `spostamenti-interpiano-sld-ntc` (§7.3.6.1) e `spettro-risposta-ntc` (§3.2), condividendo la stessa fonte GU.
  Validazione Livello 2 con ingegnere strutturista.
