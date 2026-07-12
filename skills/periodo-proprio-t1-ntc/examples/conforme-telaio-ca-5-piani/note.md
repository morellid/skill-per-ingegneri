# Note - esempio conforme telaio c.a.

## Perche' questo esempio e' importante

- Mostra il caso d'uso tipico: nessun modello disponibile -> formula [C7.3.2] della Circolare, con tutti gli input dichiarati (C1, H) e la citazione corretta della fonte (Circ. 7/2019, NON NTC: la formula C1*H^(3/4) non e' nelle NTC 2018).
- Tutti i valori sono chiusi e verificabili a mano: H^(3/4) = 16^0,75 = 8; T1 = 0,075*8 = 0,60 s; 2,5*TC = 1,00 s; 2*TC = 0,80 s.
- Mostra il pattern delle conclusioni: gerarchia [7.3.6] > [C7.3.2] (suggerimento di ripetere la stima col modello), condizioni residue a carico del progettista (regolarita' in altezza, TD), rinvio a `spettro-risposta-ntc` per TC.

## Limitazioni note

- TC = 0,4 s e' un dato fornito dall'utente, non calcolato: in un caso reale va determinato dai parametri di pericolosita' del sito.
- Il valore lambda = 0,85 e' valutato con la condizione stretta T1 < 2*TC trascritta dalla fonte.
