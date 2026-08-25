# Estratto: obblighi di segnalazione dell'art. 14 CRA - presupposti, termini, contenuti

Fonti: `../fonti/reg-ue-2024-2847-cra-segnalazione.md` (Reg. (UE) 2024/2847, CELEX
32024R2847) e `../fonti/dir-ue-2022-2555-nis2-segnalazione.md` (Dir. (UE) 2022/2555,
CELEX 32022L2555). Accessed 2026-08-25.

Estratto operativo per il fabbricante di un prodotto con elementi digitali (PDE) che
deve decidere **se**, **entro quando**, **a chi** e **con quale contenuto** segnalare.

## A. I due fatti generatori sono distinti

L'art. 14 costruisce **due obblighi separati**, con presupposti e catene di scadenze
propri. Non vanno confusi: lo stesso evento puo' farne scattare uno, l'altro o
entrambi.

| | Obbligo 1 (par. 1-2) | Obbligo 2 (par. 3-5) |
|---|---|---|
| Fatto generatore | **Vulnerabilita' attivamente sfruttata** contenuta nel PDE | **Incidente grave** che ha un impatto sulla sicurezza del PDE |
| Momento iniziale | Il fabbricante "ne viene a conoscenza" | Il fabbricante "ne viene a conoscenza" |
| Destinatari | CSIRT designato coordinatore **e** ENISA, **simultaneamente** | CSIRT designato coordinatore **e** ENISA, **simultaneamente** |
| Canale | Piattaforma unica di segnalazione ex art. 16 | Piattaforma unica di segnalazione ex art. 16 |

**"Vulnerabilita' attivamente sfruttata"** (art. 3, punto 42): "una vulnerabilita' per
la quale esistono prove attendibili che un soggetto malintenzionato l'ha sfruttata in
un sistema senza l'autorizzazione del proprietario del sistema". Due elementi
cumulativi: *prove attendibili* di sfruttamento gia' avvenuto, e assenza di
autorizzazione del proprietario. Una vulnerabilita' nota, anche grave, anche con
exploit pubblico (PoC), non e' per cio' solo "attivamente sfruttata": il testo richiede
prove che qualcuno l'abbia sfruttata.

**"Incidente grave"**: l'art. 14, par. 5, non definisce "incidente" ma stabilisce
quando un incidente e' **grave**. Un incidente e' grave se (basta uno dei due):

- lett. a) "incide negativamente o e' in grado di incidere negativamente sulla capacita'
  di un prodotto con elementi digitali di proteggere la disponibilita', l'autenticita',
  l'integrita' o la riservatezza di dati o funzioni sensibili o importanti"; **oppure**
- lett. b) "ha portato o e' in grado di portare all'introduzione o all'esecuzione di un
  codice maligno in un prodotto con elementi digitali o nei sistemi informativi e di
  rete di un utilizzatore".

Entrambe le lettere includono il **potenziale** ("e' in grado di"): non serve che il
danno si sia prodotto.

La nozione di "incidente" a monte viene dall'art. 3, punto 43, del CRA, che rinvia
all'art. 6, punto 6, della direttiva (UE) 2022/2555: "un evento che compromette la
disponibilita', l'autenticita', l'integrita' o la riservatezza di dati conservati,
trasmessi o elaborati o dei servizi offerti dai sistemi informatici e di rete o
accessibili attraverso di essi". Il "quasi incidente" (art. 6, punto 5, NIS2) e' un
evento analogo "efficacemente evitato o non si e' verificato": **non** fa scattare
l'art. 14, ed e' notificabile solo in via volontaria ex art. 15, par. 2.

## B. Le due catene di scadenze

Tutti i termini decorrono dal momento in cui **il fabbricante ne e' venuto a
conoscenza**, salvo dove indicato diversamente. Le lettere b) e c) di entrambi i
paragrafi sono precedute dalla clausola "a meno che non siano gia' state fornite le
informazioni pertinenti".

### Vulnerabilita' attivamente sfruttata (par. 2)

| Adempimento | Termine | Decorrenza |
|---|---|---|
| a) Notifica di **preallarme** | senza indebito ritardo e in ogni caso entro **24 ore** | conoscenza della vulnerabilita' attivamente sfruttata |
| b) **Notifica della vulnerabilita'** | senza indebito ritardo e in ogni caso entro **72 ore** | conoscenza della vulnerabilita' attivamente sfruttata |
| c) **Relazione finale** | entro **14 giorni** | dalla **messa a disposizione di una misura correttiva o di attenuazione** |

Il termine della relazione finale **non** decorre dalla conoscenza ne' dalla notifica
delle 72 ore: decorre dalla messa a disposizione del rimedio. Se il rimedio non e'
ancora disponibile, il termine non e' iniziato a decorrere.

### Incidente grave (par. 4)

| Adempimento | Termine | Decorrenza |
|---|---|---|
| a) Notifica di **preallarme** | senza indebito ritardo e in ogni caso entro **24 ore** | conoscenza dell'incidente grave |
| b) **Notifica dell'incidente** | senza indebito ritardo e in ogni caso entro **72 ore** | conoscenza dell'incidente grave |
| c) **Relazione finale** | entro **un mese** | dalla **trasmissione della notifica di cui alla lettera b)** |

Il testo dice "entro un mese", non "entro 30 giorni", e la decorrenza e' la
**trasmissione** della notifica delle 72 ore, non la sua scadenza: se la notifica b) e'
stata trasmessa in anticipo, il mese decorre dalla trasmissione effettiva.

### Relazione intermedia (par. 6)

Fuori dalle due catene: "se necessario, il CSIRT designato come coordinatore che ha
ricevuto per primo la notifica **puo' chiedere** ai fabbricanti di fornire una
relazione intermedia". E' un adempimento su richiesta, senza termine fissato dal testo.

## C. Contenuto minimo di ciascun adempimento

Riportato come lo formula il testo, distinguendo cio' che e' dovuto sempre da cio' che
e' condizionato ("se del caso", "se disponibili").

**Preallarme 24h - vulnerabilita' (par. 2, lett. a)**: indica, **se del caso**, gli
Stati membri sul cui territorio il fabbricante sa che il PDE e' stato messo a
disposizione. Il testo non richiede altro.

**Preallarme 24h - incidente (par. 4, lett. a)**: precisa **come minimo** se si sospetta
che l'incidente sia il risultato di atti illegittimi o malevoli; indica, se del caso,
gli Stati membri sul cui territorio il PDE e' stato messo a disposizione.

**Notifica 72h - vulnerabilita' (par. 2, lett. b)**: informazioni generali, **se
disponibili**, sul PDE interessato; natura generale dello sfruttamento e della
vulnerabilita'; misure correttive o di attenuazione adottate e quelle che gli
utilizzatori possono adottare; **se del caso**, il grado di sensibilita' attribuito dal
fabbricante alle informazioni notificate.

**Notifica 72h - incidente (par. 4, lett. b)**: informazioni generali, se disponibili,
sulla natura dell'incidente; **valutazione iniziale** dell'incidente; misure correttive
o di attenuazione adottate e quelle adottabili dagli utilizzatori; se del caso, il
grado di sensibilita'.

**Relazione finale - vulnerabilita' (par. 2, lett. c)**: comprende **almeno**
(i) descrizione della vulnerabilita', compresi gravita' e impatto; (ii) **se
disponibili**, informazioni su qualsiasi soggetto malintenzionato che l'abbia sfruttata
o la sfrutti; (iii) informazioni dettagliate sull'aggiornamento di sicurezza o sulle
altre misure correttive messe a disposizione.

**Relazione finale - incidente (par. 4, lett. c)**: comprende **almeno**
(i) descrizione dettagliata dell'incidente, gravita' e impatto; (ii) tipo di minaccia o
causa di fondo che ha probabilmente innescato l'incidente; (iii) misure di attenuazione
adottate e in corso.

Il **grado di sensibilita'** indicato ai sensi del par. 2, lett. a), non e' un campo
decorativo: e' il presupposto che l'art. 16, par. 2, secondo comma, richiama per il
ritardo eccezionale nella diffusione della notifica agli altri CSIRT.

## D. Canale e destinatario territoriale (par. 7)

Le notifiche sono trasmesse attraverso la piattaforma unica di segnalazione dell'art. 16
usando **il terminale per la notifica elettronica del CSIRT designato come coordinatore
dello Stato membro in cui il fabbricante ha lo stabilimento principale nell'Unione**, e
sono contemporaneamente accessibili all'ENISA.

**Stabilimento principale** (par. 7, secondo comma): lo Stato membro "in cui sono
prevalentemente adottate le decisioni relative alla cibersicurezza dei suoi prodotti con
elementi digitali". Se non determinabile: lo Stato membro dello stabilimento con il
**maggior numero di dipendenti** nell'Unione.

**Fabbricante senza stabilimento principale nell'Unione** (par. 7, terzo comma): si
applica la cascata, **nell'ordine**, sulla base delle informazioni a disposizione del
fabbricante:

1. lett. a) Stato membro del **rappresentante autorizzato** che agisce per il maggior
   numero di PDE del fabbricante;
2. lett. b) Stato membro dell'**importatore** che immette sul mercato il maggior numero
   di PDE del fabbricante;
3. lett. c) Stato membro del **distributore** che mette a disposizione il maggior numero
   di PDE del fabbricante;
4. lett. d) Stato membro in cui e' situato il **maggior numero di utilizzatori** dei PDE
   del fabbricante.

Solo per il caso della lett. d) il quarto comma consente di mantenere **lo stesso**
CSIRT per le notifiche successive.

Chi sia il CSIRT coordinatore per l'Italia non lo dice il CRA: vedi
`csirt-coordinatore-e-canale-italiano.md`.

## E. Obbligo autonomo di informare gli utilizzatori (par. 8)

Distinto dalla notifica alle autorita' e **non** subordinato ad essa. "Dal momento in
cui e' venuto a conoscenza", il fabbricante informa gli utilizzatori interessati e, se
del caso, tutti gli utilizzatori, della vulnerabilita' o dell'incidente e, se
necessario, delle attenuazioni e misure correttive adottabili, "se del caso in un
formato strutturato, leggibile da un dispositivo automatico e che possa essere
facilmente elaborato automaticamente".

Il testo non fissa un termine numerico per questo adempimento, ma prevede una
conseguenza: se il fabbricante non informa **tempestivamente**, i CSIRT coordinatori che
hanno ricevuto la notifica "possono fornire tali informazioni agli utilizzatori se
ritenuto proporzionato e necessario".

## F. Segnalazione volontaria (art. 15) e effetti della notifica (art. 17)

- Art. 15, par. 1-2: fabbricanti **e altre persone** possono notificare su base
  volontaria qualsiasi vulnerabilita' (non solo quelle attivamente sfruttate), le
  minacce informatiche che potrebbero incidere sul profilo di rischio del PDE, gli
  incidenti non gravi e i quasi incidenti.
- Art. 15, par. 3: il CSIRT "puo' trattare le notifiche obbligatorie in via prioritaria
  rispetto alle notifiche volontarie".
- Art. 15, par. 4: se un terzo notifica una vulnerabilita' attivamente sfruttata o un
  incidente grave sul PDE, il CSIRT ne informa **senza indebito ritardo il fabbricante**.
  Da quel momento il fabbricante "ne e' venuto a conoscenza" ai fini del par. 1.
- Art. 15, par. 5: la segnalazione volontaria "non ha l'effetto di imporre alla persona
  fisica o giuridica notificante alcun obbligo aggiuntivo a cui non sarebbe stata
  sottoposta se non avesse trasmesso la notifica".
- Art. 17, par. 4: "La sola notifica in conformita' dell'articolo 14, paragrafi 1 e 3, o
  dell'articolo 15, paragrafi 1 e 2, non sottopone la persona fisica o giuridica
  notificante a una maggiore responsabilita'".
- Art. 17, par. 6: i CSIRT coordinatori "prestano assistenza tecnica in relazione agli
  obblighi di segnalazione a norma dell'articolo 14 ai fabbricanti e in particolare ai
  fabbricanti che si qualificano come microimprese o piccole o medie imprese".

## G. Presupposti organizzativi che l'art. 13 pone a monte

L'art. 14 presuppone che il fabbricante sia in condizione di **accorgersi** di una
vulnerabilita' e di **produrre** un rimedio. Gli obblighi corrispondenti sono nell'art.
13 e nell'allegato I, parte II:

- art. 13, par. 6: quando una vulnerabilita' e' individuata in un **componente**,
  compreso un componente open source, il fabbricante la segnala a chi fabbrica o
  mantiene il componente e la corregge conformemente all'allegato I, parte II;
- art. 13, par. 7: documentazione sistematica degli aspetti di cibersicurezza,
  "comprese le vulnerabilita' di cui vengono a conoscenza e qualsiasi informazione
  pertinente fornita da terzi";
- art. 13, par. 8, ultimo comma: il fabbricante dispone di "politiche e procedure
  adeguate, comprese politiche di **divulgazione coordinata delle vulnerabilita'**, di
  cui all'allegato I, parte II, punto 5";
- art. 13, par. 17: **punto di contatto unico** che consenta agli utilizzatori di
  comunicare direttamente e rapidamente, "anche per facilitare la segnalazione di
  vulnerabilita' del prodotto con elementi digitali", facilmente identificabile e
  incluso nelle informazioni per l'utilizzatore dell'allegato II;
- allegato I, parte II, punto 1: **distinta base del software (SBOM)** "in un formato di
  uso comune e leggibile da un dispositivo automatico, che includa almeno le dipendenze
  di primo livello del prodotto";
- allegato I, parte II, punto 5: **politica di divulgazione coordinata delle
  vulnerabilita'** messa in atto e applicata;
- allegato I, parte II, punto 6: **indirizzo di contatto** per la segnalazione delle
  vulnerabilita' individuate nel prodotto.

Attenzione alla decorrenza: questi obblighi dell'art. 13 e dell'allegato I **non** sono
tra le disposizioni anticipate dall'art. 71, par. 2 (vedi sezione H). Restano il
riferimento tecnico di come ci si organizza, ma la loro applicabilita' e' successiva a
quella dell'art. 14.

## H. Date di applicazione (art. 71, par. 2) - lettura letterale

Il testo dell'art. 71, par. 2, dice:

- "Il presente regolamento si applica dall'11 dicembre 2027."
- "Tuttavia, l'articolo 14 si applica a decorrere dall'11 settembre 2026 e il capo IV
  (articoli da 35 a 51) si applica a decorrere dall'11 giugno 2026."

Le uniche disposizioni **anticipate** sono quindi l'**art. 14** e il **capo IV**. Ne
seguono due punti che il testo lascia aperti e che la skill segnala senza risolvere:

1. **L'art. 16 non e' tra le disposizioni anticipate.** L'art. 14, par. 1 e 3, impone di
   notificare "tramite la piattaforma unica di segnalazione istituita a norma
   dell'articolo 16", ma l'art. 16 e' soggetto alla data generale dell'11 dicembre 2027.
   Il Regolamento non disciplina il periodo intermedio. Sul piano operativo la
   disponibilita' concreta della piattaforma dall'11 settembre 2026 dipende da ENISA e
   dai terminali nazionali, non da questo testo: **va verificata su fonte ENISA/ACN
   prima di costruirci sopra una procedura**.
2. **L'art. 64 non e' tra le disposizioni anticipate.** Vedi sezione I.

## I. Sanzioni (art. 64) - cosa dice e cosa non dice il testo

- Par. 2: "La non conformita' ai requisiti essenziali di cibersicurezza di cui
  all'allegato I e agli obblighi di cui **agli articoli 13 e 14** e' soggetta a sanzioni
  amministrative pecuniarie fino a **15 000 000 EUR** o, se l'autore del reato e'
  un'impresa, fino al **2,5 % del fatturato mondiale totale annuo** dell'esercizio
  precedente, **se superiore**." I due tetti non sono cumulativi: si applica il maggiore,
  e la percentuale vale solo per le imprese.
- Par. 1: sono **gli Stati membri** a fissare le norme sulle sanzioni e a prendere i
  provvedimenti per assicurarne l'applicazione. L'art. 64 fissa i massimali, non
  una sanzione direttamente applicabile.
- Par. 5: nel determinare l'importo si tiene conto di natura, gravita' e durata della
  violazione e delle sue conseguenze (lett. a), di precedenti sanzioni allo stesso
  operatore per violazione analoga (lett. b), delle dimensioni dell'operatore, "in
  particolare per quanto riguarda le microimprese e le piccole e medie imprese, start up
  comprese", e della quota di mercato (lett. c).
- Par. 10, lett. a): "In deroga ai paragrafi da 3 a 9, le sanzioni amministrative
  pecuniarie di cui a tali paragrafi non si applicano ai fabbricanti che si qualificano
  come microimprese o piccole imprese per quanto riguarda il **mancato rispetto del
  termine** di cui all'articolo 14, paragrafo 2, lettera a), o all'articolo 14,
  paragrafo 4, lettera a)". La deroga riguarda quindi il solo **termine delle 24 ore**,
  non l'obbligo di notificare.
- Par. 10, lett. b): la deroga vale anche per "le violazioni del presente regolamento da
  parte di gestori di software open-source" (testo: "alle violazioni del presente
  regolamento da parte di gestori di software open-source").

**Punto di coordinamento che il testo non chiarisce.** Il par. 10 esclude le sanzioni
"di cui a tali paragrafi", cioe' quelle **dei paragrafi da 3 a 9**, mentre l'obbligo
dell'art. 14 e' sanzionato dal **paragrafo 2**, che non compare in quell'elenco.
Il testo non spiega come le due disposizioni si coordinino. La skill riporta la
formulazione letterale e **non** conclude che micro e piccole imprese siano al riparo
dal massimale del par. 2 per il ritardo sulle 24 ore: la questione va posta al
consulente legale del fabbricante o verificata su orientamenti successivi.

**Decorrenza.** L'art. 71, par. 2, anticipa espressamente il solo art. 14 e il capo IV;
l'art. 64 non e' menzionato e ricade quindi nella data generale dell'11 dicembre 2027.
Questo e' cio' che dice il testo. **Non** significa che l'inadempimento sia privo di
conseguenze tra l'11 settembre 2026 e l'11 dicembre 2027: l'art. 14 e' comunque
vincolante in quel periodo. Quali conseguenze si producano in quell'intervallo il testo
non lo dice, e questa skill non ha letto fonti che lo chiariscano: e' un punto da porre
al consulente legale, non un margine su cui contare. La skill segnala la lettura
letterale e ne indica il limite; non la usa per suggerire di rinviare gli adempimenti.

## J. Cosa la fonte NON dice

- **Non descrive la procedura di registrazione alla piattaforma unica di segnalazione.**
  L'art. 16, par. 1, dice solo che ENISA la istituisce, ne gestisce le operazioni
  quotidiane, e che l'architettura consente a Stati membri ed ENISA di predisporre i
  propri terminali per la notifica elettronica. Nessun testo su account, credenziali,
  onboarding o requisiti tecnici di accesso del fabbricante.
- **Non fissa il formato delle notifiche.** L'art. 14, par. 10, prevede che la
  Commissione **possa**, mediante atti di esecuzione, specificare formato e procedure di
  trasmissione delle notifiche di cui all'art. 14 e agli artt. 15 e 16. Finche' tali
  atti non sono adottati, il contenuto minimo e' quello dei par. 2 e 4.
- **Non disciplina i motivi di ritardo nella diffusione dal lato del fabbricante.**
  L'art. 14, par. 9, prevede un atto delegato della Commissione (termine indicato dal
  testo: entro l'11 dicembre 2025) sui termini e le condizioni per l'applicazione dei
  motivi connessi alla cibersicurezza per il ritardo nella diffusione ex art. 16, par. 2.
  Il ritardo e' comunque una decisione **del CSIRT**, non del fabbricante: il fabbricante
  puo' solo richiederlo e indicare il grado di sensibilita'.
- **Non definisce "venire a conoscenza".** Nessun testo su cosa costituisca conoscenza
  qualificata, chi in azienda debba averne, o come si documenti il momento iniziale. Il
  momento da cui decorrono le 24 ore resta un accertamento di fatto.
- **Non prevede una soglia de minimis** per numero di utenti, gravita' CVSS o impatto
  economico: i presupposti sono quelli qualitativi dei par. 2, 4 e 5.
