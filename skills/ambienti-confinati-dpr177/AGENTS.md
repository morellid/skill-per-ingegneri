# AGENTS.md - ambienti-confinati-dpr177

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale alla **qualificazione delle imprese/lavoratori autonomi** e
alle **procedure di sicurezza** per i lavori in **ambienti sospetti di
inquinamento o confinati** ai sensi del DPR 177/2011 (artt. 1-4), in raccordo con
il D.Lgs. 81/2008 (artt. 26, 66, 121, allegato IV punto 3). Target: datori di
lavoro committenti e appaltatori, RSPP, coordinatori, consulenti, imprese.

**E' una skill documentale**: non riproduce il D.Lgs. 81/2008, non definisce
regole tecniche (atmosfera, DPI), non redige valutazione dei rischi/POS/DUVRI.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dpr-177-2011**: D.P.R. 14/9/2011 n. 177, testo multivigente su Normattiva.
  Binario = pagina indice pinnata `!vig=2026-07-14` (hash stabile f2163e08...,
  pattern della skill aua-dpr59-dossier). Articoli 1-4 letti via AJAX
  (caricaArticolo) e trascritti verbatim in `references/fonti/dpr-177-2011.md`.

Estratto operativo: `references/estratti/ambienti-confinati-checklist.md`.

## Punti chiave (verificati sul testo)

- **Ambito** (art. 1): ambienti sospetti di inquinamento (artt. 66, 121 D.Lgs.
  81/2008) o confinati (allegato IV punto 3). Le procedure art. 2 c. 2 e art. 3
  c. 1-2 operano **solo in caso di appalto/lavoro autonomo** (art. 26 D.Lgs.
  81/2008).
- **Requisiti di qualificazione** (art. 2 c. 1 lett. a-h): valutazione rischi/
  sorveglianza sanitaria/emergenze; art. 21 c. 2 per familiari/autonomi; **>= 30%
  della forza lavoro con esperienza triennale** (preposti esperti); formazione con
  **verifica di apprendimento**; DPI + addestramento; addestramento su procedure;
  DURC; CCNL.
- **Subappalto** (art. 2 c. 2): vietato salvo autorizzazione espressa del
  committente + certificazione; il DPR si applica anche ai subappaltatori.
- **Procedure di appalto** (art. 3): informazione preventiva del committente
  **>= 1 giorno**; **rappresentante del committente** con funzione di indirizzo e
  coordinamento; **procedura di lavoro specifica** con fase di soccorso e
  coordinamento SSN/VVF; il mancato rispetto **fa venir meno la qualificazione**
  (c. 4).

## Convenzioni specifiche

### Cosa NON fare
- Non riprodurre il testo del D.Lgs. 81/2008 (artt. 26, 66, 121, all. IV punto 3):
  citarli come riferimento.
- Non definire regole tecniche (misurazione atmosfera, scelta DPI, procedure
  operative puntuali): rinvio al manuale del Ministero del lavoro / buone prassi.
- Non redigere valutazione dei rischi, POS o DUVRI.
- Non citare i requisiti "a memoria": citare sempre l'articolo/lettera (art. 2 c.
  1 lett. a-h, art. 3 c. 1-4).
- Non dimenticare che i requisiti valgono anche per il **singolo lavoratore
  autonomo**.

### Cosa fare
- Citare l'articolo/lettera preciso per ogni requisito e adempimento.
- Distinguere i requisiti sempre validi (art. 2 c. 1) dalle procedure che operano
  solo in appalto (art. 2 c. 2, art. 3).
- Segnalare la sanzione qualificatoria (art. 3 c. 4).
- Chiudere con il rinvio alla valutazione dei rischi e ai soggetti responsabili.

## Aggiornamento della fonte Normattiva

Testo multivigente: se si aggiorna la skill, ri-pinnare la URL a nuova
`!vig=YYYY-MM-DD`, riscaricare la pagina indice (nuovo hash) e rileggere via AJAX
gli articoli modificati.

## Validatori

- Non ancora assegnato (Livello 2 da effettuare con RSPP / esperto sicurezza).

## Stato attuale

- Versione: 0.1.0-alpha (closes #44)
- Task files: 2 (`verifica-qualificazione.md`, `checklist-procedure-appalto.md`)
- Esempi: 2 (appalto pulizia serbatoio; lavoratore autonomo non qualificabile)
