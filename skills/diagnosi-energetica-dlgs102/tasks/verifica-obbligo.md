# Task: Verifica dell'obbligo di diagnosi energetica (D.Lgs. 102/2014 art. 8)

## Obiettivo

Determinare se un'impresa e' obbligata alla diagnosi energetica ex art. 8 D.Lgs.
102/2014, quali esenzioni si applicano e quali scadenze.

## Input richiesti

- **dimensione**: numero di occupati; **fatturato annuo**; **totale di bilancio
  annuo** (per la definizione di grande impresa, art. 2);
- eventuale qualifica di **impresa a forte consumo di energia (energivora)**
  (iscrizione all'elenco CSEA ai sensi del DM MiSE 21/12/2017);
- **consumi energetici complessivi annui** in tep (per l'esenzione < 50 tep);
- presenza di un **sistema di gestione ISO 50001** (con diagnosi conforme
  all'allegato 2);
- data dell'ultima diagnosi eseguita (per collocare la prossima scadenza).

## Fonti da leggere

- `references/estratti/diagnosi-energetica-checklist.md` sezioni 1-2, 5
- se serve conferma: `references/fonti/dlgs-102-2014.md` (artt. 2, 8)

## Procedura

### Passo 1 - L'impresa e' un soggetto obbligato?
- **Grande impresa** (art. 2): **> 250 occupati E fatturato > 50 mln euro**,
  **oppure** totale di bilancio > 43 mln euro. Se si': obbligata (art. 8 c. 1).
- **Energivora** (DM MiSE 21/12/2017): obbligata **indipendentemente dalla
  dimensione** (art. 8 c. 3). La skill non stabilisce nel merito lo status di
  energivora: verificare l'iscrizione all'elenco CSEA.
- Se l'impresa non e' ne' grande ne' energivora: non e' obbligata (fermi eventuali
  incentivi/bandi per le PMI).

### Passo 2 - Esenzioni (grandi imprese)
- **Consumi annui < 50 tep**: esente (art. 8 c. 3-bis).
- **ISO 50001** con diagnosi conforme all'allegato 2: non si applica l'obbligo di
  periodicita' (art. 8 c. 1).

### Passo 3 - Scadenze
Prima diagnosi entro il **5 dicembre 2015**, poi **ogni quattro anni** (art. 8 c.
1): 2019, 2023, 2027, ... Colloca la prossima scadenza a partire dalla data
dell'ultima diagnosi (senza calcolare la data esatta al posto dell'utente se non
fornita).

### Passo 4 - Chi la esegue
**ESCo** (UNI CEI 11352) o **EGE** (UNI CEI 11339) **certificati** da organismi
accreditati (art. 8 c. 2); comunicazione dei risultati all'**ENEA**.

## Output atteso

- esito: **obbligata / non obbligata / esente**, con la citazione dell'articolo e
  il motivo (dimensione, energivora, < 50 tep, ISO 50001);
- **periodicita' e prossima scadenza** (quadriennale);
- **soggetto** che puo' eseguire la diagnosi e obbligo di comunicazione all'ENEA;
- richiamo alle **sanzioni** (art. 16: 4.000-40.000 euro per mancata diagnosi);
- avvertenza: la skill non esegue la diagnosi e non stabilisce nel merito lo
  status di energivora; la valutazione definitiva spetta all'impresa e all'auditor
  certificato.
