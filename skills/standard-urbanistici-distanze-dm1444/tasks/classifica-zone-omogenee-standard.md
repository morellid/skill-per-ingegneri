# Task: classifica-zone-omogenee-standard

Classifica le **zone territoriali omogenee** e inquadra il computo degli **standard urbanistici** secondo il
**DM 2 aprile 1968 n. 1444 (artt. 2-5)**. Supporto documentale: **non** redige lo strumento urbanistico.

## Quando usarla

Il tecnico deve classificare una porzione di territorio nelle zone omogenee del DM 1444/1968 e verificare le
dotazioni minime di spazi pubblici. Per densità, altezze e distanze usa `verifica-densita-altezza-distanze`.

## Passi

1. **Zone territoriali omogenee** (art. 2), ai sensi dell'art. 17 della L. 765/1967:
   - **A)** agglomerati urbani di carattere **storico, artistico o di particolare pregio ambientale**;
   - **B)** parti **totalmente o parzialmente edificate**, diverse dalle A): parzialmente edificate se la
     **superficie coperta ≥ 12,5% (un ottavo)** della superficie fondiaria e la **densità territoriale >
     1,5 mc/mq**;
   - **C)** parti destinate a **nuovi complessi insediativi** (inedificate o sotto i limiti di B));
   - **D)** parti destinate a **nuovi insediamenti industriali** o assimilati;
   - **E)** parti destinate ad **usi agricoli**;
   - **F)** parti destinate ad **attrezzature ed impianti di interesse generale**.

2. **Standard residenziali** (art. 3): dotazione minima inderogabile **18 mq/abitante** (escluse le sedi
   viarie), ripartiti in: **a) 4,50 mq** istruzione (asili nido, materne, scuole dell'obbligo); **b) 2,00 mq**
   attrezzature di interesse comune; **c) 9,00 mq** verde attrezzato/gioco/sport; **d) 2,50 mq** parcheggi (in
   aggiunta all'art. 18 L. 765). Si assume **25 mq/abitante** di superficie lorda abitabile (≈ 80 mc v/p),
   maggiorabili fino a 5 mq per usi connessi.

3. **Quantità minime per zona** (art. 4): nelle **zone A) e B)** le aree dell'art. 3 sono **computate in
   misura doppia**; **zone C)** quantità integrale, ridotta a **12 mq** (di cui **4** scuole) per comuni ≤
   10.000 ab. (e casi analoghi), con **15 mq** per il punto c) in zone C) contigue a connotati naturali;
   **zone E) 6 mq**; **zone F)** attrezzature di interesse generale: **1,5** (istruzione superiore) + **1**
   (sanitarie/ospedaliere) + **15** (parchi urbani/territoriali) mq/abitante.

4. **Insediamenti produttivi** (art. 5): **zone D)** spazi pubblici/collettivi **≥ 10%** dell'intera
   superficie; **commerciale/direzionale** **80 mq ogni 100 mq** di superficie lorda (metà a parcheggi; per
   zone A)/B) ridotto a metà con attrezzature integrative).

Usa la checklist in `../references/estratti/standard-urbanistici-checklist.md` (sezioni 1-3).

## Output atteso

La classificazione della/e zona/e omogenea/e e il computo delle **dotazioni minime di standard** (per abitante
e per zona), con **rinvio agli articoli** del DM 1444/1968. Nessuna redazione dello strumento urbanistico.

## Cosa NON fare

- Non **redigere** lo strumento urbanistico né dimensionare il piano.
- Non **trattare** densità, altezze e distanze (usa l'altro task); non riprodurre le articolazioni
  regionali/comunali.
