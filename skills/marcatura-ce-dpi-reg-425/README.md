# marcatura-ce-dpi-reg-425

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con esperto di marcatura CE dei DPI da completare)

Skill di **supporto documentale** al **fabbricante**, all'**ufficio tecnico** e al **tecnico** per
l'**inquadramento della classificazione, della valutazione della conformità e della marcatura CE** dei
**dispositivi di protezione individuale (DPI)** come prodotti secondo il **Regolamento (UE) 2016/425**:
categorie di rischio, procedure di conformità per categoria, obblighi documentali, dichiarazione di
conformità UE e marcatura CE.

**Non progetta** né **certifica** il DPI, **non esegue** prove e **non sostituisce** il fabbricante:
fornisce le categorie di rischio (Allegato I), le procedure di conformità (art. 19), gli obblighi del
fabbricante (artt. 8-9), la dichiarazione UE (art. 15, All. IX) e le regole della marcatura CE (artt.
16-17).

## Target

Fabbricanti di DPI, uffici tecnici/qualità, tecnici e RSPP che devono inquadrare la conformità e la
marcatura CE dei DPI come prodotti secondo il Reg. UE 2016/425.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-categoria-procedura-dpi` | Categoria di rischio (I/II/III, All. I) e procedura di conformità applicabile (art. 19, moduli/allegati) |
| `inquadra-obblighi-dichiarazione-marcatura-dpi` | Obblighi del fabbricante/mandatario (artt. 8-9), dichiarazione UE (art. 15, All. IX) e marcatura CE (artt. 16-17) |

Nucleo: **categorie di rischio** I/II/III, **procedura** di conformità (moduli A / B+C / B+C2 o D),
**obblighi** documentali del fabbricante, **dichiarazione di conformità UE** (Allegato IX) e **marcatura
CE**.

## Relazione con altre skill

- **Distinta** da `dpi-protezione-individuale-dlgs81` (uso e scelta dei DPI da parte del **datore di
  lavoro**, D.Lgs 81/2008 artt. 74-79): questa copre il **lato prodotto/fabbricante** (Reg. 2016/425).
- Appartiene al gruppo "marcatura CE dei prodotti" con `marcatura-ce-elettrici-lvd-emc-red`,
  `dop-marcatura-ce-prodotti-cpr`, `fascicolo-tecnico-macchine-reg-1230`, ecc.

## Fonti consultate

- **Regolamento (UE) 2016/425 (DPI)** - GU UE L 81 del 31.3.2016 - testo EUR-Lex (CELEX 32016R0425, SHA256
  `8b4c61bb...`), estratto con `pdftotext` e trascritto verbatim.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non progetta** né **certifica** il DPI; **non esegue** prove né l'esame UE del tipo.
- **Non riproduce** in dettaglio i **requisiti essenziali** (All. II) né i **moduli** (All. IV-VIII); **non
  individua** le norme armonizzate; **non tratta** gli organismi notificati (artt. 20+).

**La skill è un supporto documentale: non sostituisce l'organismo notificato, il fabbricante, né la lettura del Reg. UE 2016/425 e dei suoi allegati.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
