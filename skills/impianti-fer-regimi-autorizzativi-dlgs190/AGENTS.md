# AGENTS.md - impianti-fer-regimi-autorizzativi-dlgs190

Istruzioni per agent che usano o manutengono questa skill.

## Scopo e confini

La skill è un **supporto documentale** per inquadrare il **regime amministrativo** di un intervento
su impianti a fonti rinnovabili secondo il **D.Lgs. 25 novembre 2024, n. 190** - **attività libera**
(art. 7, Allegato A), **PAS** (art. 8, Allegato B), **autorizzazione unica** (art. 9, Allegato C) -
e per impostare l'adempimento del **Modello Unico Parte III** alla piattaforma **SUER** previsto dal
**D.M. MASE 15 luglio 2026, n. 223**.

**Non** presenta istanze né compila moduli, **non** riproduce i campi del Modello Unico Parte III,
**non** copre i criteri di idoneità delle aree (art. 11-bis), le zone di accelerazione (art. 12),
l'Allegato C-bis, l'Allegato D, né i modelli unici PAS/AU del D.M. 441/2025. **Non** copre la
disciplina regionale di adeguamento e **non** sostituisce il tecnico abilitato né l'amministrazione
competente.

## Fonti (Regola zero)

1. **D.Lgs. 190/2024**, testo **consolidato** al 9 agosto 2026 - indice Normattiva pinnato
   `!vig=2026-08-09`, SHA256 `5bb983a7cc6a99105d33bbf27dfaf965048329a9e7b3fbe0b440bb067e417930`,
   `not_in_repo/d190-idx.html` (codice redazionale 24G00205, GU Serie generale n. 291 del
   12/12/2024). Artt. 1, 5, 6, 7, 8, 9 e Allegati A, B, C recuperati via `caricaArticolo` nella
   stessa sessione e trascritti verbatim in `references/fonti/dlgs-190-2024-regimi.md`.
2. **D.M. MASE 15 luglio 2026, n. 223** - PDF firmato sul sito istituzionale MASE, SHA256
   `e87b9569f5ba28487fb24c6a71ac2e5fcd2c78996291b36987198f60fc4c7380`,
   `not_in_repo/dm-mase-223-2026.pdf`. Trascrizione integrale in
   `references/fonti/dm-mase-223-2026.md`.

Estratti operativi: `references/estratti/triage-regimi-amministrativi.md` e
`references/estratti/modello-unico-parte-iii-suer.md`.

## Costanti e soglie da non alterare (ancorate al testo)

- **Regimi**: attività libera art. 7 / Allegato A; PAS art. 8 / Allegato B; AU art. 9 / Allegato C
  (art. 6 cc. 1-2). Allegato C **Sez. I = regione**, **Sez. II = MASE** (art. 9 c. 2).
- **Progetto unico** (art. 6 c. 3): medesima fonte + aree vicine + stesso centro di interessi;
  potenza = **somma** delle potenze.
- **Adeguamento regionale**: **180 giorni**, nelle more si applica la disciplina previgente (art. 1
  c. 3).
- **Attività libera**: autorizzazione paesaggistica **30 giorni**, parere Soprintendenza **20
  giorni**, sospensione entro 5 giorni con termine ≤ **15 giorni** prorogabile una volta di ulteriori
  15 (art. 7 cc. 4-5). Esenzioni sempre valide: Allegato A **sez. II lett. a) nn. 1) e 3), b), c),
  e), l)** (art. 7 c. 9).
- **PAS**: silenzio-assenso **30 / 45 / 60 giorni** (cc. 6, 7, 8); sospensione una volta fino a 30
  giorni prorogabile di 30; conferenza convocata entro **5 giorni**, integrazioni entro 10,
  determinazioni entro **45 giorni**; autotutela **6 mesi**; decadenza **2 anni** (avvio) / **3
  anni** (fine lavori); presentazione entro **90 giorni perentori** da VIncA o titolo edilizio (c.
  12-ter); compensazioni **1-3%** oltre **1 MW** (c. 4 lett. m)); termini ridotti di **un terzo** per
  Allegato B sez. I lett. q) e sez. II lett. d) (c. 13).
- **AU**: verifica di assoggettabilità a VIA ≤ **90 giorni** e preventiva; art. 27-bis D.Lgs.
  152/2006 con termine ≤ **2 anni**; istruttoria **10 / 20 / 10 / 30 (+90)** giorni (c. 4);
  consultazione pubblica **30 giorni**; integrazioni post-consultazione ≤ **120 giorni**; conferenza
  conclusa in **120 giorni** con sospensioni **90 / 60 / 120**; garanzie entro **120 giorni**;
  compensazioni **1-4%**; efficacia ≥ **5 anni**; esproprio eseguito entro **1 anno**.
- **Modello Unico Parte III**: trasmissione a SUER entro **5 giorni** dall'entrata in esercizio;
  **6 mesi** per gli impianti già in esercizio; modello disponibile su SUER entro **15 giorni**
  dall'entrata in vigore del D.M.; Parte I e II fino a **200 kW**.

Ogni numero deve restare rintracciabile in `references/fonti/`. Non introdurre valori "a memoria".

## Cosa NON fare

- Non affermare che il **D.M. 223/2026 è entrato in vigore in una data specifica**: il decreto entra
  in vigore il giorno successivo alla pubblicazione sul sito MASE (art. 3 c. 1) e **quella data non
  è nel PDF**. Vale anche per i 15 giorni dell'art. 1 c. 2 e i 6 mesi dell'art. 1 c. 4, che ne
  dipendono. Esprimere le scadenze in forma relativa e segnalare la verifica.
- Non ricostruire i **campi del Modello Unico Parte III**: l'Allegato 1 non è contenuto nel PDF.
- Non descrivere l'ambito del **Modello Unico Parte I e II** come limitato agli impianti "su
  edifici": l'art. 2 c. 1 include anche "strutture e manufatti fuori terra diversi dagli edifici,
  nonché nelle relative pertinenze", fino a 200 kW.
- Non attribuire al D.M. 223/2026 **sanzioni** per la mancata o tardiva trasmissione: il decreto non
  ne prevede.
- Non trattare il vincolo dell'**art. 136 c. 1 lett. c)** del D.Lgs. 42/2004 come causa di
  esclusione dall'attività libera ex art. 7 c. 2: quel comma riguarda la **parte seconda** del
  Codice. La lett. c) attiva invece l'autorizzazione paesaggistica degli artt. 7 cc. 4-5.
- Non citare il **testo originario in GU del 2024**: il decreto è stato novellato (in particolare
  dal **D.Lgs. 178/2025**) e le versioni consolidate trascritte sono elencate in
  `references/fonti/dlgs-190-2024-regimi.md`.
- Non decidere se un'area è **idonea** (art. 11-bis) o in **zona di accelerazione** (art. 12): è
  fuori scope, va segnalato come verifica.

## Task

- `tasks/classifica-regime-amministrativo.md` - determina attività libera / PAS / AU applicando
  progetto unico, allegati, vincoli e interferenze, e mappa termini e documentazione.
- `tasks/adempi-modello-unico-parte-iii.md` - imposta la trasmissione a SUER con termine ordinario
  e transitorio, previa verifica del dies a quo.

## Manutenzione

- Se cambiano `title`/`summary`/`area`/`normative_refs` nel frontmatter, **rigenera il catalogo** con
  `uv run scripts/build_catalog.py` nello stesso commit.
- Limiti campi: `summary` ≤ 280, ogni `normative_ref` ≤ 200, `title` ≤ 80.
- Il D.Lgs. 190/2024 è in evoluzione rapida: a ogni aggiornamento riscaricare l'indice Normattiva
  pinnato (nuovo hash), riscaricare gli articoli e gli allegati, ritrascriverli e solo allora
  aggiornare estratti, task ed esempi. Verificare in particolare l'adeguamento delle regioni (art. 1
  c. 3) e l'eventuale pubblicazione dell'Allegato 1 al D.M. 223/2026.
