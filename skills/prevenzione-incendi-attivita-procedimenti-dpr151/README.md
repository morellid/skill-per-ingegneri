# prevenzione-incendi-attivita-procedimenti-dpr151

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con professionista antincendio / funzionario VV.F. da completare)

Skill di **supporto documentale** per stabilire se un'attività è **soggetta ai controlli di
prevenzione incendi** e in quale **categoria (A, B, C)** dell'**Allegato I**, e per impostare
i **procedimenti** presso il **Comando dei Vigili del fuoco**, secondo il **D.P.R. 1 agosto
2011, n. 151**.

**Non riproduce la classificazione puntuale** di ogni attività, **non redige** il progetto
antincendio, la SCIA o le asseverazioni, e **non riproduce le regole tecniche** (DM 3/8/2015):
inquadra ambito, categorie e procedimenti.

## Target

Ingegneri, professionisti antincendio e tecnici del **SUAP/VV.F.** che devono verificare
l'assoggettabilità e impostare l'iter di prevenzione incendi.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `classifica-attivita-categoria` | Verifica se l'attività è nell'Allegato I e in quale categoria A/B/C, e i procedimenti conseguenti |
| `imposta-procedimento-vvf` | Imposta il procedimento VV.F.: valutazione progetto (B/C), SCIA e controlli, CPI (C), rinnovo periodico e deroghe |

Nucleo: attività soggette e **categorie A/B/C** (art. 2 + Allegato I), **valutazione del
progetto** (art. 3, B/C, 60 gg), **SCIA** e **controlli** con visite tecniche entro 60 gg
(art. 4), **certificato di prevenzione incendi** (CPI, categoria C, 15 gg), **rinnovo
periodico** (art. 5, 5/10 anni), **obblighi in esercizio** (art. 6), **deroghe** (art. 7).

## Fonti consultate

- **D.P.R. 1 agosto 2011, n. 151** - artt. 2, 3, 4, 5, 6, 7 e Allegato I - testo vigente su
  Normattiva (indice pinnato a `!vig=2026-07-16`, codice 011G0193)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non riproduce la classificazione puntuale** (categoria A/B/C) di ogni attività: va letta
  sull'Allegato I dell'atto (tabella grafica).
- **Non redige** il progetto antincendio, la SCIA né le asseverazioni.
- **Non riproduce le regole tecniche** (DM 3/8/2015 - Codice di prevenzione incendi, RTV).
- È complementare a `piano-emergenza-antincendio-dm2021` (gestione dell'emergenza) e ad
  `atex-luoghi-lavoro-dlgs81`: questa copre l'assoggettabilità e i procedimenti VV.F.

**La skill è un supporto documentale: non sostituisce il professionista antincendio, il
Comando dei Vigili del fuoco né la lettura dell'Allegato I del D.P.R. 151/2011 e delle regole
tecniche di prevenzione incendi.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
