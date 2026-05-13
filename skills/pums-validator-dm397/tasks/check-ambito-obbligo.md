# Task: Verifica ambito di applicazione e obbligo di adozione del PUMS

## Obiettivo

Determinare se l'ente che ha redatto (o sta redigendo) il PUMS rientra nell'obbligo di adozione previsto dalle Linee guida italiane (DM 397/2017 art. 3 c.1, come modificato dal DM 396/2019). Determinare inoltre se il PUMS e' richiesto come condizione di accesso ai finanziamenti statali TRM (art. 1 c.2 DM 397/2017 + art. 2 DM 396/2019).

## Input richiesti

Chiedere all'utente:
1. Tipologia di ente: citta' metropolitana, comune, associazione di comuni, ente di area vasta (provincia), altro.
2. Popolazione di riferimento (residenti al 31/12 dell'ultimo anno disponibile).
3. Se il comune e' ricompreso o meno nel territorio di una citta' metropolitana; se e' capoluogo di citta' metropolitana.
4. Motivazione redazione: obbligo da normativa, accesso a finanziamenti TRM o ciclistici, scelta volontaria.
5. Se esiste un PUMS della citta' metropolitana (per comuni ricompresi).

## Fonti

- references/estratti/dm-4-8-2017-397-pums.md (sezioni "Ambito e finalita' (Art. 1)" e "Soggetti destinatari e ambito (Art. 3)").
- references/estratti/dm-28-8-2019-396-pums.md (sezioni "Art. 2" e "Art. 3").

## Procedura

Eseguire i seguenti check, registrando per ognuno ESITO {CONFORME / NON CONFORME / NON DETERMINABILE / NON APPLICABILE} e una motivazione testuale.

1. **Ente soggetto all'obbligo (art. 3 c.1 DM 397/2017 s.m.i.)**:
   - Citta' metropolitana => SI obbligo.
   - Comune con popolazione > 100.000 abitanti => SI obbligo.
   - Associazione di comuni con popolazione cumulativa > 100.000 abitanti => SI obbligo.
   - Ente di area vasta non citta' metropolitana (provincia) => NO obbligo (art. 3 DM 396/2019: art. 3 c.1 DM 397/2017 NON si applica).
   - Comune con popolazione minore o uguale a 100.000 abitanti => NO obbligo (eventuale adesione volontaria valida ma non vincolata alle Linee guida ai fini sanzionatori).

2. **Accesso a finanziamenti TRM (art. 1 c.2 DM 397/2017 + art. 2 DM 396/2019)**:
   - Comune con popolazione > 100.000 abitanti ricompreso in citta' metropolitana => condizione assolta se la citta' metropolitana ha adottato il PUMS (anche se non capoluogo, l'adozione del PUMS della citta' metropolitana copre).
   - Comune capoluogo di citta' metropolitana => idem (assolto se la citta' metropolitana ha adottato il PUMS).
   - Comune con popolazione > 100.000 abitanti NON ricompreso in citta' metropolitana => obbligo di adozione del proprio PUMS.
   - Citta' metropolitana => obbligo di adozione del proprio PUMS.

3. **Termine di adozione (art. 3 c.1 DM 397/2017 prorogato art. 4 DM 396/2019)**:
   - Termine originario: 24 mesi dall'entrata in vigore del DM 397/2017.
   - Termine prorogato: 24 + 12 = 36 mesi.
   - Verificare se il PUMS e' stato adottato entro tale termine; se no, registrare la posizione tardiva (puo' non essere bloccante ma ha effetti sui finanziamenti TRM, vedi art. 7 c.3 DM 396/2019).

4. **Regime transitorio per i finanziamenti TRM (art. 7 DM 396/2019)**: applicabile solo se l'istanza e' stata presentata nel periodo previsto. Se l'ente ha presentato istanze in regime transitorio, verificare la presenza di:
   - atto della Giunta (comune) o del Sindaco (citta' metropolitana / capoluogo) che approva il primo rapporto PUMS,
   - quadro conoscitivo e obiettivi del primo rapporto,
   - rispetto del cronoprogramma tipo allegato al DM 397/2017.

5. **PUMS adottati prima del DM 397/2017 (art. 7 c.3 secondo periodo DM 396/2019)**: aggiornamento in linea con i criteri del DM 397/2017 = requisito soddisfatto.

## Output

Report con:
- Riepilogo dell'inquadramento (ente, popolazione, ricomprensione in citta' metropolitana).
- Esito 1: ente soggetto all'obbligo SI/NO + motivazione.
- Esito 2: finanziamenti TRM - obbligo distinto SI/NO + motivazione.
- Esito 3: rispetto del termine di adozione + eventuali criticita'.
- Esito 4: regime transitorio applicabile SI/NO; se applicabile, presenza dei tre requisiti del primo rapporto.
- Rilievi BLOCCANTI / NON BLOCCANTI / NON DETERMINABILI.
- Rinvio finale al professionista firmatario per la verifica diretta delle fonti.

## Limiti

- Non valuta la conformita' della specifica istanza di finanziamento ad avvisi pubblici (ciascun avviso TRM o mobilita' ciclistica puo' avere requisiti aggiuntivi).
- Non interpreta deroghe regionali o leggi regionali integrative.
- Non valuta l'eventuale conflitto con norme statutarie dell'ente.
