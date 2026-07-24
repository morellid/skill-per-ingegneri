# Task — Inquadra criteri e fattore di comportamento (NTC 2018 §7.9.1-7.9.2.1)

Supporto documentale per inquadrare, per un ponte in zona sismica (NTC 2018, DM 17/1/2018, par. 7.9): il **campo
di applicazione** (§7.9.1), i **criteri generali** di progettazione dissipativo/non dissipativo (§7.9.2) e i
**valori del fattore di comportamento** q0, νk, λ(α) (§7.9.2.1). **Non** esegue verifiche né progetta i dettagli.

Fonte: `../references/fonti/ntc2018-par-7-9.md`; checklist: `../references/estratti/ponti-sismica-checklist.md`.

## Input tipico

- Schema del ponte: **travate continue su più pile** o **semplicemente appoggiate**; tipo di **pile** (fusto
  unico, sezione piena/cava, portale).
- Materiale delle pile: **c.a.**, c.a.p., carpenteria metallica; scelta del comportamento (dissipativo/non).
- Per le pile duttili in c.a.: sforzo normale di progetto **NEd**, area **Ac** e resistenza **fck** (per νk).

## Passi

1. **Campo di applicazione (§7.9.1)**
   - Verifica che il ponte sia **a pile e travate** con **pile a fusto unico** (anche portale). Pile a geometria
     complessa (telaio spaziale) richiedono criteri specifici; per tipologie diverse i q0 restano quelli della
     **Tab. 7.3.II**.

2. **Criteri generali (§7.9.2)**
   - **Non dissipativo**: capacità secondo il **Cap. 4**; per il c.a. nessuna sezione oltre la **curvatura di
     prima plasticizzazione** (§7.4.4.1.2), per c.a.p./acciaio nessun materiale oltre lo **snervamento**.
   - **Dissipativo**: meccanismo dissipativo **stabile** con **dissipazione limitata alle pile**; comportamento
     inelastico **flessionale**, **esclusa la rottura per taglio**; impegnare il maggior numero di pile; zone
     dissipative **accessibili**.
   - **Pali di fondazione**: sollecitazioni sismiche **divise per 1,5**, con dettagli **CD "B"** per **10 diametri**.
   - Capacità delle sezioni c.a. con **confinamento** considerando la **perdita dei copriferri** (0,35%).
   - Elementi sempre **elastici** (progettazione in capacità): **impalcato, apparecchi di appoggio, fondazioni,
     spalle**, pile che non scambiano azioni orizzontali con l'impalcato.

3. **Valori del fattore di comportamento (§7.9.2.1)**
   - **Non dissipativo**: **q0 = 1,0** (due componenti orizzontali).
   - **Dissipativo**: q0 max da **Tab. 7.3.II**; **λ(α) = 1 se α ≥ 3**, **λ(α) = (α/3)^0,5 se 3 > α ≥ 1** (α = L/H).
   - Elementi duttili in **c.a.**: q0 valido solo se **νk = NEd/(Ac·fck) ≤ 0,3**; comunque **νk ≤ 0,6**. Per
     **0,3 < νk < 0,6**: **q0(νk) = q0 − [(νk/0,3) − 1]·(q0 − 1)** [7.9.1].

4. **Output**: scheda con comportamento, localizzazione della dissipazione (pile), q0 di riferimento (rinvio Tab.
   7.3.II) ed eventuale riduzione per νk. Segnala che le **verifiche** e i dettagli restano fuori scope.

## Cosa NON fare

- Non eseguire le **verifiche** di duttilità/resistenza delle pile né calcolare il **q0 numerico** (Tab. 7.3.II).
- Non progettare i **dettagli costruttivi** (§7.9.6); non trattare i **carichi da traffico** (§§ 5.1.3/5.2.2) né
  il framework del fattore q per gli edifici (§7.3.1): rinvia alle skill dedicate.
- Non inventare valori: ogni numero deve essere rintracciabile in `../references/fonti/ntc2018-par-7-9.md`.
