# skill-per-ingegneri

Repository collettivo di skill AI per la pratica dell'ingegneria italiana.

## Cosa contiene

Skill AI in formato dual-agent (compatibili sia con [Anthropic Claude Code](https://claude.com/claude-code) sia con [OpenAI Codex](https://developers.openai.com/codex)), scritte in italiano, basate esclusivamente su fonti normative ufficiali (D.Lgs., decreti attuativi, linee guida pubbliche). Ogni skill e' pensata per essere usata da ingegneri iscritti all'Albo come supporto - non sostituto - nella redazione e verifica di documenti tecnici e adempimenti.

Ogni skill e' anche utilizzabile da agent che leggono lo standard aperto [`AGENTS.md`](AGENTS.md) (Codex, Cursor, Windsurf, GitHub Copilot, Devin, Amp, Antigravity, ...).

Contiene anche:
- **Metodologia replicabile** per generare nuove skill (`methodology/`)
- **Template e script** per scaffolding e validazione (`templates/`, `scripts/`)
- **Riferimenti bibliografici** strutturati con hash delle fonti (`sources.yaml` per ogni skill)

## Skill disponibili

| Skill | Ambito | Riferimenti normativi |
|---|---|---|
| [`pos-allegato-xv-checker`](skills/pos-allegato-xv-checker/) | Guida la compilazione assistita e verifica completezza e coerenza di un Piano Operativo di Sicurezza (POS) di cantiere | D.Lgs. 81/2008 art. 96-97, Allegato XV + DI 9/9/2014 modelli semplificati |
| [`dvr-generico`](skills/dvr-generico/) | Stesura, verifica e aggiornamento del Documento di Valutazione dei Rischi (DVR) cross-settoriale | D.Lgs. 81/2008 art. 17, 28, 29 |
| [`gdpr-registro-dpia`](skills/gdpr-registro-dpia/) | Registro delle attivita' di trattamento e Valutazione d'Impatto (DPIA), con modulo tracking pixel e-mail | GDPR art. 30, 35, 36 + provv. Garante + Linee guida tracking pixel (provv. 284/2026) |
| [`nis2-self-assessment`](skills/nis2-self-assessment/) | Self-assessment NIS2 (perimetro, gap analysis misure ACN, notifica incidenti, governance) | D.Lgs. 138/2024 + Det. ACN 379907/2025 |
| [`ai-act-compliance`](skills/ai-act-compliance/) | Classificazione sistemi AI + obblighi provider/deployer/GPAI/trasparenza | Reg. UE 2024/1689 (AI Act) |
| [`spettro-risposta-ntc`](skills/spettro-risposta-ntc/) | Calcolo code-driven dello spettro di risposta elastico orizzontale (TR, ag/F0/Tc*, S, eta, TB/TC/TD, Se(T)) per SLO/SLD/SLV/SLC | NTC 2018 par. 3.2 + Circ. 7/2019 |
| [`combinazioni-carico-ntc`](skills/combinazioni-carico-ntc/) | Generazione/verifica code-driven delle combinazioni delle azioni SLU/SLE/sismiche/eccezionali per edifici civili e industriali correnti | NTC 2018 par. 2.5.3 + Tab. 2.5.I + Tab. 2.6.I |
| [`carichi-atmosferici-ntc`](skills/carichi-atmosferici-ntc/) | Calcolo code-driven della pressione del vento p (par. 3.3) e del carico neve sulla copertura q_s (par. 3.4) per edifici civili e industriali correnti, dato sito (parametri zonali, altitudine), categoria di esposizione I-V, geometria (z, c_p, alpha falda, classe esposizione neve); output v_b/c_r/q_r/c_e/p e q_sk/mu_1/c_E/q_s con citazione paragrafi NTC | NTC 2018 par. 3.3 + par. 3.4 + Circ. 7/2019 par. C3.3-C3.4 |
| [`pfte-allegato-i7-checker`](skills/pfte-allegato-i7-checker/) | Checklist e verifica completezza degli elaborati di un PFTE / progetto esecutivo di lavori pubblici, integrato dal correttivo 2024 | D.Lgs. 36/2023 art. 41 + Allegato I.7 + D.Lgs. 209/2024 |
| [`modulistica-edilizia-unificata`](skills/modulistica-edilizia-unificata/) | Determina il modulo edilizio unificato (Edilizia libera / CILA / SCIA / SCIA alternativa al PdC / PdC / Sanatoria art. 36 / 36-bis) per un intervento e l'elenco degli allegati richiesti, integrato con le modifiche del Salva Casa | DPR 380/2001 + D.Lgs. 222/2016 Tabella A + DL 69/2024 conv. L. 105/2024 + Modulistica unificata 27/3/2025 |
| [`transizione-5-0-asseverazione`](skills/transizione-5-0-asseverazione/) | Asseverazione tecnica ex ante / ex post per il credito d'imposta Piano Transizione 5.0 (calcolo riduzione consumi >=3% struttura o >=5% processo, conversione tep, modelli MIMIT) | DL 19/2024 art. 38 + DM MIMIT-MEF 24/7/2024 + Circolare MIMIT 25877/2024 |
| [`dnsh-pnrr-checker`](skills/dnsh-pnrr-checker/) | Verifica documentale DNSH per interventi PNRR e, solo se la misura lo richiama espressamente, per interventi PNC: mappatura misura, schede tecniche RGS, checklist ex ante/ex post, piano evidenze e report per gara/SAL/collaudo/ReGiS | Reg. UE 2020/852 art. 17 + Reg. UE 2021/241 art. 5 e 18 + Circolare RGS 22/2024 + Guida operativa DNSH RGS 2024 + DL 77/2021 art. 14 |
| [`piano-lavoro-amianto`](skills/piano-lavoro-amianto/) | Precheck, redazione guidata e verifica del piano di lavoro per demolizione o rimozione di amianto, nel testo vigente dell'art. 256 D.Lgs. 81/2008 aggiornato dal D.Lgs. 213/2025 | D.Lgs. 81/2008 art. 251, 256, 258, 259 + D.Lgs. 213/2025 + DM 6/9/1994 |
| [`catasto-pregeo-docfa-atti-telematici`](skills/catasto-pregeo-docfa-atti-telematici/) | Assistente alla redazione e al check pre-trasmissione degli atti telematici di aggiornamento del Catasto Terreni (Pregeo 10) e del Catasto Fabbricati (Docfa 4): scelta tipologia atto Pregeo (TM/FR/FM/SC/TP), causale e categoria Docfa, EP/ES/ET/Quadro D, deposito telematico frazionamenti dal 1/7/2025, diagnosi rifiuti telematici via Sister | DPR 380/2001 art. 30 + DM 28/1998 + Circ. AdE 3/2009 + Vademecum Docfa v1.0 (7/2022) + Risoluzione AdE 40/E del 9/6/2025 |
| [`pratiche-edilizie-lr65-2014-toscana`](skills/pratiche-edilizie-lr65-2014-toscana/) | Determina il titolo abilitativo edilizio (Edilizia libera / CILA / SCIA / SCIA alternativa al PdC / PdC) per interventi in Toscana e genera la checklist documenti richiesti, con specificita' regionali (sismica DGRT 421/2014, DPGR 1/R/2022 Genio Civile, vincolo paesaggistico, Piano Operativo) | LR Toscana 65/2014 + DPR 380/2001 + DPGR 1/R/2022 + DPR 31/2017 (paesaggio) |
| [`cer-cacer-configurazione-gse`](skills/cer-cacer-configurazione-gse/) | Configurazione di CER (art. 31), GAC (art. 30 c. 2) o AID (art. 30 c. 1 lett. a) n. 2) con verifica perimetro cabina primaria, redazione guidata dello statuto, simulazione semplificata di energia condivisa, TIP, tariffa di restituzione e contributo PNRR per Comuni < 50.000 ab. (regime vigente al 2026-05-07: DM 414/2023 + DM 127/2025 + DL 19/2026 art. 27), e checklist documentale per la qualifica al portale GSE | D.Lgs. 199/2021 artt. 30-31-32 + DM MASE 7/12/2023 n. 414 + DM MASE 16/5/2025 n. 127 + DL 19/2/2026 n. 19 art. 27 + Delibera ARERA 727/2022/R/eel (TIAD) + Regole Operative CACER del GSE |
| [`sismabonus-classificazione-rischio-pam`](skills/sismabonus-classificazione-rischio-pam/) | Calcolo code-driven della classe di rischio sismico DM 58/2017 (sismabonus, metodo convenzionale): PAM come area trapezoidale della Curva di Individuazione su SLID/SLO/SLD/SLV/SLC + coda SLR, IS-V = PGA_C(SLV)/PGA_D(SLV), classe finale = peggiore tra classe PAM (8 classi A+..G) e classe IS-V (7 classi A+..F), salto classi tra stato di fatto e stato di progetto | DM 58/2017 + DM 65/2017 + DM 24/2020 + DM 329/2020 (Allegato A) + NTC 2018 cap. 3.2 e cap. 8 + Circ. 7/2019 |
| [`bandi-tipo-anac-checker`](skills/bandi-tipo-anac-checker/) | Verifica la conformita' di un disciplinare di gara agli schemi ANAC (bandi-tipo) obbligatori per le stazioni appaltanti; identifica deroghe non giustificate, clausole mancanti, riferimenti obsoleti (D.Lgs. 50/2016) e anomalie a rischio TAR prima della pubblicazione | D.Lgs. 36/2023 + Bandi-tipo ANAC (n. 1/2023 agg. Delibera 148/2026, n. 2/2026 SIA Delibera 153/2026) |
| [`oepv-valutatore-offerte-tecniche`](skills/oepv-valutatore-offerte-tecniche/) | Costruzione della matrice criteri/sottocriteri OEPV, valutazione delle offerte tecniche con metodo aggregativo-compensatore, verifica di conformita' all'art. 108 di una matrice gia' redatta | D.Lgs. 36/2023 art. 108 |
| [`cra-classificazione-pde`](skills/cra-classificazione-pde/) | Classificazione di un prodotto con elementi digitali (PDE) ai sensi del CRA (default / importante Classe I / Classe II / critico) e selezione del modulo di valutazione della conformita' (A, B+C, H, certificazione europea) + struttura documentazione tecnica Allegato VII | Reg. UE 2024/2847 (Cyber Resilience Act) |
| [`dora-gap-assessment`](skills/dora-gap-assessment/) | Gap assessment di un'entita' finanziaria (banca, IMEL, IP, SIM, assicurazione, MiCA CASP, ecc.) rispetto ai 5 pillar DORA, applicabile dal 17/1/2025 | Reg. UE 2022/2554 (DORA) artt. 5-30, 45 |
| [`ped-classificazione-conformita`](skills/ped-classificazione-conformita/) | Classificazione di un'attrezzatura a pressione (recipiente, tubazione, accessorio di sicurezza o a pressione, insieme) nelle categorie I/II/III/IV e selezione del modulo di valutazione della conformita' applicabile, marcatura e dichiarazione richieste | D.Lgs. 26/2016 (recepimento Direttiva PED 2014/68/UE) |
| [`dm37-2008-dichiarazione-conformita`](skills/dm37-2008-dichiarazione-conformita/) | Compilazione e verifica della Dichiarazione di Conformita' (DdC) degli impianti tecnologici (7 categorie a-g modello Allegato I), determinazione degli allegati obbligatori e dell'obbligo di progetto da professionista ex Art. 5 | DM 22/1/2008 n. 37 |
| [`relazione-cam-dm256-2022`](skills/relazione-cam-dm256-2022/) | Redazione e verifica della Relazione Tecnica dei Requisiti Ambientali CAM per servizi di progettazione e lavori su edifici pubblici (NC / R1 / R2 / MS): identificazione criteri applicabili, struttura capitolare, check completezza di una relazione esistente | DM 23/6/2022 n. 256 (CAM edilizia) + D.Lgs. 36/2023 art. 57 |
| [`rsia-audit-stradale-dlgs35`](skills/rsia-audit-stradale-dlgs35/) | Supporto alle quattro procedure di gestione della sicurezza delle infrastrutture stradali: VISS (impatto sui progetti), RSA (controlli sulle fasi progettuali), NSA (valutazione a livello di rete), ispezioni periodiche/mirate sulle strade in esercizio | D.Lgs. 35/2011 modificato dal D.Lgs. 213/2021 (recepimento Dir. UE 2019/1936) |
| [`pums-validator-dm397`](skills/pums-validator-dm397/) | Verifica della conformita' formale e di completezza di un Piano Urbano di Mobilita' Sostenibile (PUMS) per comuni > 100.000 ab., citta' metropolitane o associazioni di comuni che superano la soglia | DM 397/2017 + DM 396/2019 + DM 29/2021 + DM 444/2021 + Vademecum MIMS 2022 |
| [`valutazione-impatto-clima-acustico-l-447`](skills/valutazione-impatto-clima-acustico-l-447/) | Documentazione previsionale di impatto acustico (art. 8 c. 2 e c. 4) e valutazione previsionale di clima acustico (art. 8 c. 3) da allegare a SCIA/PdC/autorizzazione: mapping applicabilita', check contenuti minimi della relazione, riferimenti puntuali ai valori limite | L. 447/1995 art. 8 + DPCM 14/11/1997 + DM 16/3/1998 |
| [`valutazione-cem-srb-art-87-cce`](skills/valutazione-cem-srb-art-87-cce/) | Pratica di autorizzazione SRB (stazioni radio base, ripetitori, ponti radio) ex art. 87 CCE: check completezza istanza/SCIA, mapping iter (Ente locale + parere ARPA), checklist per la relazione predittiva CEM secondo CEI 211-7 | D.Lgs. 259/2003 art. 87 + DPCM 8/7/2003 + L. 36/2001 art. 14 + CEI 211-7 |
| [`cbam-declarant-trimestrale`](skills/cbam-declarant-trimestrale/) | Adempimenti del dichiarante CBAM autorizzato nella fase definitiva (dal 1/1/2026): verifica qualifica e applicabilita' deroghe (soglia 50 t, art. 17 §7bis con TARIC Y238 fino al 27/9/2026), pianificazione obbligo trimestrale 50% sui certificati CBAM (Art. 22 §2 dal 2027), dichiarazione annuale Art. 6 (prima volta 30/9/2027 per anno 2026), esposizione sanzionatoria Art. 26 | Reg. UE 2023/956 (CBAM) modificato da Reg. UE 2025/2083 |
| [`cedimenti-edometrici-ntc`](skills/cedimenti-edometrici-ntc/) | Controllo di completezza di una verifica dei cedimenti geotecnici (prestazioni attese, spostamenti compatibili, metodo di interazione terreno-struttura, confronto SLE) - skill di supporto documentale che non sostituisce il calcolo geotecnico | NTC 2018 + Circolare 7/2019 |
| [`predimensionamento-flessione-ca-ntc`](skills/predimensionamento-flessione-ca-ntc/) | Calcolo code-driven di M_Rd di sezione rettangolare in c.a. singolarmente armata in flessione semplice SLU (stress-block rettangolare equivalente eta=1, lambda=0.8): f_cd, f_yd, eps_yd, profondita' asse neutro x, x/d, eps_s, braccio z, M_Rd in kNm, verifica duttilita' x/d <= 0.45. Solo fck <= 50 MPa (Classe 1) e sezioni singolarmente armate | NTC 2018 par. 4.1.2.1 e 4.1.2.3.4.2 + Circolare 7/2019 par. C4.1.2 |
| [`fascicolo-tecnico-macchine-reg-1230`](skills/fascicolo-tecnico-macchine-reg-1230/) | Redazione e verifica del fascicolo tecnico di una macchina, prodotto correlato o quasi-macchina ai sensi del nuovo Regolamento Macchine UE: qualificazione del prodotto, scelta procedura di valutazione conformita' (art. 25, Allegato I, moduli A/B/C/G/H), checklist contenuti Allegato IV parti A e B, struttura dichiarazioni UE Allegato V parti A e B (sostituisce Dir. 2006/42/CE dal 14/1/2027) | Reg. UE 2023/1230 (Regolamento Macchine) |
| [`aua-dpr59-dossier`](skills/aua-dpr59-dossier/) | Supporto alla preparazione e all'autoverifica del dossier per l'Autorizzazione Unica Ambientale (AUA) per PMI e impianti non-AIA: verifica applicabilita' (PMI / non-AIA / non-VIA assorbente), mapping dei 9 titoli incorporabili ex art. 3 co. 1 (lett. a-g, g-bis, g-ter), pianificazione termini procedurali (30/90/120/150 giorni + conferenza di servizi), pianificazione rinnovo a 6 mesi dalla scadenza (durata 15 anni), triage modifica sostanziale / non sostanziale ex art. 6 | D.P.R. 13/3/2013 n. 59 + D.Lgs. 152/2006 (richiamato) + L. 447/1995 art. 8 + D.Lgs. 101/2020 artt. 24-26 (lett. g-bis/g-ter dal D.Lgs. 203/2022) + L. 241/1990 + D.P.R. 160/2010 |
| [`denuncia-opere-strutturali-l1086`](skills/denuncia-opere-strutturali-l1086/) | Diagnosi degli adempimenti procedurali strutturali e sismici del DPR 380/2001 per interventi edilizi in Italia: denuncia opere in c.a./c.a.p./metalliche (art. 65), collaudo statico (art. 67), preavviso e autorizzazione preventiva in zona sismica (artt. 93, 94, 94-bis), classificazione interventi rilevanti / minore rilevanza / privi di rilevanza ex art. 94-bis, coordinamento art. 65 e art. 93 c. 5, esclusioni commi 8-bis e 8-ter | DPR 380/2001 artt. 65, 67, 83, 93, 94, 94-bis (testo multivigente Normattiva) |
| [`relazione-geologica-geotecnica-ntc`](skills/relazione-geologica-geotecnica-ntc/) | Controllo di completezza della relazione geologica e della relazione geotecnica richieste dalle NTC 2018, controllo di coerenza tra le due relazioni (e con la relazione di calcolo) e bozza di indice commentato della relazione geotecnica - supporto documentale che non sostituisce il professionista firmatario | NTC 2018 (DM 17/01/2018) parr. 6.1-6.2.6 + Circolare C.S.LL.PP. 7/2019 parr. C6.2, C9.1 lett. g, C10.1 |

Ogni skill ha un proprio `README.md` con dettaglio target, sotto-attivita' e limiti noti.

## Struttura

```
skill-per-ingegneri/
├── AGENTS.md                    # guida cross-agent (Codex, Cursor, Copilot, ...)
├── skills/                      # le skill pubblicate (elenco completo: tabella sopra)
│   ├── pos-allegato-xv-checker/
│   │   ├── SKILL.md             # punto d'ingresso + routing (license: MIT in frontmatter)
│   │   ├── agents/
│   │   │   └── openai.yaml      # UI metadata per Codex
│   │   ├── tasks/               # istruzioni dettagliate per sotto-attivita'
│   │   ├── references/          # metadata fonti + estratti normativi
│   │   ├── examples/            # casi d'uso validi e problematici
│   │   └── CHANGELOG.md
│   └── <altre-skill>/           # stessa struttura per ciascuna skill
├── methodology/                 # come si genera e mantiene una skill
├── templates/                   # scaffold dual-agent per nuove skill
└── scripts/                     # utility CLI (new-skill, validate, fetch-sources)
```

## Come installare e usare le skill

Ogni skill in `skills/<nome>/` e' un pacchetto autonomo. Si installa nella directory skills del tuo agent.

| Agent | Path target |
|---|---|
| Anthropic Claude Code | `~/.claude/skills/<nome-skill>/` |
| OpenAI Codex | `~/.agents/skills/<nome-skill>/` |

### Installazione di una singola skill

```bash
# Claude Code
cp -r skills/pos-allegato-xv-checker ~/.claude/skills/

# Codex
cp -r skills/pos-allegato-xv-checker ~/.agents/skills/
```

### Installazione di tutto il catalogo via symlink

```bash
# Claude Code
mkdir -p ~/.claude/skills
for s in skills/*/; do
  ln -sfn "$(pwd)/$s" "$HOME/.claude/skills/$(basename "$s")"
done

# Codex
mkdir -p ~/.agents/skills
for s in skills/*/; do
  ln -sfn "$(pwd)/$s" "$HOME/.agents/skills/$(basename "$s")"
done
```

I symlink permettono di aggiornare tutte le skill installate con `git pull` nel repo.

### Installazione via Claude Code plugin marketplace

Le skill sono distribuite anche come marketplace nativo Claude Code: un plugin per ogni area del catalogo. Dentro Claude Code:

```
/plugin marketplace add morellid/skill-per-ingegneri
/plugin install <area-id>@skill-per-ingegneri
```

Dove `<area-id>` e' uno tra: `sicurezza-lavoro-cantieri`, `strutture-geotecnica`, `edilizia-urbanistica-catasto`, `appalti-opere-pubbliche`, `energia-incentivi`, `ambiente-territorio-mobilita`, `impianti-macchine-prodotti`, `software-dati-cybersecurity`. Le skill installate sono namespacciate (es. `/strutture-geotecnica:spettro-risposta-ntc`).

In alternativa, da terminale via il CLI [`vercel-labs/skills`](https://github.com/vercel-labs/skills):

```bash
npx skills@latest add morellid/skill-per-ingegneri
```

Il manifest e' in `.claude-plugin/marketplace.json`, **rigenerato automaticamente** da `scripts/build_catalog.py`.

### Installazione drag-and-drop su Claude.ai

Ogni skill e' distribuita anche come `.zip` autonomo nelle [GitHub Releases](https://github.com/morellid/skill-per-ingegneri/releases). Utile se usi Claude solo via web (claude.ai) e non hai installato Claude Code.

1. Apri l'ultima release: https://github.com/morellid/skill-per-ingegneri/releases/latest
2. Scarica il file `<skill-id>.zip` della skill che ti interessa (es. `pos-allegato-xv-checker.zip`).
3. Vai su https://claude.ai/customize/skills e fai upload (o drag-and-drop) del file `.zip`.

Lo zip contiene la skill completa (`SKILL.md`, `tasks/`, `examples/`, `references/`, `LICENSE`) in una singola directory top-level. Non serve estrarlo prima dell'upload.

### Codex `$skill-installer`

Da una sessione Codex (per skill singole):

```
$skill-installer https://github.com/<user>/skill-per-ingegneri/skills/pos-allegato-xv-checker
```

### Uso

Riavvia il tuo agent dopo l'installazione. Poi fai una domanda nel dominio della skill:

> "Verifica questo POS rispetto all'Allegato XV..."
>
> "Aiutami a redigere un DVR per un'azienda di 30 dipendenti"
>
> "Serve una DPIA per il nostro nuovo sistema di scoring clienti?"

L'agent caricara' la skill appropriata. In Codex puoi anche invocare esplicitamente: `/skills <nome-skill>`.

### Uso da altri agent (Cursor, Windsurf, GitHub Copilot, Devin, Amp, ...)

Per agent che leggono lo standard aperto [AGENTS.md](https://agents.md/), referenzia questo repo come submodule e aggiungi un puntatore al tuo progetto. Vedi [`AGENTS.md`](AGENTS.md) per i dettagli e le convenzioni.

Istruzioni dettagliate per ogni singola skill nel rispettivo `README.md` dentro `skills/<nome>/`.

## Come contribuire

Vedi [CONTRIBUTING.md](CONTRIBUTING.md). In sintesi:
- Solo fonti normative ufficiali (niente interpretazioni personali senza riferimento)
- Validazione da parte di un ingegnere di dominio prima del release
- Disclaimer di responsabilita' professionale obbligatorio in ogni skill
- Semver per skill, CHANGELOG aggiornato

## Principi

1. **Supporto, non sostituto**. Ogni skill emette output che richiede verifica e firma del professionista. Nessuna skill produce documenti auto-firmati o pronti al deposito senza revisione umana.
2. **Tracciabilita' delle fonti**. Ogni affermazione normativa e' riconducibile a un documento identificato da hash e data di consultazione (vedi `sources.yaml`).
3. **Lingua italiana**. Gli adempimenti sono italiani: istruzioni, output e riferimenti normativi sono in italiano. Struttura del codice e metadata in inglese per compatibilita' internazionale.
4. **Progressive disclosure**. Ogni skill e' monolitica ma carica solo i dettagli che servono per la specifica sotto-attivita' richiesta dall'utente.

## Autore

Davide Morelli <morelli.davide@gmail.com>

## Licenza

MIT. Vedi [LICENSE](LICENSE).

## Avvertenza

Le skill in questo repository sono strumenti di supporto e non sostituiscono il giudizio professionale. L'utilizzo improprio o non verificato degli output e' responsabilita' esclusiva dell'utente.
