# Estratto operativo - Regolarità strutturale in pianta e in altezza (NTC 2018 par. 7.2.1)

Checklist di inquadramento per il progettista strutturale. Ogni punto e' ancorato al testo trascritto in
`../fonti/ntc2018-par-7-2-1-regolarita.md`. La skill **inquadra**, non calcola la struttura ne' esegue l'analisi.

## 1. Regolare in PIANTA (tutte le condizioni a-c) - par. 7.2.1

- [ ] **(a)** distribuzione di masse e rigidezze **approssimativamente simmetrica** rispetto a due direzioni
      ortogonali e **forma compatta** (contorno di ogni orizzontamento **convesso**); rientranze ammesse se, per
      ogni rientranza, l'area tra il perimetro e la linea convessa circoscritta **non supera il 5%** dell'area
      dell'orizzontamento?
- [ ] **(b)** il **rapporto tra i lati** del rettangolo circoscritto alla pianta di ogni orizzontamento e'
      **inferiore a 4**?
- [ ] **(c)** ciascun orizzontamento e' **rigido nel proprio piano** (diaframma rigido) e con resistenza
      sufficiente a garantire la distribuzione delle azioni sismiche tra gli elementi verticali?

> Basta che **una** delle condizioni a-c non sia rispettata perche' la costruzione sia **non regolare in pianta**.

## 2. Regolare in ALTEZZA (tutte le condizioni d-g) - par. 7.2.1

- [ ] **(d)** tutti i **sistemi resistenti alle azioni orizzontali si estendono per tutta l'altezza** (o fino
      alla sommita' della rispettiva parte, se vi sono parti di altezze differenti)?
- [ ] **(e)** massa e rigidezza **costanti o graduali** dalla base alla sommita': **variazioni di massa <= 25%**;
      **rigidezza** che **non si riduce piu' del 30%** ne' **aumenta piu' del 10%** da un orizzontamento al
      sovrastante? (per la rigidezza si considerano regolari strutture con pareti/nuclei in c.a. o muratura di
      sezione costante o telai controventati in acciaio cui sia affidato **almeno il 50%** dell'azione sismica
      alla base)
- [ ] **(f)** il **rapporto capacita'/domanda allo SLV** non differisce, in resistenza, **piu' del 30%** tra
      orizzontamenti adiacenti? (eccezione: ultimo orizzontamento di strutture intelaiate di **almeno tre**
      orizzontamenti)
- [ ] **(g)** eventuali **restringimenti** avvengono con continuita', oppure il **rientro** di un orizzontamento
      **non supera il 10%** della dimensione dell'orizzontamento sottostante, **ne' il 30%** della dimensione al
      primo orizzontamento? (eccezione: ultimo orizzontamento di costruzioni di **almeno quattro**
      orizzontamenti)

> Basta che **una** delle condizioni d-g non sia rispettata perche' la costruzione sia **non regolare in
> altezza**.

## 3. Casi particolari - par. 7.2.1

- [ ] In presenza di **struttura scatolare rigida** alla base (a comportamento non dissipativo e di rigidezza
      significativamente maggiore), i controlli di regolarita' in altezza possono riferirsi alla **sola struttura
      soprastante**?
- [ ] Per i **ponti** la regolarita' e' definita al **par. 7.9.2.1** (fuori dall'ambito di questa skill).

## 4. Conseguenze della (ir)regolarità

- [ ] **Fattore di comportamento** (par. 7.3.1): q_lim = q0 * KR, con **KR = 1** se **regolare in altezza** e
      **KR = 0,8** se **non regolare in altezza** (riduzione del fattore di comportamento).
- [ ] **Metodo di analisi** (par. 7.3.3.1): l'**analisi lineare statica** e' applicabile solo se **T1 <= 2,5 TC
      o TD** **e** la costruzione e' **regolare in altezza**; altrimenti si adotta l'analisi lineare dinamica
      (modale) o non lineare.

## Fuori scope (rinvii)

- **Non** calcola la struttura ne' esegue l'analisi; **non** determina **q0** (Tab. 7.3.II) ne' le classi di
  duttilita' (par. 7.2.2).
- **Stima e limiti di T1**: par. 7.3.3.2 (skill `periodo-proprio-t1-ntc`).
- **Regolarita' dei ponti**: par. 7.9.2.1.
