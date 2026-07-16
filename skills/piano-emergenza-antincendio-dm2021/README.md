# piano-emergenza-antincendio-dm2021

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con tecnico antincendio/RSPP da completare)

Skill di **supporto documentale** all'obbligo e alla struttura del **piano di emergenza ed
evacuazione** nei luoghi di lavoro, ai sensi dell'**art. 46 del D.Lgs. 81/2008** e del
**D.M. 2 settembre 2021** (gestione della sicurezza antincendio in esercizio ed in
emergenza).

**Non esegue la valutazione del rischio incendio**, non riproduce integralmente gli
allegati del D.M. e non certifica il piano.

## Target

Datori di lavoro, RSPP e tecnici che devono stabilire se il piano di emergenza e' dovuto e
come strutturarlo.

## Cosa fa

| Sotto-attivita' | Descrizione |
|---|---|
| `determina-obbligo-piano` | Stabilisce se il piano e' obbligatorio (soglie art. 2 c.2) o se bastano le misure nel DVR (art. 2 c.4) |
| `struttura-piano-e-addetti` | Imposta i contenuti del piano (misure di emergenza, nominativi) e la designazione/formazione degli addetti antincendio (artt. 2 c.3, 4, 5) |

Nucleo: **obbligo del piano** (>= 10 lavoratori; > 50 persone al pubblico; attivita' DPR
151/2011 - art. 2 c.2), **misure nel DVR** se non obbligatorio (c.4), **contenuti** del
piano (c.3), **designazione e formazione addetti** (artt. 4-5), **base** art. 46 D.Lgs
81/2008.

## Fonti consultate

- **D.Lgs. 81/2008 art. 46** - testo vigente su Normattiva (indice pinnato a `!vig=`)
- **D.M. 2 settembre 2021** (gestione sicurezza antincendio in esercizio ed emergenza) -
  Gazzetta Ufficiale (artt. 1-8), attuativo dell'art. 46 c.3

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non esegue la valutazione del rischio incendio** (presupposto del piano e della
  designazione).
- **Non riproduce integralmente** gli allegati I-II-III del D.M. (criteri operativi,
  livelli): li richiama.
- **Non certifica** il piano ne' sostituisce il progetto antincendio (mini-codice DM
  3/9/2021) o le pratiche VV.F. (DPR 151/2011).

**La skill e' un supporto documentale: non sostituisce il datore di lavoro, l'RSPP ne' il
professionista antincendio.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
