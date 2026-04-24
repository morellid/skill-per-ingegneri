# Note di dominio - caso `costi-boilerplate-non-conforme`

## Cosa stiamo testando

Che la skill rilevi il pattern piu' comune di non-conformita' ai costi sicurezza: la **dichiarazione "a corpo"** senza dettaglio analitico, in violazione diretta del punto 4.1.3 dell'Allegato XV.

## Scelte progettuali del caso

- **Dichiarazione minima**: una riga "EUR 2.500 a corpo" che include tutto. Tipica di POS frettolosi o di POS per piccole ristrutturazioni dove il datore di lavoro "non vuole perder tempo" con dettagli.
- **Nessun prezziario**: omesso il riferimento, in violazione metodologica.
- **Mescolanza DPI ordinari/sicurezza**: altro pattern comune, che gonfia artificialmente o sottoquota i costi sicurezza.
- **Percentuale bassa (1,39%)**: al limite inferiore del range tipico per ristrutturazione. Non automaticamente errato ma, unito all'assenza di dettaglio, probabilmente sottostimato.

## Output atteso

`INADEGUATO - NON CONFORME al 4.1.3` con:
- 0/7 categorie verificabili
- 5 problemi rilevati (3 critici, 1 alto, 1 medio)
- Raccomandazione di riscrittura completa
- Citazione della sanzione art. 159 co. 1 come riferimento di severita'

## Cose che la skill DEVE catturare

- **"A corpo" come violazione**: questa parola (o frase equivalente come "in maniera forfettaria") deve far scattare il flag.
- **Impossibilita' di verifica per categoria**: la skill non puo' inventarsi una ripartizione, deve dichiarare che 7/7 categorie sono non-verificabili.
- **Mescolanza DPI**: "tutti i DPI" senza distinzione segnala il problema del carico-impresa vs carico-committente.
- **Assenza di prezziario**: flag metodologico esplicito.
- **Richiamo alla sanzione**: l'art. 159 co. 1 (ammenda per POS con elementi Allegato XV mancanti) e' il riferimento normativo di severita'. La skill lo richiama senza quantificare applicazione (spetta a ispettore).

## Cose che la skill NON dovrebbe fare

- **Falso negativo per percentuale**: non classificare il POS come "almeno la percentuale e' in range" - il problema e' metodologico, la percentuale non basta.
- **Tentare di ricostruire ripartizione**: la skill non deve inventare come si ripartirebbero i EUR 2.500 tra le 7 categorie. E' compito del datore di lavoro riscrivere.
- **Essere troppo severa sul valore assoluto**: EUR 2.500 per ristrutturazione 6 mesi potrebbe teoricamente bastare (dipende dai dettagli). Il problema centrale e' il METODO.

## Ambiguita' da gestire

- **Se il POS rinvia al PSC**: in questo caso il POS non rinvia al PSC, dichiara direttamente. Se avesse rinviato ("costi sicurezza come da PSC, EUR X"), la verifica si sposterebbe sul PSC (non disponibile qui). La skill deve distinguere i due casi.

## Complicazione reale

- **Cantieri piccoli**: molti POS di piccola impresa dichiarano "a corpo" perche' "tanto sono poche cose". E' pratica comune ma **non conforme**. La skill deve tenerli a standard uniforme, indipendentemente dalla scala.
- **PSC assente**: se il cantiere e' sotto soglia PSC (es. impresa unica, durata breve, non pericolosa per Allegato XI), il POS non ha PSC di riferimento e deve includere la stima in autonomia. Questo cantiere (cambio destinazione d'uso, 6 mesi, 180k) e' al limite - potrebbe o meno rientrare nei casi PSC.

## Cosa imparare

- La non-conformita' piu' diffusa sui costi e' metodologica, non quantitativa.
- Una dichiarazione "a corpo" e' riconoscibile come pattern e deve essere segnalata sistematicamente.
- La skill puo' aggiungere valore automatizzando un controllo che spesso viene sottovalutato.

## Fonte della struttura

Fittizio. Pattern comune nei POS delle piccole imprese per ristrutturazioni. Nessun riferimento reale.
