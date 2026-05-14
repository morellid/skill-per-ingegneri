# Task: Verifica ambito di applicazione e obbligo di adozione del PUMS

## Obiettivo

Determinare se l'ente che ha redatto (o sta redigendo) il PUMS rientra nell'obbligo di adozione previsto dalle Linee guida italiane (art. 3 c.1 del DM 397/2017, sostituito dal DM 396/2019 art. 4 e poi dal DM 29/2021 art. 1 c.2, con il termine finale fissato dal DM 444/2021 art. 1). Determinare inoltre se il PUMS e' richiesto come condizione di accesso ai finanziamenti statali per nuovi interventi di trasporto rapido di massa (TRM) e mobilita' ciclistica (art. 1 c.2 DM 397/2017 nel testo da ultimo sostituito dal DM 444/2021 art. 2 c.1).

## Input richiesti

Chiedere all'utente:
1. Tipologia di ente: citta' metropolitana, comune, associazione di comuni, ente di area vasta (provincia), altro.
2. Popolazione di riferimento (residenti al 31/12 dell'ultimo anno disponibile).
3. Se il comune e' ricompreso o meno nel territorio di una citta' metropolitana; se e' capoluogo di citta' metropolitana.
4. Motivazione redazione: obbligo da normativa, accesso a finanziamenti TRM o mobilita' ciclistica, scelta volontaria.
5. Se esiste un PUMS della citta' metropolitana (per comuni ricompresi).
6. Data dell'atto formale di adozione del PUMS (anche se solo di Giunta) e successivo atto di approvazione (Consiglio), se disponibili.

## Fonti

- references/estratti/dm-4-8-2017-397-pums.md (sezioni "Ambito e finalita' (Art. 1)" e "Soggetti destinatari e ambito (Art. 3)").
- references/estratti/dm-28-8-2019-396-pums.md (sezioni "Art. 2" e "Art. 3"; per l'art. 7 c.3 vedi nota di abrogazione nell'estratto DM 444/2021).
- references/estratti/dm-26-1-2021-29-pums.md (riformulazione dell'art. 3 c.1 DM 397/2017 in vigore tra il DM 29/2021 e il DM 444/2021).
- references/estratti/dm-12-11-2021-444-pums.md (termine unitario 1 gennaio 2023; nuovo testo dell'art. 1 c.2 DM 397/2017; criterio premiale 2022; abrogazione art. 7 c.3 DM 396/2019; piattaforma Osservatorio TPL).

## Procedura

Eseguire i seguenti check, registrando per ognuno ESITO {CONFORME / NON CONFORME / NON DETERMINABILE / NON APPLICABILE} e una motivazione testuale.

1. **Ente soggetto all'obbligo (art. 3 c.1 DM 397/2017 nel testo vigente)**:
   - Citta' metropolitana => SI obbligo.
   - Comune con popolazione > 100.000 abitanti => SI obbligo.
   - Associazione di comuni con popolazione cumulativa > 100.000 abitanti => SI obbligo.
   - Ente di area vasta non citta' metropolitana (provincia) => NO obbligo (DM 396/2019 art. 3: l'art. 3 c.1 DM 397/2017 non si applica).
   - Comune con popolazione minore o uguale a 100.000 abitanti => NO obbligo (eventuale adesione volontaria valida ma non vincolata alle Linee guida ai fini sanzionatori).

2. **Gate di accesso ai finanziamenti TRM e mobilita' ciclistica (art. 1 c.2 DM 397/2017 nel testo sostituito dal DM 444/2021 art. 2 c.1)**:
   - Per le risorse statali stanziate **a decorrere dal 1 gennaio 2023** per nuovi interventi per il trasporto rapido di massa **e la mobilita' ciclistica**, condizione di accesso e' l'**adozione** del PUMS.
   - Per i comuni > 100.000 ab. ricompresi in citta' metropolitana e per i capoluoghi di citta' metropolitana: condizione assolta dall'adozione del PUMS della citta' metropolitana (anche se non hanno proprio PUMS).
   - Comune > 100.000 ab. non ricompreso in citta' metropolitana: occorre l'adozione del **proprio** PUMS.
   - Citta' metropolitana: occorre l'adozione del proprio PUMS.
   - **Per il gate dell'art. 1 c.2 DM 397/2017 (nuovo testo)** rileva la sola **adozione** del PUMS (atto di Giunta in genere): l'art. 1 c.2 non richiede l'approvazione di Consiglio ne' la piena conformita' procedurale e di merito come condizione di accesso. Eventuali difformita' di merito (procedura, obiettivi, indicatori, monitoraggio) costituiscono questioni di **conformita' generale** del PUMS, da rilevare separatamente nelle altre sotto-attivita' della skill, e possono incidere sui controlli a valle dell'amministrazione erogante ma non sul gate dell'art. 1 c.2.

3. **Criterio premiale 2022 (art. 2 c.2 DM 444/2021)**:
   - Per le risorse destinate ai nuovi interventi TRM e mobilita' ciclistica assegnati dal MIMS **dal 1 gennaio 2022 al 31 dicembre 2022** l'adozione del PUMS opera come **criterio premiale** nel riparto, non come condizione di accesso.
   - Verificare se l'istanza dell'ente ricade nel periodo: in caso affermativo, segnalare il regime di premialita' (non bloccante) anziche' il gate di accesso vero e proprio.

4. **Termine di adozione (art. 3 c.1 DM 397/2017 nel testo da ultimo sostituito dal DM 444/2021 art. 1)**:
   - Termine unitario vigente: **1 gennaio 2023**.
   - PUMS adottato entro tale termine => CONFORME sul termine.
   - PUMS adottato dopo => registrare la posizione tardiva. Non e' di per se' causa di invalidita' del PUMS, ma puo' avere effetti sulla graduatoria di finanziamenti TRM/ciclistica (vedi punto 2) e sull'eventuale richiamo dell'amministrazione erogante.
   - Termini storici (24 mesi DM 397/2017, 36 mesi DM 396/2019, 4 aprile / 4 agosto 2021 DM 29/2021): da usare solo per ricostruzioni storiche; non rilevanti per validazione di PUMS adottati dal 2022 in poi.

5. **Verifica piattaforma Osservatorio TPL (art. 3 DM 444/2021)**:
   - L'art. 3 affida la verifica di quanto previsto dall'art. 2 e dell'ottemperanza all'art. 4 c.2 del DM 397/2017 alla piattaforma dell'Osservatorio nazionale delle politiche del trasporto pubblico locale.
   - Verificare se il PUMS e' stato registrato/aggiornato sulla piattaforma. Esito NON DETERMINABILE se l'utente non fornisce informazioni. Non bloccante per la conformita' del documento PUMS in se' (il documento puo' essere conforme anche senza registrazione), ma rilevante per il gate finanziamento.

6. **Regime transitorio TRM (art. 7 c.3 DM 396/2019)**: **ABROGATO** dall'art. 4 del DM 444/2021. Per istanze successive al 12 novembre 2021 la clausola transitoria (con primo rapporto contenente quadro conoscitivo e obiettivi, atto della Giunta/Sindaco, cronoprogramma) **non e' invocabile**. Se l'utente cita questa clausola, segnalarne l'abrogazione e indirizzare l'analisi sul gate vigente (punto 2). Per istanze pregresse alla data di abrogazione, eventuale applicazione storica rinvio all'amministrazione erogante.

## Output

Report con:
- Riepilogo dell'inquadramento (ente, popolazione, ricomprensione in citta' metropolitana).
- Esito 1: ente soggetto all'obbligo SI/NO + motivazione.
- Esito 2: gate finanziamenti TRM/ciclistica - condizione di adozione SI/NO + motivazione (e quale soggetto e' tenuto all'adozione).
- Esito 3: criterio premiale 2022 applicabile SI/NO + motivazione (se la cronologia delle istanze lo richiede).
- Esito 4: rispetto del termine 1 gennaio 2023 + eventuali criticita'.
- Esito 5: verifica piattaforma Osservatorio TPL (CONFORME / NON CONFORME / NON DETERMINABILE) + motivazione.
- Esito 6: rilievi su eventuali richiami a clausole abrogate (art. 7 c.3 DM 396/2019).
- Rilievi BLOCCANTI / NON BLOCCANTI / NON DETERMINABILI.
- Rinvio finale al professionista firmatario per la verifica diretta delle fonti e dell'eventuale avviso di finanziamento specifico.

## Limiti

- Non valuta la conformita' della specifica istanza di finanziamento ad avvisi pubblici (ciascun avviso TRM o mobilita' ciclistica puo' avere requisiti aggiuntivi).
- Non interpreta deroghe regionali o leggi regionali integrative.
- Non valuta l'eventuale conflitto con norme statutarie dell'ente.
- Il gate dell'art. 1 c.2 DM 397/2017 (nuovo testo) si esprime in termini di "adozione" del PUMS: la conformita' generale del PUMS (procedura, indicatori, monitoraggio) e' oggetto delle altre sotto-attivita' della skill e di valutazione separata dell'amministrazione erogante.
