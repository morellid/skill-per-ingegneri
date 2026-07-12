# Note - esempio caso limite fuori ambito

## Perche' questo esempio e' importante

- Le formule approssimate di T1 sono facilissime da abusare: questo esempio fissa il comportamento atteso quando i **limiti di validita' della stima** (H <= 40 m, massa approssimativamente uniforme - NTC 7.3.3.2) sono violati.
- Il modulo calcola comunque il valore della formula (utile per confronto/audit) ma la skill deve presentarlo come non utilizzabile normativamente, con le due violazioni citate testualmente dalla fonte.
- Verifica a mano: 48^0,75 = 18,23606...; T1 = 0,085 x 18,23606 = 1,55006 s (1,5501 nel JSON per il rounding a 4 decimali del modulo).

## Cosa insegna

- La differenza tra "risultato di una formula" e "stima valida ai sensi della norma".
- Il rinvio corretto: analisi modale sul modello, poi eventuale check delle condizioni dell'analisi lineare statica sul T1 cosi' ottenuto.
