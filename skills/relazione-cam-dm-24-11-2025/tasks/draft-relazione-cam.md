# Task: Redazione guidata della Relazione CAM di progetto (bozza)

Guida dialogica per la redazione della Relazione CAM di progetto ai sensi del criterio 2.1.1 dell'Allegato 1 al DM MASE 24/11/2025, secondo il modello ufficiale MASE (versione 02/02/2026). Per ciascun criterio applicabile, chiede i dati al progettista e genera la Scheda Tipo corrispondente.

## Obiettivo

Produrre una **bozza strutturata della Relazione CAM di progetto** pronta per essere revisionata, integrata e firmata dal progettista, conforme alla struttura minima del modello MASE (fonte `modello-relazione-cam-2026.md`):

1. **Normativa** - quadro normativo e tecnico di riferimento
2. **Progetto** - strategia ambientale, descrizione, tabella di applicabilita' (Tabella 1), protocollo di sostenibilita', gruppo di lavoro, Schede Tipo per criterio, criteri premianti proposti
3. **Allegati** - elenco delle relazioni di approfondimento applicabili

## Input richiesti

Prima di iniziare, raccogliere (o riprendere dall'output di `identifica-criteri-applicabili.md` se gia' eseguito):

1. **Regime applicabile** confermato (DM 24/11/2025; se transitorio DM 256/2022, questo task non si applica: usare gli estratti [STORICO]).
2. **Livello di progettazione** (PFTE / esecutivo): la Relazione e' dovuta per **ogni livello**, con approfondimento "coerente con il livello di dettaglio degli elaborati progettuali" (modello MASE, par. 3.6).
3. **Descrizione del progetto**: committente, oggetto, localizzazione, tipologia di intervento (art. 3 DPR 380/2001), consistenza dimensionale, indagini preliminari, pareri degli enti (modello, par. 3.2).
4. **Tabella di applicabilita' dei criteri** (da `identifica-criteri-applicabili.md`) o dati per costruirla.
5. **Strategia ambientale**: e' previsto uno studio LCA (par. 1.3.2)? Se si': equivalente funzionale, moduli dichiarati, tre indicatori selezionati, GWPtotal; strategie di economia circolare (modello, par. 3.1).
6. **Protocollo di sostenibilita'** eventualmente adottato (LEED, BREEAM, ITACA, CasaClima, DGNB, HQE, ARCA, SB Tool, S.A.L.E. - par. 1.3.5) e mappatura crediti/criteri.
7. **Obblighi DNSH** (es. finanziamento PNRR) e altra documentazione ambientale obbligatoria correlata (relazione di sostenibilita' ex art. 11 allegato I.7 del Codice).
8. **Gruppo di lavoro**: nominativi, qualifiche, ruoli (modello, par. 3.5); per ogni criterio serve il **professionista referente** (Scheda Tipo).
9. **Criterio di aggiudicazione** e criteri premianti che si intende proporre per i lavori (modello, par. 3.7).

## Fonti normative

Leggere prima di procedere:

- `references/fonti/modello-relazione-cam-2026.md` - struttura vincolante di riferimento
- `references/estratti/dm-cam-2025-relazione-cam-struttura.md` - criterio 2.1.1 e modello
- `references/fonti/dm-cam-24-11-2025-allegato-1.md` - elenco criteri e regole di capitolo
- `references/estratti/dm-cam-2025-ambito-transitorio.md` - solo per confermare il regime

## Procedura

### Passo 1 - Intestazione e sezione Normativa

Genera l'intestazione e la sezione "Normativa" secondo il modello MASE:

---
**RELAZIONE CAM DI PROGETTO**
ai sensi del criterio 2.1.1 dell'Allegato 1 al DM MASE 24 novembre 2025 (GU n. 281 del 3/12/2025, in vigore dal 2/2/2026)

**Oggetto**: [descrizione intervento]
**Committente / Stazione appaltante**: [nome]
**Livello di progettazione**: [PFTE / esecutivo]
**Tipologia di intervento (art. 3 DPR 380/2001)**: [tipologia]
**Data**: [data redazione]

**1. NORMATIVA**

- Clausola contrattuale "2.1.1 Relazione CAM" dell'Allegato 1 al DM 24.11.2025;
- obbligo di applicazione dei CAM ex art. 57 co. 2 D.Lgs. 36/2023;
- [altri decreti CAM applicabili al progetto: verde pubblico, arredo urbano, ecc.];
- [normative ambientali specifiche: es. DNSH per interventi PNRR];
- [normativa tecnica dello studio LCA, se presente];
- [protocollo di sostenibilita' energetico-ambientale adottato, se presente].
---

### Passo 2 - Sezione Progetto

Genera nell'ordine (modello MASE, parr. 3.1-3.7):

1. **Strategia ambientale di progetto** (par. 3.1): approccio LCA (se presente) con equivalente funzionale, moduli dichiarati, tre indicatori e sintesi critica; **GWPtotal** sull'intero ciclo di vita (esclusi moduli D) per la Carbon Footprint dell'opera e il contributo agli obiettivi climatici ex art. 11 lett. c) allegato I.7 del Codice; strategie di economia circolare. Se lo studio LCA non e' previsto, ometti i punti LCA e segnala l'eventuale criterio premiante rinunciato (2.6.3).
2. **Descrizione del progetto** (par. 3.2): tipologia, consistenza, elaborati grafici richiamati, indagini, pareri (con riferimento puntuale agli elaborati).
3. **Applicabilita' dei criteri** (par. 3.3): Tabella 1 con le colonne del modello (criterio / applicabile / non applicabile / parzialmente applicabile / motivazione tecnica / criterio del protocollo applicato / criterio DNSH correlato).
4. **Protocollo di sostenibilita'** (par. 3.4): se adottato, illustra l'equivalenza requisito/verifica tra criteri CAM e crediti del protocollo; allega la documentazione del protocollo (par. 1.3.5).
5. **Gruppo di lavoro** (par. 3.5).
6. **Applicazione dei CAM - Schede Tipo** (par. 3.6): per ogni criterio applicato genera una scheda con i campi del modello:

```
[Numero e titolo del capitolo]
[Numero e titolo del criterio]
Applicato: [SI / NO / Parzialmente]
Referente: [professionista responsabile della verifica del criterio]
Obiettivi: [sintesi dei requisiti o obiettivi prestazionali del criterio]
Risultati: [come il progetto raggiunge l'obiettivo, con eventuali valori prestazionali in tabella]
Verifica: [mezzi di verifica adottati; per NO/Parzialmente: motivazioni tecniche giustificate]
Documentazione progettuale di riferimento: [titolo elaborato + pagina]
Protocollo di sostenibilita' energetico ambientale: [credito corrispondente, se usato, con argomentazione di equivalenza]
DNSH, Relazione di sostenibilita': [obiettivo DNSH dimostrabile col criterio; integrazioni con la relazione ex art. 11 allegato I.7]
```

   Regole:
   - il contenuto dei campi "Obiettivi/Risultati/Verifica" deve basarsi sul **testo integrale del criterio nel PDF ufficiale dell'Allegato 1**: la skill non lo riproduce; chiedi all'utente i dati e, dove il testo del criterio non e' stato letto, marca "[DA COMPLETARE dal testo del criterio X.Y.Z - PDF Allegato 1]";
   - per i criteri che prevedono attivita' in collaudo/gestione, descrivere modalita' di attuazione del piano di manutenzione concordate con la SA, con responsabilita' e tempistiche (par. 3.6);
   - mezzi di prova: mai accettare "certificazioni CAM" di prodotto (par. 1.3.5); indica etichette/certificati/rapporti di prova previsti dalla "verifica" del criterio.

7. **Criteri premianti** (par. 3.7): proposta motivata dei premianti per i lavori (cap. 3.2) a supporto della SA, anche sulla base degli obiettivi del DIP.

### Passo 3 - Sezione Allegati

Elenca gli allegati applicabili al progetto (modello, par. 4): rapporto LCA (1.3.2); rapporto sullo stato dell'ambiente (2.2.9); piano ambientale di cantiere (2.5.1); piano di manutenzione dell'opera (2.3.16); piano di verifica degli interventi di risanamento; piano di decostruzione e demolizione selettiva a fine vita (2.3.17); piano di riutilizzo, riciclo e recupero dei rifiuti da C&D (2.5.4); protocollo per la misura e verifica dei risparmi. Per ciascuno: previsto/non applicabile, chi lo redige, stato.

### Passo 4 - Conclusioni

1. Nota sul livello di progettazione: la Relazione va aggiornata **ad ogni livello successivo** (criterio 2.1.1: "per tutte le fasi di progettazione").
2. Richiamo ai mezzi di prova che l'esecutore dovra' presentare alla DL (criterio 2.1.2), da riportare nel capitolato speciale del progetto esecutivo.
3. Elenco degli elementi **non verificabili dalla skill** (dati prestazionali, prove, certificazioni di prodotto, studio LCA).
4. Rinvio a revisione e **firma del progettista**.

## Output

Documento strutturato in markdown (titoli ##, tabelle, testo formale in italiano) con: intestazione + sezione Normativa; sezione Progetto (strategia, descrizione, Tabella 1, protocollo, gruppo di lavoro, Schede Tipo, premianti); sezione Allegati; conclusioni.

## Limiti

- La bozza e' un supporto alla redazione: non sostituisce la verifica tecnica del progettista firmatario.
- I contenuti prestazionali delle Schede Tipo dipendono dal testo integrale dei singoli criteri (PDF ufficiale): dove non trascritto, la skill lascia segnaposto espliciti, mai valori inventati.
- Non produce i documenti allegati (rapporto LCA, piani di cantiere/manutenzione/demolizione): ne indica solo collocazione e criterio di riferimento.
- Non verifica la coerenza interna fra le scelte dei diversi criteri.
