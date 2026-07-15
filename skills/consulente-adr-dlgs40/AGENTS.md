# AGENTS.md - consulente-adr-dlgs40

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale agli obblighi relativi al **consulente per la sicurezza dei
trasporti di merci pericolose** (DGSA) ai sensi del **D.Lgs. 40/2000**: ambito,
esenzioni, obblighi del capo dell'impresa e del consulente, qualificazione,
sanzioni. Target: imprese di trasporto/carico-scarico di merci pericolose,
consulenti (DGSA), motorizzazione civile.

**E' una skill documentale**: non redige la relazione annuale ne' la relazione
d'incidente, non riproduce gli allegati e non tratta le regole tecniche dell'ADR.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-40-2000**: D.Lgs. 4/2/2000 n. 40, testo multivigente su Normattiva.
  Binario = pagina indice pinnata `!vig=2026-07-14` (hash stabile 369d1349...,
  pattern della skill aua-dpr59-dossier). Articoli 2, 3, 4, 5, 6 letti via AJAX
  (caricaArticolo) e trascritti verbatim in `references/fonti/dlgs-40-2000.md`.

Estratto operativo: `references/estratti/consulente-adr-checklist.md`.

## Punti chiave (verificati sul testo)

- **Ambito** (art. 2): imprese che trasportano merci pericolose (strada,
  ferrovia, via navigabile interna) o effettuano carico/scarico connessi;
  esclusioni al c. 2 (Forze armate/polizia; vie navigabili non collegate all'UE).
- **Esenzioni dalla nomina** (art. 3 c. 6): quantitativi limitati (marginali
  10010/10011 allegato B DM 4/9/1996); trasporti occasionali nazionali con merci
  a pericolosita' minima.
- **Capo dell'impresa** (art. 3): nomina consulente certificato (c. 1-2),
  comunicazione alla motorizzazione civile (c. 3), conservazione relazione 5 anni
  (c. 4), responsabilita' propria (c. 5).
- **Consulente** (art. 4): relazione annuale e a ogni evento modificativo (c. 1-2),
  consegna al capo dell'impresa (c. 3), relazione d'incidente al Ministero via
  motorizzazione (c. 4-5).
- **Qualificazione** (art. 5): certificato di formazione professionale (esame,
  allegato II), eventualmente limitato a classi/modalita'.
- **Sanzioni** (art. 6, in lire): mancata nomina 3-18 mln; comunicazione/
  conservazione 1-6 mln; relazione annuale/incidente 2-12 mln; consegna/
  trasmissione 1-6 mln; vigilanza motorizzazione civile; irroga il prefetto.

## Convenzioni specifiche

### Cosa NON fare
- Non stabilire i **quantitativi limitati**: rinviare all'allegato B del DM
  4/9/1996 e all'ADR.
- Non redigere la **relazione annuale** ne' la **relazione d'incidente** (formato
  ADR 1.8.3).
- Non trattare le **regole tecniche ADR** (classificazione, imballaggi,
  etichettatura) ne' il D.Lgs. 35/2010 oltre ai richiami.
- Non citare a memoria sanzioni: citare l'articolo (2, 3, 4, 5, 6). Riportare gli
  importi in lire come nel testo (importi originari).

### Cosa fare
- Distinguere l'**ambito** (art. 2) dalle **esenzioni** dalla nomina (art. 3 c. 6).
- Distinguere gli obblighi del **capo dell'impresa** (art. 3) da quelli del
  **consulente** (art. 4).
- Ricordare la responsabilita' non delegabile del capo dell'impresa (art. 3 c. 5).

## Aggiornamento della fonte Normattiva

Testo multivigente: se si aggiorna la skill, ri-pinnare la URL a nuova
`!vig=YYYY-MM-DD`, riscaricare la pagina indice (nuovo hash) e rileggere via AJAX
gli articoli modificati; verificare il raccordo con il D.Lgs. 35/2010 e l'ADR
vigente.

## Validatori

- Non ancora assegnato (Livello 2 da effettuare con consulente DGSA).

## Stato attuale

- Versione: 0.1.0-alpha (closes #48)
- Task files: 2 (`verifica-obbligo-nomina.md`, `checklist-adempimenti.md`)
- Esempi: 2 (impresa di autotrasporto obbligata; officina esente)
