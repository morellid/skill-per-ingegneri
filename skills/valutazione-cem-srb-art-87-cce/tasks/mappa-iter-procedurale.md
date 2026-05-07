# Task - Mappa iter procedurale art. 87 CCE

## Obiettivo

Restituire al professionista una mappa puntuale dell'iter autorizzativo art. 87 D.Lgs. 259/2003: attori, atti, tempistiche, soglie, casi speciali. L'output e' un riferimento operativo, non un calendario vincolante (le tempistiche concrete dipendono dall'Ente locale e da eventuali sospensioni per integrazioni).

## Input richiesti

1. **Regime presunto**: Modello A (ordinario), Modello B (SCIA, impianti <= 20 W per singola antenna), o GSM-R ferroviario.
2. **Comune** dell'installazione (alcuni Enti locali prevedono termini piu' brevi - art. 87 c. 9 ultimo periodo).
3. **Eventuali Amministrazioni** potenzialmente dissenzienti note (es. Soprintendenza, ASL, Provincia).
4. **Data prevista** di presentazione dell'istanza (per costruire la timeline).

## Fonti

- `references/estratti/dlgs-259-2003-art-87.md` (commi 1, 2, 4, 5, 6, 7, 8, 9, 10).
- `references/estratti/dpcm-8-7-2003-limiti-cem.md` (riferimento per il parere ARPA art. 14 L. 36/2001 ex art. 87 c. 1).

## Procedura

### Mappa attori

| Attore | Ruolo | Riferimento |
|--------|-------|-------------|
| Soggetto richiedente (operatore abilitato) | Presenta istanza/SCIA | art. 87 c. 2 |
| Ente locale (Comune via SUAP) | Riceve, istruisce, autorizza/diniega | art. 87 c. 1, 2 |
| Responsabile del procedimento | Indicato all'atto della presentazione, gestisce richiesta integrazioni | art. 87 c. 2, 5 |
| ARPA/APPA territorialmente competente | Pronuncia tecnica CEM ex art. 14 L. 36/2001, entro 30 giorni dalla comunicazione | art. 87 c. 1, 4 |
| Conferenza di servizi (se dissenso) | Pronuncia entro 30 giorni dalla prima convocazione, sostituisce gli atti delle singole amministrazioni | art. 87 c. 6, 7 |
| Consiglio dei Ministri | Solo in caso di dissenso qualificato (ambiente, salute, patrimonio storico-artistico) | art. 87 c. 8 |
| Ministero (MIMIT) | Informato di convocazione ed esito conferenza | art. 87 c. 7 |

### Mappa atti

1. **Istanza ordinaria - Modello A Allegato 13** (art. 87 c. 3): per impianti con potenza singola antenna > 20 W e per le tipologie non rientranti nel SCIA.
2. **SCIA - Modello B Allegato 13** (art. 87 c. 3 ultimo periodo): impianti UMTS o altre tecnologie con potenza singola antenna <= 20 W. Conforme ai modelli predisposti dall'Ente locale; in mancanza, Modello B Allegato 13.
3. **Trasmissione contestuale ad ARPA** (art. 87 c. 4): copia dell'istanza/denuncia inoltrata in contestualita'.
4. **Pubblicizzazione** da parte dello sportello locale, senza diffondere i dati caratteristici dell'impianto (art. 87 c. 4).
5. **Richiesta integrazioni** (eventuale, una sola volta, entro 15 giorni - art. 87 c. 5).
6. **Conferenza di servizi** (se motivato dissenso da Amministrazione interessata - art. 87 c. 6).
7. **Provvedimento autorizzatorio espresso** dell'Ente locale, oppure **silenzio-assenso** ex art. 87 c. 9 dopo 90 giorni dalla presentazione del progetto e della relativa domanda (salvo c. 8).
8. **Realizzazione opere** entro 12 mesi dal provvedimento o dalla formazione del silenzio-assenso, a pena di decadenza (art. 87 c. 10).

### Mappa tempistiche (regime ordinario)

```
T0  : presentazione istanza al SUAP + trasmissione contestuale ad ARPA   (art. 87 c. 2, c. 4)
T0+15: termine per UNA eventuale richiesta di integrazione               (art. 87 c. 5)
T0+30: termine pronuncia ARPA dalla comunicazione                        (art. 87 c. 4)
T0+30: termine convocazione conferenza di servizi se dissenso            (art. 87 c. 6)
T0+30 (dalla 1a convocazione): pronuncia conferenza                      (art. 87 c. 7)
T0+90: silenzio-assenso, salvo dissenso qualificato c. 8                 (art. 87 c. 9)
T0+90+12 mesi: decadenza opere se non realizzate                         (art. 87 c. 10)
```

Nota: il termine del silenzio-assenso (90 gg) **si sospende** in caso di richiesta di integrazione e riprende a decorrere dal completamento dell'integrazione documentale (art. 87 c. 5 ultimo periodo).

### Mappa tempistiche (regime SCIA)

Per impianti UMTS o altri con singola antenna <= 20 W (art. 87 c. 3 ultimo periodo): si applica il regime SCIA, conforme ai modelli predisposti dall'Ente locale o, in mancanza, al Modello B Allegato 13. La SCIA produce i propri effetti secondo la disciplina generale del SUAP/SCIA (L. 241/1990 art. 19), con avvio attivita' contestuale alla presentazione, fermo restando il parere ARPA art. 14 L. 36/2001 e il rispetto dei limiti DPCM 8/7/2003. Il termine massimo di 90 giorni del c. 9 si applica letteralmente "alle istanze di autorizzazione e alle denunce di attivita'" (art. 87 c. 9).

> Nota di trasparenza. La fonte MIMIT catalogata in `sources.yaml` riflette il testo dell'art. 87 fino al 2013-2014. Modifiche successive (in particolare D.L. 76/2020 conv. L. 120/2020 e D.Lgs. 8 novembre 2021 n. 207) hanno introdotto ulteriori semplificazioni e puntualizzazioni sull'iter SCIA. Il professionista DEVE verificare il testo vigente su Normattiva prima di ogni deposito.

### Eventi che modificano la timeline

- **Richiesta di integrazione** (art. 87 c. 5): sospende il termine ex c. 9; riparte dal completamento.
- **Dissenso motivato di Amministrazione interessata** (art. 87 c. 6): innesca la conferenza di servizi.
- **Dissenso qualificato da Amministrazione preposta a tutela ambiente/salute/patrimonio storico-artistico** (art. 87 c. 8): rimessione al Consiglio dei Ministri; il silenzio-assenso del c. 9 NON si forma in questo caso.
- **Termini piu' brevi previsti dall'Ente locale** (art. 87 c. 9 ultimo periodo): l'Ente puo' prevedere termini piu' brevi per la conclusione del procedimento o ulteriori semplificazioni.

## Output

1. **Diagramma testuale** della timeline con date concrete (calcolate da T0 fornito dall'utente).
2. **Tabella attori-atti-termini** con riferimenti al comma applicabile.
3. **Elenco eventi a rischio** specifici alla pratica (es. presenza di vincolo paesaggistico -> probabile coinvolgimento Soprintendenza -> possibile dissenso ex c. 6, eventualmente qualificato ex c. 8).
4. **Promemoria 12 mesi**: data limite ex art. 87 c. 10 per la realizzazione delle opere a pena di decadenza.
5. **Disclaimer**: "L'iter concreto puo' essere modificato da regolamenti comunali, dalla disciplina SCIA del SUAP locale, e da modifiche normative successive al 2013-2014 non riflesse nella fonte MIMIT catalogata. Verificare il testo vigente dell'art. 87 CCE su Normattiva."

## Limiti

- Non sostituisce il calendario operativo del SUAP locale.
- Non gestisce regimi speciali GSM-R (art. 87 c. 3-bis): fuori scope.
- Non valuta il merito di un eventuale dissenso (motivato vs. qualificato): rinvia al responsabile del procedimento e al firmatario.
- Non riflette automaticamente le modifiche post-2014 dell'art. 87.
