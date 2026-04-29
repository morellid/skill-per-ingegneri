# Task: Verifica coerenza PFTE / Progetto esecutivo

Verifica che il progetto esecutivo sia **coerente** con il PFTE approvato, ai sensi dell'art. 41 co. 8 D.Lgs. 36/2023, e che contenga gli elaborati obbligatori previsti dall'Allegato I.7 art. 22 co. 4.

## Obiettivo

Produrre un report che evidenzi:
1. **Completezza** del progetto esecutivo rispetto all'art. 22 co. 4 dell'Allegato I.7
2. **Coerenza** fra PFTE e esecutivo su elementi chiave: identificazione dell'opera, ambito di intervento, importi di base, scelte progettuali, cronoprogramma
3. Eventuali **scostamenti motivati** o **non motivati** dell'esecutivo rispetto al PFTE

## Input richiesti

1. **Elenco elaborati del progetto esecutivo** (indice, albero cartelle, lista file)
2. **Elenco elaborati del PFTE approvato** (riferimento; se solo l'identificazione e l'importo basta, segnalarlo)
3. **Variabili di inquadramento** (vedi `genera-checklist-pfte.md`)
4. **Eventuale verbale o atto di approvazione del PFTE** che fissa i parametri di base
5. **Quadro economico approvato del PFTE** vs **quadro economico esecutivo** (entrambi se disponibili)
6. **Soggetto progettista**: e' lo stesso del PFTE (regola generale art. 41 co. 8) o diverso? Se diverso, motivazione formale.

Se l'input e' parziale, dichiararlo nel report e limitare la verifica.

## Fonti normative

Leggere prima di procedere:
- `references/estratti/dlgs-36-art-41.md` (in particolare comma 8)
- `references/estratti/allegato-i7-pfte.md` (per riferimento al PFTE)
- `references/estratti/allegato-i7-esecutivo.md` (struttura art. 22 co. 4)
- `references/estratti/dlgs-209-2024-modifiche.md`

## Procedura

### Passo 1 - Verifica completezza esecutivo (art. 22 co. 4)

Mappare l'elenco esecutivo ai 14+2 elaborati lett. a-p (+ p-bis, p-ter):

| Lett. | Elaborato | Articolo dettaglio | Quando obbligatorio |
|-------|-----------|--------------------|--|
| a | Relazione generale | All. I.7 art. 23 | Sempre |
| b | Relazioni specialistiche | All. I.7 art. 24 | Sempre quando le specialistiche del PFTE devono essere aggiornate |
| c | Elaborati grafici (architettonici, strutturali, impiantistici, mitigazione ambientale) | All. I.7 art. 25 | Sempre |
| d | Calcoli strutture e impianti | All. I.7 art. 26 | Sempre quando ricorrono strutture/impianti rilevanti |
| e | Piano di manutenzione opera + parti | All. I.7 art. 27 | Sempre |
| f | Aggiornamento PSC | All. I.7 art. 28 + D.Lgs. 81/2008 art. 100 | Sempre quando applicabile D.Lgs. 81/2008 |
| g | Quadro di incidenza manodopera | (in art. 22) | Sempre - funzionale a scorporo costi (art. 41 co. 14) |
| h | Cronoprogramma | (in art. 22) | Sempre - aggiornamento del cronoprogramma PFTE |
| i | Elenco prezzi unitari ed eventuali analisi | (in art. 22) | Sempre |
| l | Computo metrico estimativo + quadro economico | (in art. 22) | Sempre |
| m | Schema contratto + capitolato speciale d'appalto | (in art. 22) | Sempre |
| n | Piano particellare di esproprio aggiornato | (in art. 22) | Solo se necessarie procedure espropriative |
| o | Relazione tecnica + elaborati CAM | DM 256/2022 | Quando applicabili i CAM |
| p | Fascicolo dell'opera | D.Lgs. 81/2008 Allegato XVI | Sempre quando applicabile D.Lgs. 81/2008 |
| p-bis | Modelli informativi | art. 43 D.Lgs. 36/2023 | Solo se BIM obbligatorio |
| p-ter | Capitolato informativo | art. 43 D.Lgs. 36/2023 | Solo se BIM obbligatorio |

Per ogni elaborato classificare: presente / assente / inadeguato / non-applicabile / da-verificare.

### Passo 2 - Confronto identificativo

Verificare che l'esecutivo si riferisca **alla stessa opera** del PFTE:

- **Codice opera / CUP** (se dichiarato): deve coincidere
- **Descrizione opera**: il titolo dell'opera nell'esecutivo deve essere coerente con quello del PFTE
- **Localizzazione** (Comune, indirizzo, mappali): coerente
- **Stazione appaltante**: stessa entita' (salvo rare cessioni di RUP)

Segnalare ogni discrepanza in elenco.

### Passo 3 - Confronto economico

Confrontare i quadri economici:

- **Importo lavori (capitolo A)**: l'esecutivo dovrebbe sviluppare in dettaglio l'importo del PFTE. Scostamenti significativi (>10-15%) richiedono **giustificazione formale** della stazione appaltante.
- **Categorie SOA / OG/OS** (se dichiarate): coerenza tra PFTE e esecutivo.
- **Costi sicurezza non soggetti a ribasso**: l'esecutivo deve quantificare in modo definitivo i costi che il PFTE aveva stimato. La proporzione (in genere 1-3% sui lavori, dipende dalla categoria) deve essere coerente.
- **Quadro di incidenza manodopera**: presente nell'esecutivo (lett. g), deve essere coerente con il costo manodopera scorporato (art. 41 co. 14).
- **Somme a disposizione (capitolo B)**: l'esecutivo puo' affinarle, ma scostamenti macroscopici devono essere motivati.

### Passo 4 - Confronto progettuale

Verificare coerenza fra:

- **Piante / sezioni / prospetti**: superfici, volumi, ingombri devono essere coerenti (salvo modifiche motivate)
- **Cronoprogramma**: durata totale e fasi principali coerenti
- **Soluzioni strutturali**: tipologia (c.a., acciaio, legno, miste) coerente
- **Soluzioni impiantistiche**: tipologia (centralizzato/distribuito, fonti energetiche) coerente
- **Materiali e finiture**: linee generali coerenti
- **Vincoli (paesaggistici, archeologici, sismici)**: stesso quadro di vincoli

Modifiche significative dell'esecutivo rispetto al PFTE richiedono **motivazione scritta** della stazione appaltante e, se sostanziali, possono richiedere ri-approvazione del PFTE modificato.

### Passo 5 - Verifica progettista

Per art. 41 co. 8: l'esecutivo e' di regola redatto **dallo stesso soggetto** che ha predisposto il PFTE. Se il progettista e' diverso:

- Segnalare la discontinuita'
- Verificare che ci sia un atto formale che giustifichi la sostituzione
- Verificare che il nuovo progettista abbia formalmente assunto la responsabilita' di entrambi i livelli (per il proprio ambito)
- Ricordare l'art. 41 co. 8-bis (correttivo 2024) sulle prestazioni reintegrative del progettista in caso di errori/omissioni

### Passo 6 - Output

```markdown
# Verifica coerenza PFTE / Esecutivo - art. 41 + All. I.7 D.Lgs. 36/2023

**Data verifica**: [oggi]
**Opera**: [descrizione + CUP]
**PFTE riferimento**: [codice / data approvazione]
**Esecutivo**: [codice / data]

## Esito sintetico

[COERENTE | COERENTE CON OSSERVAZIONI | SCOSTAMENTI DA MOTIVARE | INCOMPLETO]

## A. Completezza esecutivo (art. 22 co. 4)

| Lett. | Elaborato | Stato | Note |
|-------|-----------|-------|----|
| a | Relazione generale | [presente/assente/...] | |
| b | Relazioni specialistiche | [...] | |
| ... |

Elaborati assenti / inadeguati: X

## B. Coerenza identificativa

| Elemento | PFTE | Esecutivo | Coerente? |
|----------|------|-----------|---------|
| Codice opera / CUP | [...] | [...] | si/no |
| Descrizione | [...] | [...] | si/no |
| Localizzazione | [...] | [...] | si/no |
| Stazione appaltante | [...] | [...] | si/no |

## C. Coerenza economica

| Voce | PFTE | Esecutivo | Scostamento | Note |
|------|------|-----------|-------------|----|
| Importo lavori | [...] | [...] | [%] | [coerente/da-motivare] |
| Costi sicurezza | [...] | [...] | [%] | |
| Quadro economico totale | [...] | [...] | [%] | |

## D. Coerenza progettuale

| Aspetto | PFTE | Esecutivo | Coerente? | Motivazione |
|---------|------|-----------|---------|----|
| Tipologia strutturale | [...] | [...] | | |
| Soluzione impiantistica principale | [...] | [...] | | |
| Cronoprogramma totale | [...] | [...] | | |
| Vincoli rilevati | [...] | [...] | | |

## E. Continuita' progettista (art. 41 co. 8)

- Progettista PFTE: [...]
- Progettista esecutivo: [...]
- [Stesso soggetto / Soggetto diverso con atto formale / Soggetto diverso senza atto noto]

## Problemi rilevati

| # | Area | Problema | Riferimento | Priorita' |
|---|------|----------|-------------|-----------|
| 1 | ... | ... | ... | ... |

## Raccomandazioni

- ...

## Elementi non valutabili automaticamente dalla skill

- Adeguatezza tecnica dei contenuti
- Calcoli e dimensionamenti
- Conformita' a norme di settore non Codice
- Verifica ex art. 42 della progettazione (responsabilita' di soggetto qualificato indipendente)

## Limiti di questa verifica

- Verifica documentale, non sopralluogo
- Verifica formale, non valutazione tecnica
- Dipendente dalla qualita' degli input forniti

## Rinvio al professionista firmatario

**La presente verifica non sostituisce la revisione del progettista firmatario, del RUP, ne' la verifica della progettazione ex art. 42 D.Lgs. 36/2023.**
```

## Casi limite da gestire

### Solo esecutivo, nessun PFTE (manutenzione art. 41 co. 5)
Per le manutenzioni con PFTE omesso: la verifica di coerenza non si applica. La skill deve invece controllare che l'esecutivo contenga **tutti gli elementi che sarebbero stati nel PFTE omesso** (art. 41 co. 5 ultimo periodo). Riformulare il report di conseguenza.

### Solo PFTE, nessun esecutivo (manutenzione art. 41 co. 5-bis correttivo 2024)
Verifica di coerenza non applicabile. Reindirizzare l'utente al task `verifica-completezza-pfte.md`.

### Scostamenti dovuti a varianti
Se le differenze derivano da una **variante in corso d'opera** (art. 120 D.Lgs. 36/2023), la skill rileva lo scostamento ma non lo qualifica come errore: la variante e' atto autorizzato dalla SA. Segnalare la presenza di una variante richiede esame della documentazione amministrativa.

### Progettazione esterna - riconciliazione PFTE/esecutivo
Quando entrambi i livelli sono affidati esternamente, applica art. 41 co. 9: l'avvio dell'esecutivo presuppone la determinazione della SA sul PFTE. Verificare la presenza dell'atto di approvazione del PFTE.

## Limiti di questo task

- Verifica **formale di coerenza** documentale, non valutazione tecnica.
- Non sostituisce **verifica ex art. 42**.
- Non valuta **adeguatezza tecnica** dei calcoli, scelte, soluzioni.
- Non gestisce automaticamente **varianti** o modifiche autorizzate.
- Non valuta la **legittimita'** dell'eventuale sostituzione del progettista.

## Esempi

Esempi dedicati al confronto PFTE/esecutivo non sono ancora inclusi in `examples/`. Sono previsti in versioni successive (vedi `CHANGELOG.md` Unreleased). Per esempi sul PFTE da solo (su cui questo task si appoggia per la sezione A) vedi:
- `examples/conforme-nuova-costruzione/` - PFTE completo per nuova scuola
- `examples/manutenzione-straordinaria-incompleto/` - PFTE manutenzione incompleto
