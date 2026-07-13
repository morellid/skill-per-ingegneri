# Esempio: eccentricita' oltre il limite di 1/6 - calcolo rifiutato

## Richiesta dell'utente

> "Plinto 2 x 3 m, piano di posa a -1,0 m, sabbia con phi' = 30 gradi, gamma = 18 kN/m3. Il pilastro trasmette anche un momento: eccentricita' in direzione B pari a 0,40 m. Calcolami il carico limite."

## Dati (input modulo)

- B = 2,0 m; L = 3,0 m; Df = 1,0 m
- Condizione: drenata; phi' = 30 gradi; c' = 0
- gamma = 18 kN/m3
- **eB = 0,40 m** -> eB / B = 0,20 > 1/6 = 0,167

## Cosa ci si attende

Il modulo deve **rifiutare** il calcolo: su terreno la fonte impone eccentricita' inferiore a 1/6 della dimensione ("Footings founded on soil should be designed such that the eccentricity in any direction is less than one-sixth of the actual footing dimension... If eccentricity does exceed these limits, the footing should be resized" - FHWA 8.4.3.1). L'agent riporta il messaggio bloccante e rinvia al ridimensionamento, senza calcolare comunque un valore.
