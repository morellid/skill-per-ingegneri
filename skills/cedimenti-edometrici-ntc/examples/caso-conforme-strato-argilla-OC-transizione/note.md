# Note - esempio conforme: argilla OC con transizione a NC

## Perche' questo esempio e' importante

- E' il caso d'uso centrale dell'eq. [7-4] FHWA (OC con pf > pc): il carico attraversa la preconsolidazione e il calcolo deve mostrare separatamente il contributo di ricompressione (Cr) e quello vergine (Cc), dominante.
- Tutti i valori sono chiusi e verificabili a mano: log10(1,5) = 0,176091; log10(2) = 0,301030; S = 1,11111*(0,0088046+0,0903090) = 0,110126 m -> 110,1 mm.
- Mostra il pattern di presentazione: equazione FHWA citata per strato, aggancio al cap. 12 NTC 2018 e confronto rimandato al limite Cd del progetto (§ 6.2.4.3).

## Storia dell'esempio

- v0.1.x pre-remediation: stesso input, calcolo con "formulazione classica" non source-grounded (rimossa in 0.1.1).
- v0.2.0: il calcolo torna disponibile perche' la formulazione e' ora trascritta da una fonte pubblica hashata (FHWA NHI-06-088 par. 7.5.2), citata come codice internazionale ex cap. 12 NTC.

## Limitazioni note

- delta_sigma' e' dichiarato calcolato a parte (Boussinesq) dal progettista: la skill non lo verifica.
- Il valore di sigma_p' (Casagrande) e' un input: la qualita' della sua determinazione resta al progettista (FHWA Table 7-6a richiamata, non implementata).
