# Checklist — Azioni da traffico sui ponti ferroviari (NTC 2018 §5.2.2)

Estratto operativo ancorato a `../fonti/ntc2018-par-5-2.md` (NTC 2018, DM 17/1/2018, GU n. 42 del 20/2/2018 —
S.O. n. 8). Ogni valore è tratto dal testo del par. 5.2.2 letto anche sull'immagine delle pagine PDF 168 e 171.

## 1. Modelli di carico verticali (§5.2.2.2.1)

- [ ] **LM 71**: **4 assi da Q_vk = 250 kN** a interasse **1,60 m** + **q_vk = 80 kN/m** distribuito (da 0,8 m
      dagli assi d'estremità, lunghezza illimitata). Eccentricità dal rapporto **Q_V2/Q_V1 = 1,25** [5.2.1] = s/18
      (s = 1435 mm). **α = 1,1** (ferrovie ordinarie).
- [ ] **SW/0** (traffico normale, travi continue): **q_vk = 133 kN/m**, **a = 15,0 m**, **c = 5,3 m**; **α = 1,1**.
- [ ] **SW/2** (traffico pesante): **q_vk = 150 kN/m**, **a = 25,0 m**, **c = 7,0 m**; **α = 1,0** (Tab. 5.2.I).
- [ ] **Treno scarico**: **10,0 kN/m**.
- [ ] **Marciapiedi**: **10 kN/m²** (non contemporaneo ai convogli, senza incremento dinamico).
- [ ] Ripartizione locale: **25% / 50% / 25%** su tre traverse; solette a **45°**. Rilevati a tergo spalle: **3,0 m**.

## 2. Effetti dinamici (§5.2.2.2.3)

- [ ] **V ≤ 200 km/h** e frequenza propria nel «fuso» (Fig. 5.2.7) → coefficiente dinamico **Φ**. Altrimenti
      (V > 200 km/h, fuori fuso, tipologie non convenzionali) → **analisi dinamica con convogli reali**.
- [ ] Fuso frequenze n_0 [Hz]: sup. **n_0 = 94,76·L^(−0,748)** [5.2.2]; inf. **n_0 = 80/L** (4-20 m) [5.2.3] e
      **n_0 = 23,58·L^(−0,592)** (20-100 m) [5.2.4]; trave appoggiata **n_0 = 17,75/√δ0** [5.2.5].
- [ ] **Φ2 = 1,44 / (√L_φ − 0,2) + 0,82**, con **1,00 ≤ Φ2 ≤ 1,67** [5.2.6] — elevato standard manutentivo.
- [ ] **Φ3 = 2,16 / (√L_φ − 0,2) + 0,73**, con **1,00 ≤ Φ3 ≤ 2,00** [5.2.7] — ridotto standard manutentivo.
- [ ] **L_φ** = lunghezza caratteristica (Tab. 5.2.II). Φ **non** su treno scarico e treni reali. Coeff. λ per
      armamento diretto (1,0 / 1,1); Φ_rid per copertura h > 1,0 m; Φ = 1 per pile snelle/spalle/fondazioni.

## 3. Azioni orizzontali (§5.2.2.3)

- [ ] **Forza centrifuga** [5.2.9]/[5.2.10]: verso l'esterno curva, a **1,80 m** sul P.F.; con SW a **V = 100 km/h**;
      **f** ridutt. (f = 1 per V ≤ 120 km/h o L_f ≤ 2,88 m); **non** incrementata da Φ.
- [ ] **Serpeggio**: **Q_sk = 100 kN** (concentrata, orizzontale; ×α se α > 1; **non** ×Φ).
- [ ] **Avviamento**: **Q_la,k = 33 kN/m · L ≤ 1000 kN** (LM71, SW/0, SW/2).
- [ ] **Frenatura**: **Q_lb,k = 20 kN/m · L ≤ 6000 kN** (LM71, SW/0); **35 kN/m · L** (SW/2). ×α, **non** ×Φ.

## 4. Fuori scope

- [ ] Criteri progettuali/manutentivi (§5.2.1); **combinazioni** delle azioni; **analisi dinamica** con treni
      reali; Tab. 5.2.II completa; **verifiche** (SLU/SLE, fatica, interazione statica binario-struttura).
