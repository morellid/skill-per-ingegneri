# Task: qualifica-intervento

Colloca un intervento in una **categoria dell'art. 3** (a-f) applicando i criteri
distintivi. **Non sceglie** il titolo edilizio ne' redige la pratica.

## Input attesi
- Descrizione dell'intervento (opere previste; parti interessate: finiture, impianti,
  strutture, prospetti).
- Effetti su **volumetria complessiva**, **destinazione d'uso**, **sagoma/sedime**,
  **carico urbanistico**.
- Presenza di **vincoli** (D.Lgs. 42/2004) o ubicazione in **zona A** / centro storico.

## Passi
1. **Finiture/impianti senza opere maggiori** → **manutenzione ordinaria** (lett. a).
2. **Opere anche strutturali / servizi / frazionamento-accorpamento** senza modifica
   della **volumetria complessiva** e con **originaria destinazione d'uso** →
   **manutenzione straordinaria** (lett. b); rientrano anche le modifiche ai prospetti
   per agibilita'/accesso alle condizioni indicate (no immobili tutelati).
3. **Conservazione dell'organismo** nel rispetto di elementi tipologici/formali/
   strutturali (anche con mutamento d'uso compatibile) → **restauro e risanamento
   conservativo** (lett. c).
4. **Trasformazione con organismo in tutto o in parte diverso**, o **demolizione e
   ricostruzione** (con diversi sagoma/sedime, salvo vincoli/zone A dove servono stessi
   sagoma/sedime e nessun incremento di volume), o **ripristino di crollati** con
   consistenza accertabile → **ristrutturazione edilizia** (lett. d).
5. **Trasformazione del territorio non riconducibile alle categorie precedenti** →
   **nuova costruzione** (lett. e; usa il task `distingui-nuova-costruzione` per i
   sottocasi e.1-e.7).
6. **Sostituzione del tessuto urbanistico-edilizio** (lotti/isolati/rete stradale) →
   **ristrutturazione urbanistica** (lett. f).
7. Ricorda che le definizioni **prevalgono** sugli strumenti urbanistici/regolamenti
   edilizi (c. 2).

## Output
- Categoria dell'art. 3 con la **lettera** e i criteri che l'hanno determinata
  (volumetria, destinazione d'uso, sagoma/sedime, vincoli), e i limiti applicabili.
- Nota di rinvio: la **scelta del titolo** (CILA/SCIA/PdC) e' della skill
  `modulistica-edilizia-unificata`; l'istruttoria e le tolleranze/sanatorie del Salva
  Casa restano al Comune.

## Riferimenti
- `../references/fonti/dpr-380-2001-art-3.md` (art. 3, lett. a-f, c. 2)
- `../references/estratti/definizioni-interventi-checklist.md` (sez. A-G)
