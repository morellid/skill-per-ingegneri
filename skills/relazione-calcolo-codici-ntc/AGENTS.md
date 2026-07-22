# AGENTS.md - relazione-calcolo-codici-ntc

Istruzioni per agent che usano o manutengono questa skill.

## Scopo e confini

La skill è un **supporto documentale** per inquadrare, secondo le **NTC 2018 (DM 17 gennaio 2018) Capitolo 10**
(§10.1-10.2.2):

- gli **elaborati del progetto strutturale esecutivo** e la responsabilità del progettista (§10.1);
- i **doveri nell'uso dei codici di calcolo automatico** e la documentazione del software (§10.2);
- i **contenuti della relazione di calcolo** e il **giudizio motivato di accettabilità dei risultati** (§10.2.1);
- la **valutazione indipendente** per opere di particolare importanza (§10.2.2).

**Non** esegue l'analisi né le verifiche, **non** redige la relazione al posto del progettista, **non** valuta né
certifica uno specifico software, **non** sostituisce il progettista né la Circolare 21/1/2019 n. 7.

## Fonte (Regola zero)

- Unica fonte: **PDF ufficiale della Gazzetta Ufficiale** - Supplemento Ordinario n. 8 alla G.U. n. 42 del
  20/02/2018, D.M. 17 gennaio 2018 - **Capitolo 10 (§10.1-10.2.2)** (p. 301-303 GU).
- `not_in_repo/ntc2018-gu42.pdf`, SHA256 `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46`
  (stesso PDF delle altre skill NTC del repo, hash validato live dalla CI su ogni PR).
- Testo trascritto verbatim in `references/fonti/ntc2018-par-10.md`; parafrasi operativa in
  `references/estratti/relazione-calcolo-codici-checklist.md`.
- Il Capitolo 10 è **interamente descrittivo** (procedurale/documentale): **non** contiene formule né costanti
  numeriche, quindi non è stata necessaria la verifica su immagine.

## Contenuti da non alterare (ancorati al testo)

- **Elaborati** (§10.1): relazione di calcolo, relazione materiali, elaborati grafici/particolari, piano di
  manutenzione, relazione risultati sperimentali; **responsabilità del progettista**.
- **Uso dei codici** (§10.2): affidabilità dei codici + attendibilità dei risultati; documentazione software con
  basi teoriche, algoritmi, campi d'impiego, **casi prova con file di input**.
- **Relazione di calcolo** (§10.2.1): tipo di analisi; origine/caratteristiche codici (titolo, autore, produttore,
  versione, licenza); contenuti minimi; **tabulati in allegato**; **giudizio motivato di accettabilità**
  (confronto con calcoli semplici, equilibrio reazioni/carichi).
- **Valutazione indipendente** (§10.2.2): opere di particolare importanza → ricalcolo da soggetto diverso con
  programmi diversi.

Ogni affermazione deve restare rintracciabile in `references/fonti/ntc2018-par-10.md`. Non introdurre requisiti "a
memoria".

## Task

- `tasks/inquadra-elaborati-uso-codici.md` - elaborati del progetto (§10.1) e doveri sull'uso dei codici (§10.2).
- `tasks/inquadra-relazione-giudizio-accettabilita.md` - contenuti della relazione di calcolo, giudizio di
  accettabilità e valutazione indipendente (§10.2.1, 10.2.2).

## Manutenzione

- Se cambiano `title`/`summary`/`area`/`normative_refs` nel frontmatter, **rigenera il catalogo** con
  `uv run scripts/build_catalog.py` nello stesso commit.
- Limiti campi: `summary` ≤ 280, ogni `normative_ref` ≤ 200, `title` ≤ 80.
- Le NTC 2018 sono la versione vigente; se in futuro venissero aggiornate, riscaricare il PDF, ricalcolare l'hash,
  ritrascrivere e solo allora aggiornare gli estratti.
