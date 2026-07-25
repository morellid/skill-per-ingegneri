# Task — Scegli il metodo di analisi e imposta l'analisi lineare (NTC 2018 §7.3.2-7.3.3)

Supporto documentale per **scegliere il metodo di analisi sismica** (dinamica/statica) e impostare l'**analisi lineare
dinamica** (modale) o **statica** (forze laterali) secondo le NTC 2018 (DM 17/1/2018), §7.3.2-7.3.3. **Non** esegue
l'analisi né le verifiche.

Fonte: `../references/fonti/ntc2018-par-7-3-2-7-3-4.md`; checklist: `../references/estratti/metodi-analisi-checklist.md`.

## Input tipico

- Periodo T1 (dalla modellazione o da stima), TC del sito, regolarità in altezza, numero di orizzontamenti, altezza.
- Fattore di comportamento q (dalla skill `fattore-comportamento-q-sismica-ntc`).

## Passi

1. **Scelta del metodo (§7.3.2)**
   - Il **metodo di riferimento** è l'**analisi modale con spettro di risposta** (analisi lineare dinamica), valido
     per comportamenti dissipativi e non; l'azione sismica è lo **spettro di progetto** (§3.2.3.5).
   - L'**analisi lineare statica** (forze laterali) è ammessa **solo** se la risposta, in ogni direzione principale,
     **non dipende significativamente dai modi superiori** (in pratica: costruzioni regolari e sufficientemente basse).

2. **Analisi lineare dinamica / modale (§7.3.3.1)**
   - Determinare i **modi di vibrare**; calcolare gli effetti per ciascun modo; combinarli.
   - Considerare tutti i modi con **massa partecipante > 5%** e un numero di modi con **massa totale ≥ 85%**.
   - Combinare con la **CQC** [7.3.4] (E = √(Σj Σi ρij·Ei·Ej)); tenere conto dell'**eccentricità accidentale** del
     centro di massa (§7.3.3, §7.2.6).

3. **Analisi lineare statica / forze laterali (§7.3.3.2)** — verifica l'applicabilità
   - **T1 ≤ 2,5·TC** (o TD) **e** costruzione **regolare in altezza**. Se non soddisfatta → usare la modale.
   - Se applicabile: **Fh = Sd(T1)·W·λ/g**; **Fi = Fh·zi·Wi/(Σj zj·Wj)** [7.3.7]; **λ = 0,85** se **T1 < 2·TC e ≥ 3
     orizzontamenti**, altrimenti **λ = 1,0**. (Per ≤ 40 m e massa uniforme, T1 = 2·√d [7.3.6].)

4. **Valutazione degli spostamenti (§7.3.3.3)**
   - **dE = ±μd·dEe** [7.3.8], con **μd = q** (T1 ≥ TC) o **μd = 1 + (q−1)·TC/T1** (T1 < TC) [7.3.9]; **μd ≤ 5q−4**.
   - Spostamenti allo **SLC = 1,25 × SLV**. Verificare il **P-Δ (θ)**: se θ ≥ 0,1 amplificare/valutare (θ ≤ 0,3).

5. **Output**: scheda con metodo scelto (modale o statica lineare), esito dell'applicabilità della statica lineare
   (T1≤2,5TC, regolarità), λ e la logica delle forze Fi. Segnala che l'esecuzione dell'analisi e le verifiche restano
   fuori scope.

## Cosa NON fare

- Non **eseguire** l'analisi né calcolare Sd(T1) (è lo spettro §3.2.3.5) o q (§7.3.1): sono ingredienti forniti da
  altre skill/strumenti.
- Non impostare la **pushover**: è nel task `applica-analisi-non-lineare`.
- Non inventare valori: ogni riferimento deve essere rintracciabile in `../references/fonti/ntc2018-par-7-3-2-7-3-4.md`.
