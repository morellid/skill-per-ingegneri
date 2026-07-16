# AGENTS.md - valutazione-cem-elettrodotti-dpcm2003

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto alla **verifica dei limiti** di esposizione della popolazione ai **campi
elettrici e magnetici a 50 Hz** generati dagli **elettrodotti**, ai sensi del
**D.P.C.M. 8 luglio 2003** (attuazione della legge quadro 36/2001).

**E' una skill documentale/di consultazione**: inquadra la grandezza applicabile
(limite/attenzione/qualita') e il quadro delle fasce di rispetto; **non misura** il
campo e **non calcola** la DPA (delegata al DM 29/5/2008).

## Area di catalogo

`ambiente-territorio-mobilita`, coerente con la skill affine `valutazione-cem-srb-art-87-cce`
(CEM ad alta frequenza / SRB). Questa skill copre invece la **bassa frequenza (50 Hz)**
degli elettrodotti: le due non si sovrappongono.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dpcm-8-7-2003**: D.P.C.M. 8/7/2003, pagina ELI di Gazzetta Ufficiale (riferimento
  solo-online, `sha256: null`, `binary_path: null`, come altre voci `/eli/id/.../sg`
  del repo). Artt. 1-8 e Allegato A letti via `caricaArticolo` (codice 03A09749) e
  trascritti verbatim in `references/fonti/dpcm-8-7-2003.md`.

Estratto operativo: `references/estratti/limiti-cem-checklist.md`.

## Punti chiave (verificati sul testo)

- **Campo di applicazione** (art. 1): 50 Hz, popolazione; esclusa l'esposizione
  professionale (c.2).
- **Limite di esposizione** (art. 3 c.1): **100 µT** (induzione magnetica), **5 kV/m**
  (campo elettrico), valori efficaci.
- **Valore di attenzione** (art. 3 c.2): **10 µT**, mediana 24 h, in aree gioco,
  ambienti abitativi/scolastici, luoghi con permanenza >= 4 h.
- **Obiettivo di qualita'** (art. 4): **3 µT**, mediana 24 h, per nuovi elettrodotti/
  nuove aree presso linee esistenti.
- **Misura** (art. 5): norma **CEI 211-6**; procedure **APAT-ARPA**.
- **Fasce di rispetto** (art. 6): riferimento a obiettivo di qualita' (3 µT) e portata
  in corrente (**CEI 11-60**); dati dal gestore (Ministero per > 150 kV, Regioni per
  <= 150 kV); **metodologia DPA delegata all'APAT** (DM 29/5/2008).
- **Definizioni** (Allegato A): elettrodotto = linee + sottostazioni + cabine.

## LIMITE DI FONTE (importante)

La **metodologia di calcolo** delle fasce di rispetto e delle **DPA** (art. 6 c.2) e'
approvata con **DM Ambiente 29/5/2008**, **non trascritto** (codice GU non risolto in
questo ambiente al 2026-07-16). Gli **importi/formule** della DPA NON sono riprodotti:
la skill copre il **quadro e la verifica dei limiti**, non il calcolo numerico. Se in
futuro il DM 29/5/2008 diventa reperibile su host in allowlist, si potra' aggiungere il
modulo di calcolo delle fasce.

## Convenzioni specifiche

### Cosa NON fare
- Non **inventare** l'ampiezza delle fasce / valori di DPA (sono nel DM 29/5/2008, non
  letto).
- Non fornire **esiti di misura**: la determinazione spetta ad ARPA (CEI 211-6).
- Non trattare le **alte frequenze** (SRB/RF -> `valutazione-cem-srb-art-87-cce`) ne'
  l'**esposizione professionale** (D.Lgs 81/2008 Titolo VIII).

### Cosa fare
- Inquadrare la **grandezza applicabile** (limite/attenzione/qualita') e il valore.
- Impostare la **richiesta dati** al gestore e la **verifica delle fasce**, rinviando
  al DM 29/5/2008 per il calcolo.

## Aggiornamento delle fonti

GU: verificare eventuali modifiche del DPCM 8/7/2003 e la reperibilita' del DM 29/5/2008
(metodologia fasce/DPA) per aggiungere il calcolo. Rileggere via caricaArticolo.

## Validatori

- Non ancora assegnato (Livello 2 con tecnico ARPA / esperto CEM).

## Stato attuale

- Versione: 0.1.0-alpha (closes #61)
- Task files: 2 (`inquadra-limite-applicabile.md`, `imposta-verifica-fasce.md`)
- Esempi: 2 (nuova scuola presso linea 220 kV; abitazione esistente presso linea 132 kV)
