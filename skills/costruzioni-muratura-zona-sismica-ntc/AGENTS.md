# AGENTS.md - costruzioni-muratura-zona-sismica-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **progettista strutturale** per l'**inquadramento delle regole generali** delle
costruzioni di muratura in zona sismica secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 7.8.1**:
premessa/CD"B", requisiti dei materiali, modalità costruttive e fattori di comportamento (αu/α1), criteri di
progetto e requisiti geometrici (Tab. 7.8.I). Target: ingegneri strutturisti e progettisti di edifici in
muratura.

**È una skill documentale per il tecnico**: fornisce i requisiti dei materiali, i valori di αu/α1 e i requisiti
geometrici delle pareti; **non** esegue le verifiche (pressoflessione/taglio dei pannelli) né progetta
l'armatura.

## Nota sull'area e sulla complementarita'

Area **strutture-geotecnica**. Copre le **regole generali per la muratura in zona sismica** (§7.8.1). È
**distinta** da `costruzioni-muratura-ntc` (§4.5, materiali/resistenze/verifiche **statiche**) e da
`fattore-comportamento-q-sismica-ntc` (§7.3.1, framework **generale** del fattore q): il §7.8.1 aggiunge i
requisiti sismici specifici della muratura (materiali rafforzati per agS > 0,075g, αu/α1, Tab. 7.8.I). Condivide
con le altre skill NTC la stessa fonte (PDF GU del S.O. n. 8 alla G.U. n. 42/2018). Restano fuori scope: le
verifiche dei pannelli (§§ 7.8.2-7.8.4), i metodi di analisi (§7.8.1.5), i dettagli/cordoli e la muratura armata
di dettaglio (§§ 7.8.1.7-7.8.5).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **ntc2018-par-7-8-1**: PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (DM 17 gennaio
  2018, NTC 2018), SHA256 `dda1e397...` (doppio download riproducibile, stessa fonte delle altre skill NTC).
  Par. 7.8.1 (pagine PDF 261-262) estratto con `pdftotext -layout` e verificato sull'immagine (`pdftoppm -r
  150`) per valori dei materiali, αu/α1 e Tab. 7.8.I.

Trascrizione in `references/fonti/ntc2018-par-7-8-1.md`; estratto operativo in
`references/estratti/muratura-sismica-checklist.md`.

## Punti chiave (verificati sul testo/immagine)

- **Premessa** (§7.8.1.1): muratura moderatamente dissipativa → **CD"B"**; coeff. parziali Cap. 4 **-20%** e ≥ 2.
- **Materiali** (§7.8.1.2, per agS > 0,075g): vuoti ≤ 45%; **f_bk ≥ 5 MPa** (o f_b ≥ 6); **f_bk⊥ ≥ 1,5 MPa**;
  malta ≥ 5 MPa; limiti giunti sottili/secco.
- **αu/α1** (§7.8.1.3): ordinaria 1,7; armata 1,5 (1,3 capacity design); confinata 1,6 (1,3 capacity design);
  ≤ 2,5.
- **Tab. 7.8.I** (§7.8.1.4): t_min / (h0/t)max / (l/h')min — ordinaria pietra 300/10/0,5; ordinaria artif.
  240/12/0,4; armata 240/15/qualsiasi; confinata 240/15/0,3; solai ≤ 5 m.

## Convenzioni specifiche

### Cosa NON fare
- Non **eseguire** le verifiche dei pannelli murari (pressoflessione/taglio, §§ 7.8.2-7.8.4) né i metodi di
  analisi (§7.8.1.5).
- Non **progettare** l'armatura né i dettagli/cordoli; non trattare i requisiti statici (§4.5, → skill dedicata)
  né il framework del fattore q (§7.3.1, → skill dedicata).

### Cosa fare
- Fornire premessa/CD"B", requisiti dei materiali, αu/α1 e requisiti geometrici (Tab. 7.8.I), sempre con rinvio
  al paragrafo/tabella NTC.

## Aggiornamento delle fonti

NTC: se il PDF GU cambia (nuova edizione/errata) riscaricare, ricalcolare l'hash con doppio download e
riestrarre il par. 7.8.1. Verificare sull'immagine i valori (fbk 5/1,5, malta 5, vuoti 45%, αu/α1 1,7/1,5/1,6)
e la Tab. 7.8.I (300/240/200/150 mm; 10/12/15/20; 0,5/0,4/0,3).

## Validatori

- Non ancora assegnato (Livello 2 con ingegnere strutturista esperto di muratura).

## Stato attuale

- Versione: 0.1.0-alpha (closes #454)
- Task files: 2 (`inquadra-materiali-fattori-comportamento.md`, `verifica-requisiti-geometrici-pareti.md`)
- Esempi: 2 (requisiti dei materiali e scelta di αu/α1 per una muratura ordinaria; verifica dei requisiti
  geometrici di una parete con la Tab. 7.8.I)
