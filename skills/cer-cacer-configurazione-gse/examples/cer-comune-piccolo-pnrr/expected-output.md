# Output atteso - CER su Comune piccolo con cumulo TIP + contributo PNRR

Output sintetico atteso, articolato sulle 4 sotto-attivita' richieste.

## 1. Pre-fattibilita' (task `valuta-perimetro-configurazione`)

```markdown
# Scheda di pre-fattibilita' CACER

## 1. Soggetti coinvolti
- 35 persone fisiche
- 4 PMI (turismo / artigianato), nessuna con energia come attivita' principale
- 1 ente locale (Comune) con 3 POD
- 1 ente religioso (parrocchia) con 1 POD
- Grandi imprese: NO
- Referente ipotizzato: CER stessa, con eventuale supporto di ESCo - DA CONFERMARE

## 2. Posizione e perimetro
- POD prelievo: 41 POD nel Comune di [Nome] (popolazione 1.812 ab.)
- POD immissione: 1 POD su capannone comunale, stesso Comune
- Cabina primaria: confermata su mappa GSE (perimetro CACER rispettato)
- Stesso edificio/condominio: NO

## 3. Impianti FER
- Tecnologia: FV in copertura
- Potenza singolo impianto: 350 kW (fascia 200-600 kW)
- Stato: in progetto

## 4. Configurazione consigliata
- Configurazione: **CER** (art. 31 D.Lgs. 199/2021), motivazione:
  - piu' soggetti distinti, alcuni distanti tra loro, sotto stessa cabina primaria;
  - presenza di ente locale e finalita' di riduzione poverta' energetica;
  - PMI con partecipazione non principale.
- Configurazioni alternative compatibili: nessuna (GAC art. 30 c. 2 esclusa per assenza di "stesso edificio/condominio", AID art. 30 c. 1 lett. a) n. 2 esclusa per piu' soggetti).

## 5. Verifiche obbligatorie residue
- [ ] Verifica formale cabina primaria sul portale GSE (gia' indicata, da stampare)
- [ ] Forma giuridica CER da scegliere e formalizzare (associazione, cooperativa, ente del terzo settore con iscrizione RUNTS, ecc.) - decisione da prendere con consulente legale e fiscale
- [ ] Verifica titolo abilitativo impianto FER 350 kW: il titolo applicabile dipende da DPR 380/2001, D.Lgs. 28/2011 e normativa regionale - DA VERIFICARE con il professionista (la skill non ha tra le fonti questa normativa)
- [ ] Verifica popolazione ISTAT 31/12/2025 (dichiarata 1.812 ab., dentro soglia PNRR < 50.000 ab.)
- [ ] Predisposizione DNSH per misura PNRR M2C2 1.2 (rinvio a `dnsh-pnrr-checker`)
- [ ] Verifica scadenze PNRR (regime post DL 19/2026): stipula accordi di concessione lato GSE entro 30/6/2026, entrata in esercizio entro 24 mesi dalla comunicazione dell'accordo e comunque non oltre 31/12/2027

## 6. Avvertenza finale
La presente scheda e' un supporto preliminare. La qualifica formale del servizio
CACER e' rilasciata dal GSE secondo le Regole Operative vigenti. La forma
giuridica della CER richiede la consulenza di un consulente legale e di un commercialista, e la formalizzazione dello statuto secondo la forma scelta (atto pubblico, scrittura privata autenticata, procedura RUNTS, ecc.).
```

## 2. Statuto (task `redigi-statuto-cer`) - estratto

L'output del task e' la bozza completa di statuto. Estratto dei punti chiave attesi:

- **Art. 1**: denominazione "CER [Nome]", forma giuridica suggerita "associazione riconosciuta" (DA VERIFICARE con consulente legale e formalizzare con la modalita' richiesta dalla forma scelta), sede nel municipio.
- **Art. 2**: finalita' principale = benefici ambientali (riduzione CO2) + economici (riduzione costi energia) + sociali (fondo poverta' energetica). Avanzi reinvestiti.
- **Art. 3**: perimetro = cabina primaria [ID], Comune di [Nome].
- **Art. 4**: soci ammessi = persone fisiche, PMI con partecipazione non principale, enti locali, enti religiosi; grandi imprese escluse.
- **Art. 5**: governance = assemblea con voto capitario, organo di amministrazione di 5 membri (3 cittadini, 1 Comune, 1 PMI).
- **Art. 7**: ripartizione benefici = 70% pro quota su consumo, 20% Comune per servizi pubblici, 10% fondo poverta' energetica.
- **Art. 9**: referente = CER stessa, con possibilita' di delega operativa a ESCo. Mandato a sottoscrivere documenti GSE.
- Avvertenza finale di natura non definitiva.

## 3. Simulazione (task `simula-autoconsumo-condiviso`)

```markdown
# Simulazione semplificata CACER

## 1. Ipotesi di calcolo
- FV in copertura, 350 kW
- Producibilita': 1.150 kWh/kWp/anno (FONTE: dichiarazione del progettista, simulazione PVGIS sito-specifica per copertura inclinata 15°)
- Livello di tensione: BT
- Comune: [Nome] - popolazione 1.812 ab. (dentro soglia PNRR < 50.000 ab. post DM 127/2025; era anche dentro la soglia originaria < 5.000 ab.)
- Profilo utenze: misto residenziale + terziario diurno (PMI turismo)
- Fattore di condivisione `eta_share`: 0.45 (FONTE: ipotesi del progettista basata su analisi semplificata di sovrapposizione produzione/prelievo, mix residenziale/diurno, no accumulo - da rivedere su profili orari)
- Valori TIP/TR: parametrici, DA VERIFICARE su pubblicazione GSE/ARERA vigente

## 2. Bilancio energetico annuo
| Voce | kWh/anno |
|---|---|
| Energia immessa CACER | 350 * 1.150 = 402.500 |
| Energia prelevata CACER | 320.000 |
| Energia condivisa stimata | 0.45 * min(402.500; 320.000) = 144.000 |

## 3. Flussi economici (stima parametrica)
| Voce | EUR/anno | Note |
|---|---|---|
| TIP | E_cond * (T_fissa(200-600 kW) + correttivo zonale) - DA QUANTIFICARE su valori vigenti | durata 20 anni |
| TR | E_cond * tr_unitaria(BT) - DA QUANTIFICARE su delibera ARERA vigente | |
| Contributo PNRR | min(0.40 * 420.000; massimale PNRR) ~ 168.000 una tantum | regime vigente al 2026-05-07 (DM 414/2023 + DM 127/2025 + DL 19/2026 art. 27); stipula accordi di concessione GSE entro 30/6/2026; esercizio entro 24 mesi dalla comunicazione dell'accordo (max 31/12/2027); erogazione in 3 fasi (anticipazione 30% + quota intermedia 40% + saldo - schema di derivazione DM 127/2025, da confermare sulla versione vigente delle Regole Operative GSE post DL 19/2026); riduce parte fissa TIP |

## 4. Avvertenze
- Stima parametrica, calcolo ufficiale a cura del GSE.
- TIP e TR vanno aggiornate alla data di qualifica.
- Cumulo PNRR + TIP: applicare riduzione TIP ex DM 7/12/2023.
- DNSH PNRR: rinvio a skill `dnsh-pnrr-checker`.

## 5. Disclaimer
Documento di supporto, non costituisce promessa di flussi economici futuri.
```

## 4. Checklist GSE (task `predisponi-qualifica-gse`) - estratto

- Documenti generali: anagrafica referente (CER), mandato, elenco POD (41 prelievo + 1 immissione), elenco impianti (1 FV 350 kW), stampa mappa cabina primaria.
- Documenti CER: atto costitutivo + statuto firmati, verbale nomina referente, eventuale convenzione con ESCo per gestione operativa.
- Documenti TIP: titolo abilitativo dell'impianto FV 350 kW DA VERIFICARE secondo DPR 380/2001 + D.Lgs. 28/2011 + normativa regionale (la skill non determina il titolo applicabile), titolo di disponibilita' del capannone (proprieta' Comune), schema unifilare, fine lavori, codice CENSIMP, dichiarazione non doppio incentivo.
- Documenti PNRR: attestazione ISTAT 1.812 ab. al 31/12/2025 (dentro soglia < 50.000 ab.), computo metrico 420.000 EUR, cronoprogramma coerente con regime post DL 19/2026 (stipula accordi di concessione lato GSE entro 30/6/2026, esercizio entro 24 mesi dalla comunicazione dell'accordo - max 31/12/2027), dichiarazione DNSH (rinvio skill dedicata), dichiarazioni anti-doppio-finanziamento, eventuale documentazione gara per appalto del Comune, eventuale richiesta di anticipazione fino al 30% e successiva quota intermedia del 40% (schema di derivazione DM 127/2025, percentuali da confermare sulle Regole Operative GSE post DL 19/2026).
- Adempimenti continuativi del referente.
- Avvertenza che la lista esatta segue le Regole Operative GSE vigenti.
