# AGENTS.md - pos-allegato-xv-checker

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Verifica del Piano Operativo di Sicurezza (POS) rispetto ai contenuti minimi previsti dall'**Allegato XV del D.Lgs. 9 aprile 2008 n. 81** (Testo Unico Sicurezza sul Lavoro). Target utente: ingegneri civili, coordinatori per la sicurezza in fase di esecuzione (CSE) e in fase di progettazione (CSP), datori di lavoro di imprese esecutrici, consulenti sicurezza.

## Fonti autoritative

Tutte gia' catalogate in `references/sources.yaml` con URL + hash. Quando aggiorni:

- **D.Lgs. 81/2008 testo coordinato** (INL gennaio 2025) - hash `f593e18...`
- **D.Lgs. 81/2008 originale GU 2008** - hash `bcc0e07...` (riferimento storico)
- **Normattiva** per cross-check su singoli articoli: <https://www.normattiva.it>

Estratti pertinenti gia' preparati in `references/estratti/`:
- `allegato-xv-testo.md` - testo integrale Allegato XV punti 1, 3, 4 + Allegati XV.1 e XV.2
- `dlgs-81-art-96-97.md` - obblighi datori di lavoro imprese esecutrici e affidatarie

## Articoli e punti chiave

Quando produci output, cita SEMPRE l'articolo o il punto specifico (non "il D.Lgs. 81 dice..."):

- **Allegato XV punto 3.2.1** lett. a) - l): contenuti minimi POS (10 voci obbligatorie)
- **Allegato XV punto 4.1.1** lett. a) - g): 7 categorie costi sicurezza non soggetti a ribasso
- **Allegato XV punto 4.1.3**: metodologia stima costi (analitica, prezziario, posa+smontaggio+manutenzione)
- **D.Lgs. 81/2008 art. 96**: obblighi datori di lavoro imprese in cantiere, sanzioni penali
- **D.Lgs. 81/2008 art. 97**: obblighi impresa affidataria (coordinamento, congruenza POS, trasferimento oneri)
- **D.Lgs. 81/2008 art. 100**: PSC (per riferimento incrociato POS-PSC)

## Convenzioni specifiche

### Cosa NON fare
- Non firmare/produrre POS pronti al deposito - la skill verifica, non sostituisce CSE/datore di lavoro.
- Non valutare congruita' del POS al PSC senza il PSC stesso (skill separata, futura).
- Non interpretare "workplace emotion recognition" sotto Art. 5 AI Act qui (skill `ai-act-compliance`).
- Non usare prezziari regionali specifici - la skill verifica metodologia, non prezzi unitari.

### Cosa fare
- Per ogni problema rilevato, indicare priorita' (Critica / Alta / Media / Bassa) e riferimento normativo preciso.
- Sanzione art. 159 co. 1 D.Lgs. 81 (ammenda 2.847,69 - 5.695,36 euro per POS con elementi Allegato XV mancanti) e' il riferimento di severita'. Citarla senza quantificare l'applicazione al caso specifico (compito ispettivo).
- Casi limite: mere forniture (art. 96 co. 1-bis), POS affidataria vs esecutrice (art. 97), PSC assente, riferimenti obsoleti al D.Lgs. 163/2006 - tutti gestiti nei task files.

## Validatori

- Validatore di dominio: **Fabrizio Vitale** (RSPP, Ord. Ing. Livorno) - candidato per Livello 2 validation. Cfr. `personal/notes/notes/work/vitale-collaboration/profilo-vitale.md`.

## Stato attuale

- v0.1.0-alpha rilasciata, validata Livello 1 (`scripts/validate.sh` OK).
- 4 task files completi: `check-completezza`, `check-coerenza-rischi`, `check-costi-sicurezza`, `check-coordinamento`.
- 8 esempi (4 conformi + 4 non conformi).
- Validazione Livello 2 da pianificare (validatore esterno).
