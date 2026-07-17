# AGENTS.md - comunione-ordinaria-cc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale all'inquadramento della **comunione ordinaria** (comproprietà di beni:
terreni, immobili, cose comuni) nel **Codice civile** (R.D. 262/1942), Libro III, Titolo VII,
**Capo I (Della comunione in generale)**, artt. 1100-1116: quote, uso e disposizione, obblighi/
spese, amministrazione, regolamento, innovazioni, impugnazioni, scioglimento e divisione. Target:
ingegneri, comproprietari, amministratori.

**E' una skill documentale**: inquadra la disciplina; **non redige** atti, **non quantifica** quote/
spese, non sostituisce l'avvocato/CTU.

## Nota sull'area e sulla complementarita'

Area **forense**. Distinta da `condominio-parti-comuni-assemblea-cc` (comunione **negli edifici**,
condominio, artt. 1117 ss.); complementare alle altre skill c.c. (distanze, servitu' coattive,
usucapione, contratto d'appalto, rovina d'edificio). Questa copre la **comunione ordinaria** degli
artt. 1100-1116.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **cc-comunione-1100-1116**: Codice civile (R.D. 262/1942), pagina indice Normattiva pinnata a
  `!vig=2026-07-17` (hash `f817bc32...`; codice 042U0262). Artt. 1100-1116 (versione 1, idGruppo
  139) caricati via `caricaArticolo` e trascritti verbatim.

Trascrizione in `references/fonti/cc-comunione-1100-1116.md`; estratto operativo in
`references/estratti/comunione-ordinaria-checklist.md`.

## Punti chiave (verificati sul testo)

- **Quote** presunte eguali (1101); **uso** senza alterare la destinazione ne' impedire il pari uso
  (1102); **disposizione** della quota nei limiti della quota (1103).
- **Spese** con rinunzia liberatoria e solidarieta' del cessionario (1104); **rimborso** spese
  necessarie (1110).
- **Amministrazione** a **maggioranza per valore delle quote** con informazione preventiva e ricorso
  al giudice (1105); **regolamento** e amministratore anche estraneo (1106).
- **Innovazioni/atti eccedenti**: maggioranza dei **due terzi del valore** (1108, c. 1); **consenso
  unanime** per alienazioni/diritti reali/locazioni > 9 anni (1108, c. 3).
- **Impugnazioni** entro **30 giorni** (regolamento 1107; delibere 1109, a pena di decadenza).
- **Scioglimento** sempre domandabile (1111): dilazione max 5 anni, patto di indivisione max 10
  anni; **divisione in natura** se comodamente divisibile (1114); rinvio alla divisione ereditaria
  (1116).

## Convenzioni specifiche

### Cosa NON fare
- Non **redigere** atti (regolamento, delibere, verbali, domanda/atto di divisione, cessione quota).
- Non **quantificare** quote, spese, conguagli ne' valori.
- Non trattare il **condominio** (artt. 1117 ss., skill dedicata), la **comunione legale tra
  coniugi** (artt. 177 ss.) ne' la **divisione ereditaria** (artt. 713 ss.): rinvio.

### Cosa fare
- Qualificare atti/decisioni (uso, ordinaria amministrazione, innovazione, atto eccedente) con le
  **maggioranze/consensi** richiesti; inquadrare **scioglimento** e **divisione**, sui commi degli
  artt. 1100-1116.

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del Codice civile pinnato a nuovo `!vig=` (nuovo hash) e rileggere
gli artt. 1100-1116. Il Codice civile e' storicamente stabile su questi articoli; verificare
eventuali novelle.

## Validatori

- Non ancora assegnato (Livello 2 con avvocato civilista / esperto di diritti reali).

## Stato attuale

- Versione: 0.1.0-alpha (closes #341)
- Task files: 2 (`inquadra-uso-amministrazione.md`, `inquadra-scioglimento-divisione.md`)
- Esempi: 2 (uso del cortile comune, innovazione a 2/3 e vendita all'unanimita'; scioglimento, patto
  di indivisione ridotto a 10 anni e bene non comodamente divisibile)
