# relazione-peritale-ctu-cpc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con CTU/avvocato esperto di processo civile da completare)

Skill di **supporto alla strutturazione della relazione peritale** e allo
**svolgimento delle operazioni** del **consulente tecnico d'ufficio (CTU)** nel
**processo civile**, ai sensi degli **artt. 191-201 del codice di procedura civile**,
con inquadramento del CTU **nell'albo** (D.M. 109/2023).

**Non e' una skill di merito tecnico**: struttura la relazione, i quesiti, il verbale
e i termini processuali; **non fornisce i contenuti tecnici** della perizia (rilievi,
calcoli, conclusioni) e non sostituisce le direttive del giudice.

## Target

Ingegneri nominati **CTU** in cause civili (o iscritti/aspiranti all'albo CTU).

## Cosa fa

| Sotto-attivita' | Descrizione |
|---|---|
| `struttura-relazione` | Dall'ordinanza e dai quesiti, imposta l'indice della relazione e la scansione dei termini dell'art. 195 (bozza alle parti, osservazioni, deposito con sintetica valutazione) |
| `verbale-operazioni-peritali` | Struttura il processo verbale delle operazioni (presenza parti/CTP, istanze e osservazioni, documenti) nel rispetto degli artt. 194-195 |

Nucleo: **nomina e quesiti** (art. 191), **giuramento** anche a firma digitale (art.
193), **operazioni** con intervento di parti e CTP (art. 194), **verbale e relazione**
con la scansione bozza -> osservazioni -> deposito + sintetica valutazione (art. 195),
**conciliazione** e vicende (artt. 196-201), **albo/categorie/settori** (D.M. 109/2023).

## Fonti consultate

- **Codice di procedura civile** (R.D. 1443/1940), artt. **191-201** - testo vigente
  su Normattiva (pagina indice pinnata a `!vig=`)
- **D.M. Giustizia 4/8/2023 n. 109** (albo CTU) - Gazzetta Ufficiale (riferimento
  solo-online), artt. 1-12 + settori categoria INGEGNERIA (Allegato A)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non fornisce il merito tecnico** (rilievi, calcoli, conclusioni): dipende dallo
  specifico quesito e dalla disciplina tecnica.
- Non copre la **perizia penale** (c.p.p.) ne' la **liquidazione del compenso** (vedi
  `compensi-ctu-dpr115`).
- L'**Allegato A** del D.M. 109/2023 e' trascritto verbatim solo per la categoria
  INGEGNERIA (tabella con celle multi-riga): per le altre categorie si rinvia all'atto.

**La skill e' un supporto procedurale/documentale: non sostituisce il giudice, il
difensore ne' il giudizio tecnico del consulente.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
