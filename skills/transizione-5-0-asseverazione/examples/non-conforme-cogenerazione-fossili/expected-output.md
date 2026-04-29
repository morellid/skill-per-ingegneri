# Output atteso - cogenerazione fossili (NON conforme)

> Esempio sintetico di output che la skill dovrebbe produrre per l'input descritto in `input.md`. Mostra come la skill arresta correttamente l'iter al rilevamento della violazione DNSH, **prima** di procedere con il calcolo dei risparmi e la struttura della certificazione.

## Output atteso da `verifica-ammissibilita.md`

```markdown
# Verifica ammissibilita' Piano Transizione 5.0

**Data**: 2026-04-29
**Soggetto beneficiario**: BETA Olio Spa, P.IVA 03987654321
**Settore**: ATECO 10.41.10 (produzione olio di oliva)
**Localizzazione**: Spoleto (PG)
**Perimetro**: struttura produttiva
**Certificatore**: Ing. Lucia Bianchi, EGE UNI CEI 11339
**Importo investimenti**: 3.130.000 EUR
**Avvio**: 1/7/2024 | **Completamento previsto**: 31/10/2025

## 1. Ambito soggettivo
| Requisito | Esito |
|---|---|
| Impresa residente in Italia | Conforme |
| Assenza procedure concorsuali | Conforme |
| Sicurezza/contributi | Conforme |

## 2. Ambito oggettivo - rilievo critico
| Voce | Esito |
|---|---|
| Cogeneratore a gas naturale 1,5 MWe (Allegato A?) | **CRITICO**: il bene puo' rientrare in una voce dell'Allegato A L. 232/2016, ma e' direttamente alimentato da combustibile fossile (gas naturale). Verificare con la perizia ex art. 16 se il cogeneratore e' incluso nell'allegato; tuttavia, anche se la classificazione 4.0 e' corretta, **resta la criticita' DNSH del Passo 6**. |
| SCADA + Energy Dashboarding (All. B voce 10) | Conforme alla classificazione 4.0 |
| FV 100 kW (FER, no biomasse, su stessa particella) | Conforme art. 7 DM |

## 3. Avvio e completamento
| Requisito | Esito |
|---|---|
| Avvio dal 1/1/2024 (1/7/2024) | Conforme |
| Completamento entro 31/12/2025 (31/10/2025) | Conforme |

## 4. Soglia di risparmio energetico (preliminare)
- Soglia perseguita: 3% sulla struttura produttiva
- Riduzione dichiarata: 8,9% (vedi calcolo - irrilevante in caso di esclusione DNSH)
- Esito preliminare: matematicamente conforme, **ma valutare DNSH al Passo 6**

## 5. DNSH e attivita' escluse - **BLOCCO**

| Esclusione | Riferimento | Esito |
|---|---|---|
| **Combustibili fossili (uso a valle)** | art. 5 co. 1 lett. a DM | **NON CONFORME** |

**Analisi**: l'art. 5 co. 1 lett. a del DM 24/7/2024 esclude dall'agevolazione i progetti di innovazione con investimenti destinati ad "attivita' direttamente connesse all'uso dei combustibili fossili, compreso l'uso a valle". Il **cogeneratore a gas naturale** e' una macchina **direttamente connessa all'uso del combustibile fossile** (gas naturale): l'investimento principale del progetto (2,8 mln EUR su 3,13 mln EUR, pari al 89,5% del valore) ricade nella clausola di esclusione.

**Eccezioni applicabili?**:
- "Uso a valle di combustibili fossili temporaneo e tecnicamente inevitabile per la tempestiva transizione verso un funzionamento senza combustibili fossili" (art. 5 co. 1 lett. a punto 1 DM): **NON applicabile** al cogeneratore, che e' un investimento sostitutivo di un cogeneratore preesistente, non strumentale a una transizione verso elettrificazione/idrogeno verde.
- "Macchine mobili non stradali / veicoli agricoli e forestali" con passaggio Stage I -> Stage V (art. 5 co. 1 lett. a punto 2): **NON applicabile** (cogeneratore stazionario).

**Conclusione**: il cogeneratore non rientra nelle eccezioni. **Il progetto e' inammissibile** per la quota dell'investimento riferita al cogeneratore.

> ATTENZIONE: la non ammissibilita' si applica al **progetto di innovazione complessivo**, perche' la riduzione dei consumi (8,9% sulla struttura) e' realizzata **principalmente attraverso il cogeneratore**, non attraverso il SCADA + FV. Anche escludendo il cogeneratore dal computo, la riduzione conseguibile dal solo SCADA + Energy Dashboarding sui processi della struttura produttiva sarebbe **molto inferiore al 3%**: il progetto non raggiungerebbe la soglia minima.

## 6. Soggetto certificatore
| Requisito | Esito |
|---|---|
| EGE UNI CEI 11339 + Accredia in corso di validita' | Conforme |
| Polizza RC | Conforme |
| Terzieta' | Conforme |

## 7. Tetto costi
| Vincolo | Esito |
|---|---|
| <= 50 mln EUR/anno | Compatibile |

## 8. Esito complessivo
**NON AMMISSIBILE** per violazione del principio DNSH ex art. 5 co. 1 lett. a DM 24/7/2024 (combustibili fossili - uso a valle).

## 9. Indicazione al certificatore

> Il certificatore **NON puo' rilasciare la certificazione ex ante** per il progetto di rinnovamento del cogeneratore a gas naturale.
>
> Possibili strade alternative per BETA Olio Spa:
> 1. **Riprogettare l'investimento** sostituendo il cogeneratore a gas con tecnologie compatibili DNSH (es. pompe di calore alimentate da elettricita' rinnovabile, cogeneratori a biomasse - **escluse pero' dall'art. 7 DM** per l'autoproduzione FER, ma valutabili come bene 4.0 se inclusi negli allegati A/B; idrogeno verde; recupero termico industriale).
> 2. **Scorporare** dal progetto Transizione 5.0 il cogeneratore (mantenendo investimento in autonomia con altre agevolazioni: es. detrazioni 65%, contributi regionali) e presentare al T5.0 **solo SCADA + FV**: in tal caso pero' la riduzione consumi attesa scende sotto il 3% e il progetto non e' ammissibile per mancato raggiungimento soglia.
> 3. **Valutare altri strumenti** di incentivazione: ad esempio Industria 4.0 (per l'eventuale rateo 4.0 sui beni A/B compatibili), credito d'imposta beni strumentali ordinari, incentivi regionali.

## 10. Avvertenze

- La presente verifica e' un **giudizio preliminare** del certificatore sulla compatibilita' DNSH; la valutazione definitiva spetta al MIMIT/GSE in sede di vigilanza/controllo (artt. 19-20 DM).
- Non si procede con i task `calcola-riduzione-consumi.md`, `struttura-certificazione-ex-ante.md`, `struttura-certificazione-ex-post.md`: il progetto non e' ammissibile.
- La riduzione consumi 8,9% e' tecnicamente reale ma **giuridicamente irrilevante** per Transizione 5.0: il principio DNSH **prevale** sulla soglia minima.
- Il certificatore deve **rifiutare l'incarico** o, se gia' accettato, restituire l'incarico con motivazione scritta. Procedere con la firma di una certificazione ex ante in violazione DNSH esporrebbe a:
  - **responsabilita' penale aggravata** (artt. 359, 481 c.p. + art. 76 DPR 445/2000);
  - **revoca dell'abilitazione al rilascio** delle certificazioni Transizione 5.0 (art. 19 DM);
  - **responsabilita' civile** verso lo Stato e l'impresa beneficiaria (recupero credito + interessi + sanzioni).

**La presente verifica blocca il progetto a monte. Il rinvio al consulente fiscale del cliente per valutazione di alternative e' indispensabile.**
```

## Lezione del caso

Il caso illustra:

1. La **gerarchia** delle verifiche: il DNSH (art. 5 + 18 DM) e' **prerequisito assoluto** che precede e prevale sulla verifica delle soglie di riduzione consumi.
2. La **funzione filtro** del Piano Transizione 5.0: non incentiva qualsiasi efficientamento energetico, ma quello allineato agli obiettivi del PNRR REPowerEU (transizione verso fonti rinnovabili, no combustibili fossili).
3. Il **rischio professionale** del certificatore: una certificazione ex ante "ottimistica" che ignori il DNSH espone a sanzione penale aggravata.
4. La necessita' di **documentazione preliminare** sulla compatibilita' DNSH prima di accettare un incarico di certificazione: il certificatore valuta **prima** se il progetto e' ammissibile, **poi** procede con il calcolo dei risparmi e la stesura dell'asseverazione.
