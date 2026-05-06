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
- Configurazioni alternative compatibili: nessuna (GAC esclusa per assenza di "stesso edificio/condominio", AID esclusa per piu' soggetti).

## 5. Verifiche obbligatorie residue
- [ ] Verifica formale cabina primaria sul portale GSE (gia' indicata, da stampare)
- [x] Forma giuridica CER da scegliere con notaio (associazione vs cooperativa vs ente del terzo settore)
- [ ] Verifica titolo abilitativo impianto (Modello Unico se < 200 kW non si applica; per 350 kW serve PAS o autorizzazione regionale)
- [ ] Verifica popolazione ISTAT 31/12/2025 (dichiarata 1.812 ab.)
- [ ] Predisposizione DNSH per misura PNRR M2C2 1.2

## 6. Avvertenza finale
La presente scheda e' un supporto preliminare. La qualifica formale del servizio
CACER e' rilasciata dal GSE secondo le Regole Operative vigenti. La forma
giuridica della CER richiede la consulenza di notaio e commercialista.
```

## 2. Statuto (task `redigi-statuto-cer`) - estratto

L'output del task e' la bozza completa di statuto. Estratto dei punti chiave attesi:

- **Art. 1**: denominazione "CER [Nome]", forma giuridica suggerita "associazione riconosciuta" (DA VERIFICARE CON NOTAIO), sede nel municipio.
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
- Producibilita': 1.150 kWh/kWp/anno (Centro Italia)
- Livello di tensione: BT
- Comune: [Nome] - popolazione 1.812 ab. (< 5.000)
- Profilo utenze: misto residenziale + terziario diurno (PMI turismo)
- Fattore di condivisione `eta_share`: 0.45 (mix residenziale/diurno, no accumulo)
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
| Contributo PNRR | min(0.40 * 420.000; massimale PNRR) = 168.000 una tantum | riduce parte fissa TIP |

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
- Documenti TIP: PAS dell'impianto FV 350 kW (Comunicazione/Modello Unico non applicabili sopra 200 kW), titolo di disponibilita' del capannone (proprieta' Comune), schema unifilare, fine lavori, codice CENSIMP, dichiarazione non doppio incentivo.
- Documenti PNRR: attestazione ISTAT 1.812 ab. al 31/12/2025, computo metrico 420.000 EUR, cronoprogramma con milestone PNRR, dichiarazione DNSH (rinvio skill dedicata), dichiarazioni anti-doppio-finanziamento, eventuale documentazione gara per appalto del Comune.
- Adempimenti continuativi del referente.
- Avvertenza che la lista esatta segue le Regole Operative GSE vigenti.
