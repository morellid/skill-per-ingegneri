# Task: Determina livello di conoscenza (LC) e fattore di confidenza (FC)

## Obiettivo

Date le indagini conoscitive svolte o previste su una costruzione esistente,
individuare il livello di conoscenza raggiungibile (LC1/LC2/LC3) e il fattore di
confidenza (FC) corrispondente, ai sensi di NTC 2018 par. 8.5.4 e Circolare
7/2019 par. C8.5.4 (Tabella C8.5.IV per c.a./acciaio).

## Input richiesti

- **materiale strutturale**: muratura / calcestruzzo armato / acciaio / legno /
  misto;
- stato dell'**analisi storico-critica** (par. C8.5.1);
- stato del **rilievo geometrico** (a campione / completo / completo e accurato);
- livello delle **indagini sui dettagli costruttivi**: limitate / estese /
  esaustive (per c.a./acciaio anche % di elementi con rilievo dei dettagli);
- livello delle **prove sui materiali**: limitate / estese / esaustive;
- disponibilita' di **disegni costruttivi / certificati di prova originali**.

## Fonti da leggere

- `references/estratti/ntc2018-cap8-costruzioni-esistenti.md` sezione 5
- `references/fonti/circ-7-2019-mit.md` par. C8.5.4, C8.5.4.1 (muratura),
  C8.5.4.2 (c.a./acciaio) con Tabella C8.5.IV
- `references/fonti/ntc2018-dm-17-01-2018.md` par. 8.5.4 e 8.7.2 (uso dell'FC)

## Procedura

### Passo 1 - Requisiti minimi per LC (Circolare C8.5.4)

| Livello | Requisiti minimi | FC |
|---|---|---|
| **LC1** | analisi storico-critica commisurata; rilievo geometrico completo; indagini **limitate** sui dettagli costruttivi; prove **limitate** sui materiali | **1,35** |
| **LC2** | come LC1 ma indagini **estese** sui dettagli e prove **estese** sui materiali | **1,20** |
| **LC3** | analisi storico-critica; rilievo completo e accurato; indagini **esaustive** sui dettagli; prove **esaustive** sui materiali (o documenti progettuali originali verificati, equivalenti al rilievo completo + dettagli esaustivi) | **1,00** |

Il LC complessivo e' determinato dal **livello piu' basso** tra i requisiti
soddisfatti (il LC richiede che TUTTI i requisiti minimi del livello siano
raggiunti). Per c.a./acciaio incrocia gli input con la **Tabella C8.5.IV**
(colonne: geometrie, dettagli strutturali, proprieta' dei materiali, metodi di
analisi ammessi, FC).

### Passo 2 - Precisazioni

- **FC = 1 (LC3)** si applica **limitatamente ai parametri** per cui sono state
  eseguite le prove/indagini esaustive; per gli altri parametri l'FC resta
  coerente con le prove limitate o estese effettivamente eseguite (C8.5.4).
- **Acciaio**: se il LC non e' LC2 (risp. LC3) solo per una non estesa (risp. non
  esaustiva) conoscenza sulle proprieta' dei materiali, l'FC puo' essere ridotto
  con opportune considerazioni motivate anche sull'epoca di costruzione (C8.5.4).
- **Documentazione L. 1086/71 o 64/74**: ci si puo' riferire agli atti solo dopo
  adeguata giustificazione, eventualmente integrata da indagini in opera; in tal
  caso gli FC si assumono unitari (C8.5.4).
- **LC differenziati**: per verifiche non sismiche di singoli componenti o per
  verifiche sismiche dei meccanismi locali e' possibile adottare LC differenziati
  rispetto alle verifiche sismiche globali (C8.5.4).

### Passo 3 - Come si usa l'FC (NTC 8.7.2, Circ. C8.5.4.x)

- **c.a./acciaio**: le resistenze medie dei materiali si **dividono per l'FC**
  (Tabella C8.5.IV); per i meccanismi **fragili** si dividono anche per i
  coefficienti parziali dei materiali; per i meccanismi **duttili** solo per l'FC
  (NTC 8.7.2).
- **muratura** (C8.5.4.1): la conoscenza si gradua scegliendo dai valori di
  tabella (minimi per LC1, medi per LC2, aggiornati con le prove in sito per
  LC3), oltre al quadro generale dell'FC del par. C8.5.4.
- **materiali nuovi o aggiunti**: proprieta' di calcolo come per le nuove
  costruzioni (NTC 8.7.2).

## Output atteso

- **LC raggiunto/raggiungibile** con la motivazione basata sugli input e il
  requisito che ha determinato il livello (il "collo di bottiglia");
- **FC** corrispondente (1,35 / 1,20 / 1,00) con il riferimento (C8.5.4 e, per
  c.a./acciaio, Tab. C8.5.IV);
- eventuali **precisazioni** applicabili (FC differenziato per parametro,
  riduzione per acciaio, documentazione L. 1086/64);
- indicazione di **come applicare l'FC** al materiale in esame;
- avvertenza: la determinazione del LC/FC supporta il progettista ma non
  sostituisce il piano delle indagini ne' la valutazione della sicurezza; le
  quantita' di prove delle Tabelle C8.5.V/VI sono orientative e vanno calibrate
  caso per caso.
