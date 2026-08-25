# Task: verificare i prerequisiti interni per essere in grado di adempiere all'art. 14

## Obiettivo

Verificare che il fabbricante disponga degli elementi organizzativi e tecnici senza i
quali le 24 ore dell'art. 14 non sono materialmente rispettabili, e distinguere cio' che
e' **obbligo di legge gia' applicabile** da cio' che e' **presupposto pratico** o obbligo
con decorrenza successiva.

Da usare in preparazione, prima che un evento si verifichi.

## Input richiesti

1. Il perimetro dei PDE del fabbricante (quali prodotti, quali componenti di terzi o open
   source).
2. Esiste un punto di contatto per la segnalazione delle vulnerabilita'? Dove e'
   pubblicato, chi lo presidia, con quale copertura oraria.
3. Esiste una politica di divulgazione coordinata delle vulnerabilita' (CVD)? E' scritta,
   pubblicata, applicata?
4. Esiste una SBOM? In che formato, con quale profondita', aggiornata con quale
   frequenza.
5. Come viene registrato il momento in cui una segnalazione arriva (ticket, mail, PSIRT,
   log)?
6. Chi ha l'autorita' di decidere che si notifica, e chi lo fa fuori orario.
7. Stabilimento principale e CSIRT coordinatore gia' individuati?

## Fonti

- `../references/estratti/cra-art14-obblighi-e-termini.md`, sezioni G, D, E, H.
- `../references/fonti/reg-ue-2024-2847-cra-segnalazione.md`, art. 13 par. 6, 7, 8, 17;
  allegato I parte II punti 1, 5, 6; art. 71 par. 2.
- `../references/estratti/csirt-coordinatore-e-canale-italiano.md`.

## Avvertenza sulla natura dei requisiti (da riportare sempre nell'output)

L'art. 71, par. 2, anticipa all'11 settembre 2026 il solo **art. 14** e il **capo IV**.
Gli obblighi organizzativi dell'**art. 13** e dell'**allegato I** non sono fra le
disposizioni anticipate e ricadono nella data generale dell'11 dicembre 2027.

Questo non li rende irrilevanti oggi, per una ragione operativa e non giuridica: chi non
ha un canale di ricezione delle segnalazioni, un registro del momento di arrivo e una
catena decisionale non e' materialmente in grado di rispettare un termine di 24 ore.
Presentali quindi come **prerequisiti pratici dell'art. 14 e obblighi con decorrenza
successiva**, mai come obblighi gia' esigibili. Non usare la data del 2027 per suggerire
di rinviare l'organizzazione.

## Procedura

Verifica una voce alla volta. Per ciascuna registra: presente / parziale / assente, la
fonte normativa, e la conseguenza pratica sull'art. 14.

### 1. Punto di contatto unico (art. 13, par. 17)

Il fabbricante deve disporre di un punto di contatto unico che consenta agli utilizzatori
di comunicare "direttamente e rapidamente", **anche per facilitare la segnalazione di
vulnerabilita'**. Deve essere facilmente identificabile e incluso nelle informazioni per
l'utilizzatore dell'allegato II.

Verifica: e' pubblicato dove l'utilizzatore lo trova? Chi lo legge? Con quale latenza?
Conseguenza sull'art. 14: se la segnalazione resta in una casella non presidiata, le 24
ore possono decorrere senza che nessuno se ne accorga.

### 2. Indirizzo di contatto per le vulnerabilita' (allegato I, parte II, punto 6)

Requisito distinto dal precedente: un **indirizzo di contatto** per la segnalazione delle
vulnerabilita' individuate nel prodotto. Verifica che esista e che sia raggiungibile da
un ricercatore esterno che non sia cliente.

### 3. Politica di divulgazione coordinata delle vulnerabilita' (art. 13, par. 8, ultimo comma; allegato I, parte II, punto 5)

Il testo richiede che la politica sia **messa in atto e applicata**, non solo scritta.
Verifica: e' pubblicata? definisce tempi di risposta? definisce chi decide la
divulgazione? e' coerente con l'obbligo di notifica dell'art. 14, che non e' derogabile
da un impegno di embargo preso con un ricercatore?

Segnala il punto di attrito: una policy che promette di non divulgare fino alla patch non
sospende i termini dell'art. 14 verso il CSIRT. Se la policy lascia intendere il
contrario, e' un rilievo.

### 4. SBOM (allegato I, parte II, punto 1)

Distinta base del software "in un formato di uso comune e leggibile da un dispositivo
automatico, che includa **almeno le dipendenze di primo livello** del prodotto".

Verifica: esiste, e' generata automaticamente in build, e' aggiornata a ogni release?
Conseguenza sull'art. 14: senza SBOM, stabilire in 24 ore se una vulnerabilita' di un
componente tocca il proprio prodotto e' impraticabile.

### 5. Gestione delle vulnerabilita' nei componenti (art. 13, par. 6)

Quando una vulnerabilita' e' individuata in un **componente**, compreso un componente
open source, il fabbricante la segnala a chi fabbrica o mantiene il componente e la
corregge conformemente all'allegato I, parte II. Verifica che esista un canale e un
responsabile per questa segnalazione a monte: e' un adempimento distinto dalla notifica
al CSIRT e non la sostituisce.

### 6. Documentazione sistematica (art. 13, par. 7)

Documentazione degli aspetti di cibersicurezza pertinenti, "comprese le vulnerabilita' di
cui vengono a conoscenza e qualsiasi informazione pertinente fornita da terzi".

Verifica: esiste un registro delle vulnerabilita' note? Registra **data e ora di
ricezione** e la fonte? Questo e' il punto piu' importante dell'intero check: e'
l'artefatto che documenta il momento da cui decorrono le 24 ore.

### 7. Catena decisionale e reperibilita' (nessun obbligo espresso nelle fonti)

Le fonti lette **non** impongono una procedura interna di escalation, un reperibile o un
tempo massimo di triage. Presentalo come raccomandazione organizzativa, non come
requisito normativo, e dillo esplicitamente.

Verifica comunque: chi decide che si notifica? Chi lo fa il sabato? Che cosa succede se
la segnalazione arriva il venerdi' sera?

### 8. Individuazione preventiva del CSIRT coordinatore

Non e' un obbligo autonomo, ma va fatto **prima** dell'evento: il par. 7 richiede di
sapere dove sono prevalentemente adottate le decisioni di cibersicurezza. Rinvia a
`individua-csirt-coordinatore.md`. Verifica anche lo stato operativo del terminale
nazionale e della piattaforma dell'art. 16 sui canali ENISA/ACN: le fonti normative non
lo descrivono.

### 9. Canale verso gli utilizzatori (art. 14, par. 8)

L'obbligo di informare gli utilizzatori e' **autonomo** rispetto alla notifica al CSIRT e
decorre "dal momento in cui e' venuto a conoscenza". Il testo indica, se del caso, "un
formato strutturato, leggibile da un dispositivo automatico".

Verifica: esiste una lista di contatto degli utilizzatori? Esiste un canale di advisory
(feed, pagina, formato automatico)? Ricorda la conseguenza prevista dal testo: se il
fabbricante non informa tempestivamente, i CSIRT che hanno ricevuto la notifica possono
informare direttamente gli utilizzatori.

### 10. Bozze predisposte

Non e' un requisito normativo ed e' opportuno dirlo. Verifica comunque se esistono
modelli interni per il preallarme e per la notifica delle 72 ore, coerenti col contenuto
minimo dei par. 2 e 4. Ricorda che il formato non e' fissato dal Regolamento: l'atto di
esecuzione dell'art. 14, par. 10, e' una facolta' della Commissione, e questa skill non
ha verificato ne' letto eventuali atti adottati in base a quel paragrafo. Verificarne
l'esistenza prima di congelare un modello.

## Output

1. Tabella delle dieci voci con esito (presente / parziale / assente) e riferimento
   normativo puntuale, distinguendo le voci 1-6 (obblighi con decorrenza 11 dicembre
   2027, prerequisiti pratici oggi) dalle voci 7 e 10 (raccomandazioni senza base nelle
   fonti lette) e dalle voci 8-9 (funzionali all'art. 14, gia' applicabile).
2. Le lacune che compromettono materialmente il rispetto delle 24 ore, in ordine di
   impatto, con la voce del registro degli arrivi (voce 6) in cima quando manca.
3. Punti di attrito rilevati fra policy CVD interna e obbligo di notifica.
4. Avvertenza sulle date di applicazione, integrale.
5. Rinvio al responsabile della conformita' per la validazione del piano.

## Limiti

- Non e' un audit di conformita' al CRA: non valuta i requisiti essenziali dell'allegato
  I, parte I, ne' la documentazione tecnica dell'allegato VII.
- Non definisce tempi di triage, SLA o livelli di reperibilita': le fonti lette non li
  contengono.
- Non fornisce modelli di politica CVD ne' template di notifica.
- Non verifica lo stato operativo della piattaforma dell'art. 16: e' una verifica di
  fatto sui canali ENISA/ACN.
