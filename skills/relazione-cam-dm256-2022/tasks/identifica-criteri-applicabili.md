# Task: Identifica criteri CAM applicabili

Data la tipologia di intervento, determina quali criteri del DM 23/06/2022 n. 256 si applicano e produce un prospetto di applicabilita' con indicazione dei documenti di verifica richiesti.

## Obiettivo

Restituire all'utente:

- **Tipologia di intervento classificata** secondo le definizioni del DM 256/2022 (NC / R1 / R2 / MS) con motivazione.
- **Tabella dei criteri CAM di base applicabili** (Criterio 2) con indicazione, per ciascuno: numero criterio, descrizione sintetica, requisito minimo, documenti di verifica, applicabilita' SI/NO/CONDIZIONATA.
- **Elenco dei criteri premianti potenzialmente applicabili** (Criterio 4) se la gara e' OEPV.
- **Avvertenze specifiche** per il caso in esame.

## Input richiesti

Raccogliere dall'utente (chiedere se non forniti):

1. **Tipologia di intervento**: descrivere brevemente l'intervento (es. "costruzione nuova scuola", "ristrutturazione uffici comunali con sostituzione infissi e impianti", "manutenzione straordinaria facciata con nuovo cappotto").

2. **Superfici interessate**:
   - Superficie utile complessiva dell'edificio (mq)
   - Superficie disperdente totale (mq), se ristrutturazione
   - Superficie disperdente oggetto di intervento (mq), se ristrutturazione

3. **Destinazione d'uso dell'edificio**: uffici, scuola, ospedale, biblioteca, palestra pubblica, altro.

4. **Importo lavori stimato** (EUR): necessario per il criterio 2.9 (soglia comunitaria).

5. **Presenza di aree esterne a verde**: si/no, superficie indicativa (mq).

6. **Tipo di gara**: prezzo piu' basso o OEPV? (determina se i criteri premianti sono rilevanti).

Se l'utente non conosce la distinzione R1/R2, aiutarlo: chiedere la percentuale di superficie disperdente oggetto di intervento rispetto al totale.

## Fonti normative

Leggere prima di procedere:

- `references/estratti/dm-256-2022-articoli-chiave.md` - definizioni art. 2 (NC/R1/R2/MS)
- `references/estratti/dm-256-2022-allegato-criteri-2x.md` - tabella di applicabilita' criteri 2.1-2.9
- `references/estratti/dlgs-36-2023-art57.md` - obbligo di applicazione

## Procedura

### Passo 1 - Classificazione dell'intervento

Sulla base degli input raccolti, classificare l'intervento in una delle quattro tipologie del DM 256/2022 (art. 2):

- **NC**: nuovo edificio su area non edificata o su sedime di edificio demolito integralmente.
- **R1**: ristrutturazione con superficie disperdente interessata >50% della totale.
- **R2**: ristrutturazione con superficie disperdente interessata <=50% oppure intervento su singoli elementi tecnici (es. solo infissi, solo copertura).
- **MS**: intervento di manutenzione che non altera la forma esterna, non aumenta superficie utile, non incrementa parametri urbanistici.

Riassumere la classificazione:
> "Il tuo intervento e' classificabile come **[NC/R1/R2/MS]** ai sensi dell'art. 2 DM 256/2022 perche': [motivazione]. Confermi?"

Se l'utente non e' sicuro o ha dubbi interpretativi, segnala che la classificazione e' responsabilita' del progettista e, in caso di incertezza, si applica il criterio piu' restrittivo.

### Passo 2 - Tabella criteri di base applicabili

Produrre una tabella strutturata come quella seguente. Per ogni criterio, indicare:
- Se si applica al tipo di intervento classificato
- Il requisito minimo in sintesi
- I documenti di verifica principali

**Esempio di output** (adattare al caso specifico):

| # | Criterio | Applicabile? | Requisito minimo (sintesi) | Documenti di verifica |
|---|---|---|---|---|
| 2.1 | Qualita' del suolo | SI (NC) | Assenza contaminazione; preferenza riqualificazione aree degradate | Cert. bonifica o dichiaraz. assenza contam. |
| 2.2 | Durabilita' e adattabilita' | SI (NC) | Vita utile >=50 anni struttura, >=25 anni involucro/impianti | Relaz. tecnica con vita utile dichiarata |
| 2.3 | Materiali (per categorie usate) | SI | Contenuto minimo riciclato per categoria (vedi sotto) | EPD/DAP o dichiaraz. produttore |
| 2.3.2 | Calcestruzzi strutturali | SI | >=5% aggregati riciclati (NC <4 piani) | Specifica tecnica calcestruzzo; bolla consegna |
| 2.3.4 | Legno | SI (se usato) | Cert. FSC o PEFC o legno recuperato; formaldeide <=E1 | Certificato FSC/PEFC; scheda tecnica |
| 2.3.6 | Elementi metallici | SI (se usati) | Acciaio >=75% riciclato; alluminio >=30% | Cert. produttore o EPD |
| 2.4 | Risparmio idrico | SI | Rubinetti <=6 l/min; WC doppio pulsante; raccolta meteorica se verde >=200 mq | Scheda tecnica sanitari; schema impianto |
| 2.5 | Efficienza energetica | SI | Classe A3 o superiore (NC); rispetto D.Lgs.192/2005 | APE di progetto; relaz. tecnica impianti |
| 2.6 | Aree verdi | SI (se verde >=500 mq) | >=50% specie autoctone; compost; irrigazione a goccia; >=30% sup. permeabile | Planimetria verde; elenco specie; schema irriguo |
| 2.7 | Rifiuti C&D | SI | Piano gestione rifiuti; >=70% recupero rifiuti non pericolosi | Piano rifiuti C&D |
| 2.8 | Cantiere sostenibile | SI | Misure antipolvere/rumore; Stage IIIA macchine; raccolta differenziata | Piano cantiere con misure ambientali |
| 2.9 | ISO 14001 esecutore | SI se importo >=5.538.000 EUR | Cert. ISO 14001 o EMAS dell'appaltatore | Cert. ISO 14001/EMAS |

Per il criterio 2.3, espandere la tabella con tutti i sottocriteri pertinenti ai materiali che saranno effettivamente usati nel progetto. Se il progetto non usa una determinata categoria di materiale, indicare "NON APPLICABILE (materiale non previsto nel progetto)".

### Passo 3 - Criteri premianti (solo se gara OEPV)

Se la gara e' OEPV, elencare i criteri premianti potenzialmente applicabili con indicazione del punteggio tecnico associabile (determinato dalla SA nella griglia di gara):

- **4.1** Maggior contenuto di riciclato: sempre applicabile
- **4.2** EPD verificata: sempre applicabile
- **4.3** nZEB avanzato (A4): applicabile se NC o R1
- **4.4** Adattamento climatico: applicabile se NC o R1
- **4.5** Certificazione edificio (LEED/BREEAM/ITACA): applicabile se NC o R1
- **4.6** Monitoraggio BMS: applicabile se NC, R1 o R2 con impianti

### Passo 4 - Avvertenze e prossimi passi

Indicare:
1. Criteri la cui applicabilita' dipende da dati progettuali non ancora disponibili (es. lista esatta materiali, importo definitivo lavori).
2. Criteri che richiedono verifiche preliminari specifiche (es. analisi sito per 2.1; calcolo energetico per 2.5).
3. Raccomandazione di passare al task `draft-relazione-cam.md` per redigere la relazione.

## Output

Un documento strutturato in 3 sezioni:
1. **Classificazione intervento**: tipo (NC/R1/R2/MS) + motivazione
2. **Tabella criteri di base applicabili**: come al Passo 2
3. **Criteri premianti** (se OEPV): lista con applicabilita'
4. **Avvertenze e prossimi passi**

## Limiti

- La classificazione NC/R1/R2/MS e' effettuata sulla base degli input forniti dall'utente; la responsabilita' della classificazione finale e' del progettista.
- La tabella di applicabilita' e' basata sul DM 256/2022 vigente alla data di `last_verified` in `sources.yaml`; verificare aggiornamenti ministeriali prima di applicare su una gara reale.
- I requisiti tecnici specifici per ciascun criterio (es. percentuali minime di riciclato) sono indicati in forma sintetica; per il testo ufficiale riferirsi all'Allegato DM 256/2022.
