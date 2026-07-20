---
name: marcatura-ce-dpi-reg-425
description: "Supporto documentale al fabbricante, all'ufficio tecnico e al tecnico per l'inquadramento della classificazione, della valutazione della conformita' e della marcatura CE dei dispositivi di protezione individuale (DPI) come prodotti secondo il Regolamento (UE) 2016/425. Aiuta a inquadrare la classificazione del DPI nelle categorie di rischio dell'Allegato I: categoria I per i soli rischi minimi (lesioni meccaniche superficiali, prodotti di pulizia poco aggressivi o contatto prolungato con l'acqua, superfici calde non oltre 50 gradi, luce solare, condizioni atmosferiche non estreme), categoria II per i rischi diversi da quelli delle categorie I e III, e categoria III per i soli rischi che possono causare morte o danni irreversibili (sostanze e miscele pericolose, carenza di ossigeno, agenti biologici nocivi, radiazioni ionizzanti, alta temperatura oltre 100 gradi, bassa temperatura sotto meno 50 gradi, cadute dall'alto, scosse elettriche e lavoro sotto tensione, annegamento, tagli da seghe a catena, getti ad alta pressione, ferite da proiettile o coltello, rumore nocivo); la procedura di valutazione della conformita' applicabile per categoria (articolo 19): categoria I con il controllo interno della produzione, modulo A dell'Allegato IV; categoria II con l'esame UE del tipo, modulo B dell'Allegato V, seguito dalla conformita' al tipo su controllo interno, modulo C dell'Allegato VI; categoria III con l'esame UE del tipo, modulo B, e in aggiunta il modulo C2 dell'Allegato VII o il modulo D dell'Allegato VIII, con deroga per i DPI su misura di categoria III; gli obblighi del fabbricante (articolo 8: progettazione secondo i requisiti essenziali di salute e sicurezza dell'Allegato II, documentazione tecnica dell'Allegato III, dichiarazione di conformita' UE, marcatura CE, conservazione decennale, identificazione e istruzioni) e del mandatario (articolo 9); la dichiarazione di conformita' UE con la struttura tipo dell'Allegato IX (articolo 15); e le regole di apposizione della marcatura CE (articoli 16-17), con il numero dell'organismo notificato per i DPI di categoria III. Use when a manufacturer or a technician must frame the classification, the conformity assessment and the CE marking of personal protective equipment (PPE) as products under the EU Regulation 2016/425; it is a documentary aid and does NOT design or certify the PPE, does NOT run the tests or the EU type-examination, does NOT reproduce in detail the essential health and safety requirements (Annex II) nor the modules (Annexes IV-VIII), does NOT identify the applicable harmonised standards, and does NOT replace the notified body or the manufacturer. It is distinct from the dpi-protezione-individuale-dlgs81 skill, which covers the use and selection of PPE by the employer (D.Lgs 81/2008)."
license: MIT
area: impianti-macchine-prodotti
title: "Marcatura CE dei dispositivi di protezione individuale - DPI (Reg. UE 2016/425)"
summary: "Inquadra classificazione, valutazione della conformita' e marcatura CE dei DPI (Reg. UE 2016/425): categorie di rischio I/II/III (All. I), procedure per categoria (art. 19: modulo A; B+C; B+C2 o D), obblighi del fabbricante (art. 8) e marcatura CE (artt. 16-17)."
normative_refs:
  - "Reg. (UE) 2016/425 (DPI) - art. 8 (obblighi fabbricante), art. 15 (dichiarazione UE), artt. 16-17 (marcatura CE), art. 18 e All. I (categorie di rischio I/II/III), art. 19 (moduli A/B/C/C2/D)"
  - "Rinvio (non riprodotti): Allegato II (requisiti essenziali), Allegato III (documentazione tecnica), Allegati IV-VIII (moduli), Allegato IX (dichiarazione UE); norme armonizzate EN; Reg. (CE) 765/2008"
version: 0.1.0-alpha
status: alpha
tags:
  - marcatura-ce
  - dpi
  - reg-ue-2016-425
  - categorie-di-rischio
  - valutazione-conformita
---

# Marcatura CE dei dispositivi di protezione individuale - DPI (Reg. UE 2016/425)

## Quando usare questa skill

Usala quando un **fabbricante**, un **ufficio tecnico** o un **tecnico** deve **inquadrare** la
**classificazione**, la **valutazione della conformità** e la **marcatura CE** di un **dispositivo di
protezione individuale (DPI)** come prodotto, secondo il **Regolamento (UE) 2016/425**:

- **categorie di rischio** I / II / III (art. 18, Allegato I);
- **procedura di conformità** per categoria (art. 19: moduli A / B+C / B+C2 o D);
- **obblighi** del fabbricante e del mandatario (artt. 8-9);
- **dichiarazione di conformità UE** (art. 15, Allegato IX) e **marcatura CE** (artt. 16-17).

**Non è** uno strumento che progetta o certifica il DPI, né esegue le prove: è un **supporto documentale**
che inquadra classificazione, procedura, obblighi e marcatura. È **distinta** da
`dpi-protezione-individuale-dlgs81` (uso e scelta dei DPI lato datore di lavoro).

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-categoria-procedura-dpi` | Categoria di rischio (I/II/III, All. I) e procedura di conformità applicabile (art. 19, moduli/allegati) |
| `inquadra-obblighi-dichiarazione-marcatura-dpi` | Obblighi del fabbricante/mandatario (artt. 8-9), dichiarazione UE (art. 15, All. IX) e marcatura CE (artt. 16-17) |

## Punti chiave (verificati sul testo)

- **Categorie di rischio** (art. 18, All. I): **I** rischi minimi (superfici calde ≤ 50 °C, luce solare,
  ecc.), **II** rischi diversi da I e III (residuale), **III** rischi gravissimi (morte/danni
  irreversibili: sostanze pericolose, cadute dall'alto, scosse elettriche, ≥ 100 °C, ≤ −50 °C, ecc.).
- **Procedure** (art. 19): **cat. I** → modulo A (controllo interno, All. IV); **cat. II** → modulo B (esame
  UE del tipo, All. V) + modulo C (All. VI); **cat. III** → modulo B + modulo C2 (All. VII) o modulo D
  (All. VIII); deroga cat. II per DPI su misura di cat. III.
- **Obblighi fabbricante** (art. 8): RESS (All. II), documentazione tecnica (All. III), dichiarazione UE,
  marcatura CE, **conservazione 10 anni**, identificazione, istruzioni; **mandatario** (art. 9) non progetta
  né redige la documentazione tecnica.
- **Dichiarazione UE** (art. 15, All. IX): struttura tipo; responsabilità del fabbricante.
- **Marcatura CE** (artt. 16-17): visibile/leggibile/indelebile, prima dell'immissione; per la **categoria
  III** seguita dal **numero dell'organismo notificato**.

## Fonti

- **Regolamento (UE) 2016/425 (DPI)** - GU UE L 81 del 31.3.2016 - testo EUR-Lex (CELEX 32016R0425, SHA256
  `8b4c61bb...`), estratto con `pdftotext` e trascritto verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non progetta** né **certifica** il DPI; **non esegue** prove né l'esame UE del tipo.
- **Non riproduce** in dettaglio i **requisiti essenziali** (All. II) né i **moduli** (All. IV-VIII); **non
  individua** le norme armonizzate; **non tratta** gli organismi notificati (artt. 20+).
- È **distinta** da `dpi-protezione-individuale-dlgs81` (uso/scelta dei DPI lato datore, D.Lgs 81 artt.
  74-79).

**La skill è un supporto documentale: non sostituisce l'organismo notificato, il fabbricante, né la lettura del Reg. UE 2016/425 e dei suoi allegati.**
