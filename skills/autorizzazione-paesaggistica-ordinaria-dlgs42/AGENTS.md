# AGENTS.md - autorizzazione-paesaggistica-ordinaria-dlgs42

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **progettista** (architetto/ingegnere/geometra) per l'**autorizzazione
paesaggistica ordinaria** e la **relazione paesaggistica** su immobili/aree tutelati: obbligo di
autorizzazione preventiva, documentazione, parere del soprintendente, procedura e termini, efficacia;
accertamento di compatibilita' paesaggistica postumo per interventi minori, ai sensi del **D.Lgs. 22
gennaio 2004, n. 42, artt. 146 e 167**. Target: progettisti, uffici tecnici.

**E' una skill documentale per il tecnico**: inquadra la procedura e i contenuti; **non redige** la
relazione paesaggistica/progetto, **non rilascia** l'autorizzazione/parere, non sostituisce il
progettista ne' gli enti competenti.

## Nota sull'area e sulla complementarita'

Area **edilizia-urbanistica-catasto**. Distinta da `autorizzazione-paesaggistica-semplificata-dpr31`
(procedura **semplificata** per interventi di lieve entita'): questa copre la **procedura ordinaria**
(art. 146). Complementare a `permesso-costruire-dpr380` (l'autorizzazione e' atto **presupposto** al
titolo edilizio) e a `vigilanza-sanzioni-abusi-edilizi-dpr380` (profili edilizi).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-42-2004-146-167**: D.Lgs. 42/2004 (Codice dei beni culturali e del paesaggio), pagina indice
  Normattiva pinnata a `!vig=2026-07-17` (hash `3693219b...`; codice 004G0066). Art. 146 (versione 8,
  idGruppo 26) e art. 167 (versione 4, idGruppo 29) caricati via `caricaArticolo` (formato AKN) e
  trascritti verbatim.

Trascrizione in `references/fonti/dlgs-42-2004-146-167.md`; estratto operativo in
`references/estratti/autorizzazione-paesaggistica-checklist.md`.

## Punti chiave (verificati sul testo)

- **Obbligo** di autorizzazione **preventiva** e **astensione dai lavori** (art. 146 cc. 1-2);
  **relazione paesaggistica** per la verifica di compatibilita', schemi con **DPCM 12/12/2005** (c.
  3).
- **Atto presupposto** al permesso di costruire, **niente sanatoria** (salvo art. 167 cc. 4-5),
  **efficacia 5 anni** + 1 (c. 4).
- **Parere del soprintendente** vincolante/obbligatorio, **45 giorni** (cc. 5, 8); competenza
  **regione**/delega ai **comuni** (c. 6); istruttoria **40 giorni** con relazione tecnica illustrativa
  e proposta (c. 7); **silenzio 60 giorni** e **sostitutivo** (cc. 9-10).
- **Accertamento di compatibilita'** postumo (art. 167 cc. 4-5): solo interventi **minori** (nessun
  volume/superficie utile, materiali difformi, manutenzione); **180 giorni** + parere vincolante
  soprintendenza **90 giorni**; **sanzione pecuniaria** (maggiore tra danno e profitto) o **rimessione
  in pristino**.

## Convenzioni specifiche

### Cosa NON fare
- Non **redigere** la **relazione paesaggistica** ne' il progetto; non **rilasciare** l'autorizzazione
  ne' il **parere**.
- Non riprodurre gli **schemi** della documentazione (**DPCM 12/12/2005**), la **procedura
  semplificata** (**DPR 31/2017**), l'**art. 149** ne' la **disciplina penale** (**art. 181**):
  rinvio.
- Non trattare il vincolo **monumentale** (beni culturali) ne' il titolo edilizio se non nei richiami.

### Cosa fare
- Stabilire se l'autorizzazione e' dovuta (ordinaria vs semplificata/non soggetti), inquadrare
  documentazione, procedura, parere, termini ed efficacia (art. 146) e l'accertamento postumo (art.
  167 cc. 4-5).

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.Lgs. 42/2004 pinnato a nuovo `!vig=` (nuovo hash) e rileggere
gli artt. 146 e 167, verificando le modifiche segnalate dai doppi tondi `(( ))` e dalle indicazioni
di periodo/comma soppresso (es. D.L. 133/2014, D.L. 70/2011).

## Validatori

- Non ancora assegnato (Livello 2 con architetto/esperto di beni paesaggistici).

## Stato attuale

- Versione: 0.1.0-alpha (closes #350)
- Task files: 2 (`inquadra-procedura-ordinaria.md`, `inquadra-accertamento-compatibilita.md`)
- Esempi: 2 (ampliamento in zona vincolata: iter, parere del soprintendente ed efficacia; opere
  gia' realizzate: accertamento di compatibilita' ammesso vs escluso per creazione di volume)
