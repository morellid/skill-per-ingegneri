# AGENTS.md - carichi-permanenti-sovraccarichi-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **progettista strutturale** per l'**analisi dei carichi**: **carichi permanenti**
(pesi propri strutturali e non strutturali) e **sovraccarichi variabili** (carichi imposti) per
**categoria d'uso** delle costruzioni civili e industriali, secondo le **NTC 2018** (DM 17 gennaio 2018),
**paragrafo 3.1**. Target: ingegneri strutturisti e progettisti.

**E' una skill documentale per il tecnico**: fornisce i valori tabellari (Tab. 3.1.I e 3.1.II), il carico
equivalente dei divisori e i coefficienti di riduzione; **non calcola** i carichi di progetto, **non
combina** le azioni e **non dimensiona** gli elementi.

## Nota sull'area e sulla complementarita'

Area **strutture-geotecnica**. Complementare, non sovrapposta, a `combinazioni-carico-ntc` (combinazioni
delle azioni SLU/SLE con i coefficienti ψ e γ) e `carichi-atmosferici-ntc` (vento §3.3 e neve §3.4). Questa
copre i **carichi permanenti e i sovraccarichi variabili** (§3.1): l'analisi dei carichi che precede la
combinazione. Condivide con le altre skill NTC la stessa fonte (PDF GU del S.O. n. 8 alla G.U. n. 42/2018).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **ntc2018-par-3-1**: PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (DM 17
  gennaio 2018, NTC 2018), SHA256 `dda1e397...` (doppio download riproducibile, stessa fonte delle altre
  skill NTC). Par. 3.1 estratto con `pdftotext -layout` (pp. 41-44) e trascritto verbatim.

Trascrizione in `references/fonti/ntc2018-par-3-1.md`; estratto operativo in
`references/estratti/carichi-sovraccarichi-checklist.md`.

## Punti chiave (verificati sul testo)

- **Pesi propri G1** (§3.1.2): Tab. 3.1.I (c.a. 25,0 kN/m³, acciaio 78,5, ecc.).
- **Divisori g2** (§3.1.3): 0,40/0,80/1,20/1,60/2,00 kN/m² per G2 fino a 5,00 kN/m; oltre, posizionamento
  effettivo.
- **Sovraccarichi** (§3.1.4, Tab. 3.1.II): categorie A-K (residenziale, uffici B1/B2, affollamento C1-C5,
  commerciale D, magazzini/industriale E, rimesse/parcheggi F/G, coperture H/I/K, scale/balconi); carichi
  atipici caso per caso.
- **Riduzioni** (§3.1.4.1): α_A = (5/7)·ψ0 + 10/A ≤ 1,0 (C,D ≥ 0,6); α_n = (2 + (n−2)·ψ0)/n; non
  combinabili.
- **Verifiche locali**: Qk (impronte di carico) e Hk (a 1,20 m, parapetti al bordo superiore), non
  contemporanei/combinati con le verifiche d'insieme (§3.1.4.2-3).

## Convenzioni specifiche

### Cosa NON fare
- Non **calcolare** i carichi di progetto né **combinare** le azioni (skill `combinazioni-carico-ntc`);
  non **dimensionare** gli elementi.
- Non **riprodurre** la **Tab. 2.5.I** (coefficienti ψ) né la Circolare 7/2019.
- Non trattare i **carichi da ponte** (cap. 5), l'**azione sismica** (§3.2) né il **vento/neve**
  (§3.3/3.4, skill `carichi-atmosferici-ntc`).

### Cosa fare
- Fornire i valori dei pesi propri (Tab. 3.1.I), il carico equivalente g2 dei divisori, i sovraccarichi per
  categoria (Tab. 3.1.II) e i coefficienti di riduzione α_A/α_n con i loro vincoli.

## Aggiornamento delle fonti

NTC: se il PDF GU cambia (nuova edizione/errata) riscaricare, ricalcolare l'hash con doppio download e
riestrarre/ritrascrivere il par. 3.1. Verificare che le Tab. 3.1.I/3.1.II e i coefficienti di riduzione
non siano stati modificati.

## Validatori

- Non ancora assegnato (Livello 2 con ingegnere strutturista).

## Stato attuale

- Versione: 0.1.0-alpha (closes #378)
- Task files: 2 (`inquadra-sovraccarichi-categoria.md`, `inquadra-permanenti-riduzioni.md`)
- Esempi: 2 (edificio a uso misto - sovraccarichi per categoria e parapetti; tramezzi come g2 e riduzioni
  α_A/α_n su trave e pilastro)
