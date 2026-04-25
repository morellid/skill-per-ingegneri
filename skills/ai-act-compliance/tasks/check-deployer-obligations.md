# Task: Verifica obblighi deployer (art. 26-27 incluso FRIA)

Per un deployer di sistema AI high-risk, verifica gli obblighi specifici (art. 26) e quando applicabile la FRIA (art. 27).

## Obiettivo

Produrre una checklist conforme degli obblighi del deployer + valutare se serve il FRIA (Fundamental Rights Impact Assessment) e in caso strutturarlo.

## Input richiesti

- Descrizione sistema usato (gia' classificato high-risk via `classifica-sistema.md`)
- Identita' del deployer (organismo pubblico? privato che fornisce servizi pubblici? privato standard?)
- Settore Allegato III in cui ricade
- Persone fisiche interessate (categorie, vulnerabili?)
- Provider che fornisce il sistema (per richiamare istruzioni d'uso art. 13)

## Fonti

Leggere prima: `references/estratti/ai-act-art-26-27-deployer-fria.md`

## Procedura - Obblighi art. 26

### Par. 1 - Uso conforme a istruzioni
- [ ] Misure tecniche e organizzative per garantire uso conforme a istruzioni d'uso
- [ ] Sistema usato per finalita' previste

### Par. 2 - Sorveglianza umana
- [ ] Persone fisiche specificamente designate alla sorveglianza umana
- [ ] Possesso di competenza, formazione, autorita'
- [ ] Risorse di supporto

### Par. 3 - Dati di input (se controllati dal deployer)
- [ ] Rilevanza e rappresentativita' rispetto alla finalita'

### Par. 4 - Monitoraggio funzionamento
- [ ] Monitoraggio attivo sul funzionamento secondo istruzioni
- [ ] Procedura per informare il provider in caso di anomalie (art. 72)
- [ ] Sospensione uso e notifica autorita' in caso di rischio per salute/sicurezza/diritti

### Par. 5 - Conservazione log
- [ ] Log automatici conservati per periodo adeguato, **almeno 6 mesi**

### Par. 6 - Lavoratori (se uso in luogo di lavoro)
- [ ] Informazione preventiva ai rappresentanti dei lavoratori
- [ ] Informazione preventiva ai lavoratori interessati

### Par. 7 - Persone fisiche interessate
- [ ] Informazione che sono soggette al sistema high-risk per decisioni o assistenza decisioni

### Par. 8 - Cooperazione autorita'
- [ ] Disponibilita' a cooperare

### Par. 9 - DPIA GDPR
- [ ] Uso delle informazioni art. 13 per la DPIA quando trattati dati personali

### Par. 11+12 - Registrazione + FRIA per deployer pubblici/servizi pubblici
- [ ] Registrazione banca dati UE (per deployer pubblici e privati che forniscono servizi pubblici, salvo Allegato III par. 2 infrastrutture critiche)
- [ ] FRIA art. 27 prima della messa in servizio

## Procedura - FRIA art. 27 (quando applicabile)

### Quando e' obbligatorio

Il FRIA e' obbligatorio per i deployer che siano:
- Organismi di diritto pubblico
- Enti privati che forniscono servizi pubblici
- Deployer di sistemi Allegato III par. 5 lett. b) (credit scoring) e c) (insurance pricing)

(Esclusi: Allegato III par. 2 infrastrutture critiche; Allegato III par. 6-7 contrasto/migrazione)

### Contenuti minimi (par. 1 lett. a-f)

- [ ] Descrizione processi del deployer in cui il sistema sara' usato
- [ ] Periodo e frequenza d'uso
- [ ] Categorie persone fisiche e gruppi interessati
- [ ] Rischi specifici di danno alle categorie identificate
- [ ] Misure di sorveglianza umana per il caso d'uso del deployer
- [ ] Misure in caso di materializzazione dei rischi (governance, reclamo)

### Sinergia con DPIA (par. 4)

Se gli obblighi FRIA sono gia' soddisfatti da DPIA GDPR (art. 35) o LED (art. 27), il FRIA **integra** la DPIA. In pratica: documento unico con sezioni dedicate.

### Notifica autorita' (par. 3)

Risultati FRIA da notificare via modello standardizzato dall'AI Office (in via di sviluppo).

## Output strutturato

```markdown
# Verifica obblighi deployer high-risk - [contesto]

**Data verifica**: [data]
**Sistema usato**: [descrizione + classificazione + provider]
**Deployer**: [organizzazione + ruolo - pubblico/servizi pubblici/privato standard]
**Settore Allegato III**: [par. X lett. Y]

## Esito sintetico

**Status compliance**: [CONFORME / CONFORME CON GAP / GAP SOSTANZIALI / NON CONFORME]

**FRIA richiesto**: [SI / NO]
**FRIA stato**: [Effettuato / In corso / Da fare / N/A]

## Verifica obblighi art. 26

| Par. | Obbligo | Stato | Note |
|------|---------|-------|------|
| 1 | Uso conforme istruzioni | ... | ... |
| 2 | Sorveglianza umana - persone designate | ... | ... |
| 3 | Dati input (se applicabile) | ... | ... |
| 4 | Monitoraggio funzionamento + escalation | ... | ... |
| 5 | Log >= 6 mesi | ... | ... |
| 6 | Informazione lavoratori | ... | ... |
| 7 | Informazione persone fisiche interessate | ... | ... |
| 8 | Cooperazione autorita' | ... | ... |
| 9 | DPIA GDPR (se dati personali) | ... | ... |
| 11 | Registrazione banca dati UE (se applicabile) | ... | ... |
| 12 | FRIA (se applicabile) | ... | rinvio art. 27 |

## FRIA - se applicabile

[Sezione separata con i 6 contenuti minimi par. 1 lett. a-f]

| Lett. | Contenuto | Stato | Note |
|-------|-----------|-------|------|
| a | Descrizione processi del deployer | ... | ... |
| b | Periodo e frequenza d'uso | ... | ... |
| c | Categorie persone interessate | ... | ... |
| d | Rischi specifici di danno | ... | ... |
| e | Misure sorveglianza umana | ... | ... |
| f | Misure in caso di materializzazione rischi | ... | ... |

Sinergia con DPIA: [Si - documento integrato / No - separati]

## Gap principali

[Lista per priorita']

## Raccomandazioni

[Roadmap]

## Sinergia con altre normative

- GDPR art. 30 (Registro) + 35 (DPIA): vedi skill `gdpr-registro-dpia`
- LED (D.Lgs. 51/2018): per autorita' di contrasto
- D.Lgs. 196/2003 art. 154-bis: per DPO settore pubblico

## Limiti

- Verifica documentale, non sul reale uso del sistema
- Non sostituisce parere del DPO o consulente legale specializzato
- Modello FRIA standardizzato dell'AI Office in via di pubblicazione

## Rinvio

**Per deployer di sistemi high-risk + dati personali**, e' necessaria una valutazione integrata che coinvolga:
- DPO (sempre per DPIA, fortemente consigliato per FRIA)
- Consulente legale specializzato
- Esperti tecnici (per misure sorveglianza umana e log)
- Stakeholder interni (HR, IT, sicurezza, business)

Sanzioni: fino a 15M EUR o 3% del fatturato globale annuo (art. 99 par. 4).
```

## Casi tipici

### PA italiana che usa sistema AI per assistenza pubblica (Allegato III par. 5 lett. a)
- Deployer **organismo pubblico**
- Tutti gli obblighi art. 26 + FRIA art. 27 obbligatorio
- Sinergia con AgID (linee guida PA)

### Banca italiana che usa credit scoring fornito da terzo (Allegato III par. 5 lett. b)
- Deployer **privato** ma **soggetto a FRIA obbligatorio** (per il caso specifico par. 5 lett. b)
- Sinergia con normativa Banca d'Italia + Codice deontologia centrali rischi

### Azienda manifatturiera che usa sistema HR di reclutamento AI (Allegato III par. 4)
- Deployer privato, **non obbligato a FRIA** (settore non in par. 11/12 art. 26)
- Obblighi art. 26 si applicano (sorveglianza umana, informazione lavoratori, DPIA GDPR per dati personali)

### Comune che usa sistema biometrico controllo accessi dipendenti (Allegato III par. 1 lett. b)
- Deployer pubblico
- FRIA + DPIA obbligatori (sinergia)
- Anche art. 4 dello Statuto dei Lavoratori per controllo a distanza
- Tipologia 5 Provv. Garante 467/2018 -> conferma DPIA obbligatoria

## Limiti

- Lista non esaustiva: norme nazionali italiane possono aggiungere obblighi
- Modello FRIA standardizzato in attesa di pubblicazione AI Office
- Linee guida Commissione su FRIA in preparazione

## Esempi

Vedi `examples/`:
- `deployer-pa-assistenza/` - PA che usa AI per ammissibilita' assistenza pubblica (FRIA obbligatorio)
