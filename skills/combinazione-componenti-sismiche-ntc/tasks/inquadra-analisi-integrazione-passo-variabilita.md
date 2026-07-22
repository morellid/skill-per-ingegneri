# Task: inquadra-analisi-integrazione-passo-variabilita

Inquadra l'**analisi dinamica con integrazione al passo** (numero di storie temporali) e la **risposta alla
variabilità spaziale del moto** secondo le **NTC 2018 par. 7.3.5**. Supporto documentale: **non** esegue l'analisi
ne' genera le storie temporali.

## Quando usarla

Il progettista impiega un'analisi con storie temporali (integrazione al passo) o deve tener conto della
variabilità spaziale del moto. Per la combinazione delle tre componenti con la [7.3.10] usa
`inquadra-combinazione-componenti`.

## Passi

1. **Applicazione simultanea delle componenti** (§7.3.5): nell'analisi dinamica con integrazione al passo si
   applicano **simultaneamente le due componenti orizzontali** della storia temporale del moto del terreno (e la
   **verticale**, ove necessario).
2. **Numero di storie temporali** (§7.3.5):
   - con **almeno 3 storie temporali**, si valutano gli effetti sulla struttura utilizzando i **valori più
     sfavorevoli**;
   - impiegando **almeno 7 diverse storie temporali**, gli effetti sulla struttura sono rappresentati dalla
     **media dei valori più sfavorevoli**.
3. **Variabilità spaziale del moto - analisi lineare/statica** (§7.3.5): quando la risposta e' calcolata con la
   [7.3.10], la combinazione con gli **effetti pseudo-statici** indotti dagli **spostamenti relativi** della
   variabilità spaziale del moto si effettua **solo nei casi del §3.2.4.1**, con la **radice quadrata della somma
   dei quadrati (SRSS)** (salvo §7.2.2 per gli appoggi mobili).
4. **Variabilità spaziale del moto - integrazione al passo** (§7.3.5): l'analisi puo' essere eseguita imponendo
   alla base storie temporali **differenziate**, ma **coerenti tra loro** e generate in accordo con lo **spettro
   di risposta appropriato per ciascun vincolo**; in alternativa, analisi dinamiche con **moto sincrono** tenendo
   conto degli effetti pseudo-statici del §3.2.4.

Usa la checklist in `../references/estratti/combinazione-componenti-checklist.md` (sezioni 3-4).

## Output atteso

Un inquadramento che indichi: l'applicazione simultanea delle componenti, la regola del numero di storie
temporali (>= 3 -> valori più sfavorevoli; >= 7 -> media dei valori più sfavorevoli) e i criteri per la
variabilità spaziale del moto (SRSS nei casi §3.2.4.1; storie differenziate coerenti o moto sincrono), con
**rinvio ai paragrafi** NTC. Nessuna analisi.

## Cosa NON fare

- Non eseguire l'analisi ne' generare/selezionare le storie temporali.
- Non trattare la **generazione** dell'input sismico (§3.2.4) ne' i metodi di analisi (§7.3.3/§7.3.4) al posto
  del progettista.
