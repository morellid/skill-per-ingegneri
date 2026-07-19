# AGENTS.md - valutazione-rischio-biologico-dlgs81

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **RSPP/ASPP**, al **datore di lavoro** e al **tecnico della sicurezza** per
l'inquadramento della **valutazione e gestione del rischio da esposizione ad agenti biologici** ai sensi
del **D.Lgs. 81/2008, Titolo X (artt. 266-280)**. Target: RSPP/ASPP, datori di lavoro, tecnici della
sicurezza e dell'igiene industriale (sanità, laboratori, depurazione, zootecnia, ecc.).

**E' una skill documentale per il tecnico**: inquadra definizioni, classificazione, obblighi e
adempimenti; **non redige** il DVR, **non classifica** i singoli agenti e **non definisce** i livelli di
contenimento.

## Nota sull'area e sulla complementarita'

Area **sicurezza-lavoro-cantieri**. Complementare, non sovrapposta, a `valutazione-rischio-chimico-dlgs81`
(Titolo IX Capo I - agenti chimici) e `valutazione-rischio-cancerogeni-mutageni-dlgs81` (Titolo IX Capo
II). Condivide con le altre skill D.Lgs 81 la stessa fonte (indice Normattiva del D.Lgs 81/2008, codice
008G0104).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-81-2008-266-280**: D.Lgs. 81/2008, indice Normattiva pinnato a `!vig=2026-07-17` (hash
  `18fbc542...`; codice 008G0104, idGruppo 48/49/50 per il Titolo X). Artt. 266 (v1), 267 (v1), 268 (v1),
  271 (v1), 272 (v2), 273 (v2), 279 (v2), 280 (v2) letti via `caricaArticolo` (header X-Requested-With,
  formato AKN) e trascritti verbatim (testo vigente).

Trascrizione in `references/fonti/dlgs-81-2008-266-280.md`; estratto in
`references/estratti/rischio-biologico-checklist.md`.

## Punti chiave (verificati sul testo)

- **Definizioni** (267): agente biologico (microrganismo anche OGM, coltura cellulare, endoparassita) →
  infezioni/allergie/intossicazioni.
- **Classificazione** (268): 4 gruppi per rischio di infezione; dubbio → gruppo più elevato; allegato XLVI
  (gruppi 2/3/4).
- **Valutazione** (271): nel DVR (art. 17); buona prassi microbiologica; rivalutazione ogni 3 anni;
  allegato XLIV; programma di emergenza per gruppi 3/4; RLS consultato.
- **Misure** (272-273): limitare esposti, segnale di rischio biologico (allegato XLV), procedure di
  emergenza, smaltimento rifiuti; docce, indumenti separati, DPI disinfettati, divieti.
- **Sorveglianza** (279): art. 41 se necessaria; vaccini; allontanamento (art. 42).
- **Registro esposti** (280): solo gruppi 3/4; tramite RSPP, accesso MC/RLS; conservazione 10 anni (40
  anni per infezioni latenti/gravi sequele). Il testo cita ancora l'ISPESL (ora INAIL, L. 122/2010).

## Convenzioni specifiche

### Cosa NON fare
- Non **redigere** il DVR né la valutazione del rischio; non **classificare** i singoli agenti biologici.
- Non **riprodurre** gli Allegati XLIV/XLV/XLVI né definire i **livelli di contenimento** (artt. 274-275).
- Non trattare gli **agenti chimici** (Titolo IX Capo I) né i **cancerogeni/mutageni** (Titolo IX Capo II).

### Cosa fare
- Inquadrare definizioni, classificazione in 4 gruppi, valutazione e integrazione del DVR, misure tecniche/
  igieniche, sorveglianza sanitaria e registro degli esposti.

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.Lgs. 81/2008 pinnato a nuovo `!vig=` (nuovo hash) e rileggere gli
artt. 266-280 (via `caricaArticolo` con header `X-Requested-With: XMLHttpRequest` sulla sessione aperta da
`caricaDettaglioAtto`), verificando le modifiche dei doppi tondi `(( ))` e l'eventuale aggiornamento degli
allegati XLIV/XLV/XLVI.

## Validatori

- Non ancora assegnato (Livello 2 con RSPP/tecnico della sicurezza o medico competente).

## Stato attuale

- Versione: 0.1.0-alpha (closes #376)
- Task files: 2 (`inquadra-classificazione-valutazione-biologico.md`, `inquadra-sorveglianza-registro-biologico.md`)
- Esempi: 2 (laboratorio di analisi microbiologiche con gruppo 3 - valutazione e misure; impianto di
  depurazione con gruppo 2 - sorveglianza e registro, e cosa cambia con il gruppo 3)
