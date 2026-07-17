# AGENTS.md - attrezzature-pressione-esercizio-dm329

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale alla **messa in servizio** e alle **verifiche** delle **attrezzature e insiemi
a pressione in esercizio** (fase **post-marcatura CE**): campo di applicazione, verifica di primo
impianto, esclusioni, dichiarazione di messa in servizio, riqualificazione periodica, esenzioni e
verifica di funzionamento, secondo il **D.M. 1 dicembre 2004, n. 329** (artt. 1, 4, 5, 6, 10, 11,
13). Target: ingegneri, datori di lavoro/utilizzatori, tecnici della sicurezza.

**È una skill documentale**: inquadra il metodo; **non esegue** le verifiche, **non redige** la
dichiarazione di messa in servizio, non sostituisce l'utilizzatore, il soggetto verificatore
(INAIL/ASL/soggetti abilitati) né il fabbricante.

## Nota sull'area e sulla complementarità

Area **impianti-macchine-prodotti**. Complementare e **distinta** da `ped-classificazione-conformita`
(marcatura CE / immissione sul mercato, D.Lgs. 93/2000 - che dichiara **DM 329/2004 fuori dal
proprio scope**) e da `verifiche-periodiche-attrezzature-dlgs81` (art. 71 D.Lgs. 81/2008 + DM
11/4/2011): questa copre la **messa in servizio e la riqualificazione periodica** ex DM 329/2004.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dm-329-2004-artt-1-4-5-6-10-11-13**: D.M. 1 dicembre 2004, n. 329, pagina indice Normattiva
  pinnata a `!vig=2026-07-16` (hash `5ee937bb...`; codice 005G0017). Artt. 1, 4, 5, 6, 10, 11, 13
  (idGruppo 0) caricati via `caricaArticolo` e trascritti verbatim.

Trascrizione in `references/fonti/dm-329-2004-artt-1-4-5-6-10-11-13.md`; estratto operativo in
`references/estratti/attrezzature-pressione-checklist.md`.

## Punti chiave (verificati sul testo)

- **Ambito/verifiche** (art. 1): attrezzature ex D.Lgs. 93/2000, preesistenti al 29/5/2002,
  recipienti semplici; verifiche di primo impianto, periodiche, riqualificazione, riparazione.
- **Messa in servizio** (art. 4): dovuta se **installato/assemblato dall'utilizzatore**;
  attestazione; divieto se esito negativo. **Esclusioni** (art. 5).
- **Dichiarazione** (art. 6): a **INAIL (ex ISPESL)** + **ASL**; contenuti a-e; cumulativa per serie
  GPL ≤ 13 m³ / criogenici ≤ 35 m³.
- **Riqualificazione periodica** (art. 10): integrità (art. 12) + funzionamento (art. 13);
  periodicità **allegati A/B** (ridotta dal fabbricante). **Esenzioni** (art. 11) per soglie PS/PS·V.
- **Verifica di funzionamento** (art. 13): rispondenza d'uso + accessori di sicurezza; taratura
  valvole di sicurezza.

## Convenzioni specifiche

### Cosa NON fare
- Non **eseguire** verifiche né rilasciare attestazioni/verbali (INAIL/ASL/soggetti abilitati).
- Non **redigere** la dichiarazione di messa in servizio.
- Non **riprodurre** le tabelle degli **allegati A e B** né gli articoli non trascritti (artt. 2,
  3, 12): rinviare all'atto e al manuale d'uso.
- Non confondere con la **marcatura CE** (D.Lgs. 93/2000, → `ped-classificazione-conformita`).

### Cosa fare
- **Verificare** se è dovuta la messa in servizio (art. 4/5), **comporre** i contenuti della
  dichiarazione (art. 6), **inquadrare** riqualificazione/esenzioni (artt. 10-11-13).
- Usare **INAIL** dove il testo storico cita ISPESL (soppresso, D.L. 78/2010).

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.M. 329/2004 pinnato a nuovo `!vig=` (nuovo hash) e rileggere
gli artt. 1, 4, 5, 6, 10, 11, 13, verificando eventuali modifiche.

## Validatori

- Non ancora assegnato (Livello 2 con tecnico della sicurezza / verificatore INAIL-ASL).

## Stato attuale

- Versione: 0.1.0-alpha
- Task files: 2 (`imposta-messa-in-servizio.md`, `imposta-riqualificazione-periodica.md`)
- Esempi: 2 (messa in servizio serbatoio GPL; esenzione dalla riqualificazione periodica)
