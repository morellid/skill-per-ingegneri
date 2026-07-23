# Output atteso

## Formula (DM 9 marzo 2007, Allegato, punto 2)

Il **carico d'incendio specifico di progetto** è:

**q_f,d = δ_q1 · δ_q2 · δ_n · q_f** [MJ/m²]

## Scelta dei coefficienti

- **δ_q1** (Tabella 1 — dimensione del compartimento): con **A = 600 m²** si ha **500 ≤ A < 1.000**, quindi
  **δ_q1 = 1,20**.
- **δ_q2** (Tabella 2 — tipo di attività): attività a **rischio moderato** → classe di rischio **II**, quindi
  **δ_q2 = 1,00**.
- **δ_n = Π_i δ_ni** (Tabella 3 — misure di protezione presenti):
  - rete idrica antincendio **interna**: **δ_n6 = 0,90**;
  - sistema automatico di **rivelazione/segnalazione/allarme**: **δ_n4 = 0,85**;
  - **δ_n = 0,90 · 0,85 = 0,765**.

  (Le altre misure di protezione non sono presenti, quindi i relativi δ_ni non si applicano.)

## Calcolo

q_f,d = 1,20 · 1,00 · 0,765 · 700 = **≈ 642,6 MJ/m²**

Il **carico d'incendio specifico di progetto** è **q_f,d ≈ 643 MJ/m²**.

## Note

- Il valore q_f,d è l'input per la determinazione della **classe di resistenza al fuoco** (vedi il task
  `determina-livello-classe-resistenza`): per il **livello III**, con **600 < q_f,d ≤ 900**, la **Tabella 4**
  del DM indica la **classe 60**.
- Il carico d'incendio specifico **q_f = q/A** dato in ingresso deriva a sua volta da
  **q = Σ g_i·H_i·m_i·ψ_i** (punto 1), con m_i = 0,80 per legno/materiali cellulosici (1,00 per gli altri) e
  ψ_i = 0 / 0,85 / 1 secondo il tipo di contenitore; i poteri calorifici inferiori H_i si assumono secondo
  la **UNI EN ISO 1716**.
- Supporto documentale: la scelta della classe di rischio (δ_q2) e la verifica delle condizioni di
  applicabilità delle misure di protezione restano di competenza del professionista antincendio.
