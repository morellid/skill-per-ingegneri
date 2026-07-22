# Task: classifica-categoria-sottosuolo

Inquadra la classificazione della **categoria di sottosuolo** (A-E) con l'**approccio semplificato** secondo le
**NTC 2018 par. 3.2.2**. Supporto documentale: **non** calcola lo spettro né determina i valori di VS.

## Quando usarla

Il geologo/geotecnico/strutturista deve attribuire al sito una categoria di sottosuolo A-E ai fini della
definizione dell'azione sismica. Per la categoria topografica usa `classifica-categoria-topografica`.

## Passi

1. **Scelta dell'approccio** (§3.2.2): la risposta sismica locale si valuta con **specifiche analisi** (§7.11.3)
   oppure, se le condizioni stratigrafiche e le proprietà dei terreni sono **chiaramente riconducibili** alla Tab.
   3.2.II, con l'**approccio semplificato** basato sulle onde di taglio VS. I valori di VS sono parte della
   **caratterizzazione geotecnica** del volume significativo (§6.2.2) e derivano da prove specifiche (o, con
   motivazione e solo per l'approccio semplificato, da relazioni empiriche).
2. **Velocità equivalente** (§3.2.2): calcola (dato in ingresso) la velocità equivalente

       Vs,eq = H / Σ(i=1..N) ( hi / Vs,i )                            [3.2.1]

   con hi spessore dello strato i, Vs,i velocità dello strato i, N numero di strati, H profondità del
   **substrato** (formazione con **Vs ≥ 800 m/s**). (Frazione/sommatoria verificate sull'immagine della pagina.)
3. **Piano di riferimento** (§3.2.2): la profondità del substrato si misura da: **piano di imposta** per le
   fondazioni superficiali; **testa dei pali** per le fondazioni su pali; **testa dell'opera** per le opere di
   sostegno di terreni naturali; **piano di imposta della fondazione** per i muri di terrapieni.
4. **Regola dei 30 m** (§3.2.2): se il substrato è a **profondità H > 30 m**, si usa **VS,30** (si pone H = 30 m
   nella [3.2.1], considerando gli strati fino a 30 m).
5. **Attribuzione della categoria** (Tab. 3.2.II):
   - **A**: ammassi rocciosi affioranti/terreni molto rigidi, **VS > 800 m/s** (eventuale copertura scadente di
     spessore ≤ 3 m);
   - **B**: VS,eq **compresa tra 360 e 800 m/s**;
   - **C**: VS,eq **tra 180 e 360 m/s**, substrato **> 30 m**;
   - **D**: VS,eq **tra 100 e 180 m/s**, substrato **> 30 m**;
   - **E**: terreni riconducibili a **C o D**, ma con substrato **≤ 30 m**.
6. **Non classificabile** (§3.2.2): se il sottosuolo non è riconducibile a queste categorie, occorre predisporre
   specifiche **analisi di risposta locale** (§7.11.3).

Usa la checklist in `../references/estratti/categorie-sottosuolo-topografiche-checklist.md` (sezione 1).

## Output atteso

Un inquadramento che indichi la **categoria di sottosuolo** attribuita, con la formula **Vs,eq = H/Σ(hi/Vs,i)**
[3.2.1], il piano di riferimento del substrato, la regola dei 30 m (VS,30) e i limiti di VS,eq della Tab. 3.2.II,
con **rinvio ai paragrafi/tabella** NTC. Nessun calcolo dello spettro.

## Cosa NON fare

- Non **calcolare** lo spettro né i **coefficienti di amplificazione** SS/CC (§3.2.3.2): rinvia a
  `spettro-risposta-ntc`.
- Non **determinare i valori di VS** né la stratigrafia al posto del geologo/geotecnico (§6.2.2), né eseguire le
  analisi di risposta locale (§7.11.3).
