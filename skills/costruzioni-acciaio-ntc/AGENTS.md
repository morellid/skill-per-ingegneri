# AGENTS.md - costruzioni-acciaio-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **progettista strutturale** per l'**inquadramento della progettazione delle
costruzioni di acciaio** (caso **non sismico**) secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo
4.2**: materiali, classificazione delle sezioni, coefficienti parziali, resistenze di progetto e verifiche
agli stati limite ultimi (resistenza e stabilità delle membrature). Target: ingegneri strutturisti e
progettisti.

**E' una skill documentale per il tecnico**: fornisce i materiali (S235-S460, Tab. 4.2.I/II), le classi di
sezione (1-4), i coefficienti γM (Tab. 4.2.VII), la relazione Rd = Rk/γM e i criteri di verifica; **non
calcola** le resistenze, **non esegue** le verifiche e **non dimensiona** membrature e collegamenti.

## Nota sull'area e sulla complementarita'

Area **strutture-geotecnica**. Completa la famiglia "costruzioni di X" delle skill NTC insieme a
`costruzioni-muratura-ntc` (§4.5) e `costruzioni-legno-ntc` (§4.4); complementare alle altre skill NTC del
repo (`carichi-…`, `combinazioni-carico-ntc`, `fondazioni-pali-ntc`, `opere-sostegno-ntc`). Copre il
**materiale acciaio** e le sue verifiche **non sismiche** (§4.2). La progettazione **sismica** (§7.5), i
materiali (§11.3.4) e i **collegamenti** restano fuori scope. Condivide con le altre skill NTC la stessa
fonte (PDF GU del S.O. n. 8 alla G.U. n. 42/2018).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **ntc2018-par-4-2**: PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (DM 17
  gennaio 2018, NTC 2018), SHA256 `dda1e397...` (doppio download riproducibile, stessa fonte delle altre
  skill NTC). Par. 4.2 estratto con `pdftotext -layout` (pp. 91-103) e trascritto verbatim.

Trascrizione in `references/fonti/ntc2018-par-4-2.md`; estratto operativo in
`references/estratti/costruzioni-acciaio-checklist.md`.

## Punti chiave (verificati sul testo)

- **Materiali** (§4.2.1): gradi **S235-S460**; fyk/ftk dalle Tab. 4.2.I/II; esecuzione UNI EN 1090-2.
- **Classi di sezione** (§4.2.3.1): 1 duttili (Cθ ≥ 3), 2 compatte (Cθ ≥ 1,5), 3 semi-compatte, 4 snelle
  (sezione efficace); classe composta = valore più alto.
- **Analisi** (§4.2.3): metodi E/P/EP; primo ordine ammesso se α_cr ≥ 10 (elastica) / ≥ 15 (plastica).
- **Coefficienti** (§4.2.4.1.1, Tab. 4.2.VII): Rd = Rk/γM; **γM0 = 1,05** (sezioni), **γM1 = 1,05**
  (stabilità; 1,10 ponti), **γM2 = 1,25** (frattura sezioni tese forate).
- **Resistenze SLU** (§4.2.4.1.2): trazione min(A·fyk/γM0; 0,9·Anet·ftk/γM2); compressione A·fyk/γM0;
  flessione Wpl/Wel/Weff·fyk/γM0; taglio Av·fyk/(√3·γM0).
- **Stabilità** (§4.2.4.1.3): Nb,Rd = χ·A·fyk/γM1; instabilità trascurabile se λ̄ < 0,2 o NEd < 0,04·Ncr;
  snellezza λ ≤ 200/250; svergolamento χLT (αLT 0,21/0,34/0,49/0,76).
- **Fatica** (§4.2.4.1.4): Δσd ≤ ΔσR/γMf; per gli edifici generalmente non necessaria.

## Convenzioni specifiche

### Cosa NON fare
- Non **calcolare** le resistenze di progetto né **eseguire** le verifiche (resistenza, stabilità); non
  **dimensionare** membrature e collegamenti.
- Non **riprodurre** le **Tab. 4.2.III-V** (rapporti b/t di classificazione) né la **Tab. 4.2.VIII** (curve
  di instabilità): nel PDF sono figure → rinvio a norma/EC3. Non riprodurre i materiali del **§11.3.4** né
  gli **Eurocodici** (UNI EN 1993).
- Non **trattare** la **progettazione sismica** (§7.5); non **riprodurre** la **Circolare 21/1/2019 n. 7**.

### Cosa fare
- Fornire i materiali (gradi, fyk/ftk), le classi di sezione, i coefficienti γM, la relazione Rd = Rk/γM, le
  formule delle resistenze SLU e i criteri delle verifiche di stabilità, sempre con rinvio al paragrafo NTC.

## Aggiornamento delle fonti

NTC: se il PDF GU cambia (nuova edizione/errata) riscaricare, ricalcolare l'hash con doppio download e
riestrarre/ritrascrivere il par. 4.2. Verificare che le Tab. 4.2.I/II, 4.2.VII e i coefficienti (γM0/M1/M2,
Cθ, α_cr, soglie di λ̄, limiti di snellezza) non siano stati modificati.

## Validatori

- Non ancora assegnato (Livello 2 con ingegnere strutturista).

## Stato attuale

- Versione: 0.1.0-alpha (closes #384)
- Task files: 2 (`inquadra-classe-sezione-resistenze-acciaio.md`, `inquadra-stabilita-analisi-acciaio.md`)
- Esempi: 2 (materiale/classe/γM e Mc,Rd per una trave inflessa; trazione con fori e stabilità di un'asta
  compressa)
