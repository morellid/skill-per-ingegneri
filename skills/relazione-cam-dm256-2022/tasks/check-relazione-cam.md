# Task: Verifica relazione CAM esistente

Data una Relazione Tecnica dei Requisiti Ambientali CAM gia' redatta, verifica la completezza e la conformita' ai requisiti del DM 23/06/2022 n. 256 e segnala lacune, sezioni mancanti o affermazioni insufficientemente supportate.

## Obiettivo

Restituire all'utente:

- **Esito complessivo**: CONFORME / LACUNOSA / NON CONFORME (con spiegazione)
- **Tabella di verifica per criterio**: per ogni criterio applicabile alla tipologia di intervento, esito (OK / LACUNOSO / MANCANTE) con spiegazione delle anomalie
- **Lista delle azioni correttive richieste**: descrizione dettagliata di cosa aggiungere, modificare o documentare
- **Criteri mancanti**: criteri del DM 256/2022 non trattati nella relazione, con indicazione se obbligatori o facoltativi

## Input richiesti

1. **Tipologia di intervento dichiarata nella relazione** (NC/R1/R2/MS): se non indicata nella relazione, chiederla all'utente.

2. **Testo della relazione da verificare**: l'utente fornisce il testo completo (incollato nella chat o come file allegato).

3. **Eventuali documenti allegati citati nella relazione** (se disponibili): EPD, certificati FSC/PEFC, APE di progetto, piano rifiuti C&D, etc. La verifica della relazione e' possibile anche senza questi documenti, ma l'esito sara' parziale (non si puo' verificare la coerenza dei dati tecnici).

4. **Importo dei lavori** (per il criterio 2.9): se non indicato nella relazione, chiederlo.

5. **Tipo di gara** (prezzo piu' basso / OEPV): per verificare se i criteri premianti devono essere presenti.

## Fonti normative

Leggere prima di procedere:

- `references/estratti/dm-256-2022-articoli-chiave.md` - definizioni e obblighi
- `references/estratti/dm-256-2022-allegato-criteri-2x.md` - requisiti minimi criteri di base
- `references/estratti/dm-256-2022-allegato-criteri-premianti.md` - criteri premianti (se OEPV)
- `references/estratti/dlgs-36-2023-art57.md` - base normativa dell'obbligo

## Procedura

### Passo 1 - Analisi strutturale della relazione

Verificare se la relazione:
- E' intestata correttamente con indicazione esplicita del DM 256/2022 come riferimento normativo.
- Indica la tipologia di intervento (NC/R1/R2/MS).
- Ha sezioni o paragrafi dedicati ai criteri CAM (anche se non numerati esplicitamente con la numerazione del DM).
- Contiene dichiarazioni di conformita' o non applicabilita' per ciascun criterio.

Se la relazione non menziona il DM 256/2022 come riferimento normativo, segnalare immediatamente:
> "ATTENZIONE: la relazione non cita esplicitamente il DM 23/06/2022 n. 256 come riferimento normativo CAM applicabile. Questo e' un vizio formale che la stazione appaltante potrebbe rilevare. Verificare se la relazione faceva riferimento al precedente DM 11/01/2017 (non piu' applicabile per gare bandite dopo il 08/10/2022)."

### Passo 2 - Verifica criterio per criterio

Per ogni criterio di base (2.1-2.9) applicabile alla tipologia di intervento classificata, analizzare la relazione e produrre un esito:

**OK**: la sezione e' presente, il requisito minimo e' citato, la scelta progettuale e' descritta e la documentazione di verifica e' indicata.

**LACUNOSO**: la sezione e' presente ma mancano dati tecnici specifici (es. la relazione afferma "si utilizzera' calcestruzzo con aggregati riciclati" ma non indica la percentuale), oppure la documentazione di verifica non e' specificata, oppure la dichiarazione di conformita' e' generica e non verificabile.

**MANCANTE**: il criterio non e' trattato nella relazione (e dovrebbe esserlo dato il tipo di intervento).

**NON APPLICABILE - GIUSTIFICATO**: il criterio e' dichiarato non applicabile con motivazione accettabile.

**NON APPLICABILE - NON GIUSTIFICATO**: il criterio e' dichiarato non applicabile senza motivazione o con motivazione insufficiente.

Tabella di output:

| # | Criterio | Esito | Note / Azioni correttive |
|---|---|---|---|
| 2.1 | Qualita' del suolo | [esito] | [dettaglio] |
| 2.2 | Durabilita' | [esito] | [dettaglio] |
| 2.3.2 | Calcestruzzi | [esito] | [dettaglio] |
| ... | ... | ... | ... |
| 2.8 | Cantiere sostenibile | [esito] | [dettaglio] |
| 2.9 | ISO 14001 esecutore | [esito] | [dettaglio] |

### Passo 3 - Verifica criteri premianti (solo se OEPV)

Se la gara e' OEPV, verificare:
- La relazione indica quali criteri premianti vengono adottati?
- Per ogni criterio premiante dichiarato: la prestazione e' superiore al minimo di base? I dati tecnici sono sufficientemente precisi?
- Nessun criterio premiante dichiarato e' considerato un problema (e' facoltativo), ma segnalarlo all'utente come opportunita' di miglioramento del punteggio tecnico.

### Passo 4 - Esito complessivo e lista azioni correttive

**Esito complessivo**:
- **CONFORME**: tutti i criteri applicabili hanno esito OK o NON APPLICABILE - GIUSTIFICATO.
- **LACUNOSA**: uno o piu' criteri hanno esito LACUNOSO o NON APPLICABILE - NON GIUSTIFICATO.
- **NON CONFORME**: uno o piu' criteri obbligatori hanno esito MANCANTE.

**Lista azioni correttive** (ordinata per priorita'):

Per ogni anomalia rilevata, indicare:
1. Criterio interessato
2. Problema specifico
3. Come correggerlo (cosa aggiungere o specificare)
4. Documento di verifica da produrre o aggiungere in allegato

**Esempio di azione correttiva**:
> "Criterio 2.3.2 (LACUNOSO): la relazione afferma genericamente 'si utilizzera' calcestruzzo con materiale riciclato' ma non indica la percentuale minima di aggregati riciclati richiesta (5% per edifici <4 piani, 25% per calcestruzzo non strutturale in edifici >4 piani - criterio 2.3.2 Allegato DM 256/2022). Azione: specificare la percentuale nella relazione e indicare che sara' verificata tramite la specifica tecnica del calcestruzzo (bolla di consegna con dichiarazione del produttore)."

### Passo 5 - Avvertenze finali

Indicare sempre:
1. La verifica della skill si basa sul testo della relazione fornito: non sostituisce la verifica della documentazione allegata (EPD, certificati, APE).
2. La relazione verificata deve essere firmata dal progettista responsabile.
3. In caso di dubbi interpretativi su un criterio specifico, consultare il testo integrale dell'Allegato al DM 256/2022.

## Output

Un documento strutturato con:
1. Esito complessivo (CONFORME / LACUNOSA / NON CONFORME) con motivazione sintetica
2. Tabella di verifica per criterio (Passo 2)
3. Verifica criteri premianti (se OEPV) (Passo 3)
4. Lista azioni correttive prioritizzate (Passo 4)
5. Avvertenze

## Limiti

- La verifica si limita alla completezza formale e alla coerenza con i requisiti minimi del DM 256/2022; non valuta la correttezza tecnica delle scelte progettuali.
- Non verifica la veridicita' dei dati tecnici dichiarati nella relazione (es. se il calcestruzzo scelto contiene davvero il 5% di riciclato): questa verifica e' a carico della SA in fase di esecuzione, tramite richiesta dei documenti di verifica indicati nella relazione.
- Non e' in grado di verificare i documenti allegati (EPD, certificati) se non sono forniti nel testo.
- Non aggiorna automaticamente i requisiti minimi a fronte di modifiche normative successive alla data di `last_verified`.
