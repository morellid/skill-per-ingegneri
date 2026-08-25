# Task: qualificare l'evento e stabilire se scatta l'obbligo dell'art. 14

## Obiettivo

Stabilire se un evento noto al fabbricante integra (a) una **vulnerabilita' attivamente
sfruttata**, (b) un **incidente grave** che ha impatto sulla sicurezza del PDE,
(c) entrambi, oppure (d) nessuno dei due - e fissare il **momento iniziale** da cui
decorrono i termini.

## Input richiesti

Chiedi all'utente, e non assumere:

1. **Il prodotto**: e' un prodotto software o hardware, o una soluzione di elaborazione
   dati da remoto ad esso relativa? E' commercializzato dal soggetto con il proprio nome
   o marchio? (art. 3, punti 1 e 13)
2. **Descrizione dell'evento**: che cosa e' successo o e' stato scoperto.
3. **Fonte della notizia**: ricerca interna, segnalazione di terzi, comunicazione di un
   CSIRT, threat intelligence, incidente su un cliente.
4. **Data e ora** in cui la notizia e' arrivata al fabbricante, e **a chi**.
5. **Prove disponibili** di sfruttamento effettivo: log, IoC, campioni, report di
   incident response, evidenze di terze parti.
6. **Effetti osservati o potenziali** su disponibilita', autenticita', integrita',
   riservatezza di dati o funzioni; esecuzione o introduzione di codice maligno.
7. Se il componente affetto e' **di terzi o open source** integrato nel prodotto.

## Fonti

- `../references/estratti/cra-art14-obblighi-e-termini.md`, sezioni A e B.
- `../references/fonti/reg-ue-2024-2847-cra-segnalazione.md`, art. 3 punti 40, 42, 43, 45;
  art. 14 par. 1, 3, 5.
- `../references/fonti/dir-ue-2022-2555-nis2-segnalazione.md`, art. 6 punti 5 e 6.

## Procedura

### Passo 1 - Verifica preliminare: il soggetto e' un fabbricante di PDE?

L'art. 14 si rivolge al **fabbricante**. Se il soggetto e' importatore, distributore o
rappresentante autorizzato, l'obbligo dell'art. 14 non gli e' rivolto dal testo letto.
Segnalalo e fermati: l'inquadramento del suo ruolo esula da questa skill.

Se il prodotto non e' un PDE ai sensi dell'art. 3, punto 1, l'art. 14 non si applica.
Per i casi di confine (esclusioni settoriali, ambito dell'art. 2) rinvia a
`cra-classificazione-pde`.

### Passo 2 - Test "vulnerabilita' attivamente sfruttata"

Applica la definizione dell'art. 3, punto 42, elemento per elemento. **Entrambi** devono
ricorrere:

| Elemento | Domanda | Nota |
|---|---|---|
| Prove attendibili di sfruttamento | Esistono prove attendibili che un soggetto malintenzionato **l'ha sfruttata in un sistema**? | Il testo richiede lo sfruttamento avvenuto, non la sfruttabilita' |
| Assenza di autorizzazione | Lo sfruttamento e' avvenuto **senza l'autorizzazione del proprietario del sistema**? | Esclude penetration test e bug bounty autorizzati sul sistema del proprietario |

Non integrano di per se' il presupposto, in mancanza di prove di sfruttamento effettivo:

- una vulnerabilita' con CVSS elevato ma non sfruttata;
- la pubblicazione di un proof-of-concept o di un exploit;
- l'inserimento in una lista di vulnerabilita' "note" o "probabilmente sfruttate";
- una scansione o un tentativo fallito.

Questo **non** significa che l'obbligo sia escluso: significa che il presupposto della
notifica **obbligatoria** ex art. 14, par. 1, non risulta dimostrato. Verifica il Passo 3
e considera l'art. 15.

### Passo 3 - Test "incidente grave"

Due livelli, in sequenza.

**3.1 - E' un incidente?** Definizione dell'art. 6, punto 6, NIS2 richiamata dall'art. 3,
punto 43, CRA: un evento che **compromette** disponibilita', autenticita', integrita' o
riservatezza di dati conservati, trasmessi o elaborati, o dei servizi offerti dai sistemi
informatici e di rete o accessibili attraverso di essi.

Se l'evento e' stato "efficacemente evitato" o "non si e' verificato", e' un **quasi
incidente** (art. 6, punto 5, NIS2): l'art. 14 non si applica; resta l'art. 15, par. 2
(volontaria).

**3.2 - E' grave?** Art. 14, par. 5 - basta **una** delle due lettere:

- **lett. a)**: incide negativamente **o e' in grado di incidere negativamente** sulla
  capacita' del PDE di proteggere disponibilita', autenticita', integrita' o riservatezza
  di **dati o funzioni sensibili o importanti**;
- **lett. b)**: ha portato **o e' in grado di portare** all'introduzione o all'esecuzione
  di **codice maligno** nel PDE o nei sistemi informativi e di rete di un utilizzatore.

Nota le due estensioni al **potenziale**: "e' in grado di incidere", "e' in grado di
portare". La gravita' non richiede che il danno si sia realizzato.

Nota anche che l'incidente deve avere **impatto sulla sicurezza del PDE** (art. 14,
par. 3): un incidente che colpisce l'infrastruttura aziendale del fabbricante senza
toccare la sicurezza del prodotto non e' inquadrato dal par. 3. Se pero' l'incidente ha
compromesso, ad esempio, la catena di build o la firma degli aggiornamenti, l'impatto sul
prodotto va valutato, non escluso per collocazione dell'evento.

### Passo 4 - Fissa il momento iniziale

E' il dato piu' importante dell'intero task, perche' da esso decorrono le 24 ore.

Il Regolamento **non definisce** "venire a conoscenza": non dice chi in azienda debba
saperlo, ne' come si documenti. Quindi:

- registra **data e ora** in cui l'informazione e' pervenuta al fabbricante, con la fonte
  e il destinatario interno;
- se la notizia e' arrivata tramite un CSIRT ai sensi dell'art. 15, par. 4 (segnalazione
  di un terzo), quel momento e' documentato dalla comunicazione ricevuta;
- se la conoscenza si e' formata progressivamente (prima un sospetto, poi la conferma),
  esponi entrambe le date e le evidenze, e **non scegliere tu** quale sia il momento
  rilevante: presenta la questione al responsabile della conformita', segnalando che la
  ricostruzione piu' prudente e' la data piu' remota.

### Passo 5 - Concludi, senza chiudere i dubbi a favore del non obbligo

Combina i risultati:

| Esito Passo 2 | Esito Passo 3 | Conseguenza |
|---|---|---|
| Positivo | Positivo | Due obblighi distinti e paralleli: art. 14 par. 1-2 **e** par. 3-4 |
| Positivo | Negativo | Solo la catena della vulnerabilita' (par. 2) |
| Negativo | Positivo | Solo la catena dell'incidente (par. 4) |
| Negativo | Negativo | Nessun obbligo di notifica ex art. 14 sulla base degli elementi forniti |

Se anche un solo elemento e' incerto, l'output **non deve** concludere per l'assenza
dell'obbligo. Deve dire quale elemento manca, quale prova lo dimostrerebbe, e ricordare
che l'art. 15 consente la segnalazione volontaria e che l'art. 17, par. 4, esclude che la
sola notifica comporti maggiore responsabilita'.

### Passo 6 - Adempimenti che non dipendono dalla notifica al CSIRT

Due obblighi vanno ricordati perche' non presuppongono che la notifica sia stata
trasmessa. Attenzione pero' al presupposto di ciascuno, che non e' lo stesso:

- **art. 14, par. 8**: si applica "dal momento in cui e' venuto a conoscenza di una
  vulnerabilita' attivamente sfruttata o di un incidente grave" - lo stesso presupposto
  della notifica. Se il test del Passo 3 o del Passo 4 e' positivo, il fabbricante deve
  informare gli utilizzatori interessati (e, se del caso, tutti gli utilizzatori) della
  vulnerabilita' o dell'incidente e delle misure adottabili: obbligo **autonomo rispetto
  alla notifica al CSIRT**, non subordinato al suo invio. Se il presupposto non ricorre,
  il par. 8 non si applica; informare comunque i clienti puo' essere opportuno, ma va
  presentato come scelta del fabbricante, non come obbligo dell'art. 14.
- **art. 13, par. 6**: se la vulnerabilita' e' in un **componente** di terzi o open
  source, segnalarla a chi fabbrica o mantiene il componente. Segnala pero' anche che
  l'art. 13 non e' fra le disposizioni anticipate dall'art. 71, par. 2.

## Output

Un inquadramento strutturato con:

1. Qualificazione del soggetto e del prodotto (fabbricante? PDE?).
2. Esito del test "vulnerabilita' attivamente sfruttata", elemento per elemento, con
   l'evidenza a supporto o l'evidenza mancante.
3. Esito del test "incidente" e del test "gravita'", lettera per lettera.
4. **Momento iniziale** proposto, con la fonte che lo documenta e le eventuali date
   alternative.
5. Conclusione secondo la tabella del Passo 5, con i dubbi esposti e non risolti a favore
   del non obbligo.
6. Adempimenti del Passo 6.
7. Rinvio al task `costruisci-sequenza-notifiche.md` se almeno un obbligo scatta.

## Limiti

- Non stabilisce quando la conoscenza si sia "formata" in senso giuridico: il testo tace
  e la ricostruzione e' un accertamento di fatto del fabbricante.
- Non valuta l'attendibilita' tecnica delle prove di sfruttamento: e' lavoro di analisi
  forense/threat intelligence.
- Non copre le esclusioni dall'ambito del CRA (art. 2): usa `cra-classificazione-pde`.
