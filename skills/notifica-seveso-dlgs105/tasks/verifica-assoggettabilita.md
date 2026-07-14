# Task: verifica-assoggettabilita

Determina se uno stabilimento e' soggetto al D.Lgs. 105/2015 (Seveso III) e, in
caso affermativo, se e' di **soglia inferiore** o **superiore**.

## Input richiesto

- Elenco delle **sostanze pericolose** presenti (materie prime, prodotti,
  sottoprodotti, residui, intermedi) e relative **quantita' massime detenibili**.
- Classificazione di pericolo (CLP, Reg. 1272/2008) o denominazione (per le
  sostanze nominate della parte 1 dell'allegato 1).
- Tipo di attivita' e natura del sito (per verificare le esclusioni dell'art. 2).
- Data di avvio/costruzione o di modifica (per la decorrenza degli obblighi).

## Procedura

1. **Esclusioni (art. 2 c. 2)**. Verifica se lo stabilimento ricade in una
   fattispecie esclusa (militari; radiazioni ionizzanti; trasporto e deposito
   temporaneo intermedio connesso fuori dagli stabilimenti soggetti; condotte;
   miniere/cave; offshore; stoccaggio gas offshore; discariche). Se escluso,
   fermati e indicalo.

2. **Presenza di sostanze pericolose (art. 3 lett. l, n)**. Considera le
   quantita' reali o prevedibili, comprese quelle generabili in caso di perdita
   del controllo del processo.

3. **Confronto con l'allegato 1**. Per ciascuna sostanza/categoria confronta la
   quantita' con la **colonna 2** (soglia inferiore) e la **colonna 3** (soglia
   superiore) della parte 1 (sostanze nominate) o della parte 2 (categorie di
   pericolo). Applica, ove previsto, la **regola della sommatoria** (nota 4)
   sommando le sostanze della stessa categoria.
   - **La skill NON riproduce le soglie**: indica quali colonne/parti consultare
     e chiedi all'utente i valori, oppure rinvia all'allegato 1 e al supporto di
     un tecnico. Non inventare valori di soglia.

4. **Classificazione (art. 3 lett. b-c)**:
   - quantita' >= colonna 2 ma < colonna 3 -> **soglia inferiore**;
   - quantita' >= colonna 3 -> **soglia superiore**;
   - sotto la colonna 2 (e senza superamento per sommatoria) -> **non soggetto**.

5. **Decorrenza (art. 3 lett. e-g)**. Colloca lo stabilimento tra nuovo /
   preesistente / altro per fissare i termini degli adempimenti.

## Output

- Esito assoggettabilita' (soggetto / escluso / sotto soglia) con l'articolo.
- Se soggetto: **soglia inferiore** o **superiore**, con il rinvio all'allegato 1
  e alla regola della sommatoria per la verifica quantitativa.
- Elenco degli adempimenti conseguenti (rimando a `checklist-adempimenti`).
- Avvertenza: la verifica quantitativa delle soglie e della sommatoria richiede
  la lettura dell'allegato 1 e la classificazione CLP.

## Regole

- Non stabilire le soglie sostanza-specifiche ne' eseguire la sommatoria a
  memoria: rinviare all'allegato 1.
- Citare sempre l'articolo (2, 3) a supporto della conclusione.
- Distinguere il criterio di **assoggettabilita'** (art. 2/3) dagli **obblighi**
  conseguenti (artt. 13-15).
