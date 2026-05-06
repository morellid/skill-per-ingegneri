# Note di dominio - gac-condominio-fotovoltaico-tetto

## Perche' e' un caso problematico (utile per validare la skill)

L'utente arriva con una **richiesta sbagliata**: vuole una CER per un caso che e' tipico GAC. La skill deve **correggere** la richiesta, non assecondarla.

## Punti che la skill deve cogliere correttamente

1. **Stesso edificio condominiale** = naturalmente **GAC** ai sensi dell'**art. 30 c. 2 lett. a) D.Lgs. 199/2021**, NON CER (art. 31). E NON art. 32, che disciplina ARERA / contratti / referente.
2. **Grande impresa** tra i partecipanti -> incompatibile con la qualita' di **socio CER** (art. 31). Nel GAC ex art. 30 c. 2 il partecipante e' un autoconsumatore, non socio di un ente CER, quindi il vincolo "no grandi imprese" della CER non si applica con la stessa portata. La skill stati la regola sostanziale; verifica documentale lato GSE solo per i requisiti specifici delle Regole Operative.
3. **Comune con popolazione molto > 50.000 ab.** -> il contributo PNRR ex art. 8 DM 7/12/2023 (anche nel regime esteso post DM 127/2025) NON e' accessibile per quell'impianto.
4. **Statuto** non si applica al GAC: serve un regolamento condominiale / accordo privato. La skill non deve forzare una formalizzazione notarile inutile.
5. **Producibilita'**: la skill deve **non assumere** un valore "tipico" non sourceato. L'utente fornisce il valore (qui 1.250 kWh/kWp/anno dichiarato dal progettista con simulazione PVGIS sito-specifica).
6. **Fascia di potenza TIP**: 80 kW rientra nella fascia < 200 kW, parte fissa massima.
7. **Titolo abilitativo** dell'impianto: fuori dalle fonti della skill, va segnalato come DA VERIFICARE.

## Cosa NON deve fare la skill

- Non deve creare uno statuto CER quando il GAC e' la configurazione corretta.
- Non deve attivare la sezione PNRR per un Comune con popolazione >= 50.000 ab. (regime post DM 127/2025).
- Non deve quantificare la TIP in EUR senza richiamare i valori vigenti.
- Non deve assumere che la grande impresa "rovini" l'iniziativa: il GAC e' la via per includerla.
- Non deve scegliere il titolo abilitativo dell'impianto al posto del professionista (fuori dalle fonti della skill).

## Possibili evoluzioni del caso

- Se in futuro nuove unita' commerciali si aggiungono, la struttura GAC va aggiornata via assemblea.
- Se il condominio si fonde/divide, il perimetro GAC cambia: serve riemissione del regolamento.
- Se la grande catena si ritira dal negozio e subentra una PMI, la situazione si semplifica e una CER diventa eventualmente fattibile, ma resta senza contributo PNRR (Comune > 50.000 ab. anche nel regime esteso post DM 127/2025).
