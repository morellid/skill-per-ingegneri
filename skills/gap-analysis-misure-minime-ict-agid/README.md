# gap-analysis-misure-minime-ict-agid

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con esperto sicurezza ICT PA da completare)

Skill di **supporto alla gap analysis** delle **Misure Minime di Sicurezza ICT per le
pubbliche amministrazioni** (MMS-PA), basate sugli **AgID Basic Security Control(s)
(ABSC)** della **Circolare AgID 18/4/2017 n. 2/2017**.

**Non e' una skill di assessment tecnico**: imposta la valutazione controllo per
controllo sugli 8 gruppi ABSC e la compilazione del modulo di implementazione; **non
esegue** scansioni/inventari e **non riproduce** la matrice grafica dei singoli controlli.

## Target

PA (e loro fornitori/consulenti) che devono valutare la propria conformita' alle misure
minime ICT e compilare il modulo di implementazione AgID.

## Cosa fa

| Sotto-attivita' | Descrizione |
|---|---|
| `imposta-gap-analysis` | Per ciascun gruppo ABSC (1-13) valuta i controlli: livello (Minimo/Standard/Alto), stato di attuazione, evidenze, azioni |
| `compila-modulo-implementazione` | Struttura il modulo (Allegato 2): responsabile (art. 3), firma digitale + marcatura temporale, conservazione, trasmissione al CERT-PA (art. 4) |

Nucleo: **ambito** (art. 2, soggetti art. 2 c.2 C.A.D.), **responsabile** (art. 3),
**modulo** (art. 4), **tempi** (art. 5), **8 gruppi ABSC** (1, 2, 3, 4, 5, 8, 10, 13),
**3 livelli** (Minimo obbligatorio, Standard, Alto), raccordo **FNSC**.

## Fonti consultate

- **Circolare AgID 18/4/2017 n. 2/2017** (Misure minime di sicurezza ICT per le PA) -
  **PDF ufficiale della G.U. n. 103/2017** (hashato), artt. e Allegato 1 (ABSC)
- **D.Lgs. 82/2005 (C.A.D.)** art. 14-bis e art. 2 c.2 + **direttiva PCM 1/8/2015**

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non riproduce la matrice completa** dei controlli con i flag Minimo/Standard/Alto per
  ogni `ABSC_ID`: quella e' una **tabella in formato grafico** nel PDF (pagg. ~68-73), da
  leggere sull'originale.
- **Non esegue l'assessment tecnico** dei sistemi.
- Le MMS-PA sono la **base**: per alcuni soggetti si aggiunge **NIS2** (D.Lgs 138/2024) -
  vedi `nis2-self-assessment`.

**La skill e' un supporto documentale: non sostituisce l'assessment tecnico, il
responsabile dell'attuazione ne' la lettura delle tabelle ABSC nel PDF ufficiale.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
