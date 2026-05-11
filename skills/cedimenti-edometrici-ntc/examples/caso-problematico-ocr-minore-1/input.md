# Input - Caso problematico: OCR < 1 (sigma_p < sigma_0)

## Scenario

Progettista presenta uno strato di argilla con i seguenti parametri (presumibilmente errore in qualche fase del processo):
- h0 = 2.0 m, e0 = 0.8, Cc = 0.30, Cr = 0.05
- sigma_0' = 200 kPa (geostatica)
- sigma_p' = 100 kPa (preconsolidazione dichiarata)
- Delta sigma' = 50 kPa

OCR = sigma_p / sigma_0 = 100/200 = **0.5 < 1**: **non fisicamente ammissibile**.

La preconsolidazione di un terreno e' la massima tensione che il terreno ha sopportato nella sua storia geologica. Non puo' essere inferiore alla tensione efficace attuale: se cosi' fosse, significherebbe che il terreno e' meno consolidato di quanto la storia tensionale richiede, condizione fisicamente impossibile per un terreno in equilibrio.

Possibili cause dell'errore:
- determinazione errata di sigma_p' dalla curva edometrica (metodo Casagrande / Janbu mal applicato);
- errore di unita' di misura;
- terreno sottoconsolidato (sigma_0' apparente > sigma_p' a causa di consolidazione ancora in corso, ma allora non e' valida la formulazione classica);
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

La skill deve **rifiutare** il calcolo. Il modulo Python solleva `ValueError` con messaggio esplicito che cita "OCR < 1 non e' fisicamente ammissibile" e suggerisce di "verificare i dati edometrici". L'agent deve riportare il messaggio bloccante senza aggirarlo.
