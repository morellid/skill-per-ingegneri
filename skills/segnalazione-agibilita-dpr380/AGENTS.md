# AGENTS.md - segnalazione-agibilita-dpr380

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale alla **segnalazione certificata di agibilità (SCA)**: presupposti, soggetti,
termine, interventi soggetti, sanzione, agibilità parziale, documentazione allegata, deroghe
igienico-sanitarie asseverabili, utilizzo e controlli, secondo l'**art. 24 del D.P.R. 6 giugno
2001, n. 380** (l'**art. 25** è **abrogato** dal D.Lgs. 222/2016). Target: ingegneri, architetti,
direttori dei lavori.

**È una skill documentale**: inquadra il metodo; **non redige/presenta** la SCA, **non compila** la
modulistica regionale/comunale, **non esegue** collaudi o certificazioni, non sostituisce il DL né
il professionista abilitato.

## Nota sull'area e sulla complementarità

Area **edilizia-urbanistica-catasto**. Complementare e distinta da `modulistica-edilizia-unificata`
(regime edilizio: CILA/SCIA/permesso), `catasto-pregeo-docfa-atti-telematici` (aggiornamento
catastale) e `denuncia-opere-strutturali-l1086` (denuncia opere / collaudo statico): questa copre
l'**agibilità** (art. 24).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dpr-380-2001-art-24-25**: D.P.R. 6 giugno 2001, n. 380, pagina indice Normattiva pinnata a
  `!vig=2026-07-16` (hash `98a209db...`; codice 001G0429). Art. 24 (versione 7, idGruppo 7) e art.
  25 (abrogato) caricati via `caricaArticolo` e trascritti verbatim.

Trascrizione in `references/fonti/dpr-380-2001-art-24-25.md`; estratto operativo in
`references/estratti/agibilita-checklist.md`.

## Punti chiave (verificati sul testo)

- **Strumento** (c. 1): l'agibilità è attestata mediante **segnalazione certificata** (non più
  certificato: art. 25 abrogato).
- **Soggetto/termine** (c. 2): titolare del permesso/SCIA o aventi causa, **entro 15 giorni**
  dall'ultimazione dei lavori di finitura, al **SUE**; interventi a/b/c. **Sanzione 77-464 euro**
  (c. 3).
- **Agibilità parziale** (c. 4); **documentazione** (c. 5: attestazione DL, collaudo statico art.
  67, barriere artt. 77/82, aggiornamento catastale, impianti, banda ultra larga).
- **Deroghe igienico-sanitarie** (c. 5-bis/ter): altezza fino a **2,40 m**; monostanza **20/28 mq**;
  adattabilità **DM 236/1989**.
- **Utilizzo dalla presentazione** (c. 6, art. 19 c. 3/6-bis L. 241/1990); **controlli** anche a
  campione (c. 7); **SCA senza lavori** (c. 7-bis).

## Convenzioni specifiche

### Cosa NON fare
- Non **redigere/presentare** la SCA né **compilare** la modulistica regionale/comunale.
- Non **eseguire** collaudo statico (art. 67) o certificazioni impianti/accessibilità.
- Non inventare **soglie** (usare 15 giorni, 77-464 euro, 2,40 m, 20/28 mq come da testo).

### Cosa fare
- **Comporre** l'elenco della documentazione (c. 5), **verificare** i presupposti dell'agibilità
  parziale (c. 4) e delle deroghe (c. 5-bis/ter), con rinvio agli atti e alle skill correlate.

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.P.R. 380/2001 pinnato a nuovo `!vig=` (nuovo hash) e
rileggere l'art. 24, verificando le modifiche (testo tra `(( ))`, es. D.L. 76/2020 conv. L.
120/2020).

## Validatori

- Non ancora assegnato (Livello 2 con tecnico abilitato / SUE).

## Stato attuale

- Versione: 0.1.0-alpha
- Task files: 2 (`prepara-sca.md`, `verifica-agibilita-parziale.md`)
- Esempi: 2 (agibilità nuova costruzione; agibilità parziale di singola unità)
