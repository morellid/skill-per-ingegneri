# Output atteso

## Applicabilità (NTC 2018 §5.2.2.2.3)

Per usuali tipologie di ponti e **velocità ≤ 200 km/h**, con frequenza propria della struttura all'interno
del «fuso» di Fig. 5.2.7, è sufficiente utilizzare i **coefficienti dinamici Φ** (non serve l'analisi
dinamica con convogli reali). Per una **trave semplicemente appoggiata**, la lunghezza caratteristica **L_φ**
coincide con la **luce**: L_φ = 20 m (Tab. 5.2.II, travi appoggiate).

## Coefficienti Φ

- Linea con **elevato** standard manutentivo (formula [5.2.6]):

  Φ2 = 1,44 / (√L_φ − 0,2) + 0,82 = 1,44 / (√20 − 0,2) + 0,82 = 1,44 / (4,472 − 0,2) + 0,82
     = 1,44 / 4,272 + 0,82 ≈ 0,337 + 0,82 = **≈ 1,16**   (nel limite 1,00 ≤ Φ2 ≤ 1,67).

- Linea con **ridotto** standard manutentivo (formula [5.2.7]):

  Φ3 = 2,16 / (√L_φ − 0,2) + 0,73 = 2,16 / 4,272 + 0,73 ≈ 0,506 + 0,73 = **≈ 1,24**   (nel limite 1,00 ≤ Φ3 ≤ 2,00).

## Sintesi

| Standard manutentivo | Formula | Φ (L_φ = 20 m) |
|---|---|---|
| Elevato | Φ2 = 1,44/(√L_φ − 0,2) + 0,82 | **≈ 1,16** |
| Ridotto | Φ3 = 2,16/(√L_φ − 0,2) + 0,73 | **≈ 1,24** |

## Note

- Il coefficiente Φ **aumenta l'intensità** dei modelli di carico (LM71, SW/0, SW/2) definiti al §5.2.2.2.1;
  **non** si applica al **treno scarico** né ai **treni «reali»**.
- Entrambi i valori rispettano i limiti (1,00 ≤ Φ2 ≤ 1,67; 1,00 ≤ Φ3 ≤ 2,00); se il risultato uscisse dai
  limiti si assumerebbe il valore limite.
- La skill inquadra la formula e i limiti; il calcolo mostrato è una semplice applicazione aritmetica. La
  scelta dello standard manutentivo, la determinazione di L_φ per elementi diversi dalla trave appoggiata
  (Tab. 5.2.II) e le verifiche restano di competenza del progettista.
