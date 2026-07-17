# AGENTS.md - dpi-protezione-individuale-dlgs81

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale all'inquadramento degli obblighi in materia di **dispositivi di protezione
individuale (DPI)**: definizioni, obbligo d'uso, requisiti, obblighi del datore di lavoro e dei
lavoratori, criteri per l'individuazione e l'uso, ai sensi del **D.Lgs. 9 aprile 2008, n. 81**,
Titolo III, **Capo II (artt. 74-79)**. Target: ingegneri, datori di lavoro, RSPP, lavoratori.

**E' una skill documentale**: inquadra gli obblighi; **non redige** il DVR, **non seleziona/
classifica** in concreto il DPI, non sostituisce il datore di lavoro, l'RSPP ne' il medico competente.

## Nota sull'area e sulla complementarita'

Area **sicurezza-lavoro-cantieri**. Complementare a `obblighi-datore-preposto-formazione-dlgs81`
(obblighi generali e formazione) e alle skill sui **rischi specifici** (rumore, vibrazioni, MMC,
VDT, ATEX, chimico) che rimandano ai DPI. Questa copre l'**istituto dei DPI** (artt. 74-79).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-81-2008-dpi-74-79**: D.Lgs. 81/2008, pagina indice Normattiva pinnata a `!vig=2026-07-17`
  (hash `18fbc542...`; codice 008G0104 - stesso indice delle altre skill D.Lgs. 81). Artt. 74-79
  (idGruppo 16; versioni 74 v3, 75 v1, 76 v2, 77 v2, 78 v1, 79 v3) caricati via `caricaArticolo`
  (formato AKN) e trascritti verbatim.

Trascrizione in `references/fonti/dlgs-81-2008-dpi-74-79.md`; estratto operativo in
`references/estratti/dpi-checklist.md`.

## Punti chiave (verificati sul testo)

- **Definizione** ed **esclusioni** dei DPI (art. 74).
- **Obbligo d'uso residuale**: DPI solo se la **protezione collettiva** non e' possibile/sufficiente
  (art. 75).
- **Requisiti**: conformita' al **reg. UE 2016/425**, adeguatezza, ergonomia, **compatibilita'** in
  uso simultaneo (art. 76).
- **Obblighi del datore**: valutazione dei rischi e scelta, condizioni d'uso, fornitura,
  manutenzione/igiene, informazione, formazione e **addestramento** (art. 77); addestramento
  **indispensabile** per DPI di **terza categoria** e **protettori dell'udito** (c. 5).
- **Obblighi dei lavoratori**: uso conforme, cura, divieto di modifica, riconsegna, **segnalazione**
  difetti (art. 78).
- **Criteri e rinvii**: allegato VIII e decreto ministeriale; in attesa, DM 2 maggio 2001 (art. 79).

## Convenzioni specifiche

### Cosa NON fare
- Non **redigere** il DVR ne' la valutazione dei rischi.
- Non **selezionare/classificare** in concreto il DPI (categoria, norma tecnica) ne' verificarne la
  marcatura CE.
- Non riprodurre l'**allegato VIII**, il **reg. UE 2016/425**, il **D.Lgs. 475/1992** ne' il **DM 2
  maggio 2001**: rinviarvi.

### Cosa fare
- Inquadrare quando il DPI e' dovuto (uso residuale), i requisiti, gli obblighi del datore (scelta,
  fornitura, formazione, addestramento) e dei lavoratori, sui commi degli artt. 74-79.

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.Lgs. 81/2008 pinnato a nuovo `!vig=` (nuovo hash) e rileggere
gli artt. 74-79, verificando le modifiche segnalate dai doppi tondi `(( ))` (es. adeguamento al reg.
UE 2016/425).

## Validatori

- Non ancora assegnato (Livello 2 con RSPP / esperto di sicurezza sul lavoro).

## Stato attuale

- Versione: 0.1.0-alpha (closes #343)
- Task files: 2 (`inquadra-scelta-dpi.md`, `inquadra-formazione-addestramento.md`)
- Esempi: 2 (imbracatura anticaduta e otoprotettori: uso residuale, requisiti e addestramento
  indispensabile; obblighi del lavoratore che modifica/non usa/non segnala il DPI)
