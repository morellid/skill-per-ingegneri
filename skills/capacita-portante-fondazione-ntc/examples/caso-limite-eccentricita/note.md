# Note - caso limite: eccentricita' oltre 1/6

## Perche' questo esempio e' importante

- Fissa il comportamento di sicurezza sul vincolo geometrico esplicito della fonte (FHWA 8.4.3.1): il limite non e' una preferenza numerica del modulo ma una prescrizione trascritta ("the footing should be resized"), con la motivazione fisica dichiarata dalla fonte (evitare pressione di contatto nulla).
- Mostra il pattern "rifiuto + spiegazione + strade percorribili + rinvio al progettista", coerente con gli altri casi limite del repo (OCR < 1 nei cedimenti, H > 40 m nel periodo T1).

## Cosa insegna

- La differenza tra un vincolo di input del modulo e una prescrizione della fonte: qui il rifiuto E' la risposta normativamente corretta.
- Dentro il limite, l'eccentricita' si tratta con le dimensioni efficaci di Meyerhof (eq. [8-7][8-8][8-9]), gia' implementate dal modulo.
