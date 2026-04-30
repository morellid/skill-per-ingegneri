# Catasto - Atti telematici Pregeo 10 + Docfa 4

> Versione: 0.1.0-alpha
> Stato: in sviluppo (alpha, non ancora validata da dominio terzo)

Skill di assistenza alla redazione e alla verifica pre-trasmissione degli atti telematici di aggiornamento del Catasto Terreni (Pregeo 10) e del Catasto Fabbricati (Docfa 4) ai sensi del DPR 380/2001 art. 30, del DM 28/1998, della Circolare AdE Territorio 3 del 16/10/2009 (e successive integrazioni - Circolari 44/E 2016, 11/E 2023), della Risoluzione AdE 40/E del 9/6/2025 (deposito telematico frazionamenti dal 1/7/2025), del Vademecum Do.C.Fa. v1.0 (luglio 2022) e delle istruzioni operative AdE per professionisti.

## Target

Geometri, ingegneri (sez. A e B), architetti, dottori agronomi, periti agrari, periti edili, periti industriali "edilizia" iscritti all'Ordine/Collegio competente e abilitati alla trasmissione telematica degli atti di aggiornamento catastale via Sister (Provv. AdE 11/3/2015 prot. 35112). Per le Pubbliche Amministrazioni titolari di diritti reali su beni propri, regime facoltativo (Provv. AdE 28/1/2021 prot. 27427).

## Cosa fa

Cinque sotto-attivita' (dettagli in `SKILL.md` e nei task file):

1. **Scelta della tipologia di atto Pregeo e check pre-trasmissione Catasto Terreni** - aiuta a scegliere fra Tipo Mappale (TM), Tipo Frazionamento (FR), Atto Misto (FM), Tipo Mappale con Stralcio di Corte (SC), Tipo Particellare (TP) e atti speciali; codifica la riga 9 del libretto delle misure secondo Circ. 3/2009; verifica i requisiti del nuovo deposito telematico ex art. 30 co. 5-bis DPR 380/2001 (Risoluzione AdE 40/E del 9/6/2025).
2. **Scelta della causale Docfa e categoria catastale** - guida la scelta della causale Quadro A (Nuova Costruzione, Unita' afferenti) o Quadro B (Variazione planimetrica, toponomastica, di destinazione, ecc.) e della categoria catastale (Gruppi A, B, C, D, E, F).
3. **Check pre-trasmissione Docfa - Quadro D, EP, ES, planimetrie** - verifica completezza Elaborato Planimetrico, Elenco Subalterni, Entita' Tipologiche, planimetrie e dichiarazioni obbligatorie nel Quadro D secondo il Vademecum cap. 2.4.2 e 3.1.
4. **Diagnosi rifiuti telematici Pregeo / Docfa** - mappa il messaggio di rifiuto/sospensione dell'Ufficio Provinciale Territorio sulla causa probabile e propone la correzione, citando la fonte normativa.
5. **Workflow misto Pregeo -> Docfa** - per accatastamenti che seguono un Tipo Mappale, guida la sequenza Pregeo -> approvazione -> iscrizione automatica F/6 -> Docfa di accatastamento -> voltura.

## Installazione

Vedi [`AGENTS.md` di repo](../../AGENTS.md) per le istruzioni di installazione su Anthropic Claude Code (`~/.claude/skills/`) e OpenAI Codex (`~/.agents/skills/`).

```bash
# Claude Code
cp -r skills/catasto-pregeo-docfa-atti-telematici ~/.claude/skills/

# Codex
cp -r skills/catasto-pregeo-docfa-atti-telematici ~/.agents/skills/
```

Dopo l'installazione riavvia il tuo agent (Claude Code o Codex) per la discovery.

## Fonti consultate

Lista completa con URL, data di consultazione, hash SHA256 dei binari e licenza in [`references/sources.yaml`](references/sources.yaml).

Sintesi delle fonti primarie:

- DPR 380/2001 art. 30 co. 5 e 5-bis (Testo Unico Edilizia, testo coordinato con D.Lgs. 1/2024 art. 25)
- DM 28/1998 art. 2 e art. 3 (definizione UIU e categorie F)
- DPR 445/2000 artt. 38, 47, 76 (DSAN)
- Circolare AdE Territorio 3 del 16/10/2009 (Pregeo 10) + Circ. 44/E 2016 + Circ. 11/E 2023
- Risoluzione AdE 40/E del 9/6/2025 (deposito telematico frazionamenti dal 1/7/2025)
- Vademecum Do.C.Fa. v1.0 (luglio 2022)
- Istruzioni operative Docfa 4.00.5 (luglio 2019)
- Provv. AdE 30/12/2024 (decorrenza 1/7/2025), Provv. 11/3/2015 (obbligo telematico professionisti), Provv. 28/1/2021 (PA)

## Limiti noti

La skill **non**:

- sostituisce il manuale operativo Pregeo o Docfa (non riproduce le interfacce di compilazione campo-per-campo);
- esegue calcoli topografici (compensazione, riduzione GNSS, calcolo coordinate PF);
- determina la rendita catastale (richiede tariffe d'estimo per zona censuaria, variabili);
- determina la superficie catastale ex DPR 138/1998 All. C (richiede applicazione di coefficienti);
- esegue il classamento delle UIU (compito del professionista);
- sostituisce il sopralluogo fisico per perimetrazione UIU e BCC/BCNC;
- gestisce le procedure Sister o del Portale dei Comuni (cambiano con i rilasci);
- interpreta la disciplina tavolare di Libro Fondiario (RD 499/1929) per zone Trentino, Alto Adige, Trieste, Gorizia.

La responsabilita' penale (artt. 359, 481 c.p. + art. 76 DPR 445/2000), civile e disciplinare resta in capo al professionista firmatario dell'atto trasmesso. Vedi `SKILL.md` per il disclaimer completo.

## Changelog

Vedi [CHANGELOG.md](CHANGELOG.md).
