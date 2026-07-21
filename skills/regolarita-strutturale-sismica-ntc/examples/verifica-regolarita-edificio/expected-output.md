# Output atteso - Verifica di regolarità (§7.2.1)

## Regolarità in pianta (condizioni a-c)

Per essere regolare in pianta devono valere **tutte** le condizioni a-c:

- **(a)** masse/rigidezze approssimativamente simmetriche rispetto a due direzioni ortogonali e forma compatta
  (contorno convesso): **soddisfatta** (pianta rettangolare compatta, masse/rigidezze circa simmetriche; nessuna
  rientranza oltre il 5%);
- **(b)** rapporto tra i lati del rettangolo circoscritto **< 4**: 30/12 = **2,5 < 4** → **soddisfatta**;
- **(c)** orizzontamento rigido nel proprio piano: solai in c.a. → **soddisfatta**.

→ **Regolare in pianta**: tutte le condizioni a-c sono rispettate.

## Regolarità in altezza (condizioni d-g)

Per essere regolare in altezza devono valere **tutte** le condizioni d-g. La condizione critica è la **(e)**:
massa e rigidezza costanti o graduali, con la **rigidezza** che **non si riduce più del 30%** da un
orizzontamento a quello sovrastante.

- **(e)** al terzo piano la rigidezza si riduce di **circa il 45% > 30%** → **non soddisfatta** (piano debole).

→ **Non regolare in altezza**: basta che una delle condizioni d-g non sia rispettata. Le altre (d, f, g) andrebbero
comunque verificate, ma la (e) è già violata.

## Sintesi

L'edificio è **regolare in pianta** ma **non regolare in altezza**. La regolarità in pianta e in altezza sono
**indipendenti**: un edificio può essere regolare nell'una e non nell'altra.

## Avvertenza

La skill **inquadra** i criteri e le soglie (§7.2.1); il **calcolo** di masse, rigidezze e del rapporto
capacità/domanda resta compito del progettista. Per le conseguenze (fattore KR, metodo di analisi) vedi
`inquadra-conseguenze-regolarita`.
