# regimi-suap-attivita-produttive-dlgs222

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con operatore SUAP / esperto semplificazione da completare)

Skill di **supporto documentale** all'**individuazione del regime amministrativo**
(comunicazione, SCIA, SCIA unica, SCIA condizionata, silenzio-assenso, autorizzazione)
applicabile all'**avvio, modifica, subingresso o cessazione** di un'**attivita' privata
produttiva/commerciale** presso lo **Sportello unico per le attivita' produttive (SUAP)**,
sulla base del **D.Lgs. 222/2016 ("SCIA 2")** e della sua **Tabella A**.

**Non riproduce la Tabella A attivita' per attivita'** e **non sostituisce** la valutazione
del SUAP: inquadra il **metodo di lettura** e gli **effetti/tempi** dei regimi.

## Target

Ingegneri, geometri, consulenti e operatori del **SUAP/SUE** che devono classificare
un'attivita' produttiva/commerciale per determinare il regime amministrativo prima della
presentazione allo Sportello unico.

## Cosa fa

| Sotto-attivita' | Descrizione |
|---|---|
| `individua-regime-attivita` | Individua il regime amministrativo di un'attivita' sulla Tabella A e ne inquadra effetti e tempi |
| `gestisci-scia-unica-condizionata` | Distingue e imposta SCIA, SCIA unica (art. 19-bis c. 2) e SCIA condizionata (art. 19-bis c. 3) con la Conferenza di servizi |

Nucleo: **regime dalla Tabella A** (art. 2, c. 1), **comunicazione** (c. 2), **SCIA** /
avvio immediato e controlli 60/30 gg (art. 19), **SCIA unica** (art. 19-bis c. 2), **SCIA
condizionata** con Conferenza di servizi entro 5 gg (art. 19-bis c. 3), **autorizzazione /
silenzio-assenso** (art. 20), **attivita' non elencate** (art. 2, c. 6), **livelli
ulteriori di semplificazione** (art. 5).

## Fonti consultate

- **D.Lgs. 25 novembre 2016, n. 222 ("SCIA 2")** - artt. 1, 2, 5 e Tabella A - testo
  vigente su Normattiva (indice pinnato a `!vig=2026-07-16`, codice 16G00237)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non riproduce la Tabella A attivita' per attivita'** (~245 KB): il regime esatto va
  letto sulla Tabella A dell'atto.
- **Non sostituisce** la valutazione del SUAP ne' la normativa di settore.
- È complementare a `modulistica-edilizia-unificata` (stessa Tabella A, ma per la **parte
  edilizia** - interventi DPR 380/2001 e modulistica unificata): questa copre le
  **attivita' produttive/commerciali**.

**La skill e' un supporto documentale: non sostituisce lo Sportello unico, la lettura della
Tabella A dell'atto ne' la normativa di settore applicabile all'attivita'.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
