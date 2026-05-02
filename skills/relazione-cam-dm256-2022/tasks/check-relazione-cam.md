# Task: Verifica relazione CAM esistente

Data una Relazione Tecnica dei Requisiti Ambientali CAM gia' redatta, verifica la completezza e la conformita' ai requisiti del DM 23/06/2022 n. 256 e segnala lacune, sezioni mancanti o affermazioni insufficientemente supportate.

## Obiettivo

Restituire all'utente:

- **Esito complessivo**: CONFORME / LACUNOSA / NON CONFORME (con spiegazione)
- **Tabella di verifica per criterio**: per ogni criterio applicabile alla tipologia di intervento, esito (OK / LACUNOSO / MANCANTE) con spiegazione delle anomalie
- **Lista delle azioni correttive richieste**: descrizione dettagliata di cosa aggiungere, modificare o documentare
- **Criteri mancanti**: criteri del DM 256/2022 non trattati nella relazione, con indicazione se obbligatori

## Input richiesti

1. **Tipologia di intervento dichiarata nella relazione** (NC/R1/R2/MS): se non indicata nella relazione, chiederla all'utente.

2. **Testo della relazione da verificare**: l'utente fornisce il testo completo (incollato nella chat o come file allegato).

3. **Eventuali documenti allegati citati nella relazione** (se disponibili): EPD, certificati FSC/PEFC, APE di progetto, piano rifiuti C&D, relazione acustica, etc. La verifica della relazione e' possibile anche senza questi documenti, ma l'esito sara' parziale.

4. **Tipo di gara** (prezzo piu' basso / OEPV): per verificare se i criteri premianti devono essere presenti.

5. **Tipo di affidamento** (progettazione, lavori, o congiunto): per verificare quale sezione di criteri premianti e' rilevante in caso OEPV.

## Fonti normative

Leggere prima di procedere:

- `references/estratti/dm-256-2022-articoli-chiave.md` - definizioni e obblighi
- `references/estratti/dm-256-2022-allegato-criteri-2x.md` - requisiti minimi criteri obbligatori 2.3-2.6
- `references/estratti/dm-256-2022-allegato-criteri-premianti.md` - criteri premianti (se OEPV)
- `references/estratti/dlgs-36-2023-art57.md` - base normativa dell'obbligo

## Procedura

### Passo 1 - Analisi strutturale della relazione

Verificare se la relazione:
- E' intestata correttamente con indicazione esplicita del DM 23/06/2022 n. 256 come riferimento normativo.
- Indica la tipologia di intervento (NC/R1/R2/MS).
- Ha sezioni o paragrafi dedicati ai criteri CAM delle sezioni 2.3, 2.4, 2.5 e 2.6 dell'Allegato.
- Contiene dichiarazioni di conformita' o non applicabilita' per ciascun criterio.
- Richiama la data di entrata in vigore corretta del DM 256/2022 (4 dicembre 2022).

Se la relazione non menziona il DM 256/2022 come riferimento normativo, segnalare immediatamente:
> "ATTENZIONE: la relazione non cita esplicitamente il DM 23/06/2022 n. 256 come riferimento normativo CAM applicabile. Questo e' un vizio formale che la stazione appaltante potrebbe rilevare. Verificare se la relazione faceva riferimento al precedente DM 11/10/2017 (non piu' applicabile per gare bandite dopo il 4 dicembre 2022)."

Se la relazione usa la vecchia struttura del DM 11/2017 (criteri diversi o numerazione diversa), segnalare che i criteri applicabili sono quelli del DM 256/2022 e che la struttura dell'Allegato e' organizzata per sezioni 2.3/2.4/2.5/2.6 (non per argomenti ambientali come nel precedente DM).

### Passo 2 - Verifica criterio per criterio

Per ogni criterio obbligatorio dell'Allegato DM 256/2022 applicabile alla tipologia di intervento classificata, analizzare la relazione e produrre un esito:

**OK**: la sezione e' presente, il requisito minimo e' citato, la scelta progettuale e' descritta e la documentazione di verifica e' indicata.

**LACUNOSO**: la sezione e' presente ma mancano dati tecnici specifici (es. la relazione afferma "si utilizzera' calcestruzzo con aggregati riciclati" ma non indica la percentuale minima), oppure la documentazione di verifica non e' specificata.

**MANCANTE**: il criterio non e' trattato nella relazione (e dovrebbe esserlo dato il tipo di intervento e i materiali/sistemi previsti).

**NON APPLICABILE - GIUSTIFICATO**: il criterio e' dichiarato non applicabile con motivazione accettabile (es. "il progetto non prevede l'utilizzo di calcestruzzo" per il criterio 2.5.2).

**NON APPLICABILE - NON GIUSTIFICATO**: il criterio e' dichiarato non applicabile senza motivazione o con motivazione insufficiente.

Tabella di output (adattare alle sezioni rilevanti per il tipo di intervento):

| # | Criterio | Esito | Note / Azioni correttive |
|---|---|---|---|
| **2.3 - Territoriali-urbanistici** (solo NC e ristrutturazione urbanistica) | | | |
| 2.3.2 | Permeabilita' superfici (deflusso <0,50) | [esito] | [dettaglio] |
| 2.3.3 | Isola di calore (SRI >=29; verde >=60%) | [esito] | [dettaglio] |
| 2.3.9 | Risparmio idrico (rubinetti <=6 l/min; WC <=6/3 l) | [esito] | [dettaglio] |
| *altri 2.3.x pertinenti* | ... | ... | ... |
| **2.4 - Specifiche tecniche per gli edifici** | | | |
| 2.4.2 | Prestazione energetica NZEB + comfort termico estivo | [esito] | [dettaglio] |
| 2.4.3 | Illuminazione LED 50.000 ore; gestione automatica | [esito] | [dettaglio] |
| 2.4.5 | Aerazione VMC con recupero calore; classe II UNI EN 16798-1 | [esito] | [dettaglio] |
| 2.4.9 | Tenuta all'aria n50 (NC: <2; R1: <3,5) | [esito] | [dettaglio] |
| 2.4.11 | Comfort acustico classe II UNI 11367 | [esito] | [dettaglio] |
| 2.4.12 | Radon <=200 Bq/m³ | [esito] | [dettaglio] |
| 2.4.13 | Piano di manutenzione con BIM | [esito] | [dettaglio] |
| 2.4.14 | Disassemblaggio fine vita >=70% | [esito] | [dettaglio] |
| *altri 2.4.x pertinenti* | ... | ... | ... |
| **2.5 - Prodotti da costruzione** (per ogni categoria usata) | | | |
| 2.5.1 | Emissioni indoor COV <=1.500 µg/m³; formaldeide <60 µg/m³ | [esito] | [dettaglio] |
| 2.5.2 | Calcestruzzo >=5% riciclato/recuperato/sottoprodotti | [esito] | [dettaglio] |
| 2.5.4 | Acciaio strutturale FEN >=75%; legato >=60%; CI >=12% | [esito] | [dettaglio] |
| 2.5.6 | Prodotti legnosi FSC/PEFC o >=70% riciclato | [esito] | [dettaglio] |
| 2.5.7 | Isolanti (contenuto min. per tipo; no SVHC >0,1%) | [esito] | [dettaglio] |
| *altri 2.5.x pertinenti* | ... | ... | ... |
| **2.6 - Cantiere** | | | |
| 2.6.1 | Misure ambientali cantiere; macchine Fase III A/IV/V | [esito] | [dettaglio] |
| 2.6.2 | Demolizione selettiva >=70% recupero (se demolizioni) | [esito] | [dettaglio] |

### Passo 3 - Verifica criteri premianti (solo se OEPV)

Se la gara e' OEPV, verificare:
- La relazione indica quali criteri premianti vengono adottati (dalla sezione 2.7, 3.2 o 4.3 a seconda del tipo di affidamento)?
- Per ogni criterio premiante dichiarato: la prestazione e' superiore al minimo di base? I dati tecnici sono sufficientemente precisi?
- L'assenza di criteri premianti non e' un problema (sono facoltativi), ma segnalarlo come opportunita'.

Esempi di voci da verificare per criteri premianti:
- Se dichiara 3.2.8 (emissioni indoor premianti): verificare che i limiti dichiarati siano quelli del criterio premiante (COV <=1.000 µg/m³) e non quelli base (<=1.500).
- Se dichiara 4.3.3 (prestazione energetica migliorativa): verificare che sia indicata la percentuale di riduzione rispetto al limite (NC: -10% vs classe A4).

### Passo 4 - Esito complessivo e lista azioni correttive

**Esito complessivo**:
- **CONFORME**: tutti i criteri applicabili hanno esito OK o NON APPLICABILE - GIUSTIFICATO.
- **LACUNOSA**: uno o piu' criteri hanno esito LACUNOSO o NON APPLICABILE - NON GIUSTIFICATO.
- **NON CONFORME**: uno o piu' criteri obbligatori applicabili hanno esito MANCANTE.

**Lista azioni correttive** (ordinata per priorita'):

Per ogni anomalia rilevata, indicare:
1. Criterio interessato (numero e titolo)
2. Problema specifico
3. Come correggerlo (cosa aggiungere o specificare)
4. Documento di verifica da produrre o aggiungere in allegato

**Esempio di azione correttiva**:
> "Criterio 2.5.2 - Calcestruzzi (LACUNOSO): la relazione afferma genericamente 'si utilizzera' calcestruzzo con materiale riciclato' ma non indica la percentuale minima di materia riciclata/recuperata/sottoprodotti richiesta (>=5% sul peso del prodotto - criterio 2.5.2 Allegato DM 23/06/2022 n. 256). Azione: specificare '>=5% in peso' nella relazione e indicare che sara' verificato tramite EPD di Tipo III o dichiarazione del produttore con certificazione del contenuto di riciclato (es. ReMade in Italy(R), UNI/PdR 88)."

### Passo 5 - Avvertenze finali

Indicare sempre:
1. La verifica della skill si basa sul testo della relazione fornito: non sostituisce la verifica della documentazione allegata (EPD, certificati, APE).
2. La relazione verificata deve essere firmata dal progettista responsabile.
3. In caso di dubbi interpretativi su un criterio specifico, consultare il testo integrale dell'Allegato al DM 23/06/2022 n. 256 (estratto in `references/estratti/dm-256-2022-allegato-criteri-2x.md`).

## Output

Un documento strutturato con:
1. Esito complessivo (CONFORME / LACUNOSA / NON CONFORME) con motivazione sintetica
2. Tabella di verifica per criterio (Passo 2)
3. Verifica criteri premianti (se OEPV) (Passo 3)
4. Lista azioni correttive prioritizzate (Passo 4)
5. Avvertenze

## Limiti

- La verifica si limita alla completezza formale e alla coerenza con i requisiti minimi del DM 256/2022; non valuta la correttezza tecnica delle scelte progettuali.
- Non verifica la veridicita' dei dati tecnici dichiarati nella relazione: questa verifica e' a carico della SA in fase di esecuzione, tramite richiesta dei documenti di verifica indicati nella relazione.
- Non e' in grado di verificare i documenti allegati (EPD, certificati) se non sono forniti nel testo.
- Non aggiorna automaticamente i requisiti minimi a fronte di modifiche normative successive alla data di `last_verified` in `sources.yaml`.
