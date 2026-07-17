# verifiche-periodiche-attrezzature-dlgs81

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con esperto di sicurezza / verificatore abilitato da completare)

Skill di **supporto documentale** al regime dei **controlli** e delle **verifiche periodiche**
delle **attrezzature di lavoro** (apparecchi di sollevamento, gru, ponti mobili sviluppabili,
generatori di vapore, recipienti/insiemi a pressione), secondo l'**art. 71 e l'Allegato VII
del D.Lgs. 9 aprile 2008, n. 81**.

**Non esegue le verifiche**, **non redige i verbali** e **non riproduce l'Allegato VII** (in
formato grafico): distingue i due regimi e imposta soggetti, termini e oneri.

## Target

Ingegneri, datori di lavoro, RSPP e responsabili della manutenzione che devono impostare prima
verifica e verifiche periodiche delle attrezzature soggette.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-regime-attrezzatura` | Stabilisce se un'attrezzatura è soggetta a soli controlli (art. 71 c. 8-10) o anche a verifiche periodiche dell'Allegato VII (c. 11) |
| `imposta-verifiche-periodiche` | Imposta prima verifica (INAIL, 45 giorni) e verifiche successive (ASL/ARPA/abilitati), oneri e conservazione dei verbali |

Nucleo: **controlli** da persona competente con verbali conservati **3 anni** (c. 8-10);
**verifiche periodiche** delle attrezzature **Allegato VII** (c. 11: **prima verifica INAIL**
entro **45 giorni**, **successive** ASL/ARPA o soggetti abilitati, oneri a carico del datore);
**soggetti privati abilitati** incaricati di pubblico servizio (c. 12); **DM 11/4/2011** per
modalità e abilitazione (c. 13); **VVF** (c. 13-bis); **elenco** aggiornato con decreto (c. 14).

## Fonti consultate

- **D.Lgs. 9 aprile 2008, n. 81** (T.U. sicurezza) - art. 71 e Allegato VII - testo vigente su
  Normattiva (indice pinnato a `!vig=2026-07-16`, codice 008G0104)
- **DM 11 aprile 2011** (modalità delle verifiche e abilitazione dei soggetti) - citato

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non riproduce l'Allegato VII** (elenco attrezzature e periodicità): su Normattiva è "Parte
  di provvedimento in formato grafico" → leggere sull'atto e sul DM 11/4/2011.
- **Non esegue** verifiche/controlli né **redige** i verbali.
- **Non sostituisce** INAIL, ASL/ARPA, i soggetti abilitati né il datore di lavoro; non tratta
  gli ascensori (`verifiche-periodiche-ascensori-dpr162`), gli impianti di terra
  (`verifiche-messa-a-terra-dpr462`) né la conformità PED (`ped-classificazione-conformita`).

**La skill è un supporto documentale: non sostituisce gli enti/soggetti verificatori né la
lettura dell'art. 71, dell'Allegato VII del D.Lgs. 81/2008 e del DM 11 aprile 2011.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
