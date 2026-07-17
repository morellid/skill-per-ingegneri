# AGENTS.md - usucapione-cc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale all'inquadramento dell'**usucapione** (acquisto della proprietà e dei
diritti reali di godimento per possesso continuato) secondo il **Codice civile** (R.D.
262/1942), Libro III, Titolo VIII: termini per tipo di bene, ordinaria vs abbreviata,
requisiti del possesso, rapporto con la prescrizione, interruzione. Target: tecnici,
geometri, avvocati, CTU.

**È una skill documentale**: non redige atti o domande giudiziali, non gestisce la mediazione
e non valuta il possesso in concreto.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **cc-usucapione-1158-1167**: Codice civile (R.D. 16/3/1942 n. 262), artt. 1158-1167, testo
  su Normattiva. Binario = pagina indice pinnata `!vig=2026-07-17` (hash stabile f817bc32...,
  codice 042U0262; stesso indice delle altre skill sul Codice civile). Articoli letti via AJAX
  (caricaArticolo, idGruppo 144) e trascritti verbatim in
  `references/fonti/cc-usucapione-1158-1167.md`.

Estratto operativo: `references/estratti/usucapione-checklist.md`.

## Punti chiave (verificati sul testo)

- **Termini**: immobili 20 anni ordinaria (1158) / 10 anni abbreviata (1159); piccola
  proprietà rurale 15/5 anni (1159-bis); universalità di mobili 20/10 (1160); mobili 10 (buona
  fede) / 20 (mala fede) (1161); mobili registrati 3/10 (1162).
- **Abbreviata**: richiede **cumulativamente** buona fede + titolo idoneo + trascrizione.
- **Possesso**: non vizioso (art. 1163); il **detentore** non usucapisce senza
  **interversione** (art. 1164).
- **Prescrizione**: si applicano sospensione/interruzione/computo (art. 1165); eccezioni per
  il terzo possessore (art. 1166, art. 2942).
- **Interruzione**: perdita del possesso oltre un anno (art. 1167), salvo reintegra vittoriosa.

## Convenzioni specifiche

### Cosa NON fare
- Non **redigere** atti o **domande giudiziali** di accertamento dell'usucapione.
- Non gestire la **mediazione** ex art. 5 D.Lgs. 28/2010 (skill
  `mediazione-civile-conciliazione-dlgs28`).
- Non **valutare in concreto** il possesso (continuità, animus, buona fede): rinviare ad
  avvocato/CTU.
- Non riprodurre le **norme sulla prescrizione** (artt. 2934 ss., 2942) né la **legge
  speciale** sulla piccola proprietà rurale: rinvio.
- Non citare a memoria: citare l'articolo (1158-1167) e il termine.

### Cosa fare
- Partire dal **bene** (immobile/mobile/registrato/universalità/rurale) per il termine, poi
  verificare i presupposti dell'abbreviata (buona fede/titolo/trascrizione).
- Distinguere **possesso** da **detenzione** (interversione, art. 1164).
- Tenere la skill distinta da `servitu-coattive-prediali-cc` (costituzione delle servitù) e
  dalle altre skill c.c.

## Aggiornamento della fonte Normattiva

Se si aggiorna la skill, ri-pinnare la URL a nuova `!vig=YYYY-MM-DD`, riscaricare la pagina
indice (nuovo hash) e rileggere via AJAX gli articoli modificati.

## Validatori

- Non ancora assegnato (Livello 2 da effettuare con avvocato civilista/CTU).

## Stato attuale

- Versione: 0.1.0-alpha (closes #333)
- Task files: 2 (`inquadra-usucapione.md`, `verifica-requisiti-possesso.md`)
- Esempi: 2 (ordinaria vs abbreviata di un immobile; detenzione/interversione e interruzione)
