# Task: Stima del periodo proprio T1 (NTC 2018 [7.3.6] / Circ. 7/2019 [C7.3.2])

Stima il periodo del modo di vibrare principale T1 di una costruzione, in via preliminare, con le due formule semplificate delle fonti; se l'utente fornisce TC, valuta anche la condizione T1 <= 2,5*TC per l'analisi lineare statica e il coefficiente lambda della [7.3.7].

## Obiettivo

Restituire all'utente:

- **T1 stimato** [s] con la formula appropriata, indicando esplicitamente quale ([7.3.6] NTC o [C7.3.2] Circolare) e i suoi input.
- **Esito dei limiti di applicabilita'** della stima semplificata (H <= 40 m, massa approssimativamente uniforme - NTC 7.3.3.2).
- Se TC e' fornito: **condizione T1 <= 2,5*TC** (con rinvio alla condizione alternativa su TD e alla regolarita' in altezza) e **lambda** (0,85 / 1,0) per le forze [7.3.7].
- **Avvertenze** e rinvio al progettista.

## Input richiesti

Chiedere all'utente (in base al metodo):

1. **Metodo di stima**:
   - `ntc` ([7.3.6], T1 = 2*sqrt(d)): richiede **d** [m] = spostamento laterale elastico del punto piu' alto dell'edificio dovuto alla combinazione [2.5.7] (G1 + G2 + somma psi_2j*Qkj) applicata in direzione orizzontale. Richiede quindi un modello di calcolo gia' disponibile. E' la stima che la Circolare indica come **piu' affidabile**.
   - `circolare` ([C7.3.2], T1 = C1*H^(3/4)): richiede **H** [m] dal piano di fondazione e **tipologia strutturale** (telaio-acciaio / telaio-legno / telaio-ca / muratura / altro). Stima "in via di prima approssimazione", senza modello.
2. **H** [m] anche per il metodo `ntc`, se disponibile (serve al check del limite dei 40 m).
3. **Massa approssimativamente uniforme lungo l'altezza?** (si/no - condizione della stima semplificata).
4. Opzionali: **TC** [s] dello spettro (NON calcolato da questa skill: rinvio a `spettro-risposta-ntc`) e **numero di orizzontamenti** (per lambda).

Se l'utente chiede quale metodo usare: con un modello disponibile usare `ntc` [7.3.6]; senza modello usare `circolare` [C7.3.2] segnalando che e' una prima approssimazione (gerarchia dichiarata in C7.3.3.2, vedi estratto).

## Fonti normative

Leggere prima di procedere:

- `references/estratti/t1-formule-e-limiti.md` - formule, coefficienti C1, limiti, condizioni su TC
- `references/fonti/ntc2018-dm-17-01-2018.md` - trascrizione par. 7.3.3.2 e [2.5.7]
- `references/fonti/circ-7-2019-mit.md` - trascrizione par. C7.3.3.2 e nota 9

## Procedura

### Passo 1 - Esegui il calcolo con il modulo Python

Usa SEMPRE il modulo `tasks/lib/periodo_t1.py` (mai calcoli a mano):

```bash
# metodo Circolare [C7.3.2]
python3 tasks/lib/periodo_t1.py --metodo circolare --h 16 --tipologia telaio-ca \
  --tc 0.4 --orizzontamenti 5 --massa-uniforme si

# metodo NTC [7.3.6]
python3 tasks/lib/periodo_t1.py --metodo ntc --d 0.04 --h 21 --massa-uniforme si
```

L'output e' JSON: T1_s, formula, input, avvertenze e (se TC fornito) limite 2,5*TC, esito condizione, lambda.

### Passo 2 - Presenta il risultato

Riporta:

1. **T1 = [valore] s** con la formula usata e la citazione ([7.3.6] NTC 2018 par. 7.3.3.2 oppure [C7.3.2] Circ. 7/2019 par. C7.3.3.2) e gli input effettivi (d oppure H, tipologia, C1).
2. **Limiti della stima**: esito su H <= 40 m e massa uniforme; se violati, il risultato NON e' utilizzabile come stima normativa e serve l'analisi modale.
3. **Se TC fornito**: T1 <= 2,5*TC (si/no) ricordando che l'analisi lineare statica richiede anche la **regolarita' in altezza** e che esiste la condizione alternativa su **TD** (non valutata dalla skill); lambda = 0,85 o 1,0 per la [7.3.7].
4. Se l'utente ha usato il metodo `circolare` e dispone (o disporra') di un modello: suggerisci di ripetere la stima con la [7.3.6], che la Circolare indica come piu' affidabile.

### Passo 3 - Concludi sempre con

- La stima e' **preliminare**: non sostituisce l'analisi modale ne' il giudizio del progettista strutturista.
- TC e TD dipendono dal sito: per calcolarli usare la skill `spettro-risposta-ntc` o il foglio di calcolo di progetto.
- La distribuzione delle forze [7.3.7] e l'ordinata spettrale Sd(T1) sono fuori dall'ambito di questa skill.

## Output

Blocco JSON del modulo + sintesi testuale con citazioni normative e avvertenze.

## Limiti

- Non esegue **analisi modale** ne' calcola d: lo spostamento d va ricavato dal modello di calcolo dell'utente.
- Non calcola **TC / TD / Sd(T1)** (rinvio a `spettro-risposta-ntc`).
- Non valuta la **regolarita' in altezza** (par. 7.2.1): dichiarazione a carico del progettista.
- Non copre edifici **esistenti** (cap. 8), **ponti**, ne' costruzioni oltre i limiti della stima semplificata.
- Non implementa formule di letteratura non presenti nelle fonti trascritte.
