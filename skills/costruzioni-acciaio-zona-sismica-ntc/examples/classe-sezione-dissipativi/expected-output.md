# Esempio — Output atteso: classe della sezione di un elemento dissipativo (Tab. 7.5.I)

> Supporto documentale (NTC 2018, par. 7.5.3). Il rispetto della Tab. 7.5.I e del limite NEd/Npl,Rd è
> condizione necessaria per la duttilità, non una verifica di resistenza (fuori scope).

## 1. Classe della sezione richiesta (Tab. 7.5.I)

Riga pertinente per **CD "A"** con **q0 = 5** (quindi q0 > 4):

| Classe di duttilità | q0 | Classe di sezione richiesta |
|---|---|---|
| CD "A" | q0 = 5 (> 4) | **Classe 1** |

- Le travi dissipative sono di **Classe 2**, ma per **CD "A" (q0 > 4)** la Tab. 7.5.I richiede **Classe 1**.
- **Esito: NON conforme.** Con q0 = 5 in CD "A" gli elementi dissipativi devono avere sezioni di **Classe 1**.
- **Opzioni**: adottare profili con sezioni di **Classe 1**; oppure, se si vuole mantenere sezioni di Classe 2,
  rientrare in **CD "B"** con **2 < q0 ≤ 4** (per cui la Tab. 7.5.I ammette Classe 1 o 2), rivedendo di conseguenza
  q0 e il dimensionamento.

## 2. Limite sullo sforzo normale delle colonne primarie (§7.5.3)

- Requisito [7.5.3]: **NEd/Npl,Rd ≤ 0,3**.
- Calcolo: **NEd/Npl,Rd = 900/2500 = 0,36**.
- **0,36 > 0,30** → **NON verificato**: lo sforzo normale normalizzato nelle colonne primarie dissipative supera
  il limite. Occorre aumentare la sezione della colonna (maggiore Npl,Rd) o ridurre NEd.

## Sintesi

- Travi dissipative **Classe 2** con **CD "A" (q0 = 5)**: **non conforme** (serve Classe 1 o passaggio a CD "B").
- Colonne primarie: **NEd/Npl,Rd = 0,36 > 0,3** → **non verificato**.

**Fuori scope**: le verifiche RES/DUT complete di membrature e collegamenti (§§ 7.5.3.1-7.5.6) e le regole
specifiche per tipologia restano a carico del progettista. Non sostituisce il progettista.
