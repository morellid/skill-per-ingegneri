# Note di dominio - PMI manifatturiera importante

## Perche' questo caso

Esempio paradigmatico di **soggetto importante** ex art. 6 co. 3:
- Settore Allegato II (manifattura, divisione NACE 26)
- Tipologia di soggetto presente (fabbricazione computer/elettronica)
- Dimensione "media" (oltre piccole, sotto medie -> sicuramente non grande)

E' anche un caso tipico di **PMI italiana** che si trova improvvisamente in ambito NIS2 senza preparazione interna ne' CISO dedicato.

## Aspetti di domain expertise

### 1. Mapping NACE/ATECO

L'Allegato II rinvia esplicitamente a "NACE Rev. 2 sezione C divisione 26". I codici ATECO 2007 italiani derivano da NACE (sono parzialmente armonizzati):
- ATECO 26.11 ("Fabbricazione di componenti elettronici") = NACE 26.11
- L'identificazione e' diretta. Per altri settori (es. macchinari NACE 28) la mappatura puo' richiedere verifica precisa del codice ATECO.

### 2. Sovrapposizione TISAX / NIS2 / ISO 27001

I fornitori automotive italiani sono soggetti a una **trifasizzazione**:
- **TISAX** (richiesto contrattualmente dagli OEM)
- **NIS2** (obbligo di legge)
- **ISO/IEC 27001** (spesso richiesto dai clienti enterprise)

Approccio "do-it-once":
- Costruire un ISMS unico che soddisfi tutti e tre.
- Mappare i controlli ISO 27001 Annex A -> sottocategorie Det. ACN -> requisiti TISAX.
- Audit unico (TISAX o ISO 27001) puo' fornire evidenze utili per ispezione ACN.

### 3. Ruolo nella catena di approvvigionamento (art. 3 co. 10)

ATTENZIONE: il fatto che COMPONENTECNICA sia fornitore di Marelli/Bosch (potenzialmente soggetti essenziali) NON la rende automaticamente in ambito ex art. 3 co. 10. I criteri (a-d) richiedono un legame di influenza sulle decisioni di sicurezza, gestione di sistemi critici, operazioni di sicurezza, fornitura di servizi TIC/sicurezza al soggetto. Un fornitore di componenti elettronici embedded NON rientra automaticamente in questi criteri.

In ogni caso, il soggetto e' gia' in ambito via Allegato II + size-cap rule, quindi questa analisi e' accademica.

### 4. PMI senza CISO

Il caso evidenzia un problema reale: molte PMI italiane in ambito NIS2 non hanno mai avuto un CISO. Soluzioni pragmatiche:
- **vCISO** (CISO virtuale, parte time): 1-2 giorni/mese a 1.000-1.500 EUR/giorno
- **MSSP italiano** che fornisce SOC + advisory NIS2
- Formazione del responsabile IT esistente come "compliance officer" cyber con supervisione esterna

### 5. Stabilimento in Slovacchia

Per la giurisdizione (art. 5 D.Lgs. 138/2024):
- I 25 dipendenti slovacchi e l'eventuale societa' slovacca **non rendono il soggetto NIS slovacco**: il decreto si applica al soggetto italiano stabilito in Italia.
- Pero' lo stabilimento slovacco rientrerebbe potenzialmente nel **decreto slovacco di recepimento NIS 2** (Slovacchia ha trasposto NIS 2 con propria normativa nazionale). Da verificare separatamente con consulente legale slovacco.
- Per un soggetto italiano, l'obbligo di registrazione e' su piattaforma ACN; pero' la notifica nell'art. 7 co. 4 lett. b) chiede l'elenco degli Stati membri in cui forniscono servizi che rientrano nell'ambito del decreto.

## Punti di attenzione tipici per PMI manifatturiere

1. **OT/MES**: la rete di produzione (PLC, robot, MES) ha tipicamente requisiti di disponibilita' alti e patching limitato. Approccio: segregazione di rete + monitoring + DMZ per ERP/MES.
2. **Smart working**: post-COVID molte PMI hanno ampliato VPN senza MFA strutturato. Quick win prioritario.
3. **Backup**: spesso non testati. Test di restore semestrale almeno (PR.DS-11).
4. **Vulnerability management**: assente. Scanning settimanale Nessus/Qualys + patching prioritizzato e' implementabile in poche settimane.
5. **Awareness e phishing**: i dipendenti di produzione hanno spesso meno training degli office workers. Programma differenziato per ruoli.

## Riferimenti per validazione domain expert

Validatore profilo target: consulente cybersecurity con esperienza su PMI manifatturiere automotive/industria + familiarita' con:
- TISAX (VDA-ISA), almeno conoscenza dei criteri AL2/AL3
- IEC 62443 (per la parte OT/MES)
- ISO/IEC 27001 implementazione su PMI
- Esperienza con MSSP italiani (Cyberoo, Var Group, Tecnosoft, ecc.)
