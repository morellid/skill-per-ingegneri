# Output atteso: telaio c.a. 5 piani, H = 16 m, TC = 0,4 s

## Comando eseguito

```bash
python3 tasks/lib/periodo_t1.py --metodo circolare --h 16 --tipologia telaio-ca \
  --tc 0.4 --orizzontamenti 5 --massa-uniforme si
```

## Risultato (JSON del modulo)

```json
{
  "metodo": "circolare",
  "formula": "T1 = C1*H^(3/4)  [C7.3.2] Circ. 7/2019 par. C7.3.3.2",
  "T1_s": 0.6,
  "input": {"H_m": 16.0, "tipologia": "telaio-ca", "C1": 0.075},
  "TC_s": 0.4,
  "limite_2_5_TC_s": 1.0,
  "T1_entro_2_5_TC": true,
  "lambda_forze_7_3_7": 0.85
}
```

(Avvertenze del modulo omesse per brevita': riportarle sempre nella risposta.)

## Sintesi testuale attesa

- **T1 = 0,60 s**, stimato con la [C7.3.2] della Circ. 7/2019 par. C7.3.3.2 (C1 = 0,075 per telaio in c.a., H = 16 m; H^(3/4) = 8; 0,075 x 8 = 0,60 s). Stima "in via di prima approssimazione": quando il modello sara' disponibile, ripetere con la [7.3.6] delle NTC (T1 = 2*sqrt(d)), indicata dalla Circolare come piu' affidabile.
- **Limiti della stima rispettati**: H = 16 m <= 40 m; massa dichiarata approssimativamente uniforme (NTC 7.3.3.2).
- **Condizione per l'analisi lineare statica**: T1 = 0,60 s <= 2,5*TC = 1,00 s -> soddisfatta. Restano da verificare a carico del progettista la **regolarita' in altezza** (par. 7.2.1) e, ove necessaria, la condizione alternativa su TD.
- **lambda = 0,85** per la distribuzione di forze [7.3.7] (T1 = 0,60 s < 2*TC = 0,80 s e almeno tre orizzontamenti).
- La stima e' preliminare e non sostituisce l'analisi modale ne' il giudizio del progettista. TC/TD/Sd(T1) non sono calcolati da questa skill (vedere `spettro-risposta-ntc`).
