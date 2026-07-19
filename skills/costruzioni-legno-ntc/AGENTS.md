# AGENTS.md - costruzioni-legno-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **progettista strutturale** per l'**inquadramento della progettazione delle
costruzioni di legno** (caso **non sismico**) secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo
4.4**: classi di durata del carico e classi di servizio, resistenze di progetto con kmod e γM,
deformabilità (kdef) e stati limite di esercizio, verifiche agli stati limite ultimi (resistenza e
stabilità), collegamenti e robustezza. Target: ingegneri strutturisti e progettisti.

**E' una skill documentale per il tecnico**: fornisce le classi (Tab. 4.4.I/4.4.II), i coefficienti γM
(Tab. 4.4.III), kmod (Tab. 4.4.IV) e kdef (Tab. 4.4.V), la relazione Xd = kmod·Xk/γM e i criteri di
verifica; **non calcola** le resistenze, **non esegue** le verifiche e **non dimensiona** elementi e
collegamenti.

## Nota sull'area e sulla complementarita'

Area **strutture-geotecnica**. Complementare, non sovrapposta, a `costruzioni-muratura-ntc` (§4.5) e alle
altre skill NTC del repo (`carichi-…`, `combinazioni-carico-ntc`, `fondazioni-pali-ntc`,
`opere-sostegno-ntc`): questa copre il **materiale legno** e le sue verifiche **non sismiche** (§4.4). La
progettazione **sismica** delle strutture di legno (§7.7) e le proprietà dei materiali (§11.7) restano
fuori scope. Condivide con le altre skill NTC la stessa fonte (PDF GU del S.O. n. 8 alla G.U. n. 42/2018).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **ntc2018-par-4-4**: PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (DM 17
  gennaio 2018, NTC 2018), SHA256 `dda1e397...` (doppio download riproducibile, stessa fonte delle altre
  skill NTC). Par. 4.4 estratto con `pdftotext -layout` (pp. 132-141) e trascritto verbatim.

Trascrizione in `references/fonti/ntc2018-par-4-4.md`; estratto operativo in
`references/estratti/costruzioni-legno-checklist.md`.

## Punti chiave (verificati sul testo)

- **Classi di durata** (§4.4.4, Tab. 4.4.I): permanente/lunga/media/breve/istantaneo.
- **Classi di servizio** (§4.4.5, Tab. 4.4.II): 1 (UR ≤ 65%), 2 (UR > 85% poche settimane/anno), 3
  (umidità superiore).
- **Resistenza di progetto** (§4.4.6): **Xd = kmod·Xk/γM**; kmod di combinazione = azione di minor durata;
  γM colonna A (massiccio 1,50, lamellare 1,45, LVL/OSB 1,40, unioni 1,50) o B ridotta; eccezionali 1,00.
- **SLE** (§4.4.7): fattore **1/(1+kdef)** (Tab. 4.4.V); frecce istantanea < L/300, finale < L/200.
- **SLU resistenza** (§4.4.8.1): flessione km = 0,7 (rettangolari) / 1,0 (altre); trazione, compressione,
  taglio, torsione (ksh).
- **SLU stabilità** (§4.4.8.2): kcrit,m = 1 se λrel,m ≤ 0,75; kcrit,c = 1 se λrel,c ≤ 0,3; βc = 0,2
  (massiccio) / 0,1 (lamellare); moduli al frattile 5%.
- **Esecuzione** (§4.4.15): scostamento ≤ 1/500 (lamellare) / 1/300 (massiccio).

## Convenzioni specifiche

### Cosa NON fare
- Non **calcolare** le resistenze di progetto né **eseguire** le verifiche (resistenza, stabilità, frecce);
  non **dimensionare** elementi e collegamenti.
- Non **riprodurre** le proprietà dei materiali (fk, moduli elastici, kh) del **§11.7** né gli **Eurocodici**
  (UNI EN 1995).
- Non **trattare** la **progettazione sismica** (§7.7); non **riprodurre** la **Circolare 21/1/2019 n. 7**.

### Cosa fare
- Fornire le classi di durata e di servizio, i coefficienti γM/kmod/kdef, la relazione Xd = kmod·Xk/γM, i
  criteri delle verifiche SLU (km, kcrit, βc) e SLE (frecce), sempre con rinvio al paragrafo NTC.

## Aggiornamento delle fonti

NTC: se il PDF GU cambia (nuova edizione/errata) riscaricare, ricalcolare l'hash con doppio download e
riestrarre/ritrascrivere il par. 4.4. Verificare che le Tab. 4.4.I-4.4.V e i coefficienti (γM, kmod, kdef,
km, βc, ksh, soglie di λrel) non siano stati modificati.

## Validatori

- Non ancora assegnato (Livello 2 con ingegnere strutturista).

## Stato attuale

- Versione: 0.1.0-alpha (closes #382)
- Task files: 2 (`inquadra-resistenze-progetto-legno.md`, `inquadra-verifiche-slu-sle-legno.md`)
- Esempi: 2 (kmod e γM per una trave di lamellare in copertura; frecce limite SLE e kdef per un solaio in
  legno massiccio)
