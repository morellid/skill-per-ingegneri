# AGENTS.md - direzione-lavori-esecuzione-dlgs36

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale all'**inquadramento** della **direzione dei lavori (DL)** e della
**direzione dell'esecuzione del contratto (DEC)** nella **fase esecutiva** dei **contratti
pubblici**: ruolo del RUP, nomina e compiti del DL, ufficio di direzione lavori, DL come
coordinatore per la sicurezza in esecuzione, DEC per servizi e forniture e casi in cui deve
essere diverso dal RUP, affidamento, secondo l'**art. 114 del D.Lgs. 31 marzo 2023, n. 36**.
Target: ingegneri, RUP, operatori di stazione appaltante.

**E' una skill documentale**: inquadra le figure e i loro compiti; **non nomina** il DL/DEC,
**non redige** gli atti della direzione lavori/esecuzione, non sostituisce la stazione
appaltante ne' il RUP.

## Nota sull'area e sulla complementarita'

Area **appalti-opere-pubbliche**. Complementare a `rup-responsabile-unico-progetto-dlgs36`
(art. 15, figura del RUP), a `collaudo-verifica-conformita-dlgs36`/`modifiche-varianti-
contratti-pubblici-dlgs36`/`garanzie-appalti-pubblici-dlgs36`/`subappalto-contratti-pubblici-
dlgs36` (altri istituti della fase esecutiva) e alle skill dell'area sicurezza per il
coordinatore in esecuzione (D.Lgs. 81/2008). Questa copre l'**inquadramento del DL/DEC**
nell'art. 114.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-36-2023-art114**: D.Lgs. 31 marzo 2023, n. 36, pagina indice Normattiva pinnata a
  `!vig=2026-07-17` (hash `0e9a1938...`; codice 23G00044). Art. 114 (versione 2, idGruppo 18)
  caricato via `caricaArticolo` e trascritto verbatim.

Trascrizione in `references/fonti/dlgs-36-2023-art114.md`; estratto operativo in
`references/estratti/direzione-lavori-checklist.md`.

## Punti chiave (verificati sul testo)

- **Esecuzione diretta dal RUP** (c. 1), che si avvale del DEC/DL, del coordinatore sicurezza
  in esecuzione (D.Lgs. 81/2008) e del collaudatore/verificatore, e accerta lo svolgimento
  delle funzioni.
- **Lavori** (cc. 2-3): DL nominato **prima dell'avvio della procedura**, su **proposta del
  RUP**; eventuale **ufficio di direzione lavori** (direttori operativi, ispettori di cantiere);
  controllo **tecnico, contabile e amministrativo**.
- **DL come CSE** (c. 4): contratti **<= 1 milione di euro** senza lavori complessi/interferenze,
  se il DL ha i requisiti; altrimenti direttore operativo dedicato.
- **Affidamento** (c. 6): PA ai **propri dipendenti**; in mancanza, altre PA o esterno.
- **Servizi e forniture** (cc. 7-10): DEC **di norma dal RUP** (c. 7); l'**allegato II.14**
  individua i contratti per cui il **DEC deve essere diverso dal RUP** (c. 8); assistenti (c.
  10). Carenza competenze -> comma 6 (c. 9).
- **Rinvii** (c. 5): allegato II.14 (attivita' e compiti; secondo periodo soppresso dal D.Lgs.
  209/2024) e allegato I.9 (BIM/figure di supporto).

## Convenzioni specifiche

### Cosa NON fare
- Non **nominare** il DL/DEC ne' proporne i nominativi.
- Non **redigere** gli atti della direzione lavori/esecuzione (verbali, contabilita', ordini di
  servizio, certificati) ne' i piani di sicurezza.
- Non riprodurre gli **allegati II.14 e I.9** ne' gli articoli richiamati (art. 15 RUP, art.
  116 collaudo, D.Lgs. 81/2008, art. 15 L. 241/1990, art. 30 D.Lgs. 267/2000): rinviarvi.

### Cosa fare
- Inquadrare le figure (DL/DEC), il momento della nomina, l'ufficio di direzione lavori, i
  compiti, il DL come CSE e l'affidamento, sui commi dell'art. 114; distinguere lavori (DL) da
  servizi/forniture (DEC).

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.Lgs. 36/2023 pinnato a nuovo `!vig=` (nuovo hash) e
rileggere l'art. 114, verificando le modifiche dei **decreti correttivi** (es. D.Lgs.
209/2024) segnalate dai doppi tondi `(( ))` e dall'indicazione del periodo soppresso.

## Validatori

- Non ancora assegnato (Livello 2 con esperto di contrattualistica pubblica / RUP).

## Stato attuale

- Versione: 0.1.0-alpha (closes #334)
- Task files: 2 (`inquadra-direzione-lavori.md`, `inquadra-direzione-esecuzione.md`)
- Esempi: 2 (nomina del DL e DL come CSE per lavori sotto 1 milione; DEC di norma dal RUP nei
  servizi e casi di DEC diverso dal RUP)
