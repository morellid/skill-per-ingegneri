# Note - Caso problematico: OCR < 1

## Perche' e' un caso problematico

- I parametri forniti producono OCR = 0.5, che non e' fisicamente ammissibile per un terreno in equilibrio.
- La skill correttamente rifiuta il calcolo: la formula classica (Terzaghi/Skempton) presuppone terreno in equilibrio, e applicarla a un input non fisico produrrebbe un numero privo di significato.

## Cosa la skill deve fare

1. Riportare il messaggio del modulo.
2. Spiegare il significato fisico dell'OCR e perche' < 1 non e' ammissibile.
3. Elencare le cause plausibili (errore di misura, errore di unita', terreno sottoconsolidato, scambio colonne).
4. Rinviare alla relazione geotecnica per la verifica.

## Anti-pattern da NON commettere

- **Non scambiare sigma_p e sigma_0 senza autorizzazione**: il fatto che un parametro sia minore dell'altro non implica che siano stati invertiti; potrebbe essere un errore reale di misura (e in tal caso vanno corrette le prove, non scambiati gli input).
- **Non aggirare l'errore con assunzioni**: per esempio NON assumere "Cr = 0.05 valido come default per OC, lo applico anche se OCR < 1". L'errore va segnalato, non aggirato.
- **Non inventare un cedimento**: il calcolo con OCR < 1 sarebbe privo di senso fisico. La skill deve rifiutare ed e' giusto cosi'.
- **Non confondere "argilla sottoconsolidata" con "OCR < 1 ammissibile"**: una vera argilla sottoconsolidata richiede metodi specifici (consolidazione progressiva, monitoraggio sovraccarichi) e la formulazione classica non si applica. Se l'utente sospetta sottoconsolidazione, va rinviato a una valutazione geotecnica dedicata, non risolto con scambio di parametri.
