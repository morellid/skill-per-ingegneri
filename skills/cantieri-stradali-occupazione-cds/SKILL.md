---
name: cantieri-stradali-occupazione-cds
description: "Supporto documentale all'inquadramento dell'occupazione della sede stradale e dell'apertura di opere, depositi e cantieri stradali secondo il Codice della Strada (D.Lgs. 285/1992), artt. 20 e 21. Aiuta a inquadrare l'occupazione della sede stradale (art. 20: divieto di ogni occupazione sulle strade di tipo A, B, C e D, ivi comprese fiere e mercati; ammissibilita' condizionata sulle strade di tipo E ed F con itinerario alternativo o nelle zone di rilevanza storico-ambientale senza intralcio; limiti per chioschi, edicole e installazioni e per l'occupazione dei marciapiedi con almeno 2 metri liberi per i pedoni; sanzione e obbligo di rimozione) e le opere, i depositi e i cantieri stradali (art. 21: divieto di eseguire opere o depositi e aprire cantieri, anche temporanei, senza preventiva autorizzazione o concessione dell'ente competente ex art. 26; obbligo di adottare gli accorgimenti per la sicurezza e la fluidita' della circolazione e di rendere visibile giorno e notte il personale addetto; rinvio al regolamento per la delimitazione e segnalazione del cantiere; sanzione e rimozione delle opere). Use when a technician, contractor or public body must frame the road occupation permit and the opening of a temporary road works site under the Italian Highway Code; it is a documentary aid, does not issue permits, does not draft the temporary traffic signing plan and does not reproduce the implementing regulation or technical decree."
license: MIT
area: ambiente-territorio-mobilita
title: "Cantieri stradali e occupazione della sede stradale (CdS artt. 20, 21)"
summary: "Inquadra l'occupazione della sede stradale e i cantieri stradali (CdS, D.Lgs. 285/1992): divieto/ammissibilita' per tipo di strada, chioschi e marciapiedi (art. 20); apertura di opere/depositi/cantieri con preventiva autorizzazione, sicurezza e segnalazione (art. 21)."
normative_refs:
  - "D.Lgs. 30/4/1992 n. 285 (Codice della Strada) - art. 20 (occupazione della sede stradale)"
  - "D.Lgs. 30/4/1992 n. 285 (Codice della Strada) - art. 21 (opere, depositi e cantieri stradali)"
version: 0.1.0-alpha
status: alpha
tags:
  - codice-della-strada
  - dlgs-285-1992
  - cantieri-stradali
  - occupazione-suolo
  - segnaletica-temporanea
  - mobilita
---

# Cantieri stradali e occupazione della sede stradale (CdS artt. 20, 21)

## Quando usare questa skill

Usala quando devi **inquadrare l'occupazione della sede stradale** o l'apertura di un
**cantiere stradale**, ancorandola al **Codice della Strada (D.Lgs. 285/1992)**:

- **occupazione della sede stradale** - **art. 20**: **vietata** ogni occupazione (fiere,
  mercati, veicoli, baracche, tende) sulle strade di tipo **A, B, C, D**; **ammessa a
  condizioni** sulle strade di tipo **E ed F** (itinerario alternativo per il traffico, o
  nelle zone di rilevanza storico-ambientale senza intralcio/pregiudizio alla sicurezza) (c.
  1); **chioschi/edicole/installazioni** fuori dei centri abitati non consentiti sulle fasce
  di rispetto (c. 2); nei centri abitati **occupazione dei marciapiedi** fino a **meta'**
  della larghezza, in adiacenza ai fabbricati, lasciando **>= 2 m** liberi per i pedoni,
  fuori dai triangoli di visibilita' (c. 3); **sanzione** 173-694 euro e obbligo di
  **rimozione** delle opere abusive (cc. 4-5);
- **opere, depositi e cantieri stradali** - **art. 21**: e' **vietato** eseguire opere o
  depositi e aprire cantieri (anche temporanei) su strade/pertinenze/fasce di rispetto/aree
  di visibilita' **senza preventiva autorizzazione o concessione** dell'ente competente
  (**art. 26**) (c. 1); obbligo di adottare gli **accorgimenti per la sicurezza e la
  fluidita'** della circolazione, mantenerli **efficienti giorno e notte** e rendere
  **visibile il personale** addetto (c. 2); il **regolamento** stabilisce delimitazione,
  segnalazione e modalita' di svolgimento (c. 3); **sanzione** 866-3.464 euro e obbligo di
  **rimozione** delle opere (cc. 4-5).

**Non e' una skill operativa**: non rilascia autorizzazioni, non redige il piano di
segnaletica temporanea e non riproduce il regolamento/disciplinare tecnico.

## Cosa NON fa (limiti)

- Non **rilascia** autorizzazioni/concessioni (art. 26): rinvia all'ente proprietario/
  gestore della strada.
- Non **redige** il **piano di segnaletica temporanea** ne' gli schemi di cantiere.
- Non riproduce il **Regolamento (DPR 495/1992, artt. 30-43)** ne' il **disciplinare
  tecnico DM 10/7/2002** (schemi segnaletici): rinvio.
- Non tratta la **sicurezza dei lavoratori** nei cantieri stradali (D.Lgs. 81/2008, POS,
  coordinatori): skill dedicate; fuori perimetro.
- Non riproduce la **classificazione delle strade** (art. 2) ne' la disciplina delle
  fasce/distanze (artt. 16-18): citate come rinvio.

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`inquadra-cantiere-stradale`](tasks/inquadra-cantiere-stradale.md) | Verifica l'obbligo di preventiva autorizzazione/concessione (art. 21, art. 26) e gli obblighi di sicurezza/segnalazione del cantiere, con il rinvio al regolamento |
| [`inquadra-occupazione-suolo`](tasks/inquadra-occupazione-suolo.md) | Inquadra l'ammissibilita' dell'occupazione della sede stradale per tipo di strada e i limiti per chioschi/marciapiedi (art. 20) |

## Riferimenti normativi

- **D.Lgs. 30 aprile 1992, n. 285** (Codice della Strada) - artt. **20** (occupazione
  della sede stradale) e **21** (opere, depositi e cantieri stradali); richiamati gli artt.
  **2** (classificazione strade), **18** (fasce/visibilita'), **26** (autorizzazioni/
  concessioni), il **Regolamento DPR 495/1992** (artt. 30-43) e il **DM 10/7/2002**
  (disciplinare segnaletica temporanea).

Dettaglio in `references/sources.yaml`,
`references/fonti/cds-285-1992-20-21.md`,
`references/estratti/cantieri-stradali-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: il rilascio delle autorizzazioni/concessioni, la
redazione del piano di segnaletica temporanea e l'applicazione del regolamento e del
disciplinare tecnico restano in capo all'**ente proprietario/gestore della strada** e al
**tecnico/impresa** esecutrice. **Non sostituisce** questi soggetti ne' la lettura degli
artt. 20 e 21 del Codice della Strada, del Regolamento DPR 495/1992 e del DM 10/7/2002.
