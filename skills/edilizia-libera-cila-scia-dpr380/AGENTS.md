# AGENTS.md - edilizia-libera-cila-scia-dpr380

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale ai **regimi del titolo edilizio** diversi dal permesso di costruire
secondo il **DPR 380/2001** (Testo unico edilizia), Titolo II: attività edilizia libera
(art. 6), CILA (art. 6-bis), SCIA (art. 22), SCIA in alternativa al permesso di costruire
(art. 23). Target: tecnici, progettisti, cittadini, uffici SUE.

**È una skill documentale**: non qualifica in concreto l'intervento (art. 3), non redige
la CILA/SCIA e non tratta il permesso di costruire.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dpr-380-2001-6-6bis-22-23**: D.P.R. 6/6/2001 n. 380, artt. 6, 6-bis, 22, 23, testo su
  Normattiva. Binario = pagina indice pinnata `!vig=2026-07-17` (hash stabile bac3f7b1...,
  codice 001G0429; stesso indice delle altre skill DPR 380). Articoli letti via AJAX
  (caricaArticolo, idGruppo 2 per 6/6-bis, idGruppo 6 per 22/23) e trascritti verbatim in
  `references/fonti/dpr-380-2001-6-6bis-22-23.md`.

Estratto operativo: `references/estratti/titoli-edilizi-checklist.md`.

## Punti chiave (verificati sul testo)

- **Edilizia libera** (art. 6): elenco tassativo di interventi **senza titolo** (lett. a -
  e-sexies), fatte salve le normative di settore; lettere/commi abrogati riportati come da
  fonte; regioni possono estendere (c. 6).
- **CILA** (art. 6-bis): **residuale** (interventi non in artt. 6, 10, 22); comunicazione
  **asseverata**, **niente parti strutturali**; sanzione **1.000 euro** (ridotta di due
  terzi se spontanea).
- **SCIA** (art. 22): ex **art. 19 L. 241/1990**; manutenzione straordinaria/restauro su
  parti strutturali, ristrutturazione non "pesante", varianti a permessi.
- **SCIA alternativa al PdC** (art. 23): ristrutturazione "pesante" (art. 10 c. 1 lett. c) e
  nuova costruzione/ristrutturazione urbanistica in attuazione di piani; **30 giorni** di
  preavviso, relazione del progettista, contributo (art. 16), efficacia **3 anni**, collaudo
  finale.

## Convenzioni specifiche

### Cosa NON fare
- Non **qualificare in concreto** l'intervento (art. 3): rinvio a
  `definizioni-interventi-edilizi-dpr380`.
- Non trattare il **permesso di costruire** (skill `permesso-costruire-dpr380`).
- Non riprodurre il **glossario edilizia libera** (DM 2/3/2018) né la **modulistica
  unificata** (skill `modulistica-edilizia-unificata`).
- Non **redigere** CILA/SCIA/asseverazioni.
- Non citare a memoria: citare l'articolo/comma (6, 6-bis, 22, 23).

### Cosa fare
- Partire sempre dalla **categoria** dell'intervento (art. 3) per scegliere il titolo.
- Distinguere il **discrimine strutturale** tra CILA (no parti strutturali) e SCIA (art. 22
  lett. a-b su parti strutturali).
- Segnalare **vincoli** (assensi preventivi/conferenza di servizi) e **discipline
  regionali** (ampliamento/riduzione degli ambiti).

## Aggiornamento della fonte Normattiva

Testo multivigente: se si aggiorna la skill, ri-pinnare la URL a nuova `!vig=YYYY-MM-DD`,
riscaricare la pagina indice (nuovo hash) e rileggere via AJAX gli articoli modificati.

## Validatori

- Non ancora assegnato (Livello 2 da effettuare con tecnico abilitato/esperto edilizia).

## Stato attuale

- Versione: 0.1.0-alpha (closes #325)
- Task files: 2 (`scegli-titolo-edilizio.md`, `imposta-scia-alternativa.md`)
- Esempi: 2 (CILA vs SCIA per manutenzione straordinaria; edilizia libera e SCIA
  alternativa al PdC)
