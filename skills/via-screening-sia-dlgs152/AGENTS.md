# AGENTS.md - via-screening-sia-dlgs152

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale alla **Valutazione di Impatto Ambientale (VIA)** ai sensi
della Parte Seconda del D.Lgs. 152/2006 e del DM 30/03/2015: verifica di
assoggettabilita' (screening, art. 19), Studio Preliminare Ambientale (Allegato
IV-bis), criteri di verifica (Allegato V), Studio di Impatto Ambientale - SIA
(Allegato VII). Target: ingegneri e consulenti ambientali, proponenti.

**E' una skill documentale, non decisionale**: non decide l'assoggettabilita',
non stabilisce le soglie dei progetti, non redige gli studi.

## Fonti autoritative

Catalogate in `references/sources.yaml`:

- **dlgs-152-2006-via**: D.Lgs. 152/2006 Parte Seconda, testo multivigente su
  Normattiva. Binario = pagina indice pinnata `!vig=2026-07-14` (hash stabile
  af54f5e0..., pattern della skill aua-dpr59-dossier). Testo di art. 19, All.
  IV-bis, V, VII caricato via AJAX (caricaArticolo) e trascritto verbatim in
  `references/fonti/dlgs-152-2006-via.md`.
- **dm-30-03-2015-via**: DM 30/03/2015 (GU 84/2015, hash a315fb08...) -
  trascrizione di scopo e meccanismi di adeguamento regionale in
  `references/fonti/dm-30-03-2015-via.md`.

Estratto operativo: `references/estratti/via-screening-sia-checklist.md`.

## Punti chiave (verificati sul testo)

- **Screening (art. 19)**: documento = Studio Preliminare Ambientale (All.
  IV-bis); termini perentori (c. 11): 5/15 gg completezza, 30 gg osservazioni,
  **60 gg** provvedimento (**45 gg** nei casi c. 6), proroga max +20 gg;
  provvedimento motivato sui criteri All. V, efficacia >= 5 anni.
- **Allegato V** (criteri): 1. caratteristiche del progetto; 2. localizzazione
  (aree sensibili, Natura 2000); 3. tipologia/caratteristiche dell'impatto.
- **Allegato IV-bis** (Studio Preliminare Ambientale): 5 punti.
- **Allegato VII** (SIA, art. 22): 12 punti (progetto; alternative con
  alternativa zero; scenario di base; fattori; impatti; metodi; misure e
  monitoraggio; beni culturali; vulnerabilita' Seveso; riassunto non tecnico;
  riferimenti; difficolta').
- **DM 30/03/2015**: per l'allegato IV (competenza regionale), meccanismi di
  adeguamento regionale delle soglie: riduzione in aree sensibili; incremento
  max 30%; criteri di esclusione; sempre conformi all'Allegato V.
- **Progetti soggetti**: allegato II-bis (statale) e allegato IV (regionale):
  elenchi NON trascritti (soglie), da consultare a parte.

## Convenzioni specifiche

### Cosa NON fare
- Non decidere l'assoggettabilita' a VIA (competenza dell'autorita' competente).
- Non affermare che un progetto rientra/non rientra nello screening in base a
  soglie non presenti nella skill: rinviare agli allegati II-bis/IV e al DM
  30/03/2015 + norme regionali.
- Non confondere lo Studio Preliminare Ambientale (All. IV-bis, screening) con il
  SIA (All. VII, VIA vera e propria).
- Non riprodurre i termini "a memoria": citare sempre art. 19 comma/allegato.
- Non trattare la procedura di VIA (artt. 23-27), il PAUR (art. 27-bis), la VAS.

### Cosa fare
- Citare per ogni termine/criterio l'articolo o l'allegato preciso.
- Distinguere il cogente e uniforme (D.Lgs. 152/2006, DM) dalle norme regionali.
- Nelle checklist: esito presente/carente/assente con citazione del documento.
- Chiudere con il rinvio all'autorita' competente e ai tecnici firmatari.

## Aggiornamento della fonte Normattiva

Il testo del D.Lgs. 152/2006 e' multivigente. Se si aggiorna la skill, ri-pinnare
la URL a una nuova `!vig=YYYY-MM-DD`, riscaricare la pagina indice (nuovo hash),
rileggere via AJAX gli articoli modificati e aggiornare la trascrizione e la data
"Testo in vigore dal". L'art. 19 e' spesso modificato (versione corrente in
vigore dal 17-12-2024).

## Validatori

- Non ancora assegnato (Livello 2 da effettuare con esperto VIA / valutatore).

## Stato attuale

- Versione: 0.1.0-alpha (closes #36)
- Task files: 2 (`screening-verifica-assoggettabilita.md`, `checklist-sia.md`)
- Esempi: 2 (cronoprogramma screening progetto regionale; checklist completezza
  SIA con alternative e vulnerabilita' Seveso mancanti)
