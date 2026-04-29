# Output atteso - caso problematico (categoria S2)

## Comportamento atteso del modulo

Il modulo Python rifiuta il calcolo e solleva `ValueError` con messaggio esplicito:

```
ValueError: Categoria di sottosuolo S2: NTC par. 3.2.2 prescrive analisi
specifiche di risposta sismica locale. Calcolo non eseguibile con questa
skill.
```

In Python script si traduce in exit code != 0 e traceback. In Codex/Claude Code la skill segnala il rifiuto e propone all'utente le opzioni di seguito.

## Risposta operativa al committente

L'agent deve produrre un messaggio di questo tenore:

> La categoria di sottosuolo dichiarata (S2) ai sensi NTC 2018 par. 3.2.2 prescrive **analisi specifiche di risposta sismica locale**: lo spettro generico di NTC par. 3.2.3 non e' applicabile.
>
> Possibili percorsi:
> 1. Verifica con il geologo/geotecnico se la classificazione S2 e' corretta o se rientra in C/D/E con elementi di rischio liquefazione gestiti separatamente. La S2 vera richiede depositi di terreni suscettibili di liquefazione, di argille sensitive, o categoria non classificabile in A-E.
> 2. Se la classificazione S2 e' confermata: procedere con **studio di risposta sismica locale** (RSL) ai sensi par. 3.2.2 e par. 7.11.3.4. Output dello studio: spettri di risposta specifici (sito-specifici), non riconducibili al modello tabellare delle NTC. La presente skill non copre questo workflow.
> 3. In parallelo: valutare la **liquefazione** dei terreni di fondazione ai sensi NTC par. 7.11.3 e linee guida geotecniche specifiche (responsabilita' del geotecnico).

## Nessuna tabella spettro prodotta

Per scelta progettuale: il modulo non produce alcuno spettro "approssimato" su S2 (rischio di output non conservativo). Il messaggio di errore e' bloccante.

## Verifica nella test suite

La logica di rifiuto S1/S2 e' coperta da `test_SS_S1_S2_rifiutate` in `tasks/lib/test_spettro.py`.
