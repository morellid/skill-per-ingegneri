# classificazione-rifiuti-dlgs152

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con tecnico ambientale / chimico da completare)

Skill di **supporto documentale** al **tecnico ambientale**, all'**RSGA** e al **produttore/detentore**
per la **classificazione dei rifiuti** (urbani/speciali, pericolosi/non pericolosi) e l'attribuzione dei
**codici dell'elenco europeo (EER)**, ai sensi del **D.Lgs. 3 aprile 2006, n. 152 (Codice
dell'ambiente), Parte IV, artt. 183 e 184**.

**Non attribuisce** il codice EER né la classe di pericolo del singolo rifiuto, **non redige** l'analisi
di caratterizzazione né compila i registri e **non sostituisce** il produttore, il tecnico ambientale o
il laboratorio: inquadra definizioni e criteri.

## Target

Tecnici ambientali, responsabili di sistemi di gestione ambientale (RSGA) e produttori/detentori di
rifiuti che devono inquadrare la classificazione e i codici EER.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-origine-rifiuto` | Stabilisce se è rifiuto (art. 183) e lo classifica per origine in urbano o speciale (art. 184 cc. 1-3) |
| `inquadra-pericolosita-codice` | Inquadra la pericolosità (Allegato I), l'elenco EER (Allegato D, voci a specchio) e l'attribuzione del codice a cura del produttore (art. 184 cc. 4-5) |

Nucleo: **definizioni** di rifiuto/produttore/detentore/deposito temporaneo (art. 183), **classificazione**
per origine (urbani/speciali) e pericolosità (pericolosi/non pericolosi), **elenco EER** (Allegato D) e
attribuzione del codice a cura del produttore (art. 184).

## Fonti consultate

- **D.Lgs. 3 aprile 2006, n. 152** (Codice dell'ambiente) - Parte IV, artt. 183-184 - testo vigente su
  Normattiva (indice pinnato a `!vig=2026-07-17`, codice 006G0171, idGruppo 34).

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non attribuisce** il codice EER né la classe HP del singolo rifiuto; **non redige** l'analisi di
  caratterizzazione né compila registro/FIR/MUD.
- **Non riproduce** gli Allegati D/I/L-quater/L-quinquies né le Linee guida SNPA.
- **Non tratta** il deposito temporaneo (art. 185-bis), i sottoprodotti/EoW (artt. 184-bis/ter) né le
  terre e rocce da scavo (DPR 120/2017) se non nei richiami.

**La skill è un supporto documentale: non sostituisce il produttore, il tecnico ambientale o il
laboratorio, né la lettura degli artt. 183-184 del D.Lgs. 152/2006 e dei relativi allegati.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
