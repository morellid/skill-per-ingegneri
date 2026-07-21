# Output atteso - Coefficienti e resistenze di progetto (C25/30, B450C)

## 1. Coefficienti parziali (§4.1.2.1.1)

- Calcestruzzo: **γc = 1,5**. La riduzione a 1,4 **non** si applica (richiede produzione continuativa con
  controllo e coefficiente di variazione della resistenza ≤ 10% in un sistema di qualità §11.8.3, qui
  assente).
- Acciaio: **γs = 1,15** (sempre, per tutti i tipi di acciaio).

## 2. Resistenza di progetto a compressione del calcestruzzo (§4.1.2.1.1.1)

**fcd = αcc·fck/γc** [4.1.3], con **αcc = 0,85** e **γc = 1,5**. Per la classe **C25/30** il valore
caratteristico è **fck = 25 MPa** (dato del §11.2), quindi:

**fcd = 0,85 · 25 / 1,5 = 14,17 MPa** (≈ 14,2 MPa)

(Nota: per elementi piani gettati in opera con spessore < 50 mm la resistenza andrebbe ridotta a 0,80·fcd;
non è il caso di una trave.)

## 3. Resistenza di progetto a trazione del calcestruzzo (§4.1.2.1.1.2)

**fctd = fctk/γc** [4.1.4], con **γc = 1,5**. fctk (resistenza caratteristica a trazione) si ricava dal
§11.2.10.2 (frattile 5%); il calcolo del valore numerico non è oggetto della skill.

## 4. Resistenza di progetto dell'acciaio (§4.1.2.1.1.3)

**fyd = fyk/γs** [4.1.5], con **fyk = 450 MPa** e **γs = 1,15**:

**fyd = 450 / 1,15 = 391,3 MPa**

## 5. Diagramma di calcolo del calcestruzzo (§4.1.2.1.2.1)

La classe **C25/30 ≤ C50/60**, quindi si assumono **εc2 = 0,20%** ed **εcu = 0,35%** (deformazione ultima).
Si può adottare il modello parabola-rettangolo, triangolo-rettangolo o rettangolo (stress block).

## Avvertenza

La skill **inquadra** i coefficienti (γc = 1,5, γs = 1,15) e le formule delle resistenze di progetto
(fcd = αcc·fck/γc, fctd = fctk/γc, fyd = fyk/γs) con le deformazioni del diagramma; i valori numerici usano
fck = 25 MPa e fyk = 450 MPa presi dai §11.2/11.3 (non oggetto della skill). La skill **non** dimensiona né
arma la trave e **non** esegue le verifiche: restano compito del progettista, che deve leggere il §4.1 (e i
§11.2/11.3) delle NTC 2018.
