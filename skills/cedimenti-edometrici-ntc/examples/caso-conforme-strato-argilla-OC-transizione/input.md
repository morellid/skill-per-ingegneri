# Input - Caso conforme: strato argilla OC con transizione a NC

## Scenario

Strato di argilla limosa, spessore h0 = 2.0 m al di sotto della futura fondazione superficiale di un edificio civile ordinario. Dalla relazione geotecnica e dalle prove edometriche su campioni indisturbati:
- indice dei vuoti iniziale e0 = 0.80
- indice di compressione Cc = 0.30 (ramo vergine, NC)
- indice di ricompressione Cr = 0.05 (ramo OC) — rapporto Cr/Cc = 1/6, tipico
- tensione efficace verticale media iniziale sigma_0' = 100 kPa (geostatica)
- tensione di preconsolidazione sigma_p' = 150 kPa (metodo Casagrande)

OCR = sigma_p / sigma_0 = 1.5: argilla **lievemente sovra-consolidata**.

Il calcolo strutturale per la fondazione fornisce un incremento medio di tensione efficace verticale Delta sigma' = 200 kPa nel tratto considerato (calcolato separatamente con Boussinesq, fuori scope skill).

## Parametri (input modulo)

```json
{
  "h0": 2.0,
  "e0": 0.8,
  "Cc": 0.30,
  "Cr": 0.05,
  "sigma_0": 100.0,
  "sigma_p": 150.0,
  "delta_sigma": 200.0
}
```

## Cosa ci si attende

Tensione finale sigma_f' = sigma_0' + Delta sigma' = 300 kPa: supera sigma_p' = 150 kPa, quindi il carico attraversa la preconsolidazione e si entra nel ramo NC. Il calcolo deve attivare il **ramo transizione** con due contributi:
- ramo OC da 100 a 150 kPa (con Cr)
- ramo NC da 150 a 300 kPa (con Cc)

Cedimento atteso: dell'ordine di 100 mm, dominato dal contributo NC. epsilon medio ~ 5%, sotto la soglia di avvertenza del 10%.
