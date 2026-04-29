# Circolare MISE 18 dicembre 2014 - coefficienti di conversione in tep

> Estratto sintetico dei coefficienti di conversione in tep (tonnellate equivalenti di petrolio) richiamati dall'art. 9 del DM Transizione 5.0 e dal cap. 2 della Circolare MIMIT 25877/2024 (Tab. 11) per il calcolo dei risparmi energetici.
>
> **Fonte ufficiale**: MISE - Circolare 18 dicembre 2014 (disposizioni integrative per il meccanismo dei Titoli di Efficienza Energetica), in attuazione dell'art. 19 L. 10/1991.
> **Data consultazione**: 2026-04-29.
> **Licenza**: documento amministrativo italiano, riproducibile.
>
> Riferimento sources.yaml: `circolare-mise-18-12-2014-tep`.
>
> ATTENZIONE: i coefficienti possono essere aggiornati. Verificare la versione vigente del documento al momento del calcolo. La skill rinvia a questi coefficienti come **riferimento normativo**, ma il certificatore deve applicare i fattori vigenti.

## Inquadramento

Per il calcolo dei risparmi energetici ai fini del Piano Transizione 5.0, l'art. 9 co. 6 del DM 24/7/2024 dispone:

> "Si utilizzano i coefficienti di conversione in tep applicati per la comunicazione di cui all'articolo 19 della Legge 10 del 1991 (circolare MiSE del 18/12/2014)."

E' questa la circolare che fissa il riferimento metrologico per la conversione in tep di tutti i vettori energetici utilizzati dalla struttura produttiva o dal processo interessato.

## Definizione e finalita'

La **tep** (tonnellata equivalente di petrolio) e' l'unita' di misura comune per esprimere i consumi energetici di vettori diversi (energia elettrica, combustibili fossili, calore, vapore, etc.) ed e' tradizionalmente utilizzata nei meccanismi di incentivazione dell'efficienza energetica (Titoli di Efficienza Energetica, certificati bianchi, diagnosi energetiche art. 8 D.Lgs. 102/2014).

**Equivalenza convenzionale**: 1 tep = 41,868 GJ = 11,628 MWh circa (riferito al potere calorifico inferiore del petrolio standard).

## Fattori di conversione piu' utilizzati (estratto sintetico)

| Vettore energetico | Unita' di misura naturale | Fattore di conversione (tep/unita') |
|---|---|---|
| **Energia elettrica** (lato consumi finali) | MWh | 0,187 |
| **Gas naturale** | 1000 Sm3 | 0,82 |
| **Gasolio** (per riscaldamento e altri usi) | t | 1,08 |
| **Olio combustibile** (BTZ/ATZ) | t | 0,98 |
| **GPL** (gas di petrolio liquefatti) | t | 1,10 |
| **Carbone** (mediamente) | t | 0,68 |
| **Legna** (essiccata, ~12% umidita') | t | 0,25 |
| **Cippato di legno** (umidita' ~30-40%) | t | 0,18-0,25 |
| **Pellet** | t | 0,40-0,42 |
| **Biogas** | 1000 Sm3 | 0,40-0,55 (variabile col contenuto di metano) |
| **Calore** (acquistato da rete di teleriscaldamento) | MWh termici | 0,086 |

> **Nota**: i valori riportati sono **sintetici** e riferiti alla circolare MISE 2014. Per applicazioni di asseverazione il certificatore deve **consultare il testo integrale e gli allegati della circolare vigente** e adattare i fattori al specifico vettore energetico utilizzato nella struttura produttiva (es. olio diatermico, calore di processo a vapore, idrogeno verde, biocarburanti certificati).

## Procedura di applicazione

1. Identificare **tutti i vettori energetici** in ingresso e in uscita dalla struttura produttiva o dal processo interessato (energia elettrica, gas naturale, GPL, gasolio, calore, vapore, etc.).
2. Per ciascun vettore, **misurare o stimare** il consumo annuale in **unita' naturale** (kWh, Sm3, t, MWh termici).
3. Applicare il **fattore di conversione** della circolare MISE 2014 vigente per ottenere il consumo in tep.
4. **Sommare** i contributi dei singoli vettori per ottenere il consumo totale in tep della struttura produttiva o del processo interessato.
5. Ripetere per la situazione **ex ante** (consumi misurati o stimati pre-investimento) e per la situazione **ex post** (consumi conseguibili o effettivamente conseguiti).
6. Calcolare la **riduzione percentuale**:

   `Riduzione % = (Consumo_tep_ex_ante - Consumo_tep_ex_post) / Consumo_tep_ex_ante * 100`

7. Verificare il rispetto della **soglia minima**: 3% per la struttura produttiva, 5% per il processo interessato.

## Casi particolari

### Energia elettrica autoprodotta da FER

Quando la struttura produttiva e' dotata di un impianto di autoproduzione FER per autoconsumo, **anche l'energia autoconsumata** prodotta in sito da fonti rinnovabili rientra nel computo dei consumi energetici della struttura produttiva (cap. 2 circolare MIMIT 25877/2024, in fine).

### Combustibili biogenici

Per biogas, biomasse vegetali e biocarburanti certificati, il fattore di conversione dipende dal **potere calorifico inferiore (PCI)** specifico. La circolare MISE 2014 fornisce range; per un'asseverazione robusta il certificatore dovra' indicare la **fonte specifica** del PCI utilizzato (analisi di laboratorio, scheda tecnica fornitore, banca dati ENEA).

### Vapore di processo

Per il vapore acquistato o autoprodotto, calcolare l'energia termica in MWh equivalenti sulla base di pressione, temperatura, portata e applicare il fattore di conversione del calore.

## Limiti di questo estratto

- I valori sopra riportati sono indicativi e finalizzati a orientare l'utente. **Non sostituiscono il testo integrale della circolare MISE 18/12/2014**.
- Per il calcolo asseverato, il certificatore deve **verificare l'aggiornamento** dei coefficienti (eventuali revisioni successive del MISE/MIMIT) e applicare i valori vigenti alla data di calcolo.
- La conversione in tep e' **uno strumento metrologico**: non sostituisce la verifica di coerenza fra consumi pre/post intervento (normalizzazione, indicatori di prestazione, scenario controfattuale dove applicabile).
