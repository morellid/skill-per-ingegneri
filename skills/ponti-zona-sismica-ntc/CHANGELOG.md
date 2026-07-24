# CHANGELOG - ponti-zona-sismica-ntc

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-24

### Added (closes #460)
- Prima versione della skill di supporto al **progettista strutturale** per l'**inquadramento delle regole
  generali** dei **ponti in zona sismica** secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 7.9**,
  nell'area `strutture-geotecnica`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **NTC 2018 (DM 17 gennaio 2018)** - PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio
    2018 - SHA256 dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46 (doppio download
    riproducibile, stessa fonte delle altre skill NTC del repo).
  - Par. 7.9 (pagine PDF 269-271) estratto con `pdftotext -layout` e verificato sull'immagine (`pdftoppm -r
    150 -png`) per q0, νk, λ(α), la formula [7.9.1] e KR/[7.9.2]; trascritto verbatim in
    `references/fonti/ntc2018-par-7-9.md`.
- Estratto operativo `references/estratti/ponti-sismica-checklist.md`.
- Due task: `inquadra-criteri-fattore-comportamento.md` e `verifica-regolarita-requisiti-analisi.md`.
- Due esempi: criteri e scelta di q0 per una pila in c.a.; regolarità KR e ammissibilità dell'analisi statica
  lineare.

### Contenuto ancorato al testo
- Campo di applicazione (§7.9.1): ponti a pile e travate (continue/appoggiate), pile a fusto unico; q0 da Tab.
  7.3.II. Criteri (§7.9.2): non dissipativo (Cap. 4, no curvatura di prima plasticizzazione / snervamento) o
  dissipativo (meccanismo stabile, dissipazione limitata alle pile, inelastico flessionale, esclusa rottura per
  taglio); pali /1,5 con dettagli CD"B" per 10 diametri; perdita copriferri a 0,35%; impalcato, appoggi,
  fondazioni, spalle elastici. Fattore di comportamento (§7.9.2.1): q0 = 1,0 (non diss.); dissipativo q0 (Tab.
  7.3.II) con λ(α)=1 se α≥3 e (α/3)^0,5 se 3>α≥1 (α=L/H); c.a. duttili solo se νk=NEd/(Ac·fck)≤0,3 e comunque
  νk≤0,6, con q0(νk)=q0−[(νk/0,3)−1](q0−1) [7.9.1]; regolarità ri=q0·MEd,i/MRd,i, KR=1 se r̃=rmax/rmin<2 e
  KR=2/r̃ altrimenti [7.9.2]; ponti irregolari (obliquità >45°, raggio ridotto) q=1,5, fino a 3,5 con analisi non
  lineare. Modello/analisi (§7.9.3-7.9.4.1): eccentricità accidentale 0,03·dim. impalcato; moti rigidi per φ>20°
  o B/L>2,0; ΔM=dEd·NEd [7.9.3]; analisi statica lineare con massa efficace pila ≤ 1/5 massa impalcato ed
  eccentricità ≤ 5%.

### Scope e limiti
- Non esegue le verifiche di duttilità/resistenza delle pile e dei dispositivi né i metodi di analisi non lineare
  e i dettagli costruttivi (§§ 7.9.4-7.9.6); non calcola il q0 numerico (Tab. 7.3.II); non tratta i carichi da
  traffico statici (§§ 5.1.3/5.2.2) né il fattore q per gli edifici (§7.3.1). Non sostituisce il progettista.

### Note di sviluppo
- Distinta dalle skill sui carichi da traffico dei ponti (§5.1.3/§5.2.2) e da `fattore-comportamento-q-sismica-ntc`
  (§7.3.1). Condivide la fonte GU con le altre skill NTC. Validazione Livello 2 con ingegnere strutturista esperto
  di ponti.
