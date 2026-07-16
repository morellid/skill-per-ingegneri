# valutazione-cem-elettrodotti-dpcm2003

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con tecnico ARPA/esperto CEM da completare)

Skill di **supporto alla verifica dei limiti** di esposizione della popolazione ai
**campi elettrici e magnetici a frequenza di rete (50 Hz)** generati dagli
**elettrodotti**, ai sensi del **D.P.C.M. 8 luglio 2003** (attuazione della legge quadro
36/2001).

**Non e' una skill di calcolo**: inquadra la grandezza applicabile (limite/attenzione/
qualita') e il quadro delle fasce di rispetto; **non misura** il campo e **non calcola**
la Distanza di Prima Approssimazione (DPA).

## Target

Ingegneri e tecnici che devono verificare la compatibilita' di un edificio/area con i
limiti CEM a 50 Hz di un elettrodotto, o impostare una valutazione delle fasce di
rispetto.

## Cosa fa

| Sotto-attivita' | Descrizione |
|---|---|
| `inquadra-limite-applicabile` | Dato sito e uso (esistente/nuovo, tipo area, permanenza), individua quale grandezza si applica e il valore (100 µT/5 kV/m; 10 µT; 3 µT) |
| `imposta-verifica-fasce` | Struttura la richiesta dati al gestore (portata CEI 11-60, geometria) e imposta la verifica rispetto all'obiettivo di qualita', rinviando al DM 29/5/2008 per la DPA |

Nucleo: **limite di esposizione** 100 µT / 5 kV/m (art. 3 c.1), **valore di attenzione**
10 µT mediana 24 h (art. 3 c.2), **obiettivo di qualita'** 3 µT (art. 4), **tecniche di
misura** CEI 211-6 (art. 5), **fasce di rispetto** (art. 6), **definizioni** (Allegato A).

## Fonti consultate

- **D.P.C.M. 8 luglio 2003** (elettrodotti 50 Hz), artt. 1-8 e Allegato A - testo in
  Gazzetta Ufficiale (riferimento solo-online, ELI permalink)
- **Legge 36/2001** (legge quadro) - fonte primaria delegante
- **DM Ambiente 29/5/2008** (metodologia fasce/DPA) - **citato, non riprodotto**

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non calcola la DPA** ne' l'ampiezza delle fasce: la metodologia e' nel **DM
  29/5/2008** (delegato dall'art. 6 c.2), non reperibile in questo ambiente.
- **Non esegue misure**: la determinazione dei livelli spetta ad **ARPA/tecnici** (CEI
  211-6).
- Non copre le **alte frequenze** (SRB/RF -> `valutazione-cem-srb-art-87-cce`) ne'
  l'**esposizione professionale** (D.Lgs 81/2008).

**La skill e' un supporto documentale: non sostituisce ARPA, il tecnico misuratore ne'
il calcolo delle fasce secondo il DM 29/5/2008.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
