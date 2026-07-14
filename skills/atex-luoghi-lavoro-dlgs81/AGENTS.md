# AGENTS.md - atex-luoghi-lavoro-dlgs81

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale alla **protezione dei lavoratori dai rischi da atmosfere
esplosive** (ATEX luoghi di lavoro) ai sensi del **Titolo XI del D.Lgs. 81/2008**
(recepimento dir. 1999/92/CE): ambito, obblighi del datore di lavoro, valutazione
del rischio, classificazione delle zone, DPCE, verifiche, sanzioni. Target:
datori di lavoro, RSPP, tecnici della sicurezza, consulenti.

**E' una skill documentale**: non classifica le zone, non redige la valutazione
del rischio ne' il DPCE, e **non tratta la marcatura ATEX degli apparecchi** (dir.
prodotti 2014/34/UE).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-81-2008**: D.Lgs. 9/4/2008 n. 81, Titolo XI, testo multivigente su
  Normattiva. Binario = pagina indice pinnata `!vig=2026-07-14` (hash stabile
  0664b393..., pattern della skill aua-dpr59-dossier). Articoli 287, 288, 289,
  290, 293, 294, 296, 297 letti via AJAX (caricaArticolo) e trascritti verbatim
  in `references/fonti/dlgs-81-2008.md`.

Estratto operativo: `references/estratti/atex-checklist.md`.

## Punti chiave (verificati sul testo)

- **Ambito** (art. 287): protezione dei **lavoratori** esposti ad **atmosfere
  esplosive** (art. 288); esclusioni al c. 3 (cure mediche, apparecchi a gas DPR
  661/1996, esplosivi/sostanze instabili, industrie estrattive D.Lgs. 624/1996,
  mezzi di trasporto internazionali). Include i lavori in sotterraneo (c. 2).
- **Obblighi (art. 289)**: prevenire la **formazione** (c. 1); se non possibile,
  evitare l'**accensione** e attenuare gli **effetti** (c. 2).
- **Valutazione (art. 290)**: parte dell'art. 17; considera probabilita'/durata
  atmosfere, fonti di accensione (incl. elettrostatiche), impianto/sostanze/
  processi, effetti prevedibili.
- **Zone (art. 293)**: ripartizione a norma **allegato XLIX** (0/1/2 gas-vapori;
  20/21/22 polveri); prescrizioni minime **allegato L**; segnaletica **allegato
  LI**.
- **DPCE (art. 294)**: documento sulla protezione contro le esplosioni, contenuti
  del c. 2 (rischi valutati, misure, zone, prescrizioni minime, efficienza,
  impiego sicuro attrezzature).
- **Verifiche (art. 296)**: installazioni elettriche in **zone 0, 1, 20, 21** ->
  **DPR 462/2001** (cfr. skill verifiche-messa-a-terra-dpr462).
- **Sanzioni (art. 297)**: art. 290 -> arresto 3-6 mesi o ammenda 2.500-6.400;
  artt. 289 c. 2, 293 c. 1-2, 294 c. 1-2-3, 296 -> stessa pena a carico di datore
  di lavoro e dirigenti.

## Convenzioni specifiche

### Cosa NON fare
- Non **classificare le zone** (allegato XLIX), non riprodurre prescrizioni
  minime (allegato L) o segnaletica (allegato LI): rinviare agli allegati e alle
  norme tecniche (CEI EN 60079).
- Non redigere la valutazione del rischio ne' il **DPCE**.
- Non trattare la **marcatura ATEX degli apparecchi** (dir. 2014/34/UE, eur-lex):
  fuori perimetro.
- Non citare a memoria termini/sanzioni: citare l'articolo (287-290, 293, 294,
  296, 297).

### Cosa fare
- Verificare prima le **esclusioni** (art. 287 c. 3), poi impostare la sequenza
  obblighi -> valutazione -> zone -> DPCE -> verifiche.
- Distinguere protezione dei **lavoratori** (Titolo XI) dalla marcatura degli
  **apparecchi** (2014/34/UE).
- Richiamare il raccordo con il DPR 462/2001 per le installazioni elettriche.

## Aggiornamento della fonte Normattiva

Testo multivigente: se si aggiorna la skill, ri-pinnare la URL a nuova
`!vig=YYYY-MM-DD`, riscaricare la pagina indice (nuovo hash) e rileggere via AJAX
gli articoli modificati.

## Validatori

- Non ancora assegnato (Livello 2 da effettuare con RSPP/esperto sicurezza di
  processo).

## Stato attuale

- Versione: 0.1.0-alpha (closes #57)
- Task files: 2 (`applicabilita-e-obblighi.md`, `checklist-dpce.md`)
- Esempi: 2 (reparto con polveri combustibili; deposito di esplosivi escluso)
