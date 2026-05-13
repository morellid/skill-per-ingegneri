# Gap Assessment DORA - Pillar 4 (Rischio fornitori terzi TIC) - FastPay S.p.A.

## Profilo dell'entita'

- Categoria (art. 2 par. 1): lettera d (istituto di pagamento ai sensi della direttiva 2015/2366).
- Microimpresa (art. 3 n. 60): no.
- Quadro semplificato (art. 16): **da verificare**. L'utente lo ha invocato come "impresa di investimento piccola e non interconnessa", **ma e' un istituto di pagamento**. Per gli istituti di pagamento, l'art. 16 si applica solo a quelli **esentati ai sensi della direttiva 2015/2366** (cioe' che hanno ottenuto deroga da requisiti di autorizzazione completi). Fino a verifica del professionista, in questo report si assume **quadro completo**. Se il professionista qualifica FastPay nel quadro semplificato dell'art. 16 par. 1, gli obblighi degli artt. 28-30 si applicano comunque (in proporzionalita'), salvo l'esonero del par. 2 dell'art. 28 dalla "strategia per i rischi da terzi" e della politica per le funzioni essenziali o importanti.
- Numero accordi TIC attivi: 47.
- Numero accordi a supporto di funzioni essenziali o importanti: 3 (cloud AWS, switch pagamenti, KYC). **La qualificazione "funzione essenziale o importante" art. 3 n. 22 e' giudizio del professionista**: la skill assume che AWS (cloud) sia funzione essenziale per un istituto di pagamento che vi base la propria infrastruttura, idem per lo switch pagamenti. Per KYC, l'utente lo ha qualificato come essenziale - confermare.
- Data assessment: 2026-05-13.
- Documenti analizzati: Procedura "Gestione Fornitori IT" v1.0; foglio Excel fornitori; modello standard di contratto IT 2022; 3 contratti specifici per fornitori critici.

## Sintesi

| Stato | Numero voci |
| - | - |
| CONFORME | 1 |
| PARZIALE | 7 |
| NON CONFORME | 33 |
| NON APPLICABILE | 1 |
| Totale | 42 |

## Dettaglio per area

### Principi generali (art. 28 parr. 1)

| ID | Articolo | Stato | Evidenza / lacuna |
| - | - | - | - |
| 4.1 | art. 28 par. 1 | PARZIALE | Procedura v1.0 menziona la gestione fornitori ma non integra esplicitamente i rischi terzi nel quadro di gestione del rischio TIC ex art. 6 par. 1. **Azione**: integrare il rischio terzi nel framework di rischio TIC. |
| 4.2 | art. 28 par. 1 | NON CONFORME | Nessuna documentazione che dichiari esplicitamente che FastPay rimane pienamente responsabile per i servizi esternalizzati. **Azione**: introdurre clausola di responsabilita' in policy e in tutti i contratti. |
| 4.3 | art. 28 par. 1 | PARZIALE | La proporzionalita' non e' formalizzata. **Azione**: documentare criteri di valutazione proporzionalita'. |

### Strategia per i rischi da terzi (art. 28 par. 2)

| ID | Articolo | Stato | Evidenza / lacuna |
| - | - | - | - |
| 4.4 | art. 28 par. 2 | NON CONFORME | Nessuna strategia per i rischi TIC da terzi adottata. **Azione URGENTE**: redigere e fare adottare strategia + politica per servizi TIC a supporto di funzioni essenziali. |
| 4.5 | art. 28 par. 2 | NON CONFORME | L'organo di gestione discute i rischi terzi solo 2 volte in 18 mesi: non e' un riesame periodico strutturato. **Azione**: stabilire cadenza minima semestrale di riesame all'organo di gestione. |

### Registro delle informazioni (art. 28 par. 3)

| ID | Articolo | Stato | Evidenza / lacuna |
| - | - | - | - |
| 4.6 | art. 28 par. 3 | PARZIALE | Esiste foglio Excel con 47 fornitori, ma non strutturato come registro DORA. **Azione**: trasformare in registro conforme al formato ITS (rinvio art. 28 par. 9, fuori scope di questa skill). |
| 4.7 | art. 28 par. 3 | NON CONFORME | Excel non distingue gli accordi a supporto di funzioni essenziali da quelli ordinari. **Azione**: introdurre colonna esplicita. |
| 4.8 | art. 28 par. 3 | NON CONFORME | Non sono prodotti registri subconsolidati/consolidati (se FastPay e' standalone, indicare). |
| 4.9 | art. 28 par. 3 | NON CONFORME | Mai comunicato all'autorita' competente. **Azione URGENTE**: predisporre per la prossima comunicazione annuale. |
| 4.10 | art. 28 par. 3 | PARZIALE | Registro disponibile su richiesta? In teoria si' (Excel), ma non strutturato. |
| 4.11 | art. 28 par. 3 | NON CONFORME | Mai inviate informative tempestive su accordi previsti per funzioni essenziali. **Azione URGENTE**. |

### Valutazione preliminare (art. 28 par. 4)

| ID | Articolo | Stato | Evidenza / lacuna |
| - | - | - | - |
| 4.12 | art. 28 par. 4 lettera a | NON CONFORME | Nessuna valutazione formalizzata se l'accordo riguarda una funzione essenziale o importante. **Azione URGENTE**: introdurre step di valutazione obbligatorio nella procedura. |
| 4.13 | art. 28 par. 4 lettera b | NON CONFORME | Nessuna verifica delle condizioni di vigilanza dei fornitori. |
| 4.14 | art. 28 par. 4 lettera c | NON CONFORME | Nessuna valutazione del rischio di concentrazione. **Azione**: in coordinamento con art. 29. |
| 4.15 | art. 28 par. 4 lettera d | NON CONFORME | Nessuna due diligence formalizzata. **Azione URGENTE**: introdurre questionario di due diligence in procedura. |
| 4.16 | art. 28 par. 4 lettera e | NON CONFORME | Nessuna identificazione/valutazione dei conflitti d'interesse. |

### Standard di sicurezza e audit (art. 28 parr. 5-6)

| ID | Articolo | Stato | Evidenza / lacuna |
| - | - | - | - |
| 4.17 | art. 28 par. 5 | PARZIALE | I 3 fornitori critici hanno certificazioni di settore (AWS: SOC2, ISO 27001), ma non e' formalizzato il requisito di standard nei contratti. |
| 4.18 | art. 28 par. 5 | NON CONFORME | Per le funzioni essenziali non e' imposto un requisito di "standard piu' aggiornati ed elevati". |
| 4.19 | art. 28 par. 6 | NON CONFORME | Diritti di audit previsti solo per 1 dei 3 fornitori critici, e mai esercitati. **Azione URGENTE**: introdurre clausole di audit con frequenza in tutti i contratti per funzioni essenziali. |
| 4.20 | art. 28 par. 6 | NON CONFORME | Standard di audit non specificati. |

### Risoluzione e uscita (art. 28 parr. 7-8)

| ID | Articolo | Stato | Evidenza / lacuna |
| - | - | - | - |
| 4.21 | art. 28 par. 7 | PARZIALE | Modello contratto 2022 prevede risoluzione per violazione grave (lettera a), ma non per circostanze che alterano l'esercizio (lettera b), debolezze nella gestione TIC (lettera c), impossibilita' di vigilanza (lettera d). **Azione**: aggiornare il modello contratto. |
| 4.22 | art. 28 par. 8 | NON CONFORME | Nessuna strategia di uscita documentata per i 3 fornitori a supporto di funzioni essenziali. **Azione URGENTE**: redigere strategie di uscita testabili. |
| 4.23 | art. 28 par. 8 | NON CONFORME | Conseguenza di 4.22. |
| 4.24 | art. 28 par. 8 | NON CONFORME | Conseguenza di 4.22. |

### Rischio di concentrazione (art. 29)

| ID | Articolo | Stato | Evidenza / lacuna |
| - | - | - | - |
| 4.25 | art. 29 par. 1 | NON CONFORME | Non valutato. AWS e' singolo punto di concentrazione per cloud. **Azione URGENTE**: analisi di concentrazione e piano di mitigazione (multi-cloud, second source). |
| 4.26 | art. 29 par. 2 | NON CONFORME | 2 fornitori USA non sottoposti a valutazione di rischio paese terzo (diritto fallimentare, protezione dati UE, ecc.). **Azione**: valutazione formale e documentazione. |

### Clausole contrattuali per TUTTI gli accordi (art. 30 par. 2)

| ID | Articolo | Stato | Evidenza / lacuna |
| - | - | - | - |
| 4.27 | art. 30 par. 2 lettera a | PARZIALE | Modello contratto descrive funzioni/servizi ma non sempre subappalti autorizzati. |
| 4.28 | art. 30 par. 2 lettera b | NON CONFORME | Localita' dei dati e preavviso cambio non sempre presenti. |
| 4.29 | art. 30 par. 2 lettera c | CONFORME | Riservatezza presente nel modello standard. Disponibilita'/autenticita'/integrita': in SLA generici, da estendere. |
| 4.30 | art. 30 par. 2 lettera d | NON CONFORME | Garanzie di accesso/ripristino/restituzione dati in caso di insolvenza non presenti nel modello. |
| 4.31 | art. 30 par. 2 lettera e | NON CONFORME | SLA generici, senza descrizione dei livelli di servizio strutturata. |
| 4.32 | art. 30 par. 2 lettera f | NON CONFORME | Assistenza in caso di incidente TIC non disciplinata. |
| 4.33 | art. 30 par. 2 lettera g | NON CONFORME | Cooperazione con autorita' competenti non disciplinata. **Azione URGENTE**. |
| 4.34 | art. 30 par. 2 lettera h | PARZIALE | Diritti di risoluzione presenti ma non conformi attese autorita'. |
| 4.35 | art. 30 par. 2 lettera i | NON CONFORME | Partecipazione del fornitore ai programmi di formazione non disciplinata. |

### Clausole AGGIUNTIVE per funzioni essenziali o importanti (art. 30 par. 3)

| ID | Articolo | Stato | Evidenza / lacuna |
| - | - | - | - |
| 4.36 | art. 30 par. 3 lettera a | NON CONFORME | SLA quantitativi/qualitativi precisi assenti. |
| 4.37 | art. 30 par. 3 lettera b | NON CONFORME | Termini di preavviso e segnalazione sviluppi assenti. |
| 4.38 | art. 30 par. 3 lettera c | NON CONFORME | Obbligo di piani d'emergenza testati assente. |
| 4.39 | art. 30 par. 3 lettera d | NON CONFORME | Obbligo di partecipazione al TLPT assente. **Da verificare se FastPay e' identificata per TLPT ex art. 26 par. 8**: in tal caso urgente. |
| 4.40 | art. 30 par. 3 lettera e | NON CONFORME | Diritti di monitoraggio continuo assenti. **Azione URGENTE**. |
| 4.41 | art. 30 par. 3 lettera f | NON CONFORME | Strategie di uscita con periodo di transizione obbligatorio assenti. |
| 4.42 | art. 30 par. 3 deroga microimprese | NON APPLICABILE | FastPay non e' microimpresa (50 dipendenti). |

## Punti che richiedono giudizio del professionista

1. **Qualificazione DORA dell'entita'**: l'utente ha invocato il quadro semplificato art. 16 par. 1, ma FastPay e' istituto di pagamento, non impresa di investimento. Verificare se rientra negli "istituti di pagamento esentati ai sensi della direttiva 2015/2366" (art. 16 par. 1 lettera relativa). Se SI, applica il quadro semplificato (con esonero parziale dell'art. 28 par. 2). Se NO, applica il quadro completo.
2. **Qualificazione "funzione essenziale o importante"** per ciascuno dei 47 fornitori (oltre ai 3 gia' classificati come essenziali dall'utente): in particolare per i 2 fornitori USA. Art. 3 n. 22.
3. **Identificazione per TLPT** (art. 26 par. 8): da accertare con l'autorita' competente. Se SI, voce 4.39 e' altamente urgente.
4. **Rischio di concentrazione AWS**: la mitigazione del rischio (multi-cloud) e' una scelta strategica con costi elevati. Richiede valutazione costi/benefici e decisione di CdA.

## Avvertenza

Il presente report e' uno strumento di supporto. Il giudizio finale di conformita' DORA, in particolare sulla qualificazione del quadro applicabile (semplificato vs completo) e sulla classificazione di "funzione essenziale o importante" (art. 3 n. 22) per ciascun fornitore, e' responsabilita' del professionista responsabile (CISO, compliance officer, auditor interno o consulente esterno). Le citazioni di articoli sono ricavate dalla trascrizione fedele del Regolamento (UE) 2022/2554 in `references/fonti/reg-ue-2022-2554-dora.md`. Per il formato puntuale del registro delle informazioni vedi le ITS adottate ex art. 28 par. 9 (fuori scope di questa skill di livello 1).
