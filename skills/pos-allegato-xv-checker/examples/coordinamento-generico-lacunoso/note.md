# Note di dominio - caso `coordinamento-generico-lacunoso`

## Cosa stiamo testando

Che la skill rilevi il pattern **"delega al CSE + accettazione generica del PSC"**, che e' la forma piu' comune di lacuna nei POS reali. Molti POS dichiarano conformita' agli art. 96 e 97 con formule vuote, senza processo documentato.

## Scelte progettuali del caso

- **Stesso cantiere** del caso `coordinamento-affidataria-strutturato` (scuola primaria, 14 mesi, EUR 1.2M, 5 imprese): per confronto diretto tra POS adeguato e POS inadeguato sullo stesso scenario.
- **Formule di delega**: "gestite dal CSE", "come previsto dal CSE", "rispetta tutti gli obblighi". Pattern classico.
- **Art. 97 dichiarato ma non documentato**: l'impresa si dichiara affidataria e afferma di verificare, ma non descrive come.
- **Assenze notabili**: co. 3-bis (trasferimento oneri) completamente omesso, co. 3-ter (formazione DdL) omesso.

## Output atteso

`NON CONFORME - lacune sistematiche` con:
- 8 problemi rilevati (1 critico su interferenze, 5 alti, 2 medi)
- Raccomandazione di **riscrittura integrale** della parte coordinamento
- Richiesta formale al CSE di **non approvare** l'inizio lavori

## Cose che la skill DEVE catturare

- **"L'impresa accetta il PSC"** senza identificarlo e' insufficiente.
- **"Le interferenze verranno gestite dal CSE"** e' delega che contraddice il concetto di POS come piano operativo DELL'IMPRESA.
- **"L'impresa rispetta tutti gli obblighi art. 96"** e' una dichiarazione vuota, non un'attuazione documentata.
- **Art. 97 co. 3 lett. b) con promessa ma non processo**: verifica congruenza POS esecutrici dichiarata ma senza metodo.
- **Co. 3-bis completamente assente**: trasferimento oneri sicurezza senza ribasso non menzionato.

## Cose che la skill NON dovrebbe fare

- **Accettare la dichiarazione di compliance** come compliance effettiva.
- **Essere troppo severa sull'assenza di dettagli operativi** che sono nel PSC (dove sono legittimi), ma deve pretendere il contributo specifico dell'impresa.
- **Confondere una lacuna documentale** con assenza totale del processo: non possiamo sapere se il processo esiste e il POS lo documenta male, o se il processo non esiste.

## Perche' l'interferenza e' "critica" e non solo "alta"

Le interferenze sono il **cuore del coordinamento**. La delega al CSE ("gestite dal CSE secondo PSC") significa che l'impresa abdica al suo ruolo. Il POS non e' un foglio d'accettazione del PSC, e' il contributo operativo dell'impresa alla sicurezza. Se l'impresa delega, il POS perde ragione d'essere.

## Cosa imparare

- La differenza tra POS strutturato e POS lacunoso sul coordinamento si vede in minuti di lettura: il primo ha tabelle, nomi, processi; il secondo ha verbi generici e formule di delega.
- La skill puo' aggiungere valore sistematizzando questo controllo.
- Per il CSE, ricevere questo output sul POS in fase pre-approvazione e' utile per argomentare la richiesta di revisione.

## Fonte della struttura

Fittizio. Modello di "POS copia-incolla non curato" ma realistico. Nessun riferimento reale.
