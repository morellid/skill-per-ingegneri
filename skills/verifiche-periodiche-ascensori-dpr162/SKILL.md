---
name: verifiche-periodiche-ascensori-dpr162
description: "Supporto documentale all'iter di esercizio, verifiche periodiche e manutenzione degli ascensori, montacarichi e apparecchi assimilati ai sensi del DPR 162/1999 (testo vigente, artt. 12-16). Copre la messa in esercizio (comunicazione al comune entro 60 giorni, numero di matricola entro 30 giorni), la verifica periodica ogni 2 anni e i soggetti che la eseguono (ASL/ARPA, ITL, MIT, organismi notificati, organismi di ispezione di tipo A accreditati), le verifiche straordinarie (esito negativo, incidenti, modifiche), gli obblighi di manutenzione (ditta abilitata, controlli almeno semestrali su paracadute, funi, isolamento) e il libretto e la targa. Use when an Italian building owner, administrator or engineer needs the DPR 162/1999 lift-operation obligations, the periodic-verification frequency and who performs it; it is a documentary aid and does not replace the owner, the maintainer or the verifying body."
license: MIT
area: impianti-macchine-prodotti
title: "Esercizio e verifiche periodiche ascensori - DPR 162/1999"
summary: "Iter di esercizio ascensori (DPR 162/1999, artt. 12-16): messa in esercizio (comunicazione al comune entro 60 gg, matricola entro 30 gg), verifica periodica ogni 2 anni e soggetti abilitati, verifiche straordinarie, manutenzione, libretto e targa; supporto documentale"
normative_refs:
  - "D.P.R. 30/4/1999 n. 162 (testo vigente) - artt. 12-16"
version: 0.1.0-alpha
status: alpha
tags:
  - dpr-162-1999
  - ascensori
  - verifiche-periodiche
  - manutenzione
  - sicurezza-impianti
---

# Esercizio e verifiche periodiche ascensori - DPR 162/1999

## Quando usare questa skill

Usala quando devi orientarti sull'iter di **esercizio** di un ascensore,
montacarichi o apparecchio assimilato (velocita' <= 0,15 m/s) ai sensi del DPR
162/1999:

- adempimenti di **messa in esercizio** (comunicazione al comune, numero di
  matricola);
- **periodicita' e soggetti** della verifica periodica (ogni 2 anni);
- casi di **verifica straordinaria**;
- obblighi di **manutenzione** e controlli periodici sui dispositivi di
  sicurezza;
- **libretto e targa**.

Target: proprietari e amministratori di condominio, ingegneri, ditte di
manutenzione, tecnici della sicurezza.

## Avvertenza

Questa skill e' un **supporto documentale** basato sul testo vigente del DPR
162/1999 (artt. 12-16). **Non copre** l'immissione sul mercato e la marcatura CE
dei componenti (artt. 1-11), **non definisce** le regole tecniche di
installazione (norme UNI EN, non riprodotte), **non calcola** le date concrete
delle scadenze e **non sostituisce** il proprietario, il manutentore o il
soggetto verificatore.

## Sotto-attivita' disponibili

- **Diagnosi degli adempimenti di esercizio**: dato lo stato dell'impianto,
  determina comunicazioni, periodicita' della verifica, soggetti e manutenzione
  -> `tasks/diagnosi-adempimenti.md`
- **Checklist di esercizio e verifiche**: verifica la completezza degli
  adempimenti (messa in esercizio, verifiche periodiche/straordinarie,
  manutenzione, libretto e targa) -> `tasks/checklist-esercizio.md`

Se la richiesta non e' chiara, chiedi all'utente quale sotto-attivita' desidera.

## Processo generale

1. Identifica la sotto-attivita'.
2. Carica il file `tasks/<task-scelto>.md`.
3. Richiedi gli input (tipo di impianto, stato degli adempimenti, eventi).
4. Applica la regola/checklist **citando l'articolo preciso** (artt. 12-16).
5. Chiudi con il rinvio agli obblighi del proprietario e ai soggetti competenti
   (comune, manutentore, verificatore).

## Fonti normative

Riferimenti completi in `references/sources.yaml`. Trascrizione verificata in
`references/fonti/dpr-162-1999.md` (testo vigente da Normattiva, pagina indice
pinnata `!vig=2026-07-14`), estratto operativo in
`references/estratti/verifiche-ascensori-checklist.md`.

## Limiti

Cosa questa skill NON fa:
- non copre l'immissione sul mercato / marcatura CE dei componenti (artt. 1-11,
  D.Lgs. 17/2010);
- non definisce le regole tecniche di installazione (norme UNI EN 81, a
  pagamento) ne' esegue calcoli;
- non redige la modulistica comunale ne' i portali telematici;
- non calcola le date concrete delle scadenze: fornisce periodicita' e obblighi.
