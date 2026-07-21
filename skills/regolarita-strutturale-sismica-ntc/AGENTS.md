# AGENTS.md - regolarita-strutturale-sismica-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **progettista strutturale** per l'**inquadramento della valutazione della regolarita' di
una costruzione in pianta e in altezza** ai fini della progettazione sismica secondo le **NTC 2018** (DM 17
gennaio 2018), **paragrafo 7.2.1**, e delle sue conseguenze sul metodo di analisi e sul fattore di comportamento
(par. 7.3.1, 7.3.3.1). Target: ingegneri strutturisti.

**E' una skill documentale per il tecnico**: fornisce i criteri di regolarita' (in pianta a-c, in altezza d-g)
con le soglie e le conseguenze (fattore KR = 1/0,8, applicabilita' dell'analisi lineare statica); **non calcola**
la struttura, **non esegue** l'analisi e **non determina** q0 (Tab. 7.3.II) ne' T1.

## Nota sull'area e sulla complementarita'

Area **strutture-geotecnica**. **Complementa** `spettro-risposta-ntc` (§3.2, spettro di progetto),
`periodo-proprio-t1-ntc` (§7.3.3.2, stima di T1) e `combinazioni-carico-ntc` (§2.5.3). E' **distinta**: nessuna
di queste tratta i criteri di regolarita' del §7.2.1. Condivide con le altre skill NTC la stessa fonte (PDF GU
del S.O. n. 8 alla G.U. n. 42/2018). Restano fuori scope q0 e le classi di duttilita' (§7.2.2), la stima/limiti
di T1 (§7.3.3.2) e la regolarita' dei ponti (§7.9.2.1).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **ntc2018-par-7-2-1**: PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (DM 17 gennaio
  2018, NTC 2018), SHA256 `dda1e397...` (doppio download riproducibile, stessa fonte delle altre skill NTC).
  Par. 7.2.1 (sezione REGOLARITA') estratto con `pdftotext -layout` (p. GU 208) e trascritto verbatim insieme ai
  richiami dei par. 7.3.1 (KR) e 7.3.3.1 (analisi lineare statica).

Trascrizione in `references/fonti/ntc2018-par-7-2-1-regolarita.md`; estratto operativo in
`references/estratti/regolarita-checklist.md`.

## Punti chiave (verificati sul testo)

- **Regolare in pianta** (§7.2.1, tutte le a-c): (a) simmetria masse/rigidezze su due direzioni ortogonali e
  forma compatta (contorno convesso; rientranze <= 5% dell'orizzontamento); (b) rapporto lati del rettangolo
  circoscritto < 4; (c) diaframma rigido.
- **Regolare in altezza** (§7.2.1, tutte le d-g): (d) sistemi resistenti estesi per tutta l'altezza; (e) massa e
  rigidezza graduali (massa <= 25%, rigidezza non ridotta > 30% ne' aumentata > 10% tra piani; pareti/nuclei in
  c.a./muratura o telai controventati in acciaio con >= 50% dell'azione alla base considerati regolari); (f)
  rapporto capacita'/domanda SLV entro 30% tra piani adiacenti; (g) restringimenti con rientro <= 10% del piano
  sottostante ne' > 30% del primo orizzontamento.
- **Casi particolari** (§7.2.1): struttura scatolare rigida -> controlli sulla sola struttura soprastante; ponti
  -> §7.9.2.1.
- **Conseguenze**: par. 7.3.1 KR = 1 (regolare in altezza) / 0,8 (non regolare), q_lim = q0 x KR; par. 7.3.3.1
  analisi lineare statica ammessa solo se T1 <= 2,5 TC o TD e regolare in altezza.

## Convenzioni specifiche

### Cosa NON fare
- Non **calcolare** la struttura ne' **eseguire** l'analisi; non **determinare** q0 (Tab. 7.3.II) ne' le classi
  di duttilita' (§7.2.2); non **calcolare** T1 (§7.3.3.2).
- Non **trattare** la regolarita' dei ponti (§7.9.2.1).

### Cosa fare
- Fornire i criteri di regolarita' (a-c, d-g) con le soglie e le conseguenze (KR, metodo di analisi), sempre con
  rinvio al paragrafo/lettera NTC.

## Aggiornamento delle fonti

NTC: se il PDF GU cambia (nuova edizione/errata) riscaricare, ricalcolare l'hash con doppio download e
riestrarre/ritrascrivere il par. 7.2.1. Verificare le soglie (5%, lati < 4, 25%, 30%/10%, 30%, 10%/30%) e i
valori di KR (1 / 0,8) e la condizione dell'analisi statica (T1 <= 2,5 TC o TD e regolare in altezza).

## Validatori

- Non ancora assegnato (Livello 2 con ingegnere strutturista).

## Stato attuale

- Versione: 0.1.0-alpha (closes #419)
- Task files: 2 (`inquadra-regolarita-pianta-altezza.md`, `inquadra-conseguenze-regolarita.md`)
- Esempi: 2 (verifica di regolarita' in pianta/altezza con le soglie; conseguenze della non regolarita' in
  altezza su KR e metodo di analisi)
