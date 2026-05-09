# Output atteso - Caso problematico: OCR < 1 (sigma_p < sigma_0)

## RIFIUTATO

La skill deve **rifiutare** il calcolo. Il modulo Python ritorna codice di errore 2 e stampa su stderr:

```
ERRORE: sigma_p = 100.0 kPa < sigma_0 = 200.0 kPa: OCR < 1 non e' fisicamente ammissibile (preconsolidazione non puo' essere inferiore alla tensione attuale). Verificare i dati edometrici.
```

## Risposta attesa dell'agent

> I parametri forniti producono OCR = sigma_p / sigma_0 = 100 / 200 = 0.5, che non e' fisicamente ammissibile: la tensione di preconsolidazione e' la massima tensione che il terreno ha sopportato nella sua storia geologica e non puo' essere inferiore alla tensione efficace attuale. La skill rifiuta il calcolo e suggerisce di verificare i dati edometrici.
>
> Possibili cause:
> - determinazione errata di sigma_p' dalla curva edometrica e-log(sigma') (es. metodo Casagrande / Janbu mal applicato, scarsa qualita' del campione);
> - errore di unita' di misura nello spreadsheet (kPa vs MPa);
> - terreno sottoconsolidato (consolidazione ancora in corso): in questo caso la formulazione classica della compressione monodimensionale **non si applica** e il progettista deve usare metodi specifici per terreni sottoconsolidati (es. consolidazione progressiva con monitoraggio dei sovraccarichi);
> - scambio fra colonne nei dati di input.
>
> Suggerimento: tornare alla relazione geotecnica e verificare la determinazione di sigma_p' (allegato della prova edometrica), il valore di sigma_0' (calcolo geostatico con tensioni efficaci, considerando la posizione della falda), e la coerenza delle unita' di misura. La skill non puo' procedere finche' OCR >= 1.

## Comportamento atteso dell'agent

1. Riportare il messaggio bloccante senza aggirare l'errore (per esempio NON scambiare sigma_p e sigma_0 senza l'approvazione dell'utente: e' un'assunzione che potrebbe nascondere un errore reale di misura).
2. Spiegare chiaramente il significato fisico dell'OCR e perche' < 1 non e' ammissibile.
3. Elencare le cause plausibili dell'errore.
4. Rinviare il progettista alla relazione geotecnica e alle prove edometriche per la verifica.
5. NON inventare un valore di Delta h con i dati forniti: il calcolo sarebbe privo di senso fisico.
