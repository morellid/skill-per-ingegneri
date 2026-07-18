# Task - Inquadra le verifiche SLU/SLE di muri e paratie (§6.5.3)

## Obiettivo

Inquadrare gli **stati limite** da verificare, gli **approcci progettuali** e le **combinazioni** di
coefficienti per **muri** e **paratie**, con la **Tab. 6.5.I**, e le verifiche di esercizio (§6.5.3).

## Input richiesti

- tipo di opera (muro / paratia / struttura mista);
- presenza di ancoraggi/puntoni, di falda e di manufatti sensibili adiacenti;
- necessità di verifica di **stabilità globale**.

## Procedura (ancorata al testo)

1. **Muri - SLU** (§6.5.3.1.1). Verificare [6.2.1] (E_d ≤ R_d) per gli stati limite:
   - **GEO**: **scorrimento** sul piano di posa, **carico limite** fondazione-terreno, **ribaltamento**,
     **stabilità globale**;
   - **STR**: resistenza degli elementi strutturali.
   **Approcci**: **stabilità globale** → **Approccio 1, Combinazione 2 (A2+M2+R2)** (come §6.8; Tab.
   6.2.I/6.2.II/6.8.I); **rimanenti verifiche** → **Approccio 2 (A1+M1+R3)** con **Tab. 6.5.I**. Nel
   **ribaltamento** i coefficienti R3 si applicano agli effetti delle azioni **stabilizzanti**.

   **Tab. 6.5.I (γR, gruppo R3)**: capacità portante **1,4**; scorrimento **1,1**; ribaltamento **1,15**;
   resistenza del terreno a valle **1,4**.

   Nello **scorrimento** in generale **non** si considera la **resistenza passiva** del terreno a valle;
   se giustificata, al più il **50%** e con compatibilità degli spostamenti.

2. **Paratie - SLU** (§6.5.3.1.2). Stati limite **GEO/UPL/HYD** (rotazione rigida, carico limite
   verticale, sfilamento ancoraggi, instabilità/sollevamento/sifonamento del fondo scavo, stabilità
   globale) e **STR** (ancoraggi, puntoni, resistenza della paratia). **Stabilità globale** → **Approccio
   1, Comb. 2 (A2+M2+R2)**; **UPL/HYD** come §6.2.4.2; **rimanenti** → **Approccio 1**, **Comb. 1
   (A1+M1+R1)** e **Comb. 2 (A2+M2+R1)** con **γR di R1 = 1**. Verificare **ancoraggi/puntoni/controventi**;
   per **δ > φ'/2** considerare la non planarità delle superfici nella resistenza passiva.

3. **SLE** (§6.5.3.2). Valutare gli **spostamenti** dell'opera e del terreno, compatibili con la
   funzionalità e con la sicurezza dei manufatti adiacenti; per manufatti sensibili, **analisi di
   interazione** con le fasi costruttive.

## Output

Una nota che elenchi: gli stati limite da verificare per il tipo di opera; l'approccio/combinazione per
la stabilità globale e per le rimanenti verifiche; i coefficienti della Tab. 6.5.I per i muri; le
verifiche di esercizio. **La skill inquadra approcci e coefficienti; non esegue le verifiche né calcola
E_d/R_d**, che restano compito del progettista con la relazione geotecnica e la Circolare 7/2019.
