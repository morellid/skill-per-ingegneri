# Note - Caso conforme: zona 1, pianura, categoria esposizione II

## Perche' e' un caso conforme

- Tutti gli input sono entro il dominio di validita' della skill: `a_s <= 1500 m`, categoria di esposizione I-V, zona neve standard, `0 <= alpha <= 90`.
- La struttura e' di tipologia ricorrente, quindi `c_d = 1` e' valido (NTC par. 3.3.9).
- Il sito e' in pianura aperta, categoria II coerente con NTC Tab. 3.3.III.
- Il progettista ha gia' determinato `c_p = 0.8` (parete sopravento, valore tipico CNR-DT 207).

## Cosa la skill deve fare

1. Citare NTC par. 3.3.1 (eq. 3.3.1) per la formula p = q_r * c_e * c_p * c_d.
2. Mostrare il calcolo intermedio (v_b, c_r, q_r, c_e) prima dell'output finale.
3. Citare NTC par. 3.4 e Tab. 3.4.I per la neve.
4. Concludere con rinvio al progettista e indicazione di usare la skill `combinazioni-carico-ntc` per la combinazione SLU/SLE.

## Anti-pattern da NON commettere

- Non riprodurre i numeri "a mano" parafrasando le formule: usare il modulo Python.
- Non dire "categoria di esposizione II e' standard per pianure": NTC Tab. 3.3.III dipende da rugosita', distanza dalla costa, altitudine. Va dichiarata dall'utente, non assegnata dalla skill.
- Non dire "c_p = 0.8 vale per qualsiasi geometria": c_p e' input dell'utente, non una costante.
- Non confondere q_sk (al suolo, kN/m^2) con q_s (sulla copertura, kN/m^2).
