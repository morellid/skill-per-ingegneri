# AGENTS.md - accertamento-conformita-sanatoria-dpr380

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **progettista** (geometra/architetto/ingegnere) e al **tecnico incaricato** per
l'**accertamento di conformita'** (permesso di costruire o SCIA **in sanatoria**) degli interventi
edilizi abusivi, ai sensi del **D.P.R. 6 giugno 2001, n. 380, Titolo IV, artt. 36, 36-bis e 37**, come
modificati dal **DL 69/2024 ("salva-casa"), conv. L. 105/2024**. Target: progettisti, uffici tecnici,
sportelli unici per l'edilizia.

**E' una skill documentale per il tecnico**: inquadra presupposti, doppia conformita', oblazione,
termini ed effetti; **non redige** la domanda ne' la dichiarazione di conformita', **non qualifica**
l'abuso, **non calcola** l'oblazione ne' il valore venale.

## Nota sull'area e sulla complementarita'

Area **edilizia-urbanistica-catasto**. Distinta da `vigilanza-sanzioni-abusi-edilizi-dpr380` (artt.
27/31/33/34/44: **vigilanza e sanzioni**, che **esclude** espressamente la sanatoria): questa copre
l'**accertamento di conformita'** (artt. 36/36-bis/37). Complementare a `permesso-costruire-dpr380`,
`edilizia-libera-cila-scia-dpr380` e `definizioni-interventi-edilizi-dpr380` (per la qualificazione
degli interventi).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dpr-380-2001-36-36bis-37**: DPR 380/2001, pagina indice Normattiva pinnata a `!vig=2026-07-17` (hash
  `bac3f7b1...`; codice 001G0429, idGruppo 9). Art. 36 (idSottoArticolo 1, v6), art. 36-bis
  (idSottoArticolo 2, v2), art. 37 (v5) caricati via `caricaArticolo` (formato AKN) e trascritti
  verbatim.

Trascrizione in `references/fonti/dpr-380-2001-36-36bis-37.md`; estratto operativo in
`references/estratti/accertamento-conformita-checklist.md`.

## Punti chiave (verificati sul testo)

- **Art. 36** (assenza titolo/totale difformita'): **doppia conformita' piena** (realizzazione + domanda,
  c. 1); oblazione **contributo doppio** (c. 2); **60 giorni**, **silenzio-rifiuto** (c. 3).
- **Art. 36-bis** (parziale difformita'/variazioni essenziali, **salva-casa**): **doppia conformita'
  attenuata** (urbanistica alla domanda + requisiti edilizi alla realizzazione, c. 1); **dichiarazione
  del professionista** e prova epoca ex art. 9-bis c. 1-bis (c. 3); sismica (c. 3-bis); paesaggistica
  (cc. 4, 5-bis, art. 167 D.Lgs. 42/2004); **oblazione** (c. 5: doppio contributo +20% o doppio valore
  venale, 1.032-10.328 / 516-5.164 euro); **45 giorni**, **silenzio-assenso** (c. 6).
- **Art. 37** (assenza/difformita' SCIA): sanzione **triplo** valore venale, **min 1.032 euro** (c. 1);
  vincolati (cc. 2-3); rinvio all'accertamento **art. 36-bis** (c. 6).

## Convenzioni specifiche

### Cosa NON fare
- Non **redigere** la domanda ne' la **dichiarazione di conformita'** del professionista.
- Non **qualificare** in concreto l'abuso (assenza/totale/parziale difformita'/variazione essenziale) al
  posto del tecnico: e' valutazione tecnica ex artt. 31-34.
- Non **calcolare** l'oblazione ne' il **valore venale**; non trattare il **condono** (leggi speciali).

### Cosa fare
- Stabilire l'articolo applicabile (36/36-bis/37) e la doppia conformita' richiesta; inquadrare
  dichiarazione, oblazione, profili sismici/paesaggistici, termini ed esito (silenzio-rifiuto vs
  silenzio-assenso).

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del DPR 380/2001 pinnato a nuovo `!vig=` (nuovo hash) e rileggere gli
artt. 36, 36-bis e 37 (idSottoArticolo 1/2), verificando le modifiche dei doppi tondi `(( ))` (salva-casa
DL 69/2024, L. 105/2024, ed eventuali interventi successivi).

## Validatori

- Non ancora assegnato (Livello 2 con tecnico edilizio/esperto di sanatorie).

## Stato attuale

- Versione: 0.1.0-alpha (closes #364)
- Task files: 2 (`inquadra-articolo-doppia-conformita.md`, `inquadra-procedura-oblazione-termini.md`)
- Esempi: 2 (veranda in parziale difformita' -> art. 36-bis; ampliamento in assenza di titolo -> art. 36
  con doppia conformita' piena)
