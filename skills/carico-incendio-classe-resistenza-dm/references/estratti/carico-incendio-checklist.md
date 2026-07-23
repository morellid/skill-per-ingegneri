# Checklist — Carico d'incendio specifico di progetto e classe di resistenza al fuoco (DM 9 marzo 2007)

Estratto operativo ancorato a `../fonti/dm-9-3-2007.md` (DM 9 marzo 2007, G.U. S.G. n. 74 del 29/3/2007
— S.O. n. 87). Ogni valore è tratto dal testo/tabelle del DM letti sull'immagine delle pagine.

## 1. Carico d'incendio specifico q_f (punto 1)

- [ ] Carico d'incendio: **q = Σ_i g_i·H_i·m_i·ψ_i** [MJ].
- [ ] `g_i` massa del combustibile [kg]; `H_i` potere calorifico inferiore [MJ/kg] (**UNI EN ISO 1716:2002**).
- [ ] Fattore di partecipazione **m_i**: **0,80** legno/materiali cellulosici; **1,00** altri combustibili.
- [ ] Fattore di limitazione **ψ_i**: **0** contenitori progettati per resistere al fuoco; **0,85** contenitori
      non combustibili non progettati; **1** altri casi.
- [ ] Carico d'incendio specifico: **q_f = q / A** [MJ/m²], con `A` superficie in pianta lorda del compartimento.

## 2. Carico d'incendio specifico di progetto q_f,d (punto 2)

- [ ] **q_f,d = δ_q1 · δ_q2 · δ_n · q_f** [MJ/m²].
- [ ] **δ_q1** (Tabella 1, per superficie A [m²]): A<500 → **1,00**; 500≤A<1.000 → **1,20**;
      1.000≤A<2.500 → **1,40**; 2.500≤A<5.000 → **1,60**; 5.000≤A<10.000 → **1,80**; A≥10.000 → **2,00**.
- [ ] **δ_q2** (Tabella 2, per classe di rischio): I basso → **0,80**; II moderato → **1,00**; III alto → **1,20**.
- [ ] **δ_n = Π_i δ_ni** (Tabella 3, solo misure presenti): estinzione automatica **ad acqua 0,60** / **altro 0,80**;
      evacuazione fumo/calore **0,90**; rivelazione/allarme **0,85**; squadra aziendale **0,90**; rete idrica
      **interna 0,90** / **interna+esterna 0,80**; percorsi protetti **0,90**; accessibilità mezzi VVF **0,90**.

## 3. Livelli di prestazione e classi (punto 3)

- [ ] Livelli: **I** nessun requisito (NON ammesso nel campo di applicazione); **II** evacuazione occupanti;
      **III** gestione dell'emergenza; **IV** limitato danneggiamento; **V** totale funzionalità.
- [ ] Classi (minuti): **15, 20, 30, 45, 60, 90, 120, 180, 240, 360**.
- [ ] **Livello II** (≤2 piani f.t. + 1 interrato, attività non aperta al pubblico, condizioni a-f: esodo in luogo
      sicuro, nessun danno ad altre costruzioni, affollamento ≤100 e densità ≤0,2 pers/m², no posti letto, no
      persone da assistere): **classe 30** (1 piano f.t. senza interrati) / **classe 60** (≤2 piani f.t. + 1 interrato).
- [ ] **Livello III** — **Tabella 4** (q_f,d → classe): ≤100→0; ≤200→15; ≤300→20; ≤450→30; ≤600→45; ≤900→60;
      ≤1200→90; ≤1800→120; ≤2400→180; >2400→240.
- [ ] **Livelli IV e V**: su richiesta di committente/capitolato/autorità; progettazione con DM 14/9/2005.

## 4. Incendio di progetto e curve naturali (punto 4)

- [ ] Curve nominali: **standard θ_g = 20 + 345·log10(8t+1)**; **idrocarburi** θ_g = 1080·(1−0,325·e^−0,167t−0,675·e^−2,5t)+20;
      **esterna** θ_g = 660·(1−0,687·e^−0,32t−0,313·e^−3,8t)+20 [°C], t in minuti.
- [ ] Curve naturali (approccio prestazionale): **Tabella 5** (q_f,d → classe): ≤300→0; ≤450→15; ≤600→20; ≤900→30;
      ≤1200→45; ≤1800→60; ≤2400→90; >2400→120.

## 5. Elementi strutturali (punto 5)

- [ ] Verifica della **capacità portante** in condizioni di incendio; azioni in **combinazione eccezionale**;
      no concomitanza con altre azioni eccezionali.
- [ ] Elementi strutturali **secondari** (livello III): possibile verifica alla **classe 30** alle condizioni previste.

## Fuori scope

- [ ] Progetto prestazionale di dettaglio con curve naturali/modelli d'incendio; regole tecniche verticali VVF;
      Eurocodici parte 1-2 (proprietà dei materiali ad alta temperatura); analisi termica/meccanica di dettaglio.
