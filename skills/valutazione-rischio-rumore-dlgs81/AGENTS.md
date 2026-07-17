# AGENTS.md - valutazione-rischio-rumore-dlgs81

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale alla **valutazione del rischio rumore** negli ambienti di lavoro:
definizioni, valori limite e di azione, valutazione e misurazione, misure di
prevenzione, DPI uditivi e sorveglianza sanitaria, secondo il **D.Lgs. 81/2008,
Titolo VIII, Capo II** (artt. 188-196). Target: datori di lavoro, RSPP/ASPP, ingegneri
della sicurezza e tecnici competenti in acustica.

**È una skill documentale**: classifica fasce di esposizione e obblighi; **non misura**
né **calcola** i livelli (LEX,8h), **non redige** il DVR-rumore né la relazione
fonometrica, non sostituisce il tecnico competente in acustica, il medico competente o
il datore di lavoro.

## Nota sull'area

Area **sicurezza-lavoro-cantieri**. Copre il rumore **occupazionale** (Titolo VIII Capo
II del Testo unico): distinta dalle skill sul rumore **ambientale**
(`valutazione-impatto-clima-acustico-l-447`, `mappatura-acustica-strategica-dlgs194`) e
complementare alle altre skill D.Lgs. 81 (`dvr-generico`, `duvri-interferenze-dlgs81`,
`atex-luoghi-lavoro-dlgs81`).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-81-2008-rumore**: D.Lgs. 81/2008, pagina indice Normattiva pinnata a
  `!vig=2026-07-17` (hash `18fbc542...`; codice 008G0104). Artt. 188, 189, 190, 192,
  193, 196, idGruppo 36, flagTipoArticolo 0, caricati via `caricaArticolo` e trascritti
  verbatim.

Trascrizione in `references/fonti/dlgs-81-2008-rumore.md`; estratto operativo in
`references/estratti/rischio-rumore-checklist.md`.

## Punti chiave (verificati sul testo)

- **Art. 188**: definizioni ppeak, LEX,8h (ISO 1999:1990), LEX,w.
- **Art. 189**: valori limite di esposizione LEX **87 dB(A)** / ppeak **140 dB(C)**;
  superiori di azione **85** / **137**; inferiori di azione **80** / **135**;
  possibilita' di usare LEX,w (≤ 87 dB(A), livello settimanale massimo ricorrente).
- **Art. 190**: contenuti della valutazione (c. 1); **misurazione obbligatoria** se
  superabili i valori inferiori di azione (c. 2); metodi/incertezza (c. 3-4); rinvio ad
  artt. 192-196 e documentazione ex art. 28 c. 2 (c. 5); stima con banche dati (c. 5-bis).
- **Art. 192**: misure di riduzione alla fonte/al minimo (c. 1); programma oltre i
  valori superiori (c. 2); segnaletica/delimitazione/accesso limitato (c. 3); locali di
  riposo (c. 4).
- **Art. 193**: DPI uditivi - **messa a disposizione** ≥ inferiori (c. 1 a), **obbligo
  d'uso** ≥ superiori (c. 1 b); attenuazione considerata **solo** per il valore limite
  (c. 2).
- **Art. 196**: sorveglianza sanitaria **obbligatoria** oltre i valori superiori
  (annuale o periodicita' motivata; c. 1); **estesa su richiesta** oltre gli inferiori
  (c. 2).

## Convenzioni specifiche

### Cosa NON fare
- Non **misurare** né **calcolare** i livelli (LEX,8h, LEX,w, ppeak): sono dati
  d'ingresso o compito del tecnico ex art. 190 c. 2-4.
- Non **inventare** i valori: usare 87 / 85 / 80 dB(A) e 140 / 137 / 135 dB(C) come da
  art. 189.
- Non **redigere** il DVR-rumore né la relazione fonometrica.

### Cosa fare
- **Classificare** l'esposizione nella fascia corretta e **rinviare** gli obblighi
  (misurazione, misure, segnaletica, DPI, sorveglianza) con citazione dell'articolo,
  lasciando misura/scelte al datore di lavoro, al tecnico e al medico competente.

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.Lgs. 81/2008 pinnato a nuovo `!vig=` (nuovo
hash) e rileggere gli artt. 188-196 (testo tra `(( ))` = modifiche successive). Nel
testo il micro (µ) e' reso come `\mu`.

## Validatori

- Non ancora assegnato (Livello 2 con tecnico competente in acustica / medico
  competente).

## Stato attuale

- Versione: 0.1.0-alpha
- Task files: 2 (`classifica-esposizione-valori.md`, `imposta-misure-dpi-sorveglianza.md`)
- Esempi: 2 (classificazione esposizione e obblighi - artt. 189-190; DPI uditivi e sorveglianza per fascia - artt. 193/196)
