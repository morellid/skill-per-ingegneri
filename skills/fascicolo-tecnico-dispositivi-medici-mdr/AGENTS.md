# AGENTS.md - fascicolo-tecnico-dispositivi-medici-mdr

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale alla **struttura del fascicolo tecnico** (documentazione
tecnica) di un **dispositivo medico di classe I o IIa** e al **percorso di
valutazione della conformita'** ai sensi del **Reg. (UE) 2017/745 (MDR)**. Target:
ingegneri biomedici, fabbricanti di dispositivi medici, uffici RA/QA.

**E' una skill documentale**: non classifica il dispositivo (allegato VIII), non
redige la valutazione clinica ne' individua le norme armonizzate.

## Nota sull'area di catalogo

Il repo ha 8 aree fisse (`areas.yaml`), senza un'area "biomedico". Il dispositivo
medico e' pero' un **prodotto immesso sul mercato** con documentazione tecnica e
marcatura CE: la skill e' classificata in **impianti-macchine-prodotti** (compliance
di prodotto), coerentemente con le altre skill di conformita' di prodotto (PED, CRA,
marcatura CE elettrici, SDS). Se in futuro si raggiungono >= 3 skill biomedicali, si
potra' valutare la promozione a un'area dedicata (una riga nel frontmatter).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **reg-ue-2017-745-mdr**: Reg. (UE) 2017/745 (MDR), testo consolidato eur-lex,
  online-only (`binary_path: null`, `sha256: null`; eur-lex non riproducibile con
  hash stabile, stesso approccio della skill ai-act-compliance). Allegato II
  (documentazione tecnica), allegato III (PMS), art. 52 (procedure classi I e IIa),
  intestazione allegato VIII: trascritti verbatim in
  `references/fonti/reg-ue-2017-745-mdr.md`.

Estratto operativo: `references/estratti/fascicolo-tecnico-mdr-checklist.md`.

## Punti chiave (verificati sul testo)

- **Allegato II** (6 capitoli): 1 descrizione e specifiche (con classe e
  giustificazione all. VIII); 2 informazioni del fabbricante; 3 progettazione e
  fabbricazione; 4 requisiti generali di sicurezza e prestazione (all. I); 5 analisi
  rischi/benefici e gestione del rischio; 6 verifica e convalida (valutazione
  clinica, PMCF).
- **Allegato III**: piano PMS (art. 84); rapporto sulla sicurezza (classe I) o PSUR
  (IIa/IIb/III) - artt. 85-86.
- **Art. 52 §7 (classe I)**: autodichiarazione + dichiarazione UE (art. 19); Is/Im/Ir
  con organismo notificato **limitato** a sterilita'/metrologia/riutilizzo.
- **Art. 52 §6 (classe IIa)**: allegato IX (capi I e III) **oppure** documentazione
  tecnica (all. II + III) + allegato XI (punto 10 o 18); con organismo notificato.

## Convenzioni specifiche

### Cosa NON fare
- Non **classificare** il dispositivo (regole allegato VIII): la classe e' un input.
- Non redigere **valutazione clinica**, gestione del rischio o prove: strutturarle.
- Non individuare **norme armonizzate** (a pagamento) ne' MDCG guidance.
- Non trattare **IVDR** (Reg. 2017/746), dispositivi su misura, classi IIb/III: solo
  rinvio.

### Cosa fare
- Comporre i 6 capitoli dell'allegato II e la documentazione PMS (allegato III).
- Individuare il percorso di conformita' (art. 52) per classe I/Is/Im/Ir/IIa.
- Chiudere con il rinvio al fabbricante / valutatore clinico / organismo notificato.

## Aggiornamento della fonte

eur-lex online-only (testo consolidato): a ogni aggiornamento rileggere gli allegati
II, III, VIII e l'art. 52 nella versione consolidata piu' recente.

## Validatori

- Non ancora assegnato (Livello 2 da effettuare con esperto RA dispositivi medici).

## Stato attuale

- Versione: 0.1.0-alpha (closes #47)
- Task files: 2 (`struttura-fascicolo-tecnico.md`, `scegli-percorso-conformita.md`)
- Esempi: 2 (classe I sterile Is; classe IIa percorso e fascicolo)
