# Task: determina-livello-classe-resistenza

Inquadra i **livelli di prestazione** (I-V) e la **classe di resistenza al fuoco** richiesta a un
compartimento secondo il **DM 9 marzo 2007** (punti 3-4 dell'Allegato). Supporto documentale: associa il
livello e ricava la classe dalle tabelle; **non** esegue il progetto prestazionale né le analisi.

## Quando usarla

Il tecnico ha determinato q_f,d (vedi `calcola-carico-incendio-specifico-progetto`) e deve ricavare la
classe di resistenza al fuoco richiesta, individuando prima il livello di prestazione.

## Passi

1. **Livelli di prestazione** (punto 3): individua il livello richiesto:
   - **I** — nessun requisito di resistenza al fuoco (**non ammesso** nel campo di applicazione del decreto);
   - **II** — mantenimento per un periodo sufficiente all'**evacuazione degli occupanti** in luogo sicuro
     all'esterno;
   - **III** — mantenimento per un periodo **congruo con la gestione dell'emergenza**;
   - **IV** — dopo l'incendio, **limitato danneggiamento** della costruzione;
   - **V** — dopo l'incendio, **mantenimento della totale funzionalità**.

2. **Classi** (punto 3): la classe esprime la durata minima (minuti) di svolgimento della funzione:
   **15, 20, 30, 45, 60, 90, 120, 180, 240, 360**.

3. **Livello II** — se la costruzione è fino a **2 piani fuori terra e 1 interrato**, ospita attività **non
   aperte al pubblico** e rispetta le condizioni previste (occupanti che raggiungono un luogo sicuro; nessun
   danno ad altre costruzioni; **affollamento ≤ 100 persone** e **densità ≤ 0,2 persone/m²**; assenza di
   posti letto e di persone che necessitano assistenza), la classe è:
   - **classe 30** — costruzione a **un solo piano fuori terra senza interrati**;
   - **classe 60** — costruzione fino a **due piani fuori terra e un piano interrato**.

4. **Livello III — Tabella 4** (classe in funzione di q_f,d [MJ/m²]):
   q_f,d ≤ 100 → **0**; ≤ 200 → **15**; ≤ 300 → **20**; ≤ 450 → **30**; ≤ 600 → **45**; ≤ 900 → **60**;
   ≤ 1200 → **90**; ≤ 1800 → **120**; ≤ 2400 → **180**; > 2400 → **240**.

5. **Livelli IV e V** (punto 3): richiesti da committente/capitolati/autorità competente; la progettazione
   segue i criteri del **DM 14 settembre 2005**.

6. **Incendio di progetto e curve naturali** (punto 4):
   - **curve nominali**: **standard θ_g = 20 + 345·log10(8t+1)**; **idrocarburi**; **esterna** (t in minuti);
   - con l'approccio basato su **curve naturali** la classe si ricava dalla **Tabella 5** (q_f,d [MJ/m²]):
     ≤ 300 → **0**; ≤ 450 → **15**; ≤ 600 → **20**; ≤ 900 → **30**; ≤ 1200 → **45**; ≤ 1800 → **60**;
     ≤ 2400 → **90**; > 2400 → **120**.

Usa la checklist in `../references/estratti/carico-incendio-checklist.md` (sezioni 3, 4 e 5).

## Output atteso

L'individuazione del **livello di prestazione** e la **classe di resistenza al fuoco** richiesta (dalla
Tabella 4 per il livello III, o 30/60 per il livello II), con il **rinvio al punto/tabella** del DM.
Nessun progetto prestazionale né analisi.

## Cosa NON fare

- Non **eseguire** il progetto prestazionale con curve naturali/modelli d'incendio né le analisi
  termiche/meccaniche degli elementi (verifica R in combinazione eccezionale).
- Non **stabilire** i livelli IV-V nel dettaglio (DM 14/9/2005) né riprodurre le regole tecniche verticali VVF.
