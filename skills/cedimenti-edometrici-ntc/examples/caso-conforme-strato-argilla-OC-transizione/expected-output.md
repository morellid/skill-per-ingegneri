# Output atteso - calcolo cedimento: argilla OC con transizione a NC

## Comando eseguito

```bash
python3 tasks/lib/cedimento_edometrico.py --h0 2 --e0 0.8 --cc 0.30 --cr 0.05 \
  --sigma0 100 --sigmap 150 --dsigma 200
```

## Risultato (JSON del modulo, campi principali)

```json
{
  "formulazione": "FHWA NHI-06-088 par. 7.5.2 (eq. 7-2/7-4/7-6), codice internazionale ex cap. 12 NTC 2018",
  "S_totale_m": 0.110126,
  "S_totale_mm": 110.1,
  "strati": [
    {
      "strato": 1,
      "caso": "OC",
      "equazione_FHWA": "[7-4]",
      "OCR": 1.5,
      "sigma_f": 300.0,
      "S_mm": 110.1,
      "epsilon_media": 0.055063,
      "dettaglio_m": {
        "termine_ricompressione_m": 0.009783,
        "termine_vergine_m": 0.100343
      }
    }
  ]
}
```

(Avvertenze globali del modulo omesse qui per brevita': riportarle sempre integralmente nella risposta.)

## Sintesi testuale attesa

- **S = 110,1 mm** (0,110 m) con l'**eq. [7-4]** del FHWA NHI-06-088 par. 7.5.2.2: caso sovraconsolidato (OCR = sigma_p/sigma_0 = 150/100 = 1,5) con sigma_f = 300 kPa > sigma_p = 150 kPa, quindi due contributi: ramo di ricompressione da 100 a 150 kPa con Cr (9,8 mm) + ramo vergine da 150 a 300 kPa con Cc (100,3 mm, dominante). Verifica a mano: S = 2,0/1,8 * (0,05*log10(1,5) + 0,30*log10(2)) = 0,110126 m.
- **Inquadramento normativo**: la formulazione FHWA e' usata come "altro codice internazionale" ai sensi del **cap. 12 NTC 2018** (responsabilita' del progettista sui livelli di sicurezza); il valore va confrontato con il **limite Cd** dichiarato dal progetto (NTC § 6.2.4.3, Ed <= Cd [6.2.7]).
- **Limiti richiamati**: solo consolidazione primaria (niente decorso nel tempo ne' compressione secondaria); delta_sigma' = 200 kPa e sigma_p' = 150 kPa sono input del progettista (diffusione tensioni e correzione della curva edometrica fuori ambito); deformazione media epsilon = 5,5%.
- Rinvio finale alla revisione del **progettista firmatario**.
