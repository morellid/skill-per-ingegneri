# CHANGELOG - valutazione-rischio-cem-dlgs81

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-25

### Added (closes #486)
- Prima versione della skill di supporto documentale per la **valutazione del rischio da esposizione dei lavoratori ai
  campi elettromagnetici (CEM)** secondo il **D.Lgs 81/2008, Titolo VIII Capo IV (artt. 206-212 e Allegato XXXVI)**,
  nell'area `sicurezza-lavoro-cantieri`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.Lgs 9 aprile 2008 n. 81** - Testo coordinato Edizione gennaio 2025 (INL) - SHA256
    f593e1806de920dc16def37920c5623cda2450075ed56051852f2caf6045899a (doppio download riproducibile, stesso file usato
    dalle altre skill D.Lgs 81).
  - Artt. 206-212 (e 210-bis) estratti con `pdftotext -layout` (prosa legale) e trascritti in
    `references/fonti/dlgs-81-2008-titolo-viii-capo-iv.md`. Capo IV modificato dal D.Lgs 159/2016 (dir. 2013/35/UE).
- Estratto operativo `references/estratti/valutazione-cem-checklist.md`.
- Due task: `inquadra-valutazione-e-vle.md` e `misure-e-gruppi-sensibili.md`.
- Due esempi: inquadramento della valutazione in un'officina con saldatura/riscaldamento a induzione; gestione di un
  lavoratore portatore di pacemaker (gruppi sensibili).

### Contenuto ancorato al testo
- Campo di applicazione (art. 206): CEM da 0 Hz a 300 GHz; effetti biofisici diretti e indiretti; esclusi effetti a
  lungo termine e contatto con conduttori in tensione. Definizioni (art. 207): effetti diretti termici e non termici;
  effetti indiretti (interferenza con dispositivi medici e stimolatori cardiaci, propulsione di oggetti ferromagnetici,
  innesco di detonatori, incendi/esplosioni, correnti di contatto); VLE relativi agli effetti sanitari e sensoriali; VA
  inferiori e superiori. VLE/VA (art. 208): grandezze fisiche nell'Allegato XXXVI parte I; VLE e VA nelle parti II
  (effetti non termici) e III (effetti termici); i VLE si considerano rispettati se i VA non sono superati; superamenti
  temporanei giustificati con relazione tecnico-protezionistica all'organo di vigilanza. Valutazione (art. 209): parte
  del DVR, con misura/calcolo quando necessario tenendo conto di guide pratiche UE, norme CEI, buone prassi della
  Commissione consultiva e banche dati INAIL; casi in cui misura/calcolo non necessari; attenzione ai lavoratori
  particolarmente sensibili (portatori di dispositivi medici impiantati, lavoratrici in gravidanza), sorgenti multiple
  ed esposizione simultanea a frequenze diverse. Misure (art. 210 + 210-bis): programma d'azione se i VA sono superati;
  segnaletica e accesso limitato per le aree oltre i VA; informazione e formazione; se i VLE sono superati misure
  immediate e registrazione delle cause. Sorveglianza sanitaria (art. 211): periodica, di norma annuale, a cura del
  datore. Deroghe (art. 212): autorizzazione ministeriale ai VLE (DI 30/9/2022).
- I valori numerici VLE/VA dell'Allegato XXXVI (tabelle frequenza-dipendenti) sono referenziati per struttura, non
  riprodotti.

### Scope e limiti
- Non riproduce i valori numerici VLE/VA (Allegato XXXVI); non esegue misure strumentali; non sostituisce il tecnico
  competente in agenti fisici o il medico competente. Non tratta rumore (Capo II), vibrazioni (Capo III) o ROA (Capo V),
  né l'esposizione della popolazione ai CEM (DPCM 2003 / art. 87 CCE).

### Note di sviluppo
- Completa la serie agenti fisici; distinta da `valutazione-rischio-rumore-dlgs81` (Capo II),
  `valutazione-rischio-vibrazioni-dlgs81` (Capo III), `valutazione-cem-elettrodotti-dpcm2003` e
  `valutazione-cem-srb-art-87-cce` (popolazione). Condivide la fonte (Testo coordinato INL del D.Lgs 81/2008).
  Validazione Livello 2 con tecnico competente in agenti fisici / RSPP abilitato.
