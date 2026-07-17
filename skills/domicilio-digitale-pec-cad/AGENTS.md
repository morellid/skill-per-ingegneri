# AGENTS.md - domicilio-digitale-pec-cad

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **domicilio digitale** e ai pubblici elenchi dei domicili digitali
(PEC) secondo il **Codice dell'amministrazione digitale** (D.Lgs. 82/2005): identità e
domicilio digitale (art. 3-bis), utilizzo ed effetti giuridici (art. 6), INI-PEC (art.
6-bis), IPA (art. 6-ter), INAD (art. 6-quater). Target: professionisti, imprese, PA,
cittadini.

**È una skill documentale**: non elegge/registra il domicilio digitale, non effettua
notifiche e non riproduce le Linee guida AgID.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-82-2005-domicilio-digitale**: D.Lgs. 7/3/2005 n. 82 (CAD), artt. 3-bis, 6, 6-bis,
  6-ter, 6-quater, testo su Normattiva. Binario = pagina indice pinnata `!vig=2026-07-17`
  (hash stabile a54022ef..., codice 005G0104; stesso indice della skill
  documento-informatico-firme-cad). Articoli letti via AJAX (caricaArticolo, idGruppo 2) e
  trascritti verbatim in `references/fonti/dlgs-82-2005-domicilio-digitale.md`.

Estratto operativo: `references/estratti/domicilio-digitale-checklist.md`.

## Punti chiave (verificati sul testo)

- **Domicilio digitale** (art. 3-bis): **obbligo** per PA, professionisti in albi/elenchi e
  imprese (INI-PEC o IPA, c. 1); **facoltà** per chiunque altro (INAD, c. 1-bis); domicilio
  **speciale** per determinati atti (c. 4-quinquies).
- **Effetti** (art. 6 c. 1): equiparazione a **raccomandata A/R** e a **notificazione
  postale**; spedizione al gestore, consegna = messa a disposizione; data/ora opponibili se
  conformi alle Linee guida.
- **Notifica diretta** (art. 6 c. 1-quater): la PA notifica al domicilio digitale i propri
  atti, inclusi sanzioni amministrative e atti impositivi.
- **INI-PEC** (6-bis): imprese/professionisti, MISE/MIMIT, mezzo esclusivo con la PA.
- **IPA** (6-ter): PA/gestori pubblici servizi/società a controllo pubblico, AgID,
  aggiornamento semestrale.
- **INAD** (6-quater): persone fisiche/professionisti non obbligati/altri enti, AgID,
  allineamento ANPR.

## Convenzioni specifiche

### Cosa NON fare
- Non **eleggere/registrare** il domicilio digitale né iscrivere negli indici.
- Non **effettuare notifiche** né attestare conformità.
- Non riprodurre le **Linee guida AgID** né i decreti (es. DM MISE 19/3/2013 INI-PEC).
- Non trattare **firme/documento informatico** (skill `documento-informatico-firme-cad`) né
  SPID/CIE in dettaglio (artt. 64/64-bis).
- Non citare a memoria: citare l'articolo/comma (3-bis, 6, 6-bis, 6-ter, 6-quater).

### Cosa fare
- Mappare sempre **soggetto → indice** (PA → IPA; imprese/professionisti in albo → INI-PEC;
  persone fisiche/non obbligati → INAD).
- Distinguere **domicilio digitale** (recapito) da **identità digitale** (accesso, SPID/CIE).
- Sottolineare che la consegna coincide con la **messa a disposizione** (rilevante per la
  notifica).

## Aggiornamento della fonte Normattiva

Testo multivigente: se si aggiorna la skill, ri-pinnare la URL a nuova `!vig=YYYY-MM-DD`,
riscaricare la pagina indice (nuovo hash) e rileggere via AJAX gli articoli modificati.

## Validatori

- Non ancora assegnato (Livello 2 da effettuare con esperto CAD/amministrazione digitale).

## Stato attuale

- Versione: 0.1.0-alpha (closes #326)
- Task files: 2 (`inquadra-domicilio-digitale.md`, `inquadra-effetti-notifica.md`)
- Esempi: 2 (mappatura soggetto→indice; effetti/notifica di una comunicazione PEC)
