# Task: Verifica conformita' disciplinare di gara agli schemi ANAC

Verifica che un disciplinare di gara sia conforme allo schema ANAC applicabile,
segnalando le sezioni mancanti, le clausole non allineate e le deroghe non giustificate
che espongono la procedura a rischio TAR.

## Obiettivo

Produrre un report strutturato che indichi, per ciascuna sezione del disciplinare:
- **Esito**: conforme / non conforme / deroga motivata / da verificare
- **Riferimento normativo** preciso (art. e comma D.Lgs. 36/2023)
- **Problema rilevato** e motivazione
- **Raccomandazione** per correggere o allineare allo schema ANAC

## Input richiesti

1. **Testo del disciplinare di gara** (o le sezioni rilevanti da verificare)
2. **Tipo di contratto**: lavori / servizi / forniture / **servizi di ingegneria e architettura (SIA)**
3. **Criterio di aggiudicazione**: prezzo piu' basso (PPB) o OEPV
4. **Importo a base d'asta** (EUR, IVA esclusa)
5. **Soglia**: sopra o sotto soglia europea (dal 1/1/2026: lavori >= 5.404.000 EUR;
   servizi/forniture >= 140.000 EUR PA centrali / 216.000 EUR PA sub-centrali / 432.000 EUR settori speciali;
   le soglie sono aggiornate ogni 2 anni dalla Commissione UE: verificare i valori vigenti)
6. **Contesto PNRR** (si/no): se si', il disciplinare deve rispettare termini accelerati
7. **Data di indizione**: per stabilire se applicare la versione pre o post 30 maggio 2026 degli schemi ANAC (Delibere 148/2026 e 153/2026)
8. **Se SIA: BIM richiesto/obbligatorio**: presenza nel disciplinare della clausola BIM; obbligatorio per lavori >2M euro

## Fonti normative

Leggere prima di procedere:
- `references/estratti/dlgs-36-artt-clausole-disciplinare.md` (artt. 11, 74, 87, 90, 94-103, 117-120)
- `references/estratti/anac-bandi-tipo-struttura-2023.md` (struttura schemi ANAC, deroghe ammesse)
- `references/estratti/anac-bandi-tipo-clausole-ai-l132-2025.md` (clausole AI obbligatorie da Delibera 148/2026, in vigore dal 30 maggio 2026)
- `references/fonti/anac-bando-tipo-n1-2023-agg-del-148-2026.md` (paragrafo 28 accesso agli atti: clausola alternativa per inversione procedimentale, Parere CdS n. 61/2026)
- Se SIA: `references/estratti/anac-bando-tipo-2-2026-sia-requisiti-bim.md` (importo 65/35, BIM, figure professionali UNI 11337-7)

## Procedura

### Passo 1 - Identifica lo schema ANAC di riferimento

In base agli input dell'utente, determina quale schema ANAC applicare:

| Tipo contratto | Criterio | Schema da usare |
|---------------|----------|-----------------|
| Servizi / Forniture (generici) | PPB | Schema SF-PPB |
| Servizi / Forniture (generici) | OEPV | **Bando tipo n. 1/2023** (Delibera 148/2026 dal 30/5/2026) |
| **SIA** (ingegneria/architettura) | OEPV | **Bando tipo n. 2/2026** (Delibera 153/2026 dal 30/5/2026) |
| Lavori | PPB | Schema Lavori-PPB |
| Lavori | OEPV | Schema Lavori-OEPV |

**Discriminante SIA vs servizi generici**: se l'oggetto comprende progettazione (fattibilita', esecutiva), direzione lavori, coordinamento sicurezza, verifica progetto, supporto al RUP per attivita' tecniche -> usare Bando 2/2026 (SIA). Servizi generici di consulenza, IT, manutenzione, ecc. -> Bando 1/2023.

Se la procedura e' indetta **prima del 30 maggio 2026**: applicare la versione pre-Delibera 148/2026 (Delibera 365/2025) per il Bando 1; per i SIA pre-30/5/2026 non esiste schema-tipo ANAC specifico, applicare il Bando 1 con adattamenti.

Se il disciplinare e' sotto soglia europea: applicare lo schema sopra soglia corrispondente
come riferimento, segnalando che alcune disposizioni possono essere semplificate.

Se l'utente non ha fornito il tipo di contratto o il criterio: chiedere prima di procedere.

### Passo 2 - Verifica struttura (sezioni obbligatorie presenti)

Controllare che il disciplinare contenga tutte le sezioni elencate in
`references/estratti/anac-bandi-tipo-struttura-2023.md`. Per ogni sezione:

| Sezione | Presente (si/no/parziale) | Note |
|---------|--------------------------|------|
| 1. Stazione appaltante e oggetto | | CIG, CPV, importo, durata, piattaforma |
| 2. Procedura e criterio aggiudicazione | | Tipo procedura, criterio |
| 3. Documentazione di gara | | Accesso documenti, termine chiarimenti |
| 4. Soggetti ammessi | | Impresa singola, RTI, consorzi |
| 5. Motivi di esclusione | | Artt. 94, 95, 96 D.Lgs. 36/2023 |
| 6. Requisiti di partecipazione | | Art. 100, DGUE (art. 91), FVOE (art. 99) |
| 7. Avvalimento | | Artt. 104, 105 |
| 8. Subappalto | | Art. 119, no limite % generale |
| 9. Clausola sociale | | CCNL specifico (art. 11) |
| 10. Modalita' presentazione offerte | | Termini, firma digitale |
| 11. Garanzia provvisoria | | 2%, riduzioni qualita' (art. 106) |
| 12. Soccorso istruttorio | | Art. 101, termine 5-10 gg |
| 13. Criteri aggiudicazione | | PPB: offerta anomala; OEPV: matrice |
| 14. Verifica requisiti / aggiudicazione | | FVOE (art. 99), antimafia, termini |
| 15. Garanzia definitiva | | 10% importo contrattuale (art. 117) |
| 16. Comunicazioni | | Piattaforma certificata (art. 90) |
| 17. Trattamento dati personali | | GDPR |

Ogni sezione mancante va segnalata come **Critico** se richiesta dalla legge,
come **Sostanziale** se richiesta dallo schema ANAC ma non dalla legge.

### Passo 3 - Verifica aggiornamento normativo (vecchio vs nuovo codice)

Cercare nel disciplinare i seguenti indicatori di mancato aggiornamento:

| Indicatore da cercare | Impatto | Correzione richiesta |
|-----------------------|---------|----------------------|
| "art. 80 D.Lgs. 50/2016" (esclusioni) | Critico | Sostituire con artt. 94, 95, 96 D.Lgs. 36/2023 |
| "art. 83 D.Lgs. 50/2016" (requisiti) | Critico | Sostituire con art. 100 D.Lgs. 36/2023 |
| "art. 85 D.Lgs. 50/2016" (DGUE) | Critico | Sostituire con art. 91 D.Lgs. 36/2023 |
| "art. 89 D.Lgs. 50/2016" (avvalimento) | Critico | Sostituire con artt. 104, 105 D.Lgs. 36/2023 |
| "art. 105 D.Lgs. 50/2016" (subappalto) | Critico | Sostituire con art. 119 D.Lgs. 36/2023 |
| "art. 93 D.Lgs. 50/2016" (garanzie) | Critico | Provvisoria: art. 106; definitiva: art. 117 D.Lgs. 36/2023 |
| "art. 95 o 97 D.Lgs. 50/2016" (criteri) | Critico | Sostituire con artt. 107-108 D.Lgs. 36/2023 |
| "D.Lgs. 50/2016" senza specifica | Sostanziale | Verificare ogni riferimento e aggiornare |
| Limite subappalto "max 30%" o "40%" | Critico | Rimuovere: art. 119 D.Lgs. 36/2023 non ha limite % generale |
| "art. 87 D.Lgs. 36/2023" per il DGUE | Sostanziale | Sostituire con art. 91 D.Lgs. 36/2023 (art. 87 = disciplinare) |
| Garanzia definitiva "5-10%" | Sostanziale | Sostituire con "10% importo contrattuale" (art. 117 D.Lgs. 36/2023) |

### Passo 4 - Verifica clausole chiave

Verificare il contenuto delle clausole principali contro i requisiti di legge:

**4a. Clausola sociale (art. 11 D.Lgs. 36/2023)**
- [ ] CCNL specificato con nome completo (non solo "CCNL di settore")
- [ ] Obbligo esteso ai subappaltatori
- [ ] Conseguenza del mancato rispetto: esclusione o risoluzione

**4b. Esclusioni (artt. 94, 95, 96 D.Lgs. 36/2023)**
- [ ] Cause di esclusione automatica (art. 94) elencate o rinvio esplicito all'articolo con DGUE
- [ ] Cause non automatiche (art. 95): contraddittorio previsto
- [ ] Self-cleaning previsto (art. 96 co. 6 D.Lgs. 36/2023)
- [ ] Nessun riferimento a vecchio art. 80 D.Lgs. 50/2016

**4c. Requisiti di partecipazione (art. 100 D.Lgs. 36/2023)**
- [ ] Iscrizione CCIAA o albo professionale (art. 100 co. 3)
- [ ] Fatturato, se richiesto, non superiore al doppio del valore stimato (art. 100 co. 11)
- [ ] DGUE richiesto compilato sulla PAD (art. 91 D.Lgs. 36/2023)
- [ ] FVOE menzionato per la fase di verifica dei requisiti (art. 99 D.Lgs. 36/2023)
- [ ] Nessun riferimento a vecchio art. 83 D.Lgs. 50/2016

**4d. Subappalto (art. 119 D.Lgs. 36/2023)**
- [ ] Nessun limite percentuale generale non motivato
- [ ] Indicazione delle prestazioni da subappaltare nell'offerta (condizione ammissibilita')
- [ ] Impegno PMI: almeno 20% della quota subappaltata (salvo motivazione)
- [ ] Modalita' pagamento diretto al subappaltatore (microimprese/PMI e inadempimento)

**4e. Garanzia provvisoria (art. 106 D.Lgs. 36/2023)**
- [ ] Importo base = 2% del valore stimato (modificabile motivatamente tra 1% e 4%)
- [ ] Tabella riduzioni per certificazioni (ISO 9001 -30%, PMI -50%, DLT -10%, Allegato II.13 fino a -20%)
- [ ] Schema fidejussione conforme al decreto ministeriale di cui all'art. 117 co. 12

**4f. Soccorso istruttorio (art. 101 D.Lgs. 36/2023)**
- [ ] Differenziato tra documenti ammissibili e non ammissibili
- [ ] Non esteso all'offerta tecnica o economica
- [ ] (Per gare dopo 30/5/2026) Elenco casi sanabili integrato Delibera 148/2026: mancata produzione contratto avvalimento; intestazione garanzia provvisoria non a tutti i componenti del costituendo RTI; erronea indicazione beneficiario garanzia provvisoria.

**4g. Clausole AI obbligatorie (Delibera 148/2026 - in vigore dal 30 maggio 2026)**

Vedi `references/estratti/anac-bandi-tipo-clausole-ai-l132-2025.md`.
- [ ] Paragrafo 15.1 / Domanda di partecipazione contiene dichiarazione AI per fase offerta tecnica.
- [ ] Stesso paragrafo contiene dichiarazione AI per fase esecuzione (impegno se aggiudicato).
- [ ] Riferimenti normativi citati: Reg. UE 2024/1689 + L. 132/2025 + Reg. UE 2016/679 + D.Lgs. 196/2003.
- [ ] **Se servizi intellettuali / SIA**: clausola in versione art. 13 L. 132/2025 (specifica tipologia AI, prevalenza lavoro intellettuale, controllo, verifica risultati).
- [ ] Per disciplinari indetti prima del 30 maggio 2026: clausola AI **non** ancora obbligatoria.

**4h. Solo SIA - Verifiche specifiche Bando 2/2026**

Vedi `references/estratti/anac-bando-tipo-2-2026-sia-requisiti-bim.md`.

**Importo base** (paragrafo 3):
- [ ] Calcolato ai sensi Allegato I.13 (DM 17.06.2016) con schema corrispettivi allegato.
- [ ] Esplicitato: 65% prezzo fisso non ribassabile + 35% ribassabile (art. 41 c. 15-bis Codice).
- [ ] Se progettazione >2M euro con BIM: maggiorazione 10% su onorari (Allegato I.13 art. 2 c. 5).
- [ ] DUVRI assente per servizi puramente intellettuali (costi sicurezza interferenze = 0 euro).
- [ ] Equo compenso: nessuna richiesta di prestazioni gratuite o ulteriori rispetto all'importo base.

**Aggiudicazione** (paragrafi 17-18):
- [ ] Tetto **30 punti** per offerta economica (art. 41 c. 15-bis lett. b).
- [ ] Formula non lineare con alpha tra 0,1 e 0,3; PEi = 1 per ribassi sopra media.

**BIM (se previsto nel disciplinare)**:
- [ ] Clausola BIM in Premesse, riferimento ad art. 43 Codice + Allegato I.9.
- [ ] Per progettazione lavori >2M euro: BIM obbligatorio, non facoltativo.
- [ ] Capitolato informativo allegato al disciplinare (art. 1 c. 8 Allegato I.9).
- [ ] Paragrafo 6.1 lettere h)-k): figure professionali BIM UNI 11337-7 richieste (BIM Manager, BIM Coordinator, BIM Specialist, CDE Manager) con esperienza pregressa documentabile.
- [ ] Paragrafo 16: offerta tecnica include documento autonomo "offerta di gestione informativa digitale".
- [ ] Certificazione UNI 11337-7:2018 richiesta come premio, NON come requisito.

**Offerta tecnica AI (paragrafo 16)**:
- [ ] Obbligo di indicare le attivita' strumentali svolte con sistemi AI (specifico SIA).

**Requisiti speciali (paragrafo 6.3)**:
- [ ] Requisiti economico-finanziari alternativi (art. 40 c. 1-bis Allegato II.12): copertura assicurativa 10% importo opere OPPURE fatturato globale 3 dei 5 anni non superiore a valore stimato.
- [ ] Elenco servizi con importo 1-2 volte importo lavori per categoria/ID (ultimi 10 anni).
- [ ] Eventuali servizi di punta: 2 servizi per categoria/ID 0,40-0,80 volte importo (oppure 1 servizio unico pari al minimo).

**4i. Accesso agli atti e inversione procedimentale (paragrafo 28, Delibera 148/2026 - gare indette dal 30 maggio 2026)**

Vedi `references/fonti/anac-bando-tipo-n1-2023-agg-del-148-2026.md` (sezione "Paragrafo 28").
- [ ] Il paragrafo Accesso agli atti e' allineato al testo aggiornato dalla Delibera 148/2026 (che recepisce il Parere del Consiglio di Stato n. 61 del 13/01/2026).
- [ ] **Se la SA si avvale dell'inversione procedimentale**: presente la clausola alternativa del paragrafo 28: ai partecipanti collocatisi nei primi cinque posti della graduatoria sono rese reciprocamente disponibili le offerte presentate, **ad eccezione della documentazione amministrativa degli offerenti dal secondo al quinto posto che non sia stata verificata dalla stazione appaltante**.
- [ ] Indicata la modalita' con cui la SA garantisce la disponibilita' dei documenti.
- [ ] Per i partecipanti collocatisi oltre il quinto posto: prevista la stessa modalita' di accesso ai sensi degli artt. 3-bis e 22 della L. 241/1990.
- [ ] Per gare indette prima del 30/05/2026: si applica la versione precedente dello schema (Delibera 365/2025), che conteneva il box N.B. in attesa del parere CdS: la clausola alternativa **non** e' esigibile.

### Passo 5 - Output

```markdown
# Verifica conformita' disciplinare di gara - Schema ANAC
**Gara**: [oggetto]
**Tipo contratto**: [lavori/servizi/forniture]
**Criterio aggiudicazione**: [PPB/OEPV]
**Importo a base d'asta**: EUR [importo]
**Schema ANAC di riferimento**: [SF-PPB / SF-OEPV / Lavori-PPB / Lavori-OEPV]
**Data verifica**: [data]

---

## Esito complessivo: [CONFORME / CONFORME CON RISERVA / NON CONFORME]

[Sintesi: numero di problemi critici, sostanziali, formali; indicazione se il
disciplinare appare aggiornato al D.Lgs. 36/2023 o se usa ancora il vecchio codice]

---

## Struttura: sezioni presenti

| Sezione | Esito | Note |
|---------|-------|------|
| 1. SA e oggetto | CONFORME | ... |
| ... | ... | ... |

---

## Aggiornamento normativo

| Riferimento trovato | Esito | Correzione |
|--------------------|-------|-----------|
| ... | CRITICO/OK | ... |

---

## Clausole chiave

### Clausola sociale (art. 11)
**Esito**: [conforme/non conforme]
**CCNL indicato**: [nome CCNL o "non specificato"]
**Problemi**: [descrizione o "nessuno"]

### Esclusioni (artt. 94-98)
...

### Requisiti di partecipazione
**Fatturato richiesto**: EUR [X] - [proporzionato/sproporzionato rispetto a EUR [valore stimato x2]]
...

### Subappalto (artt. 119-120)
...

### Garanzia provvisoria (art. 106)
...

### Garanzia definitiva (art. 117)
...

### Soccorso istruttorio (art. 101)
...

---

## Anomalie prioritizzate

### Priorita' CRITICA (violazioni di legge o clausole obbligatorie mancanti)

**1. [problema]**
- Riferimento: [art. X D.Lgs. 36/2023]
- Trovato: [testo del disciplinare]
- Richiesto: [testo corretto]
- Azione: [cosa fare]

### Priorita' SOSTANZIALE (deroghe allo schema ANAC non motivate)

**2. [problema]**
...

### Priorita' FORMALE (imprecisioni redazionali)

**3. [problema]**
...

---

## Avvertenze

- Questa verifica si basa sul testo fornito del disciplinare; non sostituisce la
  revisione legale dell'intero documento di gara
- Gli schemi ANAC sono aggiornati periodicamente: verificare sul portale ANAC
  la versione corrente prima della pubblicazione
- In caso di gare di importo rilevante o procedure innovative, si raccomanda
  parere legale preventivo
- Le soglie europee sono aggiornate ogni due anni dalla Commissione UE: verificare
  i valori aggiornati
```

## Limiti di questo task

- Il confronto con il testo verbatim degli schemi ANAC richiede avere il documento
  ANAC aggiornato: la skill verifica la struttura e i requisiti normativi, non ogni singola parola
- Non analizza la coerenza del disciplinare con il capitolato tecnico o con il progetto
- Non valuta la legittimita' della scelta della procedura (aperta, ristretta, negoziata)
- Non verifica la congruita' delle soglie di qualificazione con il mercato specifico

## Esempi

Vedi `examples/`:
- `conforme-servizi-ppb/` - disciplinare servizi informatici conforme allo schema SF-PPB
- `non-conforme-lavori-anomalie/` - disciplinare lavori con multipli problemi (vecchio codice, subappalto limitato)
