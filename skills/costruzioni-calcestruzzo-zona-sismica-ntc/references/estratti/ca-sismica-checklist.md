# Checklist — Costruzioni di calcestruzzo in zona sismica (NTC 2018 §7.4)

Estratto operativo ancorato a `../fonti/ntc2018-par-7-4.md` (NTC 2018, DM 17/1/2018, GU n. 42 del 20/2/2018 —
S.O. n. 8). Ogni valore è tratto dal par. 7.4 letto anche sull'immagine delle pagine PDF 228/229/230.

## 1. Materiali (§7.4.2)

- [ ] Acciaio **B450C**. **B450A** ammesso solo con **Ø 5-10 mm** per reti/tralicci, o come **armatura trasversale**
      se plasticizzazione impedita (gerarchia), elementi secondari (§7.2.3) o comportamento non dissipativo (§7.2.2).

## 2. Tipologia strutturale (§7.4.3.1)

- [ ] **A telaio**: taglio alla base **≥ 65%** del totale affidato ai telai.
- [ ] **A pareti**: taglio alla base **≥ 65%** alle pareti; semplici/composte, **singole/accoppiate**.
- [ ] **Miste telaio-pareti**: **> 50%** azione orizzontale ai telai → **equivalenti a telai**, altrimenti a pareti.
- [ ] **A pendolo inverso**: **≥ 50% massa** nel terzo superiore. Monopiano intelaiata: **N ≤ 30%** resistenza cls.
- [ ] **Deformabili torsionalmente**: **r²/ls² ≥ 1** (ls² = (L²+B²)/12). **Pareti estese debolmente armate**:
      periodo **≤ TC**, solo **CD"B"**.

## 3. Fattore di comportamento e classe di duttilità (§7.4.3.2)

- [ ] **q** calcolato secondo **§7.3.1 e Tab. 7.3.II** (skill `fattore-comportamento-q-sismica-ntc`).
- [ ] **Pareti accoppiate** se il momento base è equilibrato **≥ 20%** dalla coppia degli sforzi verticali.
- [ ] **αu/α1** — telai: **1,1** (1 piano) / **1,2** (più piani, 1 campata) / **1,3** (più piani e campate); pareti:
      **1,0** (due pareti non accoppiate) / **1,1** (altre non accoppiate) / **1,2** (accoppiate o miste equiv. pareti).
- [ ] Scelta **CD"A"/CD"B"**: pareti in CD"A" o CD"B"; pareti estese debolmente armate solo CD"B"; telai con **travi a
      spessore** → CD"B" (salvo secondari). **q > 1,5** per altre tipologie → analisi non lineari.

## 4. Gerarchia delle resistenze — verifiche RES/DUT (§7.4.4)

- [ ] Verifiche **RES + DUT** degli elementi primari (§7.3.6.1); **γRd** da **Tab. 7.2.I**; fondazioni §7.2.5;
      secondari §7.2.3.
- [ ] **Travi — taglio**: domanda da equilibrio della trave incernierata + **capacità flessionale amplificata di
      γRd**. CD"B" capacità a taglio §4.1.2.3.5. CD"A": ctgθ=1; se rapporto domande min/max **< −0,5** e supera
      **VR1 = (2 − |VEd,min|/VEd,max)·fctd·bw·d** [7.4.1] → armature **±45°**, **VEd,max ≤ As·fyd/√2** [7.4.2].
- [ ] **Travi — duttilità**: **μφ = 1,2·(2q0 − 1)** (T1 ≥ TC) o **μφ = 1,2·(1 + 2(q0 − 1)·TC/T1)** (T1 < TC) [7.4.3];
      **μφ = 2μd − 1**.
- [ ] **Pilastri — pressoflessione**: domanda a compressione **≤ 55% (CD"A") / 65% (CD"B")** della capacità a
      compressione del **solo cls**.
- [ ] **Nodo (pilastro forte-trave debole)**: **ΣMc,Rd ≥ γRd · ΣMb,Rd** [7.4.4] (escluso sommità ultimo
      orizzontamento). **Pilastri — taglio**: dalla gerarchia (momenti resistenti alle estremità amplificati di γRd).

## 5. Dettagli costruttivi e fuori scope

- [ ] **Dettagli costruttivi** (§7.4.6) di travi/pilastri/nodi/pareti differenziati CD"A"/CD"B" (zone critiche,
      armature, confinamento): il **dettaglio numerico** resta nella norma.
- [ ] **Fuori scope**: progetto ordinario non sismico (§4.1); dettaglio delle verifiche complete (§7.4.4) e dei limiti
      geometrici/di armatura (§7.4.6); le altre skill sismiche per materiale (§7.5-7.9).
