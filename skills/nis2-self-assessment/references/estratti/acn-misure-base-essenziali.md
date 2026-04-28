# Det. ACN n. 164179/2025 - Allegato 2 - Misure di base per soggetti essenziali

> Fonte: Agenzia per la Cybersicurezza Nazionale, Determinazione n. 164179 del 14 aprile 2025, Allegato 2.
> Fonte catalogata in `sources.yaml` come `acn-det-164179-2025`.
> Estratto strutturale: funzioni, categorie e sottocategorie del Framework Nazionale Cybersecurity ed. 2025 utilizzate. Per il testo verbatim dei requisiti di ogni sottocategoria, fare riferimento al PDF in `not_in_repo/acn-det-164179-2025-allegato2.pdf`.
> Data consultazione: 2026-04-29.
>
> **Avvertenza**: la Determinazione ACN 164179/2025 e' stata sostituita dalla **Determinazione ACN 379907/2025** (in vigore dal 15 gennaio 2026), che aggiorna le misure di base. La struttura per funzioni/categorie/sottocategorie e' coerente; il dettaglio dei requisiti puo' differire. Verificare l'ultima determinazione vigente sul portale ACN prima di citare requisiti specifici.

## Struttura per funzioni del Framework Nazionale Cybersecurity (ed. 2025)

L'Allegato 2 (soggetti essenziali) e' organizzato in **6 funzioni**, **18 categorie** e **35 sottocategorie**.

### 1. GOVERNO (GOVERN) - 5 categorie

#### 1.1. Contesto organizzativo (GV.OC)
- 1.1.1. **GV.OC-4**: Obiettivi, capacita' e servizi critici dai quali gli stakeholder dipendono sono compresi e comunicati. (Elenco aggiornato dei sistemi informativi e di rete rilevanti.)

#### 1.2. Strategia di gestione del rischio (GV.RM)
- 1.2.1. **GV.RM-03**: Le attivita' e gli esiti della gestione del rischio di cybersecurity sono parte integrante dei processi di risk management. (Piano di gestione dei rischi documentato e aggiornato.)

#### 1.3. Ruoli, responsabilita' e correlati poteri (GV.RR)
- 1.3.1. **GV.RR-02**: Ruoli, responsabilita' e poteri stabiliti, comunicati, applicati. (Organizzazione per la sicurezza informatica approvata dal CdA. Punto di contatto NIS + sostituto. Riesame almeno biennale o post-incidente.)
- 1.3.2. **GV.RR-04**: Cybersecurity inclusa nelle pratiche HR. (Vetting di personale autorizzato e amministratori di sistema. Clausole contrattuali post-cessazione.)

#### 1.4. Politica (GV.PO)
- 1.4.1. **GV.PO-01**: Politica per la gestione del rischio cyber stabilita, comunicata, applicata. (16 ambiti di policy obbligatori: gestione del rischio, ruoli e responsabilita', risorse umane, conformita' e audit, supply chain, asset management, vulnerabilita', BCM/DR/crisi, autenticazione e accessi, sicurezza fisica, formazione, sicurezza dati, sviluppo/configurazione/manutenzione/dismissione, protezione reti/comunicazioni, monitoring eventi, response & recovery. Politiche **approvate dagli organi di amministrazione**.)
- 1.4.2. **GV.PO-02**: La politica e' revisionata e aggiornata.

#### 1.5. Gestione del rischio della catena di approvvigionamento (GV.SC)
- 1.5.1. **GV.SC-01**: Programma supply chain risk management stabilito.
- 1.5.2. **GV.SC-02**: Ruoli e responsabilita' definiti per fornitori, clienti, partner.
- 1.5.3. **GV.SC-04**: Fornitori noti e prioritizzati per criticita'.
- 1.5.4. **GV.SC-05**: Requisiti contrattuali per i rischi di cybersecurity in supply chain.
- 1.5.5. **GV.SC-07**: Rischi da fornitori, prodotti, servizi e terze parti sono compresi.

### 2. IDENTIFICAZIONE (IDENTIFY) - 3 categorie

#### 2.1. Gestione degli asset (ID.AM)
- 2.1.1. **ID.AM-01**: Inventari dell'hardware gestito.
- 2.1.2. **ID.AM-02**: Inventari del software, servizi, sistemi gestiti.
- 2.1.3. **ID.AM-03**: Rappresentazioni delle comunicazioni di rete e dei flussi di dati.
- 2.1.4. **ID.AM-04**: Inventari dei servizi erogati dai fornitori.

#### 2.2. Valutazione del rischio (ID.RA)
- 2.2.1. **ID.RA-01**: Vulnerabilita' negli asset identificate, confermate, registrate.
- 2.2.2. **ID.RA-05**: Minacce, vulnerabilita', probabilita' e impatti combinate per analisi del rischio.
- 2.2.3. **ID.RA-06**: Risposte al rischio scelte, prioritizzate, pianificate, monitorate.
- 2.2.4. **ID.RA-08**: Processi per ricezione, analisi e risposta a divulgazione di vulnerabilita'.

#### 2.3. Miglioramento (ID.IM)
- 2.3.1. **ID.IM-01**: Miglioramenti identificati a valle delle valutazioni.
- 2.3.2. **ID.IM-04**: Piani di risposta agli incidenti aggiornati e testati.

### 3. PROTEZIONE (PROTECT) - 5 categorie

#### 3.1. Gestione delle identita', autenticazione e controllo degli accessi (PR.AA)
- 3.1.1. **PR.AA-01**: Identita' e credenziali gestite.
- 3.1.2. **PR.AA-03**: Utenti, servizi, hardware autenticati. (MFA per accessi privilegiati.)
- 3.1.3. **PR.AA-05**: Permessi, diritti, autorizzazioni di accesso definiti in policy. (Least privilege, separazione compiti.)
- 3.1.4. **PR.AA-06**: Accesso fisico agli asset gestito.

#### 3.2. Consapevolezza e formazione (PR.AT)
- 3.2.1. **PR.AT-01**: Personale sensibilizzato e formato.
- 3.2.2. **PR.AT-02**: Ruoli specializzati con formazione mirata.

#### 3.3. Sicurezza dei dati (PR.DS)
- 3.3.1. **PR.DS-01**: Riservatezza/integrita'/disponibilita' dei dati a riposo. (Crittografia per dati sensibili.)
- 3.3.2. **PR.DS-02**: Riservatezza/integrita'/disponibilita' dei dati in transito.
- 3.3.3. **PR.DS-11**: Backup dei dati creati, protetti, mantenuti, verificati.

#### 3.4. Sicurezza delle piattaforme (PR.PS)
- 3.4.1. **PR.PS-01**: Configuration management.
- 3.4.2. **PR.PS-02**: Software mantenuto, sostituito, rimosso in base al rischio.
- 3.4.3. **PR.PS-03**: Hardware mantenuto, sostituito, rimosso in base al rischio.
- 3.4.4. **PR.PS-04**: Registri di log generati e disponibili per monitoraggio continuo.
- 3.4.5. **PR.PS-06**: Pratiche di sviluppo sicuro del software (SSDLC).

#### 3.5. Resilienza dell'infrastruttura tecnologica (PR.IR)
- 3.5.1. **PR.IR-01**: Reti e ambienti protetti dall'accesso logico/uso non autorizzati. (Segmentazione, firewall, IDS/IPS.)
- 3.5.2. **PR.IR-03**: Meccanismi di resilienza in situazioni avverse.

### 4. RILEVAMENTO (DETECT) - 1 categoria

#### 4.1. Monitoraggio continuo (DE.CM)
- 4.1.1. **DE.CM-01**: Reti e servizi di rete monitorati per eventi anomali. (SIEM o equivalente.)
- 4.1.2. **DE.CM-09**: Hardware/software di elaborazione monitorati.

### 5. RISPOSTA (RESPOND) - 2 categorie

#### 5.1. Gestione degli incidenti (RS.MA)
- 5.1.1. **RS.MA-01**: Piano di risposta agli incidenti eseguito in coordinamento con terze parti.

#### 5.2. Segnalazione e comunicazione (RS.CO)
- 5.2.1. **RS.CO-02**: Stakeholder interni ed esterni informati degli incidenti. (Procedure di notifica al CSIRT Italia ex art. 25 D.Lgs. 138/2024.)

### 6. RIPRISTINO (RECOVER) - 2 categorie

#### 6.1. Esecuzione del piano di ripristino (RC.RP)
- 6.1.1. **RC.RP-01**: Parte del piano di risposta relativa al ripristino eseguita.

#### 6.2. Comunicazione sul ripristino (RC.CO)
- 6.2.1. **RC.CO-03**: Attivita' di ripristino e progressi comunicati.

## Mappatura art. 24 co. 2 D.Lgs. 138/2024 -> Allegato 2 ACN

| Lett. art. 24 co. 2 | Categorie/sottocategorie ACN |
|---------------------|-------------------------------|
| a) Politiche di analisi rischi e sicurezza | GV.RM, ID.RA, GV.PO |
| b) Gestione incidenti e notifiche | RS.MA, RS.CO, ID.IM-04 |
| c) Continuita' operativa | RC.RP, RC.CO, PR.DS-11 (backup), PR.IR-03 |
| d) Sicurezza catena approvvigionamento | GV.SC (tutte) |
| e) Sicurezza acquisizione/sviluppo/manutenzione + vuln. disclosure | PR.PS-01..06, ID.RA-08 |
| f) Valutazione efficacia | ID.IM-01, GV.RM-03 |
| g) Igiene cyber e formazione | PR.AT-01, PR.AT-02 |
| h) Crittografia / cifratura | PR.DS-01, PR.DS-02 |
| i) Sicurezza personale, controllo accessi, asset mgmt | GV.RR-04, PR.AA, ID.AM, PR.AA-06 |
| l) MFA, comunicazioni protette, comm. emergenza | PR.AA-03, PR.IR-01 |

## Numerica complessiva

- Soggetti essenziali (Allegato 2): ~ 35 sottocategorie / requisiti elencati nella Det. 164179/2025.
- Soggetti importanti (Allegato 1): sottoinsieme piu' ridotto - vedi `acn-misure-base-importanti.md`.
- Aggiornamento al 2026: la Det. **379907/2025** porta a 43 misure / 116 requisiti per essenziali e 37 misure / 87 requisiti per importanti (verificare il testo aggiornato).

## Tempi di adeguamento

- **18 mesi** dalla notifica di inserimento nell'elenco NIS per implementare le misure di sicurezza.
- **9 mesi** dalla notifica per l'obbligo di notifica incidenti significativi.
- **31 ottobre 2026**: termine ultimo per la piena operativita' delle misure di base (art. 4 Det. 379907/2025). Dopo tale data l'ACN passa dalla fase di accompagnamento alla fase ispettiva.
