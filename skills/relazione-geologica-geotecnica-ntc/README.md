# Relazione geologica e geotecnica - NTC 2018 cap. 6

> Versione: 0.1.0-alpha
> Stato: in sviluppo (alpha, validazione Livello 1)

Skill di supporto documentale per le due relazioni specialistiche richieste
dal capitolo 6 delle NTC 2018: verifica di completezza della relazione
geologica e della relazione geotecnica, controllo di coerenza tra le due (e
con la relazione di calcolo), bozza di indice commentato della relazione
geotecnica.

## Target

Ingegneri civili progettisti, geologi, collaudatori statici che devono
redigere, rivedere o esaminare relazioni geologiche e geotecniche ai sensi
di NTC 2018 e Circolare 7/2019.

## Cosa fa

- **check-relazione-geologica**: verifica i contenuti richiesti da NTC par.
  6.2.1 e Circ. C6.2.1 (modello geologico, sei aspetti, elaborati grafici,
  pericolosita' e compatibilita' geologica, ruolo del Geologo).
- **check-relazione-geotecnica**: verifica il contenuto minimo di NTC par.
  6.1.2, le dodici voci indicative di Circ. C6.2.2.5, il corredo
  documentale, i valori caratteristici e i certificati ex art. 59 DPR
  380/2001, il quadro delle verifiche SLU/SLE.
- **check-coerenza-geologica-geotecnica**: controlla la sequenza modello
  geologico -> problemi geotecnici -> indagini -> modello geotecnico, la
  coerenza stratigrafica e idrica, e la correlazione con il modello
  strutturale (Circ. C10.1).
- **draft-struttura-relazione-geotecnica**: produce un indice commentato
  modulato su tipo di opera e fase progettuale.

Per il dettaglio tecnico vedi `SKILL.md` e `tasks/`.

## Installazione

Vedi il [README di root del repo](../../README.md) per installazione e
discovery in Claude Code / Codex.

## Fonti consultate

- DM 17/01/2018 (NTC 2018), parr. 6.1-6.2.6 - GU n. 42/2018 SO n. 8
- Circolare C.S.LL.PP. 21/01/2019 n. 7, parr. C6.2-C6.2.4.3, C9.1 lett. g,
  C10.1 - GU n. 35/2019 SO n. 5

Dettaglio completo con hash SHA256 in `references/sources.yaml`;
trascrizioni delle sezioni lette in `references/fonti/`.

## Limiti noti

- Verifica documentale, non di merito: non rifa' calcoli ne' giudica
  l'adeguatezza di parametri e modelli.
- Le verifiche delle singole opere geotecniche (NTC parr. 6.3-6.11) e la
  progettazione sismica (parr. 3.2, 7.11) sono fuori scope.
- I valori dei coefficienti parziali (Tabb. 6.2.I-6.2.III) non sono coperti.
- Gli output vanno sempre sottoposti al professionista firmatario: la
  relazione geologica e' del Geologo, la geotecnica e' responsabilita' del
  Progettista (Circ. C9.1 lett. g, C10.1).

## Changelog

Vedi [CHANGELOG.md](CHANGELOG.md).
