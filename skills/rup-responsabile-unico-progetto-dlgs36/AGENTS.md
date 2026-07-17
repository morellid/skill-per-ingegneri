# AGENTS.md - rup-responsabile-unico-progetto-dlgs36

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale all'inquadramento del **Responsabile unico del progetto (RUP)**
nei contratti pubblici ai sensi dell'**art. 15 del D.Lgs. 36/2023** (Codice dei
contratti pubblici): nomina, requisiti, unicita', modelli organizzativi, compiti,
struttura di supporto, formazione, incompatibilita' e RUP delle centrali di
committenza. Target: stazioni appaltanti, enti concedenti, RUP, uffici gare.

**E' una skill documentale**: non nomina il RUP, non redige gli atti di gara e non
verifica in concreto i requisiti dell'**allegato I.2**.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-36-2023-art15**: D.Lgs. 31/3/2023 n. 36, art. 15, testo multivigente su
  Normattiva. Binario = pagina indice pinnata `!vig=2026-07-17` (hash stabile
  0e9a1938..., codice 23G00044; stesso indice delle altre skill D.Lgs. 36). Art. 15
  (versione 2, idGruppo 2) letto via AJAX (caricaArticolo) e trascritto verbatim in
  `references/fonti/dlgs-36-2023-art15.md`.

Estratto operativo: `references/estratti/rup-checklist.md`.

## Punti chiave (verificati sul testo)

- **Nomina** (c. 1): nel **primo atto di avvio**, per programmazione, progettazione,
  affidamento ed esecuzione.
- **Soggetto/requisiti** (c. 2): tra i **dipendenti** con requisiti **allegato I.2**;
  regole per enti **non PA**; nomina tra dipendenti di **altre amministrazioni** in
  caso di carenza di organico; ufficio **obbligatorio e non rifiutabile**; subentro
  **ex lege** del responsabile dell'unita' organizzativa se manca la nomina.
- **Pubblicita'** (c. 3): nominativo nel **bando/avviso**, in mancanza invito o
  affidamento diretto.
- **Unicita'/modelli** (c. 4): RUP **unico**; ammessi **responsabili di procedimento**
  per fase, ferme supervisione/indirizzo/coordinamento del RUP.
- **Compiti** (c. 5): attivita' dell'**allegato I.2**; completamento dell'intervento;
  un periodo **soppresso** dal D.Lgs. 209/2024.
- **Supporto/formazione** (c. 6-7): struttura di supporto e risorse fino all'**1%**
  della base di gara; **piano di formazione** (coerente con l'art. 37).
- **Incompatibilita'** (c. 8): nel **contraente generale** e nel **PPP** vietato il
  cumulo di RUP, responsabile dei lavori, direttore dei lavori, collaudatore
  all'affidatario o a soggetti collegati.
- **Centrali di committenza** (c. 9): designano un RUP per le attivita' di competenza.

## Convenzioni specifiche

### Cosa NON fare
- Non **riprodurre l'allegato I.2** (requisiti e compiti del RUP): citarlo come rinvio.
- Non **nominare** il RUP ne' redigere atti di avvio/bando/nomina.
- Non **verificare in concreto** requisiti o collegamenti societari (c. 8): rinviare
  alla stazione appaltante.
- Non citare a memoria soglie o divieti: citare il comma (art. 15 c. 1-9).

### Cosa fare
- Distinguere **unicita' del RUP** (c. 4) da modello con **responsabili di
  procedimento**: non esistono "due RUP".
- Trattare il **subentro ex lege** (c. 2) come regola di chiusura in mancanza di
  nomina.
- Distinguere la figura del RUP dagli istituti coperti da altre skill (subappalto
  art. 119, garanzie artt. 106/117, varianti art. 120, collaudo art. 116).

## Aggiornamento della fonte Normattiva

Testo multivigente: se si aggiorna la skill, ri-pinnare la URL a nuova
`!vig=YYYY-MM-DD`, riscaricare la pagina indice (nuovo hash) e rileggere via AJAX
l'articolo se modificato.

## Validatori

- Non ancora assegnato (Livello 2 da effettuare con esperto di contratti pubblici /
  RUP).

## Stato attuale

- Versione: 0.1.0-alpha (closes #319)
- Task files: 2 (`inquadra-nomina-rup.md`, `verifica-compiti-incompatibilita.md`)
- Esempi: 2 (nomina e modello organizzativo; incompatibilita' nel contraente generale)
