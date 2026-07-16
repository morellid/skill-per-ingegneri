# AGENTS.md - mog-231-sicurezza-lavoro

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **MOG 231 in materia di salute e sicurezza sul lavoro**: il
modello con **efficacia esimente** della responsabilita' amministrativa dell'ente per i
reati di **omicidio colposo e lesioni gravi/gravissime** commessi con violazione delle
norme antinfortunistiche (art. 25-septies D.Lgs 231/2001; requisiti dell'art. 30 D.Lgs
81/2008). Target: ingegneri, RSPP, datori di lavoro, consulenti.

**E' una skill documentale/di inquadramento**: mappa il rischio-reato e struttura i
requisiti del modello; **non redige il modello** e **non ne certifica l'idoneita'**
(riservata al giudice).

## Nota sull'issue e sull'area

Chiude l'issue **#46** (MG.2 MOG D.Lgs 231/2001 - mappatura rischi reato) limitatamente
alla **parte speciale salute e sicurezza sul lavoro**, la piu' rilevante per l'ingegneria.
Sta nell'area **sicurezza-lavoro-cantieri** (non "management": area accantonata dal
maintainer). Mirror del pattern gia' usato per `mog-231-reati-ambientali` (#63, reati
ambientali art. 25-undecies): le due skill coprono le due parti speciali 231 di interesse
ingegneristico (sicurezza e ambiente).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-231-2001**: D.Lgs. 231/2001, pagina indice Normattiva pinnata a `!vig=2026-07-16`
  (hash f6025f50...; codice 001G0293). Artt. 5, 6, 7, 25-septies (idSottoArticolo=7)
  caricati via AJAX e trascritti verbatim.
- **dlgs-81-2008-art30**: D.Lgs. 81/2008, pagina indice Normattiva pinnata a
  `!vig=2026-07-16` (hash d8991985...; codice 008G0104). Art. 30 caricato via AJAX e
  trascritto verbatim.

Trascrizioni in `references/fonti/mog-231-sicurezza-lavoro.md`; estratto in
`references/estratti/mog-231-sicurezza-checklist.md`.

## Punti chiave (verificati sul testo)

- **Responsabilita' dell'ente** (art. 5): reato nell'interesse/vantaggio, da apicali o
  sottoposti; esclusa se interesse esclusivo proprio/di terzi (c.2).
- **Esimente apicali** (art. 6): modello idoneo ed efficacemente attuato + organismo di
  vigilanza + elusione fraudolenta + assenza di omessa vigilanza.
- **Esimente sottoposti** (art. 7): modello idoneo ed efficacemente attuato.
- **Reato presupposto** (art. 25-septies): omicidio colposo (589 c.p.) / lesioni
  gravi-gravissime (590 c.p.) con violazione norme antinfortunistiche; sanzioni in quote e
  interdittive.
- **Requisiti MOG** (art. 30 D.Lgs 81/2008): sistema aziendale per gli obblighi (a-h),
  registrazione (c.2), funzioni + disciplinare (c.3), controllo/riesame (c.4), presunzione
  di conformita' UNI-INAIL SGSL / UNI EN ISO 45001 (c.5), semplificazioni PMI (c.5-bis,
  c.5-ter agg. L. 34/2026), finanziabilita' fino a 50 lavoratori (c.6).

## Convenzioni specifiche

### Cosa NON fare
- Non **redigere il modello** ne' i protocolli operativi.
- Non **certificare l'idoneita'/efficace attuazione** (giudizio del giudice).
- Non trattare **altri reati presupposto 231** (ambientali -> `mog-231-reati-ambientali`;
  o la mappatura generale multi-reato).
- Non spacciare la **ISO 45001** per equivalenza automatica al MOG 231 (presunzione solo
  "per le parti corrispondenti").

### Cosa fare
- Inquadrare presupposti, esimente e reato (artt. 5-7, 25-septies).
- Strutturare i requisiti del MOG ex art. 30 (a-h + registrazione/funzioni/controllo).

## Aggiornamento delle fonti

Normattiva: riscaricare le pagine indice pinnate a un nuovo `!vig=` (nuovi hash) e
rileggere gli artt. 5/6/7/25-septies (231) e l'art. 30 (81), attenzione alle versioni per
articolo e agli aggiornamenti (es. L. 34/2026 su art. 30 c.5-ter).

## Validatori

- Non ancora assegnato (Livello 2 con esperto 231 / legale del lavoro).

## Stato attuale

- Versione: 0.1.0-alpha (closes #46, parte speciale sicurezza sul lavoro)
- Task files: 2 (`mappa-rischio-reato.md`, `struttura-mog-art30.md`)
- Esempi: 2 (impresa di costruzioni; PMI con ISO 45001 e presunzione di conformita')
