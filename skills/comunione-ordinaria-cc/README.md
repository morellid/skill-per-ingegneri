# comunione-ordinaria-cc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con avvocato civilista / esperto di diritti reali da completare)

Skill di **supporto documentale** per il **tecnico** (ingegnere, geometra, CTU/CTP) che opera su un
**bene immobile in comunione ordinaria** (comproprietà di terreni, fabbricati, cose comuni),
disciplinata dal **Codice civile (R.D. 262/1942)**, Libro III, Titolo VII, **Capo I (Della
comunione in generale)**, artt. 1100-1116. Il fulcro è il **compito tecnico della divisione**:
**comoda divisibilità** e **progetto di divisione in natura** (art. 1114), attribuzione con
conguaglio o vendita quando il bene non è divisibile (art. 1116); a supporto, uso, spese e
maggioranze per le opere sulla cosa comune, scioglimento.

**Non dà consulenza legale**, **non redige atti** (atto di divisione, domanda giudiziale) e **non
sostituisce** l'avvocato né il giudice: inquadra il quadro civilistico entro cui il tecnico redige
la propria relazione.

## Target

Ingegneri, geometri e tecnici incaricati (CTU nominati dal giudice, CTP di parte, professionisti che
redigono relazioni di stima/divisione) che devono collocare la propria perizia (comoda divisibilità,
progetto di divisione, stima dei lotti) nel quadro della comunione ordinaria.

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
