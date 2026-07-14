# trasmittanza-termica-opache-dm2015

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con termotecnico da completare)

Skill code-driven per il **calcolo della trasmittanza termica U** di strutture
opache stratificate e la **verifica dei limiti per zona climatica del DM
26/06/2015** (requisiti minimi di prestazione energetica), in contesto APE /
Ecobonus / ristrutturazione.

- Il **metodo** U = 1/R_tot (legge di Fourier) e' fisica tecnica di pubblico
  dominio.
- I **valori limite** di U vengono dal DM 26/06/2015: Appendice B (edifici
  esistenti in riqualificazione) e Appendice A (edificio di riferimento).
- La **conducibilita' lambda** dei materiali e le **resistenze superficiali**
  R_si/R_se sono **input dell'utente** (schede tecniche, UNI EN ISO 6946): la
  skill non li stima e non riproduce le norme UNI a pagamento.

## Target

Ingegneri, architetti, termotecnici, certificatori energetici.

## Cosa fa

| Sotto-attivita' | Descrizione |
|---|---|
| `calcola-trasmittanza` | Data la stratigrafia (spessore + lambda per strato), R_si/R_se, zona climatica, tipo (parete/copertura/pavimento), regime (riqualificazione App. B / edificio di riferimento App. A) e anno: calcola U = 1/R_tot, applica l'eventuale +30% per isolamento interno, confronta con il limite DM per zona climatica ed espone l'esito e le avvertenze |

Calcolo deterministico con `tasks/lib/trasmittanza.py` (19 test):

```bash
python3 tasks/lib/trasmittanza.py \
  --strato "intonaco_int:0.015:0.70" --strato "muratura:0.25:0.40" \
  --strato "eps:0.12:0.031" --strato "rasante:0.010:0.90" \
  --rsi 0.13 --rse 0.04 --zona E --regime riqualificazione --anno 2021
# -> U = 0,213 W/(m2K); limite zona E (App. B, 2021) = 0,28; verifica: si
```

## Fonti consultate

- **DM 26/06/2015** (MiSE, "requisiti minimi"), GU n. 162 del 15/07/2015 S.O. 39
  (codice 15A05198) - Allegato 1 par. 5.2, Appendici A e B (Tabelle 1-4)

Dettaglio (URL, SHA256, trascrizione) in `references/sources.yaml`,
`references/fonti/`, `references/estratti/`.

## Limiti noti

- Verifica **1D**: il limite del DM include i ponti termici, il calcolo qui no
  -> verifica **preliminare** (completa: UNI EN ISO 14683/10211)
- Non fornisce i lambda dei materiali (input utente) ne' le R_si/R_se
- Non calcola serramenti (Uw), condensa (Glaser), trasmittanza periodica YIE,
  H'T, indice di prestazione globale, APE
- Non applica i fattori di correzione per ambienti non climatizzati (UNI/TS
  11300-1) ne' la trasmittanza equivalente controterra (UNI EN ISO 13370):
  li segnala soltanto

**La skill non sostituisce la relazione tecnica di progetto ex art. 8 D.Lgs.
192/2005 firmata dal progettista.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
