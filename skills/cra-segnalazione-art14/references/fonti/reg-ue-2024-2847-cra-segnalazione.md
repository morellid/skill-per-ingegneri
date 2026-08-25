# Fonte: Regolamento (UE) 2024/2847 (Cyber Resilience Act) - obblighi di segnalazione

## Provenienza

- Atto: **Regolamento (UE) 2024/2847** del Parlamento europeo e del Consiglio del
  23 ottobre 2024 relativo a requisiti orizzontali di cibersicurezza per i prodotti
  con elementi digitali (Cyber Resilience Act, CRA).
- ELI: <http://data.europa.eu/eli/reg/2024/2847/oj> - CELEX `32024R2847`.
- Rappresentazione scaricata: **XHTML in lingua italiana** dal repository CELLAR
  dell'Ufficio delle pubblicazioni UE,
  <http://publications.europa.eu/resource/celex/32024R2847>.
- Il medesimo URL serve rappresentazioni diverse a seconda degli header di richiesta.
  La rappresentazione qui trascritta e' quella ottenuta con
  `Accept: application/xhtml+xml` e `Accept-Language: ita` (743.211 byte). Senza header
  lo stesso URL restituisce il descrittore RDF; con il solo `Accept` risponde HTTP 400.
  I due header sono dichiarati in `sources.yaml` nei campi `accept` e `accept_language`,
  cosi' che la CI riscarichi la stessa rappresentazione su cui e' calcolato lo SHA256.
- Binario locale (non committato): `not_in_repo/reg-ue-2024-2847-cra-cellar.xhtml`.
- Accessed: 2026-08-25.

## Identificazione

| Campo | Valore |
|---|---|
| `id` in `sources.yaml` | `reg-ue-2024-2847-cra-segnalazione` |
| SHA256 del binario | `c545dfacd04be16112595c2de51b35c6d6d0329b565b393de581c77b63659f5b` |
| Versione/edizione | Testo consolidato pubblicato in GU UE L del 20 novembre 2024, come servito da CELLAR il 2026-08-25 (743.211 byte) |
| Data di trascrizione | 2026-08-25 |

## Perimetro di questa trascrizione

**Articoli inclusi**: art. 3 (punti 1, 13, 19, 21, 22, 40, 42, 43, 45), art. 13
(par. 6, 7, 8, 17), art. 14 (integrale, par. 1-10), art. 15 (integrale), art. 16
(integrale), art. 17 (integrale), art. 64 (integrale), art. 71 (integrale),
allegato I parte II (integrale).

**Volutamente esclusi**: tutti gli altri articoli del Regolamento (in particolare i capi
sulla classificazione dei prodotti, sulla valutazione della conformita', sulla vigilanza
del mercato e sulla notifica degli organismi), i considerando, e gli allegati II-VIII.
Dentro gli articoli parzialmente trascritti l'omissione e' segnalata in linea con un
marcatore `[... non trascritti]`.

Il criterio del perimetro e' che sia trascritto **verbatim** cio' che la skill
`cra-segnalazione-art14` cita: le definizioni dell'art. 3 usate dalla procedura di
segnalazione, i paragrafi dell'art. 13 che reggono la gestione delle vulnerabilita',
gli artt. 14, 15, 16 e 17 (capo relativo alla segnalazione), l'art. 64 (sanzioni),
l'art. 71 (applicazione) e l'allegato I, parte II. Per la classificazione del PDE e la
valutazione della conformita' vedi la skill `cra-classificazione-pde` e la sua
`references/fonti/`.

Il testo tra fence e' riportato con la tipografia originale della fonte (virgolette
caporali, apostrofi tipografici, accenti). La prosa di contorno di questo file usa
caratteri da tastiera standard.

## Articolo 3 - Definizioni (punti citati dalla skill)

```
Articolo 3

Definizioni

Ai fini del presente regolamento si applicano le definizioni seguenti:

1)
«prodotto con elementi digitali»: qualsiasi prodotto software o hardware e le relative soluzioni di elaborazione dati da remoto, compresi i componenti software o hardware immesso sul mercato separatamente;

13)
«fabbricante»: una persona fisica o giuridica che sviluppa o fabbrica prodotti con elementi digitali o che fa progettare, sviluppare o fabbricare prodotti con elementi digitali e li commercializza con il proprio nome o marchio, a titolo oneroso, di monetizzazione o gratuito;

19)
«microimprese», «piccole imprese» e «medie imprese», rispettivamente: le micro imprese, le piccole imprese e le medie imprese quali definite nell’allegato alla raccomandazione 2003/361/CE;

21)
«immissione sul mercato»: la prima messa a disposizione di un prodotto con elementi digitali sul mercato dell’Unione;

22)
«messa a disposizione sul mercato»: la fornitura, a titolo oneroso o gratuito, di un prodotto con elementi digitali perché sia distribuito o usato sul mercato dell’Unione nel corso di un’attività commerciale;

40)
«vulnerabilità»: un punto debole, una suscettibilità o un difetto di prodotti TIC o servizi TIC che può essere sfruttato da una minaccia informatica;

42)
«vulnerabilità attivamente sfruttata»: una vulnerabilità per la quale esistono prove attendibili che un soggetto malintenzionato l’ha sfruttata in un sistema senza l’autorizzazione del proprietario del sistema;

43)
«incidente»: un incidente quale definito all’articolo 6, punto 6), della direttiva (UE) 2022/2555;

45)
«quasi incidente»: un quasi incidente quale definito all’articolo 6, punto 5), della direttiva (UE) 2022/2555;
```

Nota di lettura (non normativa): i punti 43) e 45) rinviano alla direttiva (UE)
2022/2555. Le due definizioni richiamate sono trascritte in
`dir-ue-2022-2555-nis2-segnalazione.md`.

## Articolo 13 - Obblighi dei fabbricanti (paragrafi citati dalla skill)

```
Articolo 13

Obblighi dei fabbricanti

[paragrafi 1-5 non trascritti]

6. Quando è individuata una vulnerabilità in un componente, compreso un componente open source, integrato nel prodotto con elementi digitali, i fabbricanti la segnalano alla persona o al soggetto che si occupa della fabbricazione o della manutenzione del componente e affrontano e correggono la vulnerabilità conformemente ai requisiti di gestione delle vulnerabilità di cui all’allegato I, parte II. Qualora abbiano sviluppato una modifica del software o dell’hardware per affrontare la vulnerabilità di tale componente, i fabbricanti condividono il codice o la documentazione pertinenti con la persona o il soggetto che si occupa della fabbricazione o della manutenzione del componente, se del caso in un formato leggibile da un dispositivo automatico.
7. I fabbricanti documentano sistematicamente, in modo proporzionato alla natura e ai rischi di cibersicurezza, gli aspetti pertinenti di cibersicurezza relativi al prodotto con elementi digitali, comprese le vulnerabilità di cui vengono a conoscenza e qualsiasi informazione pertinente fornita da terzi e, se del caso, aggiornano la valutazione dei rischi di cibersicurezza del prodotto.
8. All’atto dell’immissione sul mercato di un prodotto con elementi digitali e per la durata del periodo di assistenza, i fabbricanti garantiscono che le vulnerabilità di tale prodotto, compresi i suoi componenti, siano gestite in modo efficace e in conformità dei requisiti essenziali di cibersicurezza di cui all’allegato I, parte II.
I fabbricanti determinano il periodo di assistenza in modo che rifletta la durata di utilizzo prevista del prodotto, tenendo conto, in particolare, delle ragionevoli aspettative degli utilizzatori, della natura del prodotto, compresa la sua finalità prevista, nonché del pertinente diritto dell’Unione che determina la durata di vita dei prodotti con elementi digitali. Nel determinare il periodo di assistenza, i fabbricanti possono tenere conto anche dei periodi di assistenza dei prodotti con elementi digitali che offrono funzionalità analoghe immessi sul mercato da altri fabbricanti, della disponibilità dell’ambiente operativo, dei periodi di assistenza dei componenti integrati che forniscono funzioni essenziali e che provengono da terzi, nonché degli orientamenti pertinenti forniti dall’apposito gruppo di cooperazione amministrativa (ADCO) istituito a norma dell’articolo 52, paragrafo 15, e dalla Commissione. Le questioni da prendere in considerazione per determinare il periodo di assistenza sono prese in considerazione in modo da garantire la proporzionalità.
Fatto salvo il secondo comma, il periodo di assistenza è di almeno cinque anni. Se si prevede che il prodotto con elementi digitali sarà utilizzato per meno di cinque anni, il periodo di assistenza corrisponde alla durata di utilizzo prevista.
Tenendo conto delle raccomandazioni dell’ADCO di cui all’articolo 52, paragrafo 16, la Commissione può adottare atti delegati conformemente all’articolo 61 al fine di integrare il presente regolamento specificando il periodo minimo di assistenza per determinate categorie di prodotti qualora i dati di vigilanza del mercato suggeriscano l’inadeguatezza dei periodi di assistenza.
I fabbricanti includono nella documentazione tecnica di cui all’allegato VII le informazioni prese in considerazione per determinare il periodo di assistenza di un prodotto con elementi digitali.
I fabbricanti dispongono di politiche e procedure adeguate, comprese politiche di divulgazione coordinata delle vulnerabilità, di cui all’allegato I, parte II, punto 5, per trattare e correggere potenziali vulnerabilità del prodotto con elementi digitali segnalate da fonti interne o esterne.

[paragrafi 9-16 non trascritti]

17. Ai fini del presente regolamento, i fabbricanti designano un punto di contatto unico che consenta agli utilizzatori di comunicare direttamente e rapidamente con loro, anche per facilitare la segnalazione di vulnerabilità del prodotto con elementi digitali.
I fabbricanti garantiscono che il punto di contatto unico sia facilmente identificabile dagli utilizzatori. Essi includono inoltre il punto di contatto unico nelle informazioni e istruzioni per l’utilizzatore di cui all’allegato II.
Il punto di contatto unico consente agli utilizzatori di scegliere i mezzi di comunicazione preferiti, senza limitarli agli strumenti automatizzati.

[paragrafi 18-25 non trascritti]
```

## Articolo 14 - Obblighi di segnalazione dei fabbricanti (integrale)

```
Articolo 14
Obblighi di segnalazione dei fabbricanti
1. Un fabbricante notifica simultaneamente al CSIRT designato come coordinatore, conformemente al paragrafo 7 del presente articolo, e all’ENISA, qualsiasi vulnerabilità attivamente sfruttata contenuta nel prodotto con elementi digitali di cui viene a conoscenza. Il fabbricante notifica tale vulnerabilità attivamente sfruttata tramite la piattaforma unica di segnalazione istituita a norma dell’articolo 16.
2. Ai fini della notifica di cui al paragrafo 1, il fabbricante presenta:
a)
una notifica di preallarme di una vulnerabilità attivamente sfruttata, senza indebito ritardo e in ogni caso entro 24 ore dal momento in cui il fabbricante ne è venuto a conoscenza, che indichi, se del caso, gli Stati membri sul cui territorio il fabbricante sia al corrente del fatto che il suo prodotto con elementi digitali è stato messo a disposizione;
b)
a meno che non siano già state fornite le informazioni pertinenti, una notifica delle vulnerabilità, senza indebito ritardo e in ogni caso entro 72 ore dal momento in cui il fabbricante è venuto a conoscenza della vulnerabilità attivamente sfruttata, che fornisca informazioni generali, se disponibili, sul prodotto con elementi digitali interessato, sulla natura generale dello sfruttamento e della vulnerabilità in questione, nonché sulle eventuali misure correttive o di attenuazione adottate e sulle misure correttive o di attenuazione che gli utilizzatori possono adottare, e che indichi anche, se del caso, il grado di sensibilità attribuito dal fabbricante alle informazioni notificate;
c)
a meno che non siano già state fornite le informazioni pertinenti, una relazione finale, entro 14 giorni dalla messa a disposizione di una misura correttiva o di attenuazione, che comprenda almeno:
i)
una descrizione della vulnerabilità, compresi la sua gravità e il suo impatto;
ii)
se disponibili, informazioni relative a qualsiasi soggetto malintenzionato che abbia sfruttato o che sfrutti la vulnerabilità;
iii)
informazioni dettagliate relative all’aggiornamento di sicurezza o ad altre misure correttive messe a disposizione per porre rimedio alla vulnerabilità.
3. Un fabbricante notifica simultaneamente al CSIRT designato come coordinatore, conformemente al paragrafo 7 del presente articolo, e all’ENISA, qualsiasi incidente grave che abbia un impatto sulla sicurezza del prodotto con elementi digitali di cui viene a conoscenza. Il fabbricante notifica tale incidente tramite la piattaforma unica di segnalazione istituita a norma dell’articolo 16.
4. Ai fini della notifica di cui al paragrafo 3, il fabbricante presenta:
a)
una notifica di preallarme di un incidente grave che ha un impatto sulla sicurezza del prodotto con elementi digitali, senza indebito ritardo e in ogni caso entro 24 ore dal momento in cui il fabbricante ne è venuto a conoscenza, che precisi, come minimo, se si sospetta che l’incidente sia il risultato di atti illegittimi o malevoli, e che indichi, se del caso, gli Stati membri sul cui territorio il fabbricante sia al corrente del fatto che il suo prodotto con elementi digitali è stato messo a disposizione;
b)
a meno che non siano già state fornite le informazioni pertinenti, una notifica dell’incidente, senza indebito ritardo e in ogni caso entro 72 ore dal momento in cui il fabbricante ne è venuto a conoscenza, che fornisca informazioni generali, se disponibili, sulla natura dell’incidente, una valutazione iniziale dell’incidente, nonché le eventuali misure correttive o di attenuazione adottate e le misure correttive o di attenuazione che gli utilizzatori possono adottare, e che indichi anche, se del caso, il grado di sensibilità attribuito dal fabbricante alle informazioni notificate;
c)
a meno che non siano già state fornite le informazioni pertinenti, una relazione finale entro un mese dalla trasmissione della notifica di incidente di cui alla lettera b), che comprenda almeno:
i)
una descrizione dettagliata dell’incidente, comprensiva della sua gravità e del suo impatto;
ii)
il tipo di minaccia o la causa di fondo che ha probabilmente innescato l’incidente;
iii)
le misure di attenuazione adottate e in corso;
5. Ai fini del paragrafo 3, un incidente che ha un impatto sulla sicurezza del prodotto con elementi digitali è considerato grave se:
a)
incide negativamente o è in grado di incidere negativamente sulla capacità di un prodotto con elementi digitali di proteggere la disponibilità, l’autenticità, l’integrità o la riservatezza di dati o funzioni sensibili o importanti; o
b)
ha portato o è in grado di portare all’introduzione o all’esecuzione di un codice maligno in un prodotto con elementi digitali o nei sistemi informativi e di rete di un utilizzatore del prodotto con elementi digitali.
6. Se necessario, il CSIRT designato come coordinatore che ha ricevuto per primo la notifica può chiedere ai fabbricanti di fornire una relazione intermedia sui pertinenti aggiornamenti della situazione sulla vulnerabilità attivamente sfruttata o sull’incidente grave che ha un impatto sulla sicurezza del prodotto con elementi digitali.
7. Le notifiche di cui ai paragrafi 1 e 3 del presente articolo sono trasmesse attraverso la piattaforma unica di segnalazione di cui all’articolo 16 utilizzando uno dei terminali per la notifica elettronica di cui all’articolo 16, paragrafo 1. La notifica è trasmessa utilizzando il terminale per la notifica elettronica del CSIRT designato come coordinatore dello Stato membro in cui i fabbricanti hanno lo stabilimento principale nell’Unione ed è contemporaneamente accessibile all’ENISA.
Ai fini del presente regolamento, si considera che un fabbricante abbia il suo stabilimento principale nell’Unione nello Stato membro in cui sono prevalentemente adottate le decisioni relative alla cibersicurezza dei suoi prodotti con elementi digitali. Se non è possibile determinare detto Stato membro, si considera che lo stabilimento principale sia nello Stato membro in cui il fabbricante ha lo stabilimento con il maggior numero di dipendenti nell’Unione.
Se non ha uno stabilimento principale nell’Unione, il fabbricante trasmette le notifiche di cui ai paragrafi 1 e 3 utilizzando il terminale per la notifica elettronica del CSIRT designato come coordinatore nello Stato membro determinato secondo l’ordine seguente e sulla base delle informazioni a disposizione del fabbricante:
a)
lo Stato membro in cui è stabilito il rappresentante autorizzato che agisce per conto del fabbricante per il maggior numero di prodotti con elementi digitali di tale fabbricante;
b)
lo Stato membro in cui è stabilito l’importatore che immette sul mercato il maggior numero di prodotti con elementi digitali di tale fabbricante;
c)
lo Stato membro in cui è stabilito il distributore che mette a disposizione sul mercato il maggior numero di prodotti con elementi digitali di tale fabbricante;
d)
lo Stato membro in cui è situato il maggior numero di utilizzatori di prodotti con elementi digitali di tale fabbricante.
In relazione al terzo comma, lettera d), un fabbricante può presentare notifiche relative a qualsiasi successiva vulnerabilità attivamente sfruttata o incidente grave che ha un impatto sulla sicurezza del prodotto con elementi digitali allo stesso CSIRT designato come coordinatore a cui ha presentato la prima notifica.
8. Dal momento in cui è venuto a conoscenza di una vulnerabilità attivamente sfruttata o di un incidente grave avente un impatto sulla sicurezza del prodotto con elementi digitali, il fabbricante informa gli utilizzatori interessati del prodotto con elementi digitali e, se del caso, tutti gli utilizzatori, di tale vulnerabilità o incidente e, se necessario, di qualsiasi attenuazione dei rischi e misure correttive che gli utilizzatori possono adottare per attenuare l’impatto di tale vulnerabilità o incidente, se del caso in un formato strutturato, leggibile da un dispositivo automatico e che possa essere facilmente elaborato automaticamente. Se il fabbricante non informa tempestivamente gli utilizzatori del prodotto con elementi digitali, i CSIRT designati come coordinatori che hanno ricevuto la notifica possono fornire tali informazioni agli utilizzatori se ritenuto proporzionato e necessario per prevenire o attenuare l’impatto di tale vulnerabilità o incidente.
9. Entro l’11 dicembre 2025 la Commissione adotta atti delegati conformemente all’articolo 61 per integrare il presente regolamento specificando i termini e le condizioni per l’applicazione dei motivi connessi alla cibersicurezza relativamente al ritardo nella diffusione delle notifiche di cui all’articolo 16, paragrafo 2. La Commissione coopera con la rete di CSIRT istituita a norma dell’articolo 15 della direttiva (UE) 2022/2555 e con l’ENISA nella preparazione dei progetti di atti delegati.
10. La Commissione può, mediante atti di esecuzione, specificare ulteriormente il formato e le procedure di trasmissione delle notifiche di cui al presente articolo, nonché agli articoli 15 e 16. Tali atti di esecuzione sono adottati secondo la procedura d’esame di cui all’articolo 62, paragrafo 2. La Commissione coopera con la rete di CSIRT e con l’ENISA nella preparazione del progetto di atto delegato.
```

## Articolo 15 - Segnalazione volontaria (integrale)

```
Articolo 15
Segnalazione volontaria
1. I fabbricanti e altre persone fisiche o giuridiche possono notificare a un CSIRT designato come coordinatore o all’ENISA, su base volontaria, qualsiasi vulnerabilità contenuta in un prodotto con elementi digitali nonché le minacce informatiche che potrebbero incidere sul profilo di rischio di un prodotto con elementi digitali.
2. I fabbricanti e altre persone fisiche o giuridiche possono notificare a un CSIRT designato come coordinatore o all’ENISA, su base volontaria, qualsiasi incidente che abbia un impatto sulla sicurezza del prodotto con elementi digitali e qualsiasi quasi incidente che avrebbe potuto tradursi in un simile incidente.
3. Il CSIRT designato come coordinatore o l’ENISA trattano le notifiche di cui ai paragrafi 1 e 2 del presente articolo secondo la procedura di cui all’articolo 16.
Il CSIRT designato come coordinatore può trattare le notifiche obbligatorie in via prioritaria rispetto alle notifiche volontarie.
4. Qualora una persona fisica o giuridica diversa dal fabbricante notifichi una vulnerabilità attivamente sfruttata o un incidente grave che ha un impatto sulla sicurezza di un prodotto con elementi digitali conformemente al paragrafo 1 o 2, il CSIRT designato come coordinatore ne informa senza indebito ritardo il fabbricante.
5. I CSIRT designati come coordinatori e l’ENISA garantiscono la riservatezza e la protezione adeguata delle informazioni fornite da una persona fisica o giuridica notificante. Fatti salvi la prevenzione, l’indagine, l’accertamento e il perseguimento di reati, la segnalazione volontaria non ha l’effetto di imporre alla persona fisica o giuridica notificante alcun obbligo aggiuntivo a cui non sarebbe stata sottoposta se non avesse trasmesso la notifica.
```

## Articolo 16 - Istituzione di una piattaforma unica di segnalazione (integrale)

```
Articolo 16
Istituzione di una piattaforma unica di segnalazione
1. Ai fini delle notifiche di cui all’articolo 14, paragrafi 1 e 3, e all’articolo 15, paragrafi 1 e 2, e per semplificare gli obblighi di segnalazione dei fabbricanti, l’ENISA istituisce una piattaforma unica di segnalazione. Le operazioni quotidiane di tale piattaforma unica di segnalazione sono gestite e mantenute dall’ENISA. L’architettura della piattaforma unica di segnalazione consente agli Stati membri e all’ENISA di predisporre i propri terminali per la notifica elettronica.
2. Dopo aver ricevuto una notifica, il CSIRT designato come coordinatore che ha ricevuto per primo la notifica la diffonde senza ritardo attraverso la piattaforma unica di segnalazione ai CSIRT designati come coordinatori sul cui territorio il fabbricante ha indicato che il prodotto con elementi digitali è stato messo a disposizione.
In circostanze eccezionali e, in particolare, su richiesta del fabbricante e alla luce del grado di sensibilità delle informazioni notificate indicato dal fabbricante a norma dell’articolo 14, paragrafo 2, lettera a), del presente regolamento, la diffusione della notifica può essere ritardata per motivi connessi alla cibersicurezza per un periodo di tempo strettamente necessario, anche nel caso in cui una vulnerabilità sia oggetto di una procedura di divulgazione coordinata delle vulnerabilità di cui all’articolo 12, paragrafo 1, della direttiva (UE) 2022/2555. Qualora un CSIRT decida di trattenere una notifica, informa immediatamente l’ENISA della decisione e fornisce sia una giustificazione per il trattenimento della notifica sia un’indicazione di quando diffonderà la notifica secondo la procedura di diffusione di cui al presente paragrafo. L’ENISA può sostenere il CSIRT nell’applicazione dei motivi connessi alla cibersicurezza relativamente al ritardo nella diffusione della notifica.
In circostanze particolarmente eccezionali, se il fabbricante indica nella notifica di cui all’articolo 14, paragrafo 2, lettera b):
a)
che la vulnerabilità notificata è stata attivamente sfruttata da un soggetto malintenzionato e, in base alle informazioni disponibili, non è stata sfruttata in altri Stati membri oltre a quello del CSIRT designato come coordinatore al quale il fabbricante ha notificato la vulnerabilità;
b)
che un’ulteriore diffusione immediata della vulnerabilità notificata comporterebbe probabilmente la fornitura di informazioni la cui divulgazione sarebbe contraria agli interessi essenziali di tale Stato membro; o
c)
che l’ulteriore diffusione della vulnerabilità notificata si tradurrebbe in un rischio di cibersicurezza elevato e imminente;
unicamente l’informazione dell’avvenuta notifica da parte del fabbricante, le informazioni generali sul prodotto, le informazioni sulla natura generale dello sfruttamento e l’informazione che sono stati sollevati motivi di sicurezza, devono essere rese simultaneamente disponibili a l’ENISA fino a quando la notifica completa non viene diffusa ai CSIRT interessati e all’ENISA. Se l’ENISA, sulla base di tali informazioni, ritiene che vi sia un rischio sistemico capace di incidere sulla sicurezza del mercato interno, raccomanda al CSIRT ricevente di diffondere la notifica completa agli altri CSIRT designati come coordinatori e all’ENISA stessa.
3. Dopo aver ricevuto la notifica di una vulnerabilità attivamente sfruttata in un prodotto con elementi digitali o di un incidente grave che ha un impatto sulla sicurezza di un prodotto con elementi digitali, i CSIRT designati come coordinatori forniscono alle autorità di vigilanza del mercato dei rispettivi Stati membri le informazioni notificate necessarie alle autorità di vigilanza del mercato per adempiere ai loro obblighi a norma del presente regolamento.
4. L’ENISA adotta misure adeguate e proporzionate dal punto di vista tecnico, operativo e organizzativo per gestire i rischi posti alla sicurezza della piattaforma unica di segnalazione e alle informazioni trasmesse o diffuse attraverso la stessa. Essa notifica senza indebito ritardo alla rete di CSIRT e alla Commissione qualsiasi incidente di sicurezza che incida sulla piattaforma unica di segnalazione.
5. L’ENISA, in cooperazione con la rete di CSIRT, fornisce e attua specifiche sulle misure tecniche, operative e organizzative relative all’istituzione, alla manutenzione e al funzionamento sicuro della piattaforma unica di segnalazione di cui al paragrafo 1, comprese almeno le disposizioni in materia di sicurezza relative all’istituzione, al funzionamento e alla manutenzione della piattaforma unica di segnalazione, nonché i terminali per la notifica elettronica istituiti dai CSIRT designati come coordinatori a livello nazionale e dall’ENISA a livello di Unione, compresi gli aspetti procedurali per garantire che, qualora per una vulnerabilità notificata non siano disponibili misure correttive o di attenuazione, le informazioni su tale vulnerabilità siano condivise nel rispetto di rigorosi protocolli di sicurezza e in funzione della necessità di conoscere.
6. Qualora un CSIRT designato come coordinatore sia stato informato di una vulnerabilità attivamente sfruttata nell’ambito di una procedura di divulgazione coordinata delle vulnerabilità di cui all’articolo 12, paragrafo 1, della direttiva (UE) 2022/2555, il CSIRT designato come coordinatore che ha ricevuto per primo la notifica può ritardare la diffusione della notifica in questione attraverso la piattaforma unica di segnalazione sulla base di motivi giustificati legati alla cibersicurezza per un periodo non superiore a quello strettamente necessario e fino a quando non sia stato dato il consenso alla divulgazione dalle parti coinvolte nella divulgazione coordinata delle vulnerabilità. Tale requisito non impedisce ai fabbricanti di notificare tale vulnerabilità su base volontaria secondo la procedura di cui al presente articolo.
```

## Articolo 17 - Altre disposizioni relative alla segnalazione (integrale)

```
Articolo 17
Altre disposizioni relative alla segnalazione
1. L’ENISA può trasmettere alla rete europea delle organizzazioni di collegamento per le crisi informatiche (EU-CyCLONe), istituita a norma dell’articolo 16 della direttiva (UE) 2022/2555, le informazioni notificate a norma dell’articolo 14, paragrafi 1 e 3, e dell’articolo 15, paragrafi 1 e 2, del presente regolamento se tali informazioni sono pertinenti per la gestione coordinata degli incidenti e delle crisi di cibersicurezza su vasta scala a livello operativo. Al fine di determinare tale pertinenza, l’ENISA può prendere in considerazione le analisi tecniche effettuate dalla rete di CSIRT, se disponibili.
2. Qualora sia necessario sensibilizzare il pubblico per prevenire o attenuare un incidente grave che ha un impatto sulla sicurezza del prodotto con elementi digitali o per gestire un incidente in corso, o qualora la divulgazione dell’incidente sia altrimenti nell’interesse pubblico, il CSIRT designato come coordinatore dello Stato membro pertinente può, previa consultazione del fabbricante interessato e, se del caso, in cooperazione con l’ENISA, informare il pubblico in merito all’incidente o chiedere al fabbricante di farlo.
3. L’ENISA, sulla base delle notifiche ricevute a norma dell’articolo 14, paragrafi 1 e 3, e dell’articolo 15, paragrafi 1 e 2, del presente regolamento elabora, ogni 24 mesi, una relazione tecnica sulle tendenze emergenti in materia di rischi di cibersicurezza nei prodotti con elementi digitali e la presenta al gruppo di cooperazione istituito dall’articolo 14 della direttiva (UE) 2022/2555. La prima relazione di questo tipo è presentata entro 24 mesi dalla data di applicazione degli obblighi stabiliti all’articolo 14, paragrafi 1 e 3. L’ENISA integra le informazioni pertinenti tratte dalle sue relazioni tecniche nella sua relazione sullo stato della cibersicurezza nell’Unione, presentata a norma dell’articolo 18 della direttiva (UE) 2022/2555.
4. La sola notifica in conformità dell’articolo 14, paragrafi 1 e 3, o dell’articolo 15, paragrafi 1 e 2, non sottopone la persona fisica o giuridica notificante a una maggiore responsabilità.
5. Dopo la messa a disposizione di un aggiornamento di sicurezza o l’adozione di un’altra forma di misure correttive o di attenuazione, l’ENISA, d’intesa con il fabbricante del prodotto con elementi digitali interessato, aggiunge la vulnerabilità notificata a norma dell’articolo 14, paragrafo 1, o dell’articolo 15, paragrafo 1, del presente regolamento alla banca dati europea delle vulnerabilità istituita a norma dell’articolo 12 della direttiva (UE) 2022/2555.
6. I CSIRT designati come coordinatori prestano assistenza tecnica in relazione agli obblighi di segnalazione a norma dell’articolo 14 ai fabbricanti e in particolare ai fabbricanti che si qualificano come microimprese o piccole o medie imprese.
```

## Articolo 64 - Sanzioni (integrale)

```
Articolo 64
Sanzioni
1. Gli Stati membri fissano le norme sulle sanzioni applicabili in caso di violazione del presente regolamento e prendono tutti i provvedimenti necessari per assicurarne l’applicazione. Le sanzioni previste devono essere effettive, proporzionate e dissuasive. Gli Stati membri notificano tali norme e misure alla Commissione, senza indugio, e provvedono poi a dare immediata notifica delle eventuali modifiche successive.
2. La non conformità ai requisiti essenziali di cibersicurezza di cui all’allegato I e agli obblighi di cui agli articoli 13 e 14 è soggetta a sanzioni amministrative pecuniarie fino a 15 000 000 EUR o, se l’autore del reato è un’impresa, fino al 2,5 % del fatturato mondiale totale annuo dell’esercizio precedente, se superiore.
3. La non conformità agli obblighi di cui agli articoli da 18 a 23, all’articolo 28, all’articolo 30, paragrafi da 1 a 4, all’articolo 31, paragrafi da 1 a 4, all’articolo 32, paragrafi 1, 2 e 3, all’articolo 33, paragrafo 5, e agli articoli 39, 41, 47, 49 e 53 è soggetta a sanzioni amministrative pecuniarie fino a 10 000 000 EUR o, se l’autore del reato è un’impresa, fino al 2 % del fatturato mondiale totale annuo dell’esercizio precedente, se superiore.
4. La fornitura di informazioni inesatte, incomplete o fuorvianti agli organismi notificati e alle autorità di vigilanza del mercato è soggetta a sanzioni amministrative pecuniarie fino a 5 000 000 EUR o, se l’autore del reato è un’impresa, fino all’1 % del fatturato mondiale totale annuo dell’esercizio precedente, se superiore.
5. Nel decidere l’importo della sanzione amministrativa pecuniaria in ogni singolo caso, si tiene conto di tutte le circostanze pertinenti della situazione specifica e si tiene quanto segue in debita considerazione:
a)
la natura, la gravità e la durata della violazione e delle sue conseguenze;
b)
se le stesse o altre autorità di vigilanza del mercato hanno già applicato sanzioni amministrative pecuniarie allo stesso operatore economico per una violazione analoga;
c)
le dimensioni, in particolare per quanto riguarda le microimprese e le piccole e medie imprese, start up comprese, e la quota di mercato dell’operatore economico che ha commesso la violazione.
6. Le autorità di vigilanza del mercato che applicano sanzioni amministrative pecuniarie danno comunicazione di tale applicazione alle autorità di vigilanza del mercato di altri Stati membri mediante il sistema di informazione e comunicazione di cui all’articolo 34 del regolamento (UE) 2019/1020.
7. Ciascuno Stato membro può prevedere regole che dispongano se e in quale misura possono essere inflitte sanzioni amministrative pecuniarie ad autorità pubbliche e organismi pubblici istituiti in tale Stato membro.
8. A seconda dell’ordinamento giuridico degli Stati membri, le regole in materia di sanzioni amministrative pecuniarie possono essere applicate in modo tale che le sanzioni pecuniarie siano inflitte dai tribunali nazionali competenti o da altri organismi in base alle competenze stabilite a livello nazionale in tali Stati membri. L’applicazione di tali regole in tali Stati membri ha effetto equivalente.
9. Le sanzioni amministrative pecuniarie possono essere inflitte, in funzione delle circostanze di ogni singolo caso, in aggiunta a qualsiasi altra misura correttiva o restrittiva applicata dalle autorità di vigilanza del mercato per la stessa violazione.
10. In deroga ai paragrafi da 3 a 9, le sanzioni amministrative pecuniarie di cui a tali paragrafi non si applicano:
a)
ai fabbricanti che si qualificano come microimprese o piccole imprese per quanto riguarda il mancato rispetto del termine di cui all’articolo 14, paragrafo 2, lettera a), o all’articolo 14, paragrafo 4, lettera a);
b)
alle violazioni del presente regolamento da parte di gestori di software open-source.
```

## Articolo 71 - Entrata in vigore e applicazione (integrale)

```
Articolo 71
Entrata in vigore e applicazione
1. Il presente regolamento entra in vigore il ventesimo giorno successivo alla pubblicazione nella Gazzetta ufficiale dell’Unione europea.
2. Il presente regolamento si applica dall’11 dicembre 2027.
Tuttavia, l’articolo 14 si applica a decorrere dall’11 settembre 2026 e il capo IV (articoli da 35 a 51) si applica a decorrere dall’11 giugno 2026.
Il presente regolamento è obbligatorio in tutti i suoi elementi e direttamente applicabile in ciascuno degli Stati membri
```

## Allegato I, parte II - Requisiti di gestione delle vulnerabilita' (integrale)

```
ALLEGATO I

REQUISITI ESSENZIALI DI CIBERSICUREZZA

Parte II Requisiti di gestione delle vulnerabilità
I fabbricanti di prodotti con elementi digitali:
1)
identificano e documentano le vulnerabilità e i componenti contenuti nel prodotto con elementi digitali, redigendo anche una distinta base del software in un formato di uso comune e leggibile da un dispositivo automatico, che includa almeno le dipendenze di primo livello del prodotto;
2)
in relazione ai rischi posti dai prodotti con elementi digitali, affrontano e correggono tempestivamente le vulnerabilità, anche fornendo aggiornamenti di sicurezza; ove tecnicamente fattibile, nuovi aggiornamenti di sicurezza sono forniti separatamente dagli aggiornamenti della funzionalità;
3)
effettuano prove e riesami efficaci e periodici della sicurezza del prodotto con elementi digitali;
4)
una volta reso disponibile un aggiornamento di sicurezza, condividono e divulgano pubblicamente informazioni sulle vulnerabilità risolte, compresi una descrizione delle vulnerabilità, informazioni che consentano agli utilizzatori di identificare il prodotto con elementi digitali interessato, l’impatto delle vulnerabilità, la loro gravità e informazioni chiare e accessibili che aiutino gli utilizzatori a correggere le vulnerabilità; in casi debitamente giustificati, qualora ritengano che i rischi di sicurezza legati alla divulgazione siano superiori ai benefici in termini di sicurezza, i fabbricanti possono ritardare la divulgazione di informazioni su una vulnerabilità risolta fino a quando gli utilizzatori non abbiano avuto la possibilità di applicare la pertinente patch;
5)
mettono in atto e applicano una politica di divulgazione coordinata delle vulnerabilità;
6)
adottano misure per facilitare la condivisione di informazioni sulle potenziali vulnerabilità nel loro prodotto con elementi digitali e nei componenti di terzi contenuti in tale prodotto, fornendo anche un indirizzo di contatto per la segnalazione delle vulnerabilità individuate nel prodotto con elementi digitali;
7)
prevedono meccanismi per distribuire in modo sicuro gli aggiornamenti dei prodotti con elementi digitali, per garantire che le vulnerabilità siano corrette o attenuate in modo tempestivo e, ove applicabile per gli aggiornamenti di sicurezza, in modo automatico;
8)
garantiscono che, qualora disponibili, siano diffusi tempestivamente e gratuitamente, salvo diversamente convenuto tra un fabbricante e un utilizzatore commerciale in relazione a un prodotto su misura con elementi digitali, aggiornamenti di sicurezza per risolvere i problemi di sicurezza individuati, accompagnati da messaggi di avviso che forniscano agli utilizzatori le informazioni pertinenti, comprese le potenziali misure da adottare.
```
