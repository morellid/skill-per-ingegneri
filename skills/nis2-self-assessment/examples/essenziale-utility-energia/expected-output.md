# Output atteso - Valutazione perimetro + sintesi gap

## 1. Valutazione perimetro NIS2 - ENERGOSPA S.p.A.

**Data valutazione**: 2026-04-29
**Compilato da**: simulazione skill nis2-self-assessment v0.1.0-alpha

### Esito orientativo

**SOGGETTO ESSENZIALE** ai sensi dell'art. 6 co. 1 lett. a) D.Lgs. 138/2024.

### Motivazione

#### Settori applicabili

- **Allegato I - Settore 1 Energia - Sottosettore a) Energia elettrica**:
  - Soggetto rientra in: "Gestori del sistema di distribuzione quali definiti all'articolo 2, punto 29), della direttiva (UE) 2019/944" (DSO)
  - Soggetto rientra anche in: "Produttori quali definiti all'articolo 2, punto 38), della direttiva (UE) 2019/944" (per gli impianti rinnovabili)

#### Size-cap rule (art. 3 co. 2 e art. 6 co. 1 lett. a)

- Occupati: **1.450** > 250 (massimale medie imprese) -> e' una **grande impresa**
- Fatturato: **380M EUR** > 50M -> conferma grande impresa
- Bilancio: **720M EUR** > 43M -> conferma grande impresa

L'organizzazione **supera i massimali per le medie imprese** della Raccomandazione 2003/361/CE. Quindi, ai sensi dell'art. 6 co. 1 lett. a), e' **soggetto essenziale**.

#### Applicazione indipendente dalle dimensioni

Non rilevante per la classificazione (gia' essenziale via dimensione + settore Allegato I).

### Obblighi conseguenti (sintesi)

| Obbligo | Riferimento | Termine |
|---------|-------------|---------|
| Registrazione su piattaforma ACN | art. 7 co. 1 | finestra 1 gen - 28 feb (T+0 alla prossima finestra) |
| Designazione punto di contatto NIS + sostituto | art. 7 co. 1 lett. c, co. 4 lett. d | T+0 e T+aggiornamento finestra apr-mag |
| Approvazione modalita' di implementazione misure dal CdA | art. 23 co. 1 lett. a | T+3-6 mesi (priorita' alta) |
| Adozione misure tecniche/operative/organizzative (10 elementi) | art. 24 co. 2 | T+18 mesi dalla notifica ACN, comunque entro **31/10/2026** |
| Formazione CdA + dipendenti | art. 23 co. 2 | T+6-12 mesi |
| Notifica incidenti significativi | art. 25 | T+9 mesi dalla notifica ACN |
| Sanzioni in caso di violazione | art. 38 co. 9 lett. a | fino a **max(10M EUR; 2% fatturato annuo mondiale)** = max(10M; 7,6M) = **10M EUR** in questo caso. Minimo edittale 1/20 = 500k EUR |

### Rinvio

La presente valutazione e' di supporto. La registrazione su piattaforma ACN spetta al soggetto sotto la propria responsabilita' (art. 7). Si raccomanda consulenza di legale specializzato cyber + CISO per finalizzare la classificazione.

---

## 2. Gap analysis sintetica - principali gap rilevati

| Funzione | Sottocategoria | Stato | Priorita' |
|----------|-----------------|-------|-----------|
| GOVERN | GV.PO-01 (politiche approvate dal CdA) | Liv. 2 (approvate dal management, non dal CdA) | **ALTA** - violazione diretta art. 23 co. 1 lett. a |
| GOVERN | GV.SC (supply chain risk management) | Liv. 1 (clausole base, no TPRM) | ALTA - art. 24 co. 2 lett. d |
| GOVERN | GV.RR-02 (organizzazione cyber approvata dal CdA) | Liv. 2 | ALTA |
| PROTECT | PR.AA-03 (MFA portale clienti) | Liv. 2 (parziale) | MEDIA |
| RESPOND | RS.CO-02 (procedura notifica al CSIRT Italia) | Liv. 0 | **ALTA** - viola art. 25 + art. 24 co. 2 lett. b |
| GOVERN | Formazione CdA cyber | Liv. 0 | **ALTA** - viola art. 23 co. 2 lett. a |
| RECOVER | RC.RP-01 (test di restore frequente) | Liv. 2 (1 test/anno) | MEDIA |

### Roadmap proposta

**Quick wins (0-3 mesi)**:
1. Registrazione su piattaforma ACN nella prima finestra utile + designazione punto di contatto
2. Delibera CdA: approvazione politiche cyber esistenti (formalizzazione)
3. Procedura formale di notifica al CSIRT Italia (skeleton + responsabili + canale)
4. Pianificazione formazione cyber CdA (anche un primo briefing entro T+3 mesi)

**Medio termine (3-9 mesi)**:
5. Programma TPRM strutturato (GV.SC) - prioritizzazione fornitori critici, clausole estese, audit
6. Estensione MFA al portale clienti
7. Aumento frequenza test di restore (almeno semestrale)
8. Reporting trimestrale CdA su stato cyber, incidenti, gap residui

**Lungo termine (9-18 mesi - entro 31/10/2026)**:
9. Allineamento ISMS ISO 27001 con copertura completa dei 16 ambiti GV.PO-01
10. Mappatura completa requisiti Det. ACN 379907/2025 -> evidenze documentali per ispezione
11. Esercitazione di crisi cyber con CdA (table-top con scenario ransomware su SCADA)

---

## 3. Obblighi governance - sintesi

| Area | Stato | Azione |
|------|-------|--------|
| Approvazione misure (art. 23 co. 1 lett. a) | NON CONFORME (politiche approvate dal management, non dal CdA) | Delibera CdA entro T+3 mesi |
| Sovrintendenza implementazione (art. 23 co. 1 lett. b) | PARZIALE (Comitato sicurezza ICT non riporta al CdA) | Istituire reporting trimestrale CISO -> CdA |
| Consapevolezza responsabilita' (art. 23 co. 1 lett. c) | DA VERIFICARE | Briefing legale al CdA su responsabilita' personale art. 38 co. 5-6 |
| Formazione CdA (art. 23 co. 2 lett. a) | NON CONFORME | Programma annuale entro T+6 mesi |
| Formazione dipendenti (art. 23 co. 2 lett. b) | CONFORME | Mantenere e ampliare con simulazioni |
| Informazione incidenti (art. 23 co. 3) | NON FORMALIZZATA | Procedura escalation + reporting trimestrale |

### Esposizione sanzionatoria

- **Sanzione max** ex art. 38 co. 9 lett. a) per violazione artt. 23, 24, 25: fino al **maggiore tra 10M EUR e 2% del fatturato annuo mondiale**. Per 380M EUR di fatturato: 2% = 7,6M EUR; il maggiore tra 10M e 7,6M e' **10M EUR**. Quindi cap operativo = **10M EUR**. Minimo edittale = 1/20 del massimo = 500.000 EUR.
- **Sanzione accessoria** ex art. 38 co. 6: incapacita' a svolgere funzioni dirigenziali per i membri del CdA in caso di mancata ottemperanza alla diffida.

---

## Avvertenza

Output orientativo. Le decisioni di registrazione, classificazione, notifica e implementazione misure spettano al titolare con la consulenza del CISO, di legale specializzato cyber e del responsabile compliance. Verificare il testo aggiornato della Determinazione ACN vigente sul portale `acn.gov.it/portale/en/nis/modalita-specifiche-base` prima di procedere con dettagli di requisiti specifici.
