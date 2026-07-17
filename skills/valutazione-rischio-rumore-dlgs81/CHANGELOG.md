# CHANGELOG - valutazione-rischio-rumore-dlgs81

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-17

### Added (closes #301)
- Prima versione della skill di supporto alla **valutazione del rischio rumore** negli
  ambienti di lavoro, ai sensi del **D.Lgs. 81/2008, Titolo VIII, Capo II** (artt.
  188-196), nell'area `sicurezza-lavoro-cantieri`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.Lgs. 9/4/2008 n. 81** - indice Normattiva pinnato `!vig=2026-07-17`
    SHA256: 18fbc5426cc39a513e68c7ae1c6f7a3c09eb4cfc0c4b07a591626259c793bd0e
    (codice 008G0104). Artt. 188, 189, 190, 192, 193, 196, idGruppo 36,
    flagTipoArticolo 0, via `caricaArticolo`.
  - Trascrizione verbatim in `references/fonti/dlgs-81-2008-rumore.md`.
- Estratto operativo `references/estratti/rischio-rumore-checklist.md`.
- Due task: `classifica-esposizione-valori.md` e `imposta-misure-dpi-sorveglianza.md`.
- Due esempi: classificazione dell'esposizione e obblighi (artt. 189-190); DPI uditivi
  e sorveglianza sanitaria per fascia (artt. 193, 196).

### Contenuto ancorato al testo
- Art. 188 definizioni (ppeak, LEX,8h ISO 1999:1990, LEX,w); art. 189 valori limite 87
  dB(A) / 140 dB(C), superiori di azione 85 / 137, inferiori di azione 80 / 135, con
  base settimanale; art. 190 contenuti della valutazione, obbligo di misurazione oltre
  i valori inferiori, metodi/incertezza, documentazione nel DVR (art. 28 c. 2), stima
  con banche dati (c. 5-bis); art. 192 misure di prevenzione, programma oltre i
  superiori, segnaletica/delimitazione; art. 193 DPI uditivi (messa a disposizione ≥
  inferiori, obbligo d'uso ≥ superiori; attenuazione solo per il valore limite); art.
  196 sorveglianza sanitaria (obbligatoria oltre i superiori, estesa su richiesta oltre
  gli inferiori).

### Scope e limiti
- Non misura né calcola i livelli di esposizione (LEX,8h/LEX,w/ppeak), non redige il
  DVR-rumore né la relazione fonometrica, non tratta gli altri agenti fisici del Titolo
  VIII, non sostituisce il datore di lavoro, il tecnico competente in acustica o il
  medico competente. Artt. 181, 182, 187, 191, 194, 195, 197, 198 e le norme tecniche
  (ISO 1999:1990, UNI) citati e non trascritti.

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del D.Lgs. 81/2008 pinnato
  (nuovo hash) e rileggere gli artt. 188-196 (testo tra `(( ))`). Il micro (µ) e' reso
  come `\mu` nel testo della fonte.
- Validazione Livello 2 con tecnico competente in acustica / medico competente.
