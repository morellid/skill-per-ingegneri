# CHANGELOG - terre-rocce-scavo-dpr120

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-16

### Added (closes #259)
- Prima versione della skill di supporto alla **gestione delle terre e rocce da scavo**
  (qualificazione come sottoprodotto/escluse dai rifiuti/rifiuto, cantieri piccoli e grandi,
  dichiarazione di utilizzo), ai sensi del **D.P.R. 13 giugno 2017, n. 120**, nell'area
  `ambiente-territorio-mobilita`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.P.R. 13 giugno 2017, n. 120** - indice Normattiva pinnato `!vig=2026-07-16`
    SHA256: 67cee768741ac257c39fe8955d9428211b3d3c9cb28f15d2610d9bf0b4ef9336 (codice 17G00135).
    Artt. 1, 2, 4, 20, 21, 24 (testo vigente) via `caricaArticolo`, trascritti verbatim in
    `references/fonti/dpr-120-2017.md`.
- Estratto operativo `references/estratti/terre-rocce-scavo-checklist.md`.
- Due task: `qualifica-terre-scavo.md` e `gestisci-dichiarazione-piccoli-cantieri.md`.
- Due esempi: piccolo cantiere (dichiarazione di utilizzo, allegato 6, 15 gg, Comune/ARPA);
  utilizzo nel sito di produzione (escluse dai rifiuti, art. 24).

### Contenuto ancorato al testo
- Qualificazione come sottoprodotto (art. 4, ex art. 184-bis D.Lgs. 152/2006); definizioni e
  dimensione del cantiere (art. 2: piccole <= 6.000 mc / grandi); requisiti ambientali - CSC
  (art. 20); dichiarazione di utilizzo dei piccoli cantieri (art. 21: allegato 6, 15 gg prima a
  Comune + ARPA, utilizzo entro 1 anno, DAU); utilizzo nel sito di produzione escluse dai rifiuti
  (art. 24, ex art. 185 D.Lgs. 152/2006).

### Scope e limiti
- Non riproduce i **valori CSC** (Tab. 1, Allegato 5, Parte IV, D.Lgs. 152/2006) ne' gli
  **Allegati tecnici** del DPR (campionamento/analisi, modulistica). Non esegue campionamento/
  analisi, non redige piano/dichiarazione, non sostituisce l'ARPA. Per i grandi cantieri il piano
  di utilizzo (artt. 9 e ss.) e' solo richiamato. Complementare a `trasporto-rifiuti-fir-dlgs152`
  e `bonifica-siti-contaminati-dlgs152`.

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del D.P.R. 120/2017 pinnato (nuovo hash) e
  rileggere gli articoli; verificare le CSC (D.Lgs. 152/2006) e gli allegati.
- Validazione Livello 2 con professionista ambientale / ARPA.
