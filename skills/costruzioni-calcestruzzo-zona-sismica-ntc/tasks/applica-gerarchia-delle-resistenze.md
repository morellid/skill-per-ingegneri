# Task — Applica la gerarchia delle resistenze a travi, pilastri e nodi (NTC 2018 §7.4.4)

Supporto documentale per impostare la **progettazione in capacità** (gerarchia delle resistenze) degli elementi in
c.a. — travi, pilastri, nodi — secondo le NTC 2018 (DM 17/1/2018), §7.4.4. **Non** esegue le verifiche numeriche di
dettaglio.

Fonte: `../references/fonti/ntc2018-par-7-4.md`; checklist: `../references/estratti/ca-sismica-checklist.md`.

## Input tipico

- Classe di duttilità (CD"A"/CD"B") e fattore di comportamento q0 (dal task `inquadra-tipologie-e-fattore-comportamento`).
- Capacità flessionali di progetto (Mb,Rd, Mc,Rd) di travi e pilastri ai nodi.

## Passi

1. **Impostazione generale (§7.4.4)**
   - Le verifiche riguardano gli **elementi primari** delle strutture in elevazione, con **verifiche di resistenza
     (RES) e di duttilità (DUT)** (§7.3.6.1).
   - I **fattori di sovraresistenza γRd** da usare nella progettazione in capacità sono nella **Tab. 7.2.I**.
   - Per le fondazioni vale il §7.2.5; per gli elementi secondari il §7.2.3.

2. **Travi (§7.4.4.1)**
   - **Flessione (RES)**: capacità come §4.1.2.3.4, con la larghezza collaborante della soletta (Fig. 7.4.1).
   - **Taglio (gerarchia)**: la domanda a taglio si ottiene dall'equilibrio della trave incernierata agli estremi,
     soggetta ai carichi gravitazionali e alla **capacità flessionale di progetto amplificata di γRd** (Tab. 7.2.I).
     In **CD"B"** la capacità a taglio è come §4.1.2.3.5; in **CD"A"** ctgθ=1 nelle zone dissipative e, se il rapporto
     tra domande a taglio min/max è **< −0,5** e supera **VR1 = (2 − |VEd,min|/VEd,max)·fctd·bw·d** [7.4.1], si
     dispongono **armature diagonali ±45°** con **VEd,max ≤ As·fyd/√2** [7.4.2].
   - **Duttilità (DUT)**: fattore di duttilità in curvatura richiesto **μφ = 1,2·(2q0 − 1)** (T1 ≥ TC) o **μφ =
     1,2·(1 + 2(q0 − 1)·TC/T1)** (T1 < TC) [7.4.3]; relazione **μφ = 2μd − 1**.

3. **Pilastri (§7.4.4.2)**
   - **Pressoflessione (RES)**: la domanda a compressione non deve eccedere il **55% (CD"A") / 65% (CD"B")** della
     capacità massima a compressione della sezione di **solo calcestruzzo**, per tutte le combinazioni.
   - **Gerarchia (pilastro forte-trave debole)**: per ogni nodo trave-pilastro (escluso la sommità dell'ultimo
     orizzontamento) deve valere **ΣMc,Rd ≥ γRd · ΣMb,Rd** [7.4.4], con γRd da Tab. 7.2.I.
   - **Taglio**: la domanda deriva dalla gerarchia (momenti resistenti alle estremità amplificati di γRd).

4. **Nodi trave-pilastro (§7.4.4.3)**: verifiche di resistenza del nucleo del nodo (taglio, confinamento) secondo la
   norma.

5. **Output**: schema della catena gerarchica (flessione trave → taglio trave; nodo pilastro forte-trave debole →
   taglio pilastro) con i fattori γRd e i limiti (55%/65%, [7.4.4]). Segnala che i **valori numerici completi** delle
   verifiche e i **dettagli costruttivi** (§7.4.6) sono nella norma.

## Cosa NON fare

- Non eseguire le **verifiche numeriche complete** né dimensionare le armature; non riprodurre i **dettagli
  costruttivi** (§7.4.6).
- Non applicare la gerarchia agli **elementi secondari** (§7.2.3) o alle strutture **non dissipative** (regole CD"B").
- Non inventare valori/formule: ogni riferimento deve essere rintracciabile in `../references/fonti/ntc2018-par-7-4.md`.
