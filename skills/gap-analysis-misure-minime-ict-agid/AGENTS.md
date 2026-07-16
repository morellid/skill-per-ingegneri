# AGENTS.md - gap-analysis-misure-minime-ict-agid

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto alla **gap analysis** delle **Misure Minime di Sicurezza ICT per le PA**
(MMS-PA), basate sugli **AgID Basic Security Control(s) (ABSC)** della **Circolare AgID
18/4/2017 n. 2/2017** (attuazione art. 14-bis C.A.D. e direttiva PCM 1/8/2015). Target:
PA e loro fornitori/consulenti.

**E' una skill documentale/di gap analysis**: imposta la valutazione controllo per
controllo e la compilazione del modulo; **non esegue l'assessment tecnico** e **non
riproduce la matrice grafica** dei singoli controlli.

## Area di catalogo

`software-dati-cybersecurity`, coerente con `nis2-self-assessment` (NIS2). Le MMS-PA/ABSC
sono la **base storica** per la PA; NIS2 (D.Lgs 138/2024) si **aggiunge** per alcuni
soggetti: le due skill sono complementari, non sovrapposte.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **circolare-agid-2-2017**: Circolare AgID 2/2017, **PDF ufficiale della G.U. n.
  103/2017** (codice 17A03060), scaricabile da gazzettaufficiale.it e **hashato**
  (SHA256 24e4956e...; host in allowlist). Trascritti verbatim in
  `references/fonti/circolare-agid-2-2017.md` gli articoli (Premessa/art. 1 Scopo, artt.
  2-5), la sezione Generalita', la struttura degli ABSC e i tre livelli, e i titoli +
  descrizioni delle 8 famiglie ABSC.

Estratto operativo: `references/estratti/absc-gap-analysis-checklist.md`.

## Punti chiave (verificati sul testo)

- **Ambito** (art. 2): soggetti dell'art. 2 c.2 del C.A.D.
- **Responsabile** dell'attuazione (art. 3): responsabile struttura organizzazione/
  innovazione/tecnologie (art. 17 C.A.D.) o dirigente designato.
- **Modulo di implementazione** (art. 4, Allegato 2): firma digitale + marcatura
  temporale, conservazione, trasmissione al CERT-PA in caso di incidente.
- **Tempi** (art. 5): la circolare fissava l'attuazione entro il 31/12/2017.
- **8 famiglie ABSC**: 1 (inventario dispositivi), 2 (inventario software), 3
  (configurazioni), 4 (vulnerabilita'), 5 (privilegi admin), 8 (malware), 10 (backup), 13
  (protezione dati).
- **Tre livelli**: Minimo (obbligatorio, soglia), Standard (base), Alto (obiettivo).
- **ABSC_ID** gerarchico `x.y.z`; colonna **FNSC** raccorda al Framework Nazionale Cyber
  Security.

## LIMITE DI RESA (importante)

La **matrice completa** dei controlli (`ABSC_ID x.y.z` con le colonne booleane
Minimo/Standard/Alto) e' una **tabella in formato grafico** nel PDF (Allegato 1). La resa
testuale dal PDF **non conserva in modo affidabile** l'allineamento delle X: **il livello
esatto di ogni controllo va letto sulle colonne del PDF**. Sono trascritti verbatim i
titoli e le descrizioni delle 8 famiglie e la spiegazione dei livelli; NON si desumono i
flag dei singoli controlli.

## Convenzioni specifiche

### Cosa NON fare
- Non **inventare** il flag Minimo/Standard/Alto di un controllo: leggerlo sul PDF.
- Non **eseguire l'assessment tecnico** (scansioni, inventari, test).
- Non spacciare le MMS-PA per l'intero quadro: per alcuni soggetti si aggiunge **NIS2**
  (skill `nis2-self-assessment`).

### Cosa fare
- Impostare la gap analysis per gruppo ABSC (livello, stato, evidenze, azioni).
- Strutturare il modulo di implementazione (firme, conservazione, CERT-PA).

## Aggiornamento delle fonti

GU: il PDF della G.U. n. 103/2017 e' stabile (hash 24e4956e...). Verificare eventuali
aggiornamenti/superamenti della circolare (es. evoluzione del quadro con NIS2 e misure
ACN) prima di modifiche sostanziali.

## Validatori

- Non ancora assegnato (Livello 2 con esperto sicurezza ICT PA).

## Stato attuale

- Versione: 0.1.0-alpha (closes #53)
- Task files: 2 (`imposta-gap-analysis.md`, `compila-modulo-implementazione.md`)
- Esempi: 2 (piccolo Comune - livello minimo; gruppo ABSC 5 privilegi di amministratore)
