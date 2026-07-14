# via-screening-sia-dlgs152

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con esperto VIA da completare)

Skill di **supporto documentale alla Valutazione di Impatto Ambientale (VIA)**
ai sensi della Parte Seconda del D.Lgs. 152/2006 (testo vigente) e del DM
30/03/2015. Copre la **verifica di assoggettabilita'** (screening) e la
**struttura dello Studio di Impatto Ambientale (SIA)**.

**Non e' una skill decisionale**: non decide l'assoggettabilita', non stabilisce
le soglie dei progetti, non redige gli studi.

## Target

Ingegneri e consulenti ambientali, proponenti e tecnici che predispongono la
documentazione VIA.

## Cosa fa

| Sotto-attivita' | Descrizione |
|---|---|
| `screening-verifica-assoggettabilita` | Procedura e termini perentori della verifica di assoggettabilita' (art. 19: 5/15 gg completezza, 30 gg osservazioni, 60/45 gg provvedimento, +20 gg proroga), checklist dello Studio Preliminare Ambientale (All. IV-bis) e copertura dei criteri (All. V); meccanismi di adeguamento regionale delle soglie (DM 30/03/2015: riduzione, +30%, esclusione) |
| `checklist-sia` | Checklist di completezza dei 12 punti dell'Allegato VII (contenuti del SIA di cui all'art. 22), o bozza di indice del SIA |

## Fonti consultate

- **D.Lgs. 3/4/2006 n. 152**, Parte Seconda - artt. 19, 22 + Allegati IV-bis, V,
  VII (testo vigente su Normattiva, pagina indice pinnata `!vig=2026-07-14`;
  art. 19 in vigore dal 17-12-2024)
- **DM 30/03/2015** (GU n. 84/2015) - linee guida per la verifica di
  assoggettabilita' a VIA dei progetti di competenza regionale

Dettaglio (URL, SHA256, trascrizioni) in `references/sources.yaml`,
`references/fonti/`, `references/estratti/`.

## Limiti noti

- Non contiene gli elenchi dei progetti (allegati II-bis e IV) con le soglie
  dimensionali: per stabilire se un progetto rientri nello screening, consultare
  gli allegati alla Parte Seconda e il DM 30/03/2015 + norme regionali
- Non copre la procedura di VIA vera e propria (artt. 23-27), il PAUR (art.
  27-bis), la VAS (artt. 11-18), la VIA statale (Commissione art. 8)
- Non decide l'assoggettabilita' ne' redige gli studi

**La skill e' un supporto documentale: la decisione compete all'autorita'
competente e la redazione degli studi ai tecnici firmatari.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
