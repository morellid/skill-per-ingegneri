# rsia-audit-stradale-dlgs35

> Versione: 0.1.0-alpha
> Stato: in sviluppo (validazione Livello 1, autore: Claude Opus 4.7)

Skill di supporto alle quattro procedure di gestione della sicurezza delle infrastrutture stradali del D.Lgs 15 marzo 2011, n. 35, nel testo modificato dal D.Lgs 15 novembre 2021, n. 213 (recepimento della Direttiva (UE) 2019/1936).

## Target

- Controllori della sicurezza stradale iscritti all'elenco nazionale presso il MIMS (art. 4, comma 7 D.Lgs 35/2011).
- Ingegneri stradali, tecnici dell'organo competente, tecnici di concessionari autostradali coinvolti nelle procedure VISS, RSA, NSA, ispezioni.
- Funzionari pubblici che devono valutare la conformita' di un progetto o di una rete alle prescrizioni del decreto.

La skill produce bozze tecniche di lavoro. La firma e la trasmissione restano sempre in capo al professionista qualificato.

## Cosa fa

Cinque sotto-attivita', dettagliate in `SKILL.md` e nei file `tasks/`:

- `check-ambito-applicazione.md` - verifica preliminare se la strada o il progetto rientra nel campo di applicazione del decreto.
- `draft-viss.md` - redazione della Valutazione di Impatto sulla Sicurezza Stradale (VISS) ex art. 3 e Allegato I.
- `draft-rsa.md` - redazione del Controllo di Sicurezza Stradale (RSA) ex art. 4 e Allegato II, su una delle quattro fasi (PFTE, progettazione esecutiva, ultimazione, prima fase di funzionamento).
- `draft-nsa.md` - redazione della Valutazione di Sicurezza a Livello di Rete (NSA) ex nuovo art. 5 e Allegato III, introdotta dal D.Lgs 213/2021.
- `verifica-requisiti-controllore.md` - verifica dell'idoneita' di un controllore o di una squadra (qualifiche, formazione, incompatibilita', regime transitorio art. 12 c. 4).

## Installazione

Vedi il `README.md` di root del repo per l'installazione delle skill in Claude Code (`~/.claude/skills/`) e in Codex (`~/.agents/skills/`). Il symlink alla cartella `skills/rsia-audit-stradale-dlgs35/` rende la skill disponibile in entrambi gli ambienti.

## Fonti consultate

- D.Lgs 15 marzo 2011, n. 35 - testo originale (Gazzetta Ufficiale n. 81 del 8 aprile 2011).
- D.Lgs 15 novembre 2021, n. 213 - decreto di modifica (Gazzetta Ufficiale n. 298 del 16 dicembre 2021).
- Direttiva 2008/96/CE - atto-quadro UE (testo italiano disponibile da fonti MIT).
- Direttiva (UE) 2019/1936 - riferimento strutturale (contenuti applicati attraverso il D.Lgs 213/2021).

Dettaglio completo, con hash SHA256 e link al download, in `references/sources.yaml`. Estratti testuali pertinenti in `references/estratti/`.

## Limiti noti

- La skill **non** produce documenti pronti al deposito o alla firma. Ogni output e' una bozza tecnica che deve essere rivista, integrata e firmata da un controllore qualificato.
- La skill **non** sostituisce le verifiche di campo (sopralluoghi, ispezioni visive, rilievi di velocita').
- La skill **non** copre le gallerie stradali (escluse dall'art. 1 e disciplinate dal D.Lgs 264/2006), le piste ciclabili, le strade non aperte al traffico generale.
- La skill **non** determina la qualifica formale di un soggetto come controllore: l'iscrizione all'elenco nazionale e' di competenza del MIMS.
- La skill **non** fornisce pareri legali su responsabilita' civili o penali derivanti dall'omissione delle procedure.
- La skill al momento (v0.1.0-alpha) richiede validazione di Livello 2 da parte di un controllore della sicurezza stradale iscritto all'elenco MIMS, non ancora identificato.

## Changelog

Vedi [CHANGELOG.md](CHANGELOG.md).
