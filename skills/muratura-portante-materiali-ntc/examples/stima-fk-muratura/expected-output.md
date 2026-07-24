# Esempio — Output atteso: stima della resistenza a compressione fk (Tab. 11.10.VI)

> Supporto documentale (NTC 2018, par. 11.10.3). fk è un valore caratteristico: la resistenza di progetto
> (fd = fk/γM) e le verifiche restano a carico del progettista.

## 1. Resistenza caratteristica dell'elemento fbk (§11.10.3.1.2)

- Poiché è dichiarata solo la **resistenza media fbm = 12,5 N/mm²**, per gli **elementi artificiali** si stima:
  **fbk = 0,8·fbm = 0,8 × 12,5 = 10,0 N/mm²**.

## 2. Applicabilità della tabella (§11.10.3.1.2)

- La Tab. 11.10.VI è valida per murature con **giunti orizzontali e verticali riempiti di malta e di spessore
  compreso tra 5 e 15 mm**. Qui i giunti sono **10 mm** e riempiti → **applicabile**.

## 3. Determinazione di fk dalla Tab. 11.10.VI

Per elementi artificiali pieni/semipieni, entrando con **fbk = 10,0 N/mm²** e classe di malta **M10**:

| fbk elemento (N/mm²) | M15 | M10 | M5 | M2,5 |
|---|---|---|---|---|
| 10,0 | 6,2 | **5,3** | 4,7 | 4,1 |

- **fk = 5,3 N/mm²** (riga fbk = 10,0; colonna M10). Il valore è tabellato esatto, quindi **non serve
  interpolazione**. (Per valori intermedi di fbk sarebbe ammessa l'interpolazione lineare, mai l'estrapolazione.)

## Sintesi

- **fbk = 0,8·fbm = 10,0 N/mm²**.
- Giunti 10 mm (tra 5 e 15) → tabella **applicabile**.
- **fk = 5,3 N/mm²** (Tab. 11.10.VI, fbk = 10,0, malta M10).

**Fuori scope**: la resistenza di progetto fd = fk/γM e le verifiche (§4.5); la resistenza a taglio fvk con
tensioni normali (§11.10.3.3) e i moduli di elasticità (§11.10.3.5). Non sostituisce il progettista.
