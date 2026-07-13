# Note - esempio conforme: plinto rettangolare drenato con falda

## Perche' questo esempio e' importante

- Copre il percorso completo: fattori N da phi' (eq. [8-2][8-3][8-5], verificabili contro la Table 8-2 della fonte), fattori di forma per L/B < 10 (Table 8-4), interpolazione della falda (Table 8-5: DW = 1,5 m fra Df e 1,5B+Df -> Cwgamma = 0,5 + 0,5*(1,5-1,0)/(4,0-1,0) = 0,5833), catena NTC con gamma_R = 2,3 e confronto [6.2.1].
- I tre termini sono esposti separatamente (coesione/sovraccarico/peso) per l'audit del progettista.
- Il nome della cartella conserva il caso originario della scheda; l'esempio usa un plinto rettangolare perche' esercita anche i fattori di forma (il nastro puro e' coperto dai test del modulo).

## Limitazioni note

- Ed = 900 kN e' dichiarato gia' calcolato in combinazione A1 dall'utente: la skill non lo ricostruisce.
- phi', c', gamma e DW vengono dalla relazione geotecnica: la skill non li stima ne' li valida.
- dq = 1,0 (omissione conservativa, Table 8-6): un valore diverso richiede le condizioni della fonte e va giustificato dal progettista.
