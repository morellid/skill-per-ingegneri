# Output atteso - Caso conforme: strato argilla OC con transizione a NC

## Input riportati

- Strato: h0 = 2.0 m, e0 = 0.8
- Parametri edometrici: Cc = 0.30, Cr = 0.05
- Stato tensionale: sigma_0' = 100 kPa, sigma_p' = 150 kPa, Delta sigma' = 200 kPa

## Derivati

- sigma_f' = sigma_0' + Delta sigma' = 100 + 200 = **300 kPa**
- OCR = sigma_p' / sigma_0' = 150 / 100 = **1.5** (argilla lievemente sovra-consolidata)
- Ramo: **transizione** (sigma_0' < sigma_p' < sigma_f')

## Contributi

- Delta h (ramo OC, da 100 a 150 kPa): h0/(1+e0) * Cr * log10(150/100)
  = 2/1.8 * 0.05 * 0.176091 = **0.009782848 m** = 9.78 mm
- Delta h (ramo NC, da 150 a 300 kPa): h0/(1+e0) * Cc * log10(300/150)
  = 2/1.8 * 0.30 * 0.301030 = **0.100343332 m** = 100.34 mm

## Output

- **Delta h totale = 0.110126 m = 110.126180 mm** (formula transizione completa)
- epsilon medio = Delta h / h0 = 0.110126 / 2.0 = **5.51%** (sotto la soglia di avvertenza del 10%)
- Avvertenze: nessuna

## Note

- Il cedimento e' una stima di pre-dimensionamento per singolo strato omogeneo, basata sulla formulazione classica della compressione monodimensionale (Terzaghi/Skempton). Per stratigrafie reali multilayer il progettista deve sommare i contributi strato per strato (Delta sigma' a profondita' calcolato separatamente con Boussinesq).
- Il contributo NC domina (~ 91% del totale): tipico per argille con OCR moderato sottoposte a carichi che superano sigma_p'.
- Il confronto con il cedimento ammissibile (es. 25-50 mm per edifici ordinari, valori da letteratura tecnica e norme di prodotto) e' a carico del progettista geotecnico/strutturale firmatario, ai sensi di NTC par. 6.2.4. Un cedimento di 110 mm potrebbe essere eccessivo per molte tipologie di edifici e richiedere fondazioni piu' rigide (platea), miglioramento del terreno (consolidamento, jet-grouting, ecc.) o fondazioni profonde.
- Tempi di consolidazione (Cv + Terzaghi 1D), cedimenti differenziali e distorsioni angolari restano da valutare separatamente.
- Verifica del progettista geotecnico/strutturale firmatario obbligatoria prima del deposito.
