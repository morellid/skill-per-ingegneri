# Det. ACN 379907/2025 - Allegato 1 - Misure di base per soggetti importanti

> Fonte: Agenzia per la Cybersicurezza Nazionale, Determinazione del Direttore Generale del 18/12/2025 (protocollo 379907/2025), Allegato 1.
> Fonte catalogata in `sources.yaml` come `acn-det-379907-allegato-1`.
> URL canonico: https://www.acn.gov.it/portale/documents/d/guest/allegato-1-v2
> Estratto: struttura completa per funzioni/categorie/sottocategorie. Per il testo verbatim dei requisiti puntuali fare riferimento al PDF in `not_in_repo/acn-allegato-1-v2.pdf` (SHA256 catalogato).
> Data consultazione: 2026-04-29.

## Inquadramento

Allegato 1 della Det. ACN 379907/2025 (in vigore dal 15/01/2026, art. 9 co. 3, sostitutiva della Det. 164179/2025). Si applica ai **soggetti importanti** ai sensi dell'art. 6 co. 3 D.Lgs. 138/2024 e definisce le **specifiche di base** per gli adempimenti agli obblighi degli artt. 23 e 24 D.Lgs. 138/2024.

L'organizzazione segue il **Framework Nazionale per la Cybersecurity e la Data Protection ed. 2025**.

## Struttura

L'Allegato 1 (importanti) e' organizzato in:
- **6 funzioni** (GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER)
- **18 categorie**
- **37 sottocategorie**
- **87 requisiti operativi** (conteggio numerato dal PDF)

### Lista delle 37 sottocategorie

#### 1. GOVERNO (GOVERN) - 11 sottocategorie

##### 1.1. Contesto organizzativo (GV.OC)
- 1.1.1. **GV.OC-04**: Obiettivi, capacita' e servizi critici dai quali gli stakeholder dipendono sono compresi e comunicati.

##### 1.2. Strategia di gestione del rischio (GV.RM)
- 1.2.1. **GV.RM-03**: La gestione del rischio cyber e' parte integrante dei processi di risk management.

##### 1.3. Ruoli, responsabilita' e correlati poteri (GV.RR)
- 1.3.1. **GV.RR-02**: Ruoli, responsabilita' e poteri stabiliti, comunicati, applicati. (Organizzazione per la sicurezza informatica **approvata dagli organi di amministrazione e direttivi**.)
- 1.3.2. **GV.RR-04**: Cybersecurity inclusa nelle pratiche HR.

##### 1.4. Politica (GV.PO)
- 1.4.1. **GV.PO-01**: Politica per la gestione del rischio cyber stabilita, comunicata, applicata. (Politiche **approvate dagli organi di amministrazione e direttivi**.)
- 1.4.2. **GV.PO-02**: Politica revisionata, aggiornata, comunicata, applicata.

##### 1.5. Gestione del rischio della catena di approvvigionamento (GV.SC)
- 1.5.1. **GV.SC-01**: Programma SCRM stabilito.
- 1.5.2. **GV.SC-02**: Ruoli e responsabilita' cyber per fornitori, clienti, partner.
- 1.5.3. **GV.SC-04**: Fornitori noti e prioritizzati per criticita'.
- 1.5.4. **GV.SC-05**: Requisiti contrattuali per i rischi cyber in supply chain.
- 1.5.5. **GV.SC-07**: Rischi da fornitori, prodotti, servizi e terze parti compresi e monitorati.

#### 2. IDENTIFICAZIONE (IDENTIFY) - 9 sottocategorie

##### 2.1. Gestione degli asset (ID.AM)
- 2.1.1. **ID.AM-01**: Inventari hardware.
- 2.1.2. **ID.AM-02**: Inventari software, servizi, sistemi.
- 2.1.3. **ID.AM-04**: Inventari servizi dei fornitori.

(NB: l'Allegato 1 NON include `ID.AM-03` - mappa flussi rete/dati - presente invece nell'Allegato 2 essenziali.)

##### 2.2. Valutazione del rischio (ID.RA)
- 2.2.1. **ID.RA-01**: Vulnerabilita' negli asset identificate, confermate, registrate.
- 2.2.2. **ID.RA-05**: Combinazione di minacce/vuln./prob./impatti per analisi rischio.
- 2.2.3. **ID.RA-06**: Risposte al rischio scelte, prioritizzate, pianificate, monitorate.
- 2.2.4. **ID.RA-08**: Processi di vulnerability disclosure.

##### 2.3. Miglioramento (ID.IM)
- 2.3.1. **ID.IM-01**: Miglioramenti identificati a valle delle valutazioni.
- 2.3.2. **ID.IM-04**: Piani di IR aggiornati.

#### 3. PROTEZIONE (PROTECT) - 11 sottocategorie

##### 3.1. Gestione delle identita', autenticazione e controllo degli accessi (PR.AA)
- 3.1.1. **PR.AA-01**: Identita' e credenziali gestite.
- 3.1.2. **PR.AA-03**: Utenti, servizi, hardware autenticati. (MFA per accessi privilegiati e remoti.)
- 3.1.3. **PR.AA-05**: Permessi/diritti/autorizzazioni in policy. (Least privilege, separazione compiti.)
- 3.1.4. **PR.AA-06**: Accesso fisico agli asset gestito.

##### 3.2. Consapevolezza e formazione (PR.AT)
- 3.2.1. **PR.AT-01**: Personale sensibilizzato e formato.

(NB: l'Allegato 1 NON include `PR.AT-02` - ruoli specializzati - presente invece nell'Allegato 2.)

##### 3.3. Sicurezza dei dati (PR.DS)
- 3.3.1. **PR.DS-01**: Riservatezza/integrita'/disponibilita' dati a riposo. (Crittografia per dati sensibili.)
- 3.3.2. **PR.DS-02**: Riservatezza/integrita'/disponibilita' dati in transito.
- 3.3.3. **PR.DS-11**: Backup creati, protetti, mantenuti, verificati.

##### 3.4. Sicurezza delle piattaforme (PR.PS)
- 3.4.1. **PR.PS-02**: Software mantenuto, sostituito, rimosso in base al rischio.
- 3.4.2. **PR.PS-04**: Logging centralizzato per monitoraggio continuo.
- 3.4.3. **PR.PS-06**: Pratiche di sviluppo sicuro del software (SSDLC).

(NB: l'Allegato 1 NON include `PR.PS-01` (configuration management) ne' `PR.PS-03` (hardware lifecycle), presenti nell'Allegato 2.)

##### 3.5. Resilienza dell'infrastruttura tecnologica (PR.IR)
- 3.5.1. **PR.IR-01**: Reti e ambienti protetti dall'accesso logico/uso non autorizzati. (Segmentazione, firewall, IDS/IPS.)

(NB: l'Allegato 1 NON include `PR.IR-03` - meccanismi di resilienza - presente nell'Allegato 2.)

#### 4. RILEVAMENTO (DETECT) - 2 sottocategorie

##### 4.1. Monitoraggio continuo (DE.CM)
- 4.1.1. **DE.CM-01**: Reti e servizi di rete monitorati per eventi anomali.
- 4.1.2. **DE.CM-09**: Hardware/software di elaborazione monitorati.

#### 5. RISPOSTA (RESPOND) - 2 sottocategorie

##### 5.1. Gestione degli incidenti (RS.MA)
- 5.1.1. **RS.MA-01**: Piano IR eseguito in coordinamento con terze parti.

##### 5.2. Segnalazione e comunicazione (RS.CO)
- 5.2.1. **RS.CO-02**: Stakeholder interni ed esterni informati degli incidenti. (Procedure di notifica al CSIRT Italia ex art. 25 D.Lgs. 138/2024.)

#### 6. RIPRISTINO (RECOVER) - 1 sottocategoria

##### 6.1. Esecuzione del piano di ripristino (RC.RP)
- 6.1.1. **RC.RP-01**: Parte del piano IR relativa al ripristino eseguita.

(NB: l'Allegato 1 NON include `RC.CO-03` - comunicazione ripristino - presente nell'Allegato 2.)

## Mappatura art. 24 co. 2 D.Lgs. 138/2024 -> Allegato 1 (importanti)

| Lett. art. 24 co. 2 | Sottocategorie Allegato 1 |
|---------------------|----------------------------|
| a) Politiche di analisi rischi e sicurezza ICT | GV.RM-03, ID.RA-01/05/06/08, GV.PO-01/02 |
| b) Gestione incidenti e notifiche | RS.MA-01, RS.CO-02, ID.IM-04 |
| c) Continuita' operativa | RC.RP-01, PR.DS-11 |
| d) Sicurezza catena di approvvigionamento | GV.SC-01/02/04/05/07 |
| e) SDLC + vulnerability disclosure | PR.PS-02/04/06, ID.RA-08 |
| f) Valutazione efficacia delle misure | ID.IM-01, GV.RM-03 |
| g) Igiene cyber e formazione | PR.AT-01 |
| h) Crittografia / cifratura | PR.DS-01, PR.DS-02 |
| i) Sicurezza personale, controllo accessi, asset mgmt | GV.RR-04, PR.AA-01/03/05/06, ID.AM-01/02/04 |
| l) MFA, comunicazioni protette, comm. emergenza | PR.AA-03, PR.IR-01 |

## Tempi di adeguamento (richiamo art. 3 Det. 379907/2025)

- **18 mesi** dalla **comunicazione di inserimento** nell'elenco NIS per implementare le misure di sicurezza.
- **9 mesi** dalla comunicazione di inserimento per l'avvio dell'obbligo di notifica incidenti significativi.

I termini decorrono dalla comunicazione personale, non da una data assoluta.

## Note di confronto con gli essenziali

Le **6 sottocategorie aggiuntive** dei soggetti essenziali (rispetto agli importanti) sono:
- `ID.AM-03` (mappa comunicazioni di rete e flussi dati)
- `PR.AT-02` (formazione ruoli specializzati)
- `PR.PS-01` (configuration management)
- `PR.PS-03` (hardware lifecycle)
- `PR.IR-03` (meccanismi di resilienza)
- `RC.CO-03` (comunicazione ripristino)

Anche per le sottocategorie comuni il **dettaglio dei requisiti puntuali** puo' essere meno stringente per gli importanti rispetto agli essenziali. Verificare il testo del PDF per ciascuna sottocategoria.
