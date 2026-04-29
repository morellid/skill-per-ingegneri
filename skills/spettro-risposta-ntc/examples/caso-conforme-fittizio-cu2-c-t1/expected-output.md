# Output atteso - caso conforme fittizio (CU II, C, T1)

Output prodotto dal modulo `tasks/lib/spettro.py` con il comando di `input.md`. Tutti i valori sono coerenti con NTC 2018 par. 3.2.3 e con le formule citate in `references/estratti/`.

## Riepilogo per stato limite

| SL  | P_VR | TR (anni) | ag (g) | F0    | Tc* (s) | SS    | S     | CC    | TB (s) | TC (s) | TD (s) |
|-----|------|-----------|--------|-------|---------|-------|-------|-------|--------|--------|--------|
| SLO | 81%  | 30.11     | 0.0301 | 2.5003| 0.2001  | 1.5000| 1.5000| 1.7855| 0.1191 | 0.3573 | 1.7203 |
| SLD | 63%  | 50.29     | 0.0452 | 2.5508| 0.2203  | 1.5000| 1.5000| 1.7298| 0.1270 | 0.3811 | 1.7809 |
| SLV | 10%  | 474.56    | 0.2179 | 2.7200| 0.3200  | 1.3444| 1.3444| 1.5293| 0.1631 | 0.4894 | 2.4716 |
| SLC | 5%   | 974.79    | 0.2970 | 2.7400| 0.3400  | 1.2118| 1.2118| 1.4990| 0.1699 | 0.5097 | 2.7879 |

(eta = 1.0000 e ST = 1.0 in tutti i casi; xi = 5% e categoria T1.)

## Tabella Se(T) - SLV (estratto)

```
T (s)    Se (g)     ramo
0.000    0.29293    0-TB
0.100    0.60181    0-TB
0.163    0.79676    raccordo TB
0.200    0.79676    TB-TC
0.300    0.79676    TB-TC
0.400    0.79676    TB-TC
0.489    0.79676    raccordo TC
0.500    0.77979    TC-TD
1.000    0.38989    TC-TD
2.000    0.19495    TC-TD
2.472    0.16142    raccordo TD
2.500    0.15418    TD-inf
3.000    0.10707    TD-inf
4.000    0.06023    TD-inf
```

## Verifiche di consistenza

1. Plateau SLV: a_g * S * eta * F_0 = 0.2179 * 1.3444 * 1.0 * 2.7200 = 0.7967 g (corrisponde all'output).
2. T_C(SLV) = C_C * T_C* = 1.5293 * 0.32 = 0.4894 s -> ok.
3. T_B(SLV) = T_C/3 = 0.1631 s -> ok.
4. T_D(SLV) = 4 * 0.2179 + 1.6 = 2.4716 s -> ok.
5. SS(SLO) = 1.70 - 0.60 * 2.5003 * 0.0301 = 1.655 -> clamp a 1.50 (in [1.00, 1.50]) -> ok.
6. SS(SLC) = 1.70 - 0.60 * 2.7400 * 0.2970 = 1.212 -> in range -> ok.
7. La somma Se(T_B-) e Se(T_B+) coincide entro tolleranza numerica: continuita' verificata anche dalla test suite.

## Note di interpretazione

- L'output del modulo non costituisce relazione di calcolo. Va incorporato dal progettista nella relazione di calcolo strutturale firmata.
- Per ottenere lo spettro di **progetto** S_d(T) si applica la riduzione con il fattore di comportamento q (NTC par. 3.2.3.5 e par. 7), non eseguita dalla skill.
- Le correzioni per quote intermedie del rilievo (T2/T3/T4 non in sommita') sono a cura del professionista (NTC eq. 3.2.5).
