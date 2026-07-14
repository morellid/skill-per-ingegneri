# Task: Calcola U di una struttura opaca e verifica i limiti DM 26/06/2015

## Obiettivo

Data la stratigrafia di una struttura opaca (parete verticale, copertura,
pavimento), calcolare la trasmittanza termica U e verificarla rispetto ai
valori limite per zona climatica del DM 26/06/2015 (requisiti minimi).

## Input richiesti

- **stratigrafia**: per ogni strato, dall'interno all'esterno, spessore [m] e
  **conducibilita' termica lambda** [W/(m K)]. La lambda e' un dato dell'utente
  (scheda tecnica del materiale / valore dichiarato): **il modulo non la stima**;
- **resistenze superficiali** R_si e R_se [m2 K/W] (da UNI EN ISO 6946; dato
  dell'utente). Valori comuni per parete verticale (flusso orizzontale):
  R_si = 0,13 e R_se = 0,04 - **da verificare sulla norma**, non riprodotti qui;
- **zona climatica** del Comune (A, B, C, D, E, F);
- **tipo di struttura**: parete_verticale / copertura / pavimento;
- **regime**: `riqualificazione` (edifici esistenti, Appendice B - contesto
  Ecobonus) oppure `edificio_riferimento` (nuove costruzioni / ristrutturazioni
  importanti, Appendice A);
- **anno** del limite: `2021` (corrente) o `2015`;
- se l'intervento prevede **isolamento dall'interno o in intercapedine**
  (attiva l'incremento +30% dei limiti App. B);
- eventualmente: struttura verso ambiente non climatizzato / controterra
  (attivano avvertenze sui fattori di correzione).

## Fonti da leggere

- `references/estratti/dm-2015-limiti-trasmittanza.md` (tabelle limiti + caveat)
- se serve conferma: `references/fonti/dm-26-06-2015-requisiti-minimi.md`

## Procedura (usa SEMPRE il modulo, non calcolare a mano)

```bash
python3 tasks/lib/trasmittanza.py \
  --strato "intonaco_int:0.015:0.70" \
  --strato "muratura:0.25:0.40" \
  --strato "eps:0.12:0.036" \
  --strato "intonaco_est:0.015:0.90" \
  --rsi 0.13 --rse 0.04 --zona E --tipo parete_verticale \
  --regime riqualificazione --anno 2021
```

Opzioni: `--isolamento-interno` (+30% App. B), `--verso-non-climatizzato`,
`--controterra`. Output JSON con U, dettaglio delle resistenze, limite
applicato, esito della verifica e avvertenze.

Il modulo **rifiuta** (exit 1, campo `errore`): stratigrafia vuota; spessore o
lambda non positivi; R_si/R_se mancanti; zona/tipo/regime/anno non validi;
`chiusura_trasparente` (i serramenti non si calcolano per stratigrafia: usare la
Uw dichiarata dal produttore vs Tabella 4); incremento +30% chiesto in regime
`edificio_riferimento`.

## Output atteso

- **U calcolata** [W/(m2 K)] con il dettaglio delle resistenze (R_si, somma
  strati, R_se) e la tabella degli strati;
- **limite applicato** (con citazione: DM 26/06/2015, Appendice B Tab. 1-3 o
  Appendice A, zona, anno) e se e' stato applicato l'incremento +30%;
- **esito** U <= limite (sì/no);
- riportare **integralmente le avvertenze** del modulo, in particolare:
  - il limite del DM **include i ponti termici**, la U 1D no -> verifica
    **preliminare** (completa: UNI EN ISO 14683/10211);
  - lambda e R_si/R_se sono dati dell'utente, non verificati;
  - struttura verso ambienti non climatizzati / controterra: fattori di
    correzione (UNI/TS 11300-1, UNI EN ISO 13370) non applicati dal modulo;
- avvertenza finale: la skill non sostituisce la relazione tecnica ex art. 8
  D.Lgs. 192/2005 firmata dal progettista.
