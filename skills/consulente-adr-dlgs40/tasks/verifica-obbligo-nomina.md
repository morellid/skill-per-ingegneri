# Task: verifica-obbligo-nomina

Determina se un'impresa e' tenuta a nominare il consulente per la sicurezza dei
trasporti di merci pericolose (D.Lgs. 40/2000) o se e' esente.

## Input richiesto

- Attivita': l'impresa effettua **trasporto** di merci pericolose (strada,
  ferrovia, via navigabile interna) o **carico/scarico** connesso?
- Modalita': attivita' principale/accessoria o **occasionale**?
- Quantitativi per unita' di trasporto (rispetto ai limiti dei marginali
  10010/10011 dell'allegato B al DM 4/9/1996 e agg.).
- Ambito (nazionale/internazionale) e grado di pericolosita'/inquinamento.

## Procedura

1. **Ambito (art. 2 c. 1)**: se l'impresa **trasporta** merci pericolose o
   effettua **carico/scarico** connesso -> rientra nel campo di applicazione.
2. **Esclusioni di ambito (art. 2 c. 2)**: mezzi delle Forze armate/polizia; vie
   navigabili interne nazionali non collegate all'UE -> fuori ambito.
3. **Esenzioni dalla nomina (art. 3 c. 6)**:
   - a) **quantitativi limitati** per unita' di trasporto sotto i limiti dei
     marginali 10010/10011 (allegato B DM 4/9/1996 e agg.);
   - b) trasporti **occasionali**, non attivita' principale/accessoria, in ambito
     **esclusivamente nazionale**, con merci a pericolosita'/inquinamento minimi.
   - **La skill non stabilisce i valori-soglia dei quantitativi limitati**:
     rinvia all'allegato B del DM 4/9/1996 (e all'ADR vigente) e a un consulente.

## Output

- Esito: obbligo di nomina del consulente sì/no (o esente), con l'articolo.
- Se obbligata: rimando agli adempimenti (task `checklist-adempimenti`).
- Avvertenza: i quantitativi limitati e le classi di merci vanno verificati
  sull'allegato B / ADR con un consulente qualificato.

## Regole

- Distinguere l'**ambito** (art. 2) dalle **esenzioni** dalla nomina (art. 3 c. 6).
- Non stabilire a memoria i quantitativi limitati: rinviare all'allegato B/ADR.
- Ricordare che la **responsabilita'** resta comunque del capo dell'impresa
  (art. 3 c. 5).
