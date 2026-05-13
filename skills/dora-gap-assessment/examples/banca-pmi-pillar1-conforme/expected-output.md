# Gap Assessment DORA - Pillar 1 (Gestione del rischio TIC) - Banca Esempio S.p.A.

## Profilo dell'entita'

- Categoria (art. 2 par. 1): lettera a (ente creditizio).
- Quadro applicabile: completo (artt. 5-15) - non in regime semplificato (art. 16 par. 1 non si applica alle banche).
- Microimpresa (art. 3 n. 60): no.
- Ente significativo (art. 6 par. 4 reg. 1024/2013): no, less significant institution (LSI). Per le LSI il canale di segnalazione resta a Banca d'Italia, senza trasmissione a BCE (rilevante per Pillar 2).
- Data assessment: 2026-05-13.
- Documenti analizzati: ICT Risk Management Framework v3.2; Digital Operational Resilience Strategy; Policy Information Security 2024; CMDB; ICT BCP/DR v4.0; Crisis Communication Policy v2.1; Backup Policy; Audit Report TIC 2025-02; Programma di formazione TIC 2024.

## Sintesi

| Stato | Numero voci |
| - | - |
| CONFORME | 51 |
| PARZIALE | 4 |
| NON CONFORME | 0 |
| NON APPLICABILE | 2 |
| Totale | 57 |

## Dettaglio per area

### Governance (art. 5)

| ID | Articolo | Stato | Evidenza | Lacuna / raccomandazione |
| - | - | - | - | - |
| 1.1 | art. 5 par. 1 | CONFORME | ICT Risk Management Framework v3.2 approvato CdA, integra controllo interno e linea di difesa indipendente | - |
| 1.2 | art. 5 par. 2 lettere a-i | CONFORME | CdA approva framework, strategia, BCP/DR, audit, risorse, fornitori; canale segnalazione su accordi terzi formalizzato | - |
| 1.3 | art. 5 par. 4 | CONFORME | 3 membri organo di gestione in formazione DORA 2025; formazione TIC annuale per tutto CdA | - |
| 1.3bis | art. 5 par. 3 | CONFORME | Vendor Management Office con responsabile designato a riporto del CRO sovrintende gli accordi con fornitori TIC | - |

### Quadro di gestione del rischio TIC (art. 6)

| ID | Articolo | Stato | Evidenza | Lacuna / raccomandazione |
| - | - | - | - | - |
| 1.4 | art. 6 par. 1 | CONFORME | ICT Risk Management Framework v3.2 integrato nel sistema di gestione del rischio | - |
| 1.5 | art. 6 par. 2 | CONFORME | Framework comprende politiche, procedure, strumenti | - |
| 1.6 | art. 6 par. 4 | CONFORME | ICT Risk Management Office indipendente, riporta a CRO | - |
| 1.7 | art. 6 par. 5 | CONFORME | Riesame annuale 2024-11-15 | - |
| 1.8 | art. 6 par. 6 | CONFORME | Audit interno TIC annuale eseguito da Internal Audit indipendente | - |
| 1.9 | art. 6 par. 7 | CONFORME | Processo di follow-up sui risultati critici dell'audit gestito da Internal Audit | - |
| 1.10 | art. 6 par. 8 lettere a-h | CONFORME | Digital Operational Resilience Strategy include obiettivi, KPI/KRI, mappa interdipendenze, tolleranza, multi-fornitore cloud | - |

### Sistemi, protocolli, strumenti (art. 7)

| ID | Articolo | Stato | Evidenza | Lacuna / raccomandazione |
| - | - | - | - | - |
| 1.11 | art. 7 lettere a-d | CONFORME | Sistemi TIC valutati adeguati nell'ultimo audit | - |

### Identificazione (art. 8)

| ID | Articolo | Stato | Evidenza | Lacuna / raccomandazione |
| - | - | - | - | - |
| 1.12 | art. 8 par. 1 | CONFORME | Inventario funzioni di business e ruoli TIC documentato in CMDB; riesame annuale | - |
| 1.13 | art. 8 par. 2 | CONFORME | Scenari di rischio TIC riesaminati annualmente | - |
| 1.14 | art. 8 par. 3 | CONFORME | Valutazione del rischio dopo ogni change rilevante (processo formale) | - |
| 1.15 | art. 8 par. 4 | CONFORME | CMDB con configurazioni, interdipendenze | - |
| 1.16 | art. 8 par. 5 | CONFORME | Fornitori terzi TIC mappati nel registro (Pillar 4) | - |
| 1.17 | art. 8 par. 6 | CONFORME | CMDB aggiornato in continuo | - |
| 1.18 | art. 8 par. 7 | CONFORME | 12 sistemi obsoleti identificati con piano di dismissione Q4 2024 | - |

### Protezione e prevenzione (art. 9)

| ID | Articolo | Stato | Evidenza | Lacuna / raccomandazione |
| - | - | - | - | - |
| 1.19 | art. 9 par. 1 | CONFORME | SOC 24/7 monitora sistemi | - |
| 1.20 | art. 9 par. 2 | CONFORME | Policy Information Security 2024 con focus su resilienza/CIA | - |
| 1.21 | art. 9 par. 3 | CONFORME | Procedure DLP, secure transfer, anti-data leakage in policy | - |
| 1.22 | art. 9 par. 4 lettera a | CONFORME | Policy ISMS documentata | - |
| 1.23 | art. 9 par. 4 lettera b | PARZIALE | Segmentazione rete documentata ma procedura di "disconnessione di emergenza" testata solo una volta nel 2023 | Programmare test annuale della procedura di disconnessione/segmentazione |
| 1.24 | art. 9 par. 4 lettera c | CONFORME | IAM con least privilege, autenticazione MFA, monitoraggio anomalie utenti | - |
| 1.25 | art. 9 par. 4 lettera d | CONFORME | HSM per gestione chiavi, MFA per utenti privilegiati | - |
| 1.26 | art. 9 par. 4 lettera e | CONFORME | Change management TIC con CAB approvato dal CTO | - |
| 1.27 | art. 9 par. 4 lettera f | CONFORME | Patch management con SLA documentati | - |

### Individuazione (art. 10)

| ID | Articolo | Stato | Evidenza | Lacuna / raccomandazione |
| - | - | - | - | - |
| 1.28 | art. 10 par. 1 | CONFORME | SIEM + EDR + anomaly detection di rete | - |
| 1.29 | art. 10 par. 1 (rinvio art. 25) | CONFORME | Test regolari dei meccanismi (vedi Pillar 3) | - |
| 1.30 | art. 10 par. 2 | CONFORME | Soglie e procedure di escalation documentate nel SOC playbook | - |
| 1.31 | art. 10 par. 3 | CONFORME | SOC 24/7 con risorse dedicate | - |

### Risposta e ripristino (art. 11)

| ID | Articolo | Stato | Evidenza | Lacuna / raccomandazione |
| - | - | - | - | - |
| 1.32 | art. 11 par. 1 | CONFORME | ICT BCP v4.0 approvato | - |
| 1.33 | art. 11 par. 2 lettere a-e | CONFORME | BCP/DR copre continuita', risposta, contenimento, stima impatto, comunicazione di crisi | - |
| 1.34 | art. 11 par. 3 | CONFORME | BCP/DR sottoposti a riesame indipendente da Internal Audit | - |
| 1.35 | art. 11 par. 4 | CONFORME | BCP testato annualmente (tavolino) e per funzioni esternalizzate | - |
| 1.36 | art. 11 par. 5 | CONFORME | BIA documentata e aggiornata 2024-09 con criteri quantitativi/qualitativi, copertura interdipendenze | - |
| 1.37 | art. 11 par. 6 | CONFORME | Test annuale BCP e DR, test post-change rilevante | - |
| 1.38 | art. 11 par. 7 | CONFORME | Crisis Management Function con Head of Crisis Mgmt designato | - |
| 1.39 | art. 11 par. 8 | CONFORME | Log delle attivita' di disfunzione archiviati in SIEM con retention 12 mesi | - |
| 1.40 | art. 11 par. 10 | CONFORME | Capacita' di stima costi/perdite documentata in BIA | - |

### Backup, ripristino, recupero (art. 12)

| ID | Articolo | Stato | Evidenza | Lacuna / raccomandazione |
| - | - | - | - | - |
| 1.41 | art. 12 par. 1 lettera a | CONFORME | Backup policy con frequenza/criticita' documentata | - |
| 1.42 | art. 12 par. 1 lettera b | CONFORME | Procedure di ripristino documentate | - |
| 1.43 | art. 12 par. 2 | CONFORME | Backup testati semestralmente | - |
| 1.44 | art. 12 par. 3 | CONFORME | Backup su data center secondario logicamente segregato, immutabile per 30 giorni | - |
| 1.45 | art. 12 par. 4 | CONFORME | Capacita' ridondanti su data center secondario | - |
| 1.46 | art. 12 par. 6 | CONFORME | RPO/RTO approvati dall'organo di gestione | - |

### Apprendimento e formazione (art. 13)

| ID | Articolo | Stato | Evidenza | Lacuna / raccomandazione |
| - | - | - | - | - |
| 1.47 | art. 13 par. 1 | CONFORME | Threat intelligence interna + abbonamento a feed esterni (vedi anche Pillar 5) | - |
| 1.48 | art. 13 par. 2 | PARZIALE | Riesami post-incidente eseguiti per i 2 incidenti gravi del 2024, ma non sistematizzati per tutti gli incidenti minori che hanno toccato funzioni essenziali | Estendere il riesame post-incidente anche agli incidenti minori su funzioni essenziali |
| 1.49 | art. 13 par. 3 | CONFORME | Lessons learned 2024 incorporati nella v3.2 del framework | - |
| 1.50 | art. 13 par. 4 | CONFORME | Monitoraggio KPI/KRI riportato trimestralmente a comitato rischi | - |
| 1.51 | art. 13 par. 5 | CONFORME | Report annuale del CISO al CdA con raccomandazioni | - |
| 1.52 | art. 13 par. 6 | CONFORME | Programma di formazione obbligatorio per tutti (compliance 96%) e per alti dirigenti | - |
| 1.53 | art. 13 par. 7 | PARZIALE | Monitoraggio sviluppi tecnologici documentato in report semestrale del CTO, ma non c'e' link esplicito con la valutazione del rischio TIC | Esplicitare nel framework il link tra horizon scanning tecnologico e aggiornamento del registro dei rischi TIC |

### Comunicazione (art. 14)

| ID | Articolo | Stato | Evidenza | Lacuna / raccomandazione |
| - | - | - | - | - |
| 1.54 | art. 14 par. 1 | CONFORME | Crisis Communication Policy v2.1 | - |
| 1.55 | art. 14 par. 2 | PARZIALE | Policy comunicazione cliente/personale dettagliata; comunicazione esterna a media meno dettagliata | Estendere la policy con un capitolo "comunicazione ai media in crisi" |
| 1.56 | art. 14 par. 3 | CONFORME | Head of Communications designata responsabile della strategia di comunicazione incidenti | - |

### Quadro semplificato (art. 16)

| ID | Articolo | Stato | Motivazione |
| - | - | - | - |
| 1.57 | art. 16 par. 1 | NON APPLICABILE | Banca Esempio S.p.A. non rientra tra le entita' dell'art. 16 par. 1 (imprese di investimento piccole e non interconnesse, istituti di pagamento esentati, ecc.) |
| -    | art. 3 n. 60 | NON APPLICABILE | Banca con 200K clienti, non microimpresa |

## Punti che richiedono giudizio del professionista

Voci PARZIALI che richiedono validazione del CISO/compliance officer:

1. **1.23 (art. 9 par. 4 lettera b)** - Programmazione del test annuale della procedura di disconnessione/segmentazione di rete.
2. **1.48 (art. 13 par. 2)** - Estensione del riesame post-incidente agli incidenti minori su funzioni essenziali; richiede definizione della soglia "incidente minore su funzione essenziale".
3. **1.53 (art. 13 par. 7)** - Esplicitazione del link tra horizon scanning tecnologico e registro dei rischi TIC.
4. **1.55 (art. 14 par. 2)** - Estensione della policy con capitolo "comunicazione ai media in crisi".

Voci NON APPLICABILE confermate (art. 16 par. 1, art. 3 n. 60 - banca non rientra in quadro semplificato ne' in microimpresa).

## Avvertenza

Il presente report e' uno strumento di supporto. Il giudizio finale di conformita' DORA, in particolare sulle interpretazioni dell'art. 4 (proporzionalita'), art. 16 (quadro semplificato), e sulla qualificazione di "funzione essenziale o importante" e "grave incidente TIC", e' responsabilita' del professionista responsabile (CISO, compliance officer, auditor interno o consulente esterno). Le citazioni di articoli sono ricavate dalla trascrizione fedele del Regolamento (UE) 2022/2554 in `references/fonti/reg-ue-2022-2554-dora.md`; consultarla per il riscontro testuale.
