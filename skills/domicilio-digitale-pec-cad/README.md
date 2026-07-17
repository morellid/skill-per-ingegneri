# domicilio-digitale-pec-cad

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con esperto CAD/amministrazione digitale da completare)

Skill di **supporto documentale** al **domicilio digitale** e ai pubblici elenchi dei
domicili digitali (PEC): identità e domicilio digitale (art. 3-bis), utilizzo ed effetti
giuridici (art. 6), INI-PEC (art. 6-bis), IPA (art. 6-ter) e INAD (art. 6-quater), secondo
il **Codice dell'amministrazione digitale (D.Lgs. 82/2005)**.

**Non elegge/registra** il domicilio digitale, **non effettua** notifiche, **non riproduce**
le Linee guida AgID e **non sostituisce** i gestori degli indici (AgID, MIMIT) o la PA:
inquadra il regime, l'indice competente e gli effetti.

## Target

Professionisti, imprese, pubbliche amministrazioni, cittadini.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-domicilio-digitale` | Determina l'indice competente (INI-PEC, IPA, INAD) e il regime (obbligo/facoltà) in base al soggetto (art. 3-bis, 6-bis, 6-ter, 6-quater) |
| `inquadra-effetti-notifica` | Inquadra gli effetti giuridici delle comunicazioni al domicilio digitale e la notifica diretta degli atti (art. 6) |

Nucleo: **obbligo** per PA/professionisti in albo/imprese (INI-PEC o IPA) e **facoltà** per
gli altri (INAD) - art. 3-bis; **effetti** delle comunicazioni pari alla **raccomandata
A/R** e alla **notificazione postale** - art. 6; **INI-PEC** imprese/professionisti (6-bis),
**IPA** PA (6-ter), **INAD** persone fisiche (6-quater).

## Fonti consultate

- **D.Lgs. 7/3/2005 n. 82** (CAD) - artt. 3-bis, 6, 6-bis, 6-ter, 6-quater - testo vigente
  su Normattiva (indice pinnato a `!vig=2026-07-17`, codice 005G0104)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non elegge/registra** il domicilio digitale né iscrive negli indici.
- **Non effettua** notifiche né attesta la conformità delle copie.
- **Non riproduce** le Linee guida AgID né i decreti (es. DM MISE 19/3/2013 per INI-PEC).
- **Non tratta** firme elettroniche/documento informatico (skill
  `documento-informatico-firme-cad`) né SPID/CIE in dettaglio (artt. 64/64-bis).
- **Non sostituisce** i gestori degli indici (AgID, MIMIT, InfoCamere) né la PA.

**La skill è un supporto documentale: non sostituisce i gestori degli indici, la PA, né la
lettura degli artt. 3-bis, 6, 6-bis, 6-ter, 6-quater del CAD e delle Linee guida AgID.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
