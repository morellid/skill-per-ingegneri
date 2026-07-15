# Task: verifica-fattibilita

Determina l'ammissibilita' di un intervento in un'area a pericolosita' per
alluvioni in Toscana (L.R. 41/2018) e le opere di messa in sicurezza richieste.

## Input richiesto

- **Classe di pericolosita'** del sito (aree a pericolosita' per alluvioni
  **frequenti** o **poco frequenti**), dagli atti di pianificazione di bacino
  (PGRA).
- **Battente** (m) e, se disponibile, **velocita'** della corrente (m/s) - dallo
  scenario poco frequente.
- **Tipo di intervento**: nuova costruzione, patrimonio edilizio esistente,
  ospedale/casa di cura, struttura strategica, impianto AIA, infrastruttura.
- Ubicazione dentro/fuori il territorio urbanizzato (l.r. 65/2014).

## Procedura

1. **Magnitudo idraulica (art. 2)** dai valori di battente/velocita':
   - **moderata**: battente <= 0,5 m e velocita' <= 1 m/s (o, senza velocita',
     battente <= 0,3 m);
   - **severa**: battente <= 0,5 m e velocita' > 1 m/s, oppure battente 0,5-1 m e
     velocita' <= 1 m/s (o, senza velocita', battente 0,3-0,5 m);
   - **molto severa**: battente 0,5-1 m e velocita' > 1 m/s, oppure battente > 1 m
     (o, senza velocita', battente > 0,5 m).
   - **La skill non misura battente/velocita'**: chiedili all'utente o rinvia al
     PGRA/alla relazione idraulica.

2. **Limitazioni assolute (art. 10)**: nelle aree a pericolosita' **frequente**,
   **ospedali/case di cura**, **strutture strategiche** e **impianti AIA** sono
   ammessi **solo** con le opere idrauliche dell'art. 8 c. 1 lett. a) (assenza di
   allagamenti); altrimenti vietati.

3. **Nuova costruzione (art. 11)** nelle aree a pericolosita' **frequente**:
   - magnitudo **severa/molto severa** -> opera idraulica art. 8 c. 1 **lett. a) o
     b)**;
   - magnitudo **moderata** -> opera art. 8 c. 1 **lett. a), b) o c)**.

4. **Patrimonio esistente (art. 12)**: condizioni di sicurezza idraulica
   (sopraelevazione, quote di sicurezza) secondo l'art. 12.

5. **Opere (art. 8)**: verificare che l'opera scelta (idraulica assenza/riduzione
   allagamenti, sopraelevazione, difesa locale) consegua almeno il **rischio
   medio R2** e il **non aggravio** del rischio in altre aree.

## Output

- Ammissibilita' dell'intervento (sì / no / condizionata), con l'articolo.
- Opere di messa in sicurezza richieste (lettera dell'art. 8) in funzione della
  magnitudo.
- Rinvio al PGRA/relazione idraulica per la classe e i valori del sito, e al
  progettista per il dimensionamento.

## Regole

- Non individuare la classe di pericolosita' ne' misurare battente/velocita':
  rinviare al PGRA.
- Non dimensionare le opere ne' calcolare i volumi: rinviare al progettista.
- Citare l'articolo (2, 8, 10, 11, 12). Skill valida solo per la **Toscana**.
