# Note di dominio - caso problematico S2

## Perche' questo esempio

Il rifiuto esplicito della categoria S2 (e di S1) e' una scelta progettuale **non negoziabile** della skill. Coprirla con valori SS/CC arbitrari fornirebbe un output formalmente "uno spettro NTC" ma sostanzialmente errato, perche' la norma stessa prescrive analisi specifiche di risposta sismica locale per quei sottosuoli.

NTC 2018 par. 3.2.2: "Per qualsiasi condizione di sottosuolo non classificabile nelle categorie precedenti, e' necessario predisporre specifiche analisi di risposta sismica locale. Per le condizioni speciali S1 e S2 sono richieste analisi specifiche".

## Errore comune che questo esempio intercetta

Capita che il committente, ricevuta la relazione geologica, si limiti a riportare la categoria sul modulo della skill (o del software FEM) senza che il progettista strutturale verifichi la coerenza con la natura del sottosuolo.

Se il sottosuolo e' realmente S2, lo spettro generico NTC sottostima sistematicamente l'azione sismica: l'effetto di sito di liquefazione/argille sensitive non e' rappresentato dalle formule SS/CC tabellari. Il rifiuto del calcolo e' quindi una protezione contro un falso positivo strutturale.

## Workflow corretto (rinvio professionale)

1. Ingegnere geotecnico: classificazione del sottosuolo, valutazione liquefazione (NTC par. 7.11.3.4), eventuale studio di risposta sismica locale (RSL) sito-specifico con scelta dei segnali di input compatibili con la pericolosita' INGV al sito.
2. Output dello studio RSL: spettri di risposta sito-specifici (uno per stato limite), che il progettista strutturale usa direttamente al posto dello spettro NTC tabellare.
3. La presente skill non sostituisce nessuno dei due passaggi: il rifiuto e' coerente con il principio di **supporto, non sostituto** richiamato in `SKILL.md`.

## Validazione operativa

Quando il validatore di Livello 2 testa la skill su un caso reale che dichiara S2:
- L'output atteso e' il rifiuto bloccante.
- Il validatore deve verificare che il messaggio di rifiuto includa il rinvio a NTC par. 3.2.2 e suggerisca l'RSL come percorso corretto.
- Se invece il validatore introduce S2 e ottiene uno spettro: e' un bug da segnalare immediatamente.
