# definizioni-interventi-edilizi-dpr380

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con tecnico comunale / esperto di diritto edilizio da completare)

Skill di **supporto documentale** alla **qualificazione dell'intervento edilizio**
secondo le **definizioni dell'art. 3 del D.P.R. 380/2001** (Testo unico edilizia):
manutenzione ordinaria/straordinaria, restauro e risanamento conservativo,
ristrutturazione edilizia, nuova costruzione (sottocasi e.1-e.7) e ristrutturazione
urbanistica.

**Non seleziona** il titolo edilizio (CILA/SCIA/PdC — rinvio a
`modulistica-edilizia-unificata`), **non redige** la pratica, **non applica** il Salva
Casa e **non sostituisce** il progettista o il Comune: qualifica la categoria.

## Target

Ingegneri e architetti (progettisti, tecnici comunali) e richiedenti del titolo.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `qualifica-intervento` | Colloca un intervento in una categoria dell'art. 3 (a-f) con i criteri distintivi (volumetria, destinazione d'uso, elementi tipologici, sagoma/sedime, vincoli) |
| `distingui-nuova-costruzione` | Verifica se ricade nella nuova costruzione (lett. e) applicando i sottocasi e.1-e.7 (manufatti, pertinenze oltre il 20%, manufatti leggeri, ecc.) |

Nucleo: **definizioni** dell'art. 3 - manutenzione ordinaria (a), straordinaria (b),
restauro/risanamento (c), ristrutturazione edilizia (d), nuova costruzione (e,
e.1-e.7), ristrutturazione urbanistica (f); **prevalenza** sugli strumenti urbanistici
(c. 2).

## Fonti consultate

- **D.P.R. 6/6/2001 n. 380** (Testo unico edilizia) - art. 3 - testo vigente su
  Normattiva (indice pinnato a `!vig=2026-07-17`, codice 001G0429)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non seleziona** il **titolo edilizio** (edilizia libera / CILA / SCIA / SCIA
  alternativa / PdC): rinvio a `modulistica-edilizia-unificata`; regime del permesso in
  `permesso-costruire-dpr380`.
- **Non redige** la pratica, gli elaborati o l'asseverazione.
- **Non applica** le tolleranze/sanatorie del **Salva Casa** né valuta lo **stato
  legittimo** (art. 9-bis); non tratta il **mutamento di destinazione d'uso** (art.
  23-ter) né i vincoli **paesaggistici/culturali** (D.Lgs. 42/2004).
- **Non sostituisce** il progettista né il Comune.

**La skill è un supporto documentale: non sostituisce il progettista né il Comune, né
la lettura dell'art. 3 del D.P.R. 380/2001.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
