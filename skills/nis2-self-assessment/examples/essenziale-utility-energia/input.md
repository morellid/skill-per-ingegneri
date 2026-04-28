# Input - Utility energetica grande dimensione

## Identificazione

- **Ragione sociale**: ENERGOSPA S.p.A. (esempio fittizio)
- **Settore**: distribuzione di energia elettrica (gestore del sistema di distribuzione - DSO) + produzione da fonti rinnovabili
- **Codice ATECO principale**: 35.13 (Distribuzione di energia elettrica)
- **Sede legale**: Roma
- **Sedi operative**: Roma, Milano, 12 cabine primarie distribuite sul territorio
- **Dipendenti**: 1.450
- **Fatturato annuo (2024)**: 380M EUR
- **Totale di bilancio annuo**: 720M EUR
- **Ambito geografico**: Italia (4 regioni)

## Servizi forniti

- Distribuzione di energia elettrica a ~ 480.000 clienti finali (residenziali, commerciali, PMI)
- Produzione da impianti fotovoltaici e idroelettrici per ~ 850 MW installati
- Gestione di alcune sottostazioni di trasformazione

## Identificazioni pregresse

- Non identificata come operatore di servizi essenziali ai sensi del D.Lgs. 65/2018 (NIS originale) - non era nel primo elenco
- Non identificata come soggetto critico ai sensi della Dir. 2022/2557 (decreto di recepimento in corso al momento)
- Non rientra nel Perimetro di Sicurezza Nazionale Cibernetica (DL 105/2019)
- E' regolata da ARERA per il servizio di distribuzione

## Asset critici (autovalutazione)

- Sistema SCADA per gestione cabine primarie
- Sistema di telecontrollo (ICS/OT) per oltre 200 cabine secondarie
- Sistema di billing per i 480k clienti
- Portale clienti con autenticazione SPID/CIE
- Active Directory aziendale (~ 1.500 utenti + 200 service account)
- Infrastruttura cloud ibrida (Azure + on-prem)

## Stato governance e misure cyber (sintesi)

- **CdA**: 7 membri, riunioni mensili
- **CISO**: presente, riporta al CFO; manca riporto diretto al CdA
- **Comitato sicurezza ICT**: presente, mensile; non emette atti formali al CdA
- **Politiche cyber documentate**: 8 politiche approvate dal management ICT, NON dal CdA
- **Piano di gestione del rischio cyber**: presente, aggiornato annualmente
- **ISMS**: in fase di certificazione ISO/IEC 27001 (audit di certificazione previsto T+6 mesi)
- **MFA**: implementato per accessi privilegiati e VPN dipendenti; NON implementato per portale interno utenti
- **Backup**: presente, off-site, test di restore annuale (l'ultimo a T-9 mesi)
- **SOC**: outsourcing a MSSP italiano con SIEM gestito e presidio H24
- **Awareness**: programma annuale e-learning per tutti i dipendenti, simulazioni phishing trimestrali
- **Formazione CdA cyber**: mai erogata
- **Vulnerability management**: scanning settimanale + remediation 30/60/90 giorni in base alla severita'
- **Vendor management cyber**: contratti standard con clausole base; nessun TPRM strutturato
- **Notifica incidenti**: nessuna procedura formalizzata verso CSIRT Italia (mai notificato in passato)

## Domanda dell'utente

"Siamo un soggetto NIS2? Essenziali o importanti? Cosa dobbiamo fare per essere conformi entro le scadenze?"
