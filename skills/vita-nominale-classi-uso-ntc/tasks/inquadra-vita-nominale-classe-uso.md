# Task: inquadra-vita-nominale-classe-uso

Inquadra la scelta della **vita nominale di progetto V_N** (§2.4.1) e della **classe d'uso** (§2.4.2) di una
costruzione secondo le **NTC 2018**. Supporto documentale: **non** definisce lo spettro né i periodi di ritorno.

## Quando usarla

All'avvio del progetto il progettista deve dichiarare la vita nominale di progetto e la classe d'uso della
costruzione. Per ricavare il periodo di riferimento V_R usa `inquadra-periodo-riferimento-vr`.

## Passi

1. **Vita nominale V_N - definizione** (§2.4.1): V_N è il numero di anni in cui l'opera, purché soggetta alla
   **necessaria manutenzione**, è prevista mantenere specifici **livelli prestazionali**.
2. **Valori minimi V_N** (Tab. 2.4.I): individua il **tipo di costruzione** e assumi il valore **minimo**:
   - tipo 1 - **costruzioni temporanee e provvisorie** → **V_N = 10 anni**;
   - tipo 2 - costruzioni con **livelli di prestazioni ordinari** → **V_N = 50 anni**;
   - tipo 3 - costruzioni con **livelli di prestazioni elevati** → **V_N = 100 anni**.
   Sono valori **minimi** (il progettista può adottarne di superiori) e possono servire anche per definire le
   **azioni dipendenti dal tempo**.
3. **Non temporanee** (§2.4.1): non sono temporanee le costruzioni (o parti) che possono essere **smantellate con
   l'intento di riutilizzo**.
4. **Fase di costruzione** (§2.4.1): se la fase di costruzione ha durata prevista **P_N**, la vita nominale di
   tale fase (ai fini delle azioni sismiche) va assunta **non inferiore a P_N** e **comunque non inferiore a 5
   anni**.
5. **Esonero verifiche sismiche** (§2.4.1): per opere di **tipo 1** o **in fase di costruzione** le verifiche
   sismiche **possono omettersi** quando il progetto preveda che tale condizione permanga per **meno di 2 anni**.
6. **Classe d'uso** (§2.4.2): classifica in base alle **conseguenze di interruzione di operatività/collasso**:
   - **Classe I**: presenza **solo occasionale** di persone, edifici agricoli;
   - **Classe II**: **normali affollamenti**, senza contenuti pericolosi né funzioni pubbliche/sociali essenziali;
   - **Classe III**: **affollamenti significativi**;
   - **Classe IV**: **funzioni pubbliche o strategiche importanti** (anche protezione civile).
   Gli esempi di dettaglio (industrie, ponti, reti viarie/ferroviarie, dighe) sono nel testo del §2.4.2.

Usa la checklist in `../references/estratti/vita-nominale-classi-uso-checklist.md` (sezioni 1 e 2).

## Output atteso

Un inquadramento che indichi: la **vita nominale V_N** adottata (con il tipo di costruzione della Tab. 2.4.I e le
regole per fase di costruzione ed esonero verifiche) e la **classe d'uso** I-IV con la relativa motivazione, con
**rinvio ai paragrafi/tabelle** NTC. Nessuna definizione di spettro o periodi di ritorno.

## Cosa NON fare

- Non definire lo **spettro** né i **periodi di ritorno T_R** / le probabilità di superamento degli stati limite
  (§3.2).
- Non decidere al posto del progettista la classe d'uso in casi ambigui: riporta i criteri e gli esempi del
  §2.4.2 e rimanda alla sua valutazione.
