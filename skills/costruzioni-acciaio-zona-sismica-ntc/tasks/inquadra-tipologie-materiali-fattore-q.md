# Task — Inquadra tipologie, materiali e fattore di comportamento (NTC 2018 §7.5.1-7.5.2)

Supporto documentale per inquadrare, per una struttura in acciaio in zona sismica (NTC 2018, DM 17/1/2018,
par. 7.5): le **caratteristiche dei materiali** e il fattore di sovraresistenza γov (§7.5.1), le **tipologie
strutturali** (§7.5.2.1) e i **fattori di comportamento** q0 e αu/α1 (§7.5.2.2). **Non** esegue verifiche né
progetta i collegamenti.

Fonte: `../references/fonti/ntc2018-par-7-5.md`; checklist: `../references/estratti/acciaio-sismica-checklist.md`.

## Input tipico

- Schema strutturale previsto: **telaio (MRF)**, **controventi concentrici** (a diagonale tesa attiva / a V / a K),
  **controventi eccentrici**, **a mensola/pendolo inverso**, misto, ecc.
- Numero di piani e di campate; regolarità in pianta.
- Tipo di **acciaio** previsto (S235, S275, S355, S420, S460) e scelta del comportamento (dissipativo/non).

## Passi

1. **Comportamento e materiali (§7.5, §7.5.1)**
   - Scegli il comportamento: **non dissipativo** (capacità secondo il **§4.2**, senza requisiti aggiuntivi) o
     **dissipativo** (§§ 7.1-7.3 + regole §§ 7.5.3-7.5.6).
   - Verifica che l'acciaio sia conforme al **§11.3.4.9**.
   - Assumi il **fattore di sovraresistenza del materiale γov**: **1,25** per **S235/S275/S355**; **1,15** per
     **S420/S460**.

2. **Tipologie strutturali (§7.5.2.1)**
   - Classifica la struttura tra: a) **intelaiate** (zone dissipative alle estremità delle travi); b) **controventi
     concentrici** — b1 diagonale tesa attiva, b2 a V, **b3 a K (NON dissipativa)**; c) **controventi eccentrici**
     (dissipazione nei traversi per flessione/taglio); d) **a mensola/pendolo inverso**; e) **intelaiate con
     controventi concentrici**; f) **intelaiate con tamponature**.
   - Ricorda le esclusioni: dissipazione con **dispositivi antisismici** (esclusa da questa classificazione);
     forze orizzontali su **nuclei/pareti in c.a.** → **§7.4**. Struttura a un piano con più colonne collegate in
     sommità e **carico assiale normalizzato ≤ 0,3** → assimilabile a **telaio**.

3. **Fattori di comportamento (§7.5.2.2)**
   - **q0** (valore massimo) dalla **Tab. 7.3.II** per tipologia; nel framework generale **q = q0·KR** (§7.3.1).
   - **αu/α1** (strutture regolari in pianta): **1,1** (un piano); **1,2** (telaio più piani, 1 campata); **1,3**
     (telaio più piani, più campate); **1,2** (controventi eccentrici più piani); **1,0** (mensola/pendolo inverso).
   - Nota: i valori di q0 valgono solo se rispettate le regole §§ 7.5.3-7.5.6.

4. **Output**: scheda con comportamento, tipologia strutturale (con eventuale nota «a K non dissipativa»), γov
   adottato, q0 di riferimento (rinvio Tab. 7.3.II) e αu/α1. Segnala che le **verifiche** restano fuori scope.

## Cosa NON fare

- Non eseguire le **verifiche** RES/DUT né calcolare il **q0 numerico** (Tab. 7.3.II): rinvia al progettista.
- Non progettare i **collegamenti**; non trattare i requisiti **statici** (§4.2) né il framework **generale** del
  fattore q (§7.3.1): rinvia alle skill dedicate.
- Non inventare valori: ogni numero deve essere rintracciabile in `../references/fonti/ntc2018-par-7-5.md`.
