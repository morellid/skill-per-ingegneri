# AGENTS.md - accessi-passi-carrabili-cds

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale all'inquadramento di **accessi, diramazioni e passi carrabili** dalla strada
ai fondi/fabbricati laterali: preventiva autorizzazione dell'ente proprietario, regolarizzazione,
divieti e trasformazioni, opere sui fossi, parcheggi per insediamenti, opere particolari e
consorzi, caratteristiche tecniche, sanzioni, secondo l'**art. 22 del D.Lgs. 30 aprile 1992, n.
285** (Codice della Strada). Target: ingegneri, geometri, proprietari, operatori.

**E' una skill documentale**: inquadra il regime autorizzatorio; **non rilascia** l'autorizzazione,
**non redige** l'istanza/progetto, non sostituisce l'ente proprietario/gestore della strada.

## Nota sull'area e sulla complementarita'

Area **ambiente-territorio-mobilita**. Complementare a `cantieri-stradali-occupazione-cds` (artt.
20-21, occupazione sede stradale e cantieri) e a `trasporti-eccezionali-cds-art10` (art. 10):
questa copre gli **accessi e passi carrabili** dell'art. 22.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **cds-285-1992-art22**: D.Lgs. 285/1992 (CdS), pagina indice Normattiva pinnata a
  `!vig=2026-07-17` (hash `e541dc1a...`; codice 092G0306 - stesso indice delle altre skill CdS).
  Art. 22 (versione 17, idGruppo 2) caricato via `caricaArticolo` (formato AKN) e trascritto
  verbatim.

Trascrizione in `references/fonti/cds-285-1992-art22.md`; estratto operativo in
`references/estratti/accessi-passi-carrabili-checklist.md`.

## Punti chiave (verificati sul testo)

- **Autorizzazione preventiva** dell'ente proprietario per nuovi accessi/diramazioni/innesti (c. 1),
  passi carrabili con segnale (c. 3), trasformazioni/variazioni d'uso (c. 4); regolarizzazione degli
  esistenti (c. 2).
- **Diniego** rinviato al regolamento (c. 5); **opere sui fossi** senza alterare sezione/plano-
  altimetria (c. 6); modalita' costruttive nel regolamento (c. 7).
- **Parcheggi** per accessi a insediamenti (c. 8); **opere particolari e consorzi** per proprieta'
  intercluse/forte densita'/carenze di sicurezza (c. 9).
- **Caratteristiche tecniche** con decreto MIT e **divieto** di accessi su rampe di intersezione e
  corsie di accelerazione/decelerazione (c. 10).
- **Sanzioni**: da € 173 a € 694 per accessi non autorizzati/abusivi (c. 11); da € 42 a € 173 per
  altre violazioni (c. 12); importi soggetti ad adeguamento biennale (art. 195, c. 3).

## Convenzioni specifiche

### Cosa NON fare
- Non **rilasciare** l'autorizzazione/concessione ne' esprimere il **diniego** (competono all'ente
  proprietario/gestore).
- Non **redigere** l'istanza, il **progetto** dell'accesso/passo carrabile ne' calcolare le opere.
- Non riprodurre il **Regolamento** (DPR 495/1992, artt. 44-46) ne' i **decreti MIT** sulle
  caratteristiche tecniche; non trattare titolo edilizio/SUE ne' il canone.

### Cosa fare
- Stabilire se serve l'autorizzazione e per quale fattispecie (accesso/diramazione/innesto/passo
  carrabile/trasformazione), inquadrare obblighi (fossi, parcheggi, opere particolari/consorzi),
  divieti (rampe, corsie) e sanzioni, sui commi dell'art. 22.

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del CdS pinnato a nuovo `!vig=` (nuovo hash) e rileggere l'art. 22,
verificando gli **adeguamenti biennali** delle sanzioni (art. 195, c. 3) segnalati dai doppi tondi
`(( ))`.

## Validatori

- Non ancora assegnato (Livello 2 con esperto di polizia stradale / ente proprietario della strada).

## Stato attuale

- Versione: 0.1.0-alpha (closes #339)
- Task files: 2 (`inquadra-autorizzazione-accesso.md`, `verifica-divieti-sanzioni.md`)
- Esempi: 2 (nuovo accesso carrabile a un fondo su strada provinciale; accesso a un insediamento
  senza autorizzazione e in posizione vietata)
