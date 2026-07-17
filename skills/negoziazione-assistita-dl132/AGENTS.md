# AGENTS.md - negoziazione-assistita-dl132

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al procedimento di **negoziazione assistita da avvocati**:
convenzione, condizione di procedibilita', invito e mancato accordo, esecutivita'
dell'accordo, secondo il **D.L. 132/2014 (conv. L. 162/2014), artt. 2-5**. Target:
avvocati, tecnici/ingegneri parti di controversie, CTU.

**È una skill documentale**: inquadra requisiti, casi di procedibilita' ed effetti;
**non redige** gli atti, **non fornisce** consulenza legale, non sostituisce l'avvocato
o il giudice.

## Nota sull'area

Area **forense** (diritto civile / ADR). Distinta dalla **mediazione civile** (D.Lgs.
28/2010, strumento diverso con organismo di mediazione) e complementare alle skill
forensi CTU (`relazione-peritale-ctu-cpc`, `compensi-ctu-dpr115`) e
`responsabilita-appaltatore-rovina-cc`: questa copre la **negoziazione assistita**.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dl-132-2014-negoziazione**: D.L. 132/2014 (conv. L. 162/2014), pagina indice
  Normattiva pinnata a `!vig=2026-07-17` (hash `9642e055...`; codice 14G00147). Artt.
  2, 3, 4, 5, idGruppo 2, flagTipoArticolo 0, caricati via `caricaArticolo` e trascritti
  verbatim.

Trascrizione in `references/fonti/dl-132-2014-negoziazione.md`; estratto operativo in
`references/estratti/negoziazione-assistita-checklist.md`.

## Punti chiave (verificati sul testo)

- **Art. 2**: convenzione (cooperazione in buona fede; termine 1-3 mesi prorogabile 30
  gg; oggetto su diritti disponibili; forma scritta a pena di nullita'; almeno un
  avvocato per parte; certificazione firme; modello CNF).
- **Art. 3**: condizione di procedibilita' per **risarcimento danno da circolazione di
  veicoli e natanti** e **pagamenti <= 50.000 euro**; esclusioni (ingiunzione, ATP
  696-bis, esecuzione, camera di consiglio, azione civile nel processo penale,
  consumatori); rilievo entro la prima udienza; condizione avverata (non adesione/
  rifiuto in 30 gg o decorso termine); salvezza di urgenti/cautelari.
- **Art. 4**: invito (oggetto + avvertimento spese artt. 96/642 c.p.c.); certificazioni.
- **Art. 5**: accordo = titolo esecutivo e per ipoteca giudiziale; indicazione del
  valore; conformita' a norme imperative/ordine pubblico; trascrizione nel precetto
  (art. 480 c.p.c.); autentica del pubblico ufficiale per atti soggetti a trascrizione;
  illecito deontologico impugnare l'accordo.

## Convenzioni specifiche

### Cosa NON fare
- Non **redigere** convenzione/invito/accordo ne' fornire consulenza legale.
- Non **inventare** soglie/termini: usare 50.000 euro, 30 giorni, 1-3 mesi come da
  artt. 2-3.
- Non confondere con la **mediazione** (D.Lgs. 28/2010).

### Cosa fare
- **Verificare** se ricorre la condizione di procedibilita', **inquadrare** requisiti
  ed effetti, con rinvio all'avvocato e al giudice.

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.L. 132/2014 pinnato a nuovo `!vig=` (nuovo hash)
e rileggere gli artt. 2-5 (testo tra `(( ))` = modifiche successive, es. riforma
Cartabia D.Lgs. 149/2022).

## Validatori

- Non ancora assegnato (Livello 2 con avvocato civilista).

## Stato attuale

- Versione: 0.1.0-alpha
- Task files: 2 (`verifica-condizione-procedibilita.md`, `inquadra-convenzione-accordo.md`)
- Esempi: 2 (condizione di procedibilita' pagamento <= 50k - art. 3; convenzione ed effetti dell'accordo - artt. 2/5)
