# AGENTS.md - valutazione-rischio-cem-dlgs81

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale a **RSPP, datore di lavoro, tecnico competente in agenti fisici e medico competente** per la
**valutazione del rischio da esposizione dei lavoratori ai campi elettromagnetici (CEM)** secondo il **D.Lgs 81/2008,
Titolo VIII Capo IV (artt. 206-212 e Allegato XXXVI)**.

**È una skill documentale per il tecnico**: inquadra la valutazione, il quadro VLE/VA e le misure; **non** esegue misure
strumentali, **non** riproduce i valori numerici dell'Allegato XXXVI e **non** sostituisce il tecnico competente né il
medico competente.

## Nota sull'area e sulla complementarita'

Area **sicurezza-lavoro-cantieri**. Copre il **Capo IV** (CEM). Completa la serie **agenti fisici** del Titolo VIII ed è
**distinta** da:
- `valutazione-rischio-rumore-dlgs81` (Capo II, artt. 187-198);
- `valutazione-rischio-vibrazioni-dlgs81` (Capo III, artt. 199-205);
- le **radiazioni ottiche artificiali** (Capo V, artt. 213-218) restano nella norma.
È inoltre **distinta** dalle skill sull'esposizione della **popolazione** ai CEM:
`valutazione-cem-elettrodotti-dpcm2003` (DPCM 8/7/2003) e `valutazione-cem-srb-art-87-cce` (art. 87 CCE) — framework e
limiti differenti.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-81-2008-consolidato-inl-2025-01**: Testo coordinato del D.Lgs 81/2008 — Edizione gennaio 2025 (INL), SHA256
  `f593e18...` (doppio download riproducibile, stesso file usato dalle altre skill D.Lgs 81). Artt. 206-212 e Allegato
  XXXVI estratti con `pdftotext -layout` (prosa legale, estrazione pulita). Capo IV modificato dal D.Lgs 159/2016
  (recepimento dir. 2013/35/UE). Edizione INL non ufficiale: cross-checkare su Normattiva/Gazzetta Ufficiale.

Trascrizione in `references/fonti/dlgs-81-2008-titolo-viii-capo-iv.md`; estratto operativo in
`references/estratti/valutazione-cem-checklist.md`.

## Punti chiave (dal testo di legge)

- **Campo di applicazione (206)**: CEM 0 Hz-300 GHz; effetti diretti e indiretti; non effetti a lungo termine né
  contatto con conduttori in tensione.
- **Definizioni (207)**: effetti diretti termici/non termici; effetti indiretti (dispositivi medici/pacemaker, oggetti
  ferromagnetici, detonatori, incendi, correnti di contatto); VLE (effetti sanitari/sensoriali); VA (inferiori/superiori).
- **VLE/VA (208 + All. XXXVI)**: grandezze fisiche parte I; VLE e VA parti II-III. VLE rispettati se VA non superati;
  superamenti temporanei con relazione tecnico-protezionistica all'organo di vigilanza.
- **Valutazione (209)**: parte del DVR; misura/calcolo quando necessario (guide UE, CEI, buone prassi, banche dati
  INAIL); casi esclusi; attenzione ai gruppi sensibili (dispositivi medici, gravidanza), sorgenti multiple, frequenze
  diverse.
- **Misure (210 + 210-bis)**: programma d'azione se VA superati; segnaletica e accesso limitato > VA; informazione/
  formazione; gestione superamento VLE (misure immediate + registrazione cause).
- **Sorveglianza sanitaria (211)**: periodica (di norma annuale); a cura del datore. **Deroghe (212)**: autorizzazione
  ministeriale ai VLE (DI 30/9/2022).

## Convenzioni specifiche

### Cosa NON fare
- Non **riprodurre/inventare** i valori numerici VLE/VA dell'Allegato XXXVI (tabelle frequenza-dipendenti): rinviare
  all'allegato.
- Non **eseguire misure** strumentali né decidere l'idoneità sanitaria (medico competente).
- Non confondere il framework **lavoratori** (Titolo VIII Capo IV) con quello della **popolazione** (DPCM 2003 / art.
  87 CCE).
- Non trattare **rumore** (Capo II), **vibrazioni** (Capo III) o **ROA** (Capo V): rinviare alle skill/norme dedicate.
- Non inventare contenuti: ogni elemento deve essere rintracciabile in
  `references/fonti/dlgs-81-2008-titolo-viii-capo-iv.md`.

### Cosa fare
- Aiutare a impostare la valutazione del rischio CEM, il confronto con VLE/VA (rinviando all'allegato) e le misure, con
  attenzione ai gruppi sensibili, citando l'articolo pertinente.

## Aggiornamento delle fonti

D.Lgs 81/2008: se esce una nuova edizione coordinata INL o cambiano gli artt. 206-212 / Allegato XXXVI, riscaricare il
PDF, ricalcolare l'hash con doppio download e riestrarre; cross-checkare su Normattiva.

## Validatori

- Non ancora assegnato (Livello 2 con tecnico competente in agenti fisici / RSPP abilitato).

## Stato attuale

- Versione: 0.1.0-alpha (closes #486)
- Task files: 2 (`inquadra-valutazione-e-vle.md`, `misure-e-gruppi-sensibili.md`)
- Esempi: 2 (inquadramento della valutazione in un'officina con saldatura/induzione; gestione di un lavoratore
  portatore di pacemaker)
