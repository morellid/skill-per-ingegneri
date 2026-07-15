# AGENTS.md - trasporto-rifiuti-fir-dlgs152

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale agli obblighi del **trasporto dei rifiuti** ai sensi del
**D.Lgs. 152/2006** (Parte quarta): formulario di identificazione (FIR),
iscrizione all'Albo nazionale gestori ambientali, sanzioni. Target: produttori,
trasportatori, gestori ambientali, uffici dell'Albo.

**E' una skill documentale**: non classifica il rifiuto, non redige il formulario,
non riproduce il modello del FIR ne' le regole dell'Albo.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-152-2006**: D.Lgs. 3/4/2006 n. 152 (TUA), testo multivigente su
  Normattiva. Binario = pagina indice pinnata `!vig=2026-07-14` (hash stabile
  af54f5e0..., pattern della skill aua-dpr59-dossier). Articoli 193, 212, 258
  letti via AJAX (caricaArticolo) e trascritti verbatim in
  `references/fonti/dlgs-152-2006.md`.

Estratto operativo: `references/estratti/trasporto-rifiuti-checklist.md`.

## Punti chiave (verificati sul testo)

- **FIR (art. 193)**: obbligo per il trasporto di rifiuti da enti/imprese (c. 1);
  **quattro copie** con firme di produttore/detentore, trasportatore, destinatario
  in arrivo (c. 1); modello/digitalizzazione via **RENTRI** (art. 188-bis, c. 2);
  imballaggio/etichettatura pericolosi (c. 6); esclusioni rifiuti urbani ai centri
  di raccolta (c. 7) e transfrontalieri (c. 9).
- **Albo (art. 212)**: iscrizione **requisito** per raccolta/trasporto, categorie
  e classi, garanzie finanziarie (c. 5); **semplificazione** per i produttori
  iniziali che trasportano i **propri rifiuti** non pericolosi, o pericolosi fino
  a **30 kg/30 l al giorno** come attivita' accessoria (c. 8): niente garanzie,
  iscrizione semplificata.
- **Sanzioni (art. 258 c. 4)**: trasporto senza formulario o con dati incompleti/
  inesatti (non pericolosi) **1.600-10.000 euro**; **rifiuti pericolosi senza
  formulario** **reclusione 1-3 anni** (penale).

## Convenzioni specifiche

### Cosa NON fare
- Non **classificare** il rifiuto (codici EER) ne' redigere il **formulario**.
- Non riprodurre il **modello del FIR**, il **RENTRI** (art. 188-bis) ne' le
  **categorie/classi** dell'Albo.
- Non trattare i **registri di carico/scarico** (art. 190), il **MUD** ne' l'ADR
  oltre ai richiami.
- Non citare a memoria importi/sanzioni: citare l'articolo (193, 212, 258).

### Cosa fare
- Distinguere **conto terzi** (Albo ordinario, art. 212 c. 5) da **propri rifiuti**
  (semplificazione, art. 212 c. 8, soglia 30 kg/30 l per i pericolosi).
- Ricordare che la semplificazione dell'Albo **non esenta** dal **FIR** (art. 193).
- Evidenziare la sanzione **penale** per i pericolosi senza formulario.

## Aggiornamento della fonte Normattiva

Testo multivigente (TUA, molto emendato): se si aggiorna la skill, ri-pinnare la
URL a nuova `!vig=YYYY-MM-DD`, riscaricare la pagina indice (nuovo hash) e
rileggere via AJAX gli articoli modificati; seguire l'entrata a regime del RENTRI
(art. 188-bis) per il modello del formulario.

## Validatori

- Non ancora assegnato (Livello 2 da effettuare con esperto rifiuti/Albo).

## Stato attuale

- Versione: 0.1.0-alpha (closes #65)
- Task files: 2 (`inquadra-obblighi.md`, `checklist-fir.md`)
- Esempi: 2 (trasporto conto terzi; officina con propri rifiuti pericolosi sotto
  soglia)
