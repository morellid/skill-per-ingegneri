# AGENTS.md - specifiche-tecniche-ict-appalti-dlgs36

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale alla redazione delle **specifiche tecniche** di una procedura
d'appalto **ICT** della pubblica amministrazione e alla fase preliminare di
**analisi comparativa** delle soluzioni software. Target: RUP, uffici gare, tecnici
ICT e ingegneri informatici delle PA.

**E' una skill documentale**: non redige il capitolato/disciplinare completo, non
sceglie la soluzione, non valuta le offerte e non calcola importi.

## Fonti autoritative

Catalogate in `references/sources.yaml`:

- **dlgs-36-2023**: D.Lgs. 31/3/2023 n. 36 (Codice dei contratti pubblici), artt.
  79, 80 e **allegato II.5**. Binario = pagina indice Normattiva pinnata a
  `!vig=2026-07-15` (hash 992ae622...). Articoli e allegato caricati via AJAX
  (`caricaArticolo`, idGruppo=54 per l'allegato) e trascritti verbatim in
  `references/fonti/dlgs-36-2023.md`.
- **dlgs-82-2005-cad**: D.Lgs. 7/3/2005 n. 82 (CAD), artt. 68 e 69. Binario =
  pagina indice Normattiva pinnata a `!vig=2026-07-15` (hash 2eebfb96...).
  Trascrizione verbatim in `references/fonti/dlgs-82-2005-cad.md`.

Estratto operativo: `references/estratti/specifiche-tecniche-ict-checklist.md`.

## Punti chiave (verificati sul testo)

- **Analisi comparativa (art. 68 CAD)**: valutazione tecnico-economica tra sei
  soluzioni (a-f: ad hoc, riuso, open source, cloud, proprietario, misto); criteri
  c. 1-bis (costo complessivo; formati/standard aperti e interoperabilita';
  sicurezza/protezione dati/livelli di servizio); proprietario solo se
  motivatamente impossibile accedere a soluzioni disponibili o open source
  (c. 1-ter). Modalita' AgID (rinvio).
- **Riuso (art. 69 CAD)**: rilascio codice sorgente sotto licenza aperta (c. 1);
  nel capitolato/specifiche di progetto titolarita' dei diritti in capo alla PA
  committente (c. 2); pubblicazione su piattaforme AgID (c. 2-bis).
- **Specifiche tecniche (art. 79 + all. II.5, A)**: modalita' di formulazione
  (punto 5: prestazioni/requisiti funzionali; riferimento a norme con "o
  equivalente"; misti); divieto di marchi/brevetti (punto 6) salvo eccezione con
  "o equivalente"; equivalenza (punti 7-8, mezzi di prova art. 105).
- **Etichettature (art. 80 + all. II.5, B)**: condizioni punto 1 (a-e);
  equivalenza e altri mezzi di prova (punti 2-3).
- L'art. 79 e l'art. 80 sono **norme di rinvio** all'allegato II.5 (operativo art.
  70 c. 3).

## Convenzioni specifiche

### Cosa NON fare
- Non redigere il **capitolato/disciplinare** completo ne' scegliere la soluzione.
- Non definire i **criteri di aggiudicazione / OEPV** (art. 108): rinviare alla
  skill `oepv-valutatore-offerte-tecniche`.
- Non riprodurre le **Linee guida AgID** (analisi comparativa, riuso,
  publiccode.yml) ne' le **norme tecniche** UNI/EN/ISO/IEC (a pagamento): citarle.
- Non calcolare **importi/base d'asta/soglie**.

### Cosa fare
- Impostare lo schema soluzioni + criteri (art. 68), le clausole di
  riuso/titolarita' (art. 69), la modalita' di formulazione ammessa (all. II.5) e
  le etichettature (art. 80).
- Citare sempre l'articolo/punto dell'allegato II.5.
- Chiudere con il rinvio a RUP e Linee guida AgID/ANAC.

## Aggiornamento delle fonti

Testi statali su Normattiva: se si aggiorna la skill, riscaricare le pagine indice
pinnate a un nuovo `!vig=` (nuovo hash) e rileggere gli articoli/allegato
modificati. Verificare in particolare eventuali novelle al Codice (D.Lgs. 36/2023
e correttivi) e al CAD.

## Validatori

- Non ancora assegnato (Livello 2 da effettuare con esperto di appalti ICT / RUP).

## Stato attuale

- Versione: 0.1.0-alpha (closes #50)
- Task files: 2 (`analisi-comparativa-soluzioni.md`, `formula-specifiche-tecniche.md`)
- Esempi: 2 (specifica con marchio senza "o equivalente"; analisi comparativa per
  l'acquisto di un gestionale)
