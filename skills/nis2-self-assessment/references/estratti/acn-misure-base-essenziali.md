# Det. ACN 379907/2025 - Allegato 2 - Misure di base per soggetti essenziali

> Fonte: Agenzia per la Cybersicurezza Nazionale, Determinazione del Direttore Generale del 18/12/2025 (protocollo 379907/2025), Allegato 2.
> Fonte catalogata in `sources.yaml` come `acn-det-379907-allegato-2`.
> URL canonico: https://www.acn.gov.it/portale/documents/d/guest/allegato-2-v2
> Estratto: struttura completa per funzioni/categorie/sottocategorie. Per il testo verbatim dei requisiti puntuali di ogni sottocategoria fare riferimento al PDF in `not_in_repo/acn-allegato-2-v2.pdf` (SHA256 catalogato).
> Data consultazione: 2026-04-29.

## Inquadramento

Allegato 2 della Det. ACN 379907/2025 (in vigore dal 15/01/2026, art. 9 co. 3, sostitutiva della Det. 164179/2025). Si applica ai **soggetti essenziali** ai sensi dell'art. 6 D.Lgs. 138/2024 e definisce le **specifiche di base** per gli adempimenti agli obblighi di gestione del rischio per la sicurezza informatica (art. 24 D.Lgs. 138/2024) e degli organi di amministrazione e direttivi (art. 23).

L'organizzazione segue il **Framework Nazionale per la Cybersecurity e la Data Protection ed. 2025** (sviluppato dal CIS Sapienza + Cybersecurity National Lab CINI in collaborazione con ACN, cfr. premesse Det. 379907/2025).

## Struttura

L'Allegato 2 (essenziali) e' organizzato in:
- **6 funzioni** (GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER)
- **18 categorie**
- **43 sottocategorie**
- **112 requisiti operativi** (conteggio numerato dal PDF)

### 1. GOVERNO (GOVERN) - 5 categorie, 11 sottocategorie

#### 1.1. Contesto organizzativo (GV.OC)
- 1.1.1. **GV.OC-04**: Gli obiettivi, le capacita' e i servizi critici dai quali gli stakeholder dipendono o che si aspettano dall'organizzazione sono compresi e comunicati.

#### 1.2. Strategia di gestione del rischio (GV.RM)
- 1.2.1. **GV.RM-03**: Le attivita' e gli esiti della gestione del rischio di cybersecurity sono parte integrante dei processi di gestione del rischio dell'organizzazione.

#### 1.3. Ruoli, responsabilita' e correlati poteri (GV.RR)
- 1.3.1. **GV.RR-02**: I ruoli, le responsabilita' e i correlati poteri relativi alla gestione del rischio di cybersecurity sono stabiliti, comunicati, compresi e applicati.
- 1.3.2. **GV.RR-04**: La cybersecurity e' inclusa nelle pratiche delle risorse umane.

#### 1.4. Politica (GV.PO)
- 1.4.1. **GV.PO-01**: La politica per la gestione del rischio di cybersecurity e' stabilita in base al contesto organizzativo, alla strategia di cybersecurity e alle priorita', ed e' comunicata e applicata. (16 ambiti di policy obbligatori per i soggetti essenziali; politiche **approvate dagli organi di amministrazione e direttivi**.)
- 1.4.2. **GV.PO-02**: La politica per la gestione del rischio di cybersecurity e' revisionata, aggiornata, comunicata e applicata.

#### 1.5. Gestione del rischio della catena di approvvigionamento (GV.SC)
- 1.5.1. **GV.SC-01**: Sono stabiliti e accettati dagli stakeholder dell'organizzazione il programma, la strategia, gli obiettivi, le politiche e i processi di gestione del rischio di cybersecurity della catena di approvvigionamento.
- 1.5.2. **GV.SC-02**: I ruoli e le responsabilita' in materia di cybersecurity per fornitori, clienti e partner sono stabiliti, comunicati, e coordinati internamente ed esternamente.
- 1.5.3. **GV.SC-04**: I fornitori sono noti e prioritizzati in base alla criticita'.
- 1.5.4. **GV.SC-05**: I requisiti per affrontare i rischi di cybersecurity nella catena di approvvigionamento sono stabiliti, prioritizzati e integrati nei contratti e altri tipi di accordi con fornitori e altre terze parti.
- 1.5.5. **GV.SC-07**: I rischi posti da un fornitore, dai suoi prodotti e servizi e da altre terze parti sono compresi, registrati, prioritizzati, valutati, gestiti e monitorati.

### 2. IDENTIFICAZIONE (IDENTIFY) - 3 categorie, 10 sottocategorie

#### 2.1. Gestione degli asset (ID.AM)
- 2.1.1. **ID.AM-01**: Sono mantenuti gli inventari dell'hardware gestito dall'organizzazione.
- 2.1.2. **ID.AM-02**: Sono mantenuti gli inventari del software, dei servizi e dei sistemi gestiti dall'organizzazione.
- 2.1.3. **ID.AM-03**: Sono mantenute le rappresentazioni delle comunicazioni di rete, dei flussi di dati interni e con i sistemi esterni.
- 2.1.4. **ID.AM-04**: Sono mantenuti gli inventari dei servizi erogati dai fornitori.

#### 2.2. Valutazione del rischio (ID.RA)
- 2.2.1. **ID.RA-01**: Le vulnerabilita' negli asset sono identificate, confermate e registrate.
- 2.2.2. **ID.RA-05**: Minacce, vulnerabilita', probabilita' e impatti sono utilizzati per comprendere il rischio intrinseco e per informare la prioritizzazione delle risposte al rischio.
- 2.2.3. **ID.RA-06**: Le risposte al rischio sono scelte, prioritizzate, pianificate, monitorate e comunicate.
- 2.2.4. **ID.RA-08**: Sono stabiliti processi per la ricezione, l'analisi e la risposta alle divulgazioni di vulnerabilita' provenienti da fonti interne ed esterne.

#### 2.3. Miglioramento (ID.IM)
- 2.3.1. **ID.IM-01**: Sono identificati miglioramenti in esito alle valutazioni.
- 2.3.2. **ID.IM-04**: I piani di risposta agli incidenti e gli altri piani di cybersecurity che impattano le operazioni sono stabiliti, comunicati, mantenuti e migliorati.

### 3. PROTEZIONE (PROTECT) - 5 categorie, 16 sottocategorie

#### 3.1. Gestione delle identita', autenticazione e controllo degli accessi (PR.AA)
- 3.1.1. **PR.AA-01**: Le identita' e le credenziali degli utenti, dei servizi e dell'hardware autorizzati sono gestite dall'organizzazione.
- 3.1.2. **PR.AA-03**: Utenti, servizi e hardware sono autenticati.
- 3.1.3. **PR.AA-05**: I permessi, i diritti e le autorizzazioni di accesso sono definiti in una politica, gestiti, applicati e revisionati, e incorporano i principi del minimo privilegio e della separazione dei compiti.
- 3.1.4. **PR.AA-06**: L'accesso fisico agli asset e' gestito, monitorato e applicato in misura appropriata al rischio.

#### 3.2. Consapevolezza e formazione (PR.AT)
- 3.2.1. **PR.AT-01**: Il personale e' sensibilizzato e formato in modo da possedere le conoscenze e le competenze necessarie per svolgere i compiti generali considerando i rischi di cybersecurity rilevanti.
- 3.2.2. **PR.AT-02**: Gli individui che ricoprono ruoli specializzati sono sensibilizzati e formati in modo da possedere le conoscenze e le competenze necessarie per svolgere i compiti rilevanti considerando i rischi di cybersecurity.

#### 3.3. Sicurezza dei dati (PR.DS)
- 3.3.1. **PR.DS-01**: La riservatezza, l'integrita' e la disponibilita' dei dati a riposo (data-at-rest) sono protette.
- 3.3.2. **PR.DS-02**: La riservatezza, l'integrita' e la disponibilita' dei dati in transito (data-in-transit) sono protette.
- 3.3.3. **PR.DS-11**: I backup dei dati sono creati, protetti, mantenuti e verificati.

#### 3.4. Sicurezza delle piattaforme (PR.PS)
- 3.4.1. **PR.PS-01**: Sono stabilite e applicate pratiche di gestione della configurazione.
- 3.4.2. **PR.PS-02**: Il software e' mantenuto, sostituito e rimosso in base al rischio.
- 3.4.3. **PR.PS-03**: L'hardware e' mantenuto, sostituito e rimosso in base al rischio.
- 3.4.4. **PR.PS-04**: I registri di log sono generati e resi disponibili per il monitoraggio continuo.
- 3.4.5. **PR.PS-06**: Le pratiche di sviluppo sicuro del software sono integrate e le loro prestazioni sono monitorate.

#### 3.5. Resilienza dell'infrastruttura tecnologica (PR.IR)
- 3.5.1. **PR.IR-01**: Le reti e gli ambienti sono protetti dall'accesso logico e dall'uso non autorizzati.
- 3.5.2. **PR.IR-03**: Sono implementati meccanismi per soddisfare i requisiti di resilienza in situazioni avverse.

### 4. RILEVAMENTO (DETECT) - 1 categoria, 2 sottocategorie

#### 4.1. Monitoraggio continuo (DE.CM)
- 4.1.1. **DE.CM-01**: Le reti e i servizi di rete sono monitorati per individuare eventi potenzialmente avversi.
- 4.1.2. **DE.CM-09**: L'hardware e il software di elaborazione, gli ambienti di runtime e i loro dati sono monitorati per individuare eventi potenzialmente avversi.

### 5. RISPOSTA (RESPOND) - 2 categorie, 2 sottocategorie

#### 5.1. Gestione degli incidenti (RS.MA)
- 5.1.1. **RS.MA-01**: Il piano di risposta agli incidenti e' eseguito in coordinamento con le terze parti rilevanti, una volta che un incidente e' stato dichiarato.

#### 5.2. Segnalazione e comunicazione della risposta agli incidenti (RS.CO)
- 5.2.1. **RS.CO-02**: Gli stakeholder interni ed esterni sono informati degli incidenti. (Procedure di notifica al CSIRT Italia ex art. 25 D.Lgs. 138/2024.)

### 6. RIPRISTINO (RECOVER) - 2 categorie, 2 sottocategorie

#### 6.1. Esecuzione del piano di ripristino dagli incidenti (RC.RP)
- 6.1.1. **RC.RP-01**: La parte del piano di risposta agli incidenti relativa al ripristino viene eseguita una volta avviata dal processo di risposta agli incidenti.

#### 6.2. Comunicazione sul ripristino dagli incidenti (RC.CO)
- 6.2.1. **RC.CO-03**: Le attivita' di ripristino e i progressi nel ripristino delle capacita' operative sono comunicati agli stakeholder interni ed esterni rilevanti, e ai dirigenti e ai team di leadership.

## Mappatura art. 24 co. 2 D.Lgs. 138/2024 -> Allegato 2 (essenziali)

| Lett. art. 24 co. 2 | Sottocategorie Allegato 2 |
|---------------------|----------------------------|
| a) Politiche di analisi rischi e sicurezza ICT | GV.RM-03, ID.RA-01/05/06/08, GV.PO-01/02 |
| b) Gestione incidenti e notifiche (artt. 25-26) | RS.MA-01, RS.CO-02, ID.IM-04 |
| c) Continuita' operativa (backup, DR, crisi) | RC.RP-01, RC.CO-03, PR.DS-11, PR.IR-03 |
| d) Sicurezza catena di approvvigionamento | GV.SC-01/02/04/05/07 |
| e) SDLC + vulnerability disclosure | PR.PS-01/02/03/04/06, ID.RA-08 |
| f) Valutazione efficacia delle misure | ID.IM-01, GV.RM-03 |
| g) Igiene cyber e formazione | PR.AT-01, PR.AT-02 |
| h) Crittografia / cifratura | PR.DS-01, PR.DS-02 |
| i) Sicurezza personale, controllo accessi, asset mgmt | GV.RR-04, PR.AA-01/03/05/06, ID.AM-01/02/03/04 |
| l) MFA, comunicazioni protette, comm. emergenza | PR.AA-03, PR.IR-01 |

## Differenze Allegato 1 (importanti) vs Allegato 2 (essenziali)

L'Allegato 1 (importanti) ha **37 sottocategorie** (vs 43 dell'Allegato 2). Le sottocategorie aggiuntive presenti **solo per gli essenziali** sono:

| Sottocat. solo essenziali | Funzione | Categoria |
|----------------------------|----------|-----------|
| ID.AM-03 | IDENTIFY | Gestione asset (mappa comunicazioni di rete e flussi dati) |
| PR.AT-02 | PROTECT | Formazione (ruoli specializzati) |
| PR.PS-01 | PROTECT | Sicurezza piattaforme (configuration management) |
| PR.PS-03 | PROTECT | Sicurezza piattaforme (hardware lifecycle) |
| PR.IR-03 | PROTECT | Resilienza infrastruttura (meccanismi di resilienza) |
| RC.CO-03 | RECOVER | Comunicazione ripristino |

Per le sottocategorie comuni, anche **i requisiti puntuali** possono differire fra i due allegati (gli essenziali hanno tipicamente requisiti piu' stringenti). Verificare il testo del PDF per il dettaglio puntuale.

## Tempi di adeguamento (richiamo art. 3 Det. 379907/2025)

- **18 mesi** dalla **comunicazione di inserimento** nell'elenco NIS (art. 7 co. 3 lett. a D.Lgs. 138/2024) per implementare le misure di sicurezza.
- **9 mesi** dalla comunicazione di inserimento per l'avvio dell'obbligo di notifica incidenti significativi.

I termini decorrono dalla **comunicazione personale** ricevuta da ciascun soggetto, non da una data assoluta. Il calcolo "31/10/2026" che appariva su fonti giornalistiche dell'autunno 2025 e' una **stima derivata** (18 mesi dalla notifica del primo elenco di aprile 2025), non un termine fissato dall'articolato della determinazione.
