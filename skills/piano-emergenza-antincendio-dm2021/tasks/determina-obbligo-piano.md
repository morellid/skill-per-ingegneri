# Task: determina-obbligo-piano

Stabilisce se il **piano di emergenza ed evacuazione** e' obbligatorio, ai sensi
dell'art. 2 c.2/c.4 del DM 2/9/2021.

## Input richiesti

- **Numero di lavoratori** occupati nel luogo di lavoro.
- Eventuale apertura **al pubblico** e **massima presenza contemporanea** di persone.
- Eventuale rientro dell'attivita' tra quelle **soggette a controllo VV.F.** (Allegato I
  DPR 151/2011).

## Procedura

1. **Verifica le soglie** (art. 2 c.2): il piano e' **obbligatorio** se ricorre almeno una
   delle condizioni:
   - **>= 10 lavoratori**;
   - luogo **aperto al pubblico** con **> 50 persone** contemporanee;
   - attivita' dell'**Allegato I DPR 151/2011**.
2. **Se obbligatorio** -> passa a `struttura-piano-e-addetti`.
3. **Se NON obbligatorio** (art. 2 c.4): niente piano, ma predisponi le **misure
   organizzative/gestionali** in caso di incendio da riportare nel **DVR** (o documento con
   procedure standardizzate, art. 29 c.5).

## Output atteso

- Determinazione "piano obbligatorio / non obbligatorio" con la condizione che la fa
  scattare (o la loro assenza).
- In caso negativo, elenco delle misure da inserire nel DVR.

## Avvertenze

- La valutazione delle soglie va fatta sul caso concreto (conteggio lavoratori/presenze,
  classificazione DPR 151/2011).
- L'assenza dell'obbligo di piano **non** esonera dalle **misure di emergenza** nel DVR.
