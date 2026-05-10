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
2. **Tipo di contratto**: lavori / servizi / forniture
3. **Criterio di aggiudicazione**: prezzo piu' basso (PPB) o OEPV
4. **Importo a base d'asta** (EUR, IVA esclusa)
5. **Soglia**: sopra o sotto soglia europea (dal 1/1/2026: lavori >= 5.404.000 EUR;
   servizi/forniture >= 140.000 EUR PA centrali / 216.000 EUR PA sub-centrali / 432.000 EUR settori speciali;
   le soglie sono aggiornate ogni 2 anni dalla Commissione UE: verificare i valori vigenti)
6. **Contesto PNRR** (si/no): se si', il disciplinare deve rispettare termini accelerati

## Fonti normative

Leggere prima di procedere:
- `references/estratti/dlgs-36-artt-clausole-disciplinare.md` (artt. 11, 74, 87, 90, 94-103, 117-120)
- `references/estratti/anac-bandi-tipo-struttura-2023.md` (struttura schemi ANAC, deroghe ammesse)

## Procedura

### Passo 1 - Identifica lo schema ANAC di riferimento

In base agli input dell'utente, determina quale schema ANAC applicare:

| Tipo contratto | Criterio | Schema da usare |
|---------------|----------|-----------------|
| Servizi / Forniture | PPB | Schema SF-PPB |
| Servizi / Forniture | OEPV | Schema SF-OEPV |
| Lavori | PPB | Schema Lavori-PPB |
| Lavori | OEPV | Schema Lavori-OEPV |

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
