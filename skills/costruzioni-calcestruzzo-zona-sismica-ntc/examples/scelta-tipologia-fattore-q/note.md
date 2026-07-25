# Note — Scelta di tipologia e fattore di comportamento

## Perché questo esempio

Mostra i due punti che ogni progettazione sismica di un edificio a telaio in c.a. affronta all'inizio: la
classificazione della tipologia (criterio del **65%** di taglio alla base) e la scelta della **classe di duttilità**,
con il vincolo — spesso dimenticato — che le **travi a spessore** impongono la **CD"B"**.

## Ancoraggio alla fonte

Ogni valore è tratto da `../../references/fonti/ntc2018-par-7-4.md` (NTC 2018, §7.4.3), verificato sull'immagine delle
pagine PDF 228/229:

- Struttura a telaio: resistenza a taglio alla base ai telai **≥ 65%** del totale (§7.4.3.1).
- αu/α1 telai: 1 piano **1,1**; più piani e una campata **1,2**; **più piani e più campate 1,3** (§7.4.3.2).
- Telai con **travi a spessore** (anche in una sola direzione) → **CD"B"** salvo travi «secondarie» (§7.4.3.2).

Il calcolo di q è demandato al §7.3.1/Tab. 7.3.II (skill `fattore-comportamento-q-sismica-ntc`): qui si fornisce solo
l'αu/α1 e la scelta della CD.

## Limiti

Non si calcola q né si eseguono verifiche: l'esempio riguarda solo la classificazione della tipologia e la scelta di
αu/α1 e della classe di duttilità.
