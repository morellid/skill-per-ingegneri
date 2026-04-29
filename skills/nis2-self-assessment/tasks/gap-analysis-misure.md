# Task: Gap analysis misure di base NIS2 (D.Lgs. 138/2024 art. 24 + Det. ACN 379907/2025)

Confronta le misure di sicurezza informatica gia' adottate dall'organizzazione con i 10 elementi minimi dell'art. 24 co. 2 D.Lgs. 138/2024 e con le sottocategorie del Framework Nazionale Cybersecurity (ed. 2025) richiamate dalla Determinazione ACN 379907/2025 (Allegato 1 per importanti = 37 sottocategorie / 87 requisiti; Allegato 2 per essenziali = 43 sottocategorie / 112 requisiti). La Det. 379907/2025 e' vigente dal 15/01/2026 e sostituisce la precedente Det. 164179/2025.

## Pre-requisito

Il task `valuta-perimetro` deve essere stato eseguito. La gap analysis ha senso solo se il soggetto e' in ambito (essenziale o importante). Altrimenti la skill suggerisce di non procedere.

## Obiettivo

Produrre una **gap analysis strutturata** per le 6 funzioni del Framework Nazionale Cybersecurity (GOVERN, IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER), con livello di copertura per ciascuna sottocategoria e con la lista dei gap prioritari.

L'output deve consentire di pianificare un **roadmap** di adeguamento entro le scadenze ACN (in particolare 31/10/2026 per la piena operativita' delle misure di base ex Det. 379907/2025).

## Input richiesti

- **Classificazione del soggetto** (essenziale / importante) - ricavata dal task `valuta-perimetro`.
- **Settore di attivita' principale** - per identificare specificita' settoriali (es. settori 3-4 Allegato I = DORA prevale, settore 8 = potenziale Reg. UE 2024/2690).
- **Stato attuale delle misure**, articolato per sottocategoria. La skill fornisce un questionario con riferimenti alle sottocategorie.
- **Documentazione disponibile**: politiche di sicurezza, procedure, registri di asset, report di vulnerability assessment, contratti con fornitori, piani BCM/DR, linee guida HR per il personale, policy MFA, ecc.
- **Certificazioni in essere** (ISO/IEC 27001, ISO 22301, SOC 2, ecc.) - utili per il mapping ma non sostituiscono la conformita' NIS2.

## Fonti

Leggere prima:
- `references/estratti/dlgs-138-2024-misure-art23.md` - art. 23 (governance) + art. 24 (misure)
- `references/estratti/acn-misure-base-essenziali.md` - struttura Allegato 2 ACN
- `references/estratti/acn-misure-base-importanti.md` - struttura Allegato 1 ACN
- `references/estratti/reg-ese-2024-2690-ambito.md` - per soggetti coperti dal Reg. UE 2024/2690

## Procedura

### Passo 1 - Determinare il riferimento applicabile

In base al settore e alla classificazione:

| Caso | Riferimento operativo |
|------|------------------------|
| Soggetto in settore Allegato I 8 (Infrastrutture digitali) - DNS/cloud/data center/CDN/serv. fiduciari | **Reg. UE 2024/2690** (diretto) + ENISA technical guidance |
| Soggetto in settore Allegato II 6 (mercati online, motori di ricerca, social, registrar) | **Reg. UE 2024/2690** + Det. ACN |
| Soggetto in altri settori Allegati I-IV | **Det. ACN 379907/2025** (Allegato 1 importanti / Allegato 2 essenziali) |
| Soggetto in settori 3-4 Allegato I (banche/mercati finanziari) DORA-eligible | **DORA Reg. UE 2022/2554** (Capi IV-V NIS2 esclusi - art. 3 co. 14) |

Per la maggior parte dei soggetti italiani il riferimento e' la Determinazione ACN.

### Passo 2 - Questionario per ciascuna funzione

Per ciascuna delle 6 funzioni del Framework Nazionale Cybersecurity (ed. 2025), valutare lo stato di copertura.

> **Nota metodologica importante**: la Determinazione ACN 379907/2025 NON definisce livelli di maturita' numerici. I requisiti di ciascuna sottocategoria devono essere "implementati" o non implementati, e il rispetto si misura sulla presenza dei singoli requisiti puntuali elencati nell'Allegato 1 (importanti) o Allegato 2 (essenziali) della determinazione.
>
> La scala di maturita' 0-4 di seguito proposta e' una **rubric interna non normativa**, utile come strumento di self-assessment per pianificare il roadmap. Il livello 3 corrisponde a una pratica sistematica documentata; non equivale automaticamente alla conformita' formale ai requisiti ACN, che va verificata requisito per requisito. Il giudizio finale di conformita' va espresso confrontando ciascun requisito ACN con le evidenze disponibili.

Scala di maturita' interna proposta (rubric, 0-4):

- **0 - Assente**: nessuna misura.
- **1 - Iniziale**: esistono pratiche informali, non documentate.
- **2 - Documentato**: politica/procedura formalizzata, ma applicazione disomogenea.
- **3 - Implementato**: misura applicata sistematicamente con monitoraggio. (Indicatore di candidata conformita' ai requisiti ACN, da verificare puntualmente.)
- **4 - Ottimizzato**: misura applicata, monitorata, riesaminata, integrata in metriche di rischio.

#### 1. GOVERNO (GOVERN)

| Sottocategoria | Domanda chiave | Livello (0-4) | Evidenza disponibile? |
|----------------|----------------|----------------|------------------------|
| GV.OC-04 | E' mantenuto un elenco aggiornato dei sistemi informativi e di rete rilevanti? | | |
| GV.RM-03 | Esiste un piano di gestione dei rischi cyber documentato e parte dei processi aziendali? | | |
| GV.RR-02 | L'organizzazione di sicurezza informatica e' definita, approvata dal CdA, riesaminata almeno biennalmente? | | |
| GV.RR-04 | Vetting del personale autorizzato? Clausole contrattuali post-cessazione? | | |
| GV.PO-01 | Sono adottate politiche per i 16 ambiti obbligatori (gestione rischio, ruoli, HR, audit, supply chain, asset, vuln., BCM/DR/crisi, IAM, fisica, formazione, dati, SDLC, reti, monitoring, IR/recovery)? Politiche approvate dal CdA? | | |
| GV.PO-02 | Politiche revisionate e aggiornate? | | |
| GV.SC-01 | Programma supply chain risk management (SCRM)? | | |
| GV.SC-02 | Ruoli/responsabilita' cyber per fornitori, clienti, partner? | | |
| GV.SC-04 | Fornitori prioritizzati per criticita'? | | |
| GV.SC-05 | Requisiti contrattuali cyber per fornitori? | | |
| GV.SC-07 | Rischi da terze parti compresi e monitorati? | | |

#### 2. IDENTIFICAZIONE (IDENTIFY)

| Sottocategoria | Domanda chiave | Livello (0-4) | Evidenza |
|----------------|----------------|----------------|----------|
| ID.AM-01 | Inventario hardware aggiornato? | | |
| ID.AM-02 | Inventario software/servizi/sistemi? | | |
| ID.AM-03 | Mappa flussi di rete e flussi dati? | | |
| ID.AM-04 | Inventario servizi di fornitori esterni? | | |
| ID.RA-01 | Vulnerability assessment regolare? | | |
| ID.RA-05 | Risk assessment con minacce/vuln./prob./impatti? | | |
| ID.RA-06 | Risposta al rischio prioritizzata e monitorata? | | |
| ID.RA-08 | Vulnerability disclosure policy? Processo coordinato di gestione vuln. esterne? | | |
| ID.IM-01 | Lessons learned dalle valutazioni recepiti come miglioramenti? | | |
| ID.IM-04 | Piani di IR e altri piani cyber aggiornati e testati? | | |

#### 3. PROTEZIONE (PROTECT)

| Sottocategoria | Domanda chiave | Livello (0-4) | Evidenza |
|----------------|----------------|----------------|----------|
| PR.AA-01 | IAM con identita' utenti/servizi/HW gestite? | | |
| PR.AA-03 | MFA per accessi privilegiati e remoti? | | |
| PR.AA-05 | Policy di permessi/diritti, least privilege, separazione compiti? | | |
| PR.AA-06 | Controllo accesso fisico agli asset? | | |
| PR.AT-01 | Programma awareness annuale per tutto il personale? | | |
| PR.AT-02 | Formazione specialistica per ruoli IT/sicurezza? | | |
| PR.DS-01 | Crittografia dei dati at-rest (almeno per dati sensibili)? | | |
| PR.DS-02 | Crittografia dei dati in transit (TLS, VPN)? | | |
| PR.DS-11 | Backup creati, protetti, mantenuti, verificati (test di restore)? | | |
| PR.PS-01 | Configuration management baseline applicate? | | |
| PR.PS-02 | Patch management software? | | |
| PR.PS-03 | Hardware lifecycle gestito? | | |
| PR.PS-04 | Logging centralizzato e disponibile per monitoraggio? | | |
| PR.PS-06 | Sviluppo sicuro (SSDLC) per software interno? | | |
| PR.IR-01 | Segmentazione rete + protezione perimetrale (FW/IPS)? | | |
| PR.IR-03 | Resilienza in situazioni avverse (alta disponibilita', failover)? | | |

#### 4. RILEVAMENTO (DETECT)

| Sottocategoria | Domanda chiave | Livello (0-4) | Evidenza |
|----------------|----------------|----------------|----------|
| DE.CM-01 | SIEM o monitoraggio reti/servizi attivo? | | |
| DE.CM-09 | Monitoraggio HW/SW di elaborazione, ambienti runtime? | | |

#### 5. RISPOSTA (RESPOND)

| Sottocategoria | Domanda chiave | Livello (0-4) | Evidenza |
|----------------|----------------|----------------|----------|
| RS.MA-01 | Piano IR con coordinamento terze parti (es. CSIRT, fornitori)? | | |
| RS.CO-02 | Procedure di notifica al CSIRT Italia (24h pre-notif / 72h notif) e ai destinatari? | | |

#### 6. RIPRISTINO (RECOVER)

| Sottocategoria | Domanda chiave | Livello (0-4) | Evidenza |
|----------------|----------------|----------------|----------|
| RC.RP-01 | Piano di ripristino eseguito coerentemente? | | |
| RC.CO-03 | Comunicazione di ripristino agli stakeholder? | | |

### Passo 3 - Identificazione gap prioritari

Per ciascun gap (livello < 3), assegnare:

- **Priorita'**:
  - **Alta** se la sottocategoria mappa direttamente a un elemento minimo art. 24 co. 2 D.Lgs. 138/2024 (a-l)
  - **Alta** se relativa a notifica incidenti (RS.CO-02) o backup (PR.DS-11) o IAM (PR.AA-03)
  - **Media** per altre sottocategorie
- **Effort stimato**: in giorni-uomo o complessita' (S/M/L).
- **Owner proposto**: CISO, IT, Risk, HR, Legal, Procurement.
- **Scadenza target**: in base alla notifica ACN ricevuta dal soggetto + 18 mesi (o 31/10/2026 se non ancora ricevuta).

### Passo 4 - Confronto con elementi minimi art. 24 co. 2

Verificare la mappatura ai 10 elementi minimi del decreto:

| Lett. art. 24 co. 2 | Ambito | Sottocategorie collegate | Copertura attuale | Gap prioritario? |
|---------------------|--------|---------------------------|--------------------|------------------|
| a | Politiche analisi rischi e sicurezza ICT | GV.RM, ID.RA, GV.PO | | |
| b | Gestione incidenti e notifiche | RS.MA-01, RS.CO-02, ID.IM-04 | | |
| c | Continuita' operativa | RC.RP, RC.CO, PR.DS-11, PR.IR-03 | | |
| d | Sicurezza catena di approvvigionamento | GV.SC (tutte) | | |
| e | SDLC + vuln. disclosure | PR.PS-01..06, ID.RA-08 | | |
| f | Valutazione efficacia | ID.IM-01, GV.RM-03 | | |
| g | Igiene cyber e formazione | PR.AT-01, PR.AT-02 | | |
| h | Crittografia / cifratura | PR.DS-01, PR.DS-02 | | |
| i | Sicurezza personale, accessi, asset | GV.RR-04, PR.AA, ID.AM, PR.AA-06 | | |
| l | MFA, comunicazioni protette | PR.AA-03, PR.IR-01 | | |

Se uno dei 10 ambiti e' a livello < 3 con politica non documentata: e' un **rischio sanzionatorio diretto** (art. 38 co. 8 lett. a richiama l'art. 24 sostanziale).

### Passo 5 - Sintesi e output

```markdown
# Gap analysis NIS2 - [nome organizzazione]

**Data valutazione**: [data]
**Organizzazione**: [...]
**Classificazione NIS2**: [Essenziale | Importante]
**Riferimento operativo**: [Det. ACN 379907/2025 Allegato 1 (importanti, 37 sottocat / 87 requisiti) | Allegato 2 (essenziali, 43 sottocat / 112 requisiti) | Reg. UE 2024/2690 | DORA]

## Summary

> Totali sottocategorie: 43 per soggetti essenziali (Allegato 2), 37 per soggetti importanti (Allegato 1). Riempire le righe pertinenti alla classificazione del soggetto.

Per **soggetti essenziali** (Allegato 2 - 43 sottocategorie, 112 requisiti):

| Funzione | Sottocategorie totali | A livello >= 3 | Gap rilevati |
|----------|------------------------|-----------------|--------------|
| GOVERN | 11 | [N] | [N] |
| IDENTIFY | 10 | [N] | [N] |
| PROTECT | 16 | [N] | [N] |
| DETECT | 2 | [N] | [N] |
| RESPOND | 2 | [N] | [N] |
| RECOVER | 2 | [N] | [N] |
| **TOTALE** | **43** | **[N]** | **[N]** |

Per **soggetti importanti** (Allegato 1 - 37 sottocategorie, 87 requisiti):

| Funzione | Sottocategorie totali | A livello >= 3 | Gap rilevati |
|----------|------------------------|-----------------|--------------|
| GOVERN | 11 | [N] | [N] |
| IDENTIFY | 9 | [N] | [N] |
| PROTECT | 11 | [N] | [N] |
| DETECT | 2 | [N] | [N] |
| RESPOND | 2 | [N] | [N] |
| RECOVER | 1 | [N] | [N] |
| **TOTALE** | **37** | **[N]** | **[N]** |

## Gap prioritari (ordinati per priorita')

| ID | Sottocategoria | Descrizione gap | Priorita' | Effort | Owner | Scadenza |
|----|-----------------|------------------|-----------|--------|-------|----------|
| 1 | GV.PO-01 | Politiche cyber non approvate dal CdA | Alta | M | CISO + Legal | T+3 mesi |
| 2 | RS.CO-02 | Procedura notifica al CSIRT Italia non formalizzata | Alta | S | CISO | T+1 mese |
| ... | ... | ... | ... | ... | ... | ... |

## Mappatura art. 24 co. 2 - copertura

| Elemento art. 24 | Stato | Gap prioritario? |
|-------------------|-------|------------------|
| a) Politiche analisi rischi | [conforme / parziale / non conforme] | [SI/NO] |
| b) Gestione incidenti | | |
| ... | | |

## Roadmap proposta

### Quick wins (0-3 mesi)
- [...]

### Medio termine (3-9 mesi)
- [...]

### Lungo termine (9-18 mesi - completare entro 31/10/2026)
- [...]

## Note di settore

[Per soggetti settori 8-9 Allegato I: rinvio a Reg. UE 2024/2690 + ENISA guidance.]
[Per soggetti settori 3-4 Allegato I: rinvio a DORA.]
[Per PA Allegato III: cross-check con linee guida AgID e Legge 90/2024.]

## Limiti di questa gap analysis

- E' una valutazione orientativa basata sulle informazioni fornite. Una verifica documentale o un audit sul campo possono modificare l'esito.
- I requisiti puntuali della Det. ACN 379907/2025 sono dettagliati con criteri specifici (frequenze, evidenze, attori) che richiedono lettura del testo verbatim.
- La conformita' alla Det. ACN non implica automaticamente conformita' a regolamenti settoriali (DORA, codice comunicazioni elettroniche).

## Rinvio al CISO / consulente cyber

L'output e' di supporto. Le decisioni operative su prioritizzazione, effort, scadenze e proprieta' degli interventi richiedono il giudizio di CISO, comitato sicurezza, consulente cyber o auditor terzo. **Sanzioni amministrative ex art. 38 D.Lgs. 138/2024**: fino a 10M EUR / 2% fatturato (essenziali) o 7M EUR / 1.4% (importanti) per violazioni dell'art. 24.
```

## Limiti di questo task

- Non sostituisce un audit ISO/IEC 27001 ne' una verifica di conformita' su misurazione effettiva delle misure.
- Non produce evidenze documentali ne' dossier per ispezione ACN.
- Le sottocategorie elencate riflettono la struttura della Det. 379907/2025 (vigente dal 15/01/2026). Per il dettaglio dei requisiti puntuali consultare il testo verbatim degli Allegati 1/2 in `not_in_repo/`.

## Esempi

Vedi `examples/`:
- `essenziale-utility-energia/` - gap analysis tipo per utility con SOC interno
