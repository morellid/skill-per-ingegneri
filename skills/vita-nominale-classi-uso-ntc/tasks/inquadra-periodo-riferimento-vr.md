# Task: inquadra-periodo-riferimento-vr

Ricava il **periodo di riferimento per l'azione sismica V_R** di una costruzione secondo le **NTC 2018 par.
2.4.3** e ne indica l'uso a valle. Supporto documentale: **non** definisce lo spettro né i periodi di ritorno.

## Quando usarla

Note la vita nominale V_N (§2.4.1) e la classe d'uso (§2.4.2), il progettista deve ricavare il periodo di
riferimento V_R con cui si valutano le azioni sismiche. Per fissare V_N e la classe d'uso usa
`inquadra-vita-nominale-classe-uso`.

## Passi

1. **Formula** (§2.4.3): il periodo di riferimento per l'azione sismica si ricava, per ciascun tipo di
   costruzione, moltiplicando la vita nominale di progetto V_N per il coefficiente d'uso C_U:

       V_R = V_N · C_U                                                  [2.4.1]

   (operatore di moltiplicazione verificato sull'immagine della pagina PDF, perché `pdftotext` lo perde).
2. **Coefficiente d'uso C_U** (Tab. 2.4.II): al variare della classe d'uso:
   - classe **I** → **C_U = 0,7**;
   - classe **II** → **C_U = 1,0**;
   - classe **III** → **C_U = 1,5**;
   - classe **IV** → **C_U = 2,0**.
3. **Rischio di incidente rilevante** (§2.4.3): per costruzioni a servizio di attività a **rischio di incidente
   rilevante** si adottano valori di C_U **anche superiori a 2**, in relazione alle conseguenze su ambiente e
   pubblica incolumità.
4. **Uso a valle** (§2.4.3 → §3.2): V_R è il periodo di riferimento da cui, tramite le **probabilità di
   superamento P_VR** di ciascuno stato limite, si ricavano i **periodi di ritorno T_R** dell'azione sismica. Il
   calcolo dei T_R e la definizione dello spettro **sono fuori scope**: rimanda al §3.2 (skill
   `spettro-risposta-ntc`).

Usa la checklist in `../references/estratti/vita-nominale-classi-uso-checklist.md` (sezione 3).

## Output atteso

Il **periodo di riferimento V_R = V_N · C_U** con il valore di C_U dalla Tab. 2.4.II per la classe d'uso in esame
(ed eventuale C_U > 2 per rischio di incidente rilevante), con **rinvio a formula/tabella** NTC e all'uso a valle
verso il §3.2. Nessun calcolo di spettro o periodi di ritorno.

## Cosa NON fare

- Non calcolare i **periodi di ritorno T_R** né le **probabilità di superamento P_VR** degli stati limite, né
  definire lo **spettro** (§3.2): rinvia a `spettro-risposta-ntc`.
- Non modificare i valori tabellari di C_U: sono quelli della Tab. 2.4.II (0,7/1,0/1,5/2,0).
