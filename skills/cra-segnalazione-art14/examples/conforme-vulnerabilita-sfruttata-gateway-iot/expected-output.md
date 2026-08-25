# Output atteso: gateway IoT IG-400 - inquadramento art. 14 CRA

## 1. Qualificazione

**Soggetto**: fabbricante ai sensi dell'art. 3, punto 13, CRA (commercializza il prodotto
con il proprio marchio). **Prodotto**: PDE ai sensi dell'art. 3, punto 1.

### 1.1 Vulnerabilita' attivamente sfruttata - SI'

Art. 3, punto 42: servono due elementi cumulativi.

| Elemento | Esito | Evidenza |
|---|---|---|
| Prove attendibili di sfruttamento gia' avvenuto | Soddisfatto | Report di incident response del cliente, log delle richieste di bypass, web shell caricato, traffico verso IP noto |
| Assenza di autorizzazione del proprietario del sistema | Soddisfatto | Il cliente dichiara di non aver autorizzato alcun test |

Non e' un caso di sola sfruttabilita' teorica: lo sfruttamento e' documentato su sistemi
in esercizio. Scatta l'obbligo dell'art. 14, par. 1.

### 1.2 Incidente grave - SI', obbligo distinto e parallelo

Due livelli.

- **E' un incidente?** Si': art. 6, punto 6, dir. (UE) 2022/2555, richiamato dall'art. 3,
  punto 43, CRA - la compromissione dei due gateway ha inciso su integrita' e
  riservatezza dei dati e dei servizi. Non e' un "quasi incidente" (art. 6, punto 5,
  NIS2): l'evento si e' verificato.
- **E' grave?** Si', per **entrambe** le lettere dell'art. 14, par. 5: lett. a) - ha
  inciso negativamente sulla capacita' del prodotto di proteggere integrita' e
  riservatezza; lett. b) - ha portato all'esecuzione di codice maligno nel PDE.
  Basterebbe una sola delle due.

**Conseguenza**: due obblighi distinti e paralleli, art. 14, par. 1-2 **e** par. 3-4. Non
si sommano in un'unica notifica: hanno contenuti minimi e relazioni finali diverse, e
vanno tracciati separatamente.

### 1.3 Momento iniziale

**Lunedi' 14 settembre 2026, ore 09:20** - apertura del ticket con il report allegato.

Il Regolamento non definisce "venire a conoscenza". La ricostruzione piu' prudente e la
data piu' remota documentata: qui e' l'arrivo del ticket, non la riproduzione in
laboratorio delle 13:00. La riproduzione conferma la vulnerabilita', non fonda la
conoscenza. Documentare in registro data, ora, mittente e destinatario interno.

## 2. Catena vulnerabilita' attivamente sfruttata (art. 14, par. 2)

| Adempimento | Termine | Scadenza | Base |
|---|---|---|---|
| a) Preallarme | senza indebito ritardo, in ogni caso entro 24 ore dalla conoscenza | **martedi' 15 settembre 2026, 09:20** | par. 2, lett. a) |
| b) Notifica della vulnerabilita' | senza indebito ritardo, in ogni caso entro 72 ore dalla conoscenza | **giovedi' 17 settembre 2026, 09:20** | par. 2, lett. b) |
| c) Relazione finale | entro 14 giorni dalla messa a disposizione della misura correttiva | **mercoledi' 30 settembre 2026, 18:00** (firmware 3.4.2 rilasciato il 16/09 alle 18:00) | par. 2, lett. c) |

"Entro 24 ore" e "entro 72 ore" sono limiti massimi preceduti da "senza indebito
ritardo": non sono un obiettivo da avvicinare.

### Contenuto minimo

**Preallarme (lett. a)**
- Condizionato ("se del caso"): Stati membri sul cui territorio il fabbricante sa che il
  prodotto e' stato messo a disposizione - qui Italia, Germania, Spagna, Polonia.
- Il testo non richiede altro. Il preallarme non deve attendere l'analisi completa.

**Notifica 72h (lett. b)**
- Se disponibili: informazioni generali sul PDE interessato (IG-400, firmware 3.2.0-3.4.1).
- Dovuto: natura generale dello sfruttamento (bypass di autenticazione sull'interfaccia
  web, caricamento ed esecuzione di web shell) e della vulnerabilita'.
- Dovuto: misure correttive o di attenuazione adottate (firmware 3.4.2) e misure
  adottabili dagli utilizzatori (aggiornamento; workaround di disabilitazione
  dell'interfaccia web da WAN).
- Se del caso: grado di sensibilita' attribuito alle informazioni notificate. Da decidere
  prima dell'invio: e' il presupposto che l'art. 16, par. 2, secondo comma, richiama per
  l'eventuale ritardo nella diffusione agli altri CSIRT. La decisione di ritardare resta
  del CSIRT, non del fabbricante, e non proroga i termini dell'art. 14.

**Relazione finale (lett. c)** - comprende almeno:
1. descrizione della vulnerabilita', compresi gravita' e impatto (parco stimato ~3.100
   dispositivi con firmware vulnerabile);
2. se disponibili, informazioni sul soggetto malintenzionato - qui l'attore non e'
   identificato: riportare gli IoC disponibili e dichiarare che l'attribuzione non e'
   stata possibile, senza ipotesi;
3. informazioni dettagliate sull'aggiornamento di sicurezza (3.4.2) e sulle altre misure
   correttive messe a disposizione.

## 3. Catena incidente grave (art. 14, par. 4)

| Adempimento | Termine | Scadenza | Base |
|---|---|---|---|
| a) Preallarme | entro 24 ore dalla conoscenza | **15 settembre 2026, 09:20** | par. 4, lett. a) |
| b) Notifica dell'incidente | entro 72 ore dalla conoscenza | **17 settembre 2026, 09:20** | par. 4, lett. b) |
| c) Relazione finale | entro **un mese** dalla **trasmissione** della notifica b) | se b) e' trasmessa il 16 settembre 2026, scade il **16 ottobre 2026** | par. 4, lett. c) |

Il termine e' "un mese", non "30 giorni", e decorre dalla trasmissione effettiva della
notifica delle 72 ore, non dalla sua scadenza: anticipare l'invio anticipa anche la
relazione finale.

### Contenuto minimo

**Preallarme (lett. a)**: dovuto **come minimo** precisare se si sospetta che l'incidente
sia il risultato di **atti illegittimi o malevoli** - qui si', con gli elementi
disponibili. Se del caso, gli Stati membri di messa a disposizione.

**Notifica 72h (lett. b)**: se disponibili, informazioni generali sulla natura
dell'incidente; **valutazione iniziale** dell'incidente; misure correttive o di
attenuazione adottate e adottabili dagli utilizzatori; se del caso, grado di sensibilita'.

**Relazione finale (lett. c)** - comprende almeno: descrizione dettagliata dell'incidente
con gravita' e impatto; tipo di minaccia o causa di fondo che ha probabilmente innescato
l'incidente (bypass di autenticazione nell'interfaccia web esposta); misure di
attenuazione adottate e in corso.

### Clausola di non duplicazione

Le lettere b) e c) di entrambi i paragrafi sono precedute da "a meno che non siano gia'
state fornite le informazioni pertinenti". Poiche' le due catene condividono descrizione
del prodotto, IoC e misure correttive, verificare quali elementi risultano gia' veicolati
prima di ripeterli. La clausola esonera dal ripetere le informazioni gia' fornite, non
dagli adempimenti quando restano informazioni nuove: qui la valutazione iniziale
dell'incidente e la causa di fondo sono contenuti propri della catena par. 4.

## 4. Destinatari e canale

- **Stabilimento principale**: Italia. Criterio dell'art. 14, par. 7, secondo comma - lo
  Stato membro in cui sono prevalentemente adottate le decisioni relative alla
  cibersicurezza dei prodotti. Qui il team di product security e' a Milano; il criterio
  non e' la sede legale, ma nel caso coincidono. Non occorre scendere al criterio
  sussidiario del maggior numero di dipendenti, ne' alla cascata del terzo comma.
- **CSIRT coordinatore**: **CSIRT Italia**, designato coordinatore dall'art. 16, comma 1,
  del D.Lgs. 138/2024 ai sensi dell'art. 12 della dir. (UE) 2022/2555, operante
  all'interno dell'**ACN** (art. 2, comma 1, lett. i), stesso decreto).
- **ENISA**: destinataria **simultanea** (art. 14, par. 1 e 3). Le notifiche trasmesse sul
  terminale del CSIRT competente sono contemporaneamente accessibili all'ENISA.

**Avvertenza sul canale**: l'art. 14, par. 1 e 3, rinvia alla piattaforma unica di
segnalazione dell'art. 16, che **non e' fra le disposizioni anticipate** dall'art. 71,
par. 2, all'11 settembre 2026. Nessuna delle fonti lette descrive il terminale italiano,
l'URL o le modalita' di accreditamento. Verificare lo stato operativo e le modalita' di
invio sui canali ufficiali ACN/CSIRT Italia ed ENISA **prima** della scadenza delle 24
ore, non dopo.

## 5. Obblighi paralleli

- **Informazione agli utilizzatori (art. 14, par. 8)**: dovuta "dal momento in cui e'
  venuto a conoscenza", senza termine numerico nel testo, e **autonoma** rispetto alla
  notifica al CSIRT. Riguarda gli utilizzatori interessati e, se del caso, tutti gli
  utilizzatori: qui l'intero parco IG-400 con firmware 3.2.0-3.4.1, non i soli due clienti
  compromessi. Contenuto: la vulnerabilita' o l'incidente e, se necessario, le
  attenuazioni e misure correttive adottabili. Se del caso, in un formato strutturato,
  leggibile da un dispositivo automatico. Se il fabbricante non informa tempestivamente, i
  CSIRT che hanno ricevuto la notifica possono informare direttamente gli utilizzatori.
- **Relazione intermedia (art. 14, par. 6)**: eventuale, solo se richiesta dal CSIRT
  coordinatore che ha ricevuto per primo la notifica. Nessun termine nel testo.
- **Componenti di terzi (art. 13, par. 6)**: non risulta che il bypass sia in un
  componente di terzi o open source. Se l'analisi lo rivelasse, si aggiungerebbe la
  segnalazione a chi fabbrica o mantiene il componente. Nota che l'art. 13 non e' fra le
  disposizioni anticipate dall'art. 71, par. 2.

## 6. Punti da portare al responsabile della conformita'

- Conferma del momento iniziale (14/09 ore 09:20) e sua tracciabilita' documentale.
- Decisione sul grado di sensibilita' prima della notifica delle 72 ore.
- Verifica dello stato operativo del terminale nazionale e della piattaforma dell'art. 16.
- Perimetro dell'informazione agli utilizzatori (tutti i clienti IG-400 o i soli
  interessati).

## Disclaimer

Questo inquadramento e' uno strumento di supporto: non sostituisce il giudizio del
responsabile della conformita' del fabbricante ne' la consulenza legale. La decisione di
notificare e la responsabilita' della notifica restano interamente del fabbricante.
Nessuna notifica e' stata trasmessa da questa analisi.
