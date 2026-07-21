# AGENTS.md - spostamenti-interpiano-sld-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **progettista strutturale** per l'**inquadramento della verifica di deformabilita' allo
stato limite di danno (SLD)** - i limiti di spostamento di interpiano - degli elementi strutturali secondo le
**NTC 2018** (DM 17 gennaio 2018), **paragrafi 7.3.6 e 7.3.6.1** (verifiche di rigidezza RIG). Target: ingegneri
strutturisti.

**E' una skill documentale per il tecnico**: fornisce il quadro delle verifiche (stato limite per classe d'uso),
i sei limiti di spostamento di interpiano e le regole di applicazione; **non calcola** gli spostamenti, **non
esegue** l'analisi e **non determina** q.

## Nota sull'area e sulla complementarita'

Area **strutture-geotecnica**. **Complementa** `regolarita-strutturale-sismica-ntc` (§7.2.1/7.3.1, KR e metodo di
analisi), `periodo-proprio-t1-ntc` (§7.3.3.2, stima di T1) e `spettro-risposta-ntc` (§3.2, spettro di progetto).
E' **distinta**: nessuna di queste tratta i limiti di drift allo SLD del §7.3.6.1. Condivide con le altre skill
NTC la stessa fonte (PDF GU del S.O. n. 8 alla G.U. n. 42/2018). Restano fuori scope le verifiche di resistenza
(RES) e duttilita' (DUT), gli elementi non strutturali (§7.3.6.2) e gli impianti (§7.3.6.3).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **ntc2018-par-7-3-6-1**: PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (DM 17 gennaio
  2018, NTC 2018), SHA256 `dda1e397...` (doppio download riproducibile, stessa fonte delle altre skill NTC).
  Par. 7.3.6 e 7.3.6.1 estratti con `pdftotext -layout` (pp. GU 221-222) e trascritti verbatim; i sei limiti e
  gli operatori (<= per a-d, < per e) verificati anche sull'immagine renderizzata della pagina PDF 226 (pdftoppm).

Trascrizione in `references/fonti/ntc2018-par-7-3-6-1-sld.md`; estratto operativo in
`references/estratti/spostamenti-interpiano-checklist.md`.

## Punti chiave (verificati sul testo)

- **Quadro** (§7.3.6, Tab. 7.3.III): verifica di rigidezza (RIG) allo **SLD** per le CU I e II, allo **SLO** per
  le CU III e IV.
- **Limiti di spostamento di interpiano** (§7.3.6.1): q*dr <= 0,0050 h (fragili), <= 0,0075 h (duttili), <= drp e
  <= 0,0100 h (progettate per non danneggiarsi), <= 0,0020 h (muratura ordinaria), <= 0,0030 h (armata), < 0,0025
  h (confinata). dr = differenza spostamenti solaio sup/inf (analisi §7.3.3.3 o §7.3.4), modello senza
  tamponature; h = altezza di piano; q = fattore di comportamento.
- **Regole**: CU III e IV (SLO) -> limiti ai 2/3; coesistenza -> limite piu' restrittivo; dr > 0,005 h (caso b)
  -> verifiche estese a tamponature, tramezzature e impianti.

## Convenzioni specifiche

### Cosa NON fare
- Non **calcolare** gli spostamenti ne' **eseguire** l'analisi (§7.3.3.3/§7.3.4); non **determinare** q.
- Non **confondere** l'operatore: casi a-d usano <=, il caso e (muratura confinata) usa < (strettamente minore).
- Non **trattare** le verifiche RES/DUT, gli elementi non strutturali (§7.3.6.2) ne' gli impianti (§7.3.6.3).

### Cosa fare
- Fornire il quadro (stato limite per CU), i sei limiti e le regole di applicazione, sempre con rinvio al
  paragrafo/formula NTC.

## Aggiornamento delle fonti

NTC: se il PDF GU cambia (nuova edizione/errata) riscaricare, ricalcolare l'hash con doppio download e
riestrarre/ritrascrivere i par. 7.3.6/7.3.6.1. Verificare i sei limiti (0,0050/0,0075/0,0100/0,0020/0,0030/0,0025
h) e gli operatori (<= per a-d, < per e).

## Validatori

- Non ancora assegnato (Livello 2 con ingegnere strutturista).

## Stato attuale

- Versione: 0.1.0-alpha (closes #421)
- Task files: 2 (`inquadra-limiti-spostamento-interpiano.md`, `inquadra-classe-uso-stato-limite.md`)
- Esempi: 2 (telaio in c.a. con tamponature fragili CU II -> 0,0050 h; edificio strategico CU IV con tamponature
  duttili -> SLO, 2/3 di 0,0075 h)
