# Esempio — Output atteso: capacity design e limite NEd/Npl,Rd di una colonna dissipativa

> Supporto documentale (NTC 2018, par. 7.6.4). Non è una verifica strutturale: le verifiche di resistenza/duttilità
> restano a carico del progettista.

## 1. Limite superiore della capacità EU,Rd (§7.6.4.2)

- La progettazione si basa sul **limite inferiore Epl,Rd** (da confrontare con la domanda: ESd < Epl,Rd) e sul
  **limite superiore EU,Rd = 1,1·γov·Epl,Rd**, da usare per la capacità delle altre componenti (γov al §7.5.1).
- Con **γov = 1,25** (S355) e **Epl,Rd = 800 kNm**:

  **EU,Rd = 1,1 × 1,25 × 800 = 1100 kNm.**

- Le componenti non dissipative e i collegamenti adiacenti vanno dimensionati su questo limite superiore
  (**Rj,d ≥ RU,Rd**, [7.6.1]).

## 2. Limite sullo sforzo normale della colonna primaria (§7.6.4.3)

- Requisito [7.6.3]: **NEd/Npl,Rd ≤ 0,3**.
- Calcolo: **NEd/Npl,Rd = 1800/5000 = 0,36**.
- **0,36 > 0,30** → **NON verificato**: lo sforzo normale normalizzato nella colonna primaria dissipativa supera
  il limite. Occorre aumentare la sezione della colonna (maggiore Npl,Rd) o ridurre NEd.

## Sintesi

- **EU,Rd = 1,1 × 1,25 × 800 = 1100 kNm** per il dimensionamento delle componenti non dissipative.
- Colonna primaria: **NEd/Npl,Rd = 0,36 > 0,3** → **non verificato**.

**Fuori scope**: le verifiche RES/DUT complete di membrature e collegamenti (§§ 7.6.4-7.6.8), i rapporti
larghezza/spessore (Tab. 7.6.I / §7.5.6) e le regole per tipologia restano a carico del progettista. Non
sostituisce il progettista.
