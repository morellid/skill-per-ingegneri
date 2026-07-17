# AGENTS.md - obblighi-datore-preposto-formazione-dlgs81

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale alla **ripartizione degli obblighi** di sicurezza tra **datore di lavoro,
dirigente e preposto** e alla **formazione** dei lavoratori, secondo il **D.Lgs. 9 aprile 2008, n. 81**
(artt. 18, 19, 37). Target: ingegneri, datori di lavoro, RSPP, consulenti della sicurezza.

**È una skill documentale**: inquadra chi risponde di cosa e la formazione dovuta; **non redige** il
DVR/verbali, **non riproduce** l'Accordo Stato-Regioni, non sostituisce datore, RSPP, medico competente
o formatore.

## Nota sull'area e complementarità

Area **sicurezza-lavoro-cantieri**. Complementare e distinta da `dvr-generico` (DVR, artt. 17/28),
`duvri-interferenze-dlgs81` (art. 26), `pos-allegato-xv-checker` (art. 96),
`coordinatori-sicurezza-cantieri-dlgs81` (Titolo IV) e `sorveglianza-sanitaria-medico-competente-dlgs81`
(artt. 41): questa copre gli **obblighi generali** (18/19) e la **formazione** (37).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-81-2008-artt-18-19-37**: D.Lgs. 9 aprile 2008, n. 81, pagina indice Normattiva pinnata a
  `!vig=2026-07-17` (hash `18fbc542...`; codice 008G0104). Artt. 18 (idGruppo 3, v12), 19 (idGruppo 3,
  v2), 37 (idGruppo 6, v9) caricati via `caricaArticolo` e trascritti verbatim.

Trascrizione in `references/fonti/dlgs-81-2008-artt-18-19-37.md`; estratto operativo in
`references/estratti/obblighi-formazione-checklist.md`.

## Punti chiave (verificati sul testo)

- **Art. 18**: obblighi del datore/dirigente (medico competente, addetti emergenza, individuazione del
  preposto - lett. b-bis, DPI, sorveglianza sanitaria, informazione/formazione, consegna DVR/DUVRI al
  RLS, comunicazione INAIL infortuni entro **48 ore** - lett. r).
- **NON delegabili** (art. 17, richiamato): **DVR** e **RSPP**.
- **Art. 19**: obblighi del preposto (vigilanza, intervento e **interruzione** dell'attività in caso di
  persistenza o pericolo, segnalazione, corsi ex art. 37).
- **Art. 37**: formazione sufficiente/adeguata; preposti (in presenza) e dirigenti; addestramento;
  orario di lavoro senza oneri; durate/contenuti dall'**Accordo Stato-Regioni**.

## Convenzioni specifiche

### Cosa NON fare
- Non **redigere** il DVR/DUVRI né verbali/attestati di formazione.
- Non **riprodurre** durate/contenuti dell'Accordo Stato-Regioni né gli obblighi settoriali.
- Non valutare la **validità della delega** (art. 16) o le **responsabilità** nel caso concreto.

### Cosa fare
- **Ripartire** gli obblighi (18/19), evidenziare i **non delegabili** (17), **inquadrare** la
  formazione (37) con rinvio all'Accordo Stato-Regioni.

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.Lgs. 81/2008 pinnato a nuovo `!vig=` (nuovo hash) e rileggere gli
artt. 18, 19, 37 (testo tra `(( ))`; es. modifiche D.L. 146/2021 sul preposto).

## Validatori

- Non ancora assegnato (Livello 2 con RSPP / consulente della sicurezza).

## Stato attuale

- Versione: 0.1.0-alpha
- Task files: 2 (`ripartisci-obblighi.md`, `inquadra-formazione.md`)
- Esempi: 2 (ripartizione obblighi e non delegabili; formazione di neoassunti e preposto)
