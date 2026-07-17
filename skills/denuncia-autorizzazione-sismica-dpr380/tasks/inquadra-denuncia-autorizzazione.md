# Task: inquadra-denuncia-autorizzazione

Imposta il **preavviso/denuncia** e il **deposito del progetto** (art. 93) e verifica se
serve l'**autorizzazione preventiva** all'inizio dei lavori (art. 94) per una costruzione in
zona sismica. Non redige la denuncia ne' il progetto.

## Input

- **Zona sismica** del sito (1/2/3/4) e se e' **localita' a bassa sismicita'** (art. 83): da
  verificare presso regione/comune.
- Tipo di intervento (costruzione, riparazione, sopraelevazione) e sua classificazione ex
  art. 94-bis (cfr. task `classifica-intervento-sismico`).
- Soggetti: progettista, direttore dei lavori, appaltatore.

## Procedura

1. **Denuncia dei lavori e deposito del progetto (art. 93)**
   - In **tutte le zone sismiche**, imposta il **preavviso scritto** allo **sportello unico**
     (che trasmette all'ufficio tecnico regionale) con i nominativi di progettista/DL/
     appaltatore (c. 1).
   - Prevedi il **deposito del progetto** in doppio esemplare, firmato da tecnico abilitato e
     dal DL (c. 2), con il **contenuto minimo** richiesto dall'ufficio regionale (c. 3) e
     l'**asseverazione** del progettista (rispetto NTC, coerenza strutture/architettonico) (c.
     4).
   - Ricorda che il preavviso vale anche come **denuncia ex art. 65** (opere in c.a./acciaio)
     (c. 5) e che esiste un **registro comunale** (cc. 6-7).

2. **Autorizzazione preventiva (art. 94)**
   - Verifica se il sito e' in **localita' sismica** non a **bassa sismicita'**: in tal caso i
     lavori **non possono iniziare senza preventiva autorizzazione** dell'ufficio tecnico
     regionale (c. 1).
   - Inquadra il **termine di 30 giorni** (c. 2) e il **silenzio assenso** con attestazione
     SUE (c. 2-bis); segnala il **ricorso** al presidente della giunta regionale (c. 3).

3. **Coordinamento con la classificazione (art. 94-bis)**
   - Nota che l'obbligo di autorizzazione preventiva riguarda gli interventi **"rilevanti"**;
     per **minore rilevanza**/**privi di rilevanza** vale la **deroga** (cfr. task
     `classifica-intervento-sismico`).

## Output

Sequenza degli adempimenti: denuncia/preavviso e deposito del progetto asseverato (art. 93),
ed eventuale autorizzazione preventiva (art. 94) con termini e silenzio assenso, in funzione
della zona e della classificazione. Rinvia redazione e istruttoria a progettista/DL e ufficio
regionale/SUE.

## Riferimenti

- `../references/fonti/dpr-380-2001-93-94-94bis.md` (artt. 93, 94)
- `../references/estratti/sismica-checklist.md` (sez. 0-2)
