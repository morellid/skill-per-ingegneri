# valutazione-rischio-cem-dlgs81

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con tecnico competente in agenti fisici / RSPP abilitato da completare)

Skill di **supporto documentale** per la **valutazione del rischio da esposizione dei lavoratori ai campi
elettromagnetici (CEM)** ai sensi del **D.Lgs 81/2008, Titolo VIII Capo IV (artt. 206-212 e Allegato XXXVI)**:
inquadramento della valutazione nel DVR, quando misura/calcolo sono necessari, quadro dei valori limite di esposizione
(VLE) e valori di azione (VA), effetti diretti/indiretti, misure di riduzione e gestione dei gruppi sensibili.

**Non riproduce** i valori numerici VLE/VA dell'Allegato XXXVI, **non esegue** misure strumentali e **non sostituisce**
il tecnico competente in agenti fisici né il medico competente. Completa la serie "agenti fisici" ed è **distinta** da
`valutazione-rischio-rumore-dlgs81` (Capo II) e `valutazione-rischio-vibrazioni-dlgs81` (Capo III), e dalle skill sui
CEM per la **popolazione**.

## Target

RSPP, datori di lavoro, tecnici competenti in agenti fisici e medici competenti che devono impostare o verificare la
valutazione del rischio CEM di un luogo di lavoro (saldatura, riscaldamento a induzione, elettrolisi, apparati RF,
risonanza magnetica, ecc.).

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-valutazione-e-vle` | Imposta la valutazione del rischio CEM (quando misura/calcolo, casi esclusi, elementi di attenzione) e il quadro VLE/VA rinviando all'Allegato XXXVI (artt. 208-209) |
| `misure-e-gruppi-sensibili` | Imposta le misure di riduzione (art. 210), la gestione dei gruppi sensibili (dispositivi medici, gravidanza), l'informazione/formazione, la sorveglianza sanitaria e le deroghe |

Nucleo: CEM da **0 Hz a 300 GHz** (art. 206); **effetti diretti** (termici/non termici) e **indiretti** (dispositivi
medici/pacemaker, oggetti ferromagnetici, detonatori, incendi, correnti di contatto) — art. 207; **VLE** (effetti
sanitari/sensoriali) e **VA** (inferiori/superiori) nell'Allegato XXXVI (art. 208); valutazione parte del DVR con
misura/calcolo quando necessario (art. 209); **misure** e **segnaletica** per aree > VA (art. 210); **gruppi sensibili**,
informazione/formazione (art. 210-bis), **sorveglianza sanitaria** (art. 211), **deroghe** ministeriali (art. 212).

## Relazione con altre skill

- Copre il **Capo IV** (CEM lavoratori). **Distinta** da `valutazione-rischio-rumore-dlgs81` (Capo II),
  `valutazione-rischio-vibrazioni-dlgs81` (Capo III) e dalle skill sull'esposizione della **popolazione**
  (`valutazione-cem-elettrodotti-dpcm2003`, `valutazione-cem-srb-art-87-cce`). Condivide la fonte (Testo coordinato INL
  del D.Lgs 81/2008).

## Fonti consultate

- **D.Lgs 9 aprile 2008 n. 81** — **artt. 206-212 e Allegato XXXVI** — Testo coordinato Edizione gennaio 2025 (INL),
  SHA256 `f593e18...`, estratto con `pdftotext`. Capo IV modificato dal D.Lgs 159/2016 (dir. 2013/35/UE). Edizione INL
  non ufficiale: per uso autoritativo cross-checkare su Normattiva/Gazzetta Ufficiale.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- Non riproduce i **valori numerici VLE/VA** (Allegato XXXVI, tabelle frequenza-dipendenti): il tecnico li legge
  dall'allegato.
- Non è la valutazione di **rumore** (Capo II), **vibrazioni** (Capo III) o **ROA** (Capo V), né l'esposizione della
  **popolazione** ai CEM (DPCM 2003 / art. 87 CCE).
- Non esegue **misure strumentali** né sostituisce il tecnico competente in agenti fisici o il medico competente.

**La skill è un supporto documentale: non riproduce i valori numerici VLE/VA dell'Allegato XXXVI, non esegue misure e non sostituisce il tecnico competente in agenti fisici né il medico competente.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
