# Nota — profilo resistente e coefficiente kh (legno massiccio)

- **Ancoraggio**: la formula kh = min[(150/h)^0,2 ; 1,3] [11.7.1], la dimensione di riferimento 150 mm e il
  profilo resistente (Tab. 11.7.I) provengono da `../../references/fonti/ntc2018-par-11-7.md` (§11.7.1.1),
  verificati sull'immagine delle pagine PDF 349-350 (GU 345-346).
- **Massiccio vs lamellare**: per il legno **lamellare** la dimensione di riferimento è 600 mm e la formula è
  kh = min[(600/h)^0,1 ; 1,1] [11.7.2] — da non confondere con quella del massiccio.
- **Solo fm,k e ft,0,k**: il coefficiente kh incrementa esclusivamente la resistenza a flessione e a trazione
  parallela; gli altri parametri del profilo resistente non si modificano.
- **Valore della classe**: fm,k = 24 N/mm² per la C24 è il valore associato alla classe UNI EN 338 (la skill non
  ricalcola i valori di classe: li assume come input dal profilo resistente dichiarato/di classe).
- **Limite della skill**: nessuna resistenza di progetto viene calcolata (fd = kmod·fk/γM è al §4.4, skill
  dedicata); kh qui è solo l'inquadramento dell'effetto dimensione.
