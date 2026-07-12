# Input - Caso problematico: OCR < 1 (sigma_p < sigma_0)

## Scenario

Progettista presenta uno strato di argilla con i seguenti parametri (presumibilmente errore in qualche fase del processo):
- h0 = 2.0 m, e0 = 0.8, Cc = 0.30, Cr = 0.05
- sigma_0' = 200 kPa (geostatica)
- sigma_p' = 100 kPa (preconsolidazione dichiarata)
- Delta sigma' = 50 kPa

OCR = sigma_p / sigma_0 = 100/200 = **0.5 < 1**: dato **sospetto**, da chiarire prima di calcolare.

La preconsolidazione e' la massima tensione efficace passata: un OCR < 1 significa o un errore nei dati, oppure un terreno **sottoconsolidato** (consolidazione ancora in corso sotto il carico esistente - FHWA 7.5.2.3), condizione reale ma da riconoscere e giustificare esplicitamente.

Possibili cause dell'errore:
- determinazione errata di sigma_p' dalla curva edometrica (metodo Casagrande / Janbu mal applicato);
- errore di unita' di misura;
- terreno sottoconsolidato (consolidazione ancora in corso: in tal caso serve la dichiarazione esplicita e si applica l'eq. [7-6] FHWA);
- scambio fra colonne nello spreadsheet.

## Parametri (input modulo)

```json
{
  "h0": 2.0,
  "e0": 0.8,
  "Cc": 0.30,
  "Cr": 0.05,
  "sigma_0": 200.0,
  "sigma_p": 100.0,
  "delta_sigma": 50.0
}
```

## Cosa ci si attende

La skill deve **rifiutare il calcolo di default**. Il modulo solleva `ValueError` citando "OCR < 1" con le due letture (dati errati / sottoconsolidazione reale) e indicando che solo la dichiarazione esplicita `--sottoconsolidato` abilita l'eq. [7-6]. L'agent deve riportare il messaggio bloccante senza aggirarlo e rimettere la decisione al progettista.
