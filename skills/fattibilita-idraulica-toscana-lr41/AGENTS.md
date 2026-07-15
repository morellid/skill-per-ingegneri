# AGENTS.md - fattibilita-idraulica-toscana-lr41

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale alla **fattibilita' delle trasformazioni nelle aree a
pericolosita' per alluvioni in Toscana** (L.R. 41/2018): magnitudo idraulica,
opere per la gestione del rischio, limitazioni e condizioni per la nuova
costruzione e per il patrimonio esistente. Target: progettisti, tecnici comunali,
geologi/idraulici, uffici del Genio Civile.

**E' una skill documentale e regionale (Toscana)**: non legge le mappe di
pericolosita', non misura battente/velocita', non dimensiona le opere ne' calcola
i volumi.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **lr-toscana-41-2018**: L.R. Toscana 24/7/2018 n. 41, testo vigente sulla
  Raccolta Normativa del Consiglio regionale. Binario = pagina a **testo
  completo** (URL con `pr=idx,0;artic,1`; il link base restituisce solo l'indice),
  hash stabile 4b75a500..., stesso host della skill pratiche-edilizie-lr65-2014-
  toscana. Articoli 1, 2, 7, 8, 10, 11, 12, 23, 25 letti e trascritti verbatim in
  `references/fonti/lr-toscana-41-2018.md`.

Estratto operativo: `references/estratti/fattibilita-idraulica-checklist.md`.

## Punti chiave (verificati sul testo)

- **Magnitudo idraulica** (art. 2 h1-h3): **moderata** (battente <= 0,5 m e v <= 1
  m/s; o battente <= 0,3 m); **severa** (battente <= 0,5 m e v > 1 m/s, o battente
  0,5-1 m e v <= 1 m/s; o battente 0,3-0,5 m); **molto severa** (battente 0,5-1 m e
  v > 1 m/s, o battente > 1 m; o battente > 0,5 m). Il **battente** e' riferito
  allo scenario **poco frequente**.
- **Opere (art. 8)** per il **rischio medio R2**: a) opere idrauliche assenza
  allagamenti; b) opere idrauliche riduzione a magnitudo moderata + sopraelevazione;
  c) sopraelevazione; d) difesa locale. Sempre **senza aggravio** altrove (c. 2).
- **Limitazioni (art. 10)**: in aree a pericolosita' **frequente**, ospedali/case
  di cura, strutture strategiche, impianti AIA ammessi **solo** con opera art. 8
  lett. a).
- **Nuova costruzione (art. 11)**: severa/molto severa -> opera art. 8 a) o b);
  moderata -> opera art. 8 a), b) o c).
- **Esistente (art. 12)**: condizioni di sicurezza idraulica (sopraelevazione,
  quote).

## Convenzioni specifiche

### Cosa NON fare
- Non individuare la **classe di pericolosita'** del sito ne' misurare **battente/
  velocita'**: rinviare al **PGRA**/Piani di bacino e alla relazione idraulica.
- Non **dimensionare** le opere ne' calcolare i volumi: rinviare al progettista e
  alle DGR/allegati tecnici.
- Non riprodurre il **DPGR 5/R/2020** (indagini geologiche/idrauliche/sismiche) ne'
  le mappe.
- Non estendere ad altre regioni: la skill e' solo **Toscana**.

### Cosa fare
- Determinare la magnitudo dai valori forniti (battente/velocita') e citare le
  soglie dell'art. 2.
- Applicare le limitazioni (art. 10) e le condizioni per tipo di intervento (art.
  11 nuova costruzione, art. 12 esistente).
- Chiudere con il rinvio al PGRA/relazione idraulica e all'autorita' competente.

### Nota sulla scheda #49
La issue cita il DPGR 5/R/2020 come fonte, ma quel regolamento disciplina il
deposito/controllo delle **indagini geologiche, idrauliche e sismiche** (art. 104
l.r. 65/2014), non la fattibilita' idraulica. La fonte corretta e' la **L.R.
41/2018**, adottata qui. Il "calcolo dei volumi compensativi" e' rimandato alle
DGR/allegati tecnici e al progettista.

## Aggiornamento della fonte

Testo regionale: se si aggiorna la skill, riscaricare la pagina a testo completo
(nuovo hash) e rileggere gli articoli modificati; verificare eventuali modifiche
(es. l.r. 7/2020 che ha gia' sostituito l'art. 11 c. 1).

## Validatori

- Non ancora assegnato (Livello 2 da effettuare con geologo/ingegnere idraulico
  toscano).

## Stato attuale

- Versione: 0.1.0-alpha (closes #49)
- Task files: 2 (`verifica-fattibilita.md`, `checklist-interventi.md`)
- Esempi: 2 (nuova costruzione in area a pericolosita' frequente; lotto non a
  pericolosita')
