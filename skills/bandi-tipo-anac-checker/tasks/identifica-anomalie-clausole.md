# Task: Identificazione anomalie e clausole non standard

Analizza un disciplinare di gara alla ricerca di anomalie, clausole insolite,
deroghe non giustificate rispetto agli schemi ANAC e indicatori di rischio TAR,
senza necessariamente confrontare l'intero documento con uno schema specifico.

## Obiettivo

Produrre un elenco ordinato per priorita' delle anomalie nel disciplinare, con:
- **Tipo di anomalia**: normativo / strutturale / redazionale
- **Clausola**: sezione e testo della clausola anomala
- **Motivazione**: perche' e' anomala (violazione di legge, deroga non giustificata, ...)
- **Rischio**: critico / sostanziale / formale
- **Raccomandazione**: come correggere o giustificare

## Input richiesti

1. **Testo del disciplinare** (intero o sezione specifica da analizzare)
2. **Tipo di contratto** (facoltativo ma aiuta a contestualizzare): lavori / servizi / forniture
3. **Criterio di aggiudicazione** (facoltativo): PPB o OEPV
4. **Contesto specifico** (facoltativo): PNRR, settore speciale, SA nuova, migrazione vecchio modello, ...

## Fonti normative

Leggere prima di procedere:
- `references/estratti/dlgs-36-artt-clausole-disciplinare.md`
- `references/estratti/anac-bandi-tipo-struttura-2023.md` (sezione "Indicatori di disciplinare non aggiornato")

## Procedura

### Passo 1 - Scansione rapida per indicatori critici

Prima di un'analisi approfondita, cercare i seguenti pattern ad alto impatto:

**Pattern vecchio codice (D.Lgs. 50/2016)**:
- Presenza di "D.Lgs. 50" o "Codice del 2016" o "D.Lgs. 18 aprile 2016"
  -> Ogni riferimento va esaminato: potrebbe essere rimasto dal modello precedente
- "art. 80" -> vecchio codice esclusioni (nuovo: artt. 94-98)
- "art. 83" -> vecchio codice requisiti (nuovo: artt. 100-103)
- "art. 105" -> vecchio codice subappalto (nuovo: artt. 119-120)
- "art. 93" -> vecchio codice garanzie (nuovo: artt. 117-118)

**Pattern subappalto illegittimo**:
- "subappalto" seguito da "%" o "massimo" o "non superiore al"
  -> Verificare: un limite percentuale generale non motivato e' illegittimo (art. 119 D.Lgs. 36/2023)
- "30 per cento" o "40 per cento" nella sezione subappalto
  -> Quasi certamente un retaggio del vecchio codice: va rimosso

**Pattern requisiti sproporzionati**:
- Fatturato richiesto > doppio del valore stimato del contratto
  -> Probabile violazione art. 102 D.Lgs. 36/2023: rischio ricorso per limitazione concorrenza
- Richiesta di certificazioni ISO, rating di legalita', SOA in classi superiori al necessario
  senza motivazione proporzionata all'oggetto

**Pattern clausole mancanti ad alto impatto**:
- Assenza di menzione del CCNL (violazione art. 11 D.Lgs. 36/2023)
- Assenza di DGUE (per procedure sopra soglia: art. 87 D.Lgs. 36/2023)
- Assenza di soccorso istruttorio o clausola che lo esclude genericamente

### Passo 2 - Analisi per categorie di anomalia

**Categoria A - Anomalie normative (violazioni di legge)**

Cercare specificamente:

| Area | Indicatore di anomalia | Art. violato |
|------|----------------------|-------------|
| Clausola sociale | CCNL non indicato o "di settore" generico | Art. 11 D.Lgs. 36/2023 |
| Esclusioni | Elenco cause esclusione incompleto o basato su vecchio art. 80 | Artt. 94-98 D.Lgs. 36/2023 |
| Requisiti | Fatturato > 2x valore stimato senza motivazione | Art. 100 D.Lgs. 36/2023 |
| DGUE | Assente in procedure sopra soglia | Art. 91 D.Lgs. 36/2023 |
| Subappalto | Limite percentuale non motivato | Art. 119 D.Lgs. 36/2023 |
| Garanzia provvisoria | Importo non coerente con base 2% o scelta non motivata | Art. 106 D.Lgs. 36/2023 |
| Soccorso istruttorio | Escluso anche per documenti amministrativi (non dell'offerta) | Art. 101 D.Lgs. 36/2023 |
| OEPV | Criteri non collegati all'oggetto del contratto | Art. 108 co. 6 D.Lgs. 36/2023 |

**Categoria B - Deroghe allo schema ANAC non giustificate**

Sono deroghe problematiche (non illegali, ma rischiose):
- Sezioni mancanti rispetto alla struttura standard ANAC
- Riordino delle sezioni in modo insolito senza spiegazione
- Clausole aggiuntive non presenti nello schema che limitano la partecipazione
  (es. requisiti aggiuntivi, termini piu' brevi del minimo, ...)
- Omissione delle riduzione della garanzia provvisoria per certificazioni di qualita'
  (la SA e' libera di non applicarle, ma deve indicarlo)

**Categoria C - Anomalie redazionali e di coerenza interna**

- Importo indicato in piu' punti con valori diversi
- Data o termine indicati erroneamente (es. termine offerte nel passato, o prima della
  pubblicazione prevista)
- CIG non compilato o con formato errato
- CPV non pertinente all'oggetto
- Riferimenti interni rotti (es. "come indicato nella sezione X" dove la sezione X non esiste)
- Testo in corsivo o parentesi "[da compilare]" non completato

**Categoria D - Anomalie specifiche per OEPV** (se criterio e' OEPV)

Vedere la skill `oepv-valutatore-offerte-tecniche` per la verifica dettagliata
della matrice criteri. Segnalare qui solo le anomalie strutturali:
- Matrice criteri assente dal disciplinare
- Pesi non indicati per i criteri
- Formula offerta economica non esplicitata
- Tre categorie obbligatorie (basse emissioni CO2, welfare, parita' di genere) assenti

### Passo 3 - Prioritizzazione e output

Classificare ogni anomalia trovata:

**Critico** = violazione di legge o clausola obbligatoria mancante
- Rischio: esclusione dalla procedura, annullamento degli atti di gara
- Azione: correzione obbligatoria prima della pubblicazione

**Sostanziale** = deroga non giustificata allo schema ANAC o clausola anomala
- Rischio: ricorso TAR, onere di motivazione sulla SA
- Azione: correggere o aggiungere motivazione nel disciplinare

**Formale** = imprecisione redazionale, riferimento normativo impreciso, incoerenza interna
- Rischio: nessun rischio procedurale diretto, ma imprecisioni che confondono i partecipanti
- Azione: correggere per chiarezza

```markdown
# Identificazione anomalie - Disciplinare di gara
**Oggetto**: [oggetto appalto se disponibile]
**Tipo contratto**: [lavori/servizi/forniture se disponibile]
**Data analisi**: [data]

---

## Riepilogo anomalie

| Priorita' | Numero anomalie | Azione richiesta |
|-----------|----------------|-----------------|
| Critico | [N] | Correzione obbligatoria prima della pubblicazione |
| Sostanziale | [N] | Correggere o giustificare |
| Formale | [N] | Correggere per chiarezza |

---

## Anomalie critiche

### C1. [Titolo anomalia]
**Sezione disciplinare**: [dove si trova]
**Testo trovato**: "[estratto rilevante]"
**Problema**: [spiegazione]
**Riferimento normativo**: [art. X co. Y D.Lgs. 36/2023]
**Azione**: [cosa fare]

### C2. ...

---

## Anomalie sostanziali

### S1. [Titolo anomalia]
**Sezione disciplinare**: [dove si trova]
**Testo trovato**: "[estratto]"
**Problema**: [spiegazione]
**Schema ANAC**: [cosa dice lo schema standard]
**Azione**: [correggere / aggiungere motivazione: "..."]

---

## Anomalie formali

### F1. [Titolo anomalia]
**Sezione**: [dove]
**Problema**: [spiegazione breve]
**Correzione**: [testo corretto]

---

## Indicatori di mancato aggiornamento al D.Lgs. 36/2023

[Elenco specifico dei riferimenti al vecchio codice trovati, se presenti]

---

## Avvertenze

- L'analisi si basa sul testo del disciplinare fornito
- Non sostituisce la revisione legale del documento completo
- Per le anomalie sulle clausole OEPV, usare la skill
  oepv-valutatore-offerte-tecniche per l'analisi dettagliata della matrice criteri
```

## Pattern di anomalie ricorrenti da conoscere

### 1. Disciplinare copiato dal vecchio codice senza aggiornamento
**Sintomo**: molti riferimenti a D.Lgs. 50/2016, art. 80, art. 83, limite subappalto 30%
**Frequenza**: alta (moltissime SA usano ancora modelli del 2016-2021)
**Rischio**: critico - ogni procedura e' contestabile
**Raccomandazione**: revisione sistematica e sostituzione di tutti i riferimenti normativi

### 2. Requisiti di fatturato sproporzionati
**Sintomo**: richiesta di fatturato >= 3x o 4x il valore stimato
**Frequenza**: alta per servizi professionali e IT
**Rischio**: sostanziale/critico - ricorso per limitazione della concorrenza
**Raccomandazione**: ridurre a max 2x o giustificare con la complessita' dell'appalto

### 3. Subappalto ancora limitato al 30%
**Sintomo**: "subappalto non superiore al 30% (o 40%) del valore contratto"
**Frequenza**: alta - molti RUP non conoscono la modifica
**Rischio**: critico - la clausola e' nulla per contrasto con art. 119 D.Lgs. 36/2023
**Raccomandazione**: rimuovere il limite percentuale generale; se si vuole limitare
il subappalto per lavorazioni specifiche, motivarlo

### 4. CCNL generico o assente
**Sintomo**: "CCNL applicabile al settore" senza specifica, o sezione assente
**Frequenza**: media
**Rischio**: critico - violazione art. 11 D.Lgs. 36/2023
**Raccomandazione**: indicare il CCNL specifico (es. "CCNL Metalmeccanici Industria",
"CCNL Edilizia Industria", "CCNL Studi Professionali")

### 5. Soccorso istruttorio escluso per tutti i documenti
**Sintomo**: "la mancanza di qualsiasi documento comporta l'esclusione"
**Frequenza**: bassa ma presente
**Rischio**: sostanziale - viola art. 101 D.Lgs. 36/2023
**Raccomandazione**: distinguere documenti per cui il soccorso istruttorio e' ammesso
(documenti amministrativi) da quelli per cui non lo e' (offerta tecnica ed economica)

### 6. DGUE assente per gare sopra soglia
**Sintomo**: sezione documentazione amministrativa senza menzione del DGUE
**Frequenza**: bassa
**Rischio**: critico per procedure sopra soglia (art. 87 D.Lgs. 36/2023)
**Raccomandazione**: aggiungere il DGUE come documento obbligatorio con link al format

### 7. PassOE e FVOE assenti
**Sintomo**: nessuna menzione del sistema di verifica ANAC
**Frequenza**: media
**Rischio**: sostanziale - la verifica dei requisiti post-aggiudicazione risulta
non disciplinata
**Raccomandazione**: aggiungere la sezione verifica requisiti con PassOE e FVOE

## Limiti di questo task

- L'analisi e' piu' efficace quando si ha il testo completo del disciplinare
- Per sezioni lunghe o altamente tecniche (es. capitolato speciale allegato),
  l'utente deve indicare le parti specifiche da analizzare
- Non e' un sostituto del confronto puntuale con il testo verbatim degli schemi ANAC

## Esempi

Vedi `examples/`:
- `non-conforme-lavori-anomalie/` - disciplinare lavori con multipli problemi tipici
