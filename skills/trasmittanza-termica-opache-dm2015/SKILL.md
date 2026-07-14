---
name: trasmittanza-termica-opache-dm2015
description: "Calcolo code-driven della trasmittanza termica U di strutture opache stratificate (pareti verticali, coperture, pavimenti) e verifica rispetto ai valori limite per zona climatica del DM 26/06/2015 (requisiti minimi di prestazione energetica). Il metodo U = 1/R_tot (legge di Fourier) e' fisica tecnica di pubblico dominio; i valori limite di U provengono dal DM 26/06/2015 Appendice B (edifici esistenti sottoposti a riqualificazione energetica, contesto Ecobonus) e Appendice A (edificio di riferimento). La conducibilita' lambda dei materiali e le resistenze superficiali R_si/R_se sono input dell'utente (da schede tecniche e UNI EN ISO 6946): la skill non li stima ne' riproduce le norme UNI a pagamento. Gestisce l'incremento +30% dei limiti per isolamento dall'interno o in intercapedine e avverte che il limite del DM include i ponti termici mentre il calcolo 1D no. Use when an Italian engineer needs to compute the U-value of an opaque building element from its layers and check it against the DM 26/06/2015 climatic-zone limits; it does not replace the signed technical report."
license: MIT
area: energia-incentivi
title: "Trasmittanza U strutture opache - verifica DM 26/06/2015"
summary: "Calcolo code-driven della trasmittanza U di strutture opache stratificate (U = 1/R_tot) e verifica dei limiti per zona climatica del DM 26/06/2015 (App. B riqualificazione / App. A edificio di riferimento), con +30% per isolamento interno; lambda e R_si/R_se input utente"
normative_refs:
  - "DM 26/06/2015 (MiSE, requisiti minimi) Allegato 1 par. 5.2 + Appendici A e B"
version: 0.1.0-alpha
status: alpha
tags:
  - efficienza-energetica
  - trasmittanza
  - dm-requisiti-minimi
  - ecobonus
  - code-driven
---

# Trasmittanza U strutture opache - verifica DM 26/06/2015

## Quando usare questa skill

Usala quando devi calcolare la trasmittanza termica U di una struttura opaca
stratificata (parete verticale, copertura, pavimento) a partire dai suoi strati
e verificarla rispetto ai valori limite per zona climatica del **DM 26/06/2015**
(requisiti minimi di prestazione energetica), tipicamente in contesto APE /
Ecobonus / ristrutturazione.

Target: ingegneri, architetti, termotecnici, certificatori energetici.

## Avvertenza

Questa skill calcola la trasmittanza in **regime monodimensionale** dai dati
forniti dall'utente e la confronta con i limiti del decreto. **Non sostituisce
la relazione tecnica di progetto** ex art. 8 D.Lgs. 192/2005 firmata dal
progettista. In particolare:

- il valore limite del DM **include l'effetto dei ponti termici**; la U 1D
  calcolata qui **non** li include: la verifica e' **preliminare** (la verifica
  completa richiede il calcolo dei ponti termici, UNI EN ISO 14683/10211);
- la **conducibilita' lambda** dei materiali e le **resistenze superficiali**
  R_si/R_se sono **input dell'utente** (schede tecniche, UNI EN ISO 6946): la
  skill non li stima e non riproduce le norme UNI a pagamento.

## Sotto-attivita' disponibili

- **Calcola e verifica la trasmittanza**: l'utente fornisce la stratigrafia, le
  resistenze superficiali, la zona climatica e il regime ->
  `tasks/calcola-trasmittanza.md`

## Processo generale

1. Raccogli la stratigrafia (spessore e lambda per strato), R_si/R_se, la zona
   climatica, il tipo di struttura, il regime (riqualificazione / edificio di
   riferimento) e l'anno del limite.
2. Esegui **sempre** il modulo `tasks/lib/trasmittanza.py` (non calcolare a
   mano).
3. Presenta U, il limite applicato con la citazione della tabella del DM e
   l'esito U <= limite.
4. Riporta integralmente le avvertenze (ponti termici, dati utente, fattori di
   correzione) e chiudi con il rinvio al progettista firmatario.

## Calcolo deterministico

```bash
python3 tasks/lib/trasmittanza.py \
  --strato "intonaco_int:0.015:0.70" --strato "muratura:0.25:0.40" \
  --strato "eps:0.12:0.036" --strato "intonaco_est:0.015:0.90" \
  --rsi 0.13 --rse 0.04 --zona E --regime riqualificazione --anno 2021
# -> U = 0,240 W/(m2K); limite zona E (App. B, 2021) = 0,28; verifica: si
```

Modulo `tasks/lib/trasmittanza.py` con 19 test (`tasks/lib/test_trasmittanza.py`).

## Fonti normative

Riferimenti completi in `references/sources.yaml`. Trascrizione verificata in
`references/fonti/dm-26-06-2015-requisiti-minimi.md`, estratto operativo con le
tabelle in `references/estratti/dm-2015-limiti-trasmittanza.md`.

- **DM 26/06/2015** (MiSE, "requisiti minimi"), GU n. 162/2015 S.O. 39 -
  Allegato 1 par. 5.2, Appendice A (edificio di riferimento) e Appendice B
  (edifici esistenti in riqualificazione), Tabelle 1-4.

## Limiti

Cosa questa skill NON fa:
- non fornisce i lambda dei materiali (input utente) ne' le R_si/R_se (UNI EN
  ISO 6946): non riproduce le norme UNI a pagamento;
- non calcola i ponti termici, l'H'T, l'indice di prestazione energetica
  globale, l'APE;
- non calcola la trasmittanza dei serramenti (Uw: UNI EN ISO 10077, dato del
  produttore) ne' la trasmittanza termica periodica YIE / l'inerzia;
- non verifica condensa interstiziale/superficiale (Glaser, UNI EN ISO 13788);
- non applica i fattori di correzione per ambienti non climatizzati (UNI/TS
  11300-1) ne' la trasmittanza equivalente controterra (UNI EN ISO 13370):
  segnala solo quando servono.
