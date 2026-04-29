# Estratto: D.Lgs. 36/2023 Allegato I.7 - Contenuti del progetto esecutivo

**Fonte primaria**: `sources.yaml` id `dlgs-36-2023-originale-gu-2023`
**Documento**: D.Lgs. 31 marzo 2023 n. 36 - Allegato I.7 Sezione III
**Data consultazione**: 2026-04-29
**Licenza**: testo legislativo italiano in pubblico dominio (art. 5 L. 633/1941)

> Sintesi strutturata. Per il testo letterale verificare sempre la versione vigente su Normattiva.

---

## Articoli rilevanti (Sezione III Allegato I.7)

- **Art. 22** - Progetto esecutivo (definizione + elenco elaborati)
- **Art. 23** - Relazione generale (esecutivo)
- **Art. 24** - Relazioni specialistiche
- **Art. 25** - Elaborati grafici (esecutivo)
- **Art. 26** - Calcoli delle strutture e degli impianti
- **Art. 27** - Piano di manutenzione dell'opera e delle sue parti
- **Art. 28** - Piano di sicurezza e di coordinamento

---

## Progetto esecutivo - Elaborati richiesti (art. 22 co. 4)

> **Riferimento normativo**: Allegato I.7 art. 22 co. 4 D.Lgs. 36/2023.

Salva diversa motivata determinazione della stazione appaltante (art. 22 co. 5), il progetto esecutivo e' costituito dai seguenti elaborati:

| Lett. | Elaborato | Articolo dettaglio | Note |
|-------|-----------|--------------------|----|
| a | Relazione generale | art. 23 | Sempre |
| b | Relazioni specialistiche | art. 24 | Tutte le specialistiche del PFTE aggiornate al livello esecutivo |
| c | Elaborati grafici (architettonici, strutturali, impiantistici, opere di mitigazione ambientale) | art. 25 | Sempre |
| d | Calcoli delle strutture e degli impianti | art. 26 | Sempre quando ricorre struttura o impianto rilevante |
| e | Piano di manutenzione dell'opera e delle sue parti | art. 27 | Per l'intero ciclo di vita |
| f | Aggiornamento del piano di sicurezza e di coordinamento (PSC) | art. 28; D.Lgs. 81/2008 art. 100 | Sempre quando cantiere ricade nei presupposti D.Lgs. 81/2008 |
| g | Quadro di incidenza della manodopera | (non articolato a se') | Funzionale allo scorporo costo manodopera (art. 41 co. 14) |
| h | Cronoprogramma | (non articolato a se') | Aggiornamento del cronoprogramma PFTE |
| i | Elenco dei prezzi unitari ed eventuali analisi | (non articolato a se') | Sempre |
| l | Computo metrico estimativo e quadro economico | (non articolato a se') | Sempre |
| m | Schema di contratto e capitolato speciale di appalto | (non articolato a se') | Sempre |
| n | Piano particellare di esproprio aggiornato | (non articolato a se') | Solo se necessarie procedure espropriative |
| o | Relazione tecnica ed elaborati di applicazione dei CAM | DM 256/2022 | Sempre quando applicabili i CAM (PA) |
| p | Fascicolo dell'opera adattato | D.Lgs. 81/2008 Allegato XVI | Sempre quando si applica D.Lgs. 81/2008 |
| p-bis | Modelli informativi | art. 43 D.Lgs. 36/2023 | Solo se BIM obbligatorio |
| p-ter | Capitolato informativo | art. 43 D.Lgs. 36/2023 | Solo se BIM obbligatorio |

---

## Coerenza esecutivo / PFTE

Per art. 41 co. 8, il progetto esecutivo:
- e' **coerente** con il PFTE approvato
- e' di regola redatto dallo stesso soggetto del PFTE
- determina ogni elemento dei lavori in **forma, tipologia, qualita', dimensione e prezzo**
- specifica dettagliatamente lavori, costi e tempi

Differenze rispetto al PFTE:
- **calcoli strutturali e impiantistici dettagliati** (vs calcolo sommario del PFTE)
- **elenco prezzi unitari + computo metrico estimativo definitivo** (vs computo estimativo del PFTE)
- **piano di manutenzione** completo (vs piano preliminare del PFTE)
- **schema di contratto e capitolato speciale d'appalto**
- **fascicolo dell'opera** ai sensi D.Lgs. 81/2008 Allegato XVI

---

## Quando manca / non si applica

Quando uno degli elaborati e' **omesso**, l'omissione deve essere **giustificata** per iscritto dalla stazione appaltante (art. 22 co. 5). Valutare in particolare:

- Calcoli (lett. d): omettibili solo per opere senza componenti strutturali o impiantistiche rilevanti.
- Piano espropri (lett. n): omesso solo se non necessarie espropriazioni.
- Modelli informativi e capitolato informativo (p-bis, p-ter): non richiesti se art. 43 non si applica.
- CAM (lett. o): non richiesti se l'opera non rientra fra quelle soggette al DM 256/2022 o ad altri CAM specifici.

---

## Note operative per la skill

Per la verifica di un progetto esecutivo, la skill controlla la **presenza** dei 14+2 elaborati elencati in art. 22 co. 4 e segnala:
- elaborati mancanti senza giustificazione formale
- elaborati nominati ma vuoti o boilerplate
- coerenza con il PFTE di base (numerazione, denominazione opere, importi)
- presenza degli elementi specifici (CAM, fascicolo, BIM) quando ricorrono i presupposti
