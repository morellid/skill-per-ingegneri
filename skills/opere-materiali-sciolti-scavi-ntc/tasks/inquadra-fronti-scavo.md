# Task: inquadra-fronti-scavo

Inquadra la **progettazione e la verifica dei fronti di scavo** secondo le **NTC 2018 par. 6.8.6**. Supporto
documentale: **non** calcola le verifiche ne' dimensiona lo scavo o la struttura di sostegno.

## Quando usarla

Il progettista geotecnico deve impostare indagini, criteri e verifiche di un fronte di scavo (trincea, piazzale,
scavo su pendio o in prossimita' di manufatti). Per i manufatti di materiali sciolti (rilevati, argini) usa
`inquadra-verifica-materiali-sciolti`.

## Passi

1. **Indagini geotecniche** (par. 6.8.6.1): ferme le prescrizioni generali del par. 6.2.2, tieni conto di
   **profondita'**, **ampiezza**, **destinazione** e carattere **permanente o provvisorio** dello scavo.
2. **Profilo di scavo e verifica** (par. 6.8.6.2): definisci un profilo di scavo che rispetti il par. 6.2.4;
   la verifica di sicurezza si conduce con **modalita' analoga a quella dei manufatti di materiali sciolti**
   (quindi Combinazione 2 A2+M2+R2 dell'Approccio 1, Tab. 6.2.I/6.2.II/6.8.I con gamma_R = 1,1 - vedi
   `inquadra-verifica-materiali-sciolti`).
3. **Scavi su pendio**: verifica l'influenza dello scavo sulle condizioni di **stabilita' generale del pendio**.
4. **Contesto**: tieni conto di **opere e sovraccarichi in prossimita'** dello scavo, dell'influenza sul regime
   delle **pressioni interstiziali** e della **stabilita'/funzionalita' delle costruzioni preesistenti**.
5. **Struttura di sostegno delle pareti** - obbligatoria quando: scavo in **trincea a fronte verticale di
   altezza superiore ai 2 m** in cui sia prevista la **permanenza di personale**, oppure scavo **in prossimita'
   di manufatti esistenti**. In tali casi le verifiche si svolgono agli **SLU** e agli **SLE** (quando
   pertinenti).
6. **Azioni**: quelle dovute a terreno, acqua e sovraccarichi anche transitori vanno calcolate nelle
   **condizioni piu' sfavorevoli**; le ipotesi di calcolo delle azioni e delle sollecitazioni della struttura di
   sostegno vanno giustificate portando in conto deformabilita' relativa terreno-struttura, modalita' esecutive,
   caratteristiche del terreno e tempo di permanenza dello scavo.

Usa la checklist in `../references/estratti/materiali-sciolti-scavi-checklist.md` (sezione 7).

## Output atteso

Un inquadramento che indichi: le indagini specifiche per lo scavo, i criteri di progetto del profilo, i casi in
cui **serve una struttura di sostegno** (soglia dei 2 m a fronte verticale con permanenza di personale, o
prossimita' di manufatti) e le verifiche richieste (SLU/SLE, condizioni piu' sfavorevoli), con **rinvio ai
paragrafi** NTC. Nessun calcolo o dimensionamento.

## Cosa NON fare

- Non calcolare le verifiche ne' dimensionare lo scavo o la struttura di sostegno.
- Non confondere la **struttura di sostegno delle pareti di scavo** (verifica geotecnica NTC par. 6.8.6) con le
  **armature/sbadacchiature** per la **sicurezza dei lavoratori** (D.Lgs 81/2008 Titolo IV, skill
  `sicurezza-scavi-fondazioni-dlgs81`): sono discipline distinte e complementari.
- Non trattare le **terre e rocce da scavo** come sottoprodotti (DPR 120/2017) ne' la progettazione sismica.
