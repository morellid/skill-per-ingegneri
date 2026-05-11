# Output atteso - Caso problematico: sezione sovra-armata

## RIFIUTATO

La skill deve **rifiutare** il calcolo. Il modulo Python ritorna codice di errore 2 e stampa su stderr:

```
ERRORE: Sezione sovra-armata: eps_s = 0.000497 < eps_yd = 0.001957, l'acciaio non snerva al collasso. La formula M_Rd = As * fyd * z non si applica. Aumentare b/h o ridurre As, oppure passare a calcolo iterativo con sigma_s elastico (fuori scope skill v0.1).
```

## Risposta attesa dell'agent

> La sezione 300 x 500 mm con A_s = 3500 mm^2, fck = 25 MPa, fyk = 450 MPa e' **sovra-armata**: l'acciaio non raggiunge lo snervamento (eps_s = 0.000497) al collasso del calcestruzzo (eps_yd = 0.001957 per B450C). La formula `M_Rd = A_s * f_yd * z` di NTC par. 4.1.2.3.4.2, che assume `sigma_s = f_yd`, **sovrastima la resistenza** in questa configurazione: il calcolo corretto richiede iterazione con `sigma_s = Es * eps_s` (acciaio elastico), fuori scope della skill v0.1.
>
> Possibili rimedi (a discrezione del progettista):
> - aumentare la base `b` o l'altezza `h` (riduce x, riporta l'acciaio in snervamento);
> - ridurre l'armatura tesa `A_s` (es. da 7 phi 25 a 5 phi 20);
> - passare a sezione **doppiamente armata** con armatura compressa A's, che migliora duttilita' e capacita' rotazionale (NTC par. 4.1.2 + Circ. 7/2019 par. C4.1.2). Doppia armatura **non coperta dalla skill v0.1**: usare software di calcolo strutturale certificato.
>
> Nota: realizzare sezioni sovra-armate e' sconsigliato dalla normativa e dai manuali standard di tecnica delle costruzioni perche' la rottura avviene per schiacciamento del calcestruzzo senza preavviso plastico dell'acciaio (rottura **fragile**).

## Comportamento atteso dell'agent

1. Riportare il messaggio bloccante senza aggirare l'errore (per esempio NON arrotondare A_s a 3000 per far passare il calcolo: e' una manipolazione che invalida il pre-dimensionamento).
2. Spiegare in modo chiaro perche' la sezione e' sovra-armata e quali sono i rimedi.
3. Rinviare il progettista a software di calcolo strutturale certificato per il calcolo iterativo con sigma_s elastico, oppure per il dimensionamento di sezione doppiamente armata.
4. NON inventare un valore di M_Rd con la formula classica anche se richiesto: il modulo si rifiuta proprio perche' il valore sarebbe sbagliato.
