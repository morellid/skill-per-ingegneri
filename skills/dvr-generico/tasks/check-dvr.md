# Task: Verifica completezza DVR esistente

Verifica che un DVR esistente contenga i 6 elementi obbligatori dell'art. 28 co. 2 e che soddisfi i requisiti formali (data certa, firme).

## Obiettivo

Report strutturato che indichi presenza/assenza/inadeguatezza di ciascun elemento minimo, con citazione normativa, e identificazione di gap.

## Input richiesti

- Il DVR completo (testo, PDF, scan)
- Eventualmente: l'organigramma sicurezza
- Tipologia attivita' aziendale (per individuare Titoli specifici applicabili)
- Numero lavoratori

## Fonti

Leggere prima: `references/estratti/dlgs-81-art-17-28-29.md`

## Procedura

### Passo 1 - Verifica formali

- [ ] **Data certa**: presente? (sottoscrizione, marca temporale, ecc.)
- [ ] **Firma datore di lavoro**
- [ ] **Firma RSPP**
- [ ] **Firma medico competente** (se nominato)
- [ ] **Verbale consultazione RLS** (firmato dal RLS, art. 29 co. 2)
- [ ] **Anagrafica azienda** completa
- [ ] **Custodia presso unita' produttiva** dichiarata

### Passo 2 - Verifica 6 contenuti minimi (art. 28 co. 2)

#### Lett. a) Relazione sulla valutazione di TUTTI i rischi

- [ ] Tutti i rischi identificati (cross-check con tassonomia + Titoli applicabili)
- [ ] Criteri di valutazione esplicitati
- [ ] Metodologia coerente (es. matrice P x G + livelli numerici)

Pattern problematici:
- "Rischio generico aziendale" - troppo vago
- Solo elenco di attivita' senza valutazione - manca il "calcolo"
- Esclusione di rischi che dovrebbero essere presenti (es. stress lavoro-correlato omesso, art. 28 co. 1-bis)

#### Lett. b) Misure di prevenzione/protezione + DPI

- [ ] Misure descritte per ciascun rischio significativo
- [ ] DPI elencati per categoria di rischio
- [ ] Distinzione misure preventive (riducono frequenza) vs protettive (riducono gravita')

Pattern problematici:
- "DPI conformi alla normativa" - generico
- Misure senza riferimento al rischio - boilerplate
- Solo DPI senza misure tecniche/organizzative

#### Lett. c) Programma di miglioramento

- [ ] Programma con misure future, tempi, responsabili
- [ ] Coerenza con i rischi residui non completamente mitigati

Pattern problematici:
- Programma vuoto o "vedremo prossimo anno"
- Stessi obiettivi anno dopo anno -> sospetto sito non aggiornato

#### Lett. d) Procedure di attuazione + ruoli

- [ ] Procedure operative documentate (uso DPI, emergenza, manutenzione, ecc.)
- [ ] Ruoli assegnati a soggetti con competenze + poteri
- [ ] Catena di responsabilita' chiara

#### Lett. e) Nominativi RSPP, RLS, medico competente

- [ ] Indicati nominativamente
- [ ] Date di nomina o riferimento
- [ ] RLS consultato (verbale)

#### Lett. f) Mansioni a rischio specifico

- [ ] Mansioni che richiedono formazione/addestramento riconosciuti identificate
- [ ] Verifica formazione effettuata

### Passo 3 - Verifica integrazione Titoli specifici

In base all'attivita', verificare che il DVR includa sezioni o documenti collegati per:

| Titolo | Necessario se |
|--------|---------------|
| Titolo II (luoghi) | Sempre - microclima, illuminazione, layout |
| Titolo III (attrezzature, DPI) | Sempre |
| Titolo VI (MMC) | Lavoratori movimentano carichi > 3 kg ripetitivi |
| Titolo VII (VDT) | Lavoratori VDT > 20h/sett |
| Titolo VIII Capo II (rumore) | Sempre - almeno valutazione preliminare |
| Titolo VIII Capo III (vibrazioni) | Uso attrezzi vibranti o veicoli con vibrazioni significative |
| Titolo VIII Capo IV (CEM) | Esposizioni significative |
| Titolo VIII Capo V (ottiche) | Laser, IR, UV |
| Titolo IX (chimico) | Uso/produzione sostanze chimiche pericolose |
| Titolo IX Capo II (cancerogeni/mutageni/RT) | Esposizioni a sostanze in elenco |
| Titolo X (biologico) | Sanita', laboratori, allevamento, rifiuti |
| Titolo XI (ATEX) | Atmosfere esplosive |

### Passo 4 - Verifica obblighi specifici art. 28 par. 1

- [ ] Rischio **stress lavoro-correlato** - obbligatorio (par. 1-bis), valutazione preliminare almeno
- [ ] **Lavoratrici in gravidanza** (D.Lgs. 151/2001) - sezione dedicata
- [ ] **Differenze di genere/eta'/provenienza/tipologia contrattuale** - sezione dedicata
- [ ] Per **cantieri con scavi**: rischio ordigni inesplosi (con riserva applicativa)

### Passo 5 - Output

```markdown
# Verifica completezza DVR - [azienda]

**Data verifica**: [data]
**DVR analizzato**: [versione + data del DVR]
**Settore attivita'**: [...]
**N. lavoratori**: [...]

## Esito sintetico

[CONFORME | CONFORME CON NOTE | CARENZE | NON CONFORME]

Voci complete: X/6
Voci inadeguate: Y/6
Voci assenti: Z/6
Aspetti formali (data certa, firme): [OK / Carenti]

## Verifica formali

[checklist data certa, firme, ecc.]

## Verifica 6 contenuti minimi

| Lett. | Voce | Stato | Note |
|-------|------|-------|------|
| a | Relazione valutazione rischi + criteri | ... | ... |
| b | Misure prevenzione/protezione + DPI | ... | ... |
| c | Programma miglioramento | ... | ... |
| d | Procedure + ruoli | ... | ... |
| e | Nominativi RSPP/RLS/MC + consultazione RLS | ... | ... |
| f | Mansioni a rischio specifico | ... | ... |

## Titoli specifici applicabili

| Titolo | Applicabile? | Trattato nel DVR? | Note |
|--------|--------------|-------------------|------|
| II Luoghi | SI | OK | ... |
| VI MMC | SI/NO | ... | ... |
| VIII Cap II Rumore | SI | OK | ... |
| ... | ... | ... | ... |

## Sezioni speciali

- Stress lavoro-correlato: [presente/assente, fase 1 e 2]
- Lavoratrici in gravidanza: [presente/assente]
- Differenze (genere/eta'/provenienza/contratto): [presente/assente]

## Problemi rilevati

| # | Voce/Titolo | Problema | Riferimento | Priorita' |
|---|-------------|----------|-------------|-----------|
| 1 | ... | ... | ... | ... |

## Raccomandazioni

[Lista per priorita']

## Sanzioni potenzialmente applicabili

In caso di carenze:
- Mancata redazione DVR: arresto 3-6 mesi o ammenda 2.949 - 7.532 EUR
- DVR senza lett. b/c/d: ammenda 2.847 - 5.695 EUR
- DVR senza lett. a primo periodo o f: ammenda 1.423 - 2.847 EUR

## Limiti

- Verifica documentale, non operativa
- Non sostituisce ispezione INL/ASL
- Non valuta l'effettiva applicazione delle misure dichiarate

## Rinvio al professionista

**Le carenze rilevate vanno valutate dal RSPP** in consultazione con il datore di lavoro, RLS, medico competente. La presente verifica e' di supporto, non sostituzione.
```

## Casi limite

### DVR redatto con procedure standardizzate
Verificare conformita' al modello del Coordinamento Tecnico Regioni (DM 30/11/2012). Se redatto con OIRA INAIL, generalmente conforme.

### DVR senza data certa
Carenza grave. Anche con tutti i contenuti, manca opponibilita' giuridica. Da rifare la sottoscrizione.

### DVR redatto da fornitore esterno senza coinvolgimento RLS
Carenza art. 29 co. 2. Va integrato con verbale consultazione.

### DVR datato > 5 anni senza modifiche
Sospetto: in 5 anni e' improbabile che nulla sia cambiato. Verificare se art. 29 co. 3 (rielaborazione) e' stato applicato.

## Limiti di questo task

- Verifica formale, non testa le misure in cantiere/azienda
- Non sostituisce la verifica del RSPP o ispezione autorita'

## Esempi

Vedi `examples/`:
- (Esempio condiviso con `dvr-pmi-ufficio/` - testato come stesura, applicabile anche come check)
