# Output atteso: Alpina Controls BC-10 - inquadramento art. 14 CRA

Le sei convinzioni del fabbricante sono, nell'ordine: da verificare ma fondata su un
ragionamento sbagliato, errata, errata, errata, errata, errata. Di seguito il dettaglio.

## 0. Premessa: l'art. 14 si applica anche a un fabbricante non stabilito nell'Unione

Alpina Controls sviluppa il BC-10 e lo commercializza con il proprio marchio: e'
fabbricante ai sensi dell'art. 3, punto 13. Il BC-10 e' un PDE ai sensi dell'art. 3,
punto 1, messo a disposizione sul mercato dell'Unione. L'art. 14, par. 7, terzo comma,
disciplina espressamente il fabbricante **senza stabilimento principale nell'Unione**:
l'assenza di uno stabilimento nell'Unione non esclude l'obbligo, ne determina solo il
destinatario.

## 1. Evento A - PoC pubblico su un componente open source

### Il ragionamento del fabbricante e' sbagliato, la conclusione va verificata

L'art. 3, punto 42, richiede "prove attendibili che un soggetto malintenzionato l'ha
sfruttata **in un sistema** senza l'autorizzazione del proprietario del sistema". Due
conseguenze che il fabbricante confonde:

- **Un CVSS 9.8 e un proof-of-concept pubblico non sono prove di sfruttamento.** Provano
  che la vulnerabilita' e' grave e sfruttabile, non che qualcuno l'abbia sfruttata. Su
  questo il ragionamento del fabbricante ("c'e' l'exploit, quindi e' attivamente
  sfruttata") e' errato.
- **La definizione non richiede pero' che lo sfruttamento sia avvenuto sul prodotto del
  fabbricante.** Il testo dice "in un sistema", e l'art. 14, par. 1, chiede che la
  vulnerabilita' attivamente sfruttata sia **contenuta nel** PDE. L'assenza di evidenze
  sui dispositivi BC-10 quindi **non chiude la questione**.

**Il punto decisivo e' l'inserimento nel catalogo del 1 ottobre.** Va verificato che cosa
il catalogo effettivamente attesti: se afferma, sulla base di evidenze, che la
vulnerabilita' e' stata sfruttata da un attore in sistemi reali, siamo davanti a un
possibile "prove attendibili" e l'obbligo dell'art. 14, par. 1, scatta - perche' la
vulnerabilita' e' contenuta nel BC-10. Se il catalogo si limita a censire vulnerabilita'
"probabilmente sfruttabili" o "di interesse", il presupposto non e' dimostrato.

**Questa verifica e' l'azione piu' urgente, e va fatta in ore, non in settimane**, perche'
da essa dipende se un termine di 24 ore sia gia' decorso.

### Momento iniziale: input mancante

L'input non dice **quando Alpina Controls ha appreso** dell'inserimento nel catalogo. E'
il dato da cui dipende tutto. Va accertato e documentato.

Se la conoscenza risale a giovedi' **1 ottobre 2026** e la verifica sul catalogo conferma
lo sfruttamento:

| Adempimento | Scadenza |
|---|---|
| Preallarme (par. 2, lett. a) | 2 ottobre 2026, stessa ora |
| Notifica della vulnerabilita' (par. 2, lett. b) | 4 ottobre 2026, stessa ora (domenica) |
| Relazione finale (par. 2, lett. c) | 14 giorni dalla messa a disposizione della misura correttiva - il termine **non e' ancora iniziato**, il firmware non e' rilasciato |

La scadenza delle 72 ore cade di domenica. Il testo indica ore e giorni senza qualificarli
come lavorativi e non prevede proroghe: la questione va posta al consulente, non risolta
assumendo lo slittamento al lunedi'.

### "Notifichiamo appena avremo la patch, fra due settimane" - errato

E' l'errore piu' grave del caso. Le tre scadenze del par. 2 sono indipendenti dalla
disponibilita' del rimedio: solo la **relazione finale** e' agganciata alla messa a
disposizione della misura correttiva. Preallarme e notifica delle 72 ore vanno trasmessi
anche senza patch, indicando le misure di attenuazione adottabili dagli utilizzatori.

Il contenuto minimo del preallarme e', "se del caso", i soli Stati membri di messa a
disposizione: non c'e' nulla da attendere per trasmetterlo.

### Se il presupposto non risulta dimostrato

L'output **non** conclude per l'assenza dell'obbligo. Dichiara quale elemento manca
(prove attendibili di sfruttamento effettivo), quale accertamento lo risolverebbe
(contenuto e base probatoria della voce di catalogo), e ricorda che:

- l'art. 15, par. 1, consente comunque la **segnalazione volontaria** di qualsiasi
  vulnerabilita', non solo di quelle attivamente sfruttate;
- l'art. 17, par. 4, esclude che la sola notifica comporti maggiore responsabilita';
- l'obbligo di **informare gli utilizzatori** dell'art. 14, par. 8, presuppone la
  conoscenza di una vulnerabilita' attivamente sfruttata o di un incidente grave: se il
  presupposto non ricorre, il par. 8 non si applica. Resta comunque opportuno informare i
  clienti di una vulnerabilita' CVSS 9.8 presente nel prodotto e delle misure di
  attenuazione, e diventa dovuto per l'evento B (vedi sezione 2);
- l'art. 13, par. 6, impone di segnalare la vulnerabilita' a chi mantiene il componente e
  di correggerla: qui la vulnerabilita' e' gia' pubblica e la patch upstream esiste, quindi
  l'adempimento sostanziale e' l'integrazione. Nota che l'art. 13 **non** e' fra le
  disposizioni anticipate dall'art. 71, par. 2.

## 2. Evento B - Ransomware sul server di build

### "E' l'infrastruttura aziendale, non il prodotto" - errato

L'art. 14, par. 3, riguarda "qualsiasi incidente grave che abbia un **impatto sulla
sicurezza del prodotto** con elementi digitali". Il criterio e' l'impatto sul prodotto,
non la collocazione fisica del sistema colpito. Un incidente sulla pipeline di build e
sulla **chiave privata di firma degli aggiornamenti** e' esattamente il caso in cui
l'infrastruttura tocca la sicurezza del prodotto.

**E' un incidente?** Si': art. 6, punto 6, dir. (UE) 2022/2555 (richiamato dall'art. 3,
punto 43, CRA) - la cifratura ha compromesso disponibilita' e integrita', e
l'esfiltrazione non escludibile riguarda la riservatezza. Non e' un quasi incidente: si e'
verificato.

**E' grave?** Art. 14, par. 5, lett. b): l'incidente "ha portato **o e' in grado di
portare**" all'introduzione o all'esecuzione di codice maligno nel PDE o nei sistemi
dell'utilizzatore. Una chiave di firma potenzialmente esfiltrata consente di far accettare
al parco installato un aggiornamento malevolo come legittimo: il presupposto del
potenziale e' integrato. Ricorre plausibilmente anche la lett. a). **Basta una delle due.**

Che nessun dispositivo in campo risulti malfunzionante e' irrilevante: entrambe le lettere
del par. 5 includono espressamente il potenziale.

### Timeline

Momento iniziale: **venerdi' 2 ottobre 2026, ore 16:40**, comunicazione del fornitore IT
al titolare.

| Adempimento | Termine | Scadenza |
|---|---|---|
| Preallarme (par. 4, lett. a) | 24 ore | **sabato 3 ottobre 2026, 16:40** |
| Notifica dell'incidente (par. 4, lett. b) | 72 ore | **lunedi' 5 ottobre 2026, 16:40** |
| Relazione finale (par. 4, lett. c) | un mese dalla **trasmissione** della notifica b) | dipende dalla data effettiva di invio |

Il preallarme scade di sabato. Il fabbricante non ha PSIRT ne' reperibilita': e' un
problema organizzativo, non una causa di proroga.

Contenuto del preallarme: **come minimo** se si sospetta che l'incidente sia il risultato
di atti illegittimi o malevoli - qui si'. Se del caso, gli Stati membri di messa a
disposizione (Italia, Germania, Irlanda e ogni altro Stato in cui il BC-10 risulta messo a
disposizione, per quanto noto al fabbricante).

Va inoltre valutato senza ritardo l'obbligo del par. 8 verso gli utilizzatori: se la
chiave di firma e' compromessa, le misure adottabili dagli utilizzatori (sospendere gli
aggiornamenti automatici fino a nuova comunicazione) sono precisamente cio' che il par. 8
impone di comunicare.

## 3. Destinatario: **Irlanda**, non Italia

Il fabbricante non ha stabilimento principale nell'Unione, quindi si applica la **cascata
dell'art. 14, par. 7, terzo comma**, nell'ordine:

| Ordine | Criterio | Caso Alpina |
|---|---|---|
| a) | Stato membro del rappresentante autorizzato che agisce per il maggior numero di PDE | **Irlanda** - applicabile |
| b) | Stato membro dell'importatore | Germania - non si scende qui |
| c) | Stato membro del distributore | Italia - non si scende qui |
| d) | Stato membro con il maggior numero di utilizzatori | Italia - non si scende qui |

La convinzione n. 4 e' errata: il fatto che il 70% degli utilizzatori sia in Italia
corrisponde alla lettera **d)**, l'ultima della cascata, che non si raggiunge perche' la
lettera a) e' applicabile. Il CSIRT competente e' quello **designato coordinatore
dall'Irlanda** ai sensi dell'art. 12, par. 1, della dir. (UE) 2022/2555.

**Questa skill non nomina il CSIRT coordinatore irlandese**: la designazione e' nell'atto
irlandese di recepimento della NIS2, che non e' fra le fonti lette. Va verificata
sull'elenco dei CSIRT coordinatori (Rete di CSIRT nazionali / ENISA) prima della scadenza
delle 24 ore.

Nota collaterale: la regola del quarto comma, che consente di mantenere lo stesso CSIRT
per le notifiche successive, vale **solo** per il caso della lett. d) e qui non si applica.

L'ENISA e' destinataria **simultanea** in entrambi i casi (art. 14, par. 1 e 3).

**Avvertenza sul canale**: l'art. 16 non e' fra le disposizioni anticipate all'11 settembre
2026 dall'art. 71, par. 2, e nessuna fonte letta descrive i terminali nazionali. Lo stato
operativo va verificato su ENISA e sull'autorita' irlandese.

## 4. "Siamo una microimpresa, l'art. 64, par. 10, ci esonera" - errato

Tre errori sovrapposti.

1. **La deroga non riguarda l'obbligo, ma un solo termine.** Il par. 10, lett. a), esclude
   le sanzioni "per quanto riguarda il **mancato rispetto del termine** di cui
   all'articolo 14, paragrafo 2, lettera a), o all'articolo 14, paragrafo 4, lettera a)":
   cioe' le sole **24 ore del preallarme**. Le notifiche delle 72 ore, le relazioni finali
   e l'obbligo di notificare in se' restano pienamente esigibili.
2. **La deroga ha una portata testuale che non copre l'ipotesi.** Il par. 10 esclude le
   sanzioni "di cui a tali paragrafi", cioe' quelle dei **paragrafi da 3 a 9**, mentre la
   violazione degli obblighi dell'art. 14 e' sanzionata dal **paragrafo 2**, che non
   compare in quell'elenco. Il testo non spiega come le due disposizioni si coordinino.
   Questa skill riporta la formulazione letterale e **non** conclude che le micro e piccole
   imprese siano al riparo dal massimale del par. 2: la questione va posta al consulente
   legale.
3. **La qualifica di microimpresa non e' assunta, si verifica.** L'art. 3, punto 19,
   rinvia alle definizioni dell'allegato alla raccomandazione 2003/361/CE, che **non e'
   fra le fonti lette da questa skill**. Il conteggio dei dipendenti e del fatturato secondo
   quella raccomandazione, incluse le regole su imprese associate e collegate, va fatto
   sul testo della raccomandazione.

Va aggiunto che l'art. 64 **non** e' fra le disposizioni anticipate dall'art. 71, par. 2, e
ricade quindi nella data generale dell'11 dicembre 2027. Questo e' cio' che dice il testo.
**Non** significa che l'inadempimento sia privo di conseguenze: l'art. 14 e' comunque
vincolante dall'11 settembre 2026. Quali conseguenze si producano prima dell'11 dicembre
2027 il testo non lo dice e le fonti lette non lo chiariscono: e' una domanda per il
consulente legale, non una ragione per rinviare.

Elemento a favore del fabbricante, invece reale: l'art. 17, par. 6, impegna i CSIRT
coordinatori a prestare **assistenza tecnica** sugli obblighi dell'art. 14, in particolare
ai fabbricanti che si qualificano come microimprese o piccole o medie imprese.

## 5. "Meglio non notificare, ci espone" - errato

L'art. 17, par. 4: "La sola notifica in conformita' dell'articolo 14, paragrafi 1 e 3, o
dell'articolo 15, paragrafi 1 e 2, non sottopone la persona fisica o giuridica notificante
a una maggiore responsabilita'". Per la segnalazione volontaria, l'art. 15, par. 5,
aggiunge che essa non impone alcun obbligo aggiuntivo. Non notificare, al contrario, e' la
condotta che espone.

## 6. "Abbiamo gia' notificato all'autorita' nazionale, copre anche il CRA" - errato

Nessuna delle fonti lette prevede che un adempimento assorba l'altro. Due precisazioni:

- il regime NIS2 (in Italia, D.Lgs. 138/2024) ha presupposti, termini e destinatari
  propri; il regime dell'art. 14 CRA riguarda i **fabbricanti di PDE**. Di quel decreto
  questa skill ha letto i soli artt. 2, 15 e 16 - quelli che designano il CSIRT
  coordinatore - e non le disposizioni che ne definiscono l'ambito soggettivo: se e in
  che misura Alpina Controls vi ricada e' domanda per il consulente;
- Alpina Controls e' una societa' svizzera: una notifica alla propria autorita' nazionale
  non e' in alcun modo il canale previsto dall'art. 14, par. 7, che indica il terminale del
  CSIRT coordinatore di uno **Stato membro**.

## 7. Lacune organizzative che rendono l'adempimento impraticabile

Sono obblighi dell'art. 13 e dell'allegato I, parte II, **non anticipati** dall'art. 71,
par. 2 (decorrenza 11 dicembre 2027), ma sono i prerequisiti pratici senza i quali un
termine di 24 ore non e' rispettabile. Vanno segnalati come tali, non come inadempimenti
attuali.

| Voce | Stato | Base | Impatto sull'art. 14 |
|---|---|---|---|
| Registro delle vulnerabilita' con data e ora di ricezione | assente | art. 13, par. 7 | Il momento iniziale dell'evento A non e' documentabile: e' la lacuna piu' grave |
| Punto di contatto unico presidiato | parziale (`info@`, orario d'ufficio) | art. 13, par. 17 | Una segnalazione del venerdi' sera puo' consumare l'intero termine |
| Indirizzo di contatto per le vulnerabilita' | assente | allegato I, parte II, punto 6 | Un ricercatore esterno non ha canale |
| Politica di divulgazione coordinata | assente | art. 13, par. 8; allegato I, parte II, punto 5 | Nessuna procedura di gestione |
| SBOM | assente | allegato I, parte II, punto 1 | Stabilire in ore quali prodotti usano la libreria e' impraticabile |
| CSIRT coordinatore individuato in anticipo | assente | art. 14, par. 7 | Si scopre a termine gia' decorrente |
| Catena decisionale e reperibilita' | assente | nessun obbligo nelle fonti lette | Raccomandazione organizzativa, non requisito normativo |

## 8. Azioni immediate, in ordine

1. Accertare che cosa attesti la voce di catalogo del 1 ottobre e quando il fabbricante ne
   ha avuto conoscenza (evento A).
2. Trattare l'evento B come incidente grave e verificare la praticabilita' del canale
   presso il CSIRT coordinatore **irlandese** ed ENISA: il preallarme scade sabato 3
   ottobre alle 16:40.
3. Valutare senza ritardo la comunicazione agli utilizzatori sulla possibile compromissione
   della chiave di firma (art. 14, par. 8).
4. Sottoporre al consulente legale i due punti di coordinamento aperti (portata del par. 10
   dell'art. 64; decorrenza dell'art. 64) e la qualifica di microimpresa secondo la
   raccomandazione 2003/361/CE.
5. Non attendere il firmware corretto per notificare.

## Disclaimer

Questo inquadramento e' uno strumento di supporto: non sostituisce il giudizio del
responsabile della conformita' del fabbricante ne' la consulenza legale. La decisione di
notificare e la responsabilita' della notifica restano interamente del fabbricante.
Nessuna notifica e' stata trasmessa da questa analisi.
