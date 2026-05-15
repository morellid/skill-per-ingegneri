# Task: checklist marcatura CE e dichiarazione UE di conformita'

## Obiettivo

Verificare la completezza degli adempimenti di marcatura CE (art. 15) e degli elementi della dichiarazione UE di conformita' (art. 5 e Allegato VII) per un'attrezzatura a pressione o un insieme.

## Input richiesti

Chiedi all'utente:

- Documentazione fornita: bozza o copia della dichiarazione di conformita' UE, foto della targhetta con la marcatura CE, copia della documentazione tecnica indice, mandato del rappresentante autorizzato se presente.
- Identificativi: nome del fabbricante, indirizzo postale completo, numero di tipo/lotto/serie, riferimento al modulo di valutazione applicato (art. 10 c. 2).
- Norme armonizzate applicate (con riferimento di pubblicazione in GUUE) o, in alternativa, descrizione delle soluzioni adottate per soddisfare i RES dell'Allegato I.
- Se applicabile: identificativo dell'organismo notificato (numero a 4 cifre) che ha condotto la procedura.
- Se altre direttive UE si applicano contemporaneamente (es. direttiva macchine, EMC): elenco.

## Fonti

- `references/estratti/dlgs-26-2016-classificazione-moduli.md` sezione 7 (dichiarazione UE) e sezione 8 (marcatura CE).
- `references/fonti/dlgs-26-2016.md` art. 4-bis (obblighi fabbricante), art. 5 (presunzione conformita' e dichiarazione UE), art. 15 (marcatura CE).

## Procedura

### Checklist marcatura CE (art. 15)

1. **Apposizione fisica** (c. 2): la marcatura CE e' apposta in modo visibile, leggibile e indelebile su ciascuna attrezzatura a pressione o sulla sua targhetta, e su ciascun insieme o sulla sua targhetta, per attrezzature e insiemi che sono completi o in uno stato che consente la verifica finale (Allegato I punto 3.2). Se la natura dell'attrezzatura non consente l'apposizione, la marcatura va sull'imballaggio e sui documenti di accompagnamento.
2. **Insiemi e componenti** (c. 3): non si appone la marcatura CE su ciascuna attrezzatura componente; le attrezzature gia' marcate al momento dell'incorporazione conservano la propria marcatura.
3. **Tempo dell'apposizione** (c. 4): la marcatura va apposta prima dell'immissione sul mercato.
4. **Numero identificativo dell'organismo notificato**: per i moduli con coinvolgimento di organismo notificato (A2, B, C2, D, D1, E, E1, F, G, H, H1), accanto alla marcatura CE va apposto il numero a 4 cifre dell'organismo (cfr. punto 5.1 di ciascun modulo nell'Allegato III). Per il modulo A non si appone alcun numero di organismo notificato.
5. **Principi generali**: la marcatura CE e' soggetta ai principi generali dell'art. 30 del regolamento CE 765/2008 (riferimento incrociato dell'art. 15 c. 1).

### Checklist dichiarazione UE di conformita' (art. 5 e Allegato VII)

1. **Struttura tipo** (art. 5 c. 4): conforme all'Allegato VII del decreto. La struttura tipo include almeno: identificazione del fabbricante (nome e indirizzo) e del rappresentante autorizzato se nominato; oggetto della dichiarazione (numero di tipo/lotto/serie); riferimento al D.Lgs 26/2016 e alla direttiva 2014/68/UE; norme armonizzate applicate con riferimenti di pubblicazione in GUUE (o descrizione delle soluzioni adottate per i RES); riferimento al modulo di valutazione applicato; identificativo dell'organismo notificato (se coinvolto) con riferimento al certificato di esame UE del tipo o equivalente; firma per conto del fabbricante; luogo e data di emissione.
2. **Identificazione univoca dell'attrezzatura** (art. 4-bis c. 5): numero di tipo, di lotto, di serie, o altro elemento che consenta l'identificazione. La dichiarazione UE deve identificare univocamente l'attrezzatura.
3. **Lingua** (art. 5 c. 4 ultimo periodo): per il mercato italiano la dichiarazione UE va redatta in lingua italiana; nei mercati di altri Stati membri, nella lingua o nelle lingue richieste.
4. **Aggiornamento continuo**: la dichiarazione e' "continuamente aggiornata" (art. 5 c. 4).
5. **Dichiarazione unica multi-direttiva** (art. 5 c. 5): se all'attrezzatura si applicano piu' atti UE che prescrivono una dichiarazione UE, va compilata un'unica dichiarazione che cita tutti gli atti applicabili.
6. **Responsabilita'** (art. 5 c. 6): con la dichiarazione UE il fabbricante si assume la responsabilita' della conformita' al decreto.

### Adempimenti conservativi

1. **Documentazione tecnica e dichiarazione UE**: conservate dal fabbricante per **dieci anni** dalla data di immissione sul mercato (art. 4-bis c. 3).
2. **Importatori**: per dieci anni mantengono la dichiarazione UE a disposizione delle autorita' di vigilanza e garantiscono che la documentazione tecnica possa essere resa disponibile su richiesta (art. 4-quater c. 8).
3. **Rappresentante autorizzato** (art. 4-ter c. 2 lett. a): mantenere a disposizione delle autorita' nazionali la dichiarazione UE e la documentazione tecnica per dieci anni, se incluso nel mandato.

### Identificazione e contatti del fabbricante (art. 4-bis c. 6)

1. Sull'attrezzatura o sull'insieme: nome, denominazione commerciale o marchio registrato, indirizzo postale di contatto. In via subordinata: sull'imballaggio o nei documenti di accompagnamento.
2. Indirizzo unico di contatto.
3. Per il mercato italiano: informazioni di contatto in lingua italiana.

### Istruzioni e informazioni di sicurezza (art. 4-bis c. 7)

1. Accompagnano l'attrezzatura/insieme.
2. Conformi all'Allegato I punti 3.3 e 3.4.
3. Lingua: facilmente compresa dai consumatori/utilizzatori; per il mercato italiano in lingua italiana.

## Output

```
Checklist marcatura CE e dichiarazione UE - <descrizione attrezzatura>

Marcatura CE (art. 15):
- [SI/NO/PARZIALE] Apposta in modo visibile, leggibile, indelebile sull'attrezzatura o targhetta
- [SI/NO/N.A.]      Affianco al CE: numero identificativo organismo notificato (richiesto per moduli != A)
- [SI/NO]           Apposta prima dell'immissione sul mercato
- [SI/NO]           Conformita' art. 30 reg. CE 765/2008 (uso del logo CE)

Dichiarazione UE (art. 5, Allegato VII):
- [SI/NO] Identificazione fabbricante e rappresentante autorizzato (se nominato)
- [SI/NO] Oggetto della dichiarazione (numero tipo/lotto/serie)
- [SI/NO] Riferimento a D.Lgs 26/2016 e Dir. 2014/68/UE
- [SI/NO] Elenco norme armonizzate applicate (con riferimenti GUUE) o descrizione soluzioni RES
- [SI/NO] Modulo di valutazione applicato
- [SI/NO] Organismo notificato (numero e riferimento certificato) - se modulo lo prevede
- [SI/NO] Firma per conto del fabbricante, luogo e data
- [SI/NO] Lingua italiana (per mercato italiano)
- [SI/NO] Dichiarazione unica per piu' direttive UE (se applicabili)

Conservazione e tracciabilita':
- [SI/NO] Conservazione documentazione tecnica + dichiarazione UE per 10 anni (art. 4-bis c. 3)
- [SI/NO] Numero di tipo/lotto/serie sull'attrezzatura
- [SI/NO] Nome, marchio e indirizzo di contatto sull'attrezzatura o sull'imballaggio
- [SI/NO] Istruzioni e informazioni di sicurezza in italiano (art. 4-bis c. 7)

Anomalie rilevate:
- <elenco specifico>

Rinvio:
- La dichiarazione UE finale e' firmata dal fabbricante o dal rappresentante autorizzato.
  La skill non firma documenti.
- La validita' del certificato di esame UE del tipo dipende dall'organismo notificato e dalle
  successive modifiche di progetto: il fabbricante deve aggiornare l'organismo notificato.
```

## Limiti

- La skill non interpreta la struttura puntuale dell'Allegato VII (modello tipo di dichiarazione): elenca gli elementi minimi previsti e rinvia al modello per il formato letterale.
- Non verifica la legittimita' della scelta delle norme armonizzate (es. se la norma armonizzata applicata copre effettivamente i RES rilevanti per quel progetto).
- Non valuta l'apposizione fisica della marcatura sull'attrezzatura: la verifica e' visiva, sull'oggetto.
- Per attrezzature soggette ad altre direttive UE (macchine, EMC, ATEX, ecc.) la skill segnala il vincolo dell'art. 5 c. 5 (dichiarazione unica) ma non verifica gli adempimenti delle altre direttive.
