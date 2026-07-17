---
name: contratto-appalto-cc
description: "Supporto documentale all'inquadramento del contratto di appalto nel Codice civile (R.D. 262/1942, Libro IV, Titolo III, Capo VII), artt. 1655-1666 e 1671. Aiuta a inquadrare la nozione di appalto come contratto con cui una parte assume, con organizzazione dei mezzi necessari e gestione a proprio rischio, il compimento di un'opera o di un servizio verso un corrispettivo in danaro (art. 1655); il divieto di subappalto senza autorizzazione del committente (art. 1656); la determinazione del corrispettivo con tariffe/usi o dal giudice (art. 1657); la fornitura della materia di norma a carico dell'appaltatore (art. 1658); le variazioni del progetto - concordate con autorizzazione scritta (art. 1659), necessarie a regola d'arte con la soglia del sesto per il recesso (art. 1660), ordinate dal committente entro il sesto con compenso per i maggiori lavori (art. 1661); la verifica nel corso dell'opera e la risoluzione (art. 1662); la denuncia dei difetti della materia fornita dal committente (art. 1663); l'onerosita' o difficolta' dell'esecuzione, con revisione del prezzo per la parte eccedente il decimo ed equo compenso per difficolta' geologiche/idriche impreviste (art. 1664); la verifica e il pagamento dell'opera con accettazione anche tacita (art. 1665); la verifica e il pagamento per singole partite (art. 1666); il recesso unilaterale del committente con indennizzo di spese, lavori eseguiti e mancato guadagno (art. 1671). Use when an engineer, appaltatore, or committente must frame a private works/services contract (appalto) under the Italian Civil Code; it is a documentary aid and does NOT draft the contract, does NOT quantify amounts, does NOT cover liability for defects/ruin (artt. 1667-1669) nor public procurement (D.Lgs. 36/2023), and does NOT replace a lawyer or CTU."
license: MIT
area: forense
title: "Contratto di appalto nel Codice civile (c.c. artt. 1655-1666, 1671)"
summary: "Inquadra il contratto di appalto nel Codice civile (artt. 1655-1666, 1671): nozione, subappalto, corrispettivo, variazioni (soglia del sesto), onerosita' sopravvenuta (soglia del decimo), verifica e pagamento con accettazione, recesso del committente. Non redige il contratto."
normative_refs:
  - "Codice civile (R.D. 16 marzo 1942, n. 262) - Libro IV, Titolo III, Capo VII (Dell'appalto), artt. 1655-1666 e 1671"
  - "Rinvio (non riprodotti): artt. 1667-1669 c.c. (difformita', vizi, rovina - skill responsabilita-appaltatore-rovina-cc), art. 2222 c.c. (contratto d'opera), D.Lgs. 36/2023 (appalto pubblico)"
version: 0.1.0-alpha
status: alpha
tags:
  - appalto
  - codice-civile
  - contratto-appalto
  - variazioni
  - recesso
---

# Contratto di appalto nel Codice civile (c.c. artt. 1655-1666, 1671)

## Quando usare questa skill

Usala quando un **ingegnere, appaltatore o committente** deve **inquadrare** un **contratto di
appalto** di diritto privato (opere o servizi) secondo il **Codice civile** (R.D. 16 marzo 1942,
n. 262), Libro IV, Titolo III, **Capo VII (Dell'appalto)**, artt. 1655-1666 e 1671:

- **nozione** e distinzione dal contratto d'opera (art. 1655);
- **subappalto**, **corrispettivo**, **materia** (artt. 1656-1658);
- **variazioni** del progetto (artt. 1659-1661);
- **verifica**, **difetti**, **onerosita' sopravvenuta**, **pagamento**, **recesso** (artt.
  1662-1666, 1671).

Per la **responsabilita'** dell'appaltatore per **difformita', vizi e rovina** (artt. 1667-1669)
usa `responsabilita-appaltatore-rovina-cc`; per l'**appalto pubblico** usa le skill D.Lgs.
36/2023 (`subappalto-contratti-pubblici-dlgs36`, `direzione-lavori-esecuzione-dlgs36`,
`modifiche-varianti-contratti-pubblici-dlgs36`, ecc.). Questa copre la **disciplina civilistica**
dell'appalto privato.

## Nozione, subappalto, corrispettivo, materia (artt. 1655-1658)

- **Nozione** (art. 1655): l'appalto e' il contratto con cui una parte assume, con
  **organizzazione dei mezzi necessari** e **gestione a proprio rischio**, il compimento di
  un'**opera** o di un **servizio** verso un **corrispettivo in danaro**. Gli elementi
  "organizzazione" e "rischio" distinguono l'appalto dal **contratto d'opera** (art. 2222, in cui
  prevale il lavoro personale del prestatore).
- **Subappalto** (art. 1656): l'appaltatore **non puo'** subappaltare senza **autorizzazione**
  del committente.
- **Corrispettivo** (art. 1657): se non determinato, si calcola su **tariffe/usi**; in mancanza,
  lo determina il **giudice**.
- **Materia** (art. 1658): e' fornita dall'**appaltatore**, salvo diversa convenzione o uso.

## Variazioni del progetto (artt. 1659-1661)

- **Concordate** (art. 1659): l'appaltatore non puo' variare le modalita' convenute senza
  **autorizzazione**, da **provare per iscritto**; se il prezzo e' **globale** (a corpo), non ha
  diritto a compenso per variazioni/aggiunte salvo patto diverso.
- **Necessarie** (art. 1660): se servono variazioni per la **regola d'arte** e le parti non si
  accordano, decide il **giudice** (variazioni e prezzo); se l'importo supera il **sesto** del
  prezzo, l'**appaltatore** puo' recedere con equa indennita'; se le variazioni sono di notevole
  entita', il **committente** puo' recedere con equo indennizzo.
- **Ordinate dal committente** (art. 1661): ammesse entro il **sesto** del prezzo, con **compenso
  per i maggiori lavori** (anche a prezzo globale); il limite non vale se le variazioni, pur entro
  il sesto, importano **notevoli modificazioni** della natura dell'opera o dei quantitativi.

## Verifica, difetti, onerosita', pagamento (artt. 1662-1666)

- **Verifica in corso d'opera** (art. 1662): il committente controlla e, se l'esecuzione non
  procede secondo contratto e regola d'arte, fissa un **congruo termine**; decorso inutilmente, il
  contratto e' **risoluto** salvo risarcimento.
- **Difetti della materia** (art. 1663): l'appaltatore deve dare **pronto avviso** dei difetti
  della materia fornita dal committente.
- **Onerosita'/difficolta'** (art. 1664): per variazioni **impreviste** di costo di materiali/
  manodopera oltre il **decimo** del prezzo, si puo' chiedere la **revisione** (solo per la parte
  eccedente il decimo); per **difficolta' geologiche/idriche** impreviste, spetta un **equo
  compenso**.
- **Verifica e pagamento** (art. 1665): il committente ha diritto di **verificare** l'opera prima
  della consegna; l'opera si considera **accettata** se il committente non verifica senza giusti
  motivi, o riceve la consegna **senza riserve**; con l'accettazione sorge il diritto al
  **pagamento**.
- **Singole partite** (art. 1666): per opere **a partite**, la verifica e il pagamento possono
  avvenire **per partite**; il pagamento presume l'accettazione della parte pagata (non i semplici
  **acconti**).

## Recesso unilaterale del committente (art. 1671)

Il **committente** puo' **recedere** dal contratto in **ogni momento** (anche a esecuzione
iniziata), purche' tenga **indenne** l'appaltatore di: **spese** sostenute, **lavori eseguiti** e
**mancato guadagno**.

## Cosa NON fa (limiti)

- **Non redige** il contratto d'appalto ne' gli atti (autorizzazioni scritte alle variazioni,
  riserve, verbali di verifica, diffide, dichiarazioni di recesso).
- **Non quantifica** corrispettivi, revisioni, indennita' o mancato guadagno.
- **Non tratta** la **responsabilita'** per difformita', vizi e rovina (artt. 1667-1669, skill
  `responsabilita-appaltatore-rovina-cc`), l'estinzione/morte dell'appaltatore (artt. 1672-1677) ne'
  l'**appalto pubblico** (D.Lgs. 36/2023).

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`inquadra-contratto-appalto`](tasks/inquadra-contratto-appalto.md) | Inquadra nozione, subappalto, corrispettivo, materia e regime della verifica/pagamento di un appalto privato (artt. 1655-1658, 1662, 1665-1666) |
| [`gestisci-variazioni-recesso`](tasks/gestisci-variazioni-recesso.md) | Inquadra le variazioni del progetto (soglia del sesto), l'onerosita' sopravvenuta (soglia del decimo) e il recesso del committente (artt. 1659-1661, 1664, 1671) |

## Riferimenti normativi

- **Codice civile (R.D. 16 marzo 1942, n. 262)** - Libro IV, Titolo III, **Capo VII (Dell'appalto)**:
  artt. **1655** (nozione), **1656** (subappalto), **1657** (corrispettivo), **1658** (materia),
  **1659-1661** (variazioni), **1662** (verifica in corso d'opera), **1663** (difetti della
  materia), **1664** (onerosita'/difficolta'), **1665** (verifica e pagamento), **1666** (singole
  partite), **1671** (recesso unilaterale).
- Citati come **rinvio** (non riprodotti): artt. **1667-1669** (difformita', vizi, rovina - skill
  dedicata), artt. **1672-1677** (estinzione, morte dell'appaltatore), art. **2222** (contratto
  d'opera), **D.Lgs. 36/2023** (Codice dei contratti pubblici).

Dettaglio in `references/sources.yaml`, `references/fonti/cc-appalto-1655-1671.md`,
`references/estratti/contratto-appalto-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: la redazione del contratto, la qualificazione in concreto del
rapporto (appalto vs contratto d'opera/subfornitura), la quantificazione degli importi e la
gestione del contenzioso restano responsabilita' delle **parti** e dei loro **consulenti legali/
tecnici**, sul testo vigente degli artt. 1655 ss. La skill **non sostituisce** l'avvocato, il CTU
ne' la lettura degli articoli del Codice civile e delle clausole contrattuali.
