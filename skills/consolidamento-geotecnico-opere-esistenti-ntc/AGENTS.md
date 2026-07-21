# AGENTS.md - consolidamento-geotecnico-opere-esistenti-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **progettista geotecnico e strutturale** per l'**inquadramento della progettazione degli
interventi di consolidamento geotecnico di opere esistenti** (sottofondazioni, rinforzo delle fondazioni,
miglioramento del terreno di fondazione) secondo le **NTC 2018** (DM 17 gennaio 2018), **paragrafo 6.10**:
criteri generali, indagini, tipi di consolidamento, controlli e monitoraggio. Target: ingegneri geotecnici e
strutturisti.

**E' una skill documentale per il tecnico**: fornisce l'individuazione delle cause, il principio del progetto
unitario geotecnico-strutturale, i sei tipi di consolidamento e la regola del controllo obbligatorio; **non
calcola** ne' **dimensiona** gli interventi, **non definisce** il modello geotecnico e **non progetta** il
risanamento strutturale.

## Nota sull'area e sulla complementarita'

Area **strutture-geotecnica**. **Complementa** `costruzioni-esistenti-ntc-cap8` (classificazione strutturale
dell'esistente: LC/FC, adeguamento/miglioramento/riparazione - Cap. 8) e `relazione-geologica-geotecnica-ntc`
(che esclude i §6.3-6.12). E' **distinta** da queste: il §6.10 e' il **consolidamento geotecnico** del sistema
fondazione-terreno di un'opera esistente. Condivide con le altre skill NTC la stessa fonte (PDF GU del S.O. n. 8
alla G.U. n. 42/2018). Restano fuori scope il miglioramento/rinforzo dei terreni in generale (§6.9) e la
progettazione sismica (Cap. 7).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **ntc2018-par-6-10**: PDF del Supplemento Ordinario n. 8 alla G.U. n. 42 del 20 febbraio 2018 (DM 17 gennaio
  2018, NTC 2018), SHA256 `dda1e397...` (doppio download riproducibile, stessa fonte delle altre skill NTC).
  Par. 6.10 estratto con `pdftotext -layout` (pp. GU 203-204) e trascritto verbatim.

Trascrizione in `references/fonti/ntc2018-par-6-10.md`; estratto operativo in
`references/estratti/consolidamento-geotecnico-checklist.md`.

## Punti chiave (verificati sul testo)

- **Ambito** (§6.10): provvedimenti sul sistema manufatto-terreno per eliminare o mitigare difetti di
  comportamento di un'opera esistente.
- **Criteri generali** (§6.10.1): individuazione delle **cause** (sovrastruttura, fondazioni, terreno); progetto
  sviluppato **unitariamente con quello strutturale**; modalita' esecutive e opere provvisionali parte
  integrante; metodo osservazionale se la complessita' e' documentata.
- **Indagini** (§6.10.2): su terreno e fondazioni esistenti, dalla documentazione disponibile; cautele per
  manufatti sensibili; misura dei caratteri cinematici, delle pressioni interstiziali e degli spostamenti nel
  volume significativo, protratte per fenomeni stagionali.
- **Tipi di consolidamento** (§6.10.3): sei metodi (miglioramento/rinforzo dei terreni; miglioramento/rinforzo
  dei materiali della fondazione; ampliamento della base se superficiale; trasferimento del carico a strati piu'
  profondi; sostegni laterali; rettifica degli spostamenti del piano di posa). **Particolari cautele** per
  interventi con variazioni di volume (congelamento, iniezioni, gettiniezione).
- **Controlli/monitoraggio** (§6.10.4): controllo dell'efficacia **obbligatorio** quando l'intervento comporta
  una **ridistribuzione delle sollecitazioni al contatto terreno-manufatto**; monitoraggio previsto in progetto;
  esiti come elemento di collaudo.

## Convenzioni specifiche

### Cosa NON fare
- Non **calcolare** ne' **dimensionare** gli interventi di consolidamento; non **definire** il modello
  geotecnico ne' **progettare** il risanamento strutturale.
- Non **trattare** il miglioramento/rinforzo dei terreni in generale (§6.9), la classificazione sismica
  dell'esistente (Cap. 8) ne' la progettazione sismica (Cap. 7).

### Cosa fare
- Fornire l'individuazione delle cause, il principio del progetto unitario, i sei tipi di consolidamento e la
  regola del controllo obbligatorio, sempre con rinvio al paragrafo NTC.

## Aggiornamento delle fonti

NTC: se il PDF GU cambia (nuova edizione/errata) riscaricare, ricalcolare l'hash con doppio download e
riestrarre/ritrascrivere il par. 6.10. Verificare i sei tipi di consolidamento (§6.10.3) e la regola del
controllo obbligatorio (§6.10.4).

## Validatori

- Non ancora assegnato (Livello 2 con ingegnere geotecnico/strutturista).

## Stato attuale

- Versione: 0.1.0-alpha (closes #417)
- Task files: 2 (`inquadra-criteri-tipi-consolidamento.md`, `inquadra-indagini-controlli-consolidamento.md`)
- Esempi: 2 (i sei tipi di consolidamento e le cautele; obbligo di controllo e progetto unitario
  geotecnico-strutturale)
