# Note - Caso problematico: sezione sovra-armata

## Perche' e' un caso problematico

- L'armatura tesa `A_s = 3500 mm^2` e' troppo elevata rispetto alla sezione 300 x 500 mm con C25/30 + B450C.
- Il rapporto x/d risulta circa 0.876 (`x = 402.93 mm`, `d = 460 mm`), ben oltre il limite di duttilita' raccomandato (0.45) e oltre il limite balanced (~ 0.641 per B450C, sopra il quale l'acciaio non snerva).
- La sezione e' **fragile**: rottura per schiacciamento del calcestruzzo senza plateau plastico dell'acciaio.

## Cosa la skill deve fare

1. Rifiutare il calcolo riportando il messaggio del modulo.
2. Spiegare la natura dell'errore (sovra-armatura, acciaio non snerva).
3. Suggerire i rimedi (aumentare b/h, ridurre A_s, doppia armatura).
4. Rinviare il progettista a software esterno per il calcolo corretto.

## Anti-pattern da NON commettere

- **Non aggirare l'errore** modificando A_s (es. "uso A_s = 2000 invece di 3500"): e' una manipolazione che invalida il pre-dimensionamento.
- **Non calcolare M_Rd con la formula classica** anche se l'utente insiste: il valore sarebbe sbagliato (sovrastima della resistenza). La skill esiste proprio per evitare questo.
- **Non confondere "sovra-armata" con "x/d > 0.45"**: x/d > 0.45 ma con acciaio snervato e' un caso "non duttile" che la skill calcola con avvertenza; sovra-armata (eps_s < eps_yd) e' una condizione molto piu' severa che la skill rifiuta.
- **Non inventare un valore di M_Rd da memoria**: non esiste una formula chiusa semplice per sezioni sovra-armate; servono iterazioni o software dedicato.

## Test corrispondente

Il test `TestEndToEnd.test_sezione_sovra_armata_solleva` in `tasks/lib/test_flessione_ca.py` verifica che il modulo sollevi `ValueError` con messaggio contenente "sovra-armata" per A_s = 3500 mm^2 nelle condizioni date. Il test `TestCLI.test_cli_sovra_armata` verifica lo stesso comportamento via CLI con codice di uscita 2.
