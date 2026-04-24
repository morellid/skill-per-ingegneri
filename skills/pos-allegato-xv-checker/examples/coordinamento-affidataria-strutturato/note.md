# Note di dominio - caso `coordinamento-affidataria-strutturato`

## Cosa stiamo testando

Che la skill riconosca come **conforme** un POS di impresa affidataria ben strutturato sul coordinamento, con documentazione completa di PSC/CSE, altre imprese, riunioni, interferenze, e conformita' art. 96/97.

## Scelte progettuali del caso

- **POS affidataria**: rileva per art. 97, che ha obblighi aggiuntivi rispetto alla semplice esecutrice.
- **5 imprese totali**: complessita' tipica di cantiere medio pubblico. Test per la capacita' della skill di tracciare molteplici imprese.
- **Subappaltatori dichiarati in fase preliminare** (POS "da trasmettere"): prassi accettabile. Test che la skill non classifichi come "mancante" una dichiarazione "da trasmettere".
- **Interferenze multiple con misure specifiche**: 4 interferenze interne + 1 esterna (scuola). Test matching tipologia interferenza / tipo di misura.
- **Interferenza con committente terzo** (scuola in funzione): caso tipico di cantieri pubblici. Test sensibilita' a rischi relazionali/terzi.
- **Conformita' art. 96 tabulata**: impresa "fa il compito bene" documentando tutte le 7 lettere. Test che la skill riconosca la struttura pulita.
- **Art. 97 tutti e 4 i commi documentati**: verifica congruenza POS esecutrici con processo descritto. Test che la skill distingua "dichiarazione di intenti" da "processo strutturato".

## Output atteso

`CONFORME` con 2 problemi di priorita' bassa (raccomandazioni su frequenza riunioni nelle fasi di picco, monitoraggio effettiva ricezione POS subappaltatrici).

## Cose che la skill DOVREBBE fare

- Riconoscere la tabella delle imprese con fase di intervento come buona pratica.
- Accettare "POS da trasmettere" per imprese non ancora in cantiere come stato legittimo.
- Valorizzare la tabella art. 96 per lettera come struttura di controllo efficace.
- Riconoscere il processo a 4 controlli per verifica congruenza POS esecutrici come contenuto sostanziale (non boilerplate).
- Suggerire incremento frequenza riunioni nelle fasi di massima sovrapposizione.

## Cose che la skill NON dovrebbe fare

- **Falso positivo** per "POS subappaltatrici da trasmettere": e' normale a inizio cantiere che non tutti siano gia' disponibili.
- **Pretendere** di verificare contenuti del PSC (non fornito).
- **Dichiarare mancante** l'attuazione pratica del coordinamento: questo e' compito del CSE in cantiere, non del POS.

## Complicazioni da gestire

- **Interferenza con scuola funzionante**: non e' una classica interferenza tra imprese, e' con terzi esterni. La skill deve categorizzarla come gestione di rischio con terzi (coordinamento committente + misure tecniche specifiche come recinzione fonoassorbente).
- **Sfasamento dettagliato in Allegato A**: la skill non ha accesso all'Allegato, deve accettare il rinvio come prassi (e segnalare come limite della verifica).

## Cosa imparare

- Un POS affidataria di qualita' ha: identificazione esplicita PSC/CSE, tabella imprese con fasi, 4 tipi di riunioni, tabella art. 96 per lettera, processo art. 97 in 4 controlli.
- La skill puo' valorizzare la struttura tabellare e la documentazione di processo (non solo di intenti).
- Il valore aggiunto sta nel segnalare le fasi in cui la frequenza di coordinamento e' insufficiente rispetto alla complessita' (mesi 9-11 in questo caso).

## Fonte della struttura

Fittizio. Struttura ispirata a POS affidataria di media-alta qualita' per cantieri pubblici. Nessun riferimento reale.
