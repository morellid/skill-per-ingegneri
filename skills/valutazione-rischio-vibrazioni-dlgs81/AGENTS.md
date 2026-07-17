# AGENTS.md - valutazione-rischio-vibrazioni-dlgs81

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale alla **valutazione del rischio da vibrazioni meccaniche**
(mano-braccio e corpo intero): definizioni, valori limite e d'azione, valutazione dei
rischi, misure di prevenzione, sorveglianza sanitaria e deroghe, secondo il **D.Lgs.
81/2008, Titolo VIII, Capo III** (artt. 200-205). Target: datori di lavoro, RSPP/ASPP,
ingegneri della sicurezza e tecnici competenti.

**È una skill documentale**: classifica fasce di esposizione e obblighi; **non misura**
né **calcola** i livelli (A(8)), **non redige** il DVR-vibrazioni né la relazione
tecnica, non sostituisce il tecnico competente, il medico competente o il datore di
lavoro.

## Nota sull'area

Area **sicurezza-lavoro-cantieri**. Copre le **vibrazioni** (Capo III del Titolo VIII):
complementare a `valutazione-rischio-rumore-dlgs81` (Capo II, rumore) e alle altre
skill D.Lgs. 81 (`dvr-generico`, `duvri-interferenze-dlgs81`, `atex-luoghi-lavoro-dlgs81`).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-81-2008-vibrazioni**: D.Lgs. 81/2008, pagina indice Normattiva pinnata a
  `!vig=2026-07-17` (hash `18fbc542...`; codice 008G0104; stesso indice della skill
  rumore, atto identico). Artt. 200-205, idGruppo 37, flagTipoArticolo 0, caricati via
  `caricaArticolo` e trascritti verbatim.

Trascrizione in `references/fonti/dlgs-81-2008-vibrazioni.md`; estratto operativo in
`references/estratti/rischio-vibrazioni-checklist.md`.

## Punti chiave (verificati sul testo)

- **Art. 200**: definizioni mano-braccio / corpo intero; esposizione giornaliera A(8).
- **Art. 201**: mano-braccio valore limite **5 m/s²** (breve 20), azione **2,5 m/s²**;
  corpo intero valore limite **1,0 m/s²** (breve 1,5), azione **0,5 m/s²**; livello
  giornaliero massimo ricorrente in caso di variabilita'.
- **Art. 202**: valutazione e, quando necessario, misurazione (metodo di riferimento);
  banche dati ISPESL/regioni/costruttore; allegato XXXV parti A (mano-braccio) e B
  (corpo intero); elementi da considerare (c. 5).
- **Art. 203**: programma di misure oltre i valori d'azione (c. 1); misure immediate se
  superato il valore limite, con individuazione delle cause (c. 2).
- **Art. 204**: sorveglianza sanitaria obbligatoria oltre i valori d'azione (annuale o
  periodicita' motivata; c. 1); estesa secondo il medico competente (c. 2).
- **Art. 205**: deroghe navigazione marittima/aerea (limite corpo intero; c. 1) o
  esposizioni occasionali (media 40 ore; c. 2); organo di vigilanza, max 4 anni (c. 3);
  sorveglianza intensificata (c. 4); prospetto quadriennale UE (c. 5).

## Convenzioni specifiche

### Cosa NON fare
- Non **misurare** né **calcolare** l'A(8): dato d'ingresso o compito del tecnico ex
  art. 202 e allegato XXXV.
- Non **inventare** i valori: usare 5 / 2,5 (mano-braccio) e 1,0 / 0,5 m/s² (corpo
  intero) come da art. 201.
- Non **redigere** il DVR-vibrazioni né la relazione tecnica.

### Cosa fare
- **Classificare** l'esposizione nella fascia corretta e **rinviare** gli obblighi
  (valutazione/misura, misure, sorveglianza, deroghe) con citazione dell'articolo,
  lasciando misura/scelte al datore di lavoro, al tecnico e al medico competente.

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.Lgs. 81/2008 pinnato a nuovo `!vig=` (nuovo
hash) e rileggere gli artt. 200-205 (testo tra `(( ))` = modifiche successive).

## Validatori

- Non ancora assegnato (Livello 2 con tecnico competente / medico competente).

## Stato attuale

- Versione: 0.1.0-alpha
- Task files: 2 (`classifica-esposizione-vibrazioni.md`, `imposta-misure-sorveglianza-deroghe.md`)
- Esempi: 2 (classificazione mano-braccio/corpo intero - art. 201; superamento limite e deroga - artt. 203/205/204)
