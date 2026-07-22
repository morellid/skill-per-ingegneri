# Task: classifica-categoria-topografica

Inquadra la classificazione della **categoria topografica** (T1-T4) secondo le **NTC 2018 par. 3.2.2**. Supporto
documentale: **non** calcola lo spettro né il coefficiente di amplificazione topografica ST.

## Quando usarla

Il geologo/geotecnico/strutturista deve attribuire al sito una categoria topografica ai fini della definizione
dell'azione sismica. Per la categoria di sottosuolo usa `classifica-categoria-sottosuolo`.

## Passi

1. **Scelta dell'approccio** (§3.2.2): per **condizioni topografiche complesse** occorre predisporre specifiche
   analisi di risposta sismica locale; per **configurazioni superficiali semplici** si adotta la classificazione
   della Tab. 3.2.III.
2. **Attribuzione della categoria** (Tab. 3.2.III), in funzione dell'**inclinazione media i** e della forma:
   - **T1**: superficie **pianeggiante**, pendii e rilievi **isolati** con **i ≤ 15°**;
   - **T2**: **pendii** con **i > 15°**;
   - **T3**: **rilievi** con larghezza in cresta molto minore che alla base e **15° ≤ i ≤ 30°**;
   - **T4**: **rilievi** con larghezza in cresta molto minore che alla base e **i > 30°**.
   (Operatori ≤ / > verificati sull'immagine della pagina.)
3. **Ambito di applicazione** (§3.2.2): le categorie topografiche si riferiscono a configurazioni geometriche
   prevalentemente **bidimensionali** (creste o dorsali allungate) e devono essere considerate nella definizione
   dell'azione sismica **se di altezza maggiore di 30 m**. Per altezze non superiori a 30 m l'effetto topografico,
   nell'approccio semplificato, non modifica la classificazione (di norma T1).

Usa la checklist in `../references/estratti/categorie-sottosuolo-topografiche-checklist.md` (sezione 2).

## Output atteso

Un inquadramento che indichi la **categoria topografica** T1-T4 con il criterio (inclinazione media i, forma del
rilievo) e la condizione di applicabilità (configurazioni 2D, altezza > 30 m), con **rinvio al paragrafo/tabella**
NTC. Nessun calcolo del coefficiente ST né dello spettro.

## Cosa NON fare

- Non **calcolare** il coefficiente di amplificazione topografica **ST** né lo **spettro** (§3.2.3.2): rinvia a
  `spettro-risposta-ntc`.
- Non trattare le **condizioni topografiche complesse** con l'approccio semplificato: in tal caso servono analisi
  di risposta locale (§7.11.3).
