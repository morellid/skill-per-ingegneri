# Task: inquadra-regolarita-pianta-altezza

Inquadra la **verifica dei criteri di regolarità in pianta e in altezza** di un edificio secondo le **NTC 2018
par. 7.2.1**. Supporto documentale: **non** calcola la struttura ne' esegue l'analisi.

## Quando usarla

Il progettista deve stabilire se una costruzione e' regolare in pianta e/o in altezza. Per le **conseguenze** su
metodo di analisi e fattore di comportamento (par. 7.3) usa `inquadra-conseguenze-regolarita`.

## Passi

1. **Regolare in pianta** - vanno rispettate **tutte** le condizioni a-c (§7.2.1):
   - **(a)** masse e rigidezze **approssimativamente simmetriche** rispetto a due direzioni ortogonali e **forma
     compatta** (contorno di ogni orizzontamento **convesso**); le rientranze sono ammesse se, per ogni
     rientranza, l'area tra il perimetro e la linea convessa circoscritta **non supera il 5%** dell'area
     dell'orizzontamento;
   - **(b)** il **rapporto tra i lati** del rettangolo circoscritto alla pianta e' **inferiore a 4**;
   - **(c)** ciascun orizzontamento e' **rigido nel proprio piano** (diaframma rigido) con resistenza sufficiente.
2. **Regolare in altezza** - vanno rispettate **tutte** le condizioni d-g (§7.2.1):
   - **(d)** i **sistemi resistenti alle azioni orizzontali si estendono per tutta l'altezza** (o fino alla
     sommita' della rispettiva parte);
   - **(e)** massa e rigidezza **costanti o graduali**: **variazioni di massa <= 25%**; **rigidezza** che **non
     si riduce piu' del 30%** ne' **aumenta piu' del 10%** da un orizzontamento al sovrastante (per la rigidezza
     si considerano regolari strutture con pareti/nuclei in c.a. o muratura di sezione costante o telai
     controventati in acciaio cui sia affidato **almeno il 50%** dell'azione sismica alla base);
   - **(f)** il **rapporto capacita'/domanda allo SLV** non differisce in resistenza **piu' del 30%** tra
     orizzontamenti adiacenti (eccezione: ultimo orizzontamento di strutture intelaiate di **almeno tre** piani);
   - **(g)** i **restringimenti** avvengono con continuita', oppure il **rientro** di un orizzontamento **non
     supera il 10%** della dimensione sottostante **ne' il 30%** della dimensione al primo orizzontamento
     (eccezione: ultimo orizzontamento di costruzioni di **almeno quattro** piani).
3. **Casi particolari** (§7.2.1): con **struttura scatolare rigida** alla base (a comportamento non dissipativo e
   di rigidezza significativamente maggiore), i controlli di regolarita' in altezza possono riferirsi alla **sola
   struttura soprastante**. Per i **ponti** la regolarita' e' definita al **§7.9.2.1** (fuori ambito).
4. **Conclusione**: la costruzione e' **regolare in pianta** solo se valgono **tutte** le a-c, ed e' **regolare
   in altezza** solo se valgono **tutte** le d-g; regolarita' in pianta e in altezza sono **indipendenti**.

Usa la checklist in `../references/estratti/regolarita-checklist.md` (sezioni 1-3).

## Output atteso

Un inquadramento che, per l'edificio in esame, elenchi le condizioni a-c (pianta) e d-g (altezza) con le
relative soglie e indichi se la costruzione risulta regolare in pianta e/o in altezza, con **rinvio ai
paragrafi/lettere** NTC. Nessun calcolo strutturale.

## Cosa NON fare

- Non calcolare masse, rigidezze o il rapporto capacita'/domanda al posto del progettista; non eseguire
  l'analisi.
- Non determinare q0 (Tab. 7.3.II) ne' le classi di duttilita' (§7.2.2); non trattare la regolarita' dei **ponti**
  (§7.9.2.1).
