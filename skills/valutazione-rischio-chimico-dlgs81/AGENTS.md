# AGENTS.md - valutazione-rischio-chimico-dlgs81

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **datore di lavoro**, all'**RSPP** e al **tecnico della sicurezza** per la
**valutazione del rischio chimico** da agenti chimici pericolosi e le relative **misure di prevenzione e
protezione**, ai sensi del **D.Lgs. 9 aprile 2008, n. 81, Titolo IX, Capo I, artt. 222-227**. Target:
datori di lavoro, RSPP, tecnici della sicurezza, chimici.

**E' una skill documentale per il tecnico**: inquadra obblighi, contenuti e gerarchia delle misure;
**non redige** il DVR/valutazione del rischio chimico, **non esegue** misurazioni ne' applica algoritmi
di stima (es. modelli tipo MoVaRisCh).

## Nota sull'area e sulla complementarita'

Area **sicurezza-lavoro-cantieri**. Distinta da `scheda-dati-sicurezza-sds-reg878` (compilazione della
**SDS** lato **fornitore**, Reg. UE 2020/878) e da `atex-luoghi-lavoro-dlgs81` (atmosfere esplosive,
Titolo XI): questa copre la **valutazione del rischio chimico** lato **datore di lavoro** (Titolo IX
Capo I). Complementare a `dvr-generico` (in cui la valutazione del rischio chimico confluisce),
`sorveglianza-sanitaria-medico-competente-dlgs81` (artt. 229-230) e
`dispositivi-protezione-individuale-dlgs81`.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-81-2008-222-227**: D.Lgs. 81/2008, pagina indice Normattiva pinnata a `!vig=2026-07-17` (hash
  `18fbc542...`; codice 008G0104, idGruppo 41). Artt. 222 (v4), 223 (v4), 224 (v1), 225 (v2), 226 (v1),
  227 (v2) caricati via `caricaArticolo` (formato AKN) e trascritti verbatim.

Trascrizione in `references/fonti/dlgs-81-2008-222-227.md`; estratto operativo in
`references/estratti/rischio-chimico-checklist.md`.

## Punti chiave (verificati sul testo)

- **Definizioni** (art. 222): agente chimico pericoloso = **CLP (Reg. CE 1272/2008)** o con **VLEP**
  (Allegato XXXVIII); **pericolo** (proprieta') vs **rischio** (probabilita').
- **Valutazione** (art. 223): dentro il **DVR (art. 28)**; SDS **REACH**, esposizione, VLEP, effetto
  combinato, attivita' nuove preventive, aggiornamento.
- **Misure generali** (art. 224): eliminare/ridurre; **deroga** se rischio **basso e irrilevante** (no
  artt. 225, 226, 229, 230).
- **Misure specifiche** (art. 225): **sostituzione** poi **gerarchia** (controlli tecnici > collettive >
  DPI > sorveglianza sanitaria); **misurazioni** (Allegato XLI); superamento VLEP -> **organo di
  vigilanza**.
- **Emergenze** (art. 226) e **informazione/formazione** (art. 227): piano, SDS, etichettatura (Titolo
  V).

## Convenzioni specifiche

### Cosa NON fare
- Non **redigere** il DVR ne' la valutazione del rischio chimico; non **eseguire** misurazioni ne'
  applicare **algoritmi di stima** (es. MoVaRisCh).
- Non riprodurre gli **Allegati XXXVIII/XLI** ne' i regolamenti **CLP/REACH**: rinvio.
- Non trattare **cancerogeni/mutageni** (Titolo IX Capo II), **amianto** (Capo III) ne' **ATEX** (Titolo
  XI): rinvio alle skill/temi dedicati.

### Cosa fare
- Inquadrare definizioni (222), criteri e contenuti della valutazione (223), deroga (224), gerarchia
  delle misure e misurazioni (225), emergenze (226), informazione/formazione (227).

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.Lgs. 81/2008 pinnato a nuovo `!vig=` (nuovo hash) e rileggere gli
artt. 222-227, verificando le modifiche dei doppi tondi `(( ))` (es. adeguamenti al CLP, D.Lgs.
39/2016).

## Validatori

- Non ancora assegnato (Livello 2 con RSPP/chimico/medico competente).

## Stato attuale

- Versione: 0.1.0-alpha (closes #358)
- Task files: 2 (`inquadra-valutazione-rischio-chimico.md`, `inquadra-misure-emergenze-formazione.md`)
- Esempi: 2 (verniciatura con solventi: valutazione e gerarchia delle misure; detergente in ufficio:
  deroga per rischio basso/irrilevante)
