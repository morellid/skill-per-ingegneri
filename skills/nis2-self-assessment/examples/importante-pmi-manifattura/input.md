# Input - PMI manifatturiera media impresa

## Identificazione

- **Ragione sociale**: COMPONENTECNICA S.r.l. (esempio fittizio)
- **Settore**: fabbricazione di componenti elettronici per l'industria automotive
- **Codice ATECO principale**: 26.11 (Fabbricazione di componenti elettronici)
- **Sede legale**: Modena
- **Sedi operative**: Modena (HQ + stabilimento), Bologna (R&D), Bratislava (stabilimento estero piccolo)
- **Dipendenti**: 180 in Italia + 25 in Slovacchia = **205 totali**
- **Fatturato annuo (2024)**: 42M EUR
- **Totale di bilancio annuo**: 35M EUR
- **Ambito geografico**: Italia, Slovacchia, esportazione in 12 Paesi UE + alcuni extra-UE

## Servizi/prodotti forniti

- Componenti elettronici per ECU automotive (Tier 2 supplier)
- Servizi di assemblaggio elettronico (EMS) per terzi
- Tre linee di produzione automatizzate

## Identificazioni pregresse

- Non identificata come operatore di servizi essenziali ai sensi del D.Lgs. 65/2018
- Non identificata come soggetto critico ai sensi della Dir. 2022/2557
- Non rientra nel Perimetro di Sicurezza Nazionale Cibernetica
- Fornitore di Tier 1 automotive (Marelli, Bosch Italia, ecc.)

## Asset critici (autovalutazione)

- ERP SAP (on-prem) per gestione produzione, logistica, finanza
- MES (Manufacturing Execution System) interconnesso con linee di produzione
- PLM (Product Lifecycle Management) con dati progettuali clienti (sotto NDA)
- File server con disegni, BoM, processi produttivi
- Active Directory aziendale (~ 220 utenti)
- VPN per smart working e accessi fornitori

## Stato governance e misure cyber (sintesi)

- **Governance**: amministratore unico (proprietario) + direttore generale
- **CISO**: NO. Responsabilita' cyber su responsabile IT (1 persona) che riporta al CFO
- **Politiche cyber documentate**: 2 (uso accettabile + password policy), entrambe vecchie e non riviste da 5 anni
- **ISMS / certificazioni**: nessuna; valutata internamente l'adesione a TISAX (richiesta da Marelli) ma non ancora implementata
- **MFA**: assente, salvo VPN
- **Backup**: backup giornaliero su NAS + settimanale su nastro off-site; ultimo test di restore: 2 anni fa
- **SOC**: assente; antivirus endpoint enterprise + firewall perimetrale di base
- **Awareness**: corso una tantum nel 2022, mai ripetuto
- **Vulnerability management**: nessun processo strutturato
- **Vendor management cyber**: nessuna clausola
- **Notifica incidenti**: nessuna procedura
- **OT/MES sicurezza**: rete OT separata dalla IT su firewall, ma l'MES e' collegato al ERP

## Domanda dell'utente

"Riceviamo richieste dai nostri clienti automotive (Marelli) che ci chiedono di essere conformi a NIS2 e TISAX. Siamo davvero soggetti NIS2? Cosa dobbiamo fare?"
