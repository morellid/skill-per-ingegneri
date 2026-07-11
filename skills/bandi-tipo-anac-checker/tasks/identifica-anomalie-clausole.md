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
- `references/estratti/anac-bandi-tipo-clausole-ai-l132-2025.md` (clausole AI obbligatorie dal 30 maggio 2026)
- `references/fonti/anac-bando-tipo-n1-2023-agg-del-148-2026.md` (sezione "Paragrafo 28": clausola alternativa accesso agli atti per inversione procedimentale, Parere CdS n. 61/2026)
- Se l'oggetto e' SIA: `references/estratti/anac-bando-tipo-2-2026-sia-requisiti-bim.md` (importo 65/35, BIM, equo compenso)

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
- Assenza di menzione del CCNL (violazione art. 11 co. 2 D.Lgs. 36/2023)
- Assenza di DGUE o mancata compilazione sulla PAD (art. 91 D.Lgs. 36/2023)
- Assenza di soccorso istruttorio o clausola che lo esclude genericamente

### Passo 2 - Analisi per categorie di anomalia

**Categoria A - Anomalie normative (violazioni di legge)**

Cercare specificamente:

| Area | Indicatore di anomalia | Art. violato |
|------|----------------------|-------------|
| Clausola sociale | CCNL non indicato o "di settore" generico senza codice alfanumerico | Art. 11 co. 2 D.Lgs. 36/2023 |
| Esclusioni | Elenco cause esclusione incompleto o basato su vecchio art. 80 D.Lgs. 50/2016 | Artt. 94, 95, 96 D.Lgs. 36/2023 |
| Requisiti | Fatturato > 2x valore stimato senza motivazione (per servizi/forniture) | Art. 100 co. 11 D.Lgs. 36/2023 |
| DGUE | Assente o non compilato sulla PAD | Art. 91 D.Lgs. 36/2023 |
| Subappalto | Limite percentuale non motivato (es. "max 30%") | Art. 119 D.Lgs. 36/2023 |
| Garanzia provvisoria | Importo non coerente con base 2% (range 1-4%) o riduzioni omesse | Art. 106 D.Lgs. 36/2023 |
| Garanzia definitiva | Percentuale errata (es. "5-10%" invece di 10% con incrementi ribasso) | Art. 117 D.Lgs. 36/2023 |
| Soccorso istruttorio | Escluso per documenti amministrativi o termine fuori range 5-10 gg | Art. 101 D.Lgs. 36/2023 |
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

**Categoria E - Anomalie clausole AI (per gare dal 30 maggio 2026)**

Dopo l'efficacia della Delibera 148/2026 (Bando 1) e Delibera 153/2026 (Bando 2 SIA), il paragrafo 15.1 / Domanda di partecipazione **deve** contenere le dichiarazioni AI:
- [ ] Clausola AI assente: **critico** (violazione dello schema-tipo ANAC vincolante).
- [ ] Riferimenti normativi parziali (solo Reg. UE 2024/1689 oppure solo L. 132/2025): **sostanziale**.
- [ ] Per servizi intellettuali / SIA: clausola in versione generica anziche' versione art. 13 L. 132/2025 (con specifica tipologia AI + garanzie prevalenza/controllo/verifica): **sostanziale**.
- [ ] Divieto generalizzato d'uso AI (clausola piu' restrittiva del modello-tipo) senza motivazione: **sostanziale**.
- [ ] Per SIA: omessa clausola in paragrafo 16 sull'indicazione attivita' AI strumentali in offerta tecnica: **sostanziale**.

**Categoria F - Anomalie specifiche SIA (Bando 2/2026)**

Vedi `references/estratti/anac-bando-tipo-2-2026-sia-requisiti-bim.md` per la checklist completa. Anomalie tipiche:

| Indicatore | Riferimento | Rischio |
|-----------|-------------|---------|
| Importo base senza distinzione 65% non ribassabile / 35% ribassabile | Art. 41 c. 15-bis Codice | Critico |
| Punteggio offerta economica > 30 punti | Art. 41 c. 15-bis lett. b | Critico |
| Maggiorazione 10% non applicata su onorari per progettazione >2M euro con BIM | Allegato I.13 art. 2 c. 5 | Sostanziale |
| Equo compenso violato (richiesta prestazioni gratuite o ulteriori) | Art. 8 L. 49/2023 + Allegato I.13 | Critico |
| BIM imposto in procedure lavori <2M euro senza riferimento Capitolato informativo | Art. 43 c. 2 Codice, Allegato I.9 | Sostanziale |
| Figure BIM richieste non corrispondono a UNI 11337-7 (BIM Manager/Coordinator/Specialist/CDE Manager) | Bando 2/2026 par. 6.1 h-k | Sostanziale |
| Capitolato informativo non allegato al disciplinare | Allegato I.9 c. 8 | Critico (se BIM) |
| Offerta tecnica BIM senza documento autonomo "offerta di gestione informativa digitale" | Bando 2/2026 par. 16 c) | Sostanziale |
| Certificazione UNI 11337-7:2018 richiesta come requisito anziche' come premio | Bando 2/2026 par. 6.1 NB | Sostanziale |
| DUVRI richiesto per SIA puramente intellettuali | Art. 26 c. 3-bis D.Lgs. 81/2008 | Formale |
| Requisiti tecnici basati su contratti ultimi 5 anni anziche' 10 | Art. 40 c. 1-bis Allegato II.12 | Sostanziale |

**Categoria G - Anomalie accesso agli atti / inversione procedimentale (paragrafo 28, Delibera 148/2026 - gare indette dal 30 maggio 2026)**

Vedi `references/fonti/anac-bando-tipo-n1-2023-agg-del-148-2026.md` (sezione "Paragrafo 28").
- [ ] Gara con inversione procedimentale ma paragrafo Accesso agli atti senza la clausola alternativa (offerte rese reciprocamente disponibili ai primi cinque classificati, ad eccezione della documentazione amministrativa degli offerenti dal secondo al quinto posto non verificata dalla SA): **sostanziale** (deroga allo schema-tipo aggiornato).
- [ ] Paragrafo Accesso agli atti che riporta ancora il box N.B. "in attesa del parere del Consiglio di Stato": **formale** (disciplinare non aggiornato: il parere n. 61 del 13/01/2026 e' stato emesso e recepito dalla Delibera 148/2026, che ha eliminato il box).
- [ ] Modalita' con cui la SA garantisce la disponibilita' dei documenti non indicata: **formale**.
- [ ] Nessuna previsione di accesso per i partecipanti collocatisi oltre il quinto posto (artt. 3-bis e 22 L. 241/1990): **sostanziale**.
- Nota: per gare indette prima del 30/05/2026 si applica la versione precedente dello schema (Delibera 365/2025): la clausola alternativa non e' esigibile e la sua assenza non e' un'anomalia.

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
