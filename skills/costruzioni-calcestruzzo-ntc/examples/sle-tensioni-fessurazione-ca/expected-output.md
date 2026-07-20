# Output atteso - Limiti di tensione e stato limite di fessurazione (SLE)

## 1. Limitazione delle tensioni (§4.1.2.2.5)

Per il **calcestruzzo** (tensione massima di compressione in esercizio):

- **σc ≤ 0,60·fck** in **combinazione caratteristica (rara)** [4.1.15] → con fck = 25 MPa: σc ≤ **15,0 MPa**;
- **σc ≤ 0,45·fck** in **combinazione quasi permanente** [4.1.16] → σc ≤ **11,25 MPa**.

Il limite in combinazione quasi permanente (0,45·fck) serve a garantire la validità dell'ipotesi di
viscosità lineare; il superamento richiederebbe di considerare la viscosità non lineare.

Per l'**acciaio** (tensione massima in esercizio):

- **σs ≤ 0,8·fyk** [4.1.17] → con fyk = 450 MPa: σs ≤ **360 MPa** (per la combinazione caratteristica).

## 2. Stato limite di fessurazione (§4.1.2.2.4)

In **condizioni ambientali ordinarie** e con armatura **poco sensibile** alla corrosione, lo stato limite
pertinente è l'**apertura delle fessure**. I valori nominali limite di apertura calcolata sono:

- **w1 = 0,2 mm**, **w2 = 0,3 mm**, **w3 = 0,4 mm**.

Per condizioni ambientali **ordinarie** e armatura **poco sensibile**, tipicamente:

- **combinazione frequente** → apertura fessure ≤ **w2 (0,3 mm)**;
- **combinazione quasi permanente** → apertura fessure ≤ **w1 (0,2 mm)**.

(Per armature molto sensibili, o in condizioni aggressive/molto aggressive, si adottano limiti più severi -
fino agli stati limite di formazione delle fessure o di decompressione.)

La verifica consiste nel controllare che il valore caratteristico di apertura calcolato **wk** non superi il
limite pertinente.

## Avvertenza

La skill **inquadra** i limiti di tensione (0,60·fck, 0,45·fck, 0,8·fyk) e la scelta dello stato limite di
fessurazione con le aperture w1/w2/w3; i valori numerici in MPa derivano solo da fck = 25 e fyk = 450 (dai
§11.2/11.3). La skill **non calcola** le tensioni effettive né l'apertura wk e **non** esegue le verifiche:
restano compito del progettista, che deve leggere il §4.1 delle NTC 2018 e la Circolare 7/2019.
