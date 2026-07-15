# marcatura-ce-elettrici-lvd-emc-red

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con esperto marcatura CE elettrica da completare)

Skill di **supporto documentale alla marcatura CE dei prodotti elettrici/
elettronici** secondo le tre direttive di prodotto: **LVD 2014/35/UE** (bassa
tensione), **EMC 2014/30/UE** (compatibilita' elettromagnetica) e **RED 2014/53/UE**
(apparecchiature radio).

**Non e' una skill di prova/progetto**: individua direttive, procedura di
conformita' e documentazione; non individua le norme armonizzate (a pagamento),
non esegue le prove ne' redige la dichiarazione finale.

## Target

Fabbricanti, uffici tecnici, ingegneri elettrici/elettronici.

## Cosa fa

| Sotto-attivita' | Descrizione |
|---|---|
| `individua-direttive` | Dato il prodotto, determina quale/i direttiva/e si applica/applicano (LVD, EMC, RED) e come si combinano (la RED incorpora sicurezza LVD ed EMC) |
| `scegli-procedura-conformita` | Per ciascuna direttiva, individua procedura/moduli, quando serve l'organismo notificato, e struttura documentazione, dichiarazione UE e marcatura CE |

Nucleo: **ambito** delle tre direttive, **procedure di conformita'** e **moduli**
(A; esame UE del tipo B+C; garanzia di qualita' totale H), **quando serve un
organismo notificato**, **documentazione tecnica**, **dichiarazione UE di
conformita'** (anche semplificata RED) e **marcatura CE**.

## Fonti consultate

- **Direttiva 2014/35/UE (LVD)**, **2014/30/UE (EMC)**, **2014/53/UE (RED)** - testo
  su eur-lex (online-only). Recepite in Italia da D.Lgs. 86/2016, 80/2016, 128/2016.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- Non individua le **norme armonizzate** (EN a pagamento) ne' esegue le **prove**
- Non redige materialmente documentazione/dichiarazione: ne fornisce struttura
- Non copre altre direttive (macchine 2023/1230, ATEX 2014/34, ErP, RoHS): rinvio

**La skill e' un supporto documentale: non sostituisce il fabbricante, il
laboratorio di prova ne' l'organismo notificato.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
