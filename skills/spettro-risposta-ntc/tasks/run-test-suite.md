# Task: esecuzione test suite del modulo di calcolo

## Obiettivo

Eseguire la test suite Python che verifica:
1. Le formule chiuse di NTC par. 3.2.3 (TR<->P_VR, eta, SS clamping, periodi caratteristici).
2. La continuita' di Se(T) ai raccordi TB, TC, TD.
3. L'interpolazione logaritmica sui 9 TR di riferimento (round-trip e bracket).
4. I valori canonici (VN=50 CU II -> TR_SLV ~ 475 anni).
5. Il rifiuto esplicito di S1/S2 e di TR fuori reticolo.

## Quando usare questo task

- "Verifico che il modulo dia ancora i valori attesi dopo una modifica"
- "Eseguo la regression suite prima di un release"
- "Voglio capire quali casi sono coperti dai test"

## Procedura

Da root del repo o dalla skill installata:

```bash
cd skills/spettro-risposta-ntc/tasks/lib
python3 -m unittest test_spettro -v
```

Oppure direttamente:

```bash
python3 skills/spettro-risposta-ntc/tasks/lib/test_spettro.py -v
```

## Output atteso

23 test, tutti pass:

```
test_continuita_TB ... ok
test_continuita_TC ... ok
test_continuita_TD ... ok
test_Se_T_zero ... ok
test_Se_T_T_grande ... ok
test_round_trip_su_nodo ... ok
test_interp_tra_due_nodi ... ok
test_fuori_reticolo_solleva_errore ... ok
test_SS_categoria_A ... ok
test_SS_clamping ... ok
test_SS_S1_S2_rifiutate ... ok
...
Ran 23 tests in 0.00x s
OK
```

Se anche un solo test fallisce: NON usare la skill in produzione, segnala il fail come issue al maintainer.

## Casi di confronto vs CSLP (validazione di campo)

I test interni qui descritti coprono la consistenza delle formule. La validazione "di campo" (Livello 2 di [`methodology/validazione.md`](../../../methodology/validazione.md)) richiede confronto numerico vs foglio Excel CSLP su almeno 10 casi reali.

Procedura per il validatore:
1. Scegli un sito reale (lat, lon).
2. Estrai dal foglio CSLP i parametri ag, F0, Tc* per i 9 TR di riferimento al sito.
3. Estrai dal foglio CSLP i valori TR, ag, F0, Tc*, S, eta, TB, TC, TD per ciascuno SL e per categoria sottosuolo/topografica scelta.
4. Esegui il modulo Python con gli stessi input.
5. Confronta tutti i parametri con tolleranza:
   - TR: tolleranza 0.5 anni
   - ag: tolleranza 0.0005 g
   - F0: tolleranza 0.01
   - Tc*: tolleranza 0.005 s
   - SS, S, CC, eta, TB, TC, TD: tolleranza 0.001 (relativa)
6. Documenta caso e risultato in un nuovo `examples/caso-<nome>/`.

Discrepanze entro tolleranza sono attese (interpolazione finita); discrepanze maggiori sono bug.
