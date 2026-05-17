# Task: Elenco dei fornitori rilevanti NIS (art. 18 Det. ACN 127437/2026)

Identifica i fornitori "rilevanti NIS" del soggetto e prepara l'elenco da comunicare all'ACN tramite il "Servizio NIS/Aggiornamento annuale informazioni" entro la finestra annuale **15 aprile - 31 maggio**.

## Pre-requisito

Il soggetto deve essere in ambito NIS (esito "essenziale" o "importante" del task `valuta-perimetro`) ed essere gia' iscritto sulla piattaforma ACN ai sensi dell'art. 7 D.Lgs. 138/2024.

L'obbligo si applica a **tutti i soggetti NIS** (essenziali e importanti), ad eccezione delle entita' finanziarie DORA solo per gli obblighi specifici dell'art. 16 co. 3 lett. b) e dell'art. 17 della Det. 127437/2026 (organi di amministrazione): **l'esenzione DORA NON copre l'art. 18 sui fornitori rilevanti**. I soggetti DORA-NIS devono quindi comunque elencare i fornitori rilevanti.

## Obiettivo

Produrre la tabella dei fornitori rilevanti NIS pronta per il caricamento sulla piattaforma ACN, con i 5 campi obbligatori per ciascun fornitore (denominazione, codice fiscale, Paese sede legale, codici CPV, criterio di rilevanza applicato).

## Fonti

Leggere prima:
- `references/estratti/acn-det-127437-2026-art18-fornitori.md` - art. 1 lett. ll), art. 16 co. 1, art. 16 co. 3 lett. g), art. 18, art. 24 co. 3
- `references/estratti/dlgs-138-2024-allegati-i-iv.md` - Allegato I punti 8 e 9 (per il criterio 1)

## Input richiesti

- **Elenco completo dei fornitori** del soggetto NIS: fornitori IT/ICT, fornitori di servizi gestiti, fornitori di servizi cloud, fornitori di servizi di telecomunicazione, fornitori di servizi di sicurezza gestiti, fornitori di software/SaaS, fornitori di outsourcing, fornitori critici non IT (es. utility energetica per data center, fornitori di servizi industriali OT).
- **Per ciascun fornitore**, almeno:
  - Denominazione e ragione sociale
  - Codice fiscale (P.IVA per soggetti italiani; identificativo equivalente per soggetti esteri, ove disponibile)
  - Paese della sede legale
  - Descrizione della fornitura (oggetto del contratto, servizi/prodotti forniti)
- **Mappa delle attivita' / servizi del soggetto NIS in ambito**: quali servizi rientrano nel decreto NIS, quali fornitori abilitano l'erogazione di tali servizi.

## Procedura

### Passo 1 - Verifica finestra temporale

Determinare se la finestra annuale di aggiornamento e' aperta (art. 16 co. 1 Det. 127437/2026):

| Anno corrente | Finestra aperta | Apertura | Chiusura |
|---------------|------------------|-----------|----------|
| 2026 (prima applicazione) | da definire alla data | **15 aprile 2026** | **31 maggio 2026** |
| 2027 e successivi | annuale fissa | 15 aprile | 31 maggio |

**Nota operativa**:
- Se siamo fuori finestra, l'elenco non puo' essere trasmesso tramite il "Servizio NIS/Aggiornamento annuale informazioni". Eventuali modifiche **post-finestra** seguono il regime dell'aggiornamento continuo (art. 19) entro 14 giorni dalla modifica (art. 1 co. 1 lett. hh).
- Per i soggetti del primo elenco 2025 che permangono nel 2026, la piattaforma precompila l'elenco con le informazioni trasmesse fino al 14 aprile 2026 (art. 16 co. 12 Det. 127437/2026).
- Per i soggetti nuovi 2026 con registrazione tardiva, il termine per completare l'aggiornamento annuale e' di 30 giorni dalla ricezione della comunicazione di inserimento ex art. 7 co. 3 lett. a) (art. 16 co. 11 Det. 127437/2026).

### Passo 2 - Censimento dell'universo dei fornitori da valutare

Costruire l'elenco di tutti i fornitori del soggetto NIS che potenzialmente possono qualificarsi come rilevanti. Includere almeno:

| Categoria | Esempi | Da valutare? |
|-----------|--------|--------------|
| Fornitori cloud / SaaS / IaaS / PaaS | hyperscaler, cloud regionali, SaaS verticali | SI |
| Fornitori DNS / TLD / registrar | gestori di nomi di dominio | SI |
| Fornitori CDN / IXP | distribuzione contenuti, scambi di traffico | SI |
| Fornitori reti / servizi di comunicazione elettronica | operatori telefonia/dati, ISP | SI |
| Fornitori di servizi gestiti (MSP) | outsourcing IT, managed networking, helpdesk gestito | SI |
| Fornitori di servizi di sicurezza gestiti (MSSP) | SOC esternalizzato, MDR, threat intelligence operativa | SI |
| Fornitori di software / componenti critici | ERP, CRM, sistemi industriali, EDR, firewall, applicativi core business | SI |
| Fornitori di servizi fiduciari | firma, sigillo, marcatura temporale, eIDAS | SI |
| Fornitori di data center / colocation / housing | strutture fisiche con sistemi del soggetto NIS | SI |
| Fornitori OT / SCADA / sistemi industriali | per soggetti con processi industriali critici | SI (valutare criterio 2) |
| Fornitori di utility (energia, acqua) per asset critici | utility che alimenta il data center primario | SI (valutare criterio 2) |
| Fornitori amministrativi non IT (pulizie, cancelleria) | | NO |
| Fornitori marketing / advertising senza accesso a dati critici | | NO |

**Nota operativa**: l'universo iniziale deve essere **largo**: meglio includere fornitori marginali e poi escluderli in Passo 3 sulla base dei due criteri, piuttosto che omettere un fornitore rilevante. La mancata comunicazione di un fornitore rilevante e' un'omissione informativa sanzionabile ai sensi dell'art. 38 D.Lgs. 138/2024 e dell'art. 2 co. 4 Det. 127437/2026.

### Passo 3 - Applicazione dei due criteri di rilevanza (art. 1 co. 1 lett. ll Det. 127437/2026)

Per ciascun fornitore dell'universo, valutare se soddisfa **almeno uno** dei due criteri:

#### Criterio 1: Fornitura ICT (Allegato I, punti 8 e 9, D.Lgs. 138/2024)

La fornitura e' riconducibile a:

| Punto Allegato I | Tipologia | Esempi di forniture |
|------------------|-----------|---------------------|
| 8 - Infrastrutture digitali | Fornitori IXP | scambio di traffico Internet |
| 8 | Fornitori DNS | risoluzione di nomi di dominio |
| 8 | Gestori registri TLD | gestione di top-level domain (es. .it) |
| 8 | Fornitori servizi cloud | IaaS, PaaS, SaaS |
| 8 | Fornitori data center | colocation, hosting |
| 8 | Fornitori CDN | rete di distribuzione contenuti |
| 8 | Fornitori servizi fiduciari (eIDAS) | firma, sigillo, marcatura temporale |
| 8 | Fornitori reti pubbliche di comunicazione elettronica | operatori telefonia/dati |
| 8 | Fornitori servizi di comunicazione elettronica accessibili al pubblico | telefonia, Internet residenziale/business |
| 9 - Gestione servizi TIC B2B | Fornitori di servizi gestiti (MSP) | outsourcing IT, helpdesk gestito, network management |
| 9 | Fornitori di servizi di sicurezza gestiti (MSSP) | SOC, MDR, vulnerability management gestito |

**Risposta**: SI/NO al criterio 1.

#### Criterio 2: Fornitura non fungibile con impatto significativo

L'interruzione o la compromissione della fornitura comporta un **impatto significativo** sulla capacita' del soggetto NIS di erogare le attivita' o i servizi per i quali rientra nell'ambito di applicazione del decreto NIS, **anche per effetto dell'indisponibilita' di fornitori alternativi**.

Test operativo - rispondere SI a entrambe le sotto-domande:

| Sotto-domanda | Risposta |
|---------------|----------|
| 2.a - L'interruzione (per N ore/giorni significative per il business) della fornitura impatta la capacita' del soggetto di erogare i servizi in ambito NIS? | SI/NO |
| 2.b - Esiste un fornitore alternativo immediatamente sostitutivo (entro tempi compatibili con la continuita' operativa)? | SI: criterio 2 NON soddisfatto / NO: criterio 2 SODDISFATTO |

**Nota operativa**: il criterio 2 ha valenza ampia e copre fornitori non strettamente ICT. Esempi tipici:
- Fornitore di servizi industriali OT/SCADA proprietario su cui gira l'impianto primario, senza alternative compatibili nel breve termine.
- Software gestionale verticale custom su cui ruota il processo di erogazione del servizio essenziale.
- Fornitore di utility (energia, acqua) per il data center primario non dotato di alimentazione di backup adeguata.

**Risposta**: SI/NO al criterio 2.

#### Esito per il fornitore

| Criterio 1 (ICT) | Criterio 2 (non fungibile) | Esito |
|------------------|----------------------------|-------|
| SI | qualsiasi | **Rilevante** (criterio 1) |
| NO | SI | **Rilevante** (criterio 2) |
| NO | NO | Non rilevante - escludere dall'elenco |

### Passo 4 - Raccolta dei dati di dettaglio per ogni fornitore rilevante

Per ciascun fornitore qualificato come rilevante, raccogliere i 5 campi richiesti dall'art. 18 Det. 127437/2026:

| Campo | Riferimento | Note operative |
|-------|-------------|----------------|
| a) Denominazione | art. 18 lett. a) | Ragione sociale come da Registro delle Imprese (o equivalente nel Paese di sede legale) |
| b) Codice fiscale | art. 18 lett. b) | P.IVA per soggetti italiani; identificativo equivalente del Paese estero (es. VAT EU, EIN US, ABN AU) |
| c) Paese sede legale | art. 18 lett. c) | Codice ISO 3166-1 alpha-2 o nome del Paese |
| d) Codici CPV | art. 18 lett. d) | Riferimento Reg. (CE) n. 2195/2002. Format XXXXXXXX-Y (8 cifre + cifra di controllo). Indicare i codici relativi alle forniture **di cui il soggetto NIS fruisce** (non l'intero catalogo del fornitore). Possono essere piu' codici per fornitore. |
| e) Criterio di rilevanza | art. 18 lett. e) | Indicare il criterio di cui all'art. 1 co. 1 lett. ll): **1** (fornitura ICT - Allegato I p. 8-9) oppure **2** (fornitura non fungibile). Se entrambi applicabili, indicarli entrambi |

**CPV - codici di riferimento per le forniture ICT** (esempi, non esaustivo):

| CPV | Descrizione |
|-----|-------------|
| 30200000-1 | Apparecchiature informatiche e forniture |
| 32400000-7 | Reti |
| 32500000-8 | Materiale per telecomunicazioni |
| 48000000-8 | Pacchetti software e sistemi di informazione |
| 64200000-8 | Servizi di telecomunicazione |
| 72000000-5 | Servizi informatici: consulenza, sviluppo software, Internet e supporto |
| 72500000-0 | Servizi informatici |
| 72600000-6 | Servizi di consulenza e di supporto informatico |
| 72700000-7 | Servizi di reti informatiche |

Per i codici esatti consultare il vocabolario ufficiale (https://simap.ted.europa.eu/cpv) o le pubblicazioni della Commissione Europea.

### Passo 5 - Compilazione della tabella di output

```markdown
# Elenco fornitori rilevanti NIS - [nome organizzazione]

**Data**: [YYYY-MM-DD]
**Finestra di aggiornamento ACN**: 15 aprile - 31 maggio [YYYY]
**Anno di riferimento**: [YYYY]
**Compilato da**: [nome / ruolo]

## Tabella fornitori rilevanti

| # | Denominazione | Codice fiscale | Paese sede legale | Codici CPV | Criterio (1=ICT / 2=non fungibile) | Note interne (non comunicate ad ACN) |
|---|---------------|-----------------|---------------------|--------------|--------------------------------------|-----------------------------------------|
| 1 | [...] | [...] | [...] | [...] | [...] | [breve descrizione fornitura] |
| 2 | [...] | [...] | [...] | [...] | [...] | |
| ... | | | | | | |

## Fornitori valutati ma esclusi (motivazione documentata)

| # | Denominazione | Categoria fornitura | Motivo esclusione |
|---|---------------|---------------------|---------------------|
| ... | [...] | [...] | [criterio 1 NO + criterio 2 NO: fornitura sostituibile in tempi compatibili / non ricondotta a Allegato I p. 8-9] |

## Trasmissione

- [ ] Tutti i fornitori rilevanti elencati nella tabella sono stati censiti nel "Servizio NIS/Aggiornamento annuale informazioni" entro il 31 maggio [YYYY].
- [ ] Il punto di contatto ha confermato l'aggiornamento ai sensi del DPR 445/2000 (art. 16 co. 7 Det. 127437/2026).
- [ ] Copia dell'aggiornamento e' stata ricevuta al domicilio digitale del soggetto (art. 16 co. 7).

## Aggiornamento continuo (post-finestra)

Se dopo il 31 maggio cambia l'elenco (nuovo fornitore rilevante, fornitore cessato, modifica codici CPV), l'aggiornamento e' trasmesso tramite il "Servizio NIS/Aggiornamento continuo informazioni" entro **14 giorni** dalla modifica (art. 19 Det. 127437/2026 + art. 1 co. 1 lett. hh).
```

## Casi tipici

| Caso | Categoria | Criterio applicato | Note |
|------|-----------|---------------------|------|
| Fornitore cloud IaaS hyperscaler | Allegato I.8 | Criterio 1 | Fornitura ICT (cloud) - rilevante per definizione |
| Operatore telefonia mobile aziendale | Allegato I.8 | Criterio 1 | Fornitura ICT (servizio comunicazione elettronica) |
| MSP che gestisce la rete aziendale | Allegato I.9 | Criterio 1 | Servizi TIC gestiti - rilevante per definizione |
| Software ERP custom su cui ruota il fatturato | (non ricondotto a Allegato I p.8-9) | Criterio 2 | Fornitura non fungibile (non c'e' alternativa nel breve) |
| Utility elettrica primaria del data center | (non ICT) | Criterio 2 (se data center senza alimentazione di backup adeguata) | Valutare se l'alternativa di emergenza (gruppi elettrogeni, UPS, secondo fornitore) e' immediata |
| Servizio di pulizia uffici | (non ICT, non critico) | Nessuno | Non rilevante |
| Fornitore di carta per stampanti | (non ICT, fungibile) | Nessuno | Non rilevante |
| Vendor del firewall perimetrale (licenza + supporto) | Allegato I.9 (se servizio di sicurezza gestito) oppure Criterio 2 | Criterio 1 o 2 | Se solo licenza software senza gestione, valutare criterio 2 (impatto interruzione patch/supporto) |

## Limiti di questo task

- L'elenco e' una **dichiarazione di parte** del soggetto NIS sotto la propria responsabilita' (DPR 445/2000 - art. 16 co. 7 Det. 127437/2026). L'ACN puo' svolgere verifiche di coerenza (art. 14 Det. 127437/2026, sui dati di registrazione; per i fornitori rilevanti il riferimento e' l'art. 38 D.Lgs. 138/2024 sulla dichiarazione mendace).
- La definizione di "fornitori alternativi" del criterio 2 e' qualitativa: la valutazione richiede analisi del contratto, dei tempi di sostituzione tecnologica/contrattuale, dei costi di switching. Non c'e' una soglia numerica fissata dalla determinazione.
- I codici CPV non sono ufficialmente "tassonomia ACN": e' il vocabolario europeo degli appalti pubblici (Reg. CE 2195/2002). L'allineamento di una fornitura privata al CPV richiede una scelta del soggetto NIS che e' opportuno documentare internamente.
- L'elenco e' **annuale**: serve un processo strutturato di revisione interna periodica per assicurare l'aggiornamento continuo (art. 19) entro 14 giorni dalle modifiche significative.
- Le informazioni trasmesse all'ACN sono **a divulgazione limitata** (art. 3 co. 7 Det. 127437/2026): non sono pubblicate dall'ACN ne' divulgate a terzi non legittimati.
