# AGENTS.md - videoterminali-vdt-dlgs81

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale agli **obblighi in materia di uso di attrezzature munite di
videoterminali (VDT)** ai sensi del **Titolo VII del D.Lgs. 81/2008** (artt.
172-177): campo di applicazione ed esclusioni, definizioni (videoterminalista),
obblighi del datore di lavoro, pause, sorveglianza sanitaria, informazione e
formazione. Target: datori di lavoro, RSPP/ASPP, ingegneri della sicurezza,
ergonomi, medici competenti.

**E' una skill documentale**: non redige il DVR-VDT ne' la relazione ergonomica,
non riproduce l'**allegato XXXIV** (requisiti minimi tecnici del posto) e non
esprime giudizi di sorveglianza sanitaria.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-81-2008-vdt**: D.Lgs. 9/4/2008 n. 81, Titolo VII, testo multivigente su
  Normattiva. Binario = pagina indice pinnata `!vig=2026-07-17` (hash stabile
  18fbc542..., codice redazionale 008G0104; stesso indice delle altre skill
  D.Lgs. 81). Articoli 172, 173, 174, 175, 176, 177 letti via AJAX
  (caricaArticolo: idGruppo 32 per 172-173, idGruppo 33 per 174-177) e
  trascritti verbatim in `references/fonti/dlgs-81-2008-vdt.md`.

Estratto operativo: `references/estratti/vdt-checklist.md`.

## Punti chiave (verificati sul testo)

- **Campo di applicazione** (art. 172): si applica alle attivita' che comportano
  l'uso di **VDT**; **escluse** guida di veicoli/macchine, sistemi informatici a
  bordo di mezzi di trasporto, sistemi a **uso prioritario del pubblico**,
  calcolatrici, registratori di cassa, attrezzature con **display di piccole
  dimensioni** per il controllo diretto delle stesse, macchine di videoscrittura
  **senza schermo separato**.
- **Definizioni** (art. 173): **videoterminale**, **posto di lavoro** (VDT,
  tastiera, piano, sedile, ambiente, interfaccia) e **lavoratore
  (videoterminalista)** = chi utilizza il VDT **in modo sistematico o abituale
  per venti ore settimanali**, dedotte le interruzioni di cui all'art. 175.
- **Obblighi del datore** (art. 174): **analisi dei posti** (rischi per la
  vista/occhi, problemi di **postura** e affaticamento fisico o mentale,
  condizioni **ergonomiche/igiene** ambientale); adozione delle misure;
  organizzazione dei posti conforme ai **requisiti minimi dell'allegato XXXIV**.
- **Pause** (art. 175): il videoterminalista ha diritto a interruzione; in
  assenza di disposizione contrattuale, **pausa di 15 minuti ogni 120 minuti** di
  applicazione continuativa; **non cumulabile** a inizio/fine turno; la **pausa
  e' parte dell'orario** di lavoro e non e' riassorbibile.
- **Sorveglianza sanitaria** (art. 176): ex **art. 41**, per rischi **vista e
  occhi** (a) e apparato **muscolo-scheletrico** (b); periodicita' **biennale**
  per idonei con prescrizioni/limitazioni e per chi ha compiuto il **50° anno**,
  altrimenti **quinquennale**; **dispositivi speciali di correzione visiva** a
  carico del datore quando necessari e non sostituibili con quelli normali.
- **Informazione e formazione** (art. 177): il datore fornisce informazione e
  formazione, in particolare su misure applicabili, modalita' di svolgimento
  dell'attivita', protezione degli occhi e della vista.

## Convenzioni specifiche

### Cosa NON fare
- Non **riprodurre l'allegato XXXIV** (requisiti minimi tecnici: schermo,
  tastiera, piano di lavoro, sedile, ambiente, interfaccia): citarlo come rinvio.
- Non **redigere** il DVR-VDT ne' la relazione ergonomica.
- Non esprimere **giudizi di idoneita'/sorveglianza sanitaria** (art. 41): sono
  del medico competente.
- Non citare a memoria soglie o periodicita': citare l'articolo (172-177).

### Cosa fare
- Verificare prima le **esclusioni** (art. 172), poi qualificare il lavoratore
  (art. 173, 20 ore), poi impostare obblighi -> pause -> sorveglianza ->
  formazione.
- Distinguere il **dato di fatto** (superamento effettivo delle 20 ore) dalla
  definizione normativa: la skill inquadra, non accerta l'orario.
- Trattare le **pause** (art. 175) come misura organizzativa distinta dalla
  sorveglianza sanitaria (art. 176).

## Aggiornamento della fonte Normattiva

Testo multivigente: se si aggiorna la skill, ri-pinnare la URL a nuova
`!vig=YYYY-MM-DD`, riscaricare la pagina indice (nuovo hash) e rileggere via AJAX
gli articoli modificati.

## Validatori

- Non ancora assegnato (Livello 2 da effettuare con RSPP / medico competente /
  ergonomo).

## Stato attuale

- Versione: 0.1.0-alpha (closes #317)
- Task files: 2 (`inquadra-videoterminalista-obblighi.md`,
  `imposta-sorveglianza-formazione.md`)
- Esempi: 2 (videoterminalista con pause ex art. 175; sorveglianza sanitaria per
  eta'/idoneita' ex art. 176)
