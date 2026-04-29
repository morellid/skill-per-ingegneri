# NIS2 self-assessment (D.Lgs. 138/2024)

> Versione: 0.1.0-alpha
> Stato: in sviluppo - validazione Livello 1 (auto-validazione autore). Validazione Livello 2 con consulente cybersecurity da pianificare.

Skill di supporto alla self-assessment NIS2 per organizzazioni italiane (private e pubbliche) ai sensi del **D.Lgs. 4 settembre 2024, n. 138** (recepimento della Direttiva (UE) 2022/2555) e dei provvedimenti attuativi dell'**Agenzia per la Cybersicurezza Nazionale (ACN)**.

## Target

CISO, IT manager, DPO, ingegneri dell'informazione, consulenti cybersecurity di organizzazioni italiane potenzialmente in ambito NIS. Utile per:
- Organizzazioni che si affacciano per la prima volta alla compliance NIS2
- Consulenti che supportano piu' clienti nella registrazione sulla piattaforma ACN
- Ingegneri dell'informazione che valutano se i loro sistemi/clienti rientrano nel perimetro
- DPO che devono coordinare NIS2 con GDPR

## Cosa fa

La skill articola la self-assessment in 4 sotto-attivita':

1. **Valutazione del perimetro** - "siamo soggetti NIS2? essenziali o importanti?" (art. 3, 6 D.Lgs. 138/2024 + Allegati I-IV)
2. **Gap analysis misure di base** - confronto fra le misure adottate e i requisiti del Framework Nazionale Cybersecurity richiamati dalla Determinazione ACN 379907/2025 vigente dal 15/01/2026 (Allegato 1 importanti, 37 sottocat / Allegato 2 essenziali, 43 sottocat) + 10 elementi minimi art. 24 co. 2
3. **Verifica incidente significativo** - "questo incidente va notificato? in quanto tempo?" (art. 25: 24h pre-notifica / 72h notifica / 1 mese report finale)
4. **Obblighi governance** - "cosa deve fare il CdA?" (art. 23: approvazione misure, formazione, responsabilita' personale)

Per il dettaglio tecnico vedi [`SKILL.md`](SKILL.md). Routing fra task da `SKILL.md`.

## Installazione

Compatibile con Anthropic Claude Code e OpenAI Codex.

```bash
# Claude Code
cp -r skills/nis2-self-assessment ~/.claude/skills/

# Codex
cp -r skills/nis2-self-assessment ~/.agents/skills/

# Oppure symlink dal repo
ln -sfn "$(pwd)/skills/nis2-self-assessment" "$HOME/.claude/skills/nis2-self-assessment"
ln -sfn "$(pwd)/skills/nis2-self-assessment" "$HOME/.agents/skills/nis2-self-assessment"
```

Riavvia il tuo agent per la discovery.

## Fonti consultate

Fonti primarie (testo verbatim catalogato e analizzato):
- **D.Lgs. 4 settembre 2024, n. 138** - GU Serie Generale n. 230 del 01/10/2024 (in vigore dal 16/10/2024)
- **Direttiva (UE) 2022/2555 (NIS 2)** del 14/12/2022
- **Regolamento di esecuzione (UE) 2024/2690** del 17/10/2024 (per sottoinsieme di soggetti)
- **Determinazione ACN n. 164179 del 14/04/2025** (sostituita)
- **Determinazione ACN n. 379907 del 18/12/2025** (in vigore dal 15/01/2026; sostitutiva della 164179/2025; cataloga il documento principale + 4 Allegati: misure importanti, misure essenziali, incidenti importanti, incidenti essenziali). I termini di adeguamento (18 mesi misure / 9 mesi notifica incidenti) decorrono dalla **comunicazione di inserimento** personale ricevuta dal soggetto.

Dettaglio completo in [`references/sources.yaml`](references/sources.yaml). Estratti testuali in [`references/estratti/`](references/estratti/).

## Limiti noti

Questa skill **non**:
- Sostituisce il CISO, il consulente cybersecurity o il legale specializzato
- Produce documenti pronti per la registrazione sulla piattaforma ACN o per la notifica al CSIRT Italia
- Esegue audit di conformita' o ispezioni
- Valida la conformita' al Reg. UE 2024/2690 nel dettaglio dei requisiti tecnici (rinvio a ENISA technical guidance)
- Gestisce la conformita' DORA per gli enti finanziari (settori 3-4 Allegato I) - rinvio a Reg. UE 2022/2554
- Sostituisce il punto di contatto NIS designato dal soggetto sulla piattaforma ACN

**Sanzioni amministrative ex art. 38 D.Lgs. 138/2024**: fino a 10M EUR o 2% fatturato (essenziali), 7M EUR o 1.4% (importanti). La skill non fornisce difesa legale.

## Changelog

Vedi [CHANGELOG.md](CHANGELOG.md).
