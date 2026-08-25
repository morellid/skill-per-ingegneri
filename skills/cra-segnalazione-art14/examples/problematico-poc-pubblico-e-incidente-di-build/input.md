# Input: PoC pubblico su un componente e ransomware sul server di build

## Il fabbricante

- **Alpina Controls AG**, societa' svizzera, 8 dipendenti e fatturato annuo di circa
  1,4 milioni di euro. Non ha stabilimenti nell'Unione.
- Produce controllori per impianti di building automation (modello BC-10, firmware
  proprietario che integra una libreria open source di parsing MQTT).
- Nell'Unione si avvale di: un **rappresentante autorizzato in Irlanda** (agisce per
  tutti i prodotti del fabbricante), un **importatore in Germania**, un **distributore in
  Italia**. Circa il 70% degli utilizzatori finali e' in Italia.
- Non ha un PSIRT. Le segnalazioni arrivano a `info@` e vengono lette in orario
  d'ufficio. Non esiste un registro delle vulnerabilita' note. Non esiste una politica di
  divulgazione coordinata. La SBOM non e' prodotta.

## I due eventi

### Evento A - PoC pubblico su un componente

- **Lunedi' 28 settembre 2026**: viene pubblicata una CVE con punteggio CVSS 9.8 sulla
  libreria MQTT open source integrata nel firmware BC-10, insieme a un proof-of-concept
  funzionante su GitHub.
- **Giovedi' 1 ottobre 2026**: la CVE viene inserita in un catalogo pubblico di
  vulnerabilita' "note per essere sfruttate".
- Il fabbricante verifica che il BC-10 usa la versione vulnerabile della libreria. Non ha
  alcuna evidenza di sfruttamento su propri dispositivi: nessun log anomalo, nessuna
  segnalazione di clienti, nessun IoC.
- La patch della libreria upstream esiste; il fabbricante stima due settimane per
  integrarla e rilasciare il firmware.

### Evento B - Ransomware sul server di build

- **Venerdi' 2 ottobre 2026, ore 16:40**: il fornitore IT comunica al titolare che il
  server di build e' stato cifrato da un ransomware. Il server ospitava la pipeline di
  compilazione del firmware BC-10 e la chiave privata usata per firmare gli
  aggiornamenti. Non e' possibile escludere l'esfiltrazione della chiave.
- Il fabbricante considera l'evento "un problema informatico interno, non del prodotto",
  perche' nessun dispositivo in campo risulta malfunzionante.

## Le convinzioni del fabbricante, da verificare

1. "L'evento A e' una vulnerabilita' attivamente sfruttata: e' in un catalogo di
   vulnerabilita' sfruttate e c'e' un exploit pubblico. Notifichiamo appena avremo la
   patch, tra due settimane."
2. "L'evento B non riguarda il CRA: e' l'infrastruttura aziendale, non il prodotto."
3. "Siamo una microimpresa, quindi l'art. 64, paragrafo 10, ci esonera dalle sanzioni:
   possiamo prenderci il tempo necessario."
4. "Notifichiamo al CSIRT italiano, visto che i clienti sono quasi tutti in Italia."
5. "Meglio non notificare finche' non abbiamo capito bene: una notifica ci espone."
6. "Abbiamo gia' notificato l'incidente ransomware alla nostra autorita' nazionale; questo
   copre anche il CRA."

## Domanda all'agent

Per ciascuno dei due eventi: scatta l'obbligo dell'art. 14? Entro quando? A chi? E le sei
convinzioni sopra sono corrette?
