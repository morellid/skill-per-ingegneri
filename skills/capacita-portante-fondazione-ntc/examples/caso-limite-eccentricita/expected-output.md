# Output atteso: eccentricita' eB = 0,40 m su B = 2,0 m - rifiuto

## Comando eseguito

```bash
python3 tasks/lib/capacita_portante.py --b 2 --l 3 --df 1 --gamma 18 \
  --condizione drenata --phi 30 --eb 0.4
```

## Risultato (JSON del modulo)

```json
{
  "errore": "eccentricita' oltre il limite di 1/6 della dimensione (fondazione su terreno, FHWA 8.4.3.1): 'the footing should be resized'. Ridimensionare la fondazione; la skill non calcola oltre il limite."
}
```

Exit code 1.

## Sintesi testuale attesa

La risposta corretta della skill NON e' produrre un numero, ma:

1. **riportare il messaggio bloccante del modulo senza aggirarlo**: eB/B = 0,40/2,0 = 0,20 >= 1/6 = 0,167;
2. spiegare il perche' dalla fonte (FHWA 8.4.3.1, trascritta): i limiti di eccentricita' (1/6 su terreno, 1/4 su roccia) garantiscono che non si abbia pressione di contatto nulla sotto la fondazione; oltre il limite "the footing should be resized";
3. indicare le strade: **ridimensionare la fondazione** (aumentare B), ridurre il momento trasmesso, o rivedere lo schema; dopo il ridimensionamento il calcolo si riesegue con le dimensioni efficaci (B' = B - 2eB, eq. [8-7]);
4. rinviare al **progettista firmatario**.

Un output che calcolasse comunque qult con eB = 0,40 m sarebbe un output SBAGLIATO per questa skill.
