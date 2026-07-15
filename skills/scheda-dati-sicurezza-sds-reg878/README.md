# scheda-dati-sicurezza-sds-reg878

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con esperto REACH/CLP da completare)

Skill di **supporto documentale alla compilazione e alla verifica di completezza
della Scheda di Dati di Sicurezza (SDS)** secondo l'**allegato II del REACH** quale
sostituito dal **Reg. (UE) 2020/878** (formato a 16 sezioni).

**Non e' una skill di classificazione**: struttura e verifica le 16 sezioni; non
classifica ai sensi del CLP, non compie la valutazione della sicurezza chimica e
non ricava i valori (esposizione, tossicologia, trasporto).

## Target

Ingegneri chimici/di processo, RSPP, uffici regolatori dei fornitori di
sostanze/miscele.

## Cosa fa

| Sotto-attivita' | Descrizione |
|---|---|
| `compila-sds` | Struttura le 16 sezioni e le sotto-sezioni della SDS secondo l'allegato II, con le prescrizioni generali della Parte A |
| `verifica-completezza-sds` | Verifica completezza e conformita' formale di una SDS esistente (sezioni/sotto-sezioni, datazione/revisione, assenza di indicazioni minimizzanti) |

Nucleo: le **16 sezioni obbligatorie** (identificazione, pericoli, composizione,
primo soccorso, antincendio, rilascio accidentale, manipolazione/immagazzinamento,
controlli esposizione/DPI, proprieta' fisiche e chimiche, stabilita'/reattivita',
tossicologiche, ecologiche, smaltimento, trasporto, regolamentazione, altre
informazioni) e le **prescrizioni generali** della Parte A.

## Fonti consultate

- **Reg. (UE) 2020/878** (sostituisce l'allegato II REACH) - Parte A (prescrizioni
  generali) e Parte B (16 sezioni), testo su eur-lex (online-only)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- Non **classifica** ai sensi del **CLP** (Reg. 1272/2008) ne' esegue la
  valutazione della sicurezza chimica
- Non stabilisce **quando** la SDS e' obbligatoria (art. 31 REACH, rinvio)
- Non ricava i **valori** delle singole sezioni

**La skill e' un supporto documentale: non sostituisce la persona competente, il
classificatore CLP ne' la valutazione della sicurezza chimica.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
