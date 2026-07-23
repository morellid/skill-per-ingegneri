# Task — Inquadra materiali e fattori di comportamento (NTC 2018 §7.8.1.1-7.8.1.3)

Supporto documentale per inquadrare, per un edificio in muratura in zona sismica (NTC 2018, DM 17/1/2018,
par. 7.8.1): la **premessa** e la classe di duttilità (§7.8.1.1), i **requisiti dei materiali** (§7.8.1.2) e i
**fattori di comportamento** αu/α1 (§7.8.1.3). **Non** esegue verifiche dei pannelli né progetta l'armatura.

Fonte: `../references/fonti/ntc2018-par-7-8-1.md`; checklist: `../references/estratti/muratura-sismica-checklist.md`.

## Input tipico

- Tipologia di muratura prevista: **ordinaria / armata / confinata**.
- Elementi resistenti: pietra squadrata o elementi artificiali (percentuale di vuoti, resistenze f_bk / f_b).
- Malta di allettamento prevista (classe/resistenza media).
- Accelerazione di sito allo SLV: **agS** (per capire se valgono le eccezioni/limiti per agS ≤ 0,075g o ≤ 0,15g).
- Eventuale uso di giunti sottili o giunti verticali non riempiti.

## Passi

1. **Premessa / duttilità (§7.8.1.1)**
   - Ricorda che, nel rispetto dei §§ 4.5 e 11.10, le costruzioni di muratura sono **moderatamente dissipative**
     → classe di duttilità **CD"B"**.
   - I **coefficienti parziali di sicurezza** per la resistenza del materiale (Cap. 4) possono essere **ridotti
     del 20%** e comunque **fino a un valore non inferiore a 2**.

2. **Requisiti dei materiali (§7.8.1.2)** — oltre a quelli del §4.5.2 e, **salvo agS ≤ 0,075g**:
   - **percentuale volumetrica dei vuoti ≤ 45%**; setti paralleli al piano del muro **continui e rettilinei**;
   - **f_bk (direzione portante, area lorda) ≥ 5 MPa** oppure **f_b (media normalizzata) ≥ 6 MPa**;
   - **f_bk (direzione perpendicolare, nel piano parete) ≥ 1,5 MPa**;
   - **malta di allettamento (muratura ordinaria) ≥ 5 MPa** (M5);
   - **giunti sottili** (0,5-3 mm): solo agS ≤ 0,15g, con altezza ≤ 10,5 m (agS≤0,075g) / 7 m (0,075-0,15g) e
     piani ≤ 3 / ≤ 2; **giunti verticali non riempiti**: solo agS ≤ 0,075g, ≤ 2 piani, h ≤ 7 m;
   - elementi con giunti sottili/secco: **setti interni ≥ 7 mm**, **esterni ≥ 10 mm**, **foratura ≤ 55%**;
   - muratura di **pietra non squadrata/listata**: solo agS ≤ 0,075g.

3. **Fattori di comportamento (§7.8.1.3)**
   - q0 (valore di base) da **Tab. 7.3.II**; si assume sempre **q = q0·KR** (KR al §7.3.1).
   - Il rapporto di sovraresistenza **αu/α1** si ricava da analisi statica non lineare (§7.3.4.2) e **non può
     superare 2,5**. In assenza di analisi non lineare, valori forfettari:
     **ordinaria 1,7**; **armata 1,5** (**1,3** con progettazione in capacità); **confinata 1,6** (**1,3** con
     progettazione in capacità).

4. **Output**: scheda con classe di duttilità, esito requisiti materiali (rispettati / non rispettati, con il
   valore mancante), αu/α1 adottato e rinvio ai paragrafi/tabelle. Segnala sempre che le **verifiche** dei
   pannelli restano fuori scope (§§ 7.8.2-7.8.4).

## Cosa NON fare

- Non eseguire le **verifiche** dei pannelli (pressoflessione/taglio) né i **metodi di analisi** (§7.8.1.5).
- Non progettare l'**armatura** né i dettagli; non trattare i requisiti **statici** (§4.5) né il framework
  **generale** del fattore q (§7.3.1): rinvia alle skill dedicate.
- Non inventare valori: ogni numero deve essere rintracciabile in `../references/fonti/ntc2018-par-7-8-1.md`.
