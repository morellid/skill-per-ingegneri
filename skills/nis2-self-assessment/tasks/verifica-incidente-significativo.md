# Task: Verifica incidente significativo (art. 25 D.Lgs. 138/2024)

Determina se un evento di sicurezza informatica costituisce "incidente significativo" ai sensi dell'art. 25 co. 4 D.Lgs. 138/2024 e quali tempistiche di notifica al CSIRT Italia si applicano.

## Pre-requisito

Il soggetto deve essere in ambito NIS2 (essenziale o importante). Se non lo e', valutare se l'incidente comporta altri obblighi (GDPR, codice comunicazioni elettroniche, PSNC, DORA).

## Obiettivo

Produrre una valutazione strutturata che concluda con uno dei 4 esiti:

- **NOTIFICA OBBLIGATORIA - SCATTATA** - l'evento e' incidente significativo: avviare immediatamente la procedura di pre-notifica entro 24 ore.
- **NOTIFICA OBBLIGATORIA - DA AVVIARE** - in corso di acquisizione dei dati per confermare. Avviare procedura cautelativa.
- **NON SIGNIFICATIVO** - evento non raggiunge le soglie IS-1..4. Buona pratica: documentare la valutazione internamente per finalita' di accountability e revisione periodica delle soglie DE.CM-01. Non e' previsto un "registro incidenti interno" come obbligo nominativo nel D.Lgs. 138/2024 ne' nella Det. 379907/2025; la documentazione interna deriva dai requisiti di gestione incidenti (RS.MA-01) e di miglioramento continuo (ID.IM-01, ID.IM-04).
- **NOTIFICA VOLONTARIA RACCOMANDATA** - quasi-incidente o minaccia significativa che il soggetto puo' notificare ex art. 26.

## Input richiesti

- **Descrizione tecnica dell'evento**: cosa e' successo, quando, da chi rilevato, vettore di attacco/causa.
- **Tempistica**: data/ora di rilevamento (= "conoscenza" dell'incidente, da cui decorre il termine 24h/72h).
- **Servizio/i impattato/i**: quali asset/servizi sono coinvolti, criticita' per il business e per i destinatari.
- **Stato attuale**: incidente in corso, contenuto, risolto?
- **Impatti rilevati o stimati**:
  - Indisponibilita' del servizio (durata, percentuale di utenti coinvolti)
  - Compromissione di dati (categorie, volume, sensibilita')
  - Compromissione di account/identita' (numero, livello privilegio)
  - Perdita finanziaria (diretta e stimata)
  - Impatto su terzi (clienti, cittadini, pazienti, operatori dipendenti)
  - Impatto transfrontaliero (servizi forniti in altri Stati membri UE)
- **Atti illegittimi/malevoli**: ci sono indicatori che suggeriscono attacco doloso? (rilevante per pre-notifica art. 25 co. 5 lett. a + comunicazione Autorita' di contrasto art. 25 co. 8)
- **Sovrapposizione GDPR**: l'incidente coinvolge dati personali? (notifica parallela al Garante ex art. 33 GDPR)

## Fonti

Leggere prima:
- `references/estratti/dlgs-138-2024-incident-art25.md` - art. 25 co. 4-12
- `references/estratti/acn-incidenti-significativi.md` - soglie ACN

## Procedura

### Passo 1 - Determinare il tempo zero

"Conoscenza dell'incidente" (T0) = momento in cui il soggetto **viene a conoscenza** dell'incidente significativo. Questo decorre da quando il responsabile della sicurezza, l'IT o un canale ufficiale viene avvertito da fonte interna o esterna.

NON da quando l'incidente si e' verificato tecnicamente. Esempio: ransomware attivato a T-72h ma rilevato a T0; il termine di 24h/72h decorre da T0.

Da T0:
- **24 ore**: pre-notifica al CSIRT Italia
- **72 ore**: notifica con valutazione iniziale
- **1 mese dalla notifica**: relazione finale

### Passo 2 - Verifica criteri di significativita' (art. 25 co. 4)

Almeno UNO dei due deve essere soddisfatto perche' l'incidente sia significativo:

**Lett. a)** - Impatto sul soggetto:
- Grave perturbazione operativa dei servizi forniti?
- Perdite finanziarie per il soggetto interessato?

**Lett. b)** - Impatto sui terzi:
- Ripercussioni o idoneita' a provocare ripercussioni su altre persone fisiche o giuridiche?
- Perdite materiali o immateriali considerevoli su terzi?

| Criterio | Soddisfatto? | Motivazione |
|----------|---------------|-------------|
| 25.4.a) Grave perturbazione operativa | [SI/NO/POTENZIALE] | |
| 25.4.a) Perdite finanziarie per il soggetto | [SI/NO/POTENZIALE] | |
| 25.4.b) Ripercussioni su altre persone fisiche/giuridiche | [SI/NO/POTENZIALE] | |
| 25.4.b) Perdite materiali/immateriali considerevoli per terzi | [SI/NO/POTENZIALE] | |

Anche un solo SI o POTENZIALE -> incidente significativo.

### Passo 3 - Verifica codici incidente significativo di base (Allegati 3-4 Det. ACN 379907/2025)

Applicare i codici **verbatim** della Determinazione (vedi `references/estratti/acn-incidenti-significativi.md` per il testo completo).

**Per soggetti importanti (Allegato 3) - 3 codici**:

| Codice | Descrizione (riassunta) | Soddisfatto? |
|--------|--------------------------|---------------|
| **IS-1** | Evidenza di perdita di riservatezza, verso l'esterno, di dati digitali del soggetto NIS | [SI/NO] |
| **IS-2** | Evidenza di perdita di integrita', con impatto verso l'esterno, di dati digitali del soggetto NIS | [SI/NO] |
| **IS-3** | Violazione dei livelli di servizio (SL) stabiliti ai sensi della misura DE.CM-01 | [SI/NO] |

**Per soggetti essenziali (Allegato 4) - 4 codici** (tutti i precedenti + IS-4):

| Codice | Descrizione (riassunta) | Soddisfatto? |
|--------|--------------------------|---------------|
| **IS-1** | Evidenza di perdita di riservatezza esterna | [SI/NO] |
| **IS-2** | Evidenza di perdita di integrita' con impatto esterno | [SI/NO] |
| **IS-3** | Violazione SL definiti ai sensi DE.CM-01 | [SI/NO] |
| **IS-4** | Evidenza, anche sulla base dei parametri quali-quantitativi DE.CM-01, di accesso non autorizzato o abuso di privilegi a dati digitali del soggetto NIS | [SI/NO] |

**Note operative**:
- Le **soglie quale-quantitative** per IS-3 e IS-4 sono definite **dal soggetto stesso** ai sensi della misura DE.CM-01 dell'Allegato 1/2. La determinazione NON impone valori numerici generali (es. ore di indisponibilita', percentuali utenti, soglie EUR).
- IS-1 e IS-2 sono qualitativi: la soglia e' "evidenza di perdita verso l'esterno", senza requisito di volume.
- Per gli **operatori telco** (definiti dall'art. 1 lett. s della Det. 379907/2025: >= 1% utenti nazionali OR >= 1.000.000 utenti), si applicano in **aggiunta** le soglie quantitative dell'art. 6 co. 2:

| Caso telco | Durata | % utenti nazionali colpiti |
|-------------|--------|------------------------------|
| a) | > 1 ora | > 15% |
| b) | > 2 ore | > 10% |
| c) | > 4 ore | > 5% |
| d) | > 6 ore | > 2% |
| e) | > 8 ore | > 1% |

Per tutti gli altri soggetti, **non esistono soglie nazionali quantitative**: la soglia e' definita internamente al soggetto.

### Passo 4 - Verifica casi speciali

| Caso | Implicazione |
|------|---------------|
| Prestatore di servizi fiduciari | Notifica entro **24h** anche per la notifica art. 25 co. 5 lett. b (non 72h) - art. 25 co. 6 |
| Soggetto PSNC (DL 105/2019) | La notifica PSNC effettuata assolve all'obbligo NIS2 - art. 1 co. 8 DL 105/2019 |
| Soggetto DORA-eligible (settori 3-4 Allegato I) | Notifica DORA prevale (Reg. UE 2022/2554) - art. 3 co. 14 D.Lgs. 138/2024 |
| Incidente con dati personali | Notifica parallela al Garante Privacy (72h da art. 33 GDPR) |
| Incidente con caratteristiche criminali sospette | Su richiesta CSIRT, segnalazione anche all'Autorita' di contrasto (art. 25 co. 8) |
| Fornitore reti/servizi comunicazione elettronica | Verificare obblighi paralleli ex codice comunicazioni elettroniche (D.Lgs. 259/2003 art. 40) |

### Passo 5 - Avvio procedura di pre-notifica (entro 24h)

Se incidente significativo confermato o probabile:

**Pre-notifica art. 25 co. 5 lett. a)** - contenuto minimo:
- Identificazione del soggetto e del punto di contatto NIS
- Descrizione sintetica dell'evento e del momento di rilevamento (T0)
- Servizi/asset coinvolti
- Indicazione preliminare:
  - L'incidente puo' ritenersi risultato di **atti illegittimi o malevoli**? [SI / NO / NON DETERMINABILE]
  - L'incidente puo' avere **impatto transfrontaliero**? [SI / NO / NON DETERMINABILE]

Canale: piattaforma digitale ACN. Punto di contatto NIS abilitato (art. 7).

### Passo 6 - Notifica entro 72h (art. 25 co. 5 lett. b)

Aggiornamento e contenuto minimo:
- Aggiornamento delle informazioni della pre-notifica
- **Valutazione iniziale**:
  - Gravita' dell'incidente
  - Impatto stimato (su servizi, terzi, transfrontaliero)
- **Indicatori di compromissione (IoC)** ove disponibili: hash file malevoli, IP/domini C2, TTP osservate (MITRE ATT&CK), CVE sfruttate, ecc.

Per prestatori servizi fiduciari: notifica anche entro 24h (deroga art. 25 co. 6).

### Passo 7 - Relazione finale entro 1 mese (art. 25 co. 5 lett. d)

Contenuto:
1. Descrizione dettagliata dell'incidente, gravita', impatto
2. Tipo di minaccia o **root cause**
3. Misure di attenuazione adottate e in corso
4. Impatto transfrontaliero (ove noto)

Se l'incidente e' ancora in corso al momento del report finale:
- Relazione **mensile** sui progressi
- Relazione finale entro 1 mese dalla **conclusione** della gestione (art. 25 co. 5 lett. e)

### Passo 8 - Comunicazione ai destinatari del servizio (art. 25 co. 9-10)

Sentito il CSIRT Italia, valutare:
- **Comunicazione ai destinatari** se l'incidente puo' ripercuotersi sui servizi forniti (art. 25 co. 9)
- **Comunicazione di misure correttive** ai destinatari potenzialmente interessati da una minaccia significativa (art. 25 co. 10)

Tale comunicazione e' senza ingiustificato ritardo, contestualizzata.

### Passo 9 - Sintesi e output

```markdown
# Valutazione di incidente significativo NIS2 - [organizzazione]

**Data valutazione**: [data ora]
**Soggetto**: [classificazione: essenziale/importante]
**T0 (conoscenza)**: [data ora]
**Termini**:
- Pre-notifica entro: [T0 + 24h]
- Notifica entro: [T0 + 72h]
- Relazione finale entro: [T0 + 72h + 1 mese]

## Esito orientativo

**[NOTIFICA OBBLIGATORIA - SCATTATA | NOTIFICA OBBLIGATORIA - DA AVVIARE | NON SIGNIFICATIVO | NOTIFICA VOLONTARIA RACCOMANDATA]**

## Motivazione

### Criteri art. 25 co. 4
[Quale lettera (a/b) e' soddisfatta. Motivazione.]

### Soglie ACN applicabili
[Categoria/soglia che fa scattare l'obbligo.]

### Casi speciali
[Prestatore servizi fiduciari? PSNC? DORA? GDPR? Comunicazione elettronica?]

## Pre-notifica suggerita (entro 24h)

```
A: CSIRT Italia (piattaforma ACN)
Da: [punto di contatto NIS]
Soggetto: Pre-notifica art. 25 co. 5 lett. a) - [identificativo soggetto]

Soggetto: [ragione sociale, classificazione NIS2]
Punto di contatto: [nome / ruolo / contatti]
T0 (conoscenza): [data ora]

Descrizione sintetica:
[2-3 righe]

Servizi/asset coinvolti:
[elenco]

Indicazioni preliminari:
- Atti illegittimi/malevoli: [SI / NO / NON DETERMINABILE]
- Impatto transfrontaliero: [SI / NO / NON DETERMINABILE]

Stato: [in corso / contenuto / risolto]
```

## Notifica suggerita (entro 72h)

[Skeleton di notifica dettagliata con valutazione iniziale, IoC, gravita'.]

## Relazione finale (entro 1 mese)

[Skeleton con descrizione, root cause, mitigazione, impatto transfrontaliero.]

## Notifiche parallele

- GDPR (se dati personali coinvolti): notifica al Garante entro 72h da T0
- PSNC: se applicabile, una notifica unificata
- DORA: se ente finanziario DORA-eligible, prevale
- Codice comunicazioni elettroniche: per fornitori reti/servizi

## Limiti di questa valutazione

- Si basa sulle informazioni fornite al momento. L'evolversi dell'incidente puo' modificarne la classificazione.
- Le soglie quantitative ACN sono indicative; verificare il testo della Det. 379907/2025 Allegato 3/4.
- La decisione finale di notifica spetta al soggetto sotto la propria responsabilita' (art. 25 co. 1, art. 7 punto di contatto).
- L'art. 25 co. 3 stabilisce che la notifica non espone a responsabilita' aggiuntiva: in caso di dubbio, prevale la notifica.

## Rinvio al CISO / DPO / consulente cyber / legale

La presente valutazione e' di supporto. La decisione di notifica rimane in capo al soggetto e al suo punto di contatto NIS, in coordinamento con CISO, DPO (se dati personali), consulente cyber e legale. **Mancata notifica e' violazione art. 25 sanzionata ex art. 38 co. 8 lett. a)**: fino a 10M EUR / 2% fatturato (essenziali).
```

## Casi tipici (esempi orientativi)

Esempi non esaustivi: l'esito dipende dai parametri DE.CM-01 specifici del soggetto e dalle definizioni di "perdita di riservatezza/integrita' verso l'esterno" del soggetto stesso.

| Caso | Soggetto | Codice possibile | Esito orientativo |
|------|----------|-------------------|-------------------|
| Ransomware su server di produzione: indisponibilita' supera SL definito ex DE.CM-01 | Importante | IS-3 | Significativo - notifica obbligatoria |
| Phishing campaign rilevata, 2 account utente compromessi, no movimento laterale | Importante | (nessun codice IS soddisfatto) | Non significativo - documentazione interna |
| Esfiltrazione DB clienti contenente dati personali con evidenza di trasferimento esterno | Essenziale | IS-1 (perdita riservatezza esterna) + IS-4 (accesso non autorizzato) | Significativo + notifica GDPR parallela (Garante 72h art. 33 GDPR) |
| ICS compromesso in centrale elettrica, evitato blackout grazie a reroute manuale | Essenziale (energia) | IS-2 (potenziale modifica integrita' con impatto esterno) e/o IS-4 | Da valutare in relazione ai parametri DE.CM-01 e alla soglia interna; in dubbio, notifica per art. 25 co. 3 (la notifica non aggrava la responsabilita') |
| Compromissione domain controller (AD admin) contenuta in 2 ore, no movimento ulteriore | Essenziale | IS-4 (abuso privilegi su asset rilevante con dati digitali) | Significativo - notifica obbligatoria |
| Ransomware su server di test isolato, no impatto produzione, no esfiltrazione | Importante | (nessun codice IS soddisfatto) | Non significativo - registrazione nei log interni; valutare come quasi-incidente per notifica volontaria art. 26 |
| Operatore telco, 1.5h indisponibilita' nazionale rete mobile, 18% utenti colpiti | Importante (telco) | Soglia art. 6 co. 2 lett. a Det. 379907/2025 (>1h e >15%) -> IS-3 | Significativo - notifica obbligatoria |

## Limiti di questo task

- Non sostituisce la valutazione del CSIRT/SOC interno o del consulente cyber.
- Non integra automaticamente con piattaforme di IR/SOAR.
- Non produce la notifica formale: il punto di contatto NIS (art. 7) trasmette tramite la piattaforma ACN.
- Le soglie quale-quantitative DE.CM-01 sono **definite dal soggetto stesso**: la valutazione finale dipende dai parametri puntuali interni, non da tabelle generiche.
- Per gli operatori telco, le soglie nazionali dell'art. 6 co. 2 sono cumulative con i codici IS-1..3.

## Esempi

Vedi `examples/`. (In v0.1.0-alpha gli esempi disponibili coprono solo i casi di perimetro: utility energetica essenziale e PMI manifattura importante. Esempi dedicati di valutazione incidente da aggiungere in iterazioni successive.)
