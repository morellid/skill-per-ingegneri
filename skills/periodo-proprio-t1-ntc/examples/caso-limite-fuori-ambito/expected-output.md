# Output atteso: torre 48 m, massa non uniforme - stima NON utilizzabile

## Comando eseguito

```bash
python3 tasks/lib/periodo_t1.py --metodo circolare --h 48 --tipologia telaio-acciaio \
  --massa-uniforme no
```

## Risultato (JSON del modulo, campi principali)

```json
{
  "metodo": "circolare",
  "formula": "T1 = C1*H^(3/4)  [C7.3.2] Circ. 7/2019 par. C7.3.3.2",
  "T1_s": 1.5501,
  "input": {"H_m": 48.0, "tipologia": "telaio-acciaio", "C1": 0.085}
}
```

con avvertenze del modulo che includono:

- H = 48 m > 40 m: la stima semplificata di T1 e' prevista dalle NTC per costruzioni che non superino i 40 m di altezza (NTC 7.3.3.2); fuori da questo limite serve l'analisi modale;
- massa dichiarata NON approssimativamente uniforme lungo l'altezza: la stima semplificata non e' applicabile (NTC 7.3.3.2).

## Sintesi testuale attesa

La risposta corretta della skill NON e' consegnare "T1 = 1,55 s" come risultato utilizzabile, ma:

1. riportare il valore numerico **come mero output della formula**, chiarendo che per questo edificio la stima semplificata e' **fuori dal proprio ambito di validita'** per due ragioni indipendenti (H = 48 m > 40 m; massa non approssimativamente uniforme - entrambe le condizioni sono nel testo del par. 7.3.3.2 NTC 2018);
2. indicare che il periodo T1 va determinato con l'**analisi modale** sul modello di calcolo;
3. ricordare che anche l'**analisi lineare statica** richiede condizioni (T1 <= 2,5*TC o TD, regolarita' in altezza) da verificare sul T1 calcolato correttamente;
4. rinviare al progettista strutturista per ogni impiego del valore.

Un output che presentasse 1,55 s come "il periodo dell'edificio" senza le avvertenze sarebbe un output SBAGLIATO per questa skill.
