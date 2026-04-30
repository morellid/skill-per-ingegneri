# Transizione 5.0 - Asseverazione tecnica EGE/ESCO/ingegnere/perito

> Versione: 0.1.0-alpha
> Stato: in sviluppo (Livello 1 - autore-driven, fonti pubbliche)

Skill AI di supporto alla redazione e verifica della **certificazione tecnica ex ante ed ex post** richiesta dal Piano Transizione 5.0 (DL 19/2024 art. 38, DM MIMIT-MEF 24 luglio 2024, circolare operativa MIMIT 25877/2024).

## Target

- **EGE** (Esperti Gestione dell'Energia) certificati UNI CEI 11339 da organismo Accredia
- **ESCo** (Energy Service Company) certificate UNI CEI 11352 da organismo Accredia
- **Ingegneri** iscritti nelle sezioni A o B dell'albo professionale, con esperienza in efficienza energetica dei processi produttivi
- **Periti industriali** e periti industriali laureati iscritti all'albo nelle sezioni "meccanica ed efficienza energetica" o "impiantistica elettrica ed automazione", con esperienza in efficienza energetica dei processi produttivi

> Riferimento art. 15 co. 6 DM 24/7/2024.

## Cosa fa

Quattro sotto-attivita' (per il dettaglio tecnico vedi `SKILL.md`):

1. **`tasks/verifica-ammissibilita.md`** - Verifica preliminare di ammissibilita' del progetto al Piano Transizione 5.0 (ambito soggettivo/oggettivo, avvio/completamento, DNSH, soggetto certificatore, tetto 50 mln EUR/anno).
2. **`tasks/calcola-riduzione-consumi.md`** - Calcolo strutturato della riduzione dei consumi energetici (>=3% struttura produttiva o >=5% processo interessato), con baseline ex ante, indicatori di prestazione, normalizzazione, scenario controfattuale, conversione in tep secondo circolare MISE 18/12/2014.
3. **`tasks/struttura-certificazione-ex-ante.md`** - Bozza testuale della Certificazione Ex Ante (Allegato VIII della circolare MIMIT) e della Relazione Tecnica Ex Ante (Allegato IX), con dichiarazione di terzieta' (Allegato III).
4. **`tasks/struttura-certificazione-ex-post.md`** - Bozza testuale della Certificazione Ex Post (Allegato X) e della Relazione Tecnica Ex Post (Allegato XI), con confronto sui dati misurati ex post e gestione di eventuali scostamenti / modifiche al progetto (FAQ MIMIT 2.10).

## Installazione

| Agent | Path target |
|---|---|
| Anthropic Claude Code | `~/.claude/skills/transizione-5-0-asseverazione/` |
| OpenAI Codex | `~/.agents/skills/transizione-5-0-asseverazione/` |

```bash
# Claude Code
cp -r skills/transizione-5-0-asseverazione ~/.claude/skills/

# Codex
cp -r skills/transizione-5-0-asseverazione ~/.agents/skills/
```

Riavviare l'agent.

## Fonti consultate

Dettaglio in [`references/sources.yaml`](references/sources.yaml). Fonti primarie:

- **DL 2 marzo 2024 n. 19** art. 38 (convertito dalla L. 56/2024) - istituzione Piano Transizione 5.0
- **DM MIMIT-MEF 24 luglio 2024** - decreto attuativo (GU n. 183 del 06/08/2024, codice 24A04160)
- **Circolare operativa MIMIT 16 agosto 2024 prot. 25877** - chiarimenti tecnici e modelli vincolanti delle certificazioni
- **FAQ MIMIT** - aggiornamento 10 aprile 2025 (versione vigente al `last_verified`)
- **Circolare MISE 18 dicembre 2014** - coefficienti di conversione in tep ex art. 19 L. 10/1991

Fonti di rinvio:

- **UNI CEI 11339:2009** (EGE) - norma proprietaria, requisiti del certificatore
- **UNI CEI 11352:2014** (ESCo) - norma proprietaria, requisiti del certificatore
- **L. 232/2016** allegati A e B - beni 4.0
- **DPR 445/2000** artt. 46-76 - DSAN e sanzioni penali
- **Codice penale** artt. 359, 481 - persona esercente servizio di pubblica necessita'
- **Reg. UE 2020/852** art. 17 - principio DNSH

## Limiti noti

- La skill **non e' la perizia tecnica caratteristiche e interconnessione beni 4.0** (art. 16 DM): adempimento distinto, di ingegnere/perito o ente accreditato.
- La skill **non e' la certificazione contabile** (art. 17 DM): adempimento del revisore legale dei conti.
- La skill **non sostituisce il sopralluogo** presso la struttura produttiva (espressamente richiesto dai modelli Allegati VIII / X).
- La skill **non valida l'indipendenza** del certificatore (verifica del MIMIT/GSE in sede di vigilanza).
- La skill **non interagisce con il portale TR5 GSE**: il caricamento e' adempimento separato.
- La skill **non aggiorna automaticamente** coefficienti tep, aliquote, soglie a fronte di modifiche normative successive (es. L. 207/2024 e successivi DM correttivi). Verificare `last_verified` di `sources.yaml`.

**Ogni output e' supporto al valutatore indipendente, non sostituzione.** Il rischio penale (artt. 359, 481 c.p. + art. 76 DPR 445/2000) e civile resta in capo al certificatore firmatario.

## Avvertenza

La certificazione tecnica del Piano Transizione 5.0 e' resa ai sensi degli artt. 46 e segg. DPR 445/2000 e degli artt. 359 e 481 del codice penale. Il certificatore agisce in qualita' di **persona esercente un servizio di pubblica necessita'**: false attestazioni espongono a **responsabilita' penale aggravata** oltre che a responsabilita' civile e perdita dell'abilitazione al rilascio.

## Changelog

Vedi [CHANGELOG.md](CHANGELOG.md).
