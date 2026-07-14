# Task: Diagnosi degli adempimenti DPR 462/2001 per un impianto

## Obiettivo

Dato un impianto in un luogo di lavoro, determinare: se rientra nel DPR 462/2001,
la periodicita' della verifica periodica, i soggetti che la eseguono e gli
adempimenti collegati (messa in esercizio, denuncia, comunicazioni INAIL).

## Input richiesti

- **tipo di impianto**: impianto di messa a terra / dispositivo di protezione
  contro le scariche atmosferiche / impianto elettrico in luogo con pericolo di
  esplosione;
- **ambiente/luogo** in cui e' installato: ordinario / cantiere / locale ad uso
  medico / ambiente a maggior rischio in caso di incendio / luogo con pericolo di
  esplosione;
- se e' un impianto **nuovo** (messa in esercizio) o **esistente** (verifiche
  periodiche gia' in corso);
- eventuale data dell'ultima verifica / della messa in esercizio (per
  contestualizzare, senza calcolare date al posto dell'utente).

## Fonti da leggere

- `references/estratti/verifiche-messa-a-terra-checklist.md` sezioni 1-6
- se serve conferma: `references/fonti/dpr-462-2001.md` (artt. 1, 2, 4, 5, 6, 7-bis)

## Procedura

### Passo 1 - Rientra nel DPR 462/2001?
Verifica che sia uno dei tre impianti dell'art. 1 **in un luogo di lavoro**.
Se non e' in un luogo di lavoro (es. civile abitazione non datoriale), il DPR
462/2001 non si applica: segnalalo.

### Passo 2 - Periodicita' della verifica periodica (regola di decisione)

| Condizione | Periodicita' | Rif. |
|---|---|---|
| Messa a terra / scariche atmosferiche in ambiente ordinario | **5 anni** | art. 4 c. 1 |
| Cantiere | **2 anni** | art. 4 c. 1 |
| Locale ad uso medico | **2 anni** | art. 4 c. 1 |
| Ambiente a maggior rischio in caso di incendio | **2 anni** | art. 4 c. 1 |
| Luogo con pericolo di esplosione | **2 anni** | art. 6 c. 1 |

Applica: parti da 5 anni; se ricorre una delle condizioni "a 2 anni",
la periodicita' e' biennale. Cita l'articolo.

### Passo 3 - Chi esegue la verifica (art. 4 c. 2 / art. 6 c. 2)
**ASL/ARPA** competenti **oppure organismi abilitati** individuati dal Ministero
(oggi Ministero delle imprese e del made in Italy), criteri UNI CEI. Il
verificatore rilascia un **verbale** da conservare ed esibire.

### Passo 4 - Se impianto nuovo: messa in esercizio e denuncia
- messa a terra / scariche atmosferiche (art. 2): dichiarazione di conformita'
  dell'installatore (= omologazione); **entro 30 giorni** invio a **INAIL e
  ASL/ARPA** (o SUAP); **prima verifica a campione** INAIL (art. 3);
- luoghi con pericolo di esplosione (art. 5): dichiarazione di conformita';
  entro 30 giorni ad **ASL/ARPA**; **omologazione = prima verifica** ASL/ARPA.

### Passo 5 - Comunicazione INAIL (art. 7-bis)
Il datore di lavoro **comunica all'INAIL, per via informatica, il nominativo
dell'organismo** incaricato delle verifiche periodiche; l'organismo versa
all'INAIL il 5% della tariffa.

### Passo 6 - Onerosita'
Tutte le verifiche sono a carico del datore di lavoro.

## Output atteso

- conferma dell'applicabilita' del DPR 462/2001 (o esclusione motivata);
- **periodicita'** con la citazione dell'articolo e la condizione che la
  determina;
- **soggetti** che eseguono la verifica e obbligo di verbale;
- **adempimenti di messa in esercizio/denuncia** se impianto nuovo;
- **comunicazione INAIL** del nominativo dell'organismo (art. 7-bis);
- nota "ISPESL = INAIL";
- avvertenza: la skill non calcola le date concrete delle scadenze e non
  sostituisce installatore, organismo verificatore e datore di lavoro.
