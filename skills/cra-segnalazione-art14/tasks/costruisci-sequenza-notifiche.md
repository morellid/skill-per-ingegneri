# Task: costruire la sequenza degli adempimenti e il contenuto delle notifiche

## Obiettivo

Dato un obbligo gia' qualificato (vedi `qualifica-evento-segnalabile.md`), produrre la
**sequenza datata** degli adempimenti dovuti e il **contenuto minimo** di ciascuno,
distinguendo cio' che il testo impone da cio' che condiziona a disponibilita' o
opportunita'.

## Input richiesti

1. Quale catena si applica: vulnerabilita' attivamente sfruttata (art. 14, par. 2),
   incidente grave (par. 4), o entrambe.
2. **Data e ora del momento iniziale** ("venuto a conoscenza"), come fissato nel task di
   qualificazione.
3. Se una **misura correttiva o di attenuazione** e' gia' stata messa a disposizione e,
   in tal caso, quando (serve per la relazione finale sulle vulnerabilita').
4. Se una notifica e' gia' stata trasmessa, quale e quando.
5. Stati membri sul cui territorio il fabbricante sa che il PDE e' stato messo a
   disposizione, se noti.
6. Se il fabbricante intende chiedere un trattamento riservato: quale **grado di
   sensibilita'** attribuisce alle informazioni.

## Fonti

- `../references/estratti/cra-art14-obblighi-e-termini.md`, sezioni B, C, D, E.
- `../references/fonti/reg-ue-2024-2847-cra-segnalazione.md`, art. 14 par. 2, 4, 6, 7, 8;
  art. 16 par. 2.

## Procedura

### Passo 1 - Costruisci la timeline

Calcola le scadenze dal momento iniziale. Riporta sempre **anche la formula del testo**,
non solo la data: le 24 e le 72 ore sono termini massimi preceduti da "senza indebito
ritardo", quindi la scadenza non e' un obiettivo ma un limite.

**Catena vulnerabilita' attivamente sfruttata (par. 2)**

| # | Adempimento | Termine | Decorrenza |
|---|---|---|---|
| 1 | Notifica di preallarme | senza indebito ritardo, in ogni caso entro **24 ore** | conoscenza |
| 2 | Notifica della vulnerabilita' | senza indebito ritardo, in ogni caso entro **72 ore** | conoscenza |
| 3 | Relazione finale | entro **14 giorni** | **messa a disposizione della misura correttiva o di attenuazione** |

**Catena incidente grave (par. 4)**

| # | Adempimento | Termine | Decorrenza |
|---|---|---|---|
| 1 | Notifica di preallarme | senza indebito ritardo, in ogni caso entro **24 ore** | conoscenza |
| 2 | Notifica dell'incidente | senza indebito ritardo, in ogni caso entro **72 ore** | conoscenza |
| 3 | Relazione finale | entro **un mese** | **trasmissione** della notifica n. 2 |

Due errori da non commettere:

- la relazione finale sulla **vulnerabilita'** non decorre dalla conoscenza ne' dalle
  72 ore, ma dalla messa a disposizione del rimedio. Se il rimedio non esiste ancora, il
  termine non e' iniziato: dillo esplicitamente invece di indicare una data;
- la relazione finale sull'**incidente** e' "entro un mese" (non "30 giorni") dalla
  **trasmissione effettiva** della notifica delle 72 ore, non dalla scadenza del termine.
  Se la notifica e' stata trasmessa in anticipo, il mese decorre da quel momento.

Se entrambe le catene sono attive, presentale **affiancate e distinte**: hanno lo stesso
momento iniziale ma esiti finali diversi, e vanno tracciate separatamente.

### Passo 2 - Verifica la clausola di non duplicazione

Le lettere b) e c) di entrambi i paragrafi sono precedute da "**a meno che non siano gia'
state fornite le informazioni pertinenti**". Se un adempimento precedente ha gia'
veicolato tutte le informazioni richieste dal successivo, il testo non impone di
ripeterle.

Applicala con cautela: la clausola esonera dal fornire **le informazioni pertinenti**
gia' fornite, non dall'adempimento in quanto tale quando restano informazioni nuove.
Nell'output indica quali elementi risultano gia' coperti e quali no, e lascia la
decisione al fabbricante.

### Passo 3 - Compila il contenuto minimo di ciascun adempimento

Per ogni adempimento produci due elenchi separati: **dovuto** e **condizionato**.

**Preallarme 24h - vulnerabilita' (par. 2, lett. a)**
- Condizionato ("se del caso"): gli Stati membri sul cui territorio il fabbricante sa che
  il PDE e' stato messo a disposizione.
- Il testo non richiede altro. Non aggiungere requisiti di contenuto che non ci sono.

**Preallarme 24h - incidente (par. 4, lett. a)**
- Dovuto ("come minimo"): se si sospetta che l'incidente sia il risultato di **atti
  illegittimi o malevoli**.
- Condizionato ("se del caso"): gli Stati membri di messa a disposizione.

**Notifica 72h - vulnerabilita' (par. 2, lett. b)**
- Condizionato ("se disponibili"): informazioni generali sul PDE interessato.
- Dovuto: natura generale **dello sfruttamento** e **della vulnerabilita'**; misure
  correttive o di attenuazione adottate; misure che **gli utilizzatori** possono adottare.
- Condizionato ("se del caso"): **grado di sensibilita'** attribuito dal fabbricante alle
  informazioni notificate.

**Notifica 72h - incidente (par. 4, lett. b)**
- Condizionato ("se disponibili"): informazioni generali sulla natura dell'incidente.
- Dovuto: **valutazione iniziale** dell'incidente; misure correttive o di attenuazione
  adottate; misure adottabili dagli utilizzatori.
- Condizionato ("se del caso"): grado di sensibilita'.

**Relazione finale - vulnerabilita' (par. 2, lett. c)** - "comprende **almeno**":
1. descrizione della vulnerabilita', compresi **gravita'** e **impatto**;
2. se disponibili, informazioni su qualsiasi **soggetto malintenzionato** che l'abbia
   sfruttata o la sfrutti;
3. informazioni **dettagliate** sull'aggiornamento di sicurezza o sulle altre misure
   correttive messe a disposizione.

**Relazione finale - incidente (par. 4, lett. c)** - "comprende **almeno**":
1. descrizione **dettagliata** dell'incidente, gravita' e impatto;
2. **tipo di minaccia o causa di fondo** che ha probabilmente innescato l'incidente;
3. misure di attenuazione **adottate e in corso**.

"Almeno" significa che l'elenco e' un minimo, non un modulo chiuso.

### Passo 4 - Il grado di sensibilita' non e' un campo decorativo

Se il fabbricante ha ragioni per chiedere che la notifica non sia immediatamente diffusa
agli altri CSIRT, spiega il meccanismo effettivo:

- l'indicazione del **grado di sensibilita'** attribuito dal fabbricante alle
  informazioni notificate e' prevista, "se del caso", nel contenuto della **notifica
  delle 72 ore**: art. 14, par. 2, lett. b), per la vulnerabilita' e art. 14, par. 4,
  lett. b), per l'incidente. Il preallarme delle 24 ore (lett. a) non la contempla;
- l'art. 16, par. 2, secondo comma, consente al CSIRT di **ritardare la diffusione** "in
  circostanze eccezionali e, in particolare, su richiesta del fabbricante e alla luce del
  grado di sensibilita'", per il tempo strettamente necessario. Nota che quel comma
  rinvia letteralmente al "grado di sensibilita' ... indicato dal fabbricante a norma
  dell'articolo 14, paragrafo 2, lettera a)", mentre l'indicazione e' prevista dalla
  lett. b): e' un disallineamento del testo, che la skill riporta senza risolverlo e che
  non incide sulla condotta pratica (il grado si indica nella notifica delle 72 ore);
- l'art. 16, par. 2, terzo comma, prevede un regime ancora piu' ristretto "in circostanze
  particolarmente eccezionali", sulla base di indicazioni che il fabbricante deve dare
  **nella notifica di cui all'art. 14, par. 2, lett. b)**;
- l'art. 16, par. 6, riguarda il ritardo quando la vulnerabilita' e' gia' in una
  procedura di divulgazione coordinata ex art. 12, par. 1, NIS2.

In ogni caso **la decisione di ritardare e' del CSIRT, non del fabbricante**: il
fabbricante puo' chiederlo e fornire gli elementi. Non presentare il ritardo come un
diritto o come una proroga del termine di notifica: i termini dell'art. 14 restano.

### Passo 5 - Adempimenti paralleli da inserire nella timeline

- **Informazione agli utilizzatori (art. 14, par. 8)**: dovuta "dal momento in cui e'
  venuto a conoscenza", senza un termine numerico nel testo. Va nella timeline come
  adempimento parallelo, non successivo alla notifica. Ricorda la conseguenza prevista
  dal testo: se il fabbricante non informa tempestivamente, i CSIRT che hanno ricevuto la
  notifica possono informare direttamente gli utilizzatori. Se tecnicamente possibile,
  usa "un formato strutturato, leggibile da un dispositivo automatico".
- **Relazione intermedia (art. 14, par. 6)**: eventuale, solo su richiesta del CSIRT che
  ha ricevuto per primo la notifica. Nessun termine nel testo. Inseriscila come voce
  condizionale.
- **Segnalazione al manutentore del componente (art. 13, par. 6)**, se la vulnerabilita'
  e' in un componente di terzi o open source.

### Passo 6 - Canale e verifica di praticabilita'

Indica che le notifiche vanno trasmesse tramite la piattaforma unica di segnalazione
dell'art. 16, sul terminale del CSIRT coordinatore competente (vedi
`individua-csirt-coordinatore.md`), simultaneamente accessibili all'ENISA.

**Chiudi sempre con l'avvertenza sulla praticabilita' del canale**: l'art. 71, par. 2,
anticipa all'11 settembre 2026 il solo art. 14 e il capo IV, non l'art. 16. Lo stato
effettivo della piattaforma e del terminale nazionale va verificato su ENISA e
ACN/CSIRT Italia. Non presumere che il canale sia attivo e non indicare URL o modalita'
di accesso: le fonti lette non li contengono.

## Output

1. Timeline datata, per catena, con termine, formula del testo e decorrenza di ciascun
   adempimento; per la relazione finale sulle vulnerabilita', l'indicazione esplicita se
   il termine non e' ancora iniziato.
2. Per ogni adempimento, contenuto **dovuto** e contenuto **condizionato**, separati.
3. Elementi gia' coperti da adempimenti precedenti (clausola di non duplicazione).
4. Adempimenti paralleli e condizionali del Passo 5.
5. Nota sul grado di sensibilita' e su chi decide il ritardo.
6. Avvertenza sul canale e rinvio al responsabile della conformita'.

## Limiti

- Non redige il testo della notifica: struttura il contenuto minimo dovuto.
- Non conosce il formato: l'atto di esecuzione dell'art. 14, par. 10, e' una facolta'
  della Commissione, e questa skill non ha verificato ne' letto eventuali atti adottati
  in base a quel paragrafo.
- Non calcola termini in ore lavorative o giorni feriali: il testo indica ore, giorni e
  "un mese" senza qualificarli. Se la scadenza cade in un giorno non lavorativo,
  segnalalo come questione da porre al consulente, non risolverla.
- Non decide se la clausola "a meno che non siano gia' state fornite le informazioni
  pertinenti" esoneri in concreto.
