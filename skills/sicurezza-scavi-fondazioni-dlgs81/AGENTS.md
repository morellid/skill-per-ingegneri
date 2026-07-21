# AGENTS.md - sicurezza-scavi-fondazioni-dlgs81

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **coordinatore per la sicurezza** (CSP/CSE), al **direttore dei lavori** e
all'**impresa** per la **sicurezza degli scavi e delle fondazioni** in cantiere (splateamenti,
sbancamenti, pozzi, trincee, cunicoli): inclinazione/armatura delle fronti, deposito sul ciglio,
presenza di gas, ai sensi del **D.Lgs. 9 aprile 2008, n. 81, Titolo IV, Capo II, Sezione III, artt.
118-121**. Target: coordinatori, direttori dei lavori, imprese, uffici tecnici.

**E' una skill documentale per il tecnico**: inquadra obblighi, presidi e soglie; **non redige** il
POS/PSC ne' la relazione geotecnica, **non dimensiona** armature/sbadacchiature, **non calcola** la
stabilita' delle pareti.

## Nota sull'area e sulla complementarita'

Area **sicurezza-lavoro-cantieri**. Distinta da `terre-rocce-scavo-dpr120` (gestione delle **terre e
rocce da scavo**, DPR 120/2017) e da `capacita-portante-fondazione-ntc` (**geotecnica**, capacita'
portante): questa copre la **sicurezza** degli scavi in cantiere. Complementare a
`pos-allegato-xv-checker`, `coordinatori-sicurezza-cantieri-dlgs81`, `dispositivi-protezione-
individuale-dlgs81` e `segnaletica-salute-sicurezza-dlgs81`.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-81-2008-118-121**: D.Lgs. 81/2008, pagina indice Normattiva pinnata a `!vig=2026-07-17` (hash
  `18fbc542...`; codice 008G0104, idGruppo 21). Artt. 118 (v2), 119 (v2), 120 (v1), 121 (v1) caricati
  via `caricaArticolo` (formato AKN) e trascritti verbatim.

Trascrizione in `references/fonti/dlgs-81-2008-118-121.md`; estratto operativo in
`references/estratti/sicurezza-scavi-checklist.md`.

## Punti chiave (verificati sul testo)

- **Splateamento** (art. 118): inclinazione/tracciato anti-franamento; **divieto di scalzamento alla
  base oltre m 1,50** (c. 1); armatura se rischio frane (c. 2); divieti su escavatore/ciglio (c. 3);
  delimitazione (c. 5).
- **Pozzi/scavi/cunicoli** (art. 119): **armature oltre m 1,50** (c. 1); tavole **sporgenti >= 30 cm**
  (c. 2); sottomurazioni (c. 4); **impalcato nei pozzi oltre 3 m** (c. 6); assistenza esterna e
  recupero infortunato (c. 7); Allegato XVIII punto 3.4 (c. 7-bis).
- **Deposito sul ciglio** (art. 120): vietato, salvo puntellature.
- **Gas negli scavi** (art. 121): DPI vie respiratorie + sistema di salvataggio con sorveglianza esterna
  (c. 2); bonifica/ventilazione e divieto fiamme (c. 4); lavoro in coppia (c. 5).

## Convenzioni specifiche

### Cosa NON fare
- Non **redigere** il POS/PSC ne' la relazione geotecnica; non **dimensionare** armature/sbadacchiature
  ne' **calcolare** la stabilita' delle pareti dello scavo.
- Non riprodurre l'**Allegato XVIII**; rinvio.
- Non trattare la **gestione delle terre** (DPR 120/2017) ne' la **capacita' portante** geotecnica
  (NTC): rinvio alle skill dedicate.

### Cosa fare
- Inquadrare i presidi in base a tipo e profondita' dello scavo con le soglie 1,50 m / 30 cm / 3 m
  (artt. 118-120) e le misure contro i gas (art. 121); rinviare a progettista/relazione geotecnica per
  il dimensionamento e a DPR 177/2011 per gli ambienti confinati.

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.Lgs. 81/2008 pinnato a nuovo `!vig=` (nuovo hash) e rileggere gli
artt. 118-121, verificando le modifiche dei doppi tondi `(( ))` (D.Lgs. 106/2009).

## Validatori

- Non ancora assegnato (Livello 2 con coordinatore per la sicurezza/geotecnico).

## Stato attuale

- Versione: 0.1.0-alpha (closes #356)
- Task files: 2 (`inquadra-presidi-scavo.md`, `inquadra-gas-negli-scavi.md`)
- Esempi: 2 (trincea 2,20 m con armature e deposito sul ciglio; pozzo di fondazione 4 m con impalcato e
  rischio gas)
