# AGENTS.md - sottoprodotti-end-of-waste-dlgs152

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale all'inquadramento del **sottoprodotto** (art. 184-bis) e della
**cessazione della qualifica di rifiuto - End of Waste** (art. 184-ter) del **D.Lgs.
152/2006** (Codice dell'ambiente), Parte IV (Rifiuti). Target: tecnici, produttori,
gestori di rifiuti, consulenti ambientali.

**È una skill documentale**: non classifica in concreto un materiale, non riproduce i
decreti ministeriali di criterio e non sostituisce l'autorità competente o ISPRA/ARPA.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-152-2006-184bis-184ter**: D.Lgs. 3/4/2006 n. 152, artt. 184-bis e 184-ter, testo
  su Normattiva. Binario = pagina indice pinnata `!vig=2026-07-17` (hash stabile
  c2175fe5..., codice 006G0171; stesso indice delle altre skill D.Lgs. 152). Articoli
  letti via AJAX (caricaArticolo, idGruppo 34, idSottoArticolo 2/3) e trascritti verbatim
  in `references/fonti/dlgs-152-2006-184bis-184ter.md`.

Estratto operativo: `references/estratti/sottoprodotti-eow-checklist.md`.

## Punti chiave (verificati sul testo)

- **Sottoprodotto** (art. 184-bis c. 1): non è rifiuto (art. 183 c. 1 lett. a) se ricorrono
  **tutte e quattro** le condizioni cumulative (a: origine da processo di produzione non
  come scopo primario; b: certezza dell'utilizzo; c: nessun trattamento oltre la normale
  pratica industriale; d: utilizzo legale). Criteri con DM (c. 2); c. 2-bis abrogato.
- **End of Waste** (art. 184-ter c. 1): il rifiuto **cessa** di essere tale dopo
  un'**operazione di recupero** se soddisfa le condizioni (a: scopi specifici; b:
  mercato/domanda; c: requisiti tecnici e standard; d: nessun impatto negativo).
- **Criteri** (c. 2): regolamenti UE o caso per caso con DM.
- **In mancanza di criteri** (c. 3): autorizzazioni artt. 208/209/211 e Titolo III-bis, con
  **parere ISPRA/ARPA**; dichiarazione di conformità.
- **Adempimenti**: comunicazioni (c. 3-bis), controlli a campione (c. 3-ter), registro
  **RECER** (c. 3-septies), computo obiettivi (c. 4), disciplina rifiuti fino alla
  cessazione (c. 5), REACH primo utilizzatore (c. 5-bis), **NEW** dal 1/1/2026 (c. 5-ter).

## Convenzioni specifiche

### Cosa NON fare
- Non **classificare in concreto** un materiale: inquadrare le condizioni di legge.
- Non **riprodurre i DM di criterio** (c. 2, es. DM 264/2016 sottoprodotti; regolamenti/DM
  EoW): rinvio.
- Non riprodurre l'art. 183 (definizioni) né gli artt. 208/209/211 (autorizzazioni): rinvio.
- Non **redigere** la dichiarazione di conformità né l'istanza autorizzativa.
- Non citare a memoria: citare il comma (184-bis c. 1-2; 184-ter c. 1-5-quater).

### Cosa fare
- Tenere ferma la distinzione: **sottoprodotto** = mai stato rifiuto; **End of Waste** = è
  stato rifiuto e lo cessa dopo recupero.
- Verificare la **cumulatività** delle condizioni (una che manca → resta rifiuto).
- Distinguere questa skill da `deposito-classificazione-rifiuti-dlgs152` (deposito/HP) e
  `trasporto-rifiuti-fir-dlgs152` (FIR/trasporto).

## Aggiornamento della fonte Normattiva

Testo multivigente: se si aggiorna la skill, ri-pinnare la URL a nuova `!vig=YYYY-MM-DD`,
riscaricare la pagina indice (nuovo hash) e rileggere via AJAX gli articoli modificati.

## Validatori

- Non ancora assegnato (Livello 2 da effettuare con esperto rifiuti/economia circolare).

## Stato attuale

- Versione: 0.1.0-alpha (closes #322)
- Task files: 2 (`verifica-sottoprodotto.md`, `inquadra-end-of-waste.md`)
- Esempi: 2 (segatura come sottoprodotto; aggregato riciclato End of Waste)
