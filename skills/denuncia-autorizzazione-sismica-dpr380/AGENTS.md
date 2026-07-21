# AGENTS.md - denuncia-autorizzazione-sismica-dpr380

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale agli **adempimenti per le costruzioni in zone sismiche** secondo il
**DPR 380/2001**, Parte II, Capo IV: denuncia dei lavori e deposito del progetto (art. 93),
autorizzazione preventiva all'inizio dei lavori (art. 94), classificazione degli interventi
strutturali (art. 94-bis). Target: progettisti, direttori dei lavori, uffici tecnici
regionali, SUE.

**È una skill documentale**: non redige la denuncia/istanza ne' il progetto strutturale, non
esegue calcoli e non sostituisce l'ufficio tecnico regionale/SUE.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dpr-380-2001-93-94-94bis**: D.P.R. 6/6/2001 n. 380, artt. 93, 94, 94-bis, testo su
  Normattiva. Binario = pagina indice pinnata `!vig=2026-07-17` (hash stabile bac3f7b1...,
  codice 001G0429; stesso indice delle altre skill DPR 380). Articoli letti via AJAX
  (caricaArticolo, idGruppo 18) e trascritti verbatim in
  `references/fonti/dpr-380-2001-93-94-94bis.md`.

Estratto operativo: `references/estratti/sismica-checklist.md`.

## Punti chiave (verificati sul testo)

- **Denuncia** (art. 93): in **tutte** le zone sismiche (art. 83), **preavviso scritto** allo
  sportello unico + **deposito del progetto** firmato + **asseverazione** del progettista
  (NTC, coerenza strutture/architettonico); vale come **denuncia ex art. 65**; registro
  comunale.
- **Autorizzazione** (art. 94): nelle localita' sismiche **non a bassa sismicita'**,
  **preventiva autorizzazione** dell'ufficio tecnico regionale prima dell'inizio lavori;
  **30 giorni**, **silenzio assenso** (c. 2-bis), ricorso al presidente della giunta.
- **Classificazione** (art. 94-bis): **rilevanti** (a, zona 1/2 alta, atipiche, strategici →
  **autorizzazione** c. 3), **minore rilevanza** (b) e **privi di rilevanza** (c) → **deroga**
  (c. 4), salvo **controlli a campione** (c. 5); artt. 65 e 67 fermi (c. 6). Linee guida DM
  30/4/2018 e regioni: rinvio.

## Convenzioni specifiche

### Cosa NON fare
- Non **redigere** denuncia/istanza/asseverazione ne' il **progetto strutturale**.
- Non **eseguire calcoli** (NTC): rinvio alle skill NTC.
- Non riprodurre le **linee guida MIT (DM 30/4/2018)** ne' le **procedure regionali**: rinvio.
- Non trattare la **denuncia opere in c.a./acciaio** (art. 65, skill
  `denuncia-opere-strutturali-l1086`) ne' individuare la **zona sismica** (art. 83).
- Non citare a memoria: citare l'articolo/comma (93, 94, 94-bis).

### Cosa fare
- Partire dalla **zona sismica** (1-4, art. 83) e dalla **classificazione** ex art. 94-bis
  per dedurre il regime (autorizzazione vs deposito).
- Distinguere **denuncia/deposito** (sempre in zona sismica, art. 93) da **autorizzazione
  preventiva** (solo interventi rilevanti/localita' non a bassa sismicita').
- Tenere la skill distinta da `denuncia-opere-strutturali-l1086` e dalle skill NTC di calcolo.

## Aggiornamento della fonte Normattiva

Testo multivigente: se si aggiorna la skill, ri-pinnare la URL a nuova `!vig=YYYY-MM-DD`,
riscaricare la pagina indice (nuovo hash) e rileggere via AJAX gli articoli modificati.

## Validatori

- Non ancora assegnato (Livello 2 da effettuare con ingegnere strutturista/ufficio sismica).

## Stato attuale

- Versione: 0.1.0-alpha (closes #330)
- Task files: 2 (`inquadra-denuncia-autorizzazione.md`, `classifica-intervento-sismico.md`)
- Esempi: 2 (nuova costruzione ordinaria in zona 2; adeguamento strategico zona 1 vs
  riparazione locale zona 3)
