# AGENTS.md - riuso-software-pa-cad69

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale agli obblighi di **acquisizione (analisi comparativa), riuso e
rilascio in open source** del software delle PA (**C.A.D. artt. 68-69**) e alla
**documentazione a corredo** (README, documentazione tecnica, publiccode.yml, tempi,
registrazione su Developers Italia) delle **Linee guida AgID**. Target: PA e loro
fornitori, RTD, uffici IT.

**E' una skill documentale**: inquadra obblighi e contenuti; **non sceglie la licenza**,
non compila campo-per-campo il publiccode.yml e non esegue la valutazione tecnica.

## Nota sull'area e sull'allowlist

Area **software-dati-cybersecurity**. La fonte AgID e' su host istituzionale
**agid.gov.it**, aggiunto (insieme a developers.italia.it) alla allowlist della CI
(`OFFICIAL_HOST_SUFFIXES` in `.github/workflows/scripts/verify-sources.py`) come fonte
ufficiale istituzionale. Complementare a `specifiche-tecniche-ict-appalti-dlgs36` (#50,
D.Lgs 36/2023 art. 79 + CAD art. 68, lato acquisizione/gara): questa copre il **lato
riuso/rilascio** (CAD art. 69) e la documentazione open source.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **cad-68-69**: D.Lgs. 82/2005 (C.A.D.), artt. 68-69, pagina indice Normattiva pinnata a
  `!vig=2026-07-16` (hash 5e75c6b9...; codice 005G0104), articoli via caricaArticolo.
- **linee-guida-riuso-agid**: AgID - Linee guida su acquisizione e riuso di software per
  le PA, PDF ufficiale su agid.gov.it (hash 41925c4d..., 101 pagine). Estratti verbatim
  dell'Allegato A (A.7 README, A.8 documentazione, A.9 tempi, A.11 publiccode.yml /
  Developers Italia).

Trascrizioni in `references/fonti/riuso-software-pa.md`; estratto in
`references/estratti/riuso-software-checklist.md`.

## Punti chiave (verificati sul testo)

- **Art. 68**: analisi comparativa tecnico-economica tra sviluppo ad hoc, riuso, open
  source, cloud, proprietario; principi (riuso, neutralita' tecnologica).
- **Art. 69**: obbligo di rendere disponibile il codice sorgente completo di
  documentazione, in repertorio pubblico sotto licenza aperta, in uso gratuito ad altre
  PA; eccezioni (ordine/sicurezza pubblica, difesa, elezioni).
- **README** (A.7): contenuti MUST/SHOULD (copyright dell'Amministrazione, manutentori,
  e-mail sicurezza).
- **Documentazione** (A.8): formato versionabile riga per riga (HTML/Markdown/reST/LaTeX);
  ODT/DOCX/PDF non ammessi per la tecnica.
- **Tempi** (A.9): 15 giorni se non c'e' sviluppo aperto.
- **publiccode.yml** (A.11): file nella root del repository per la registrazione su
  Developers Italia (formato: github.com/italia/publiccode.yml).

## Convenzioni specifiche

### Cosa NON fare
- Non **scegliere la licenza** al posto dell'Amministrazione.
- Non **riprodurre il formato campo-per-campo del publiccode.yml** (standard Developers
  Italia): rinviare alla documentazione ufficiale del formato.
- Non eseguire la **valutazione comparativa tecnica** ne' redigere codice/documentazione.

### Cosa fare
- Impostare l'analisi comparativa (art. 68) e strutturare il rilascio (art. 69 + Allegato
  A: licenza, README, documentazione, tempi, publiccode.yml).

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del C.A.D. pinnato a nuovo `!vig=` e rileggere artt.
68-69. AgID: verificare eventuali nuove versioni delle Linee guida su agid.gov.it (nuovo
hash del PDF) e del formato publiccode.yml.

## Validatori

- Non ancora assegnato (Livello 2 con RTD / esperto open source PA).

## Stato attuale

- Versione: 0.1.0-alpha (closes #51)
- Task files: 2 (`imposta-analisi-comparativa.md`, `prepara-rilascio-open-source.md`)
- Esempi: 2 (obbligo di rilascio di un gestionale comunale; formati della documentazione)
