# sorveglianza-sanitaria-medico-competente-dlgs81

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con medico competente / RSPP da completare)

Skill di **supporto documentale** alla **sorveglianza sanitaria** dei lavoratori e agli **obblighi
del medico competente**, secondo il **D.Lgs. 81/2008** (T.U. salute e sicurezza sul lavoro), artt.
25 e 38-41.

**Non esprime giudizi sanitari** (esclusivi del medico competente), **non riproduce** gli Allegati
3A/3B e **non sostituisce** il medico competente, l'RSPP o il datore: inquadra quadro e adempimenti.

## Target

Datori di lavoro, RSPP e consulenti della sicurezza.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `imposta-sorveglianza-sanitaria` | Stabilisce quando la sorveglianza è dovuta e i tipi di visita applicabili (art. 41) |
| `gestisci-giudizio-idoneita-ricorso` | Inquadra i quattro giudizi di idoneità, la forma scritta e il ricorso all'ASL (30 giorni) |

Nucleo: casi della sorveglianza (art. 41 c.1), tipi di visita (c.2), divieti e spese (cc.3-4),
quattro giudizi di idoneità (c.6), ricorso all'ASL entro 30 giorni (c.9), obblighi e requisiti del
medico competente (artt. 25, 38-40).

## Fonti consultate

- **D.Lgs. 9 aprile 2008, n. 81** (T.U. sicurezza) - artt. 25, 38, 39, 40, 41 - testo vigente su
  Normattiva (indice pinnato a `!vig=2026-07-16`, codice 008G0104)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non esprime giudizi sanitari** né definisce i **protocolli sanitari** (esami, periodicità
  puntuale): sono del medico competente.
- **Non riproduce** gli **Allegati 3A/3B** (cartella sanitaria e di rischio).
- **Non sostituisce** il medico competente, l'RSPP né il datore di lavoro.
- È complementare a `dvr-generico` (la valutazione dei rischi attiva la sorveglianza).

**La skill è un supporto documentale: non sostituisce il medico competente, l'RSPP né la lettura
del D.Lgs. 81/2008 e dei suoi Allegati.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
