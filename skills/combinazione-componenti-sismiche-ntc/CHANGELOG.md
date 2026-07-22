# CHANGELOG - combinazione-componenti-sismiche-ntc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-22

### Added (closes #425)
- Prima versione della skill di supporto al **progettista strutturale** per l'**inquadramento della combinazione
  delle componenti dell'azione sismica** e della risposta alla variabilità spaziale del moto secondo le **NTC
  2018** (DM 17 gennaio 2018), **paragrafo 7.3.5**, nell'area `strutture-geotecnica`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **NTC 2018 (DM 17 gennaio 2018)** - PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio
    2018 - SHA256: dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46 (doppio download
    riproducibile, stessa fonte delle altre skill NTC del repo).
  - Par. 7.3.5 estratto con `pdftotext -layout` (p. GU 221) e trascritto verbatim in
    `references/fonti/ntc2018-par-7-3-5.md`. La formula [7.3.10] e' stata verificata sull'immagine renderizzata
    della pagina PDF 225 (pdftoppm), perche' pdftotext perde i segni "+".
- Estratto operativo `references/estratti/combinazione-componenti-checklist.md`.
- Due task: `inquadra-combinazione-componenti.md` e `inquadra-analisi-integrazione-passo-variabilita.md`.
- Due esempi: combinazione delle componenti con permutazione circolare (edificio senza componente verticale);
  numero di storie temporali (3 -> valori piu' sfavorevoli, 7 -> media) nell'integrazione al passo.

### Contenuto ancorato al testo
- Combinazione delle tre componenti (§7.3.5, analisi dinamica o statica, lineare o non lineare): 1,00 x Ex + 0,30
  x Ey + 0,30 x Ez [7.3.10]; effetti piu' gravosi dal confronto tra le tre combinazioni ottenute permutando
  circolarmente i coefficienti moltiplicativi (coefficiente unitario assegnato a turno a ciascuna componente,
  0,30 alle altre due). Componente verticale: tenuta in conto solo nei casi previsti al §7.2.2. Variabilità
  spaziale del moto: la risposta va combinata con gli effetti pseudo-statici degli spostamenti relativi solo nei
  casi del §3.2.4.1, con la radice quadrata della somma dei quadrati (SRSS), salvo §7.2.2 per gli appoggi mobili.
  Analisi dinamica con integrazione al passo: due componenti orizzontali applicate simultaneamente (piu' la
  verticale ove necessario); con almeno 3 storie temporali si usano i valori piu' sfavorevoli, con almeno 7
  diverse storie temporali gli effetti sono la media dei valori piu' sfavorevoli; per la variabilità spaziale,
  storie temporali differenziate ma coerenti per ciascun vincolo oppure moto sincrono con effetti pseudo-statici
  (§3.2.4).

### Scope e limiti
- Non esegue l'analisi ne' calcola gli effetti, non genera/seleziona le storie temporali, non tratta i casi che
  richiedono la componente verticale (§7.2.2) ne' la variabilità spaziale del moto (§3.2.4), non riproduce la
  Circolare 21/1/2019 n. 7. Non sostituisce il progettista.

### Note di sviluppo
- Complementa `combinazioni-carico-ntc` (§2.5.3), `criteri-modellazione-sismica-ntc` (§7.2.6),
  `regolarita-strutturale-sismica-ntc` (§7.2.1), `spostamenti-interpiano-sld-ntc` (§7.3.6.1) e
  `spettro-risposta-ntc` (§3.2), condividendo la stessa fonte GU. Validazione Livello 2 con ingegnere
  strutturista.
