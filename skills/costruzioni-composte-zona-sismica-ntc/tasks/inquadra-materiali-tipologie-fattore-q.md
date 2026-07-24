# Task — Inquadra comportamenti, materiali, tipologie e fattore di comportamento (NTC 2018 §7.6-7.6.3)

Supporto documentale per inquadrare, per una struttura composta acciaio-calcestruzzo in zona sismica (NTC 2018,
DM 17/1/2018, par. 7.6): i **comportamenti** (§7.6), le **caratteristiche dei materiali** (§7.6.1), le **tipologie
strutturali** e i **fattori di comportamento** q0 (§7.6.2) e la **rigidezza** della sezione composta (§7.6.3).
**Non** esegue verifiche né progetta i collegamenti.

Fonte: `../references/fonti/ntc2018-par-7-6.md`; checklist: `../references/estratti/composte-sismica-checklist.md`.

## Input tipico

- Schema strutturale previsto: **telaio**, **controventi concentrici** (in acciaio), **controventi eccentrici**,
  **mensola/pendolo inverso**, **intelaiato controventato**; presenza di pareti/nuclei in c.a.
- Materiali previsti: **classe del calcestruzzo**, **acciaio per c.a.** (B450C/B450A), **acciaio strutturale**.
- Comportamento scelto: non dissipativo / dissipativo (con zone dissipative in membrature composte o in acciaio).

## Passi

1. **Comportamento (§7.6)**
   - Scegli tra: **a) non dissipativo** (capacità secondo il **§4.3**, senza requisiti aggiuntivi); **b)
     dissipativo** con zone dissipative in **membrature composte**; **c) dissipativo** con zone dissipative in
     **acciaio** (con misure per prevenire il contributo del cls e garantire l'integrità del cls compresso).

2. **Materiali (§7.6.1)**
   - **Calcestruzzo**: non ammesso **< C20/25 o LC20/22**; non consentito **> C40/50 o LC40/44**.
   - **Acciaio per c.a.**: **B450C** (§11.3.2.1); **B450A** solo nei casi del §7.4.2.2.
   - **Acciaio strutturale**: qualità di cui al **§7.5** e **§11.3.4**.

3. **Tipologie e fattori di comportamento (§7.6.2)**
   - Classifica la tipologia (funzionamento §7.5.2): **a) intelaiate**; **b) controventi concentrici in acciaio**;
     **c) controventi eccentrici** (connessioni in acciaio); **d) mensola/pendolo inverso**; **e) intelaiate
     controventate**. Se la resistenza è affidata a **pareti/nuclei in c.a.** → **§7.4**.
   - **q0** (valore massimo) dalla **Tab. 7.3.II** (con prescrizioni §7.5.2); nel framework generale **q = q0·KR**.

4. **Rigidezza della sezione composta (§7.6.3)**
   - **Cls compresso**: coefficiente di omogeneizzazione **n = Ea/Ecm = 7**; momento d'inerzia **non fessurato I1**
     (include la soletta nella larghezza efficace, §7.6.5.1).
   - **Cls teso**: momento d'inerzia **fessurato I2** (cls non reagente; attive solo profilo e armatura).

5. **Output**: scheda con comportamento, esito requisiti materiali (classi cls e acciaio), tipologia, q0 di
   riferimento (rinvio Tab. 7.3.II) e coefficiente n per la rigidezza. Segnala che le **verifiche** restano fuori
   scope.

## Cosa NON fare

- Non eseguire le **verifiche** di dettaglio RES/DUT né calcolare il **q0 numerico** (Tab. 7.3.II).
- Non progettare i **collegamenti**; non trattare i requisiti **statici** (§4.3), le regole sismiche dell'acciaio
  (§7.5) né il framework del fattore q (§7.3.1): rinvia alle skill dedicate.
- Non inventare valori: ogni numero deve essere rintracciabile in `../references/fonti/ntc2018-par-7-6.md`.
