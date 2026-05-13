# Pillar 3 - Gap assessment: Test di resilienza operativa digitale (DORA artt. 24-27)

## Obiettivo

Mappare le pratiche dell'entita' finanziaria in materia di programma di test di resilienza operativa digitale, test di strumenti e sistemi TIC, Threat-Led Penetration Testing (TLPT) e requisiti dei soggetti incaricati, rispetto agli obblighi degli artt. 24-27 del Regolamento (UE) 2022/2554 (DORA).

## Input richiesti

Chiedere all'utente:

1. **Identificazione dell'entita'**:
   - Categoria DORA (art. 2 par. 1 lettere a-u).
   - Microimpresa (art. 3 n. 60): si' / no. **Le microimprese sono escluse dagli artt. 24-25 nel modo specifico previsto dall'art. 25 par. 3 (combinazione approccio basato sul rischio + pianificazione strategica)**.
   - Quadro semplificato (art. 16 par. 1): se applicabile, l'entita' e' **esclusa dal TLPT obbligatorio dell'art. 26 par. 1**.
   - L'entita' e' stata identificata dall'autorita' competente come tenuta al TLPT (art. 26 par. 8)? Per gli enti creditizi significativi: ricorre solo a test esterni (art. 26 par. 8).
   - Depositario centrale di titoli o controparte centrale? (Obbligo specifico art. 25 par. 2 di valutazioni delle vulnerabilita' prima di ciascun rilascio).
2. **Documentazione disponibile**:
   - Programma di test di resilienza operativa digitale (Digital Operational Resilience Testing Programme).
   - Metodologia di test (scoping, classificazione di vulnerabilita', remediation tracking).
   - Politica di indipendenza dei tester interni/esterni.
   - Calendario test annuale (per sistemi/applicazioni TIC che supportano funzioni essenziali o importanti).
   - Per TLPT: scope document, threat intelligence report, plan, end-of-test report.
   - Contratti con soggetti esterni incaricati dei test, in particolare TLPT (art. 27 par. 3).
3. **Evidenze operative**:
   - Anno dell'ultimo test annuale eseguito sui sistemi a supporto di funzioni essenziali o importanti.
   - Anno dell'ultimo TLPT eseguito.
   - Tipi di test eseguiti negli ultimi 12 mesi (vulnerability scan, pentest, red team, scenario-based, end-to-end, source code review, ecc.).
   - Esistenza di un processo di remediation con tracciamento e SLA.

## Fonti

- Trascrizione del Regolamento DORA: `references/fonti/reg-ue-2022-2554-dora.md`.
- Estratti curati Pillar 3: `references/estratti/reg-ue-2022-2554-dora.md` sezione "Pillar 3 - Test di resilienza operativa digitale".
- In particolare:
  - Art. 24: requisiti generali per il programma di test.
  - Art. 25: test di strumenti e sistemi TIC.
  - Art. 26: TLPT.
  - Art. 27: requisiti dei soggetti incaricati dei TLPT.

## Procedura

Per ciascuna delle voci di controllo:

1. Confronta le evidenze documentali/operative raccolte con l'obbligo DORA.
2. Cita l'articolo e paragrafo esatto.
3. Classifica lo stato: **CONFORME** / **PARZIALE** / **NON CONFORME** / **NON APPLICABILE** (con motivazione esplicita).
4. Per microimpresa o quadro semplificato: applicare le esclusioni specifiche degli artt. 25 par. 3 e 26 par. 1.
5. Per il TLPT: verificare se l'entita' rientra tra quelle identificate ai sensi dell'art. 26 par. 8; se non identificata, marcare le voci TLPT (3.13-3.20) come **NON APPLICABILE - non identificata ai sensi dell'art. 26 par. 8**.

### Voci di controllo

**Programma generale (art. 24)**:
3.1 Le entita' diverse dalle microimprese stabiliscono, mantengono e riesaminano un programma di test di resilienza operativa digitale solido ed esaustivo (par. 1), come parte integrante del quadro per la gestione del rischio TIC?
3.2 Il programma comprende valutazioni, test, metodologie, pratiche e strumenti degli artt. 25-26 (par. 2)?
3.3 Approccio basato sul rischio conforme all'art. 4 par. 2 (par. 3): proporzionalita' rispetto a dimensioni/profilo/natura, considerazione di mutevole contesto, rischi specifici, criticita' di patrimoni informativi e servizi?
3.4 I test sono svolti da soggetti **indipendenti** interni o esterni (par. 4)? Per test interni: risorse sufficienti, evitare conflitti d'interesse?
3.5 Esistono procedure e politiche per priorita', classificazione e rimedio dei problemi rilevati nei test, e metodologie di convalida interna (par. 5)?
3.6 **Test adeguati svolti almeno annualmente** su tutti i sistemi e le applicazioni TIC a supporto di **funzioni essenziali o importanti** (par. 6)?

**Test di strumenti e sistemi (art. 25)**:
3.7 Il programma include, secondo le caratteristiche dell'entita': valutazione e scansione delle vulnerabilita'; analisi open source; valutazioni della sicurezza delle reti; analisi delle carenze; esami della sicurezza fisica; questionari e scansione del software; esame del codice sorgente (ove fattibile); test basati su scenari; test di compatibilita'; test di prestazione; test end-to-end; test di penetrazione (par. 1)?
3.8 Per depositari centrali di titoli e controparti centrali: valutazioni delle vulnerabilita' **prima di ciascun rilascio** di applicazioni e componenti infrastrutturali e servizi TIC a supporto delle funzioni essenziali o importanti (par. 2)?
3.9 Se microimpresa: i test sono eseguiti combinando approccio basato sul rischio e pianificazione strategica (par. 3)?

**TLPT - obblighi sostanziali (art. 26)**:
3.10 L'entita' e' stata identificata dall'autorita' competente come tenuta al TLPT (par. 8)? Se no, le voci TLPT vanno marcate NON APPLICABILE.
3.11 Se identificata: il TLPT e' effettuato con **cadenza almeno triennale** (par. 1)? L'autorita' competente puo' adattare la frequenza in base al profilo di rischio.
3.12 Il TLPT riguarda alcune o tutte le **funzioni essenziali o importanti**, su sistemi attivi di produzione, identificando sistemi/processi/tecnologie TIC anche presso fornitori terzi (par. 2)?
3.13 Se i fornitori terzi TIC rientrano nell'ambito del TLPT: l'entita' adotta le misure e salvaguardie necessarie ed e' sempre pienamente responsabile (par. 3)?
3.14 E' stata valutata la possibilita' di "pooled testing" qualora la partecipazione del fornitore terzo possa avere impatto avverso su clienti non DORA (par. 4)?
3.15 **Ogni 3 test** condotti con tester interni, l'entita' utilizza un soggetto esterno (par. 8)? Per **enti creditizi significativi**: ricorrono **esclusivamente** a tester esterni (par. 8)?

**TLPT - requisiti dei tester (art. 27)**:
3.16 I soggetti incaricati hanno massimo grado di idoneita' e reputazione (par. 1 lettera a)?
3.17 Hanno capacita' tecniche e organizzative ed esperienza dimostrata in analisi delle minacce, pentest, red team (par. 1 lettera b)?
3.18 Sono certificati da un ente di accreditamento in uno SM o aderiscono a codici/quadri etici formali (par. 1 lettera c)?
3.19 Esiste una garanzia indipendente o una relazione di audit sulla gestione dei rischi connessi all'esecuzione del TLPT (par. 1 lettera d)?
3.20 Sono debitamente coperti da assicurazioni di responsabilita' professionale, anche contro colpa e negligenza (par. 1 lettera e)?
3.21 Per i tester **interni**: l'autorita' competente ha approvato il ricorso (par. 2)? Sono dedicate risorse sufficienti? Sono prevenuti conflitti d'interesse? Il soggetto che fornisce **l'analisi delle minacce e' esterno** (par. 2)?
3.22 I contratti con tester esterni prevedono solida gestione dei risultati del TLPT e trattamento corretto dei dati (par. 3)?

## Output

Generare un report markdown con la seguente struttura:

```
# Gap Assessment DORA - Pillar 3 (Test di resilienza operativa digitale)

## Profilo dell'entita'
- Categoria (art. 2 par. 1): ...
- Microimpresa (art. 3 n. 60): si' / no
- Quadro semplificato (art. 16 par. 1): si' / no
- Identificata per TLPT (art. 26 par. 8): si' / no / non noto
- Ente creditizio significativo (art. 6 par. 4 reg. 1024/2013): si' / no
- Depositario centrale o CCP (per art. 25 par. 2): si' / no
- Data assessment: 2026-MM-DD
- Documenti analizzati: <elenco>

## Sintesi
| Stato | Numero voci |
| - | - |
| CONFORME | N |
| PARZIALE | N |
| NON CONFORME | N |
| NON APPLICABILE | N |
| Totale | 22 |

## Dettaglio per area

### Programma generale (art. 24)
### Test di strumenti e sistemi TIC (art. 25)
### TLPT - obblighi sostanziali (art. 26)
### TLPT - requisiti dei tester (art. 27)

## Punti che richiedono giudizio del professionista
[Elenco delle voci PARZIALI/NON APPLICABILI che richiedono validazione del professionista, con attenzione a: qualificazione di "funzione essenziale o importante" (art. 3 n. 22), valutazione del rischio per programmare i test, decisione sul ricorso a tester interni vs esterni, scelta di pooled testing.]

## Avvertenza
Il presente report e' uno strumento di supporto. Il giudizio finale sulla conformita' al programma di test e in particolare l'identificazione delle "funzioni essenziali o importanti" e' responsabilita' del professionista responsabile. Per il TLPT, le RTS adottate ex art. 26 par. 11 (in linea con TIBER-EU) contengono i requisiti operativi puntuali (scope, metodologia, fasi), fuori scope di questa skill. Le citazioni di articoli sono ricavate dalla trascrizione fedele del Regolamento (UE) 2022/2554 in `references/fonti/reg-ue-2022-2554-dora.md`.
```

## Limiti

- Il task **non** valuta le RTS adottate ex art. 26 par. 11 (in linea con TIBER-EU), che disciplinano in dettaglio scope, metodologia, fasi e requisiti operativi del TLPT.
- Il task **non** rilascia attestazioni: solo mappature.
- L'identificazione dell'entita' come tenuta al TLPT (art. 26 par. 8) spetta all'autorita' competente: se l'utente non ha ricevuto comunicazione formale, le voci TLPT vanno marcate "NON APPLICABILE - non identificata ai sensi dell'art. 26 par. 8" con nota di verifica.
- L'esecuzione concreta dei test e la valutazione dei loro risultati e' fuori scope: la skill verifica solo l'esistenza, struttura e periodicita' del programma.
