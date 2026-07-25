# Note — Verifica di applicabilità dell'analisi lineare statica

## Perché questo esempio

Mostra le due condizioni di applicabilità del metodo delle forze laterali (T1 ≤ 2,5·TC e regolarità in altezza) e la
scelta del coefficiente λ, che sono le decisioni che ogni progettista prende all'inizio di un'analisi lineare.

## Ancoraggio alla fonte

Ogni valore/formula è tratto da `../../references/fonti/ntc2018-par-7-3-2-7-3-4.md` (NTC 2018, §7.3.2-7.3.3.2),
verificato sull'immagine delle pagine PDF 222/223:

- Analisi lineare statica ammessa solo se la risposta non dipende dai modi superiori (§7.3.2).
- Applicabilità: **T1 ≤ 2,5·TC** (o TD) **e regolare in altezza** (§7.3.3.2).
- **Fh = Sd(T1)·W·λ/g**; **Fi = Fh·zi·Wi/(Σj zj·Wj)** [7.3.7]; **λ = 0,85** se **T1 < 2·TC e ≥ 3 orizzontamenti**,
  altrimenti **1,0** (§7.3.3.2).

I confronti numerici (2,5·TC = 1,00 s; 2·TC = 0,80 s) sono semplici applicazioni aritmetiche delle soglie sui dati di
input, non valori di fonte.

## Limiti

Non si calcola Sd(T1) né q né si esegue l'analisi: l'esempio riguarda solo l'applicabilità del metodo e la scelta di λ.
