# AGENTS.md - SKILL_NAME_PLACEHOLDER

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

[Descrivere in 2-3 frasi il dominio della skill: che documento/adempimento copre, quale norma/decreto e' il riferimento principale, chi e' il target utente.]

## Fonti autoritative

[Elencare le fonti normative ufficiali catalogate in `references/sources.yaml`. Per ognuna: nome breve, hash o id del catalogo, eventuale URL canonico.]

- **Fonte 1** - hash `...`
- **Fonte 2** - hash `...`

Estratti pertinenti gia' preparati in `references/estratti/`:
- `<file>.md` - cosa contiene

## Articoli e punti chiave

[Elencare gli articoli/punti normativi che la skill cita piu' frequentemente. Quando l'agent produce output, deve citare il riferimento preciso, non la legge in generale.]

- **Art. X co. Y lett. Z**: cosa dice
- **Allegato N punto P.Q**: cosa dice

## Convenzioni specifiche

### Cosa NON fare
- [Anti-pattern 1 specifico al dominio]
- [Anti-pattern 2]

### Cosa fare
- [Best practice 1: cosa citare, in che ordine]
- [Best practice 2: come strutturare l'output]
- [Best practice 3: limiti di responsabilita' del professionista firmatario]

## Validatori

- [Nome cognome (ruolo, ente)] - se identificato per Livello 2 validation.

## Stato attuale

- Versione: vedi `CHANGELOG.md`
- Validazione: Livello 1 / Livello 2 / Livello 3
- Task files: elenco
- Esempi: numero conformi + numero problematici
