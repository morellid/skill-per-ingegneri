# Output atteso - Valutazione perimetro PMI manifattura

## Valutazione perimetro NIS2 - COMPONENTECNICA S.r.l.

**Data valutazione**: 2026-04-29

### Esito orientativo

**SOGGETTO IMPORTANTE** ai sensi dell'art. 6 co. 3 D.Lgs. 138/2024 (in ambito ex art. 3 ma non rientra nelle categorie essenziali di art. 6 co. 1).

### Motivazione

#### Settori applicabili

- **Allegato II - Settore 5 Fabbricazione - Sottosettore b) Fabbricazione di computer, prodotti di elettronica e ottica**:
  - Soggetto rientra in: "Imprese che svolgono attivita' economiche di cui alla sezione C, divisione 26, della NACE Rev. 2"
  - Codice ATECO 26.11 corrisponde a NACE 26.11 = "Manufacture of electronic components and boards" -> rientra nella divisione 26 NACE.

#### Size-cap rule (art. 3 co. 2)

- Occupati: **205** > 50 (massimale piccole imprese) -> e' una **media impresa**
- Fatturato: 42M EUR > 10M -> conferma media
- Bilancio: 35M EUR > 10M -> conferma media

L'organizzazione **supera i massimali per le piccole imprese** della Raccomandazione 2003/361/CE -> **e' in ambito** NIS2 (art. 3 co. 2).

#### Verifica essenziale (art. 6 co. 1)

- **Lett. a)**: il soggetto e' in **Allegato II**, non Allegato I -> non puo' essere essenziale via lett. a).
- **Lett. b)**: non identificato come soggetto critico ex Dir. 2022/2557.
- **Lett. c)**: non e' fornitore reti/servizi comunicazione elettronica.
- **Lett. d)**: non e' prestatore servizi fiduciari ne' gestore TLD/DNS.
- **Lett. e)**: non e' PA centrale.

Quindi: **NON essenziale** -> **soggetto importante** (art. 6 co. 3).

#### Note dimensionali

Attenzione: il calcolo dimensionale per gruppi/imprese collegate (art. 6 par. 2 dell'Allegato Racc. 2003/361/CE) puo' richiedere il consolidamento con la sede slovacca se questa e' parte dello stesso gruppo o associata. La presenza di 25 dipendenti aggiuntivi e' gia' inclusa nel totale 205. Verificare con commercialista per il consolidamento corretto se ci sono altre societa' del gruppo.

### Obblighi conseguenti (sintesi)

| Obbligo | Riferimento | Termine |
|---------|-------------|---------|
| Registrazione su piattaforma ACN | art. 7 co. 1 | finestra 1 gen - 28 feb (T+0 alla prossima finestra) |
| Designazione punto di contatto NIS + sostituto | art. 7 co. 1 lett. c, co. 4 lett. d | T+0 e finestra apr-mag |
| Approvazione modalita' di implementazione misure dal CdA / AU | art. 23 co. 1 lett. a | T+3-6 mesi |
| Adozione misure tecniche/operative/organizzative | art. 24 co. 2 | T+18 mesi dalla notifica ACN, comunque entro **31/10/2026** |
| Formazione organi + dipendenti | art. 23 co. 2 | T+6-12 mesi |
| Notifica incidenti significativi | art. 25 | T+9 mesi dalla notifica ACN |
| Sanzioni in caso di violazione | art. 38 co. 9 lett. b | fino a **max(7M EUR; 1,4% fatturato annuo mondiale)** = max(7M; 588k) = **7M EUR** in questo caso. Minimo edittale 1/30 = 233k EUR |

### Sovrapposizione con TISAX (note di esperienza, non normative)

> Le seguenti considerazioni sono note di esperienza di dominio. La skill non cataloga TISAX come fonte normativa primaria; per i dettagli verificare direttamente con il cliente automotive che richiede l'audit.

- TISAX (Trusted Information Security Assessment eXchange) e' uno **schema di assessment di settore automotive** richiesto contrattualmente da OEM e Tier 1.
- NIS2 e' un **obbligo di legge** indipendente dai contratti.
- I due regimi sono parzialmente sovrapposti: chi e' conforme a TISAX (livello AL3 tipico per Tier 2 con dati riservati cliente) ha gia' molte misure ANCHE utili per la conformita' NIS2.
- La mappatura puntuale TISAX -> Det. ACN richiede analisi specifica e va effettuata caso per caso.

Raccomandazione: implementare TISAX in modo che soddisfi anche i requisiti NIS2 minimi (approccio "do-it-once") e' una scelta di efficienza operativa, da valutare con il consulente.

---

## Gap analysis sintetica - principali gap rilevati

| Funzione | Sottocategoria | Stato | Priorita' |
|----------|-----------------|-------|-----------|
| GOVERN | GV.PO-01 (16 ambiti politiche) | Liv. 1 (2 politiche su 16, vecchie) | **ALTA** |
| GOVERN | GV.RR-02 (organizzazione cyber approvata) | Liv. 0 | **ALTA** |
| GOVERN | GV.SC (supply chain) | Liv. 0 | ALTA |
| IDENTIFY | ID.AM-01/02/03 (inventari + flussi) | Liv. 1 | MEDIA |
| IDENTIFY | ID.RA-05 (risk assessment) | Liv. 0 | ALTA |
| PROTECT | PR.AA-03 (MFA) | Liv. 1 (solo VPN) | ALTA |
| PROTECT | PR.AT-01 (awareness) | Liv. 1 (corso 2022 mai ripetuto) | ALTA |
| PROTECT | PR.DS-11 (test backup) | Liv. 1 (test 2 anni fa) | ALTA |
| DETECT | DE.CM-01 (SOC/SIEM) | Liv. 0 | ALTA |
| RESPOND | RS.MA-01 (piano IR) | Liv. 0 | **ALTA** |
| RESPOND | RS.CO-02 (notifica CSIRT) | Liv. 0 | **ALTA** |
| RECOVER | RC.RP-01 | Liv. 1 | MEDIA |

### Situazione critica

L'organizzazione e' a livello molto basso su tutti i 10 elementi minimi art. 24 co. 2. Lo sforzo di adeguamento e' significativo per una PMI senza CISO interno.

### Roadmap proposta

**Quick wins (0-3 mesi)**:
1. Registrazione su piattaforma ACN
2. Atto formale dell'AU di approvazione di un primo set minimo di politiche cyber
3. Affidamento a MSSP italiano per SOC managed (setup di SIEM cloud-based)
4. Implementazione MFA per accessi a ERP, file server, AD admin

**Medio termine (3-9 mesi)**:
5. Risk assessment completo + classificazione asset
6. 16 politiche di sicurezza GV.PO-01 (template di settore + adattamento)
7. Procedura formale di IR + notifica al CSIRT Italia
8. Awareness program + simulazioni phishing
9. Backup test trimestrale + DR plan documentato
10. TPRM base sui fornitori critici (es. fornitore SAP)

**Lungo termine (9-18 mesi dalla comunicazione di inserimento ACN)**:
11. Implementazione TISAX (se richiesto dai clienti) come progetto integrato con NIS2
12. Vulnerability management strutturato
13. SDLC sicuro per software interno (PLM, integrazioni)
14. Piena conformita' Det. ACN 379907/2025 Allegato 1 (importanti, 37 sottocategorie)

> Nota: il termine 18 mesi decorre dalla **comunicazione personale di inserimento** sulla piattaforma ACN (art. 3 co. 1 Det. 379907/2025), non da una data assoluta.

### Risorse necessarie

- **CISO/responsabile cyber**: per organizzazioni di queste dimensioni e in ambito NIS2 e' opportuno valutare l'assunzione (anche part-time) o l'affidamento a un vCISO esterno. Affidare la responsabilita' cyber a un solo IT manager senza supporto specialistico e' tipicamente fragile.
- **Budget di adeguamento**: la skill non fornisce stime di mercato. Le quotazioni per consulenza, tooling e servizi MSSP variano per area geografica, livello di MSSP e maturita' iniziale del soggetto. Richiedere preventivi specifici a operatori di mercato.

### Esposizione sanzionatoria

- **Sanzione max** ex art. 38 co. 9 lett. b) per violazioni artt. 23, 24, 25: fino al **maggiore tra 7M EUR e 1,4% del fatturato annuo mondiale**. Per 42M EUR di fatturato: 1,4% = 588.000 EUR; il maggiore tra 7M e 588k e' **7M EUR**. Quindi cap operativo = **7M EUR**.
- **Sanzione minima edittale**: 1/30 del massimo edittale = **233.333 EUR**.

---

## Rinvio

Output orientativo. Per una PMI senza CISO interno e' fortemente raccomandato avvalersi di un consulente cybersecurity con esperienza NIS2 per coordinare l'adeguamento. La sovrapposizione con TISAX richiede pianificazione integrata. La consulenza legale e' opportuna per valutare le clausole con i clienti (es. Marelli) che fanno riferimento a NIS2.
