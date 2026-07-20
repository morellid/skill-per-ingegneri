# AGENTS.md - costruzioni-calcestruzzo-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **progettista strutturale** per l'**inquadramento della progettazione delle
costruzioni di calcestruzzo** (c.a., c.a.p., non armato; caso **non sismico**) secondo le **NTC 2018** (DM
17 gennaio 2018), **paragrafo 4.1**: classi di resistenza, resistenze di progetto e coefficienti parziali,
diagrammi di calcolo, verifiche agli stati limite ultimi e di esercizio. Target: ingegneri strutturisti e
progettisti.

**E' una skill documentale per il tecnico**: fornisce le classi (Tab. 4.1.I), i coefficienti γc/γs, le
resistenze di progetto (fcd, fctd, fyd), i diagrammi di calcolo e i criteri di verifica; **non calcola** le
resistenze, **non esegue** le verifiche e **non dimensiona** né **arma** gli elementi.

## Nota sull'area e sulla complementarita'

Area **strutture-geotecnica**. Completa la famiglia "costruzioni di X" delle skill NTC insieme a
`costruzioni-acciaio-ntc` (§4.2), `costruzioni-legno-ntc` (§4.4) e `costruzioni-muratura-ntc` (§4.5).
**Complementare** (inquadramento documentale) al code-driven `predimensionamento-flessione-ca-ntc`, che
esegue il predimensionamento a flessione: questa skill copre l'intero quadro documentale del §4.1
(materiali, coefficienti, verifiche), l'altra fa il calcolo di predimensionamento a flessione. La
progettazione **sismica** (§7.4), i materiali (§11.2/11.3) e i calcestruzzi speciali restano fuori scope.
Condivide con le altre skill NTC la stessa fonte (PDF GU del S.O. n. 8 alla G.U. n. 42/2018).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **ntc2018-par-4-1**: PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (DM 17
  gennaio 2018, NTC 2018), SHA256 `dda1e397...` (doppio download riproducibile, stessa fonte delle altre
  skill NTC). Par. 4.1 estratto con `pdftotext -layout` (pp. 71-90) e trascritto verbatim.

Trascrizione in `references/fonti/ntc2018-par-4-1.md`; estratto operativo in
`references/estratti/costruzioni-calcestruzzo-checklist.md`.

## Punti chiave (verificati sul testo)

- **Classi** (Tab. 4.1.I): C8/10-C90/105; analisi con x/d ≤ 0,45 (fck ≤ 50) / 0,35 (fck > 50).
- **Resistenze di progetto** (§4.1.2.1.1): fcd = αcc·fck/γc (αcc = 0,85, γc = 1,5, → 1,4 controllata; 0,80·fcd
  elementi piani < 50 mm); fctd = fctk/γc; fyd = fyk/γs (γs = 1,15 sempre).
- **Diagrammi** (§4.1.2.1.2): parabola-rettangolo/triangolo-rettangolo/stress block; εc2 = 0,20%, εcu =
  0,35% (≤ C50/60).
- **SLU** (§4.1.2.3): pressoflessione, taglio (traliccio 1 ≤ ctgθ ≤ 2,5), torsione, punzonamento.
- **SLE** (§4.1.2.2): fessurazione (w1 = 0,2 / w2 = 0,3 / w3 = 0,4 mm); tensioni (σc ≤ 0,60·fck rara,
  σc ≤ 0,45·fck quasi permanente, σs ≤ 0,8·fyk).

## Convenzioni specifiche

### Cosa NON fare
- Non **calcolare** le resistenze di progetto né **eseguire** le verifiche (SLU/SLE); non **dimensionare**
  né **armare** gli elementi.
- Non **riprodurre** le proprietà dei materiali (fck, fctk, fyk, moduli) dei **§11.2/11.3** né gli
  **Eurocodici** (UNI EN 1992).
- Non **trattare** la **progettazione sismica** (§7.4) né i calcestruzzi speciali (leggeri §4.1.12,
  fibrorinforzati §11.2.12); non **riprodurre** la **Circolare 21/1/2019 n. 7**.
- Non **sovrapporsi** a `predimensionamento-flessione-ca-ntc` (calcolo di predimensionamento a flessione).

### Cosa fare
- Fornire le classi, i coefficienti γc/γs, le formule delle resistenze di progetto, i diagrammi di calcolo e
  i criteri delle verifiche SLU/SLE, sempre con rinvio al paragrafo NTC.

## Aggiornamento delle fonti

NTC: se il PDF GU cambia (nuova edizione/errata) riscaricare, ricalcolare l'hash con doppio download e
riestrarre/ritrascrivere il par. 4.1. Verificare che i coefficienti (γc, γs, αcc), le deformazioni
(εc2, εcu), i limiti (x/d, ctgθ, σc, σs, wk) non siano stati modificati.

## Validatori

- Non ancora assegnato (Livello 2 con ingegnere strutturista).

## Stato attuale

- Versione: 0.1.0-alpha (closes #390)
- Task files: 2 (`inquadra-resistenze-progetto-ca.md`, `inquadra-verifiche-slu-sle-ca.md`)
- Esempi: 2 (resistenze di progetto e coefficienti per una trave C25/30 B450C; verifiche SLE di tensione e
  fessurazione)
