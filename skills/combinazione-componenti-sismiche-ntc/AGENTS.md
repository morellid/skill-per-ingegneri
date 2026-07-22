# AGENTS.md - combinazione-componenti-sismiche-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **progettista strutturale** per l'**inquadramento della combinazione delle componenti
dell'azione sismica** e della risposta alla variabilità spaziale del moto secondo le **NTC 2018** (DM 17 gennaio
2018), **paragrafo 7.3.5**. Target: ingegneri strutturisti.

**E' una skill documentale per il tecnico**: fornisce la regola di combinazione (1,00 Ex + 0,30 Ey + 0,30 Ez, con
permutazione circolare), la condizione sulla componente verticale, i criteri per la variabilità spaziale (SRSS) e
la regola sul numero di storie temporali (3/7); **non esegue** l'analisi, **non calcola** gli effetti e **non
genera** le storie temporali.

## Nota sull'area e sulla complementarita'

Area **strutture-geotecnica**. **Complementa** `combinazioni-carico-ntc` (§2.5.3, combinazioni di carico e ψ, non
la combinazione delle componenti sismiche), `criteri-modellazione-sismica-ntc` (§7.2.6),
`regolarita-strutturale-sismica-ntc` (§7.2.1), `spostamenti-interpiano-sld-ntc` (§7.3.6.1) e `spettro-risposta-ntc`
(§3.2). E' **distinta**: nessuna di queste tratta la combinazione delle componenti del §7.3.5. Condivide con le
altre skill NTC la stessa fonte (PDF GU del S.O. n. 8 alla G.U. n. 42/2018). Restano fuori scope i casi che
richiedono la componente verticale (§7.2.2) e la variabilità spaziale del moto (§3.2.4).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **ntc2018-par-7-3-5**: PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (DM 17 gennaio
  2018, NTC 2018), SHA256 `dda1e397...` (doppio download riproducibile, stessa fonte delle altre skill NTC).
  Par. 7.3.5 estratto con `pdftotext -layout` (p. GU 221) e trascritto verbatim; la formula [7.3.10] verificata
  anche sull'immagine renderizzata della pagina PDF 225 (pdftoppm), perche' pdftotext perde i segni "+".

Trascrizione in `references/fonti/ntc2018-par-7-3-5.md`; estratto operativo in
`references/estratti/combinazione-componenti-checklist.md`.

## Punti chiave (verificati sul testo)

- **Combinazione** (§7.3.5): **1,00 x Ex + 0,30 x Ey + 0,30 x Ez** [7.3.10]; effetti piu' gravosi dal confronto
  tra le **tre combinazioni** ottenute **permutando circolarmente** i coefficienti (1,00 a turno su ciascuna
  componente, 0,30 sulle altre due).
- **Componente verticale** (§7.3.5): solo nei casi previsti al §7.2.2.
- **Variabilità spaziale del moto** (§7.3.5): effetti pseudo-statici (spostamenti relativi) combinati con **SRSS**
  solo nei casi del §3.2.4.1 (salvo §7.2.2 per appoggi mobili).
- **Integrazione al passo** (§7.3.5): due componenti orizzontali simultanee (+ verticale ove necessario); **>= 3
  storie temporali -> valori piu' sfavorevoli**; **>= 7 storie temporali -> media dei valori piu' sfavorevoli**;
  variabilità spaziale con storie differenziate coerenti per ciascun vincolo o moto sincrono (§3.2.4).

## Convenzioni specifiche

### Cosa NON fare
- Non **eseguire** l'analisi ne' **calcolare** gli effetti; non **generare/selezionare** le storie temporali.
- Non **confondere** i coefficienti (1,00 dominante, 0,30 le altre due) ne' dimenticare la **permutazione
  circolare** (tre combinazioni, o due con la sola parte orizzontale).
- Non **trattare** i casi della componente verticale (§7.2.2) ne' la variabilità spaziale del moto (§3.2.4).

### Cosa fare
- Fornire la regola [7.3.10] con la permutazione circolare, la condizione sulla verticale, i criteri SRSS e la
  regola 3/7 delle storie temporali, sempre con rinvio al paragrafo/formula NTC.

## Aggiornamento delle fonti

NTC: se il PDF GU cambia (nuova edizione/errata) riscaricare, ricalcolare l'hash con doppio download e
riestrarre/ritrascrivere il par. 7.3.5. Verificare la formula [7.3.10] (1,00/0,30/0,30, segni + sull'immagine) e
la regola delle storie temporali (3 -> valori piu' sfavorevoli; 7 -> media).

## Validatori

- Non ancora assegnato (Livello 2 con ingegnere strutturista).

## Stato attuale

- Versione: 0.1.0-alpha (closes #425)
- Task files: 2 (`inquadra-combinazione-componenti.md`, `inquadra-analisi-integrazione-passo-variabilita.md`)
- Esempi: 2 (combinazione delle componenti con permutazione circolare; numero di storie temporali 3/7
  nell'integrazione al passo)
