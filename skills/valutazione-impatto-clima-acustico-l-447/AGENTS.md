# AGENTS.md - valutazione-impatto-clima-acustico-l-447

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Skill di supporto al **tecnico competente in acustica ambientale (TCAA)**
e al progettista per la **documentazione previsionale di impatto
acustico** (L. 447/1995 art. 8 c. 2 e c. 4) e per la **valutazione
previsionale di clima acustico** (L. 447/1995 art. 8 c. 3) da allegare
a SCIA, PdC, autorizzazione/licenza per attivita' produttive, sportive,
ricreative, o per insediamenti sensibili (scuole, ospedali, case di
cura, parchi pubblici, residenze prossime a opere c. 2).

Gli adempimenti sono dettati dalla L. 26 ottobre 1995 n. 447 (legge
quadro sull'inquinamento acustico), dal DPCM 14 novembre 1997 (valori
limite, criterio differenziale, valori di attenzione e di qualita') e
dal DM Ambiente 16 marzo 1998 (tecniche di rilevamento e misurazione
dell'inquinamento acustico).

## Fonti autoritative

Catalogate in `references/sources.yaml`:

- **L. 447/1995** - PDF MASE, hash `fde4e8d55618848c73e7a4ba4f4a2fb3edfb49cb3f30802cc591e2985ef9a6ae`.
- **DPCM 14/11/1997** - HTML aggregato gazzettaufficiale.it, hash `265982c3e2970b27d6078d33e19a9ad06d91c683bb1c1ecd86758a8dc377a47c`. URL: https://www.gazzettaufficiale.it/eli/id/1997/12/01/097A9602/sg
- **DM 16/3/1998** - HTML aggregato gazzettaufficiale.it, hash `76e067861e2477d6ea782ca621bea641ca3be0a5e9bceaeaa7fc9df2865c83c4`. URL: https://www.gazzettaufficiale.it/eli/id/1998/04/01/098A2679/sg
- **L. 447/1995 (Normattiva)** - reference-only per testo vigente con coordinamento.

Estratti pertinenti in `references/estratti/`:

- `legge-447-1995-art-8.md` - art. 8 (commi 1-6), art. 4 c. 1 lett. l)
  rinvio Regioni, art. 6 c. 1 lett. d) controllo comunale, art. 2
  definizioni (incluso TCAA, da leggere alla luce del D.Lgs.
  42/2017 art. 21).
- `dpcm-14-11-1997-valori-limite.md` - art. 1-7 + Tabelle A (classi),
  B (emissione), C (immissione), D (qualita'); art. 4 differenziale,
  art. 6 attenzione.
- `dm-16-03-1998-tecniche-misurazione.md` - art. 1-2 + Allegato A
  definizioni (T_M, T_R, K_I, K_T, K_B); B norme tecniche misure;
  C rumore stradale e ferroviario; D rapporto fonometrico.

## Articoli e punti chiave

- **L. 447/1995 art. 8 c. 2**: documentazione di impatto acustico per
  opere a)-f) (aeroporti, strade A-F D.Lgs. 285/1992, discoteche,
  circoli/pubblici esercizi rumorosi, impianti sportivi, ferrovie).
- **L. 447/1995 art. 8 c. 3**: valutazione previsionale di clima
  acustico per insediamenti sensibili a)-e) (scuole/asili nido,
  ospedali, case di cura/riposo, parchi pubblici, nuove residenze
  prossime a opere c. 2).
- **L. 447/1995 art. 8 c. 4**: documentazione previsionale di impatto
  acustico a corredo di concessione edilizia / SCIA edilizia di
  impianti e infrastrutture per attivita' produttive, sportive,
  ricreative, o postazioni di servizi commerciali polifunzionali, e
  a corredo di domanda di licenza / autorizzazione all'esercizio di
  attivita' produttive.
- **L. 447/1995 art. 8 c. 6**: nulla-osta del comune se le emissioni
  previste superano i limiti di emissione di Tabella B DPCM
  14/11/1997.
- **L. 447/1995 art. 4 c. 1 lett. l)**: rinvio alla legge regionale.
- **L. 447/1995 art. 6 c. 2**: rinvio al regolamento comunale in
  materia di inquinamento acustico.
- **D.Lgs. 17/02/2017 n. 42 art. 21**: elenco nazionale TCAA
  (sostituisce il regime ex art. 2 c. 6-8 L. 447/1995).
- **DPCM 14/11/1997 Tabelle A, B, C, D** + **art. 4 differenziale**
  (5 dB diurno / 3 dB notturno, ambienti abitativi, esclusa classe
  VI e casi di trascurabilita' c. 2).
- **DM 16/3/1998 art. 2** strumentazione classe 1 + calibrazione
  +/- 0.5 dB + taratura biennale SIT; **allegato A** definizioni;
  **allegato B** norme tecniche misure; **allegato C** rumore
  stradale (T_M >= 1 settimana) e ferroviario (T_M >= 24 h);
  **allegato D** rapporto fonometrico.
- **DPR 459/1998** (rumore ferroviario) e **DPR 142/2004** (rumore
  stradale): regimi propri di fasce di pertinenza acustica;
  **rinvio strutturale**, fuori scope di questa skill.

## Convenzioni specifiche

### Cosa NON fare

- **Non quotare numericamente** valori di fascia di pertinenza,
  classi di strada o limiti specifici di DPR 459/1998 / DPR 142/2004.
  Solo rinvio strutturale.
- **Non eseguire calcoli di Leq** ne' previsionali di propagazione
  (ISO 9613-2, NMPB, ecc.).
- **Non confondere** valori limite di emissione (Tabella B, riferiti
  alla singola sorgente) con valori limite di immissione (Tabella C,
  riferiti al ricettore - sono due cose diverse, art. 2 L. 447/1995).
- **Non assumere** che il differenziale (DPCM 14/11/1997 art. 4) sia
  rispettato senza verifica esplicita: deve essere verificato o, in
  alternativa, va dichiarata l'applicabilita' di una delle condizioni
  di trascurabilita' del comma 2.
- **Non sostituire** la verifica del **testo vigente** della L.
  447/1995, del DPCM 14/11/1997 e del DM 16/3/1998 su Normattiva al
  momento del deposito.
- **Non riferire i numeri delle Tabelle B / C / D** alla classe
  sbagliata: la classe e' quella del **lotto del ricettore o della
  sorgente**, e i valori sono distinti per **periodo diurno / notturno**.
- **Non escludere il regime DPR 459/1998 / DPR 142/2004** quando una
  ferrovia o una strada A-F sono adiacenti: non si applica la Tabella
  C all'interno delle fasce di pertinenza (DPCM 14/11/1997 art. 3
  c. 2).

### Cosa fare

- **Citare sempre comma e lettera** dell'art. 8 L. 447/1995 in modo
  esplicito (es. "art. 8 c. 2 lett. e)").
- **Distinguere chiaramente** le quattro fattispecie (impatto c. 2,
  clima c. 3, previsione c. 4 a corredo titolo, nulla-osta c. 6) e
  segnalare i casi in cui si combinano.
- **Indicare classe acustica del lotto e di quelle confinanti** (per
  i criteri di accostabilita' fra classi non contigue rinvio alla
  legge regionale ai sensi dell'art. 4 c. 1 lett. l) L. 447/1995)
  e i valori delle Tabelle facendo riferimento all'estratto, non
  riproducendoli a memoria.
- **Chiudere ogni output** con i quattro rinvii formali:
  1. legge regionale (art. 4 c. 1 lett. l) L. 447/1995),
  2. regolamento comunale (art. 6 c. 2 L. 447/1995),
  3. testo vigente Normattiva,
  4. TCAA firmatario (D.Lgs. 42/2017 art. 21) + progettista per la
     parte progettuale.
- **Strumentazione di classe 1** per misure (DM 16/3/1998 art. 2 c. 1),
  calibrazione **+/- 0.5 dB** prima e dopo ogni ciclo (art. 2 c. 2),
  e taratura **biennale SIT** (art. 2 c. 3).
- **Tempi di misura coerenti** con allegato C DM 16/3/1998: T_M >=
  1 settimana per rumore stradale, T_M >= 24 h per rumore ferroviario.

## Validatori

- Nessun validatore Livello 2 di dominio identificato al momento.

## Stato attuale

- Versione: 0.1.0-alpha (cfr. `CHANGELOG.md`).
- Validazione: Livello 1 (validate.sh + adversarial review interna).
- Task files: 4 (`mappa-applicabilita-art-8.md`,
  `check-completezza-impatto-acustico.md`,
  `check-completezza-clima-acustico.md`,
  `checklist-relazione-previsionale.md`).
- Esempi: 1 conforme (`palestra-classe-iv-conforme`) + 1 problematico
  (`scuola-prossima-strada-incompleta`).
