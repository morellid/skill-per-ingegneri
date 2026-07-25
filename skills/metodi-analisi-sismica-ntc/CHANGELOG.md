# CHANGELOG - metodi-analisi-sismica-ntc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-25

### Added (closes #476)
- Prima versione della skill di supporto al **progettista strutturale** per la **scelta e l'impostazione del metodo di
  analisi sismica** secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafi 7.3.2, 7.3.3 e 7.3.4** (Cap. 7),
  nell'area `strutture-geotecnica`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **NTC 2018 (DM 17 gennaio 2018)** - PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio
    2018 - SHA256 dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46 (doppio download
    riproducibile, stessa fonte delle altre skill NTC del repo).
  - Parr. 7.3.2-7.3.4 (pagine PDF 222-224 = GU 218-220) estratti con `pdftotext -layout`; tutti i valori numerici e le
    formule (masse ≥85%, T1≤2,5TC, Fh/Fi/λ, μd, θ, 75%/1,3TC/6 modi) verificati sull'immagine (`pdftoppm -r 150 -png`)
    delle pagine PDF 222/223/224 e trascritti in `references/fonti/ntc2018-par-7-3-2-7-3-4.md`.
- Estratto operativo `references/estratti/metodi-analisi-checklist.md`.
- Due task: `scegli-metodo-e-analisi-lineare.md` e `applica-analisi-non-lineare.md`.
- Due esempi: verifica di applicabilità dell'analisi lineare statica; impostazione delle distribuzioni di forze per la
  pushover.

### Contenuto ancorato al testo
- Scelta (§7.3.2): metodo di riferimento analisi modale con spettro di risposta (analisi lineare dinamica); analisi
  lineare statica (forze laterali) solo se la risposta non dipende dai modi superiori; analisi non lineare dinamica
  (storie temporali) o statica (forze crescenti monotone). Lineare dinamica (§7.3.3.1): modi con massa partecipante >
  5%, totale ≥ 85%; combinazione CQC [7.3.4] con ρij [7.3.5a/b]; eccentricità accidentale. Lineare statica (§7.3.3.2):
  applicabile se T1 ≤ 2,5·TC (o TD) e regolare in altezza; ≤ 40 m, T1 = 2√d [7.3.6]; Fi = Fh·zi·Wi/Σ(zj·Wj) [7.3.7],
  Fh = Sd(T1)·W·λ/g, λ = 0,85 se T1 < 2·TC e ≥ 3 orizzontamenti, altrimenti 1,0. Spostamenti (§7.3.3.3): dE = ±μd·dEe
  [7.3.8], μd = q (T1≥TC) o 1+(q−1)·TC/T1 (T1<TC) [7.3.9], μd ≤ 5q−4, SLC = 1,25·SLV; θ (P-Δ) [7.3.3] trascurabile se
  θ<0,1, incremento 1/(1−θ) se 0,1–0,2, analisi non lineare se 0,2–0,3, θ ≤ 0,3. Non lineare (§7.3.4): dinamica con
  integrazione al passo e confronto con modale, obbligatoria per isolamento non lineare (§7.10.5.2); statica/pushover
  con sistema equivalente, forze risultante Fb, punto di controllo al centro di massa dell'ultimo livello, curva di
  capacità Fb–dc, almeno 2 distribuzioni (Gruppo 1 modo fondamentale ≥ 75% o distribuzione modale con modi ≥ 85%
  obbligatoria se T1 > 1,3·TC; Gruppo 2 uniforme, adattiva, multimodale ≥ 6 modi).

### Scope e limiti
- Non esegue l'analisi né le verifiche; non tratta il fattore q (§7.3.1), la formula di T1 (§7.3.3.2), i criteri di
  modellazione (§7.2.6) né la combinazione delle componenti (§7.3.5). Non sostituisce il progettista né la Circolare
  2019.

### Note di sviluppo
- Distinta da `fattore-comportamento-q-sismica-ntc` (§7.3.1), `periodo-proprio-t1-ntc` (§7.3.3.2),
  `criteri-modellazione-sismica-ntc` (§7.2.6) e `combinazione-componenti-sismiche-ntc` (§7.3.5). Condivide la fonte GU
  con le altre skill NTC. Validazione Livello 2 con ingegnere strutturista esperto di analisi sismica.
