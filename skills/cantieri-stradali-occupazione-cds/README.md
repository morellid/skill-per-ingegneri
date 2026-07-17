# cantieri-stradali-occupazione-cds

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con esperto CdS/gestione strade da completare)

Skill di **supporto documentale** all'**occupazione della sede stradale** (art. 20) e alle
**opere, depositi e cantieri stradali** (art. 21), secondo il **Codice della Strada (D.Lgs.
285/1992)**: regime autorizzatorio, obblighi di sicurezza e segnalazione, sanzioni.

**Non rilascia** autorizzazioni/concessioni, **non redige** il piano di segnaletica
temporanea, **non riproduce** il Regolamento (DPR 495/1992) né il disciplinare tecnico (DM
10/7/2002) e **non sostituisce** l'ente proprietario/gestore della strada: inquadra il
regime e gli obblighi.

## Target

Tecnici, imprese, enti proprietari/gestori della strada.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-cantiere-stradale` | Verifica l'obbligo di preventiva autorizzazione/concessione (art. 21, art. 26) e gli obblighi di sicurezza/segnalazione del cantiere |
| `inquadra-occupazione-suolo` | Inquadra l'ammissibilità dell'occupazione della sede stradale per tipo di strada e i limiti per chioschi/marciapiedi (art. 20) |

Nucleo: **occupazione** vietata su strade A/B/C/D e ammessa a condizioni su E/F, limiti per
chioschi e marciapiedi (>= 2 m liberi), sanzioni (art. 20); **cantieri** con preventiva
autorizzazione/concessione dell'ente competente, sicurezza e visibilità del personale,
segnalazione secondo il regolamento, sanzioni (art. 21).

## Fonti consultate

- **D.Lgs. 30/4/1992 n. 285** (Codice della Strada) - artt. 20, 21 - testo vigente su
  Normattiva (indice pinnato a `!vig=2026-07-17`, codice 092G0306)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non rilascia** autorizzazioni/concessioni (art. 26): rinvia all'ente.
- **Non redige** il piano di segnaletica temporanea né gli schemi di cantiere.
- **Non riproduce** il Regolamento (DPR 495/1992, artt. 30-43) né il disciplinare DM
  10/7/2002 (schemi segnaletici).
- **Non tratta** la sicurezza dei lavoratori nei cantieri (D.Lgs. 81/2008): fuori perimetro.
- **Non riproduce** la classificazione delle strade (art. 2) né le fasce/distanze (artt.
  16-18).
- **Non sostituisce** l'ente proprietario/gestore né il tecnico/impresa.

**La skill è un supporto documentale: non sostituisce l'ente proprietario/gestore della
strada, il tecnico/impresa, né la lettura degli artt. 20 e 21 del Codice della Strada, del
Regolamento DPR 495/1992 e del DM 10/7/2002.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
