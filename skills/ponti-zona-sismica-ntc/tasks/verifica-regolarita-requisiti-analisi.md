# Task — Verifica regolarità e requisiti dell'analisi (NTC 2018 §7.9.2.1, §7.9.3-7.9.4.1)

Supporto documentale per verificare la **regolarità** di un ponte (fattore KR) e i **requisiti** per il modello e
l'**analisi statica lineare** secondo il par. 7.9 delle NTC 2018 (DM 17/1/2018). **Non** sostituisce le verifiche
di duttilità/resistenza.

Fonte: `../references/fonti/ntc2018-par-7-9.md`; checklist: `../references/estratti/ponti-sismica-checklist.md`.

## Input tipico

- Per ogni pila del sistema resistente al sisma nella direzione considerata: **MEd,i** (momento alla base dalla
  combinazione sismica) e **MRd,i** (momento resistente); q0 adottato.
- Schema (isostatico / travata continua), geometria (obliquità φ, rapporto B/L, curvatura), simmetria/eccentricità.
- Masse: **massa efficace** di ciascuna pila e **massa dell'impalcato** portata.

## Passi

1. **Regolarità e KR (§7.9.2.1)**
   - Per ciascun elemento duttile calcola **ri = q0·MEd,i/MRd,i**.
   - Calcola **r̃ = ri,max/ri,min** sulle pile del sistema resistente nella direzione considerata (si possono
     escludere le pile con resistenza a taglio ≤ **20%** della resistenza totale / n. elementi).
   - Se **r̃ < 2** → geometria **regolare**, **KR = 1**. Se **r̃ ≥ 2** → **KR = 2/r̃** [7.9.2], comunque
     **q = q0·KR ≥ 1**.
   - Ponti a **geometria irregolare** (obliquità > 45°, raggio di curvatura molto ridotto): **q = 1,5**; valori
     maggiori, comunque **≤ 3,5**, solo con **analisi non lineare**.

2. **Modello strutturale (§7.9.3)**
   - **Eccentricità accidentale** (§7.2.6): **0,03 volte** la dimensione dell'impalcato ⊥ all'azione sismica.
   - Se **obliquità φ > 20°** o **B/L > 2,0**: attenzione ai **moti rigidi** attorno all'asse verticale.
   - Rigidezza degli elementi in c.a. secondo l'effettivo **stato di fessurazione**.

3. **Analisi statica lineare (§7.9.4.1)** — ammessa se:
   - a) in entrambe le direzioni, per **travate appoggiate**, massa efficace di ciascuna pila **≤ 1/5** della
     massa dell'impalcato da essa portata;
   - b) direzione **longitudinale**, ponti rettilinei a travata continua, massa efficace complessiva delle pile
     **≤ 1/5** della massa dell'impalcato;
   - c) direzione **trasversale**, se soddisfatta la b) e simmetria rispetto alla mezzeria o **eccentricità ≤ 5%**
     della lunghezza del ponte.
   - Con metodi lineari, incremento flettente per non linearità geometriche **ΔM = dEd·NEd** [7.9.3].

4. **Output**: valore di r̃ e KR (o q per ponti irregolari), esito dei requisiti di modello (eccentricità 0,03,
   obliquità/B-L) ed esito di ammissibilità dell'analisi statica lineare. Segnala che è un inquadramento, non una
   verifica di resistenza.

## Cosa NON fare

- Non confondere la **regolarità** (KR) e i requisiti dell'**analisi** con le **verifiche** di duttilità/
  resistenza delle pile (fuori scope).
- Non applicare l'analisi statica lineare fuori dai casi a)/b)/c); non adottare q > 1,5 per ponti irregolari senza
  analisi non lineare.
- Non inventare valori: ogni limite deve essere rintracciabile in `../references/fonti/ntc2018-par-7-9.md`.
