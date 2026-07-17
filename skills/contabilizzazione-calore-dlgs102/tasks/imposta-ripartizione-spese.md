# Task: imposta-ripartizione-spese

Imposta lo **schema di ripartizione delle spese** ex art. 9 c. 5 lett. d: quota
**>= 50%** ai prelievi volontari e quota residua (millesimi/mq/mc/potenze, UNI 10200),
con i casi particolari (prima stagione, edifici gia' provvisti, guida ENEA). **Non
calcola** i millesimi ne' le quote.

## Input attesi
- I **consumi effettivi** (prelievi volontari) rilevati da sotto-contatori/ripartitori
  (dato d'ingresso: non e' compito della skill misurarli/calcolarli).
- I dati per la **quota involontaria** (millesimi, mq/mc utili, potenze installate).
- Se e' la **prima stagione termica** dopo l'installazione o se l'edificio era **gia'
  provvisto** e ripartito.

## Passi
1. **Quota volontaria** (lett. d): attribuisci una **quota di almeno il 50%**
   dell'importo complessivo agli **effettivi prelievi volontari** di energia termica
   (misurati).
2. **Quota residua** (lett. d): ripartisci il resto secondo un criterio tra
   **millesimi**, **metri quadri** o **metri cubi utili**, oppure **potenze installate**
   (criteri UNI 10200). Indica che la scelta e il calcolo spettano al termotecnico/
   amministratore.
3. **Prima stagione termica** (lett. d): per la prima stagione successiva
   all'installazione la suddivisione puo' essere fatta ai **soli millesimi di
   proprieta'**.
4. **Edifici gia' provvisti** (lett. d): se, alla data di entrata in vigore, si era
   gia' installato e ripartito, le disposizioni sono **facoltative**.
5. **Differenze di fabbisogno > 50%** (c. 5-quater): se, con **relazione tecnica
   asseverata**, sono comprovate differenze di fabbisogno termico per mq **> 50%** tra
   le unita', si fa riferimento alla **guida ENEA** sulle ripartizioni suggerite.

## Output
- Schema di ripartizione: **quota volontaria >= 50%** + criterio della **quota
  residua**, con i casi particolari (prima stagione, edifici gia' provvisti, guida
  ENEA) e il **rinvio al comma/lettera**.
- Nota di rinvio: il **calcolo** delle quote e dei millesimi termici (UNI 10200) e la
  **tabella** di ripartizione restano al termotecnico e all'amministratore.

## Riferimenti
- `../references/fonti/dlgs-102-2014-art-9.md` (art. 9 c. 5 lett. d, c. 5-quater)
- `../references/estratti/contabilizzazione-calore-checklist.md` (sez. E, F)
