# Esempio — Output atteso: profilo resistente e coefficiente kh per una trave in legno massiccio

> Supporto documentale (NTC 2018, par. 11.7). Non è una verifica di progetto: la resistenza di progetto
> (fd = kmod·fk/γM) e le verifiche restano a carico del progettista.

## 1. Caso di qualificazione (§11.7.1, §11.7.2)

- Il legno massiccio a sezione rettangolare conforme a **UNI EN 14081-1** e **marcato CE** rientra nel **caso A**
  del §11.1 (Marcatura CE). La classe **C24** appartiene alle classi di resistenza **UNI EN 338**, cui è associato
  il profilo resistente (fm,k, ft,0,k, …, moduli, massa volumica — Tab. 11.7.I).

## 2. Applicabilità del coefficiente kh (§11.7.1.1)

- Per il **legno massiccio** la dimensione di riferimento è **150 mm**. L'elemento è **inflesso** con altezza
  **h = 120 mm < 150 mm** → **kh applicabile** a fm,k (e ft,0,k).
- Calcolo: **kh = min[(150/h)^0,2 ; 1,3] = min[(150/120)^0,2 ; 1,3]**.
  - (150/120) = 1,25; 1,25^0,2 = e^(0,2·ln1,25) = e^(0,2·0,2231) = e^0,04463 ≈ **1,046**.
  - **kh = min[1,046 ; 1,3] = 1,046** (arrotondabile a ~1,05).

## 3. Valore di fm,k incrementato

- **fm,k,adj = kh · fm,k = 1,046 × 24 ≈ 25,1 N/mm²** (l'incremento è modesto perché h è di poco inferiore a 150 mm).
- Nota: il coefficiente kh incrementa **solo fm,k e ft,0,k**, non gli altri parametri del profilo resistente.

## Sintesi

- Massiccio C24 marcato CE → **caso A** (UNI EN 14081-1, classi UNI EN 338).
- h = 120 mm < 150 mm → **kh = min[(150/120)^0,2 ; 1,3] ≈ 1,05**.
- **fm,k incrementato ≈ 1,05 × 24 ≈ 25,1 N/mm²**.

**Fuori scope**: la resistenza di progetto fd = kmod·fk/γM e le verifiche (§4.4). Non sostituisce il progettista.
