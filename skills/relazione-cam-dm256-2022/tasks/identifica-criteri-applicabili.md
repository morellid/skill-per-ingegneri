# Task: Identifica criteri CAM applicabili

Data la tipologia di intervento, determina quali criteri del DM 23/06/2022 n. 256 si applicano e produce un prospetto di applicabilita' con indicazione dei documenti di verifica richiesti.

## Obiettivo

Restituire all'utente:

- **Tipologia di intervento classificata** secondo le definizioni del DM 256/2022 (art. 2) con motivazione.
- **Prospetto dei criteri CAM obbligatori applicabili**: per ogni sezione (2.3, 2.4, 2.5, 2.6), indicare quali criteri si applicano e quelli non applicabili con motivazione.
- **Elenco dei criteri premianti potenzialmente applicabili** (sezione 2.7 per progettazione, 3.2 per lavori, 4.3 per congiunto) se la gara e' OEPV.
- **Avvertenze specifiche** per il caso in esame.

## Input richiesti

Raccogliere dall'utente (chiedere se non forniti):

1. **Tipologia di intervento**: descrivere brevemente l'intervento (es. "costruzione nuova scuola", "ristrutturazione uffici comunali con sostituzione infissi e impianti", "manutenzione straordinaria facciata con nuovo cappotto").

2. **Superfici interessate**:
   - Superficie utile complessiva dell'edificio (mq)
   - Superficie disperdente totale (mq), se ristrutturazione
   - Superficie disperdente oggetto di intervento (mq), se ristrutturazione

3. **Destinazione d'uso dell'edificio**: uffici, scuola, ospedale, biblioteca, palestra pubblica, altro.

4. **Presenza di aree esterne a verde**: si/no, superficie indicativa (mq).

5. **Tipo di gara**: prezzo piu' basso o OEPV? (determina se i criteri premianti sono rilevanti).

6. **Tipo di affidamento**: solo progettazione, solo lavori, oppure congiunto progettazione e lavori? (determina quale sezione di criteri premianti si applica).

Se l'utente non conosce la distinzione R1/R2, aiutarlo: chiedere la percentuale di superficie disperdente oggetto di intervento rispetto al totale.

## Fonti normative

Leggere prima di procedere:

- `references/estratti/dm-256-2022-articoli-chiave.md` - definizioni art. 2 (NC/R1/R2/MS)
- `references/estratti/dm-256-2022-allegato-criteri-2x.md` - criteri obbligatori (sezioni 2.3-2.6) con tabella di applicabilita'
- `references/estratti/dm-256-2022-allegato-criteri-premianti.md` - criteri premianti (2.7, 3.2, 4.3)
- `references/estratti/dlgs-36-2023-art57.md` - obbligo di applicazione

## Procedura

### Passo 1 - Classificazione dell'intervento

Sulla base degli input raccolti, classificare l'intervento in una delle quattro tipologie del DM 256/2022 (art. 2):

- **NC**: nuovo edificio su area non edificata o su sedime di edificio demolito integralmente.
- **R1**: ristrutturazione con superficie disperdente interessata >50% della totale.
- **R2**: ristrutturazione con superficie disperdente interessata <=50% oppure intervento su singoli elementi tecnici (es. solo infissi, solo copertura).
- **MS**: intervento di manutenzione che non altera la forma esterna, non aumenta superficie utile, non incrementa parametri urbanistici.
- **Intervento non riguardante l'intero edificio** (es. sostituzione infissi, rifacimento cappotto su edificio esistente): caso speciale - si applicano SOLO i criteri 2.5 (prodotti da costruzione) e 2.6 (cantiere).

Riassumere la classificazione:
> "Il tuo intervento e' classificabile come **[tipo]** ai sensi dell'art. 2 DM 256/2022 perche': [motivazione]. Confermi?"

Se l'utente non e' sicuro o ha dubbi interpretativi, segnala che la classificazione e' responsabilita' del progettista e, in caso di incertezza, si applica il criterio piu' restrittivo.

### Passo 2 - Prospetto criteri obbligatori applicabili

La struttura corretta dei criteri obbligatori nell'Allegato DM 256/2022 e' la seguente:

**Sezione 2.3 - Specifiche tecniche territoriali-urbanistiche** (solo NC e ristrutturazione urbanistica):
- 2.3.1 Inserimento naturalistico e paesaggistico
- 2.3.2 Permeabilita' della superficie territoriale (deflusso <0,50)
- 2.3.3 Riduzione isola di calore (SRI >=29, verde >=60% sup. permeabile)
- 2.3.4 Riduzione impatto sul sistema idrografico
- 2.3.5 Infrastrutturazione primaria (raccolta meteorica, irrigazione verde, rifiuti, illuminazione, sottoservizi)
- 2.3.6 Infrastrutturazione secondaria e mobilita' sostenibile
- 2.3.7 Approvvigionamento energetico da FER
- 2.3.8 Rapporto sullo stato dell'ambiente (non per interventi in VIA)
- 2.3.9 Risparmio idrico (rubinetteria <=6 l/min; WC doppio scarico <=6/3 l)

**Sezione 2.4 - Specifiche tecniche progettuali per gli edifici** (NC e R1 per la maggior parte; R2 e MS per elementi coinvolti):
- 2.4.1 Diagnosi energetica (R1 e R2 con superficie >=1.000 mq)
- 2.4.2 Prestazione energetica NZEB + comfort termico estivo (NC e R1)
- 2.4.3 Impianti illuminazione interni (LED 50.000 ore; gestione automatica)
- 2.4.4 Ispezionabilita' e manutenzione impianti
- 2.4.5 Aerazione, ventilazione e qualita' aria (NC e R1: classe II UNI EN 16798-1; VMC con recupero calore)
- 2.4.6 Benessere termico (classe B UNI EN ISO 7730)
- 2.4.7 Illuminazione naturale (300 lux al 50% punti; NC e ristrutturazione urbanistica)
- 2.4.8 Dispositivi di ombreggiamento (NC e ristrutturazione urbanistica; gtot <=0,35)
- 2.4.9 Tenuta all'aria (NC: n50 <2; R1: n50 <3,5)
- 2.4.10 Inquinamento elettromagnetico
- 2.4.11 Prestazioni e comfort acustici (classe II UNI 11367)
- 2.4.12 Radon (<=200 Bq/m³)
- 2.4.13 Piano di manutenzione con archiviazione BIM
- 2.4.14 Disassemblaggio e fine vita (>=70% componenti disassemblabili)

**Sezione 2.5 - Specifiche tecniche per i prodotti da costruzione** (tutti i tipi di intervento, incluso non-intero-edificio):
- 2.5.1 Emissioni indoor (COV totali <=1.500 µg/m³; formaldeide <60 µg/m³; etc.)
- 2.5.2 Calcestruzzi (>=5% riciclato/recuperato/sottoprodotti)
- 2.5.3 Prodotti prefabbricati in calcestruzzo (>=5%; CAC >=7,5%)
- 2.5.4 Acciaio strutturale (FEN non legato >=75%; legato >=60%; ciclo integrale >=12%)
- 2.5.5 Laterizi (>=15% muratura e solai; >=7,5% coperture e facciavista)
- 2.5.6 Prodotti legnosi (FSC o PEFC; oppure >=70% riciclato)
- 2.5.7 Isolanti (per categoria: cellulosa 80%, lana vetro 60%, lana roccia 15%, EPS 15%, XPS 10%, PUR rigido 2%; no SVHC >0,1%)
- 2.5.8 Tramezzature/contropareti/controsoffitti a secco (>=10%; gesso >=5%)
- 2.5.9 Murature in pietrame e miste (solo materiale riutilizzato o di recupero)
- 2.5.10 Pavimenti (dure: Ecolabel UE; resilienti plastici >=20%; gomma >=10%)
- 2.5.11 Serramenti e oscuranti in PVC (>=20% riciclato)
- 2.5.12 Tubazioni in PVC e polipropilene (>=20% riciclato)
- 2.5.13 Pitture e vernici (Ecolabel UE; o assenza metalli pesanti; o assenza pericolo acquatico H400/H410/H411)

**Sezione 2.6 - Specifiche tecniche progettuali relative al cantiere** (tutti i tipi di intervento):
- 2.6.1 Prestazioni ambientali del cantiere (misure antipolvere, antirumore, risparmio idrico, protezione suolo, macchine Fase III A min da gennaio 2022; Fase IV da gennaio 2024; Fase V da gennaio 2026)
- 2.6.2 Demolizione selettiva, recupero e riciclo (>=70% in peso rifiuti non pericolosi; se presenti demolizioni)
- 2.6.3 Conservazione strato superficiale del terreno (se ci sono movimenti di terra)
- 2.6.4 Rinterri e riempimenti (materiale di scavo riutilizzato; riempimenti >=70% riciclato per miscele betonabili; >=30% per miscele legate)

Produrre per il caso specifico una tabella con le sezioni/criteri applicabili, non applicabili (con motivazione), e da verificare in funzione dei materiali definitivi.

**Esempio di output per NC uffici PA**:

| Sezione | Criteri | Applicabile? | Note |
|---|---|---|---|
| 2.3 | 2.3.1-2.3.9 | SI (NC) | Tutti i criteri territoriali-urbanistici si applicano |
| 2.4 | 2.4.1 | NO | Diagnosi energetica: solo R1/R2 >=1.000 mq |
| 2.4 | 2.4.2 | SI | Obbligatorio NZEB per NC |
| 2.4 | 2.4.3-2.4.14 | SI | Applicabili nella quasi totalita' |
| 2.5 | Per categorie usate | SI | Verificare elenco materiali definitivo |
| 2.6 | 2.6.1 | SI | Sempre obbligatorio |
| 2.6 | 2.6.2 | SI se demolizioni | Specificare se previste demolizioni |
| 2.6 | 2.6.3 | SI se movimenti di terra | Da verificare |
| 2.6 | 2.6.4 | Condizionata | Solo se ci sono rinterri o riempimenti |

Per la sezione 2.5 (prodotti), espandere la tabella con ogni categoria di materiale che sara' effettivamente usato nel progetto. Se un materiale non e' previsto, indicare "NON APPLICABILE - materiale non previsto nel progetto".

### Passo 3 - Criteri premianti (solo se gara OEPV)

Se la gara e' OEPV, elencare i criteri premianti potenzialmente applicabili in funzione del tipo di affidamento:

**Per affidamento del servizio di progettazione (sezione 2.7)**:
- 2.7.1 Competenza tecnica dei progettisti (esperto ambientale certificato ISO/IEC 17024)
- 2.7.2 LCA e LCC del progetto (studio ambientale ed economico del ciclo di vita)
- 2.7.3 Progettazione in BIM con dati ambientali CAM
- 2.7.4 Valutazione ESG del progettista

**Per affidamento dei lavori (sezione 3.2)**:
- 3.2.1 ISO 14001 o EMAS dell'impresa esecutrice
- 3.2.2 Valutazione ESG dell'impresa
- 3.2.3 Prestazioni migliorative dei prodotti da costruzione
- 3.2.4 LCA/LCC varianti migliorative (solo se il progetto base ha LCA/LCC)
- 3.2.5 Distanza di trasporto <=150 km (almeno 60% dei prodotti)
- 3.2.6 Capacita' tecnica dei posatori (professionisti certificati UNI)
- 3.2.7 Lubrificanti biodegradabili/rigenerati
- 3.2.8 Emissioni indoor ridotte (COV <=1.000 µg/m³ vs 1.500 base)
- 3.2.9 Materiali prodotti in impianti EU/ETS (acciaio, cemento, ceramica, vetro)
- 3.2.10 Etichettature ambientali (Ecolabel UE o Made Green in Italy classe A)

**Per affidamento congiunto (sezione 4.3)** - in aggiunta a 2.7 e 3.2:
- 4.3.1 LCA e LCC del progetto migliorativo (non insieme a 4.3.3)
- 4.3.2 Valutazione ESG
- 4.3.3 Prestazione energetica migliorativa (NC: -10% vs limite classe A4; R2 involucro: -30% EPH,nd)
- 4.3.4 Materiali rinnovabili >=20% (escluse strutture portanti)
- 4.3.5 Selezione gres porcellanato con tool LCC del MITE
- 4.3.6 BACS classe A (UNI EN 15232-1) per automazione edificio
- 4.3.7 Piano M&V risparmi energetici (IPMVP, UNI ISO 50015 o UNI CEN EN 17267)
- 4.3.8 Fine vita impianti (piano disassemblaggio per NC >500 m³ e R1)

### Passo 4 - Avvertenze e prossimi passi

Indicare:
1. Criteri la cui applicabilita' dipende da dati progettuali non ancora disponibili (es. lista esatta materiali per la sezione 2.5).
2. Criteri che richiedono verifiche preliminari specifiche (es. calcolo energetico per 2.4.2; diagnosi energetica per 2.4.1; analisi radon per 2.4.12 in zone a rischio).
3. Raccomandazione di passare al task `draft-relazione-cam.md` per redigere la relazione.

## Output

Un documento strutturato in 4 sezioni:
1. **Classificazione intervento**: tipo (NC/R1/R2/MS) + motivazione
2. **Prospetto criteri obbligatori**: suddiviso per sezione 2.3/2.4/2.5/2.6
3. **Criteri premianti** (se OEPV): per tipo di affidamento
4. **Avvertenze e prossimi passi**

## Limiti

- La classificazione NC/R1/R2/MS e' effettuata sulla base degli input forniti dall'utente; la responsabilita' della classificazione finale e' del progettista.
- Il prospetto di applicabilita' e' basato sul DM 256/2022 vigente alla data di `last_verified` in `sources.yaml`; verificare aggiornamenti ministeriali prima di applicare su una gara reale.
- I requisiti tecnici specifici per ciascun criterio sono indicati in forma sintetica; per il testo ufficiale riferirsi all'Allegato DM 256/2022 (estratto in `references/estratti/dm-256-2022-allegato-criteri-2x.md`).
