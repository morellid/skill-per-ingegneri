# Note di dominio - gac-condominio-fotovoltaico-tetto

## Perche' e' un caso problematico (utile per validare la skill)

L'utente arriva con una **richiesta sbagliata**: vuole una CER per un caso che e' tipico GAC. La skill deve **correggere** la richiesta, non assecondarla.

## Punti che la skill deve cogliere correttamente

1. **Stesso edificio condominiale** = naturalmente **GAC** (art. 32 D.Lgs. 199/2021), non CER. La CER e' pensata per soggetti distinti su perimetro cabina primaria.
2. **Grande impresa** tra i partecipanti -> incompatibile con la qualita' di socio CER (art. 31 c. 2). Nel GAC e' un autoconsumatore, non socio di un ente CER, quindi il vincolo non si pone con la stessa rigidita'. La skill puo' segnalare la necessita' di verifica puntuale sulle Regole Operative GSE.
3. **Comune con popolazione > 5.000 ab.** -> il contributo PNRR ex art. 8 DM 7/12/2023 NON e' accessibile per quell'impianto.
4. **Statuto** non si applica al GAC: serve un regolamento condominiale / accordo privato. La skill non deve forzare un atto pubblico inutile.
5. **Producibilita'** in Pianura Padana piu' alta del Centro Italia (1.200-1.300 kWh/kWp/anno tipica): la skill deve usare un valore coerente con la latitudine.
6. **Fascia di potenza TIP**: 80 kW rientra nella fascia < 200 kW, parte fissa massima.

## Cosa NON deve fare la skill

- Non deve creare uno statuto CER quando il GAC e' la configurazione corretta.
- Non deve attivare la sezione PNRR per un Comune > 5.000 ab.
- Non deve quantificare la TIP in EUR senza richiamare i valori vigenti.
- Non deve assumere che la grande impresa "rovini" l'iniziativa: il GAC e' la via per includerla.

## Possibili evoluzioni del caso

- Se in futuro nuove unita' commerciali si aggiungono, la struttura GAC va aggiornata via assemblea.
- Se il condominio si fonde/divide, il perimetro GAC cambia: serve riemissione del regolamento.
- Se la grande catena si ritira dal negozio e subentra una PMI, la situazione si semplifica e una CER diventa eventualmente fattibile, ma senza contributo PNRR (Comune > 5.000 ab.).
