# AGENTS.md - servitu-coattive-prediali-cc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale all'inquadramento delle **servitù prediali coattive** (legali) di
più diretto interesse tecnico secondo il **Codice civile** (R.D. 262/1942), Libro III,
Titolo VI: nozione, costituzione, passaggio coattivo (fondo intercluso e non intercluso),
acquedotto coattivo, elettrodotto coattivo e vie funicolari. Target: tecnici, geometri,
ingegneri, avvocati, CTU.

**È una skill documentale**: non redige atti o domande giudiziali, non quantifica
l'indennità e non riproduce le leggi speciali su acque ed elettrodotti.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **codice-civile-servitu-coattive**: Codice civile (R.D. 16/3/1942 n. 262), artt. 1027,
  1031, 1032, 1033, 1051, 1052, 1053, 1055, 1056, 1057, testo su Normattiva. Binario =
  pagina indice pinnata `!vig=2026-07-17` (hash stabile f817bc32..., codice 042U0262;
  stesso indice delle altre skill sul Codice civile). Articoli letti via AJAX
  (caricaArticolo, idGruppo 125-131) e trascritti verbatim in
  `references/fonti/cc-servitu-coattive.md`.

Estratto operativo: `references/estratti/servitu-coattive-checklist.md`.

## Punti chiave (verificati sul testo)

- **Nozione** (art. 1027): peso su un fondo (servente) per l'utilità di altro fondo
  (dominante) di diverso proprietario.
- **Costituzione** (art. 1031): coattiva, volontaria, per usucapione o destinazione del
  padre di famiglia.
- **Costituzione coattiva** (art. 1032): con **sentenza** (o atto amministrativo) in
  mancanza di contratto; fissa modalità e **indennità**; opposizione prima del pagamento.
- **Acquedotto coattivo** (art. 1033): passaggio alle acque per bisogni della vita/usi
  agrari/industriali; esenti case, cortili, giardini, aie.
- **Passaggio coattivo** (artt. 1051-1052): fondo **intercluso** o accesso
  **inadatto/insufficiente** non ampliabile; criteri accesso più breve/minor danno;
  Corte cost. 167/1999 (accessibilità).
- **Indennità/cessazione** (artt. 1053, 1055): indennità proporzionata al danno (valore
  zona ex art. 1038); soppressione se cessa l'interclusione.
- **Elettrodotto/vie funicolari** (artt. 1056-1057): passaggio "in conformità delle leggi
  in materia" (rinvio).

## Convenzioni specifiche

### Cosa NON fare
- Non **riprodurre le leggi speciali** su acque (R.D. 1775/1933) ed elettrodotti: rinvio.
- Non **redigere** atti costitutivi o domande giudiziali.
- Non **quantificare l'indennità** (art. 1038): rinviare al CTU.
- Non confondere la servitù di elettrodotto **civilistica** (art. 1056) con quella
  **amministrativa/espropriativa** (DPR 327/2001).
- Non citare a memoria: citare l'articolo (1027-1057).

### Cosa fare
- Verificare prima il **presupposto** (interclusione, diritto sulle acque) poi
  localizzazione, costituzione, indennità.
- Distinguere **servente** e **dominante** e le **esenzioni** (case/cortili/giardini/aie).
- Tenere separata questa skill da `distanze-legali-costruzioni-cc` e
  `espropriazione-pubblica-utilita-dpr327`.

## Aggiornamento della fonte Normattiva

Se si aggiorna la skill, ri-pinnare la URL a nuova `!vig=YYYY-MM-DD`, riscaricare la
pagina indice (nuovo hash) e rileggere via AJAX gli articoli modificati.

## Validatori

- Non ancora assegnato (Livello 2 da effettuare con avvocato civilista / CTU).

## Stato attuale

- Versione: 0.1.0-alpha (closes #321)
- Task files: 2 (`inquadra-passaggio-coattivo.md`, `inquadra-servitu-acque-elettrodotto.md`)
- Esempi: 2 (passaggio coattivo fondo intercluso; acquedotto ed elettrodotto coattivo)
