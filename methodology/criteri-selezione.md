# Criteri di selezione delle skill

Come decidere se un task vale una skill, e quale skill costruire per prima.

## Priorita' alta - costruire

Un task e' buon candidato se soddisfa la maggioranza di questi criteri:

1. **Ripetibilita'**: il task si ripete con struttura simile tra pratiche diverse. Esempi: verifica POS, redazione relazione geologica, calcolo costi sicurezza.
2. **Volume**: molti ingegneri lo svolgono, molte volte all'anno. Filtro: stimativamente 100+ pratiche/anno aggregate nel territorio nazionale.
3. **Normativa stabile e pubblica**: il riferimento normativo e' chiaro, cambia lentamente, documenti consultabili gratuitamente (Gazzetta Ufficiale, GU regionali).
4. **Verifica oggettiva**: l'output puo' essere confrontato contro una checklist o un testo normativo, non richiede giudizio soggettivo.
5. **Rischio contenuto**: un errore della skill viene intercettato dalla revisione del professionista prima di produrre danno.

## Priorita' bassa - rimandare

Un task NON e' buon candidato oggi se:

- Richiede giudizio professionale difficile da codificare (es. valutazione estetica, scelta architettonica)
- La normativa cambia rapidamente o e' ambigua (es. norme transitorie in evoluzione)
- Le fonti sono a pagamento e non distribuibili (es. norme UNI non pubbliche) **senza** che la skill possa comunque lavorare via riferimenti strutturali
- L'output ha impatto diretto su sicurezza pubblica senza revisione (es. calcoli strutturali consegnati direttamente)
- Il dominio richiede dati proprietari o riservati dell'Ordine/PA

## Anti-criteri (skip assoluto)

Mai costruire skill che:

- **Auto-firmino documenti** senza revisione umana
- **Generino calcoli strutturali** o dimensionamenti critici senza gating
- **Accedano a dati personali di terzi** senza consenso
- **Sostituiscano obblighi di firma digitale del professionista**
- **Vengano presentate come "certificate" o "valide"** - le skill sono supporti, non certificazioni

## Coda prioritizzata attuale

Aggiornare questa sezione a ogni nuova proposta.

| Pos. | Skill | Dominio | Motivazione | Stato |
|------|-------|---------|-------------|-------|
| 1 | pos-allegato-xv-checker | Sicurezza cantieri | Alta ripetibilita', normativa stabile (D.Lgs. 81/2008 Allegato XV), volume nazionale elevato | In sviluppo |
| 2 | TBD | TBD | Da proporre al laboratorio del 10 maggio 2026 | Da validare |

## Processo di decisione

1. Proposta in issue su GitHub con breve descrizione + check contro i criteri sopra
2. Discussione aperta almeno 7 giorni
3. Decisione: costruire / rimandare / scartare
4. Se "costruire": scaffold con `scripts/new-skill.sh` e segue [`generazione-skill.md`](generazione-skill.md)
