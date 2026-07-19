# CHANGELOG - valutazione-rischio-biologico-dlgs81

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-18

### Added (closes #376)
- Prima versione della skill di supporto al **RSPP/ASPP**, al **datore di lavoro** e al **tecnico della
  sicurezza** per l'inquadramento della **valutazione e gestione del rischio da esposizione ad agenti
  biologici** ai sensi del **D.Lgs. 81/2008, Titolo X (artt. 266-280)**, nell'area
  `sicurezza-lavoro-cantieri`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.Lgs. 81/2008** - indice Normattiva pinnato `!vig=2026-07-17` SHA256:
    18fbc5426cc39a513e68c7ae1c6f7a3c09eb4cfc0c4b07a591626259c793bd0e (codice 008G0104, idGruppo
    48/49/50). Artt. 266 (v1), 267 (v1), 268 (v1), 271 (v1), 272 (v2), 273 (v2), 279 (v2), 280 (v2) via
    `caricaArticolo` (header X-Requested-With, formato AKN).
  - Trascrizione verbatim in `references/fonti/dlgs-81-2008-266-280.md` (testo vigente).
- Estratto operativo `references/estratti/rischio-biologico-checklist.md`.
- Due task: `inquadra-classificazione-valutazione-biologico.md` e
  `inquadra-sorveglianza-registro-biologico.md`.
- Due esempi: laboratorio di analisi microbiologiche con agenti di gruppo 3 (classificazione, valutazione
  e misure); impianto di depurazione con agenti di gruppo 2 (sorveglianza sanitaria e registro degli
  esposti, e cosa cambia con il gruppo 3).

### Contenuto ancorato al testo
- Campo di applicazione (266). Definizioni di agente biologico, microrganismo e coltura cellulare (267).
  Classificazione degli agenti nei quattro gruppi a seconda del rischio di infezione, con l'allegato XLVI
  per i gruppi 2/3/4 e la regola del gruppo più elevato in caso di dubbio (268). Valutazione del rischio
  integrata nel documento dell'art. 17, con classificazione, malattie, effetti allergici/tossici,
  sinergismi, buona prassi microbiologica, rivalutazione almeno triennale, attività dell'allegato XLIV e
  programma di emergenza per i gruppi 3 e 4, con consultazione del RLS (271). Misure tecniche,
  organizzative e procedurali - limitazione degli esposti, segnale di rischio biologico dell'allegato XLV,
  procedure di emergenza, raccolta e smaltimento dei rifiuti (272); misure igieniche - servizi con docce,
  indumenti separati, DPI disinfettati, divieti nelle aree a rischio (273). Prevenzione e controllo con
  sorveglianza sanitaria dell'art. 41, vaccini e allontanamento dell'art. 42 (279). Registri degli esposti
  per i gruppi 3 e 4 e degli eventi accidentali, tenuti tramite l'RSPP con accesso di medico competente e
  RLS, comunicazioni all'organo di vigilanza e conservazione fino a 10 anni, ovvero 40 anni per gli agenti
  con infezioni latenti o gravi sequele (280).

### Scope e limiti
- Non redige il DVR né la valutazione del rischio, non classifica i singoli agenti, non riproduce gli
  Allegati XLIV/XLV/XLVI né definisce i livelli di contenimento (artt. 274-275). Non tratta gli agenti
  chimici (Titolo IX Capo I) né i cancerogeni/mutageni (Titolo IX Capo II). Non sostituisce il datore di
  lavoro, l'RSPP né il medico competente.

### Note di sviluppo
- Completa la copertura del Titolo IX/X del D.Lgs 81 sugli agenti pericolosi, insieme a
  `valutazione-rischio-chimico-dlgs81` e `valutazione-rischio-cancerogeni-mutageni-dlgs81`. Il testo cita
  ancora l'ISPESL (funzioni ora dell'INAIL, L. 122/2010). Validazione Livello 2 con RSPP/tecnico della
  sicurezza o medico competente.
