# AGENTS.md - bandi-tipo-anac-checker

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Verifica formale della conformita' di un disciplinare di gara agli schemi ANAC (bandi-tipo) per le procedure di appalto pubblico ai sensi del D.Lgs. 31 marzo 2023 n. 36 (Codice dei contratti pubblici). Target: RUP e stazioni appaltanti che devono pubblicare una procedura di gara e vogliono verificare la conformita' del disciplinare prima della pubblicazione. Il rischio principale e' la presenza di clausole non conformi al nuovo codice o deroghe non giustificate rispetto agli schemi ANAC, che espongono la procedura a ricorso TAR con annullamento degli atti di gara.

## Fonti autoritative

Fonti catalogate in `references/sources.yaml`:

- **D.Lgs. 36/2023** - id `dlgs-36-2023-originale-gu-2023` - fonte primaria vincolante (nuovo codice contratti pubblici)
- **D.Lgs. 209/2024 (correttivo)** - id `dlgs-209-2024-correttivo` - modifiche al codice
- **ANAC Schemi disciplinare 2023 - Servizi/Forniture PPB** - id `anac-schema-disciplinare-sf-ppb-2023`
- **ANAC Schemi disciplinare 2023 - Servizi/Forniture OEPV** - id `anac-schema-disciplinare-sf-oepv-2023`
- **ANAC Schemi disciplinare 2023 - Lavori PPB** - id `anac-schema-disciplinare-lavori-ppb-2023`
- **ANAC Schemi disciplinare 2023 - Lavori OEPV** - id `anac-schema-disciplinare-lavori-oepv-2023`

Estratti in `references/estratti/`:
- `dlgs-36-artt-clausole-disciplinare.md` - artt. 11, 74, 87, 90, 94-103, 117-120 D.Lgs. 36/2023
- `anac-bandi-tipo-struttura-2023.md` - struttura e clausole obbligatorie degli schemi ANAC

## Articoli e punti chiave

**AVVERTENZA**: La numerazione degli articoli del D.Lgs. 36/2023 e' diversa dal D.Lgs. 50/2016.
Verificare sempre il numero esatto su Normattiva prima di citare un articolo in un documento.

- **Art. 11**: clausole sociali obbligatorie - CCNL applicabile al settore e alla zona geografica; operatore economico deve garantire ai lavoratori condizioni non inferiori al CCNL
- **Art. 57**: criteri ambientali minimi (CAM) - obbligatori per le categorie coperte dai DM attuativi
- **Art. 58**: suddivisione in lotti - motivazione obbligatoria se appalto non suddiviso
- **Art. 60**: revisione prezzi - obbligatoria per contratti > 12 mesi
- **Art. 74 co. 1**: contenuto minimo del bando di gara (oggetto, CPV, importo, criteri selezione, criterio aggiudicazione, termine presentazione offerte)
- **Art. 87**: disciplinare di gara e capitolato speciale (NON il DGUE: quello e' art. 91)
- **Art. 91**: DGUE - obbligatorio per procedure sopra soglia; format europeo standardizzato
- **Art. 90**: comunicazioni - modalita' digitali obbligatorie; piattaforma certificata
- **Art. 94**: motivi di esclusione automatica (condanne penali, violazioni fiscali, false dichiarazioni, irregolarita' grave)
- **Art. 95-98**: motivi di esclusione non automatica (insolvenza, illecito professionale, conflitti di interesse)
- **Art. 100**: criteri di selezione e requisiti speciali - include proporzionalita' del fatturato richiesto
- **Art. 101**: soccorso istruttorio - ammesso per documenti amministrativi; non ammesso per carenze che incidono sull'offerta
- **Art. 106**: garanzia provvisoria - base 2% con possibilita' di modifica motivata (1-4%); riduzioni per certificazioni qualita'
- **Art. 117**: garanzia definitiva - 5-10% in funzione del ribasso
- **Art. 119-120**: subappalto - nessun limite percentuale generale; indicazione subappaltatori sopra soglia; pagamento diretto in certi casi

## Convenzioni specifiche

### Cosa NON fare

- Non affermare mai che un disciplinare e' "legalmente valido" o "privo di rischi TAR": la skill produce un'analisi di conformita' formale, non una certificazione di legittimita'.
- Non confrontare clausole con il D.Lgs. 50/2016 (vecchio codice) come se fosse ancora vigente: il D.Lgs. 36/2023 e' vigente dal 1 luglio 2023. Il vecchio codice e' rilevante solo per identificare riferimenti obsoleti da segnalare come errori.
- Non produrre testo sostitutivo di clausole da inserire direttamente nel disciplinare senza avvertenza che richiede revisione legale.
- Non trattare gli schemi ANAC come testo intangibile: le deroghe motivate sono ammesse; il compito e' segnalarle e valutarne il rischio, non rifiutarle categoricamente.
- Non confondere i requisiti minimi obbligatori per legge (D.Lgs. 36/2023) con le clausole degli schemi ANAC (standard per SA qualificate): sono livelli diversi di obbligatorieta'.

### Cosa fare

- Citare sempre l'articolo e il comma preciso per ogni regola applicata (es. "art. 94 co. 1 lett. a) D.Lgs. 36/2023" non "il codice").
- Classificare le anomalie in tre livelli di severita':
  - **Critico**: articolo di legge violato o clausola obbligatoria mancante -> rischio esclusione dalla procedura o annullamento degli atti
  - **Sostanziale**: deroga allo schema ANAC non motivata -> rischio ricorso TAR, onere motivazionale sulla SA
  - **Formale**: imprecisione redazionale, rinvio normativo impreciso ma non incide sulla sostanza -> nessun rischio, ma va corretto
- Verificare sempre se il disciplinare fa ancora riferimento al vecchio codice (D.Lgs. 50/2016, artt. 80/83/...): e' il primo segnale di un documento non aggiornato.
- Per ogni deroga identificata: (a) cosa dice lo schema ANAC standard, (b) cosa dice il disciplinare, (c) se la deroga e' motivata, (d) livello di rischio.
- Segnalare quando un confronto richiederebbe il testo aggiornato degli schemi ANAC: la skill non ha accesso in tempo reale ai PDF ANAC; l'utente deve verificare sul portale ANAC la versione corrente.

## Validatori

- Nessun validatore Livello 2 identificato al momento del rilascio. La skill richiede validazione da RUP esperto o consulente legale specializzato in appalti pubblici prima di passare a Livello 2.

## Stato attuale

- Versione: 0.1.0-alpha (vedi `CHANGELOG.md`)
- Validazione: Livello 1 (revisione interna, nessun esperto di dominio esterno)
- Task files: 2 (check-conformita-disciplinare, identifica-anomalie-clausole)
- Esempi: 1 conforme (servizi/forniture PPB) + 1 non conforme (lavori con anomalie multiple)
- Known issues: schemi ANAC non embedabili per intero; la skill verifica struttura e requisiti normativi, non il testo verbatim degli schemi; soglie europee aggiornate annualmente, verificare i valori correnti
