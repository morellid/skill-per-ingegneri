# fascicolo-tecnico-dispositivi-medici-mdr

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con esperto RA dispositivi medici da completare)

Skill di **supporto documentale alla struttura del fascicolo tecnico**
(documentazione tecnica) di un **dispositivo medico di classe I o IIa** e al
**percorso di valutazione della conformita'** ai sensi del **Reg. (UE) 2017/745
(MDR)**.

**Non e' una skill di classificazione ne' di merito clinico**: struttura il
fascicolo e indica il percorso di conformita'; non applica le regole dell'allegato
VIII (la classe e' un input), non redige la valutazione clinica ne' individua le
norme armonizzate.

## Target

Ingegneri biomedici, fabbricanti di dispositivi medici, uffici RA/QA.

## Cosa fa

| Sotto-attivita' | Descrizione |
|---|---|
| `struttura-fascicolo-tecnico` | Compone i sei capitoli della documentazione tecnica (allegato II) e la documentazione PMS (allegato III) |
| `scegli-percorso-conformita` | Data la classe (I, Is/Im/Ir, IIa), individua il percorso di valutazione della conformita' (art. 52) e il ruolo dell'organismo notificato |

Nucleo: i **6 capitoli** dell'allegato II (documentazione tecnica), l'**allegato
III** (sorveglianza post-commercializzazione) e i **percorsi dell'art. 52** per le
classi I (incl. Is/Im/Ir) e IIa.

## Fonti consultate

- **Reg. (UE) 2017/745 (MDR)** - art. 52, allegati II, III, VIII, testo consolidato
  su eur-lex (online-only)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- Non **classifica** il dispositivo (allegato VIII): la classe e' un input
- Non redige **valutazione clinica**, gestione del rischio o prove
- Non individua le **norme armonizzate** (a pagamento) ne' gli MDCG guidance
- Non copre IVDR (Reg. 2017/746), dispositivi su misura, classi IIb/III: rinvio

**La skill e' un supporto documentale: non sostituisce il fabbricante, il
valutatore clinico ne' l'organismo notificato.**

> Nota area di catalogo: classificata in `impianti-macchine-prodotti` (compliance di
> prodotto: il dispositivo e' un prodotto immesso sul mercato con documentazione
> tecnica e marcatura CE), il repo non ha un'area "biomedico" dedicata.

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
