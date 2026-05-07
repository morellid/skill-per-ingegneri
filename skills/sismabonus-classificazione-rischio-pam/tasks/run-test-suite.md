# Task: esecuzione test suite

## Obiettivo

Eseguire la test suite Python del modulo di calcolo per verificare la consistenza interna delle formule, il corretto funzionamento dei bordi delle tabelle classi PAM/IS-V, la regola del salto classi, la validazione input e l'anti-drift fixture-based.

## Quando eseguirlo

- Prima di un release (alpha -> beta -> stable).
- Dopo ogni modifica al modulo `tasks/lib/sismabonus.py`.
- Quando un validatore di dominio chiede evidenza che il modulo sia internamente consistente.
- Come pre-check prima della validazione di campo (Livello 2) vs software certificati.

## Procedura

```bash
python3 ${CLAUDE_SKILL_DIR}/tasks/lib/test_sismabonus.py
```

In Codex / altri agent: sostituire `${CLAUDE_SKILL_DIR}` con il path assoluto della skill installata.

Output atteso: tutti i test pass (1 skipped accettato solo se la fixture conforme non e' presente; in v0.1.0-alpha la fixture e' presente e il test deve passare).

## Cosa copre la test suite (consistenza interna)

- **Formula PAM**: trapezoidale a 4 termini SLID->SLO->SLD->SLV->SLC + termine di coda lambda(SLC) × CR(SLR), con verifica numerica esplicita su valori scelti (test_pam_formula_a_mano).
- **Bordi tabella classi PAM**: A+ ≤ 0.50%, A ≤ 1.0%, B ≤ 1.5%, C ≤ 2.5%, D ≤ 3.5%, E ≤ 4.5%, F ≤ 7.5%, G > 7.5% (Allegato A punto 2.3).
- **Bordi tabella classi IS-V**: A+ > 100%, A 80-100%, B 60-80%, C 45-60%, D 30-45%, E 15-30%, F < 15% (Allegato A punto 2.3).
- **Regola classe finale**: peggiore tra classe PAM e classe IS-V (Allegato A punto 2.3).
- **Regola salto classi**: differenza in graduatoria tra classe stato di fatto e classe stato di progetto, su scala A+, A, B, C, D, E, F, G (Allegato A punto 3).
- **Rilevamento curva non monotona**: TR_C non ordinati per severita' (test_pam_non_monotona_segnalata).
- **Validazione input**: rifiuta TR negativi/zero, PGA NaN/inf/string/bool, accetta PGA_C(SLV)=0 come limite (edificio "crollato").
- **CLI**: smoke test con --input-json, fatto-only e fatto+progetto, error handling friendly su chiavi mancanti, file inesistente, JSON con NaN/Infinity (RFC 8259 violato).
- **Anti-drift fixture**: confronto numerico tra output del modulo e `examples/caso-conforme-fittizio/expected.json`. Se i numeri cambiano, sia il fixture sia gli estratti normativi vanno aggiornati di conserva.

## Cosa NON copre la test suite

- **Confronto numerico vs software certificati** (ClaSS S.I.S., CDM Win STS, EdiSis Newsoft, MasterSap-SismiClass AMV) su edifici reali. Questa e' la **validazione di campo (Livello 2)**, prerequisito del release stabile, da eseguire seguendo il piano sotto.
- **Verifica manuale dell'analisi di vulnerabilita'**: la skill prende TR_C e PGA_C in input, non li ricalcola. La correttezza dell'analisi e' responsabilita' del progettista strutturale.
- **Implementazione del metodo semplificato per muratura**: fuori scope v0.1.0-alpha.

## Piano validazione di campo (Livello 2)

Prima del release stabile (v1.0.0):

1. Reperire 10+ edifici reali con classificazione gia' eseguita da software certificato (ClaSS, CDM Win, EdiSis o MasterSap-SismiClass), idealmente:
   - 4 in c.a., 3 in muratura, 2 in acciaio, 1 misto
   - Mix di zone sismiche italiane (Z1, Z2, Z3, Z4)
   - Mix di livelli di conoscenza (LC1, LC2, LC3) con fattori di confidenza diversi
   - Almeno 2 casi con stato di fatto + stato di progetto (per validare salto classi)
2. Per ciascun edificio, estrarre TR_C, PGA_C, PGA_D dal report del software certificato e costruire il file JSON di input.
3. Eseguire `sismabonus.py --input-json` e confrontare PAM, IS-V, classe PAM, classe IS-V, classe finale, salto classi.
4. Tolleranze accettabili (per software diversi possono esserci piccole differenze di trapezoidale/capping/arrotondamento):
   - PAM: |delta| ≤ 0.05% in valore assoluto
   - IS-V: |delta| ≤ 0.5% in valore assoluto
   - Classe: identica, OPPURE diversa solo se entrambe le classi sono adiacenti e il valore e' al bordo (entro 0.05% per PAM, 1% per IS-V).
5. Documentare ogni discrepanza in `examples/caso-validazione-livello-2/` con input, output del modulo, output del software certificato e analisi della differenza.
6. Se le discrepanze sono spiegabili (capping diverso, arrotondamento, differenze di interpolazione lambda): aggiornare la documentazione del modulo per spiegare la convenzione adottata.
7. Se le discrepanze NON sono spiegabili: bug. Aprire issue, sospendere il release stabile finche' non risolto.

Solo al completamento del Livello 2 con esito positivo su 10+ casi la skill puo' uscire dallo stato 0.x e diventare 1.0.0 stabile.
