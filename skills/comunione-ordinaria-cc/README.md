# comunione-ordinaria-cc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con avvocato civilista / esperto di diritti reali da completare)

Skill di **supporto documentale** all'inquadramento della **comunione ordinaria** (comproprietà di
beni: terreni, immobili, cose comuni) nel **Codice civile (R.D. 262/1942)**, Libro III, Titolo VII,
**Capo I (Della comunione in generale)**, artt. 1100-1116: quote, uso, spese, amministrazione,
innovazioni, impugnazioni, scioglimento e divisione.

**Non redige atti** né quantifica quote/spese e **non sostituisce** l'avvocato né il CTU: inquadra
la disciplina della comunione ordinaria.

## Target

Ingegneri, comproprietari e amministratori che devono inquadrare diritti, decisioni, spese,
maggioranze o lo scioglimento di un bene in comunione ordinaria.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-uso-amministrazione` | Inquadra uso della cosa comune, spese, amministrazione a maggioranza per valore, regolamento e innovazioni/atti eccedenti (artt. 1102-1109) |
| `inquadra-scioglimento-divisione` | Inquadra scioglimento, patto di indivisione, divisione in natura e diritti dei creditori (artt. 1111-1116) |

Nucleo: **quote** presunte eguali (1101), **uso** della cosa comune (1102), **spese** (1104),
**amministrazione** a maggioranza per valore delle quote (1105), **innovazioni** a 2/3 e **consenso
unanime** per alienazioni/diritti reali/locazioni > 9 anni (1108), **impugnazioni** a 30 giorni
(1107, 1109), **scioglimento** e **divisione** (1111-1116).

## Fonti consultate

- **Codice civile (R.D. 16 marzo 1942, n. 262)** - artt. 1100-1116 - testo vigente su Normattiva
  (indice pinnato a `!vig=2026-07-17`, codice 042U0262)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non redige** atti (regolamento, delibere, verbali, domanda di divisione, cessione della quota).
- **Non quantifica** quote, spese, conguagli né valori dei beni.
- **Non tratta** il **condominio** negli edifici (artt. 1117 ss., skill
  `condominio-parti-comuni-assemblea-cc`), la comunione legale tra coniugi (artt. 177 ss.) né la
  divisione ereditaria (artt. 713 ss.).

**La skill è un supporto documentale: non sostituisce l'avvocato, il CTU né la lettura degli artt.
1100 ss. del Codice civile e del titolo/regolamento della comunione.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
