# Output atteso - Trazione con fori e stabilità dell'asta compressa

## 1. Diagonale tesa con fori (§4.2.4.1.2.1)

Per una membratura tesa con **sezione indebolita da fori**, la resistenza di progetto a trazione **Nt,Rd** è
il **minore** fra due valori [4.2.5-7]:

- **resistenza plastica della sezione lorda**: **Npl,Rd = A·fyk / γM0** [4.2.6], con **γM0 = 1,05**;
- **resistenza a rottura della sezione netta**: **Nu,Rd = 0,9·Anet·ftk / γM2** [4.2.7], con **γM2 = 1,25**
  (coefficiente per la frattura delle sezioni tese indebolite dai fori).

La verifica è **NEd/Nt,Rd ≤ 1**. Per S355 (t ≤ 40 mm) si assumono fyk = 355 e ftk = 510 N/mm² (Tab. 4.2.I);
A è l'area lorda, Anet l'area netta in corrispondenza dei fori. I valori numerici li calcola il progettista.

## 2. Asta compressa: quando trascurare l'instabilità (§4.2.4.1.3.1)

La verifica di stabilità dell'asta compressa è **NEd/Nb,Rd ≤ 1** [4.2.41], con **Nb,Rd = χ·A·fyk / γM1**
[4.2.42] (classi 1, 2, 3), **γM1 = 1,05**. Il coefficiente **χ = 1/(Φ + √(Φ² − λ̄²)) ≤ 1** [4.2.44] dipende
dalla **snellezza normalizzata λ̄ = √(A·fyk/Ncr)** [4.2.45] e dal fattore di imperfezione α (curva di
instabilità, Tab. 4.2.VIII / EC3).

I fenomeni di instabilità si possono **trascurare** quando:

- **λ̄ < 0,2**, oppure
- **NEd < 0,04·Ncr**

(con Ncr carico critico elastico). In tal caso la verifica si riconduce alla resistenza a compressione
della sezione (Nc,Rd = A·fyk/γM0).

## 3. Limiti di snellezza (§4.2.4.1.3.1)

È opportuno limitare la **snellezza λ = l0/i** [4.2.47] (l0 = β·l lunghezza d'inflessione) a:

- **λ ≤ 200** per le **membrature principali**;
- **λ ≤ 250** per le **membrature secondarie**.

## Avvertenza

La skill **inquadra** le formule e i coefficienti (Nt,Rd = min(A·fyk/γM0; 0,9·Anet·ftk/γM2); Nb,Rd =
χ·A·fyk/γM1; soglia λ̄ < 0,2; limiti 200/250); **non calcola** A, Anet, Ncr, χ né le resistenze in valore e
**non esegue** le verifiche. Restano compito del progettista strutturale, che deve leggere il §4.2 (e per le
curve di instabilità la Tab. 4.2.VIII / EC3) delle NTC 2018.
