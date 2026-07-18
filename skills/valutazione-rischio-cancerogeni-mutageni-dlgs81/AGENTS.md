# AGENTS.md - valutazione-rischio-cancerogeni-mutageni-dlgs81

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **RSPP/ASPP**, al **datore di lavoro** e al **tecnico della sicurezza** per
l'inquadramento della **valutazione e gestione del rischio da agenti cancerogeni, mutageni e da sostanze
tossiche per la riproduzione** ai sensi del **D.Lgs. 81/2008, Titolo IX, Capo II (artt. 233-243)**, nel
testo vigente aggiornato dal **D.Lgs. 135/2024**. Target: RSPP/ASPP, datori di lavoro, tecnici della
sicurezza e dell'igiene industriale.

**E' una skill documentale per il tecnico**: inquadra obblighi, contenuti, gerarchia delle misure e
adempimenti; **non redige** il DVR, **non esegue** misurazioni o campionamenti, **non applica** i valori
limite di esposizione.

## Nota sull'area e sulla complementarita'

Area **sicurezza-lavoro-cantieri**. Complementare, non sovrapposta, a `valutazione-rischio-chimico-dlgs81`
(Titolo IX **Capo I** - agenti chimici) e distinta dalle skill sui rischi fisici (rumore, vibrazioni) e
dagli agenti biologici (Titolo X, non coperto). Condivide con le altre skill D.Lgs 81 la stessa fonte
(indice Normattiva del D.Lgs 81/2008, codice 008G0104).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-81-2008-233-243**: D.Lgs. 81/2008, indice Normattiva pinnato a `!vig=2026-07-17` (hash
  `18fbc542...`; codice 008G0104, idGruppo 42/43/44 per il Capo II). Artt. 233 (v2), 234 (v3), 235 (v3),
  236 (v3), 237 (v2), 238 (v1), 239 (v2), 242 (v4), 243 (v3) letti via `caricaArticolo` (header
  X-Requested-With, formato AKN) e trascritti verbatim (testo vigente agg. D.Lgs. 135/2024).

Trascrizione in `references/fonti/dlgs-81-2008-233-243.md`; estratto in
`references/estratti/rischio-cancerogeni-checklist.md`.

## Punti chiave (verificati sul testo)

- **Campo** (233): cancerogeni/mutageni/tossici per la riproduzione; escluso l'amianto (Capo III).
- **Definizioni** (234): cat. 1A/1B CLP (Reg. CE 1272/2008) o allegato XLII; sostanza tossica per la
  riproduzione priva di soglia / con valore soglia (allegato XLIII); valore limite, valore limite
  biologico, sorveglianza sanitaria.
- **Sostituzione/riduzione** (235): sostituzione → sistema chiuso → riduzione al più basso valore
  tecnicamente possibile; esposizione ≤ valore limite (allegato XLIII).
- **Valutazione** (236): nel DVR (art. 17) e integrazione (art. 28 c. 2 / art. 29 c. 5).
- **Misure** (237-238): quantitativi minimi, limitazione esposti, aree con divieto di fumo, aspirazione
  localizzata (art. 18 c. 1 q), misurazione (allegato XLI), igiene e DPI.
- **Informazione/formazione** (239): prima dell'adibizione, quinquennale, etichettatura CLP.
- **Sorveglianza** (242): se rischio; parere del medico competente; allontanamento (art. 42).
- **Registro esposti** (243): tramite medico competente, accesso RSPP/RLS; cartelle (art. 25); invio
  INAIL; conservazione 40 anni (cancerogeni/mutageni) e ≥5 anni (tossici per la riproduzione).

## Convenzioni specifiche

### Cosa NON fare
- Non **redigere** il DVR né la valutazione del rischio; non **eseguire** misurazioni/campionamenti; non
  **applicare** i valori limite di esposizione.
- Non **riprodurre** gli Allegati XLI/XLII/XLIII/XLIII-bis né i regolamenti CLP/REACH.
- Non trattare l'**amianto** (Capo III), gli **agenti chimici** (Capo I) né gli **agenti biologici**
  (Titolo X).

### Cosa fare
- Inquadrare campo, definizioni, gerarchia sostituzione/riduzione, valutazione e integrazione del DVR,
  misure tecniche/organizzative/igieniche, informazione/formazione, sorveglianza sanitaria e registro
  esposti.

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.Lgs. 81/2008 pinnato a nuovo `!vig=` (nuovo hash) e rileggere gli
artt. 233-243 (via `caricaArticolo` con header `X-Requested-With: XMLHttpRequest` sulla sessione aperta da
`caricaDettaglioAtto`), verificando le modifiche dei doppi tondi `(( ))` (es. ulteriori adeguamenti dopo
il D.Lgs. 135/2024).

## Validatori

- Non ancora assegnato (Livello 2 con RSPP/tecnico della sicurezza o medico competente).

## Stato attuale

- Versione: 0.1.0-alpha (closes #370)
- Task files: 2 (`inquadra-valutazione-misure-cancerogeni.md`, `inquadra-sorveglianza-registro-esposti.md`)
- Esempi: 2 (officina galvanica Cr VI - valutazione e integrazione del DVR, gerarchia delle misure;
  polveri di legno duro - sorveglianza sanitaria e registro esposti)
