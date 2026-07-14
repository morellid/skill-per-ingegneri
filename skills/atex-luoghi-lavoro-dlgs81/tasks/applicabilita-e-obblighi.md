# Task: applicabilita-e-obblighi

Determina se il Titolo XI del D.Lgs. 81/2008 (ATEX luoghi di lavoro) si applica a
un luogo di lavoro e imposta la sequenza degli obblighi del datore di lavoro.

## Input richiesto

- Sostanze presenti (infiammabili: gas, vapori, nebbie, polveri) e processi.
- Natura del luogo (compresi lavori in sotterraneo) e attivita' svolte.
- Eventuale ricorrere di una fattispecie esclusa (art. 287 c. 3).

## Procedura

1. **Applicabilita' (art. 287, def. art. 288)**:
   - Verifica se puo' formarsi un'**atmosfera esplosiva** (miscela con l'aria di
     sostanze infiammabili in cui la combustione si propaga - art. 288).
   - Verifica le **esclusioni** (art. 287 c. 3): cure mediche in atto; apparecchi
     a gas (DPR 661/1996); esplosivi/sostanze chimicamente instabili; industrie
     estrattive (D.Lgs. 624/1996); mezzi di trasporto soggetti ad accordi
     internazionali (salvo veicoli destinati a operare in atmosfera esplosiva).
     Include i lavori in **sotterraneo** con aree esplosive (c. 2).

2. **Obblighi del datore di lavoro (art. 289)**: **prima** prevenire la
   **formazione** di atmosfere esplosive (c. 1); se non possibile, **evitare
   l'accensione** e **attenuare gli effetti** (c. 2).

3. **Valutazione dei rischi di esplosione (art. 290)**: come parte della
   valutazione dei rischi (art. 17), considerando probabilita' e durata delle
   atmosfere esplosive, fonti di accensione (incl. scariche elettrostatiche),
   caratteristiche di impianto/sostanze/processi, entita' degli effetti.

4. **Classificazione delle zone (art. 293)**: ripartire le aree in **zone** a
   norma dell'**allegato XLIX** (0/1/2 gas-vapori; 20/21/22 polveri); applicare
   le **prescrizioni minime** (allegato L); **segnaletica** (allegato LI) e
   allarmi ove necessario.
   - **La skill non classifica le zone**: rinvia all'allegato XLIX e alle norme
     tecniche (es. CEI EN 60079). Non inventare l'assegnazione di zona.

5. **DPCE (art. 294)**: elaborare e aggiornare il **documento sulla protezione
   contro le esplosioni** (rimando a `checklist-dpce`).

6. **Verifiche (art. 296)**: le installazioni elettriche nelle **zone 0, 1, 20,
   21** vanno sottoposte alle verifiche del **DPR 462/2001** (cfr. skill
   verifiche-messa-a-terra-dpr462).

## Output

- Esito applicabilita' (soggetto / escluso) con l'articolo.
- Sequenza degli obblighi (prevenzione, valutazione, zone, DPCE, verifiche) con i
  rispettivi articoli.
- Avvertenza: la classificazione delle zone e la valutazione richiedono gli
  allegati e le norme tecniche e un tecnico qualificato.

## Regole

- Non classificare le zone ne' redigere la valutazione "a memoria": rinviare
  all'allegato XLIX e alle norme tecniche.
- Distinguere la protezione dei **lavoratori** (Titolo XI) dalla **marcatura ATEX
  degli apparecchi** (dir. 2014/34/UE), fuori perimetro.
- Citare l'articolo (287-290, 293, 294, 296).
