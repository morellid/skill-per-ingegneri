# Note di dominio - caso conforme fittizio

## Perche' questo esempio

Caso "ordinario residenziale" classico:
- Costruzione con livelli di prestazione ordinari (V_N = 50)
- Classe d'uso II (residenziale, terziario non strategico)
- Sottosuolo C (terreni a grana grossa mediamente addensati o terreni a grana fina mediamente consistenti, V_S,30 in 180-360 m/s)
- Topografia T1 (pianeggiante o pendio con i <= 15 grad)

Sono i parametri piu' frequenti nei progetti di edilizia ordinaria italiana e quindi il primo banco di prova della skill.

## Cosa verifica

1. **Pipeline completa** dall'input lato professionista all'output spettro tabulato per i 4 SL.
2. **Interpolazione log-log** sui T_R: SLO ricade vicino al nodo k=30, SLV vicino al nodo k=475, SLD/SLC tra nodi adiacenti.
3. **Clamp di SS** (cat. C): per SLO con a_g molto basso si attiva il limite superiore SS=1.50.
4. **Plateau di Se(T) tra T_B e T_C**: visibilmente costante a 0.79676 g per SLV.
5. **Continuita' nei raccordi T_B, T_C, T_D**: confermata anche dalla test suite (`test_continuita_TB`, `test_continuita_TC`, `test_continuita_TD`).

## Limiti dell'esempio

- I parametri di pericolosita' sono **fittizi** e progettati per leggibilita' (ag/F0/Tc* monotoni crescenti). Un sito reale puo' avere monotonia non perfetta.
- Il caso non copre cat. di sottosuolo D o E (clamp diversi, valori CC con esponenti maggiori).
- Il caso non copre topografia T2/T3/T4 (ST > 1).
- Per la validazione di Livello 2 (validazione di dominio) servono casi reali con confronto vs CSLP, vedi `tasks/run-test-suite.md`.
