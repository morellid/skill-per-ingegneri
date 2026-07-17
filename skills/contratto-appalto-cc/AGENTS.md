# AGENTS.md - contratto-appalto-cc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale all'inquadramento del **contratto di appalto** di diritto privato nel
**Codice civile** (R.D. 262/1942), Libro IV, Titolo III, **Capo VII (Dell'appalto)**, artt.
1655-1666 e 1671: nozione, subappalto, corrispettivo, fornitura della materia, variazioni del
progetto, verifica in corso d'opera, difetti della materia, onerosita'/difficolta' dell'esecuzione,
verifica e pagamento, recesso unilaterale. Target: ingegneri, appaltatori, committenti.

**E' una skill documentale**: inquadra la disciplina civilistica; **non redige** il contratto ne'
gli atti, **non quantifica** importi, non sostituisce l'avvocato/CTU.

## Nota sull'area e sulla complementarita'

Area **forense**. Complementare a `responsabilita-appaltatore-rovina-cc` (artt. 1667-1669:
difformita', vizi, rovina) e distinta dalle skill sull'**appalto pubblico** (D.Lgs. 36/2023:
`subappalto-contratti-pubblici-dlgs36`, `direzione-lavori-esecuzione-dlgs36`, `modifiche-varianti-
contratti-pubblici-dlgs36`, `garanzie-appalti-pubblici-dlgs36`). Questa copre gli artt. 1655-1666
e 1671 del Codice civile.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **cc-appalto-1655-1671**: Codice civile (R.D. 262/1942), pagina indice Normattiva pinnata a
  `!vig=2026-07-17` (hash `f817bc32...`; codice 042U0262). Artt. 1655-1666 e 1671 (versione 1,
  idGruppo 208) caricati via `caricaArticolo` e trascritti verbatim.

Trascrizione in `references/fonti/cc-appalto-1655-1671.md`; estratto operativo in
`references/estratti/contratto-appalto-checklist.md`.

## Punti chiave (verificati sul testo)

- **Nozione** (1655): organizzazione dei mezzi + gestione a proprio rischio (distinzione dal
  contratto d'opera, art. 2222).
- **Subappalto** (1656): previa autorizzazione del committente.
- **Corrispettivo** (1657), **materia** (1658).
- **Variazioni**: concordate con prova scritta (1659), necessarie con soglia del **sesto** per il
  recesso (1660), ordinate dal committente entro il **sesto** con compenso (1661).
- **Verifica in corso d'opera** e risoluzione (1662); **difetti della materia** (1663).
- **Onerosita'/difficolta'** (1664): revisione per la sola eccedenza oltre il **decimo**; equo
  compenso per difficolta' geologiche/idriche.
- **Verifica e pagamento** con accettazione anche tacita (1665); per **singole partite** (1666).
- **Recesso** del committente con indennizzo di spese, lavori e mancato guadagno (1671).

## Convenzioni specifiche

### Cosa NON fare
- Non **redigere** il contratto ne' gli atti (autorizzazioni scritte, riserve, verbali di verifica,
  dichiarazione di recesso).
- Non **quantificare** corrispettivi/revisioni/indennita' in via definitiva.
- Non trattare la **responsabilita'** per difformita'/vizi/rovina (1667-1669, skill dedicata) ne'
  l'**appalto pubblico** (D.Lgs. 36/2023); non riprodurre gli artt. 1668, 1670, 1672-1677 ne' l'art.
  2222 (rinvio).

### Cosa fare
- Qualificare il rapporto (appalto vs contratto d'opera), inquadrare subappalto, corrispettivo,
  materia, variazioni (soglia del sesto), onerosita' (soglia del decimo), verifica/pagamento e
  recesso, sui commi degli artt. 1655-1666 e 1671.

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del Codice civile pinnato a nuovo `!vig=` (nuovo hash) e rileggere
gli artt. 1655-1666 e 1671. Il Codice civile e' storicamente stabile su questi articoli, ma
verificare eventuali novelle.

## Validatori

- Non ancora assegnato (Livello 2 con avvocato civilista / esperto di contrattualistica).

## Stato attuale

- Versione: 0.1.0-alpha (closes #337)
- Task files: 2 (`inquadra-contratto-appalto.md`, `gestisci-variazioni-recesso.md`)
- Esempi: 2 (qualificazione appalto vs contratto d'opera e accettazione tacita; variazioni oltre il
  sesto, revisione oltre il decimo e recesso del committente)
