# Task - Inquadra le verifiche SLU/SLE delle fondazioni su pali (§6.4.3.1-6.4.3.4)

## Obiettivo

Inquadrare gli **stati limite** da verificare, gli **approcci progettuali** e le **combinazioni** di
coefficienti per le **fondazioni su pali** e le **fondazioni miste** a platea su pali (NTC 2018 §6.4.3).

## Input richiesti

- tipo di fondazione: **soli pali** o **fondazione mista** (analisi di interazione significativa?);
- tipo di palo (infisso / trivellato / a elica continua) e presenza di **carichi trasversali**;
- presenza di **falda**, di **pendii** (stabilità globale) e di **attrito negativo**;
- necessità di verifica di **stabilità globale**.

## Procedura (ancorata al testo)

1. **Impostazione** (§6.4.3). Se l'interazione terreno-fondazione è **non significativa/omessa** →
   verifiche sui **soli pali** (§6.4.3.1-6.4.3.2); se **significativa** → verifiche sulla **fondazione
   mista** (§6.4.3.3-6.4.3.4). Fra le azioni permanenti includere **peso proprio del palo** e **attrito
   negativo** (γM del caso **M1**, Tab. 6.2.II). Sisma: §7.11.5.3.2 (non trattato).

2. **SLU pali** (§6.4.3.1). Verificare [6.2.1] (E_d ≤ R_d) per:
   - **GEO**: carico limite **assiale**, carico limite **trasversale**, **sfilamento** in trazione,
     **stabilità globale**;
   - **STR**: resistenza dei **pali** e della **struttura di collegamento**.
   **Approcci**: **stabilità globale** → **Approccio 1, Comb. 2 (A2+M2+R2)** (Tab. 6.2.I/6.2.II/6.8.I);
   **rimanenti** → **Approccio 2 (A1+M1+R3)** con Tab. 6.4.II/6.4.VI. Nelle verifiche **STR** il γR **non**
   si porta in conto.

3. **Coefficienti** (§6.4.3.1.1). **R_d = R_k / γR** con la **Tab. 6.4.II (R3)**: base **1,15/1,35/1,3**
   (infissi/trivellati/elica), laterale in compressione **1,15**, totale **1,15/1,30/1,25**, laterale in
   trazione **1,25**. Per la **palificata** sommare le R_k dei pali con possibili **riduzioni per effetto
   di gruppo**. Per i **carichi trasversali** (§6.4.3.1.2) applicare **γT = 1,3** (Tab. 6.4.VI).

4. **SLE pali** (§6.4.3.2). Verificare **cedimenti/sollevamenti** e **spostamenti trasversali** nelle
   combinazioni caratteristiche (§2.5.3), compatibili con i requisiti prestazionali [6.2.7].

5. **Fondazioni miste** (§6.4.3.3-6.4.3.4). SLU GEO/STR con **stabilità globale in Approccio 1 Comb. 2
   (A2+M2+R2)**; se la [6.2.1] è garantita dalla **sola platea** (§6.4.2.1), ai pali la sola funzione di
   **riduzione degli spostamenti**; il contributo dei pali alle azioni verticali usa il **γR (R3) della
   Tab. 6.4.I**. SLE: interazione compatibile con i requisiti prestazionali [6.2.7].

## Output

Una nota che elenchi: gli stati limite da verificare per il tipo di fondazione; l'approccio/combinazione
per la stabilità globale e per le rimanenti verifiche; i coefficienti della Tab. 6.4.II e il γT dei
carichi trasversali; le verifiche di esercizio. **La skill inquadra approcci e coefficienti; non esegue le
verifiche né calcola R_k/R_d**, che restano compito del progettista con la relazione geotecnica e la
Circolare 7/2019.
