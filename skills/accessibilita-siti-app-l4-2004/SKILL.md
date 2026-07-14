---
name: accessibilita-siti-app-l4-2004
description: "Supporto documentale agli obblighi di accessibilita' dei siti web e delle applicazioni mobili ai sensi della Legge Stanca (L. 4/2004, testo vigente aggiornato dal D.Lgs. 106/2018 di recepimento della dir. UE 2016/2102): aiuta a determinare se un soggetto e' obbligato (soggetti pubblici e assimilati dell'art. 3 c. 1 - PA, concessionari di servizi pubblici, organismi di diritto pubblico, soggetti con contributi pubblici; grandi privati dell'art. 3 c. 1-bis con fatturato medio sopra 500 milioni), le esclusioni (art. 3 c. 2), gli obblighi negli appalti IT e la nullita' dei contratti per siti e app non accessibili (art. 4), il rinvio ai requisiti tecnici delle linee guida AgID (art. 11, che recepiscono EN 301 549 e WCAG), la vigilanza e il monitoraggio AgID (art. 7) e le responsabilita' e sanzioni (art. 9: responsabilita' dirigenziale per il pubblico, sanzione AgID fino al 5 per cento del fatturato per i grandi privati). Use when an Italian public body or large private operator must map digital-accessibility duties, contract nullity and penalties; it is a documentary aid and does not run the WCAG technical audit nor draft the accessibility statement."
license: MIT
area: software-dati-cybersecurity
title: "Accessibilita' siti web e app - Legge Stanca (L. 4/2004)"
summary: "Obblighi di accessibilita' di siti web e app (Legge Stanca, L. 4/2004): chi e' obbligato (soggetti pubblici art. 3 c. 1; grandi privati > 500 mln art. 3 c. 1-bis), obblighi negli appalti e nullita' dei contratti (art. 4), requisiti tecnici AgID (art. 11), sanzioni (art. 9)"
normative_refs:
  - "L. 9/1/2004 n. 4 (Legge Stanca, testo vigente) - artt. 2, 3, 4, 7, 9, 11 (agg. D.Lgs. 106/2018, dir. UE 2016/2102)"
version: 0.1.0-alpha
status: alpha
tags:
  - legge-4-2004
  - accessibilita
  - siti-web
  - applicazioni-mobili
  - agid
---

# Accessibilita' siti web e app - Legge Stanca (L. 4/2004)

## Quando usare questa skill

Usala quando devi orientarti sugli obblighi di **accessibilita' dei siti web e
delle applicazioni mobili** ai sensi della **Legge Stanca (L. 4/2004)**, nel testo
vigente (aggiornato dal D.Lgs. 106/2018, recepimento della dir. UE 2016/2102):

- capire se un soggetto e' **obbligato** (soggetti pubblici e assimilati dell'art.
  3 c. 1; **grandi privati** dell'art. 3 c. 1-bis con fatturato > 500 mln) e le
  **esclusioni** (art. 3 c. 2);
- gli **obblighi negli appalti IT** e la **nullita' dei contratti** per siti/app
  non accessibili (art. 4);
- il rinvio ai **requisiti tecnici** delle **linee guida AgID** (art. 11);
- la **vigilanza/monitoraggio AgID** (art. 7) e le **responsabilita'/sanzioni**
  (art. 9).

**Non e' una skill di calcolo**: non esegue l'audit tecnico WCAG dei singoli
criteri, non redige la dichiarazione di accessibilita' ne' riproduce le linee
guida AgID.

## Cosa NON fa (limiti)

- Non riproduce i **requisiti tecnici** (linee guida AgID, EN 301 549, WCAG 2.1)
  ne' esegue l'audit dei criteri di successo: rinvia alle linee guida AgID.
- Non redige la **dichiarazione di accessibilita'** ne' compila i modelli AgID.
- Non tratta l'**European Accessibility Act** (D.Lgs. 82/2022) per prodotti e
  servizi privati oltre ai richiami.
- Non sostituisce l'AgID, il RTD ne' il tecnico incaricato.

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`verifica-obbligo`](tasks/verifica-obbligo.md) | Dato il soggetto (natura pubblica/privata, fatturato, tipo di servizio), determina se e' obbligato (art. 3 c. 1 / c. 1-bis), le esclusioni e il regime di responsabilita'/sanzioni applicabile |
| [`checklist-appalto-contratto`](tasks/checklist-appalto-contratto.md) | Verifica gli obblighi di accessibilita' negli appalti IT e nei contratti di realizzazione/modifica di siti e app (necessarieta' dei requisiti, clausola di nullita', adeguamento) - art. 4 |

## Riferimenti normativi

- **L. 9/1/2004 n. 4** (Legge Stanca), testo vigente su Normattiva (pagina indice
  pinnata `!vig=2026-07-14`) - artt. 2 (definizioni), 3 (ambito), 4 (obblighi), 7
  (AgID), 9 (responsabilita'), 11 (requisiti tecnici).

Dettaglio in `references/sources.yaml`, `references/fonti/legge-4-2004.md`,
`references/estratti/accessibilita-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: i requisiti tecnici e l'audit di conformita'
richiedono la lettura delle linee guida AgID e delle WCAG e l'intervento di
tecnici; la responsabilita' resta del soggetto obbligato.
