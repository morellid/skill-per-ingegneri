# Task: inquadra-approcci-progettuali-slu

Inquadra gli **stati limite ultimi geotecnici** (EQU, STR, GEO), i **due approcci progettuali** e i **coefficienti
parziali sulle azioni** secondo le **NTC 2018 par. 6.2.4.1**. Supporto documentale: **non** esegue le verifiche.

## Quando usarla

Il progettista deve impostare una verifica geotecnica agli SLU e scegliere l'approccio progettuale e la
combinazione dei coefficienti sulle azioni. Per i coefficienti sui parametri del terreno usa
`inquadra-coefficienti-parametri-geotecnici`.

## Passi

1. **Individua lo stato limite** (§6.2.4.1):
   - **EQU** (perdita di equilibrio del corpo rigido): **Einst,d ≤ Estb,d** (azione instabilizzante ≤
     stabilizzante); fattori parziali dalla **colonna EQU** della Tab. 6.2.I;
   - **STR** (resistenza di un elemento strutturale) e **GEO** (resistenza del terreno): **Ed ≤ Rd** [6.2.1].
2. **Scegli l'approccio progettuale** (§6.2.4): le verifiche impiegano combinazioni di gruppi di coefficienti per
   **azioni (A1/A2)**, **parametri geotecnici (M1/M2)** e **resistenze (R1/R2/R3)**, nell'ambito di due approcci
   alternativi:
   - **Approccio 1**: **due** combinazioni (ognuna può essere critica per aspetti diversi);
   - **Approccio 2**: **un'unica** combinazione.
3. **Regola di default** (§6.2.4): per gli SLU **non espressamente trattati** nei §6.3-6.11 si usa l'**Approccio 1**
   con le combinazioni **(A1+M1+R1)** e **(A2+M2+R2)**. I fattori del **gruppo R1 sono sempre unitari**; quelli del
   **gruppo R2** sono **≥ 1** e, in assenza di indicazioni specifiche, vanno scelti dal progettista in relazione
   alle incertezze.
4. **Coefficienti sulle azioni** (§6.2.4.1.1, Tab. 6.2.I), colonne EQU / A1 / A2:
   - **G1** (permanenti): favorevoli 0,9/1,0/1,0; **sfavorevoli 1,1/1,3/1,0**;
   - **G2** (permanenti non strutturali): favorevoli 0,8/0,8/0,8; **sfavorevoli 1,5/1,5/1,3**;
   - **Q** (variabili): favorevoli 0,0; **sfavorevoli 1,5/1,5/1,3**.
   Il **terreno e l'acqua** sono **carichi permanenti (strutturali)** quando contribuiscono con
   peso/resistenza/rigidezza; per la **spinta delle terre** si usano i **γG1**.

Usa la checklist in `../references/estratti/verifiche-geotecniche-slu-checklist.md` (sezioni 1 e 2).

## Output atteso

Un inquadramento che indichi lo stato limite (EQU/STR/GEO) con la relativa condizione (Einst,d ≤ Estb,d oppure Ed
≤ Rd [6.2.1]), l'approccio progettuale e le combinazioni di gruppi (per default Approccio 1 (A1+M1+R1) e
(A2+M2+R2), R1 unitari/R2≥1) e i coefficienti sulle azioni della Tab. 6.2.I, con **rinvio ai paragrafi/tabella**
NTC. Nessuna verifica numerica.

## Cosa NON fare

- Non **eseguire** la verifica né calcolare le azioni di progetto.
- Non attribuire i **coefficienti γR** specifici dell'opera (§6.3-6.11): rinvia alle skill d'opera; qui si tratta
  solo il framework generale e le azioni (Tab. 6.2.I).
