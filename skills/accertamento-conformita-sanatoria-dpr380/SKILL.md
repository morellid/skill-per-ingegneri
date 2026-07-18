---
name: accertamento-conformita-sanatoria-dpr380
description: "Supporto documentale al progettista (geometra, architetto, ingegnere) e al tecnico incaricato per l'accertamento di conformita' (permesso di costruire o SCIA in sanatoria) degli interventi edilizi abusivi, ai sensi del D.P.R. 6 giugno 2001, n. 380 (Testo unico edilizia), Titolo IV, artt. 36, 36-bis e 37, come modificati dal decreto-legge 69/2024 (salva-casa) convertito dalla legge 105/2024. Aiuta a stabilire quale articolo si applica in base alla qualificazione dell'abuso: assenza di titolo o totale difformita' con doppia conformita' piena, cioe' conformita' urbanistica ed edilizia sia al momento della realizzazione sia al momento della domanda, oblazione pari al contributo di costruzione in misura doppia e decisione in sessanta giorni con silenzio-rifiuto (art. 36); parziale difformita' e variazioni essenziali con la doppia conformita' attenuata introdotta dal salva-casa, cioe' conformita' urbanistica al momento della domanda e requisiti edilizi al momento della realizzazione, la dichiarazione del professionista abilitato che attesta le conformita' e prova l'epoca di realizzazione, gli interventi anche strutturali prescrivibili dallo sportello unico, i profili sismici e paesaggistici, l'oblazione con l'incremento del venti per cento o il doppio del valore venale e la decisione in quarantacinque giorni con silenzio-assenso (art. 36-bis); gli interventi in assenza o difformita' dalla segnalazione certificata di inizio attivita' con la sanzione pecuniaria pari al triplo dell'aumento del valore venale, minimo 1.032 euro, e il rinvio all'accertamento dell'art. 36-bis (art. 37). Use when a surveyor, architect, or engineer must frame the building compliance assessment (permit or SCIA in condono/sanatoria) for unlawful works under D.P.R. 380/2001 as amended by the 2024 salva-casa reform; it is a documentary aid and does NOT draft the application or the compliance statement, does NOT classify the abuse or compute the oblation or venal value, does NOT cover the condono under special laws, and does NOT replace the designer, the one-stop building desk, or the competent authorities."
license: MIT
area: edilizia-urbanistica-catasto
title: "Accertamento di conformita' / sanatoria edilizia - salva-casa (DPR 380/2001)"
summary: "Inquadra l'accertamento di conformita' (sanatoria edilizia) del DPR 380/2001 dopo il salva-casa: doppia conformita' piena per assenza titolo/totale difformita' (36), attenuata per parziale difformita'/variazioni essenziali con silenzio-assenso 45 gg (36-bis), sanzione SCIA (37)."
normative_refs:
  - "D.P.R. 6 giugno 2001, n. 380 (Testo unico edilizia) - artt. 36 (assenza titolo/totale difformita'), 36-bis (parziale difformita'/variazioni essenziali - salva-casa) e 37 (assenza/difformita' SCIA)"
  - "Rinvio: D.L. 69/2024 conv. L. 105/2024 (salva-casa, introduce l'art. 36-bis); artt. 31-34, 34-bis, 9-bis, 44 DPR 380; art. 167 D.Lgs. 42/2004; leggi condono (non trattate)"
version: 0.1.0-alpha
status: alpha
tags:
  - accertamento-conformita
  - sanatoria-edilizia
  - salva-casa
  - dpr-380-2001
  - doppia-conformita
---

# Accertamento di conformità / sanatoria edilizia - salva-casa (DPR 380/2001 artt. 36, 36-bis, 37)

## Quando usare questa skill

Usala quando un **progettista** (geometra/architetto/ingegnere) o un **tecnico incaricato** deve
**inquadrare** l'**accertamento di conformità** (permesso di costruire o SCIA **in sanatoria**) di un
intervento edilizio abusivo, secondo il **D.P.R. 6 giugno 2001, n. 380** (Testo unico edilizia),
**Titolo IV, artt. 36, 36-bis e 37**, come modificati dal **DL 69/2024 ("salva-casa"), conv. L.
105/2024**:

- capire **quale articolo** si applica in base al tipo di abuso;
- **art. 36** (assenza di titolo / totale difformità): doppia conformità piena;
- **art. 36-bis** (parziale difformità / variazioni essenziali): doppia conformità attenuata;
- **art. 37** (assenza/difformità dalla SCIA): sanzione e rinvio all'art. 36-bis.

**Non è** uno strumento che redige la domanda o la dichiarazione di conformità, né qualifica l'abuso o
calcola l'oblazione: è un **supporto documentale** che inquadra presupposti, termini ed effetti.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-articolo-doppia-conformita` | Stabilisce quale articolo si applica (36/36-bis/37) e quale doppia conformità è richiesta in base alla qualificazione dell'abuso |
| `inquadra-procedura-oblazione-termini` | Inquadra dichiarazione del professionista, oblazione, profili sismici/paesaggistici, termini ed esito (art. 36-bis; art. 37) |

## Punti chiave (verificati sul testo)

- **Art. 36** (assenza titolo/totale difformità): **doppia conformità piena** (realizzazione **e**
  domanda) (c. 1); oblazione = **contributo doppio** (c. 2); **60 giorni**, **silenzio-rifiuto** (c. 3).
- **Art. 36-bis** (parziale difformità/variazioni essenziali, **salva-casa**): **doppia conformità
  attenuata** (urbanistica alla **domanda** + requisiti edilizi alla **realizzazione**) (c. 1);
  **dichiarazione del professionista abilitato** e prova dell'**epoca** (art. 9-bis c. 1-bis) (c. 3);
  **sismica** (c. 3-bis) e **paesaggistica** (cc. 4, 5-bis); **oblazione** (c. 5: doppio contributo
  **+20%** o doppio valore venale, **1.032-10.328** / **516-5.164 euro**); **45 giorni**,
  **silenzio-assenso** (c. 6).
- **Art. 37** (assenza/difformità SCIA): sanzione **triplo** dell'aumento del valore venale, **min 1.032
  euro** (c. 1); vincolati (cc. 2-3); rinvio all'accertamento **art. 36-bis** (c. 6).

## Fonti

- **D.P.R. 6 giugno 2001, n. 380** (Testo unico edilizia) - **artt. 36, 36-bis, 37** - testo vigente su
  Normattiva (indice pinnato a `!vig=2026-07-17`, codice 001G0429, idGruppo 9).

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non redige** la domanda di sanatoria né la **dichiarazione di conformità** del professionista.
- **Non qualifica** l'abuso (assenza/totale/parziale/variazione essenziale) al posto del tecnico; **non
  calcola** l'oblazione né il **valore venale**.
- **Non tratta** il **condono** (leggi speciali: L. 47/1985 capo IV, L. 724/1994, L. 326/2003) né lo
  **stato legittimo** (art. 9-bis) se non nei richiami.

**La skill è un supporto documentale: non sostituisce il progettista, lo sportello unico per l'edilizia
o gli enti competenti, né la lettura degli artt. 36-37 del D.P.R. 380/2001 e delle norme del salva-casa.**
