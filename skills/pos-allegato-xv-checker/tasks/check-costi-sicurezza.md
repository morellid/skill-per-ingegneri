# Task: Verifica costi sicurezza non soggetti a ribasso

> **Stato**: scaffold. Contenuto normativo da popolare in sessione dedicata con Allegato XV punto 4 alla mano.

## Obiettivo

Verificare il computo dei costi per la sicurezza indicati nel POS, controllando:
- Presenza delle voci obbligatorie per tipologia di cantiere
- Correttezza metodologica del computo (non a corpo generico, analitico per voce)
- Coerenza con l'entita' dell'opera

## Input richiesti

- Sezione del POS relativa ai costi della sicurezza
- Idealmente: computo metrico estimativo dei costi sicurezza
- Contesto: importo complessivo dei lavori, tipologia cantiere

## Fonti

Riferimento normativo primario:
- Allegato XV punto 4 - "Stima dei costi della sicurezza"
- Codice Appalti (D.Lgs. 36/2023) per gli aspetti di non-ribasso
- Linee guida ANAC sui costi della sicurezza (dove applicabili)

## Procedura

**[Da completare con metodologia validata.]**

Struttura attesa:

1. Identificazione della sezione costi nel documento
2. Classificazione delle voci secondo le categorie dell'Allegato XV punto 4.1:
   - Apprestamenti (opere provvisionali, ponteggi, DPC)
   - DPI specifici per rischi particolari (non i DPI ordinari)
   - Impianti elettrici di cantiere (quando richiesti dal PSC)
   - Mezzi e servizi di protezione collettiva
   - Procedure specifiche (es. coordinamento interferenze)
   - Misure di coordinamento attivo
3. Verifica:
   - Ogni voce ha importo specifico (non "a corpo indistinto")?
   - Il totale e' congruo con il tipo/entita' di opera?
   - Sono distinti i costi sicurezza da quelli generali non soggetti a ribasso?
4. Flag su incongruenze

## Output atteso

```markdown
## Verifica costi sicurezza

### Sintesi
- Totale costi sicurezza dichiarati: EUR XXX
- Percentuale su importo lavori: Y%
- Classificazione per categoria Allegato XV punto 4.1: ...

### Verifiche per categoria
| Categoria | Voci trovate | Importo | Note |
|-----------|-------------|---------|------|
| Apprestamenti | N | EUR X | Esempi: ponteggi, trabattelli |
| DPI specifici | ... | ... | ... |
| ...

### Problemi rilevati
- Voce X generica senza dettaglio analitico
- Percentuale anomala rispetto a benchmark (qualitativo)
- ...

### Raccomandazioni
- ...

Rinvio obbligatorio: "La congruita' dei costi della sicurezza rispetto al cantiere specifico e' valutata dal CSP in fase di progettazione e verificata dal CSE. La presente verifica non sostituisce tale valutazione."
```

## Limiti di questo task

- Non dispone di prezziari regionali aggiornati per verifiche parametriche puntuali
- Non conosce il cantiere fisico, quindi non puo' giudicare congruita' assoluta
- Verifica formale della struttura del computo, non di prezzi unitari

## Placeholder - da completare

- [ ] Struttura tipica dei computi costi sicurezza (template)
- [ ] Range percentuali di riferimento per tipologie di lavoro (edilizia civile, OOPP, ristrutturazioni)
- [ ] Keyword per riconoscimento automatico voci
- [ ] Criteri per identificare voci "a corpo" problematiche
- [ ] Riferimenti a prezziari standard (Tipologie di riferimento, non valori)
