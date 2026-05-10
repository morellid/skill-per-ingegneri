# Task: Verifica completezza PFTE

Verifica che un PFTE gia' redatto contenga tutti gli elaborati obbligatori previsti dall'art. 6 co. 7 dell'Allegato I.7 D.Lgs. 36/2023, in funzione delle variabili di inquadramento dell'opera.

## Obiettivo

Produrre un report strutturato che indichi, per ciascun elaborato dell'art. 6 co. 7:
- **Stato**: presente / assente / inadeguato / non-applicabile / da-verificare
- **Citazione normativa precisa** (articolo + lettera Allegato I.7)
- **Problema rilevato** (quando presente)
- **Raccomandazione** (cosa integrare o chiarire)

## Input richiesti

1. **Elenco / indice degli elaborati del PFTE** in forma leggibile, in alternativa o in combinazione di:
   - Albero cartelle del PFTE depositato (es. `01_Relazioni/`, `02_Grafici/`, ...)
   - Indice della relazione generale
   - Lista file pdf consegnati alla stazione appaltante
   - Estratti di alcune relazioni se disponibili

2. **Variabili di inquadramento** (come per `genera-checklist-pfte.md`):
   - Categoria intervento
   - Importo lavori
   - Espropri si/no
   - VIA si/no
   - BIM si/no
   - Modalita' di affidamento
   - Regime manutenzione (se applicabile)
   - Verifica archeologica si/no

3. **Contesto opzionale**:
   - DIP redatto dal RUP (estratto): se fornito, permette il check di **coerenza** con cio' che il RUP ha richiesto
   - Quadro esigenziale: se fornito, verificare che gli elaborati lo recepiscano

Se l'input e' parziale (es. solo l'indice della relazione generale), procedere e segnalare nel report che la verifica e' limitata a cio' che e' stato fornito.

## Fonti normative

Leggere prima di procedere:
- `references/estratti/dlgs-36-art-41.md`
- `references/estratti/allegato-i7-pfte.md`
- `references/estratti/dlgs-209-2024-modifiche.md`

## Procedura

### Passo 1 - Riconoscimento elaborati nel PFTE

Mappare il contenuto fornito ai 18 elaborati dell'art. 6 co. 7 (lett. a-t, escluse j,k,w,x,y per convenzione legislativa italiana). Le denominazioni effettive nel PFTE possono variare; alcune euristiche di matching:

> **Riferimento**: l'elenco normativo e' all'Allegato I.7 art. 6 co. 7 (D.Lgs. 36/2023,
> GU n. 77 SO n. 12/L). Verificato verbatim in `references/fonti/dlgs-36-2023-allegato-i7.md`.

| Voce normativa | Possibili denominazioni nei PFTE reali |
|----------------|----------------------------------------|
| a) Relazione generale | "Relazione generale", "Relazione illustrativa generale", "01_Relazione generale" |
| b) Relazione tecnica + indagini | "Relazione tecnica", "Relazione tecnica generale", "Relazione geologica", "Relazione geotecnica", "Relazione idraulica", "Relazioni specialistiche" (insieme) |
| c) Verifica archeologica | "Relazione archeologica preventiva", "Verifica preventiva interesse archeologico", "VIA archeologica" |
| d) Studio impatto ambientale | "SIA", "Studio impatto ambientale", "Quadro di riferimento ambientale" |
| e) Relazione di sostenibilita' | "Relazione di sostenibilita'", "Sostenibilita' dell'opera" |
| f) Rilievi plano-altimetrici | "Rilievo topografico", "Rilievi", "Stato di consistenza", "Plani-altimetria" |
| g) Modelli informativi BIM | "Capitolato informativo", "Relazione BIM", "Modelli IFC", "BEP", "PIM" |
| h) Elaborati grafici | "Tavole", "Elaborati grafici", "Planimetrie", "Sezioni", "Prospetti" |
| i) Computo sommario | "Computo estimativo", "Stima sommaria", "Calcolo sommario" |
| l) Quadro economico | "Quadro economico", "QE" |
| m) Piano economico-finanziario | "PEF", "Piano economico-finanziario" (solo PPP) |
| n) Cronoprogramma | "Cronoprogramma", "Diagramma di Gantt" |
| o) PSC | "Piano di sicurezza e coordinamento", "PSC" |
| p) Capitolato informativo | "Capitolato informativo" (solo appalto integrato + BIM) |
| q) Piano preliminare manutenzione | "Piano di manutenzione", "Piano preliminare di manutenzione" |
| r) Monitoraggio geotecnico e strutturale | "Piano di monitoraggio strutturale", "Piano di monitoraggio geotecnico" |
| s) Monitoraggio ambientale (VIA / SA che lo richieda) | "Piano di monitoraggio ambientale", "PMA" |
| t) Piano particellare espropri | "Piano particellare di esproprio", "PPE" |

> Quando una denominazione e' ambigua (es. "relazioni specialistiche" puo' coprire b + parti di r/s), classificare come `da-verificare` e segnalare la lacuna documentale.

### Passo 2 - Classificazione di ciascuna voce

Per ogni lettera dell'art. 6 co. 7, classifica:

- **presente**: l'elaborato e' identificato chiaramente nell'indice/cartelle, con denominazione coerente.
- **assente**: l'elaborato e' obbligatorio per le variabili di inquadramento ma non e' presente.
- **inadeguato**: presente ma non sviluppa i contenuti minimi (vedi "Indicatori di inadeguatezza" sotto).
- **non-applicabile**: l'elaborato non e' richiesto per le variabili di inquadramento (es. piano espropri se no espropri).
- **da-verificare**: l'input non e' sufficiente per decidere.

### Passo 3 - Indicatori di inadeguatezza (per ogni elaborato)

> Questi sono indicatori di **prima istanza** per il check formale. La valutazione di adeguatezza tecnica spetta al progettista firmatario e al verificatore ex art. 42.

- **Relazione generale (a)**: deve descrivere l'opera, l'inquadramento, la genesi del progetto, le scelte fondamentali. Una relazione di poche pagine senza inquadramento normativo e' **inadeguata**.
- **Relazione tecnica (b)**: deve essere accompagnata da indagini, rilievi, studi specialistici. Un solo file "relazione tecnica" senza specialistiche per opere strutturali rilevanti e' **potenzialmente inadeguato**.
- **Studio di impatto ambientale (d)**: se opera soggetta a VIA, deve seguire la struttura del D.Lgs. 152/2006 (Quadro programmatico, progettuale, ambientale). Studi di "screening" senza VIA effettiva sono **inadeguati** se la VIA e' dovuta.
- **Elaborati grafici (h)**: devono includere planimetrie generali, planimetrie di dettaglio, sezioni, prospetti, schemi funzionali. Solo planimetrie senza sezioni/prospetti per nuova costruzione e' **inadeguato**.
- **Computo estimativo (i)**: deve essere "calcolo sommario dei lavori" coerente con la fase PFTE. Un solo importo lordo senza scomposizione e' **inadeguato**.
- **Quadro economico (l)**: deve esporre A) lavori, B) somme a disposizione, C) IVA. Un quadro economico senza distinzione lavori / somme a disposizione e' **inadeguato**.
- **PSC (o)**: deve seguire l'Allegato XV D.Lgs. 81/2008 anche in fase PFTE. Un PSC che dichiara "redazione rimandata a fase esecutiva" senza giustificazione e' **inadeguato** in PFTE base di gara.
- **Piano preliminare di manutenzione (q)**: deve coprire tutte le parti dell'opera. Un piano che cita solo "manutenzione ordinaria" senza dettaglio per componenti e' **potenzialmente inadeguato**.

### Passo 4 - Output

```markdown
# Verifica completezza PFTE - art. 41 + Allegato I.7 D.Lgs. 36/2023

**Data verifica**: [oggi]
**PFTE analizzato**: [identificativo]
**Inquadramento intervento**: [come dichiarato dall'utente]

## Esito sintetico

[COMPLETO | COMPLETO CON RISERVA | INCOMPLETO | DUBBIO | VERIFICA INSUFFICIENTE]

Elaborati richiesti: X
Elaborati presenti: Y
Elaborati assenti / inadeguati: Z

## Documenti pre-progettuali

| Documento | Stato | Riferimento |
|-----------|-------|-------------|
| Quadro esigenziale | [presente/assente/non-fornito] | All. I.7 art. 1 |
| DOCFAP | [presente/non-applicabile/...] | All. I.7 art. 2 |
| DIP | [presente/non-fornito/da-richiedere-al-RUP] | All. I.7 art. 3 |

## Dettaglio elaborati PFTE (art. 6 co. 7)

| Lett. | Elaborato | Stato | Riferimento | Note |
|-------|-----------|-------|-------------|----|
| a | Relazione generale | [presente/assente/inadeguato] | All. I.7 art. 7 | [breve nota] |
| b | Relazione tecnica + indagini | [...] | All. I.7 art. 8 | [...] |
| ... |

## Problemi rilevati

| # | Voce | Problema | Riferimento normativo | Priorita' |
|---|------|----------|----------------------|-----------|
| 1 | ... | ... | All. I.7 art. ... | Alta/Media/Bassa |

## Raccomandazioni

- Integrare la voce X con [...]
- Chiarire se [...]
- Recuperare il documento Y dal RUP per cross-check con il DIP

## Elementi non valutabili automaticamente dalla skill

- Adeguatezza tecnica dei contenuti dei singoli elaborati
- Coerenza con il DIP del RUP (se non fornito alla skill)
- Conformita' a norme di settore non incluse nel Codice
- Calcoli, stime, indagini specifiche

## Limiti di questa verifica

- Verifica formale di **presenza** e indicatori di base, non valutazione di adeguatezza tecnica.
- Verifica su documento, non su sopralluogo.
- Non sostituisce la verifica ex art. 42 del Codice (verificatore qualificato).
- I risultati dipendono dalla completezza dell'input fornito.

## Rinvio al professionista firmatario

**La presente verifica non sostituisce la revisione del progettista firmatario, del RUP, ne' del verificatore ex art. 42 D.Lgs. 36/2023.** La responsabilita' finale sulla completezza e adeguatezza del PFTE resta al professionista firmatario.
```

## Casi limite da gestire

### Indice non disponibile / formato strano
Se l'utente fornisce solo testi non strutturati senza chiari riferimenti agli elaborati, dichiararlo nel report e ridurre la verifica a cio' che e' identificabile.

### PFTE per manutenzione (regime art. 41 co. 5-bis)
Applicare la lista minima dell'**Allegato I.7 art. 6 co. 8-bis** (relazione generale, computo metrico estimativo, elenco prezzi unitari, PSC). Verificare anche l'**eccezione** dell'art. 41 co. 5-bis: il regime NON si applica se l'intervento prevede rinnovo o sostituzione di **parti strutturali** o **impianti**. In quel caso non e' "manutenzione co. 5-bis" e si applica il regime ordinario PFTE + esecutivo.

NON segnalare come "assenti" gli elaborati esclusi dal regime (relazione di sostenibilita', SIA, capitolato informativo, piano espropri ecc.). Segnalare invece, se mancano, il cronoprogramma e la descrizione tecnica come **best practice** non obbligatorie ma utili.

### PFTE in variante urbanistica
Aspettarsi un PFTE piu' ampio: relazioni urbanistiche e ambientali piu' sviluppate, piano espropri tipicamente presente, sostituzione del progetto preliminare e definitivo per art. 41 co. 7. Segnalare se mancano elementi tipici (analisi vincoli, conformita' urbanistica).

### Appalto integrato
Verificare presenza obbligatoria di disciplinare descrittivo e prestazionale (art. 14), capitolato informativo (art. 13-ter) se BIM, e PSC sviluppato per consentire la quantificazione costi sicurezza non ribassabili.

### Carenza di elaborati per opere sopra soglia europea
Per opere di importo pari o superiore alla soglia europea per i lavori (rinvio dinamico ad art. 14 D.Lgs. 36/2023), segnalare se manca il DOCFAP (Allegato I.7 art. 2 co. 5): il PFTE post-DOCFAP e' presunto allineato alle alternative valutate, e l'assenza del DOCFAP rende difficoltosa la verifica di coerenza. Per opere fra 150.001 EUR e la soglia europea, il DOCFAP e' facoltativo (co. 6): la sua assenza non e' un problema, ma se la SA lo aveva incluso nel DIP, segnalarne la mancanza.

## Limiti di questo task

- Verifica **formale** sulla presenza degli elaborati, non sulla loro adeguatezza tecnica.
- Non sostituisce la **verifica della progettazione ex art. 42** del Codice.
- Non valuta la **coerenza con il DIP** se il DIP non e' fornito.
- Non valuta le **stime di costo** ne' le scelte progettuali sostanziali.
- Non valuta il rispetto delle **norme di settore** (NTC, antincendio, accessibilita', acustica, energia, CAM se non e' fornito specifico riferimento).

## Esempi

Vedi `examples/`:
- `conforme-nuova-costruzione/` - PFTE completo per nuova scuola
- `manutenzione-straordinaria-incompleto/` - PFTE manutenzione con elaborati mancanti
