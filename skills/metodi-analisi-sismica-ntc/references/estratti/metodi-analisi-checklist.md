# Checklist — Metodi di analisi sismica (NTC 2018 §7.3.2-7.3.4)

Estratto operativo ancorato a `../fonti/ntc2018-par-7-3-2-7-3-4.md` (NTC 2018, DM 17/1/2018, GU n. 42 del 20/2/2018 —
S.O. n. 8). Ogni valore è tratto dai parr. 7.3.2-7.3.4 letti anche sull'immagine delle pagine PDF 222/223/224.

## 1. Scelta del metodo (§7.3.2)

- [ ] **Metodo di riferimento**: **analisi modale con spettro di risposta** (analisi lineare dinamica), per
      comportamenti dissipativi e non; spettro di progetto §3.2.3.5.
- [ ] **Analisi lineare statica** (forze laterali): ammessa **solo** se la risposta, in ogni direzione principale,
      **non dipende significativamente dai modi superiori**.
- [ ] **Analisi non lineare**: dinamica (storie temporali) o statica (forze crescenti monotone).

## 2. Analisi lineare dinamica / modale (§7.3.3.1)

- [ ] Considerare tutti i modi con **massa partecipante > 5%** e un numero di modi con **massa totale ≥ 85%**.
- [ ] Combinazione **CQC** [7.3.4]: E = √(Σj Σi ρij·Ei·Ej), con ρij funzione di ξ e βij = Tj/Ti.
- [ ] Tenere conto dell'**eccentricità accidentale** del centro di massa (§7.3.3, momenti torcenti; §7.2.6).

## 3. Analisi lineare statica / forze laterali (§7.3.3.2)

- [ ] **Applicabilità**: **T1 ≤ 2,5·TC** (o TD) **e** costruzione **regolare in altezza**.
- [ ] Stima di T1 (≤ 40 m, massa uniforme): **T1 = 2·√d** [7.3.6] (d = spostamento elastico del punto più alto, m).
- [ ] **Fh = Sd(T1)·W·λ/g**; **Fi = Fh·zi·Wi/(Σj zj·Wj)** [7.3.7].
- [ ] **λ = 0,85** se **T1 < 2·TC e ≥ 3 orizzontamenti**, altrimenti **λ = 1,0**.

## 4. Spostamenti (§7.3.3.3)

- [ ] **dE = ±μd·dEe** [7.3.8], con **μd = q** (T1 ≥ TC) o **μd = 1 + (q−1)·TC/T1** (T1 < TC) [7.3.9]; **μd ≤ 5q−4**.
- [ ] Spostamenti allo **SLC = 1,25 × SLV** (in assenza di valutazioni più accurate).
- [ ] **P-Δ (θ)**: θ = (P·dEr)/(V·h) [7.3.3]; trascurabile se **θ < 0,1**; amplificazione **1/(1−θ)** se 0,1–0,2;
      analisi non lineare se 0,2–0,3; **θ ≤ 0,3**.

## 5. Analisi non lineare (§7.3.4)

- [ ] Usabile per: spostamenti, verifiche di duttilità SLC, domanda inelastica, valutazione αu/α1, progetto nuovi,
      capacità esistenti.
- [ ] **Non lineare dinamica** (§7.3.4.1): integrazione al passo con storie temporali (§3.2.3.6); **confronto con
      analisi modale**; obbligatoria per isolamento non lineare-equivalente (§7.10.5.2).
- [ ] **Non lineare statica / pushover** (§7.3.4.2): sistema equivalente; forze orizzontali risultante **Fb**; punto
      di controllo al **centro di massa dell'ultimo livello** (esclusi torrini); curva di capacità **Fb–dc**.
- [ ] Pushover: **almeno 2 distribuzioni** (una Gruppo 1 + una Gruppo 2). **Gruppo 1**: modo fondamentale **≥ 75%** →
      forze statiche o forma modale; distribuzione modale (modi **≥ 85%**) **obbligatoria se T1 > 1,3·TC**. **Gruppo
      2**: a) uniforme, b) adattiva, c) multimodale (**≥ 6 modi**).

## 6. Fuori scope

- [ ] Fattore di comportamento q e scelta lineare/non lineare (§7.3.1); formula di T1 (skill dedicata); criteri di
      modellazione (§7.2.6); combinazione componenti (§7.3.5); spettro di progetto (§3.2.3.5); verifiche SLU/SLE.
