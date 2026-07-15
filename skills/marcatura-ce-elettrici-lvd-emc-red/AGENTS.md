# AGENTS.md - marcatura-ce-elettrici-lvd-emc-red

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale alla **marcatura CE** dei **prodotti elettrici/elettronici**
secondo le tre direttive di prodotto: **LVD 2014/35/UE** (bassa tensione), **EMC
2014/30/UE** (compatibilita' elettromagnetica) e **RED 2014/53/UE** (apparecchiature
radio). Target: fabbricanti, uffici tecnici, ingegneri elettrici/elettronici.

**E' una skill documentale**: non individua le norme armonizzate (a pagamento),
non esegue le prove, non redige materialmente la documentazione.

## Fonti autoritative

Catalogate in `references/sources.yaml` (tre direttive eur-lex, online-only:
`binary_path: null`, `sha256: null`; eur-lex non riproducibile con hash stabile,
stesso approccio della skill ai-act-compliance):

- **dir-2014-35-lvd**: art. 1, all. I, III (Modulo A), IV. Trascrizione in
  `references/fonti/dir-2014-35-lvd.md`.
- **dir-2014-30-emc**: all. I, art. 14, all. II-III. In
  `references/fonti/dir-2014-30-emc.md`.
- **dir-2014-53-red**: art. 3, 17, all. II-VII. In
  `references/fonti/dir-2014-53-red.md`.

Estratto operativo: `references/estratti/marcatura-ce-elettrici-checklist.md`.

## Punti chiave (verificati sul testo)

- **LVD**: campo 50-1000 V ca / 75-1500 V cc; unica procedura = **Modulo A**
  (controllo interno, all. III), **senza organismo notificato**.
- **EMC (art. 14)**: **Modulo A** (all. II) **o** esame UE del tipo **B** +
  conformita' al tipo **C** (all. III).
- **RED (art. 17)**: **A** / **B+C** / **H**; per l'**art. 3.1**, solo A ammesso
  **solo** applicando le norme armonizzate, altrimenti **organismo notificato**
  (B+C o H). Documentazione tecnica all. V; dichiarazione UE all. VI; semplificata
  all. VII.
- La **RED incorpora** sicurezza LVD (art. 3.1.a) ed EMC (art. 3.1.b): per le
  apparecchiature radio non si applicano separatamente LVD ed EMC.
- **Marcatura CE**: seguita dal **numero dell'organismo notificato** quando questo
  interviene in fase di produzione.

## Convenzioni specifiche

### Cosa NON fare
- Non individuare le **norme armonizzate** (EN a pagamento) ne' eseguire/interpretare
  le **prove** (EMC, sicurezza, spettro).
- Non redigere materialmente documentazione/dichiarazione: fornirne struttura.
- Non trattare altre direttive (macchine 2023/1230, ATEX 2014/34, ErP, RoHS):
  solo rinvio.

### Cosa fare
- Individuare direttiva/e applicabile/i e le loro combinazioni.
- Scegliere procedura/moduli e stabilire se serve l'organismo notificato.
- Strutturare documentazione tecnica, dichiarazione UE e marcatura CE.

## Aggiornamento delle fonti

eur-lex online-only: a ogni aggiornamento rileggere gli articoli/allegati citati
delle tre direttive (ed eventuali atti delegati, es. RED sul caricabatterie
comune).

## Validatori

- Non ancora assegnato (Livello 2 da effettuare con esperto marcatura CE
  elettrica).

## Stato attuale

- Versione: 0.1.0-alpha (closes #60)
- Task files: 2 (`individua-direttive.md`, `scegli-procedura-conformita.md`)
- Esempi: 2 (alimentatore LVD+EMC; apparecchiatura radio RED e scelta del modulo)
