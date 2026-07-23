# Task: inquadra-effetti-dinamici-azioni-orizzontali

Inquadra gli **effetti dinamici** (coefficienti Φ2/Φ3, lunghezza caratteristica L_φ) e le **azioni
orizzontali** (centrifuga, serpeggio, avviamento/frenatura) del traffico ferroviario secondo le **NTC 2018
par. 5.2.2.2.3-5.2.2.3**. Supporto documentale: **non** esegue analisi né verifiche.

## Quando usarla

Il progettista ha definito i modelli di carico verticali (vedi
`inquadra-modelli-carico-verticali-ferroviari`) e deve tenerne conto degli effetti dinamici e delle azioni
orizzontali.

## Passi

1. **Campo di applicazione degli effetti dinamici** (§5.2.2.2.3): per usuali tipologie di ponti e **velocità ≤
   200 km/h**, con frequenza propria dentro il **fuso** di Fig. 5.2.7, si usano i **coefficienti dinamici Φ**;
   per **V > 200 km/h**, frequenza fuori dal fuso o **tipologie non convenzionali** (strallati, sospesi,
   grande luce…) → **analisi dinamica con convogli reali**. Fuso: n_0 = 94,76·L^(−0,748) [5.2.2] (sup.);
   n_0 = 80/L (4-20 m) [5.2.3] e n_0 = 23,58·L^(−0,592) (20-100 m) [5.2.4] (inf.); trave appoggiata
   n_0 = 17,75/√δ0 [5.2.5].

2. **Coefficienti dinamici Φ** (§5.2.2.2.3), con **L_φ** lunghezza caratteristica (Tab. 5.2.II):
   - linee con **elevato** standard manutentivo: **Φ2 = 1,44 / (√L_φ − 0,2) + 0,82**, con **1,00 ≤ Φ2 ≤ 1,67**
     [5.2.6];
   - linee con **ridotto** standard manutentivo: **Φ3 = 2,16 / (√L_φ − 0,2) + 0,73**, con **1,00 ≤ Φ3 ≤ 2,00**
     [5.2.7].
   Φ **non** si applica al **treno scarico** né ai **treni reali**. Per armamento diretto si aggiunge λ (1,0
   per L_φ ≤ 8 m ed L_φ > 90 m; 1,1 per 8 < L_φ ≤ 90 m); per copertura h > 1,0 m si riduce (Φ_rid [5.2.8]);
   per pile snelle (λ ≤ 30), spalle, fondazioni, muri → Φ = 1.

3. **Forza centrifuga** (§5.2.2.3.1): per binario in curva, verso l'esterno, applicata a **1,80 m** sopra il
   P.F.; con i modelli SW si assume **V = 100 km/h**. Valore caratteristico [5.2.9]:
   **Q_tk = (V²/(127·r))·f·α·Q_vk** (analogamente q_tk), con **f** fattore di riduzione [5.2.10] (**f = 1** per
   V ≤ 120 km/h o L_f ≤ 2,88 m); **non** incrementata da Φ.

4. **Azione laterale (serpeggio)** (§5.2.2.3.2): forza concentrata orizzontale **Q_sk = 100 kN**, applicata
   alla sommità della rotaia più alta, perpendicolare all'asse del binario; ×α se α > 1, **non** ×Φ; sempre
   combinata con i carichi verticali.

5. **Avviamento e frenatura** (§5.2.2.3.3): forze longitudinali distribuite su una lunghezza L:
   - **avviamento**: **Q_la,k = 33 kN/m · L ≤ 1000 kN** (LM71, SW/0, SW/2);
   - **frenatura**: **Q_lb,k = 20 kN/m · L ≤ 6000 kN** (LM71, SW/0); **Q_lb,k = 35 kN/m · L** (SW/2).
   Da moltiplicare per **α**, **non** per Φ; per il treno scarico si trascurano; ponti a doppio binario: due
   treni in versi opposti (uno in avviamento, l'altro in frenatura).

Usa la checklist in `../references/estratti/azioni-ferroviari-checklist.md` (sezioni 2 e 3).

## Output atteso

Un inquadramento degli effetti dinamici (coefficienti Φ2/Φ3, campo di applicazione, L_φ) e delle azioni
orizzontali (centrifuga, serpeggio, avviamento/frenatura) con i valori caratteristici e le regole di
combinazione (×α, non ×Φ), con **rinvio ai paragrafi/formule** NTC. Nessuna analisi né verifica.

## Cosa NON fare

- Non **eseguire** l'analisi dinamica con treni reali né calcolare numericamente le sollecitazioni.
- Non **riprodurre** la Tab. 5.2.II completa (L_φ per ogni elemento) né eseguire le combinazioni/verifiche.
