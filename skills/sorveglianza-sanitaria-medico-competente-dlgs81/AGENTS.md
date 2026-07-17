# AGENTS.md - sorveglianza-sanitaria-medico-competente-dlgs81

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale alla **sorveglianza sanitaria** dei lavoratori e agli **obblighi del medico
competente** (D.Lgs. 81/2008, artt. 25, 38-41): casi, tipi di visita, giudizio di idoneita' alla
mansione, ricorso, requisiti del medico competente. Target: datori di lavoro, RSPP, consulenti
della sicurezza.

**E' una skill documentale**: inquadra il quadro e gli adempimenti; **non esprime giudizi
sanitari** (esclusivi del medico competente), non riproduce gli Allegati 3A/3B e non sostituisce il
medico competente/RSPP/datore.

## Nota sull'area e sulla complementarita'

Area **sicurezza-lavoro-cantieri**. Complementare a `dvr-generico` (la valutazione dei rischi
attiva la sorveglianza), `duvri-interferenze-dlgs81`, `piano-emergenza-antincendio-dm2021`,
`mog-231-sicurezza-lavoro`: questa copre la **sorveglianza sanitaria**.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-81-2008-sorveglianza**: D.Lgs. 81/2008, indice Normattiva pinnato `!vig=2026-07-16`
  (hash `d8991985...`, codice 008G0104). Artt. 25, 38, 39, 40, 41 (testo vigente) via
  `caricaArticolo`, trascritti verbatim.

Trascrizione in `references/fonti/dlgs-81-2008-sorveglianza.md`; estratto in
`references/estratti/sorveglianza-sanitaria-checklist.md`.

## Punti chiave (verificati sul testo)

- **Art. 41, c. 1**: sorveglianza nei **casi di legge** e in base al **DVR**, o su richiesta del
  lavoratore.
- **c. 2**: visite preventiva/preassuntiva, periodica (**di norma annuale**), su richiesta, cambio
  mansione, cessazione, **ripresa dopo > 60 gg**, alcol/sostanze.
- **c. 3-4**: divieti (no gravidanza); visite **a spese del datore**.
- **c. 6**: quattro giudizi (idoneita'; idoneita' parziale con prescrizioni/limitazioni; inidoneita'
  temporanea; inidoneita' permanente); **c. 6-bis** forma scritta; **c. 7** limiti temporali.
- **c. 9**: **ricorso all'ASL entro 30 giorni**.
- **Art. 25** obblighi (DVR, cartella sanitaria e di rischio - All. 3A, sopralluoghi); **artt. 38-40**
  requisiti, svolgimento, rapporti con il SSN (All. 3B).

## Convenzioni specifiche

### Cosa NON fare
- Non **esprimere giudizi sanitari** ne' definire i **protocolli sanitari** (esami/periodicita'
  puntuale): sono del medico competente.
- Non **riprodurre gli Allegati 3A/3B** ne' inventare periodicita'/valori.

### Cosa fare
- Inquadrare quando la sorveglianza e' dovuta, i tipi di visita, i giudizi e il ricorso, con gli
  obblighi/requisiti del medico competente.

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.Lgs. 81/2008 pinnato a nuovo `!vig=` (nuovo hash) e
rileggere gli artt. 25, 38-41 (soggetti a modifiche frequenti - es. L. 203/2024).

## Validatori

- Non ancora assegnato (Livello 2 con medico competente / RSPP).

## Stato attuale

- Versione: 0.1.0-alpha (closes #263)
- Task files: 2 (`imposta-sorveglianza-sanitaria.md`, `gestisci-giudizio-idoneita-ricorso.md`)
- Esempi: 2 (rientro dopo assenza > 60 giorni; giudizio con limitazioni e ricorso)
