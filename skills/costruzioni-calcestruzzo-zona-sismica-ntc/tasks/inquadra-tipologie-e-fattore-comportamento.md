# Task — Inquadra tipologia strutturale e fattore di comportamento del c.a. sismico (NTC 2018 §7.4.2-7.4.3)

Supporto documentale per classificare la **tipologia strutturale** di un edificio in c.a., scegliere il **fattore di
comportamento** (αu/α1) e la **classe di duttilità** (CD"A"/CD"B") secondo le NTC 2018 (DM 17/1/2018), §7.4.2-7.4.3.
**Non** esegue il progetto né le verifiche.

Fonte: `../references/fonti/ntc2018-par-7-4.md`; checklist: `../references/estratti/ca-sismica-checklist.md`.

## Input tipico

- Schema strutturale (telai, pareti, misto), numero di piani/campate, distribuzione delle masse.
- Aliquote di taglio alla base assorbite da telai e pareti; presenza di travi a spessore.

## Passi

1. **Materiali (§7.4.2)**
   - Verifica l'impiego di **acciaio B450C**; **B450A** ammesso solo con **Ø 5-10 mm** per reti/tralicci o come
     armatura trasversale se la plasticizzazione è impedita (gerarchia), negli elementi secondari (§7.2.3) o nelle
     strutture non dissipative (§7.2.2).

2. **Tipologia strutturale (§7.4.3.1)**
   - **A telaio**: resistenza a taglio alla base affidata ai telai **≥ 65%** del totale.
   - **A pareti**: taglio alla base alle pareti **≥ 65%**; distingui semplici/composte e singole/accoppiate.
   - **Miste telaio-pareti**: se **> 50%** dell'azione orizzontale è assorbita dai telai → **miste equivalenti a
     telai**, altrimenti **equivalenti a pareti**.
   - **A pendolo inverso**: **≥ 50% della massa** nel terzo superiore. Monopiano intelaiata: **N ≤ 30%** della
     resistenza a compressione del solo cls.
   - **Deformabili torsionalmente**: se a qualche piano **r²/ls² < 1** (ls² = (L²+B²)/12 per pianta rettangolare).
   - **A pareti estese debolmente armate**: comportamento scatolare e **periodo ≤ TC** → solo **CD"B"**.

3. **Fattore di comportamento e classe di duttilità (§7.4.3.2)**
   - Il **q** si calcola secondo il **§7.3.1 e la Tab. 7.3.II** (skill `fattore-comportamento-q-sismica-ntc`).
   - Determina se la struttura è **a pareti accoppiate** (momento base equilibrato **≥ 20%** dalla coppia degli sforzi
     verticali).
   - Applica gli **αu/α1** per struttura regolare in pianta: telai **1,1** (1 piano) / **1,2** (più piani, 1 campata) /
     **1,3** (più piani e campate); pareti **1,0** (due pareti non accoppiate) / **1,1** (altre non accoppiate) /
     **1,2** (accoppiate o miste equiv. pareti).
   - Scegli la **CD**: pareti in CD"A" o CD"B"; pareti estese debolmente armate solo CD"B"; telai con **travi a
     spessore** → CD"B" (salvo travi «secondarie»). Per **q > 1,5** con tipologie diverse → giustificazione con
     analisi non lineari.

4. **Output**: scheda con tipologia strutturale, αu/α1, classe di duttilità e rinvio al calcolo di q (§7.3.1). Segnala
   che il progetto e le verifiche (gerarchia, dettagli) sono nel task `applica-gerarchia-delle-resistenze` e, per il
   dettaglio numerico, nella norma.

## Cosa NON fare

- Non calcolare il valore numerico di **q** (è il §7.3.1, → skill `fattore-comportamento-q-sismica-ntc`): qui si
  forniscono gli αu/α1 e le regole di scelta della CD specifiche del c.a.
- Non eseguire le **verifiche** né i **dettagli costruttivi** (§7.4.4/7.4.6).
- Non inventare valori: ogni riferimento deve essere rintracciabile in `../references/fonti/ntc2018-par-7-4.md`.
