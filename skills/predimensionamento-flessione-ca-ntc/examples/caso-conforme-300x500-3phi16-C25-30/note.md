# Note - Caso conforme: trave 300x500 con 3 phi 16, C25/30 + B450C

## Perche' e' un caso conforme

- Tutti gli input sono entro il dominio di validita' della skill: fck = 25 MPa < 50 MPa (Classe 1), sezione singolarmente armata, flessione semplice, geometria coerente (`d < h`).
- Il calcolo di A_s da "3 phi 16" e' corretto: `A_s = 3 * pi * 16^2 / 4 = 603.185789... mm^2`, arrotondato a 603.19.
- L'altezza utile `d = 460 mm` e' coerente con la geometria (copriferro 30 + staffe 8 + barra 16/2 ~ 46 mm, quindi `d ~ 454 mm`; il valore 460 e' un'approssimazione prudenziale).
- C25/30 + B450C e' la combinazione piu' comune in edilizia civile italiana ordinaria.

## Cosa la skill deve fare

1. Citare NTC par. 4.1.2.1.1 per il calcolo di f_cd e f_yd.
2. Riportare il rapporto x/d e l'esito della verifica di duttilita' (snervamento + raccomandazione 0.45).
3. Riportare M_Rd in kNm (formato leggibile per il progettista).
4. Concludere con rinvio: M_Rd e' resistente, M_Ed va calcolato a parte, taglio e SLE restano a carico del progettista.

## Anti-pattern da NON commettere

- **Non riprodurre i numeri "a mano" parafrasando le formule**: usare il modulo Python.
- **Non assumere d = h - 30 o simili senza giustificazione**: il copriferro varia con classe esposizione, diametro staffe e barre. Va dichiarato dall'utente.
- **Non dedurre A_s da "3 phi 16" senza verifica**: se l'utente da' n e phi, calcola A_s = n * pi * phi^2 / 4 e CONFERMA con l'utente prima di passarlo al modulo. Per "3 phi 16" il valore corretto e' 603.19 mm^2 (non 600, non 480).
- **Non aggirare la verifica di duttilita'**: il progettista deve sapere se x/d <= 0.45 o no, anche quando il calcolo va a buon fine.
- **Non confondere M_Rd (resistente) con M_Ed (sollecitazione)**: M_Rd >= M_Ed e' la verifica, ma M_Ed va calcolato dalla combinazione SLU separatamente.
