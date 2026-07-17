# AGENTS.md - mediazione-civile-conciliazione-dlgs28

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale alla **mediazione civile e commerciale** finalizzata alla conciliazione:
condizione di procedibilità e materie, esclusioni, procedimento, conclusione ed efficacia esecutiva
dell'accordo, secondo il **D.Lgs. 4 marzo 2010, n. 28** (artt. 5, 8, 11, 12; testo vigente post
riforma Cartabia). Target: ingegneri (come mediatori, esperti/CTU o parti), tecnici, consulenti.

**È una skill documentale**: inquadra procedibilità/procedimento/esiti; **non svolge** la mediazione,
**non redige** verbale/accordo, non fornisce contenuto di merito né consulenza legale, non sostituisce
il mediatore, l'organismo, l'avvocato o il giudice.

## Nota sull'area

Area **forense**. Fa crescere l'area (oggi `compensi-ctu-dpr115`, `relazione-peritale-ctu-cpc`;
l'ATP ex art. 696-bis c.p.c. è oggetto di skill/PR dedicata). La **consulenza tecnica preventiva**
(art. 696-bis c.p.c.) è **esclusa** dalla mediazione obbligatoria (art. 5, c. 6, lett. c): tenere
distinti i due istituti.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-28-2010-artt-5-8-11-12**: D.Lgs. 4 marzo 2010, n. 28, pagina indice Normattiva pinnata a
  `!vig=2026-07-17` (hash `e09c1d94...`; codice 010G0050). Artt. 5 (v10), 8 (v7), 11 (v6), 12 (v6),
  grp2, caricati via `caricaArticolo` e trascritti verbatim (commi operativi).

Trascrizione in `references/fonti/dlgs-28-2010-artt-5-8-11-12.md`; estratto operativo in
`references/estratti/mediazione-checklist.md`.

## Punti chiave (verificati sul testo)

- **Condizione di procedibilità** (art. 5): elenco materie; improcedibilità entro la prima udienza;
  condizione avverata col primo incontro senza accordo; esclusioni (ingiunzione, sfratto, 696-bis,
  possessori, esecuzione, camera di consiglio, ecc.); cautelari non preclusi.
- **Procedimento** (art. 8): primo incontro **20-40 gg**; effetti su prescrizione/decadenza;
  partecipazione personale; assistenza avvocati; esperti CTU.
- **Conclusione** (art. 11): verbale con accordo allegato; proposta e **7 gg** per accettare/rifiutare;
  deposito; conservazione triennale; autentica per atti art. 2643 c.c.
- **Efficacia esecutiva** (art. 12): titolo esecutivo se tutte le parti assistite dagli avvocati
  (certificazione); altrimenti omologazione con decreto del presidente del tribunale.

## Convenzioni specifiche

### Cosa NON fare
- Non **svolgere** la mediazione né **redigere** verbale/accordo.
- Non fornire il **merito tecnico** né **consulenza legale** (materie, competenza, strategia).
- Non inventare **termini/materie** (usare 20-40 gg, 7 gg, triennio e l'elenco dell'art. 5 come da
  testo); non riprodurre tariffe/indennità (DM parametri).

### Cosa fare
- **Stabilire** l'obbligatorietà per la materia; **inquadrare** procedimento, conclusione ed
  efficacia esecutiva, con rinvio agli articoli richiamati.

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.Lgs. 28/2010 pinnato a nuovo `!vig=` (nuovo hash) e rileggere
gli artt. 5, 8, 11, 12 (materia soggetta a riforme; testo tra `(( ))`).

## Validatori

- Non ancora assegnato (Livello 2 con avvocato/mediatore o organismo di mediazione).

## Stato attuale

- Versione: 0.1.0-alpha
- Task files: 2 (`verifica-condizione-procedibilita.md`, `inquadra-procedimento-esito.md`)
- Esempi: 2 (condizione di procedibilità in materia condominiale; verbale/accordo ed efficacia esecutiva)
