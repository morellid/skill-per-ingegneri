# CHANGELOG - videoterminali-vdt-dlgs81

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-17

### Added (closes #317)
- Prima versione della skill di supporto documentale agli obblighi in materia di
  uso di attrezzature munite di videoterminali (VDT), Titolo VII del D.Lgs.
  81/2008 (artt. 172-177).
- Fonte scaricata, hashata e letta (Regola zero):
  - D.Lgs. 9/4/2008 n. 81 - testo multivigente su Normattiva, pagina indice
    pinnata `!vig=2026-07-17` SHA256:
    18fbc5426cc39a513e68c7ae1c6f7a3c09eb4cfc0c4b07a591626259c793bd0e
    (riproducibile, doppio download; codice redazionale 008G0104, stesso indice
    delle altre skill D.Lgs. 81). Articoli 172 (campo di applicazione), 173
    (definizioni), 174 (obblighi del datore), 175 (svolgimento quotidiano -
    pause), 176 (sorveglianza sanitaria) e 177 (informazione e formazione) letti
    via AJAX (caricaArticolo, idGruppo 32 per 172-173, idGruppo 33 per 174-177) e
    trascritti verbatim in `references/fonti/dlgs-81-2008-vdt.md`.
- Estratto operativo `references/estratti/vdt-checklist.md` con campo/esclusioni,
  videoterminalista, obblighi del datore, pause, sorveglianza sanitaria,
  informazione e formazione.
- Due task: `inquadra-videoterminalista-obblighi.md` (applicabilita',
  qualificazione, obblighi e pause) e `imposta-sorveglianza-formazione.md`
  (sorveglianza sanitaria e informazione/formazione).
- Due esempi: videoterminalista con calcolo delle pause (art. 175, 15 min/120) e
  sorveglianza sanitaria per eta'/idoneita' (art. 176, biennale/quinquennale).

### Nota di source-grounding (#317)
La skill e' source-grounded sul **testo vigente del D.Lgs. 81/2008 Titolo VII
letto da Normattiva** (fonte ufficiale). L'**allegato XXXIV** (requisiti minimi
tecnici del posto: schermo, tastiera, piano di lavoro, sedile, ambiente,
interfaccia elaboratore/uomo) richiamato dall'art. 174 e' **citato come rinvio e
non riprodotto**. Gli artt. **41** (sorveglianza sanitaria), **28** (valutazione
dei rischi) e **18** (obblighi del datore) sono citati.

### Note di sviluppo
- Testo multivigente: ad ogni aggiornamento ri-pinnare la URL Normattiva e
  rileggere gli articoli modificati.
- Validazione Livello 2 da effettuare con RSPP / medico competente / ergonomo.
- Possibili estensioni future: trascrizione mirata dell'allegato XXXIV (requisiti
  minimi del posto di lavoro) e raccordo con la valutazione dei rischi (art. 28).
