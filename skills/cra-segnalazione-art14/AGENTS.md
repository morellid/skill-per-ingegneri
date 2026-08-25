# AGENTS.md - cra-segnalazione-art14

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Obblighi di **segnalazione di vulnerabilita' attivamente sfruttate e incidenti gravi** posti al fabbricante di prodotti con elementi digitali (PDE) dall'**art. 14 del Regolamento (UE) 2024/2847 - Cyber Resilience Act**, applicabili **dall'11 settembre 2026** (art. 71, par. 2). Target: security engineer, PSIRT, ingegnere di prodotto o firmware, compliance manager del fabbricante. La skill inquadra l'adempimento (qualificazione, termini, contenuti, destinatario, prerequisiti); non trasmette notifiche e non classifica il prodotto - per la classificazione vedi `cra-classificazione-pde`.

## Fonti autoritative

Tre fonti, tutte trascritte in `skills/cra-segnalazione-art14/references/fonti/` e
registrate in `skills/cra-segnalazione-art14/references/sources.yaml` (i path che
seguono sono relativi a quella directory `references/`):

- **Reg. (UE) 2024/2847 (CRA)** - CELEX 32024R2847, via CELLAR con negoziazione `Accept: application/xhtml+xml` + `Accept-Language: ita`, sha256 `c545dfacd04be16112595c2de51b35c6d6d0329b565b393de581c77b63659f5b` -> `reg-ue-2024-2847-cra-segnalazione.md`.
- **Dir. (UE) 2022/2555 (NIS2)** - CELEX 32022L2555, stessa via, sha256 `8cd3ee965243a2b4eaef6d3902ca6d12840950d5e8d144d3f98d156088cf55b1` -> `dir-ue-2022-2555-nis2-segnalazione.md`. Serve perche' l'art. 3, punti 43 e 45, del CRA definisce "incidente" e "quasi incidente" **solo per rinvio**.
- **D.Lgs. 4 settembre 2024, n. 138** - GU Serie generale n. 230 dell'1/10/2024, sha256 `056dfbb1ddd34c163585250ae5631270ed8d27ce16ac5b30576cff4e88169e36` -> `dlgs-138-2024-csirt-italia.md`. Serve solo per una cosa: **il CRA non nomina il CSIRT di alcuno Stato membro**.

Estratti operativi in `references/estratti/`:
- `cra-art14-obblighi-e-termini.md` - presupposti, catene di scadenze, contenuti minimi, canale, sanzioni, cosa la fonte non dice.
- `csirt-coordinatore-e-canale-italiano.md` - catena di rinvii CRA -> NIS2 -> D.Lgs. 138/2024 e limiti da non superare.

## Articoli e punti chiave

- **Art. 3, punto 42** (CRA): "vulnerabilita' attivamente sfruttata" - due elementi cumulativi, prove attendibili di sfruttamento **in un sistema** e assenza di autorizzazione del proprietario.
- **Art. 3, punti 43 e 45**: "incidente" e "quasi incidente", per rinvio all'art. 6, punti 6 e 5, NIS2.
- **Art. 3, punto 19**: micro, piccole e medie imprese per rinvio alla raccomandazione 2003/361/CE (**non letta**).
- **Art. 14, par. 1-2**: obbligo su vulnerabilita' attivamente sfruttata - 24h / 72h / relazione finale entro 14 giorni **dalla messa a disposizione del rimedio**.
- **Art. 14, par. 3-4**: obbligo su incidente grave con impatto sulla sicurezza del PDE - 24h / 72h / relazione finale entro **un mese dalla trasmissione** della notifica delle 72 ore.
- **Art. 14, par. 5**: quando un incidente e' grave - lett. a) o lett. b), entrambe estese al potenziale ("e' in grado di").
- **Art. 14, par. 6**: relazione intermedia su richiesta del CSIRT, senza termine.
- **Art. 14, par. 7**: stabilimento principale (decisioni di cibersicurezza; sussidiario: maggior numero di dipendenti) e cascata a)-d) per il fabbricante non stabilito nell'Unione.
- **Art. 14, par. 8**: obbligo autonomo di informare gli utilizzatori.
- **Art. 14, par. 9 e 10**: atto delegato e atto di esecuzione della Commissione - **nessuno dei due e' stato letto**.
- **Art. 15**: segnalazione volontaria; par. 4 - il CSIRT informa il fabbricante della segnalazione di un terzo.
- **Art. 16, par. 1-2 e 6**: piattaforma unica, terminali nazionali, ritardo nella diffusione (decisione del CSIRT).
- **Art. 17, par. 4 e 6**: la sola notifica non aumenta la responsabilita'; assistenza tecnica dei CSIRT alle PMI.
- **Art. 13, par. 6, 7, 8, 17** e **allegato I, parte II, punti 1, 5, 6**: prerequisiti organizzativi (segnalazione al manutentore del componente, documentazione, politica CVD, punto di contatto unico, SBOM, indirizzo di contatto).
- **Art. 64, par. 1, 2, 5, 10**: massimali sanzionatori (15 000 000 EUR o 2,5% del fatturato mondiale, se superiore) e deroga per micro e piccole imprese.
- **Art. 71, par. 2**: 11 dicembre 2027 in generale; **solo** art. 14 dall'11 settembre 2026 e capo IV dall'11 giugno 2026.
- **NIS2 art. 12, par. 1**: designazione del CSIRT coordinatore.
- **D.Lgs. 138/2024, art. 16, c. 1** e **art. 2, c. 1, lett. i)**: CSIRT Italia coordinatore, operante presso ACN.

## Convenzioni specifiche

### Cosa NON fare

- Non scrivere "30 giorni" per la relazione finale sull'incidente: il testo dice **un mese**, e decorre dalla **trasmissione** della notifica delle 72 ore, non dalla sua scadenza.
- Non agganciare la relazione finale sulla vulnerabilita' alla conoscenza o alle 72 ore: decorre dalla **messa a disposizione del rimedio**. Se il rimedio non c'e', il termine non e' iniziato.
- Non trattare CVSS elevato, PoC pubblico o presenza in un catalogo come sinonimi di "attivamente sfruttata". E, all'opposto, non concludere che il presupposto manchi solo perche' non ci sono evidenze sui dispositivi **del fabbricante**: la definizione richiede lo sfruttamento "in un sistema".
- Non risolvere un dubbio di qualificazione a favore del non obbligo. Esporre l'elemento mancante e rinviare al fabbricante.
- Non escludere un incidente perche' ha colpito l'infrastruttura aziendale: il criterio del par. 3 e' l'**impatto sulla sicurezza del prodotto** (build chain, firma degli aggiornamenti, distribuzione).
- Non nominare il CSIRT coordinatore di uno Stato membro diverso dall'Italia: le designazioni nazionali non sono fra le fonti lette.
- Non indicare URL, portali, moduli o procedure di accreditamento alla piattaforma dell'art. 16: le fonti non li contengono.
- Non affermare che una notifica NIS2 assolva l'obbligo del CRA, o viceversa.
- Non affermare che micro e piccole imprese siano al riparo dalle sanzioni: la deroga dell'art. 64, par. 10, riguarda il solo termine delle 24 ore e deroga "ai paragrafi da 3 a 9", mentre l'art. 14 e' sanzionato dal par. 2. Riportare la formulazione letterale e rinviare al consulente.
- Non usare la decorrenza dell'art. 64 (11 dicembre 2027) per suggerire che l'inadempimento sia senza conseguenze o che si possa rinviare.
- Non citare atti delegati o di esecuzione ex art. 14, par. 9 e 10, ne' la politica nazionale CVD ex art. 16, c. 4, D.Lgs. 138/2024: non sono stati letti.
- Non assumere il momento in cui il fabbricante e' "venuto a conoscenza": chiederlo sempre.

### Cosa fare

- Citare sempre articolo **e paragrafo** (e lettera, dove esiste): "art. 14, par. 2, lett. c)", non "il CRA".
- Distinguere in ogni output tre livelli: cio' che il testo **impone**, cio' che e' **condizionato** ("se del caso", "se disponibili"), cio' su cui il testo **tace**.
- Trattare i due fatti generatori come **catene parallele** quando ricorrono entrambi, con relazioni finali distinte.
- Riportare sempre, accanto alla data calcolata, la formula del testo ("senza indebito ritardo e in ogni caso entro 24 ore"): le 24 e le 72 ore sono limiti, non obiettivi.
- Chiudere ogni output con il rinvio al responsabile della conformita' del fabbricante e, per i punti di coordinamento aperti (sezioni H e I dell'estratto), al consulente legale.
- Ricordare l'obbligo autonomo del par. 8 verso gli utilizzatori: non e' subordinato alla notifica al CSIRT.

## Validatori

- Validatore di dominio (product security / compliance engineer con esperienza CRA e PSIRT) - da identificare per la validazione di Livello 2.

## Stato attuale

- Versione: vedi `CHANGELOG.md` (`0.1.0-alpha`).
- Validazione: Livello 1 (autore + adversarial review).
- Task files: 4 (`qualifica-evento-segnalabile`, `costruisci-sequenza-notifiche`, `individua-csirt-coordinatore`, `check-prerequisiti-interni`).
- Esempi: 1 conforme + 1 problematico.
