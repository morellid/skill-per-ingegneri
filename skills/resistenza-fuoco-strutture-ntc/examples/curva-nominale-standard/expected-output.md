# Output atteso - Curva nominale standard d'incendio (§3.6.1.5.1, [3.6.2])

## 1. Curva da usare

Per materiali combustibili prevalentemente di **natura cellulosica**, la curva di incendio nominale di
riferimento è la **curva nominale standard** [3.6.2]:

    θg = 20 + 345 · log10(8t + 1)  [°C]

con θg = temperatura dei gas caldi (°C) e t = tempo (minuti primi). Trattandosi di **curva nominale**, le
temperature si valutano per l'intervallo di tempo **pari alla classe** (qui **R 60 → fino a t = 60 min**),
**senza fase di raffreddamento**.

## 2. Temperature richieste

- a **t = 30 min**: θg = 20 + 345·log10(8·30 + 1) = 20 + 345·log10(241) = 20 + 345·2,382 ≈ **20 + 822 = 842
  °C**;
- a **t = 60 min**: θg = 20 + 345·log10(8·60 + 1) = 20 + 345·log10(481) = 20 + 345·2,682 ≈ **20 + 925 = 945
  °C**.

## 3. Uso nella verifica

La curva θg(t) è il **dato di ingresso termico** per l'analisi dell'evoluzione della temperatura negli
elementi (§3.6.1.5.2) e, quindi, per l'analisi del comportamento meccanico in **combinazione eccezionale**
(§3.6.1.5.3). La verifica è soddisfatta se la **resistenza meccanica** è mantenuta per il **tempo pari alla
classe** (R 60 → 60 min) (§3.6.1.5.4).

(Per incendi di **idrocarburi** si userebbe la curva [3.6.3]; per strutture **esterne** al compartimento la
curva [3.6.4].)

## Avvertenza

La skill **inquadra** le formule delle curve nominali e il criterio di verifica (tempo della classe). I valori
di θg sono un'**illustrazione** dell'applicazione di [3.6.2]: l'analisi termica negli elementi, le proprietà
dei materiali ad alta temperatura (Eurocodici parte 1-2) e la verifica meccanica restano compito del
progettista, secondo il §3.6.1 delle NTC 2018.
