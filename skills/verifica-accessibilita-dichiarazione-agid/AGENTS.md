# AGENTS.md - verifica-accessibilita-dichiarazione-agid

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **metodo di verifica dell'accessibilita'** (verifica tecnica +
verifica soggettiva) e alla **dichiarazione di accessibilita'** degli strumenti informatici
(siti web, app mobili, software, documenti), secondo le **Linee guida AgID
sull'accessibilita' degli strumenti informatici** (adottate ex art. 11 L. 4/2004, versione
21/12/2022). Target: PA e fornitori, RTD, uffici IT, grandi operatori privati obbligati.

**E' una skill documentale**: inquadra metodo, contenuti e scadenze; **non esegue l'audit
tecnico** WCAG/EN 301549, non riproduce la norma UNI CEI EN 301549 (a pagamento) ne' compila
la dichiarazione sulla piattaforma AgID.

## Nota sull'area e sulla complementarita'

Area **software-dati-cybersecurity**. La fonte AgID e' su host istituzionale
**agid.gov.it**, gia' in allowlist della CI (`OFFICIAL_HOST_SUFFIXES` in
`.github/workflows/scripts/verify-sources.py`, aggiunto per la skill `riuso-software-pa-cad69`).
Complementare a `accessibilita-siti-app-l4-2004` (obblighi giuridici della Legge Stanca:
soggetti, esclusioni, appalti, vigilanza, sanzioni): questa copre il **metodo di verifica**
e la **dichiarazione**.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **linee-guida-accessibilita-agid**: AgID - Linee guida sull'accessibilita' degli strumenti
  informatici, versione 21/12/2022, PDF ufficiale su agid.gov.it (hash `9043373e...`, 39
  pagine, testo nativo, riproducibile). Estratti verbatim dei capitoli 2 (requisiti), 3
  (verifica), 4 (dichiarazione), 6 (onere sproporzionato), 7 (feedback/Difensore civico).

Trascrizione in `references/fonti/linee-guida-accessibilita-agid.md`; estratto in
`references/estratti/accessibilita-verifica-checklist.md`.

## Punti chiave (verificati sul testo)

- **Requisiti Web** (cap. 2): punto 9 UNI CEI EN 301549; **WCAG 2.1 AA** (nuovi) / **WCAG
  2.0 AA** (pre 23/9/2020). Documenti non web / software: punti 10 e 11.
- **Verifica tecnica** (cap. 3): Prospetti/Appendici EN 301549 (A.1, C.10, C.11).
- **Verifica soggettiva**: obbligatoria **sopra soglia** (art. 35 D.Lgs 50/2016); 4 fasi
  (esperti fattori umani, scala 1-5; gruppo di valutazione con persone con disabilita';
  esecuzione task; rapporto con livelli di qualita'); 12 criteri essenziali.
- **Dichiarazione** (cap. 4): form sulla **piattaforma AgID** (modello Allegato 1); link nel
  footer; riesame **23 settembre**; validita' 24 sett-23 sett; art. 9 L. 4/2004; obiettivi
  annuali PA entro il **31 marzo**.
- **Deroghe** (cap. 6): onere sproporzionato (art. 3-ter L. 4/2004), casi a-h.
- **Attuazione** (cap. 7): feedback (art. 3-bis), Difensore civico digitale (art. 3-quinquies,
  30 giorni).

## Convenzioni specifiche

### Cosa NON fare
- Non **riprodurre la UNI CEI EN 301549** (a pagamento) ne' le **WCAG**: rinviare ai
  punti/Prospetti/Appendici e ai criteri di successo.
- Non **eseguire l'audit** tecnico o soggettivo al posto del soggetto erogatore.
- Non **compilare la dichiarazione** (form sulla piattaforma AgID).
- Non trattare gli **obblighi/sanzioni** della L. 4/2004 (skill `accessibilita-siti-app-l4-2004`).

### Cosa fare
- Impostare la verifica (tecnica + soggettiva, con la soglia art. 35) e strutturare la
  dichiarazione (modello AgID, fonti, link, scadenze) e gli obiettivi annuali.

## Aggiornamento delle fonti

AgID: verificare eventuali nuove versioni delle Linee guida sull'accessibilita' su
agid.gov.it (nuovo hash del PDF) e gli eventuali aggiornamenti della norma UNI CEI EN 301549
e delle WCAG richiamate.

## Validatori

- Non ancora assegnato (Livello 2 con esperto di accessibilita' / RTD).

## Stato attuale

- Versione: 0.1.0-alpha (closes #247)
- Task files: 2 (`imposta-verifica-accessibilita.md`, `predisponi-dichiarazione-accessibilita.md`)
- Esempi: 2 (verifica soggettiva sopra soglia; scadenze annuali della dichiarazione)
