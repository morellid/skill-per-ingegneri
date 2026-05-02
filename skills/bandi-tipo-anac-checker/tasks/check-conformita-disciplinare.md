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
5. **Soglia**: sopra o sotto soglia europea (al 2025: lavori >= 5.538.000 EUR,
   servizi/forniture >= 221.000 EUR per PA centrali / 221.000 EUR PA locali / 443.000 EUR enti di settore speciale)
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
| 5. Motivi di esclusione | | Artt. 94-98 D.Lgs. 36/2023 |
| 6. Requisiti di partecipazione | | Artt. 100-103, DGUE, PassOE, FVOE |
| 7. Avvalimento | | Artt. 104-106 |
| 8. Subappalto | | Artt. 119-120, no limite % generale |
| 9. Clausola sociale | | CCNL specifico (art. 11) |
| 10. Modalita' presentazione offerte | | Termini, firma digitale |
| 11. Garanzia provvisoria | | 2%, riduzioni qualita' (art. 117) |
| 12. Soccorso istruttorio | | Art. 101 |
| 13. Criteri aggiudicazione | | PPB: offerta anomala; OEPV: matrice |
| 14. Verifica requisiti / aggiudicazione | | FVOE, antimafia, termini |
| 15. Garanzia definitiva | | 5-10% (art. 118) |
| 16. Comunicazioni | | Piattaforma certificata (art. 90) |
| 17. Trattamento dati personali | | GDPR |

Ogni sezione mancante va segnalata come **Critico** se richiesta dalla legge,
come **Sostanziale** se richiesta dallo schema ANAC ma non dalla legge.

### Passo 3 - Verifica aggiornamento normativo (vecchio vs nuovo codice)

Cercare nel disciplinare i seguenti indicatori di mancato aggiornamento:

| Indicatore da cercare | Impatto | Correzione richiesta |
|-----------------------|---------|----------------------|
| "art. 80 D.Lgs. 50/2016" | Critico | Sostituire con artt. 94-98 D.Lgs. 36/2023 |
| "art. 83 D.Lgs. 50/2016" | Critico | Sostituire con artt. 100-103 D.Lgs. 36/2023 |
| "art. 89 D.Lgs. 50/2016" | Critico | Sostituire con artt. 104-106 D.Lgs. 36/2023 |
| "art. 105 D.Lgs. 50/2016" | Critico | Sostituire con artt. 119-120 D.Lgs. 36/2023 |
| "art. 93 D.Lgs. 50/2016" | Critico | Sostituire con artt. 117-118 D.Lgs. 36/2023 |
| "art. 95/97 D.Lgs. 50/2016" | Critico | Sostituire con artt. 107-108 D.Lgs. 36/2023 |
| "D.Lgs. 50/2016" senza specifica | Sostanziale | Verificare ogni riferimento e aggiornare |
| Limite subappalto "max 30%" o "40%" | Critico | Rimuovere: illegittimo sotto art. 119 D.Lgs. 36/2023 |

### Passo 4 - Verifica clausole chiave

Verificare il contenuto delle clausole principali contro i requisiti di legge:

**4a. Clausola sociale (art. 11 D.Lgs. 36/2023)**
- [ ] CCNL specificato con nome completo (non solo "CCNL di settore")
- [ ] Obbligo esteso ai subappaltatori
- [ ] Conseguenza del mancato rispetto: esclusione o risoluzione

**4b. Esclusioni (artt. 94-98 D.Lgs. 36/2023)**
- [ ] Cause di esclusione automatica elencate (non solo rinvio all'articolo)
- [ ] Cause facoltative indicate con scelta esplicita della SA
- [ ] Self-cleaning (art. 99) previsto
- [ ] Nessun riferimento a vecchio art. 80

**4c. Requisiti di partecipazione**
- [ ] Fatturato richiesto <= doppio del valore stimato (salvo eccezioni motivate)
- [ ] DGUE richiesto (procedure sopra soglia)
- [ ] PassOE richiesto
- [ ] FVOE menzionato per la fase di verifica
- [ ] Nessun riferimento a vecchio art. 83

**4d. Subappalto (art. 119 D.Lgs. 36/2023)**
- [ ] Nessun limite percentuale generale non motivato
- [ ] Dichiarazione subappalto al momento dell'offerta (sopra soglia)
- [ ] Modalita' pagamento diretto al subappaltatore

**4e. Garanzia provvisoria (art. 117 D.Lgs. 36/2023)**
- [ ] Importo = 2% del valore stimato
- [ ] Tabella riduzioni per certificazioni di qualita'
- [ ] Schema fidejussione allegato o rinvio a modello ANAC

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

### Garanzia provvisoria (art. 117)
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
