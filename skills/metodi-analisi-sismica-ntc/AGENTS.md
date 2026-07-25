# AGENTS.md - metodi-analisi-sismica-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **progettista strutturale** per la **scelta e l'impostazione del metodo di analisi sismica**
secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafi 7.3.2, 7.3.3 e 7.3.4** (Cap. 7 «Progettazione per azioni
sismiche»): scelta dinamica/statica (§7.3.2), analisi lineare dinamica/modale (§7.3.3.1), analisi lineare statica/forze
laterali (§7.3.3.2), valutazione degli spostamenti (§7.3.3.3), analisi non lineare dinamica e statica/pushover (§7.3.4).

**È una skill documentale per il tecnico**: inquadra la scelta del metodo e le sue condizioni di applicabilità; **non**
esegue l'analisi né le verifiche.

## Nota sull'area e sulla complementarita'

Area **strutture-geotecnica**. Copre i **metodi di analisi sismica** (§7.3.2-7.3.4, Cap. 7). È **distinta** da:
- `fattore-comportamento-q-sismica-ntc` (§7.3.1, scelta lineare/non lineare e fattore q);
- `periodo-proprio-t1-ntc` (§7.3.3.2, solo la formula code-driven di T1 = 2√d);
- `criteri-modellazione-sismica-ntc` (§7.2.6, criteri di modellazione);
- `combinazione-componenti-sismiche-ntc` (§7.3.5, combinazione delle componenti);
- `spostamenti-interpiano-sld-ntc` (§7.3.6.1, verifiche SLD).
Questa skill è il tassello dei **metodi di analisi** (§7.3.2-7.3.4). Condivide la fonte GU con le altre skill NTC.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **ntc2018-par-7-3-2-7-3-4**: PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (DM 17 gennaio
  2018, NTC 2018), SHA256 `dda1e397...` (doppio download riproducibile, stessa fonte delle altre skill NTC).
  Parr. 7.3.2-7.3.4 (pagine PDF 222-224) estratti con `pdftotext -layout`; tutti i valori numerici e le formule
  (masse ≥85%, T1≤2,5TC, Fh/Fi/λ, μd, θ, 75%/1,3TC/6 modi) verificati sull'immagine (`pdftoppm -r 150`) delle pagine
  PDF 222/223/224.

Trascrizione in `references/fonti/ntc2018-par-7-3-2-7-3-4.md`; estratto operativo in
`references/estratti/metodi-analisi-checklist.md`.

## Punti chiave (verificati sul testo/immagine)

- **§7.3.2**: metodo di riferimento = **analisi modale con spettro** (lineare dinamica); **lineare statica** solo se la
  risposta non dipende dai modi superiori; non lineare dinamica/statica.
- **§7.3.3.1**: modi con **massa > 5%**, totale **≥ 85%**; combinazione **CQC** [7.3.4]; eccentricità accidentale.
- **§7.3.3.2**: applicabile se **T1 ≤ 2,5·TC** (o TD) e **regolare in altezza**; **Fh = Sd(T1)·W·λ/g**; **Fi =
  Fh·zi·Wi/Σ(zj·Wj)** [7.3.7]; **λ = 0,85** (T1<2TC, ≥3 orizzontamenti) o **1,0**; T1 = 2√d [7.3.6] (≤40 m).
- **§7.3.3.3**: **dE = μd·dEe** [7.3.8]; μd [7.3.9] ≤ **5q−4**; **SLC = 1,25·SLV**; **θ (P-Δ)** ≤ 0,3.
- **§7.3.4.2** (pushover): curva **Fb–dc**, punto di controllo al centro di massa dell'ultimo livello, **≥ 2
  distribuzioni** (Gruppo 1 **≥ 75%** / modale se **T1 > 1,3·TC**; Gruppo 2 uniforme/adattiva/multimodale **≥ 6 modi**).

## Convenzioni specifiche

### Cosa NON fare
- Non **eseguire** l'analisi (modale, statica, pushover, time-history) né le **verifiche**; non dimensionare.
- Non trattare il **fattore q** (§7.3.1), i **criteri di modellazione** (§7.2.6) né la **combinazione delle
  componenti** (§7.3.5): rinvia alle skill dedicate.
- Non inventare valori/formule: ogni numero deve essere rintracciabile in
  `references/fonti/ntc2018-par-7-3-2-7-3-4.md`.

### Cosa fare
- Fornire la scelta del metodo e le condizioni di applicabilità (statica lineare vs modale vs pushover), le
  distribuzioni della pushover e i requisiti (masse partecipanti, T1, λ, distribuzioni), sempre con rinvio al
  sotto-paragrafo/formula NTC.

## Aggiornamento delle fonti

NTC: se il PDF GU cambia (nuova edizione/errata) riscaricare, ricalcolare l'hash con doppio download e riestrarre
i parr. 7.3.2-7.3.4. Verificare sull'immagine i valori (>5%/≥85%; T1≤2,5TC; λ 0,85/1,0; μd≤5q−4; SLC 1,25; θ≤0,3;
pushover 75%/85%/1,3TC/6 modi).

## Validatori

- Non ancora assegnato (Livello 2 con ingegnere strutturista esperto di analisi sismica).

## Stato attuale

- Versione: 0.1.0-alpha (closes #476)
- Task files: 2 (`scegli-metodo-e-analisi-lineare.md`, `applica-analisi-non-lineare.md`)
- Esempi: 2 (verifica di applicabilità dell'analisi lineare statica; impostazione delle distribuzioni di forze per la
  pushover)
