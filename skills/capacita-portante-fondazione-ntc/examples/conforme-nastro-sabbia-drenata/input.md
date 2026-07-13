# Esempio: plinto rettangolare su sabbia limosa, condizione drenata, falda presente

## Richiesta dell'utente

> "Plinto 2 x 3 m con piano di posa a -1,0 m su sabbia limosa omogenea (dalla relazione geotecnica: phi' = 30 gradi, c' = 5 kPa, gamma = 18 kN/m3). Falda a -1,5 m dal piano campagna. Carico verticale centrato; l'azione di progetto normale al piano di posa in combinazione A1 e' Ed = 900 kN. Verifica a carico limite NTC."

## Dati (input modulo)

- B = 2,0 m; L = 3,0 m; Df = 1,0 m
- Condizione: drenata; phi' = 30 gradi; c' = 5 kPa (valori caratteristici dalla relazione geotecnica = valori di progetto con M1 = 1,0)
- gamma = 18 kN/m3 (sopra e sotto il piano di posa)
- DW = 1,5 m dal piano campagna
- Nessuna eccentricita'; nessun sovraccarico applicato; dq = 1,0 (default conservativo)
- Ed = 900 kN

## Screening fuori ambito

Carico verticale, base e piano campagna orizzontali, terreno omogeneo, nessuna azione sismica: il caso rientra nell'ambito della skill.
