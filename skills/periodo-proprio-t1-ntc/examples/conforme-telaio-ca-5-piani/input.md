# Esempio: telaio in c.a. di 5 piani - stima T1 e check analisi lineare statica

## Richiesta dell'utente

> "Edificio per uffici, telaio in c.a., 5 piani fuori terra, altezza 16 m dal piano di fondazione, massa regolare lungo l'altezza. Non ho ancora il modello. TC del sito = 0,4 s. Posso usare l'analisi statica lineare? Quanto vale T1?"

## Dati

- Tipologia: telaio in calcestruzzo armato
- H = 16 m dal piano di fondazione
- Orizzontamenti: 5
- Massa distribuita in modo approssimativamente uniforme: si
- Modello di calcolo: non disponibile -> metodo `circolare` [C7.3.2]
- TC = 0,4 s (calcolato a parte dall'utente)
