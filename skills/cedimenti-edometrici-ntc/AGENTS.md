# AGENTS.md - cedimenti-edometrici-ntc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Calcolo code-driven del **cedimento di consolidazione primaria** (compressione monodimensionale, per strati/sublayer) e **verifica documentale** delle verifiche SLE sui cedimenti. Quadro normativo: NTC 2018 § 6.2.4.3 (Ed <= Cd [6.2.7]) + Circ. 7/2019 C6.2. Formulazione di calcolo: **FHWA NHI-06-088 par. 7.5.2**, usata come "altro codice internazionale" ai sensi del **cap. 12 NTC 2018**. Target: ingegneri geotecnici e strutturisti in fase preliminare.

## Fonti autoritative

Catalogate in `references/sources.yaml`:

- **ntc2018-dm-17-01-2018**: NTC 2018 (hash reale) - trascrizioni § 6.2.4.3 + cap. 12 in `references/fonti/ntc2018-dm-17-01-2018.md`
- **circ-7-2019-mit**: Circ. 7/2019 (hash reale) - `references/fonti/circ-7-2019-mit.md`
- **fhwa-nhi-06-088**: FHWA NHI-06-088 (U.S. DOT 2006, pubblico dominio, "No restrictions", hash riproducibile) - trascrizioni parr. 7.5.2 e 5.4.6.1 in `references/fonti/fhwa-nhi-06-088.md`

Estratti: `fhwa-consolidazione-primaria.md` (equazioni e limiti), `ntc2018-par-6-2.md`, `circ-7-2019-c-6-2.md`.

## Punti chiave (verificati sul testo)

- **OCR = pc/po** (FHWA 7.5.2): = 1 NC; > 1 OC; < 1 sottoconsolidato (condizione reale: consolidazione ancora in corso; se ignorata il cedimento totale e' sottostimato - 7.5.2.3)
- **Eq. [7-2]** NC: Sc = somma( Cc/(1+e0) * H0 * log10(pf/p0) )
- **Eq. [7-4]** OC, valida per **pf > pc**: termine Cr (ricompressione pc/p0) + termine Cc (vergine pf/pc)
- **Eq. [7-6]** UC: entrambi i termini su Cc (consolidazione in corso p0/pc + incremento pf/p0)
- **Sublayer** con tensioni al centro, spessori tipici 1,5-3 m; S totale = somma dei contributi (7.5.2.2)
- **Correlazioni Cc** (Table 5-5): variabilita' fino a un fattore 5, "should not be used for final design" (5.4.6.1)
- **Cap. 12 NTC**: "altri codici internazionali" ammessi per quanto non trattato dalla norma; responsabilita' del progettista sui livelli di sicurezza

## Convenzioni specifiche

### Cosa NON fare

- **Non calcolare numeri "a mano"**: l'unica fonte legittima dei numeri e' lo stdout di `tasks/lib/cedimento_edometrico.py`.
- **Non attribuire la formulazione alle NTC**: le NTC non contengono la formula; citarla sempre come FHWA NHI-06-088 par. 7.5.2, usata ex cap. 12 NTC 2018.
- **Non calcolare il caso OC con sigma_f <= sigma_p**: le eq. 7-4/7-5 trascritte valgono per pf > pc; riportare il rifiuto del modulo, non inventare il ramo di sola ricompressione.
- **Non aggirare il rifiuto su OCR < 1**: l'eq. [7-6] si applica solo dietro dichiarazione esplicita (`--sottoconsolidato`) di sottoconsolidazione reale, giustificata dal progettista.
- **Non inventare i parametri edometrici** (Cc, Cr, e0, sigma_p'): vengono dalla relazione geotecnica / prove edometriche; le correlazioni Table 5-5 servono solo da sanity check ("should not be used for final design").
- **Non confondere sigma_p' (preconsolidazione) con sigma_f' (= sigma_0' + delta_sigma')**.
- **Non calcolare** delta_sigma' (diffusione tensioni), sigma_p' dalla curva (Table 7-6a), tempi di consolidazione (7.5.3), compressione secondaria (7.5.4), cedimenti differenziali.

### Cosa fare

- **Eseguire sempre il modulo** e riportare integralmente le sue avvertenze.
- **Citare per ogni strato l'equazione FHWA applicata** ([7-2]/[7-4]/[7-6], par. 7.5.2) e l'aggancio normativo (cap. 12 + § 6.2.4.3, confronto con Cd del progetto).
- **Mostrare la struttura completa**: input per strato, OCR, caso, contributi dei termini, S in m e mm, epsilon media.
- Per la verifica documentale usare `tasks/check-verifica-cedimenti.md`.
- **Concludere con il rinvio al progettista firmatario** (il confronto col cedimento ammissibile Cd resta a suo carico).

## Validatori

- (Da identificare) Validatore Livello 2: ingegnere geotecnico, confronto vs casi pubblicati o software geotecnico certificato su casi con copertura NC/OC/UC.

## Stato attuale

- Versione: 0.2.0 (reintroduzione del calcolatore su fonte pubblica FHWA - closes #32; vedi `CHANGELOG.md`)
- Task files: `tasks/calcola-cedimento-edometrico.md` (+ modulo `tasks/lib/cedimento_edometrico.py`, 15 test verdi) e `tasks/check-verifica-cedimenti.md` (verifica documentale)
- Esempi: 1 conforme (OC con transizione, 110,1 mm) + 1 problematico (OCR < 1 rifiutato di default)
