# Task: calcola-carico-incendio-specifico-progetto

Inquadra il **carico d'incendio specifico** q_f e il **carico d'incendio specifico di progetto** q_f,d di un
compartimento secondo il **DM 9 marzo 2007** (punti 1-2 dell'Allegato). Supporto documentale: fornisce
formula e coefficienti tabellari; **non** sostituisce la valutazione del professionista antincendio.

## Quando usarla

Il tecnico deve quantificare il carico d'incendio di un compartimento (input per la classe di resistenza al
fuoco). Per il passaggio da q_f,d alla classe usa `determina-livello-classe-resistenza`.

## Passi

1. **Carico d'incendio** q (punto 1): somma sui materiali combustibili presenti,

   **q = Σ_i g_i · H_i · m_i · ψ_i** [MJ]

   - **g_i**: massa dell'i-esimo combustibile [kg];
   - **H_i**: potere calorifico inferiore [MJ/kg], determinato secondo **UNI EN ISO 1716:2002**;
   - **m_i** (partecipazione alla combustione): **0,80** per legno e materiali di natura cellulosica; **1,00**
     per tutti gli altri combustibili;
   - **ψ_i** (limitazione della partecipazione): **0** se il materiale è in contenitori progettati per
     resistere al fuoco; **0,85** se in contenitori non combustibili non progettati a tale scopo; **1** negli
     altri casi.

2. **Carico d'incendio specifico** (punto 1): **q_f = q / A** [MJ/m²], con **A** superficie in pianta lorda
   del compartimento [m²].

3. **Carico d'incendio specifico di progetto** (punto 2): **q_f,d = δ_q1 · δ_q2 · δ_n · q_f** [MJ/m²], dove:
   - **δ_q1** (Tabella 1, per superficie A [m²]): A<500 → **1,00**; 500≤A<1.000 → **1,20**; 1.000≤A<2.500 →
     **1,40**; 2.500≤A<5.000 → **1,60**; 5.000≤A<10.000 → **1,80**; A≥10.000 → **2,00**;
   - **δ_q2** (Tabella 2, per classe di rischio dell'attività): I basso → **0,80**; II moderato → **1,00**;
     III alto → **1,20**;
   - **δ_n = Π_i δ_ni** (Tabella 3, solo per le misure di protezione effettivamente presenti): estinzione
     automatica **ad acqua 0,60** / **altro tipo 0,80**; evacuazione automatica fumo e calore **0,90**;
     rivelazione/segnalazione/allarme **0,85**; squadra aziendale antincendio **0,90**; rete idrica
     **interna 0,90** / **interna e esterna 0,80**; percorsi protetti di accesso **0,90**; accessibilità ai
     mezzi di soccorso VVF **0,90**.

Usa la checklist in `../references/estratti/carico-incendio-checklist.md` (sezioni 1 e 2).

## Output atteso

Il valore (o l'impostazione del calcolo) di **q_f** e **q_f,d = δ_q1·δ_q2·δ_n·q_f**, con i coefficienti
scelti dalle Tabelle 1-3 e il **rinvio al punto/tabella** del DM. Nessuna sostituzione della valutazione del
professionista.

## Cosa NON fare

- Non **fornire** i valori di H_i (sono nella **UNI EN ISO 1716**) né le proprietà dei materiali ad alta
  temperatura (Eurocodici parte 1-2).
- Non **derivare** la classe di resistenza al fuoco (usa l'altro task) né eseguire il progetto prestazionale
  con curve naturali.
