# AGENTS.md - scarichi-emissioni-dlgs152

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale alle **autorizzazioni ambientali singole** (residuali
rispetto ad AUA e AIA) per lo **scarico di acque reflue industriali** (art. 124
D.Lgs. 152/2006, Parte terza) e per le **emissioni in atmosfera** degli
stabilimenti (art. 269, Parte quinta), con le sanzioni (artt. 137, 279). Target:
gestori, consulenti ambientali, uffici provincia/regione/ente d'ambito.

**E' una skill documentale**: non legge i valori limite degli allegati, non
redige le domande, non decide l'inquadramento AUA/AIA.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-152-2006**: D.Lgs. 3/4/2006 n. 152 (TUA), testo multivigente su
  Normattiva. Binario = pagina indice pinnata `!vig=2026-07-14` (hash stabile
  af54f5e0..., pattern della skill aua-dpr59-dossier). Articoli 124 (v. 3), 137,
  269 (v. 7), 279 letti via AJAX (caricaArticolo) e trascritti verbatim in
  `references/fonti/dlgs-152-2006.md`.

Estratto operativo: `references/estratti/scarichi-emissioni-checklist.md`.

## Punti chiave (verificati sul testo)

- **AUA/AIA prima**: se lo stabilimento e' soggetto ad AUA (DPR 59/2013) o AIA
  (art. 29-quattuordecies), scarico ed emissioni **confluiscono** in quel titolo
  (art. 269 c. 1-bis; richiami artt. 137 c. 1, 279 c. 1). La skill copre il caso
  **residuale** dell'autorizzazione singola.
- **Scarico (art. 124)**: tutti gli scarichi preventivamente autorizzati (c. 1);
  autorita' **provincia / ente d'ambito** (c. 7, termine **90 gg**); **durata 4
  anni**, rinnovo **1 anno prima**; sostanze pericolose (art. 108) rinnovo
  espresso entro 6 mesi (c. 8); **nuova autorizzazione/comunicazione** per
  modifiche (c. 12).
- **Emissioni (art. 269)**: autorizzazione per tutti gli stabilimenti che
  emettono (c. 1, salvo art. 272/267), **riferita allo stabilimento**; domanda
  con **progetto + relazione tecnica** (c. 2); **durata 15 anni**, rinnovo 1 anno
  prima (c. 7); **modifiche sostanziali -> nuova autorizzazione** (c. 8).
- **Sanzioni**: scarichi (art. 137) - senza autorizzazione arresto 2 mesi-2 anni
  o ammenda 1.500-10.000, aggravanti sostanze pericolose/valori limite; emissioni
  (art. 279) - senza autorizzazione arresto 2 mesi-2 anni o ammenda 1.000-10.000,
  violazione valori limite arresto fino a 1 anno o ammenda fino a 10.000.

## Convenzioni specifiche

### Cosa NON fare
- Non riprodurre i **valori limite** (Allegato 5 parte terza; Allegati I-V parte
  quinta): rinviare agli allegati.
- Non decidere l'inquadramento **AUA/AIA**: segnalarlo e rinviare.
- Non redigere domande, progetti o relazioni tecniche.
- Non citare a memoria durate/sanzioni: citare l'articolo (124, 137, 269, 279).
- Non confondere la durata dello scarico (4 anni) con quella delle emissioni
  (15 anni).

### Cosa fare
- Verificare **sempre prima** l'eventuale assorbimento in AUA/AIA.
- Distinguere scarico (Parte terza) ed emissioni (Parte quinta) con i rispettivi
  articoli, autorita', durate e sanzioni.
- Chiudere con il rinvio agli allegati e all'autorita' competente.

## Aggiornamento della fonte Normattiva

Testo multivigente (TUA, molto emendato): se si aggiorna la skill, ri-pinnare la
URL a nuova `!vig=YYYY-MM-DD`, riscaricare la pagina indice (nuovo hash) e
rileggere via AJAX gli articoli modificati (usare le versioni piu' alte:
attualmente art. 124 v. 3, art. 269 v. 7).

## Validatori

- Non ancora assegnato (Livello 2 da effettuare con consulente ambientale).

## Stato attuale

- Versione: 0.1.0-alpha (closes #64)
- Task files: 2 (`inquadra-autorizzazione.md`, `checklist-domanda-rinnovo.md`)
- Esempi: 2 (nuovo scarico industriale; nuovo stabilimento con emissioni)
