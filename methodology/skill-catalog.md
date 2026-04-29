# Catalogo skill candidate

Lista ragionata delle skill candidate per il repository, organizzate per area dell'ingegneria italiana. Ogni voce e' identificata da un **codice scheda** (es. `CT.3`, `SC.1`, `EL.1`) referenziato dalle issue GitHub di proposta nuova skill.

Per i criteri di valutazione e il processo decisionale vedi [`criteri-selezione.md`](criteri-selezione.md). Le skill vengono costruite seguendo [`generazione-skill.md`](generazione-skill.md) e validate con [`validazione.md`](validazione.md).

## Metodologia di selezione

Criteri (uguali per ogni area):

1. **Operazione ricorrente / ripetitiva**: adempimento formale, relazione partendo da dati strutturati, compilazione documento normato.
2. **Documentazione ufficiale dettagliata** disponibile online da autorita' riconosciute (Gazzetta Ufficiale, Normattiva, Ministeri, INAIL, ENEA, GSE, MASE, MIT, MIMIT, ISPRA, Agenzia Entrate, ANAC, EUR-Lex, Banca d'Italia).
3. **Pain percepito**: gli ingegneri del settore lo trovano effettivamente noioso o complesso da fare manualmente.
4. **Rischio basso/medio e validabile**: l'output deve essere verificabile (checklist, conformita' formale).

Esclusi come fonte primaria gli standard a pagamento (UNI, ISO, IEC, SAE, PMI, AIAG-VDA): skill basate solo su norme a pagamento sono strutturalmente fragili per copyright. Quando applicabile, ripiegare su DM/regolamenti che richiamano la norma (es. DM 37/2008 al posto di UNI 7129).

---

# Parte 1 - Ingegneria civile

## Famiglie di task dell'ingegnere civile

| Famiglia                                      | Volume      | Time-consuming | Doc ufficiale                                  | Note                                  |
| --------------------------------------------- | ----------- | -------------- | ---------------------------------------------- | ------------------------------------- |
| Sicurezza cantieri (POS, PSC, PSS, fascicolo) | Altissimo   | Alto           | D.Lgs 81/08 All. XV - tabella contenuti minimi | Ideale: strutturato                   |
| Relazione CAM (appalti pubblici)              | Alto (PA)   | Alto           | DM 256/2022 - criteri puntuali                 | Obbligatorio da 2022                  |
| Prevenzione incendi (SCIA, valutazione)       | Medio-alto  | Altissimo      | DM 3/8/2015 RTO + 15+ RTV                      | Rischio: materia tecnica critica      |
| Strutture / NTC (relazione tecnica)           | Alto        | Alto           | NTC 2018 + Circ. 7/2019                        | Troppo ampio per skill singola        |
| Pratiche edilizie CILA/SCIA/PdC Toscana       | Altissimo   | Medio          | LR 65/2014 + regolamenti                       | Cambia spesso - 2019/20/21/24         |
| APE - Attestato Prestazione Energetica        | Alto        | Medio          | DM 26/6/2015 + SIERT Toscana                   | Workflow su piattaforma, poco margine |
| Progettazione opere pubbliche (PFTE/esec)     | Medio       | Alto           | D.Lgs 36/2023 + allegati                       | Checklist documentale utile           |
| Sismica / sismabonus / vulnerabilita'         | Alto        | Alto           | DM 58/2017 + NTC cap.8 + Circ.7/2019           |                                       |
| Pratiche strutturali (Genio Civile)           | Alto        | Medio          | L. 1086/1971 + L. 64/1974 + DPR 380            |                                       |
| Acustica edilizia (passiva)                   | Alto        | Medio          | DPCM 5/12/1997                                 |                                       |
| Idraulica / invarianza                        | Alto (reg.) | Medio          | DPGR 5/R 2020 (Tosc.) - RR 7/2017 (Lomb.)      |                                       |
| Catasto Pregeo/Docfa                          | Altissimo   | Alto           | AdE - vademecum nazionale                      |                                       |
| Modulistica edilizia + Salva Casa             | Altissimo   | Alto           | DPR 380 + DL 69/2024 + Funzione Pubblica       |                                       |
| Direzione lavori / contabilita'               | Alto        | Medio          | Variabile, prassi                              | Meno strutturato                      |
| Urbanistica / piani                           | Basso-medio | Alto           | Variabile comunale                             | Troppo frammentato                    |

## Ranking skill candidate civili

### Priorita' 1 - quick win (basso rischio, alto volume)

**1. POS Allegato XV - Checker & Assistant** (gia' skill in repo: [`pos-allegato-xv-checker`](../skills/pos-allegato-xv-checker/))
- Cosa fa: verifica che un POS copra tutti i contenuti minimi dell'Allegato XV punto 3.2 (dati impresa, lavorazioni, DPI, sostanze pericolose, rumore, formazione, procedure, etc.). Se manca qualcosa, lo segnala. Fornisce template compilabile.
- Perche' qui: documentazione puntuale (una tabella), rischio basso (verifica conformita' formale, non sostituisce CSE), volume altissimo.
- Sforzo: 3-5 giorni.
- Fonti: [tussl.it Allegato XV](https://tussl.it/allegati/allegato-xv), testo ufficiale D.Lgs 81/08.
- Validazione: 10 POS reali (anonimizzati), confronto con checklist cartacea.

**2. Relazione CAM DM 256/2022 - Guided draft**
- Cosa fa: data la tipologia di opera, genera struttura della Relazione CAM con capitoli obbligatori e per ciascun criterio richiede input al progettista. Produce prima bozza.
- Perche' qui: decreto strutturato, obbligatorio per appalti PA dal 2022, valore economico percepito alto.
- Sforzo: 5-7 giorni.
- Fonti: [DM 256/2022 Allegato](https://www.bosettiegatti.eu/info/norme/statali/2022_dm_23_06_cam_edilizia_Allegato.pdf).

**3. Modulistica edilizia unificata + Salva Casa DL 69/2024** (CT.3)
- Cosa fa: dato l'intervento, indica modulo unificato (CILA, SCIA, PdC, SCIA alternativa) e relativi allegati; integra modifiche Salva Casa 2024-2025.
- Perche' qui: **volume strutturalmente massimo** fra ingegneri edili/architetti italiani; modulistica nazionale ufficiale aggiornata 27/3/2025 (Salva Casa).
- Fonti: [Funzione Pubblica - modulistica Salva Casa](https://www.funzionepubblica.gov.it/it/ministro/comunicazione/notizie/approvata-la-modulistica-edilizia-per-l-applicazione-del-salva-casa/), [DPR 380/2001](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:2001-06-06;380), [D.Lgs 222/2016](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2016-11-25;222).

**4. Pregeo 10 + Docfa 4** (CT.1 + CT.2)
- Cosa fa: assistente compilazione atti telematici Catasto Terreni (Pregeo) e Catasto Fabbricati (Docfa); riduce rifiuti telematici frequenti.
- Perche' qui: **volume altissimo** trasversale geometri+ingegneri edili; vademecum AdE pubblico ed esaustivo; rischio rifiuti = re-lavorazione.
- Fonti: [AdE Pregeo](https://www.agenziaentrate.gov.it/portale/schede/fabbricatiterreni/aggiornamento-catasto-terreni-pregeo), [AdE Docfa istruzioni](https://www.agenziaentrate.gov.it/portale/schede/fabbricatiterreni/aggiornamento-catasto-fabbricati-docfa/istruzioni-operative-docfa-professionisti).

### Priorita' 2 - alto valore con specializzazione

**5. SCIA antincendio RTO/RTV - Navigator**
- Codice ben strutturato (RTO + RTV), doc VVF ufficiale. Da posizionare come "assistente di consultazione".
- Sforzo: 7-10 giorni (mappare tutte le RTV).
- Fonti: [vigilfuoco.it codice prevenzione incendi](https://www.vigilfuoco.it/servizi-le-aziende-e-i-professionisti/prevenzione-incendi/testi-coordinati-di-prevenzione/codice-prevenzione-incendi).

**6. Pratiche edilizie Toscana LR 65/2014 - Document checker**
- LOCALE Toscana. Rischio: normativa cambia spesso (4 aggiornamenti 2019-2024).
- Sforzo: 5-7 giorni.
- Fonti: [LR 65/2014](https://raccoltanormativa.consiglio.regione.toscana.it/articolo?urndoc=urn%3Anir%3Aregione.toscana%3Alegge%3A2014-11-10%3B65), [Regolamenti attuativi](https://www.regione.toscana.it/-/regolamenti-attuativi).

**7. Classificazione rischio sismico DM 58/2017 - Asseverazione** (CV.1)
- Cosa fa: calcolo classe di rischio pre/post intervento + generazione Allegato B; guida alla compilazione asseverazione.
- Perche' qui: alto volume sismabonus, doc ufficiale completa e gratuita (MIT), Allegato A tabellato, output strutturato (Allegato B).
- Fonti: [DM 58/2017 MIT](https://www.mit.gov.it/normativa/decreto-ministeriale-numero-58-del-28022017), [DM 65/2017 MIT](https://www.mit.gov.it/normativa/decreto-ministeriale-numero-65-del-07032017).

**8. Pratiche strutturali Genio Civile - Decision tree**
- Cosa fa: dato l'intervento, distingue obbligo denuncia art. 65 DPR 380 (L. 1086/1971) vs autorizzazione/deposito sismico (L. 64/1974 + DPR 380 artt. 93-94bis); per Toscana, classificazione rilevante/minore rilevanza/priva (LR 65/2014 art. 170-bis).
- Perche' qui: alto volume (zone 1-2-3 = quasi tutta Italia), errori frequenti con sanzioni penali, doc gratuita.
- Fonti: [L. 1086/1971](https://www.bosettiegatti.eu/info/norme/statali/1971_1086.htm), [L. 64/1974](https://www.bosettiegatti.eu/info/norme/statali/1974_0064.htm), [DPR 380/2001](https://www.bosettiegatti.eu/info/norme/statali/2001_0380.htm).

**9. Invarianza idraulica Toscana DPGR 5/R/2020**
- Cosa fa: assistente calcolo volumi compensativi e classi pericolosita' per relazione invarianza.
- Perche' qui: territorio toscano, normativa locale gratuita ben strutturata, alto pain. Modello replicabile (Lombardia RR 7/2017, Emilia DGR 2112/2016) come pacchetti separati per regione.
- Fonti: [DPGR Toscana 5/R 2020](https://raccoltanormativa.consiglio.regione.toscana.it/articolo?urndoc=urn%3Anir%3Aregione.toscana%3Aregolamento.giunta%3A2020-01-30%3B5%2FR), [RR Lombardia 7/2017](https://normelombardia.consiglio.regione.lombardia.it/normelombardia/Accessibile/main.aspx?view=showdoc&iddoc=rr002017112300007).

### Priorita' 3 - utili ma piu' complesse

**10. NTC 2018 + Circ. 7/2019 - Query assistant**
- Risponde a domande puntuali su NTC citando paragrafo e Circolare. Non calcola, non dimensiona.
- Sforzo: 3-4 giorni.
- Fonti: [NTC 2018 GU 42/2018](https://www.gazzettaufficiale.it/eli/id/2018/2/20/18A00716/sg), [Circ. 7/2019](https://www.gazzettaufficiale.it/eli/id/2019/02/11/19A00855/sg).

**11. PFTE D.Lgs 36/2023 - Checklist progettazione** (PR.1)
- Cosa fa: dato livello progettuale (PFTE), elenca documenti obbligatori art. 41 + Allegato I.7; integra correttivo D.Lgs 209/2024.
- Perche' qui: volume altissimo PA, evergreen 2025-2030, pain alto perche' PFTE sostituisce progetto definitivo.
- Sforzo: 2-3 giorni (versione checklist) + 5 giorni (estensione bandi-tipo ANAC).
- Fonti: [D.Lgs 36/2023](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2023-03-31;36), [ANAC](https://www.anticorruzione.it/).

**12. Verifica vulnerabilita' NTC cap. 8 + Circ. 7/2019**
- Cosa fa: assistente Q&A su LC/FC, distinzione adeguamento/miglioramento/locale (par. 8.4).
- Rischio: alto (sicurezza strutturale), posizionare come "consultazione norma", non sostituzione del progettista.

**13. Verifica requisiti acustici passivi DPCM 5/12/1997**
- Cosa fa: check limiti per categoria edificio (R'w, D2m,nT,w, L'n,w, LASmax, LAeq).
- Volume: alto (qualsiasi nuovo edificio o ristrutturazione pesante); rischio: contenzioso post-vendita.
- Fonti: [DPCM 5/12/1997](https://www.gazzettaufficiale.it/eli/id/1997/12/22/097A9933/sg), [PDF ANIT](https://www.anit.it/wp-content/uploads/2015/02/DPCM-5-dicembre-1997.pdf).

**14. Verifiche ascensori DPR 162/1999**
- Volume alto (ogni condominio), iter procedurale.
- Fonti: [DPR 162/1999](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1999-04-30;162).

**15. Relazione geologica/geotecnica NTC cap. 6** (GT.1)
- Volume altissimo trasversale a tutta edilizia strutturale; pain alto perche' richiede integrazione geologo+strutturista.

### Escluse / rimandate (civile)

- **APE**: il workflow gira su piattaforma SIERT, la skill puo' pre-validare ma aggiunge poco valore.
- **Calcoli strutturali FEM completi** (modello edificio non lineare, push-over, time-history): dominio di software dedicati (SAP2000, Midas, ProSap, Dolmen, EdiLus). Validazione decennale, responsabilita' del progettista, casi limite insidiosi. **Nota**: questa esclusione non copre i calcoli normativi tabellari, le formule chiuse NTC e i pre-dimensionamenti, vedi sezione "Calcoli ingegneristici code-driven".
- **Urbanistica comunale**: troppo frammentata, meglio piano a piano.
- **Acustica edilizia UNI 11367/11444 (classificazione)**: norma a pagamento, skill puo' ragionare su metodo ma non riprodurre tabelle.
- **BIM Capitolato Informativo UNI 11337**: norma a pagamento. Alternativa praticabile: skill di compliance su DM 312/2021 (soglie obbligo BIM PA: 15M dal 2022, 5,35M dal 2023, 1M dal 2025), [DM 312/2021](https://www.mit.gov.it/normativa/decreto-ministeriale-numero-312-del-02082021).
- **Collaudo statico DPR 380 art. 67**: skill nicchia ma alto valore, rimandata.

## Calcoli ingegneristici code-driven

> **Premessa metodologica.** Le skill possono includere codice Python/TS eseguito deterministicamente. Per un calcolo ingegneristico (formula chiusa o iterazione semplice), il codice elimina l'errore stocastico tipico degli LLM su numeri e produce output **verificabile e riproducibile** (test suite contro Excel ufficiali / software certificati). Questo cambia il calcolo del rischio: una skill code-driven su NTC ha rischio **inferiore** a una skill testuale di consultazione, non superiore.
>
> **Perimetro corretto.** Skill code-driven adatte a: pre-dimensionamenti, calcoli normativi tabellari, formule chiuse NTC/Eurocodici (parte gratuita), lookup parametri (vento, neve, sismica), combinazioni di carico, verifiche puntuali sezioni. **Non** adatte a: analisi modale di struttura completa, push-over, time-history, modellazione non lineare, restano dominio FEM dedicato.
>
> **Posizionamento.** L'output e' sempre verificato dal progettista (asseveratore firma, non l'AI). Le skill forniscono **check + bozza**, non sostituiscono il professionista. Il requisito NTC 2018 §10.2 sull'affidabilita' dei codici di calcolo si applica al software FEM, non a un calcolatore di formula chiusa con test suite pubblica.

| #     | Skill                                                                                                                                                       | Doc ufficiale                                                                                                                                          | Volume                            | Pain        | Rischio                                          |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------- | ----------- | ------------------------------------------------ |
| SC.1  | **Spettro di risposta NTC §3.2** - input: coordinate sito + vita nominale + classe uso + cat. sottosuolo. Output: ag, F0, T*c per SLO/SLD/SLV/SLC + Se(T)   | [NTC 2018 §3.2 + Allegato A](https://www.gazzettaufficiale.it/eli/id/2018/2/20/18A00716/sg) + [reticolo INGV](http://zonesismiche.mi.ingv.it/)         | Altissimo (ogni progetto sismico) | Medio       | Basso (deterministico, verificabile vs Excel CSLP) |
| SC.2  | **Calcolo PAM (Perdita Annua Media) sismabonus** DM 58/2017 Allegato A - classe rischio pre/post intervento                                                 | [DM 58/2017 Allegato A](https://www.mit.gov.it/normativa/decreto-ministeriale-numero-58-del-28022017) (formule esplicite)                              | Alto (sismabonus)                 | Alto        | Medio (asseverazione, sinergia con CV.1)         |
| SC.3  | **Combinazioni di carico NTC §2.5.3** SLU/SLE/sismica - matrice combinazioni con γ, ψ0, ψ1, ψ2                                                               | NTC 2018 §2.5.3 (tabella)                                                                                                                              | Altissimo                         | Medio       | Basso                                            |
| SC.4  | **Carichi vento NTC §3.3** - pressione cinetica qb + ce + cp per geometria edificio                                                                         | NTC 2018 §3.3 + Circ. 7/2019                                                                                                                           | Alto                              | Medio       | Basso                                            |
| SC.5  | **Carichi neve NTC §3.4** - qsk + μ1 + ce + ct per copertura (1-2 falde, multipla)                                                                          | NTC 2018 §3.4 + Circ. 7/2019                                                                                                                           | Alto                              | Basso-medio | Basso                                            |
| SC.6  | **Pre-dimensionamento sezione c.a. SLU flessione semplice** - dato b, h, As, fck, fyk → MRd                                                                 | NTC 2018 §4.1.2.1 + Circ. 7/2019 (formule chiuse)                                                                                                      | Alto                              | Basso       | Basso (pre-dim, non sostituisce verifica completa) |
| SC.7  | **Trasmittanza U pareti opache** stratigrafico - dato pacchetto layer → Uw + verifica DM 26/6/2015                                                          | DM 26/6/2015 + UNI 10355 (lookup λ materiali)                                                                                                          | Alto (APE, Ecobonus)              | Medio       | Basso                                            |
| SC.8  | **Periodo proprio T1 approssimato NTC §7.3.3.2** - C1·H^(3/4) per stima preliminare                                                                         | NTC 2018 §7.3.3.2                                                                                                                                      | Medio                             | Basso       | Basso                                            |
| SC.9  | **Capacita' portante fondazione superficiale NTC §6.4.2** - formula Brinch-Hansen/Vesic                                                                     | NTC 2018 §6.4 + Circ. 7/2019                                                                                                                           | Medio                             | Medio       | Medio (pre-dim)                                  |
| SC.10 | **Cedimenti edometrici NTC §6.2** - formula compressione monodimensionale                                                                                   | NTC 2018 §6.2 + Circ. 7/2019                                                                                                                           | Medio                             | Medio       | Medio (pre-dim)                                  |

**Validazione richiesta** per ogni skill code-driven: test suite con casi di confronto contro fogli Excel ufficiali (es. CSLP per spettro NTC) o software certificati (10 casi reali pre-rilascio).

**Top SC**: `SC.1 Spettro NTC` (volume altissimo, verificabile vs Excel CSLP, prerequisito di ogni progetto sismico), `SC.3 Combinazioni di carico` (volume altissimo, errori frequenti su γ/ψ), `SC.2 PAM sismabonus` (sinergia diretta con CV.1 Classificazione rischio sismico).

---

# Parte 2 - Skill candidate multi-area

Legenda: Volume = stima frequenza nazionale. Pain = complessita' procedurale + tempo umano per pratica tipo. Rischio = severita' conseguenze errore.

## Software / AI / Data

| #    | Skill                                                                                                            | Doc ufficiale                                  | Volume | Pain      | Rischio |
| ---- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | ------ | --------- | ------- |
| SW.1 | **GDPR Registro trattamenti (art. 30) + DPIA (art. 35)**                                                          | GDPR Reg. UE 2016/679 + WP248 + linee guida Garante | Alto   | Alto      | Alto    |
| SW.2 | **Capitolato tecnico ICT per appalti PA**                                                                         | AgID linee guida ICT + D.Lgs 36/2023           | Medio  | Alto      | Medio   |
| SW.3 | **Documentazione AgID per riuso software PA** (modello.italia.it, manifest, README PA)                            | linee guida AgID Riuso 2017 + Developers Italia | Medio  | Medio     | Basso   |
| SW.4 | **WCAG 2.1 audit form** per servizi PA                                                                            | WCAG 2.1 + linee guida AgID accessibilita'      | Alto   | Medio-alto | Medio   |

**Top SW**: `SW.1 GDPR` (gia' skill in repo: [`gdpr-registro-dpia`](../skills/gdpr-registro-dpia/)).

## Cybersecurity

| #    | Skill                                                                                                                                                                                         | Doc ufficiale                                                                                                                                                                                                                          | Volume                              | Pain    | Rischio          | Timing                                |
| ---- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- | ------- | ---------------- | ------------------------------------- |
| CY.1 | **NIS2 self-assessment** (D.Lgs 138/2024)                                                                                                                                                      | D.Lgs 138/2024 + atti delegati ENISA                                                                                                                                                                                                   | Alto                                | Altissimo | Alto             | (gia' skill in repo: [`nis2-self-assessment`](../skills/nis2-self-assessment/)) |
| CY.2 | **Misure minime ICT AgID** (Circ. 2/2017 ABSC) - gap analysis                                                                                                                                  | Circolare AgID 2/2017 + 17 controlli ABSC                                                                                                                                                                                              | Alto                                | Alto    | Medio            |                                       |
| CY.3 | **ISO 27001 SoA** draft                                                                                                                                                                        | ISO 27001:2022 (norma a pagamento, struttura pubblica)                                                                                                                                                                                  | Medio                               | Alto    | Medio            |                                       |
| CY.4 | **DORA gap assessment 5 pillar** Reg. UE 2022/2554 - ICT risk, incident, testing, third-party, info-sharing                                                                                    | [Reg. UE 2022/2554](https://eur-lex.europa.eu/eli/reg/2022/2554/oj), [Banca d'Italia DORA](https://www.bancaditalia.it/compiti/vigilanza/normativa/archivio-norme/disposizioni/disp-vigilanza-su-DORA/)                              | Alto (banche, assicur., crypto)     | Alto    | Sanzioni         | In vigore 17/01/2025                  |
| CY.5 | **CRA Cyber Resilience Act** Reg. UE 2024/2847 - classificazione PDE + documentazione tecnica + SBOM + vulnerability handling                                                                  | [Reg. UE 2024/2847](https://eur-lex.europa.eu/eli/reg/2024/2847/oj)                                                                                                                                                                    | Altissimo (ogni produttore HW/SW IoT) | Alto    | CE marking bloccato | Reporting 11/9/2026, full 11/12/2027 |

**Top CY**: `CY.1 NIS2` per pubblico ampio; `CY.4 DORA` se target finance/ICT-to-finance; `CY.5 CRA` per produttori di prodotti con elementi digitali (timing 2026-2027).

## Automazione / Robotica

| #    | Skill                                                                                              | Doc ufficiale                                                | Volume | Pain | Rischio |
| ---- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | ------ | ---- | ------- |
| AU.1 | **Fascicolo tecnico macchine** (Reg. UE 2023/1230) - struttura + analisi rischi                     | Reg. UE 2023/1230 (in vigore 20/01/2027) + UNI EN ISO 12100  | Alto   | Alto | Medio   |
| AU.2 | **Performance Level / SIL** assistant                                                               | UNI EN ISO 13849-1 + IEC 62061 (norme a pagamento)            | Medio  | Alto | Alto    |
| AU.3 | **Manuale uso e manutenzione** template-driven da fascicolo tecnico                                 | Reg. UE 2023/1230 Allegato III                               | Alto   | Medio | Basso   |

**Top AU**: `AU.1 Fascicolo tecnico macchine`. Reg. UE 2023/1230 entra in vigore 20/01/2027, timing di skill perfetto per finestra 2026.

## Meccanica

Convergenza con automazione. Specifiche meccanica:

| #    | Skill                                                              | Doc ufficiale                              | Volume | Pain | Rischio |
| ---- | ------------------------------------------------------------------ | ------------------------------------------ | ------ | ---- | ------- |
| ME.1 | **PED - Direttiva attrezzature pressione** (Reg. UE 2014/68)        | Direttiva PED 2014/68/UE + INAIL guide      | Medio  | Alto | Alto    |
| ME.2 | **ATEX - Direttiva atmosfere esplosive**                            | Direttiva 2014/34/UE + D.Lgs 81 Tit. XI    | Medio  | Alto | Alto    |

**Top ME**: `AU.1` piu' largamente applicabile. Per pure-meccanici, `ME.1 PED`.

## Chimica / Processi

| #    | Skill                                                                                                                                                  | Doc ufficiale                                                                                                                                                         | Volume                       | Pain | Rischio    |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- | ---- | ---------- |
| CH.1 | **AUA - Autorizzazione Unica Ambientale** (DPR 59/2013)                                                                                                 | DPR 59/2013 + regolamenti regionali                                                                                                                                   | Alto                         | Altissimo | Alto       |
| CH.2 | **Schede Sicurezza (SDS) REACH/CLP** - All. II Reg. 2020/878                                                                                            | Reg. 1907/2006 + 1272/2008 + 2020/878                                                                                                                                  | Altissimo                    | Alto | Alto       |
| CH.3 | **HAZOP study** structuring + report                                                                                                                    | IEC 61882 + UNI EN 31010 (norme a pag.)                                                                                                                                | Medio                        | Alto | Alto       |
| CH.4 | **Notifica stabilimento Seveso III - All. 5 D.Lgs 105/2015** + assoggettabilita' soglia inferiore/superiore                                              | [ISPRA Seveso III](https://www.isprambiente.gov.it/it/servizi/controlli-sui-pericoli-di-incidente-rilevante-direttiva-seveso-iii/documentazione-tecnica-e-normativa) | Basso-medio (~1000 stab.)    | Alto | Molto alto |

**Top CH**: `CH.1 AUA dossier`. Volume altissimo, doc strutturata, pain reale.

## Elettrica / Elettronica

| #    | Skill                                                                                                                                              | Doc ufficiale                                                                                          | Volume                  | Pain  | Rischio |
| ---- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ----------------------- | ----- | ------- |
| EL.1 | **DM 37/2008 - Dichiarazione conformita' impianti**                                                                                                  | DM 22/01/2008 n. 37                                                                                    | Altissimo               | Alto  | Medio   |
| EL.2 | **DPR 462/2001 - Verifiche periodiche messa a terra**                                                                                                | DPR 462/2001 + INAIL                                                                                   | Alto                    | Medio | Medio   |
| EL.3 | **Marcatura CE prodotti elettrici** (LVD, EMC, RED)                                                                                                  | 3 direttive + norme armonizzate                                                                        | Medio                   | Alto  | Alto    |
| EL.4 | **Valutazione CEM elettrodotti DPCM 8/7/2003** (50 Hz, calcolo DPA) - per nuove costruzioni vicino linee                                              | [DPCM 8/7/2003 elettrodotti](https://www.gazzettaufficiale.it/eli/id/2003/08/29/03A09749/sg)             | Medio                   | Medio | Alto    |

**Top EL**: `EL.1 DM 37/2008`. Volume altissimo, ogni installatore.

## Telecomunicazioni / CEM

| #    | Skill                                                                                                                                                  | Doc ufficiale                                                                                            | Volume                                       | Pain | Rischio |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- | -------------------------------------------- | ---- | ------- |
| TC.1 | **Pratica art. 87 Codice CCE (D.Lgs 259/2003)** - autorizzazione SRB / impianti radioelettrici, doc tecnica + simulazione CEM                            | [D.Lgs 259/2003](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2003-08-01;259) | Alto (post-5G, densificazione)               | Alto | Alto    |
| TC.2 | **Valutazione esposizione CEM SRB DPCM 8/7/2003** (100 kHz - 300 GHz) - limiti 20/6 V/m, simulazione                                                    | [DPCM 8/7/2003 SRB](https://www.gazzettaufficiale.it/eli/id/2003/08/28/03A09711/sg)                      | Medio                                        | Alto | Alto    |

**Top TC**: `TC.1 + TC.2` combinabili, settore con pubblico professionale ampio (operatori telecom + tower companies + studi consulenza CEM); doc pubblica e stabile; pain procedurale reale (SUAP + ARPA + 90 gg).

## Energy / Rinnovabili

| #    | Skill                                                                                                                                                                                                                                                                                                                                                                                  | Doc ufficiale                                                                                                                                                                                                                                                                              | Volume                                  | Pain      | Rischio                              |
| ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------- | --------- | ------------------------------------ |
| EN.1 | **Diagnosi energetica D.Lgs 102/2014** (UNI CEI EN 16247)                                                                                                                                                                                                                                                                                                                              | D.Lgs 102/2014 + DM 100/2023                                                                                                                                                                                                                                                              | Alto                                    | Alto      | Medio                                |
| EN.2 | **Modello Unico GSE per FV domestici** (<200 kW)                                                                                                                                                                                                                                                                                                                                       | Decreto MISE + procedura GSE                                                                                                                                                                                                                                                              | Alto                                    | Alto      | Medio                                |
| EN.3 | **Pratica TICA Terna/E-Distribuzione**                                                                                                                                                                                                                                                                                                                                                  | TICA delibera ARERA 99/2008                                                                                                                                                                                                                                                                | Medio                                   | Alto      | Medio                                |
| EN.4 | **Detrazioni ecobonus / superbonus** - pratica ENEA con asseverazioni                                                                                                                                                                                                                                                                                                                  | DM 6/8/2020 + linee guida ENEA                                                                                                                                                                                                                                                            | Alto                                    | Altissimo | Alto                                 |
| EN.5 | **Configurazione CER + qualifica GSE DM 7/12/2023** - perimetro cabina primaria, statuto, TIAD, simulazione autoconsumo virtuale                                                                                                                                                                                                                                                       | [GSE Regole Operative CACER](https://www.gse.it/documenti_site/Documenti%20GSE/Servizi%20per%20te/AUTOCONSUMO/Gruppi%20di%20autoconsumatori%20e%20comunita%20di%20energia%20rinnovabile/Regole%20e%20procedure/ALLEGATO%201%20Regole%20Operative%20CACER.pdf), [Portale GSE Autoconsumo](https://www.gse.it/servizi-per-te/autoconsumo) | Molto alto (boom 2024-2026 PNRR)         | Alto      | Medio                                |
| EN.6 | **Piano Transizione 5.0 - asseverazione tecnica EGE/ESCO** + calcolo riduzione consumi (≥3% impianto / ≥5% processo)                                                                                                                                                                                                                                                                   | [DM 24/7/2024](https://www.gazzettaufficiale.it/eli/id/2024/08/06/24A04160/SG), [GSE TR5](https://www.gse.it/servizi-per-te/attuazione-misure-pnrr/transizione-5-0/come-accedere)                                                                                                          | Altissimo                               | Molto alto | Resp. penale falsa asseveraz.        |

**Top EN**: `EN.6 Transizione 5.0` (HOT 2024-2026, scadenze GSE feb 2026), `EN.5 CER GSE` (boom PNRR). `EN.1 Diagnosi energetica` resta candidata robusta evergreen.

## Ambiente / Sostenibilita'

| #     | Skill                                                                                                                                              | Doc ufficiale                                                                                                                                                                                                                            | Volume                          | Pain  | Rischio                          |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- | ----- | -------------------------------- |
| AM.1  | **MUD - Modello Unico Dichiarazione ambientale** annuale                                                                                            | DPCM 28/12/2017 + UnionCamere                                                                                                                                                                                                            | Altissimo                       | Alto  | Alto                             |
| AM.2  | AUA / AIA dossier (vedi CH.1, sinergica)                                                                                                            | come sopra                                                                                                                                                                                                                              | Alto                            | Alto  | Alto                             |
| AM.3  | **Bonifica siti contaminati** (D.Lgs 152/06 Tit V) - piano caratterizzazione                                                                        | D.Lgs 152/06 + linee guida ISPRA                                                                                                                                                                                                        | Medio                           | Alto  | Alto                             |
| AM.4  | **MOG D.Lgs 231/2001 parte ambientale** - mappatura rischi reato                                                                                    | D.Lgs 231/2001 + 152/2006                                                                                                                                                                                                                | Medio                           | Alto  | Alto                             |
| AM.5  | **Verifica assoggettabilita' VIA (screening) art. 19 + DM 52/2015**                                                                                  | [Indicazioni operative MASE](https://va.mite.gov.it/it-IT/ps/Comunicazione/IndicazioniOperativeVAVIA), [Allegati 152/06](https://www.bosettiegatti.eu/info/norme/statali/2006_0152_allegati.htm)                                       | Alto                            | Medio | Medio                            |
| AM.6  | **Studio Impatto Ambientale (SIA) Allegato VII** - struttura/checklist                                                                              | come sopra                                                                                                                                                                                                                              | Medio (progetti grandi)         | Alto  | Alto                             |
| AM.7  | **Autorizzazione scarichi industriali art. 124 D.Lgs 152/06** (residuale rispetto AUA)                                                              | [Art. 124 D.Lgs 152/06](https://www.gazzettaufficiale.it/atto/serie_generale/caricaArticolo?art.idArticolo=124&art.codiceRedazionale=006G0171)                                                                                          | Alto                            | Medio | Alto (sanzioni penali art. 137)  |
| AM.8  | **Piano di lavoro amianto art. 256 D.Lgs 81/08 + DM 6/9/1994** - notifica ASL 30 gg, DPI, procedure rimozione                                       | [DM 6/9/1994](https://www.gazzettaufficiale.it/eli/id/1994/09/20/094A5917/sg)                                                                                                                                                            | Molto alto                      | Medio | Alto                             |
| AM.9  | **Documentazione previsionale impatto acustico L. 447/95 + DPCM 14/11/1997** - SCIA/PdC attivita' produttive, locali pubblici                       | [Legge 447/95](https://www.mase.gov.it/portale/documents/d/guest/legge_26_10_95_447-pdf-1), [DPCM 14/11/1997](https://www.anit.it/wp-content/uploads/2015/02/DPCM_14_11_19971.pdf)                                                       | Molto alto                      | Medio | Medio                            |
| AM.10 | **Valutazione previsionale clima acustico** (scuole/ospedali/RSA/residenze)                                                                          | come sopra                                                                                                                                                                                                                              | Alto                            | Medio | Medio                            |
| AM.11 | **Mappatura acustica strategica D.Lgs 194/2005** - agglomerati >100k ab + infrastrutture, modellistica CNOSSOS-EU                                   | [D.Lgs 194/2005](https://www.bosettiegatti.eu/info/norme/statali/2005_0194.htm)                                                                                                                                                          | Basso (grandi enti, 5-anni)     | Molto alto | Medio (infrazioni UE)            |
| AM.12 | **Autorizzazione emissioni atmosfera art. 269 D.Lgs 152/06** (per non-AUA)                                                                          | [Art. 269](https://www.gazzettaufficiale.it/atto/serie_generale/caricaArticolo?art.idArticolo=269&art.codiceRedazionale=006G0171)                                                                                                       | Alto                            | Alto  | Alto (sanzioni art. 279)         |

**Top AM**: `AM.1 MUD` (annuale, scadenza fissa, doc puntuale); `AM.9 Impatto acustico` (volume altissimo, doc gratuita); `AM.8 Piano amianto` (volume strutturalmente alto, doc puntuale DM 6/9/1994).

## Sicurezza lavoro

| #    | Skill                                                                                                                                              | Doc ufficiale                                                                                                                                                                                                                            | Volume    | Pain      | Rischio                                       |
| ---- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | --------- | --------------------------------------------- |
| SL.1 | **DVR - Documento Valutazione Rischi** (art. 28-29 D.Lgs 81) - gia' skill in repo: [`dvr-generico`](../skills/dvr-generico/)                        | D.Lgs 81/2008 + INAIL strumenti settoriali                                                                                                                                                                                              | Altissimo | Altissimo | Alto                                          |
| SL.2 | **DUVRI - Valutazione Rischi Interferenze** (art. 26)                                                                                              | art. 26 D.Lgs 81 + INAIL                                                                                                                                                                                                                | Alto      | Alto      | Alto                                          |
| SL.3 | **Stress lavoro-correlato** (Acc. 2010 + INAIL)                                                                                                    | Acc. 2010 + INAIL metodologia                                                                                                                                                                                                           | Medio     | Medio     | Medio                                         |
| SL.4 | **Piano emergenza** (DM 2/9/2021)                                                                                                                  | DM 2/9/2021 + UNI ISO 22320                                                                                                                                                                                                              | Medio     | Medio     | Alto                                          |
| SL.5 | **DPR 177/2011 - Procedura ingressi ambienti confinati** - qualificazione impresa + procedure operative                                            | [DPR 177/2011](https://www.gazzettaufficiale.it/eli/id/2011/11/08/011G0219/sg), [Manuale Min. Lavoro ambienti confinati](https://www.lavoro.gov.it/temi-e-priorita/salute-e-sicurezza/focus-on/commissione-consultiva-permanente/Documents/manuale-ambienti-confinati.pdf) | Medio     | Alto      | Molto alto (incidenti mortali frequenti)      |

**Top SL**: `SL.1 DVR` (gia' skill in repo). Trasversale a OGNI settore.

## Trasporti / Logistica

| #    | Skill                                                                                                                                                                                                                                                  | Doc ufficiale                                                                                                                                                                            | Volume                  | Pain       | Rischio |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- | ---------- | ------- |
| TR.1 | **ADR - relazione annuale consulente trasporti merci pericolose**                                                                                                                                                                                       | D.Lgs 40/2000 + Acc. ADR 2025                                                                                                                                                            | Alto                    | Alto       | Alto    |
| TR.2 | **Piano sicurezza trasporto rifiuti**                                                                                                                                                                                                                   | D.Lgs 152/2006                                                                                                                                                                            | Medio                   | Medio      | Medio   |
| TR.3 | **PUMS - Piano Urbano Mobilita' Sostenibile DM 397/2017** - obbligo Comuni >100k ab + citta' metropolitane, scenari + KPI + VAS                                                                                                                          | [Vademecum PUMS MIT](https://www.mit.gov.it/nfsmitgov/files/media/documentazione/2022-11/VademecumPUMS_ver.31122.pdf)                                                                  | Medio                   | Molto alto | Medio   |
| TR.4 | **Audit/RSIA sicurezza stradale D.Lgs 35/2011** (esteso D.Lgs 213/2021) - autostrade + strade tipo B fuori TEN                                                                                                                                          | [D.Lgs 35/2011](https://www.mit.gov.it/normativa/decreto-legislativo-numero-35-del-15032011)                                                                                            | Medio (in espansione)   | Alto       | Alto    |
| TR.5 | **Autorizzazione transiti eccezionali art. 10 CdS** + LG MIT 2022                                                                                                                                                                                       | [LG MIT trasporti eccezionali](https://www.mit.gov.it/nfsmitgov/files/media/normativa/2022-09/Allegato_1__LLGG_Trasporti_in_condizioni_di_eccezionalita.pdf)                            | Alto                    | Medio      | Medio   |

**Top TR**: `TR.1 ADR`. `TR.4 RSIA` in espansione post D.Lgs 213/2021. `TR.3 PUMS` per chi lavora con grandi Comuni.

## Biomedico

| #    | Skill                                                                | Doc ufficiale                                  | Volume | Pain      | Rischio |
| ---- | -------------------------------------------------------------------- | ---------------------------------------------- | ------ | --------- | ------- |
| BM.1 | **MDR - Fascicolo tecnico dispositivi medici Classe I/IIa**           | Reg. UE 2017/745 (MDR)                          | Alto   | Altissimo | Alto    |
| BM.2 | **Notifica DM al Ministero salute**                                   | DM 21/12/2009 + procedura ministeriale          | Medio  | Medio     | Medio   |

**Top BM**: `BM.1 MDR Classe I/IIa`. Mercato post-MDR pienamente applicato dal 2025.

## Management / Consulenza

| #    | Skill                                                                                                                                                                                                                                                                                                | Doc ufficiale                                                                                                                                                                                                                                                                                                                              | Volume                                       | Pain       | Rischio                              |
| ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------- | ---------- | ------------------------------------ |
| MG.1 | **Bilancio Sostenibilita' / CSRD ESRS** - struttura per PMI                                                                                                                                                                                                                                          | Direttiva CSRD 2022/2464 + ESRS PMI                                                                                                                                                                                                                                                                                                        | Bassa-media                                  | Altissimo  | Alto                                 |
| MG.2 | **MOG D.Lgs 231/2001** - mappatura rischi reato + parte speciale                                                                                                                                                                                                                                     | D.Lgs 231/2001                                                                                                                                                                                                                                                                                                                              | Media                                        | Alto       | Alto                                 |
| MG.3 | **Privacy Impact Assessment** + Registro (vedi SW.1)                                                                                                                                                                                                                                                | come SW.1                                                                                                                                                                                                                                                                                                                                   | Alta                                         | Alto       | Alto                                 |
| MG.4 | **CSRD ESRS E1 Climate Change** Reg. 2023/2772 + D.Lgs 125/2024 - GHG Scope 1-2-3, transition plan, targets                                                                                                                                                                                          | [D.Lgs 125/2024](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2024-09-06;125), [Reg. 2023/2772](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02023R2772-20231222)                                                                                                                              | Alto (in scaling)                            | Molto alto | -                                    |
| MG.5 | **DNSH PNRR (Tassonomia Reg. UE 2020/852)** - schede ex ante/ex post per progetti finanziati                                                                                                                                                                                                         | [Circolare MEF 33/2022](https://www.rgs.mef.gov.it/VERSIONE-I/circolari/2022/circolare_n_33_2022/), [Reg. UE 2020/852](https://eur-lex.europa.eu/eli/reg/2020/852/oj)                                                                                                                                                                       | Altissimo (progetti PNRR)                    | Alto       | Decadenza fondi PNRR                 |
| MG.6 | **CBAM declarant trimestrale Reg. UE 2023/956** - calcolo embedded emissions importazioni (ferro, acciaio, alluminio, cemento, fertilizz., H2, elettr.)                                                                                                                                              | [Reg. UE 2023/956](https://eur-lex.europa.eu/eli/reg/2023/956/oj), [ADM CBAM](https://www.adm.gov.it/portale/en/cbam-carbon-border-adjustment-mechanism), [MASE CBAM](https://www.ets.minambiente.it/CBAM)                                                                                                                                  | Alto (importatori metall./cementieri)        | Molto alto | Sanzioni 10-50 EUR/t CO2eq           |

**Top MG**: `MG.5 DNSH PNRR` (volume altissimo evergreen), `MG.6 CBAM` (timing 1/1/2026), `MG.2 MOG 231` (volume strutturale).

## Procurement PA

| #    | Skill                                                                                                                                                | Doc ufficiale                                                                                                                                                       | Volume                            | Pain | Rischio              |
| ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- | ---- | -------------------- |
| PR.1 | **PFTE D.Lgs 36/2023 art. 41 + Allegato I.7** + correttivo D.Lgs 209/2024 - elaborati cambiati, PFTE sostituisce PD                                  | [D.Lgs 36/2023](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2023-03-31;36), [ANAC](https://www.anticorruzione.it/)                  | Molto alto (ogni opera pubblica)  | Alto | Alto (esclusione gara) |
| PR.2 | **Documenti gara conformi bandi-tipo ANAC** - obbligo per stazioni appaltanti                                                                         | come sopra                                                                                                                                                          | Alto                              | Alto | Alto                 |
| PR.3 | **Valutatore offerte tecniche OEPV** (matrice criteri/sottocriteri Allegato II.4)                                                                     | come sopra                                                                                                                                                          | Alto                              | Alto | Alto (ricorso TAR)   |

**Top PR**: tutti e tre, sinergici, doc pubblica completa, volume altissimo PA.

## Catasto / Edilizia amministrativa

| #    | Skill                                                                                                                                                | Doc ufficiale                                                                                                                                                                                                | Volume     | Pain | Rischio |
| ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- | ---- | ------- |
| CT.1 | **Pregeo 10** (atti aggiornamento Catasto Terreni) - flusso telematico obbligatorio, rifiuti frequenti                                                | [AdE Pregeo](https://www.agenziaentrate.gov.it/portale/schede/fabbricatiterreni/aggiornamento-catasto-terreni-pregeo)                                                                                       | Alto       | Alto | Alto    |
| CT.2 | **Docfa 4** (Catasto Fabbricati) - vademecum nazionale ufficiale                                                                                      | [AdE Docfa](https://www.agenziaentrate.gov.it/portale/schede/fabbricatiterreni/aggiornamento-catasto-fabbricati-docfa/istruzioni-operative-docfa-professionisti)                                              | Alto       | Alto | Alto    |
| CT.3 | **Modulistica edilizia unificata + Salva Casa DL 69/2024** - CILA/SCIA/PdC/SCIA alternativa, aggiornata 27/3/2025                                     | [Funzione Pubblica - Salva Casa](https://www.funzionepubblica.gov.it/it/ministro/comunicazione/notizie/approvata-la-modulistica-edilizia-per-l-applicazione-del-salva-casa/)                                | Molto alto | Alto | Medio   |
| CT.4 | **Pratica unica SUAP attivita' produttive D.Lgs 222/2016** - tabella A regimi amministrativi                                                          | [D.Lgs 222/2016](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2016-11-25;222), [Impresainungiorno](https://www.impresainungiorno.gov.it/)                                       | Alto       | Alto | Medio   |

**Top CT**: `CT.3 Modulistica edilizia` (volume probabilmente il piu' alto in assoluto fra ingegneri edili/architetti italiani); `CT.1+CT.2 Pregeo+Docfa` (vademecum AdE pubblico, volume altissimo).

## CTU / Ingegneria forense

| #    | Skill                                                                                                                                                | Doc ufficiale                                                                                                                                                                                                | Volume                  | Pain | Rischio |
| ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------- | ---- | ------- |
| FR.1 | **Struttura relazione peritale CTU** (cpc artt. 191-201) + DM 109/2023 - quesiti, verbalizzazione operazioni peritali                                 | [DM 109/2023](https://www.gazzettaufficiale.it/eli/id/2023/08/11/23G00121/sg)                                                                                                                                | Alto (per CTU iscritti) | Alto | Alto    |
| FR.2 | **Calcolo liquidazione compensi CTU** DM 30/5/2002 + DPR 115/2002 - tariffe a vacazione/percentuale                                                   | [DPR 115/2002](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:2002-05-30;115)                                                                                  | Medio                   | Alto | Medio   |

**Top FR**: nicchia ma alto valore unitario. Buona per ingegneri civili che fanno CTU.

## Geotecnica (trasversale civile)

| #    | Skill                                                                                                                                                | Doc ufficiale                  | Volume                                | Pain | Rischio |
| ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ | ------------------------------------- | ---- | ------- |
| GT.1 | **Relazione geologica + geotecnica NTC 2018 cap. 6** - obbligatoria per ogni opera strutturale rilevante                                              | NTC 2018 + Circ. 7/2019 (cap. 6) | Alto (trasversale a edilizia strutturale) | Alto | Alto    |

## Hot topic 2025-2026 (regolamenti UE recenti, cross-area)

Sezione cross-settoriale per regolamenti UE/IT con timing critico 2024-2027. Ogni voce e' gia' citata anche nella sezione settoriale di pertinenza; qui consolidati per visibilita'.

| #    | Skill                                                | Settore                              | Timing                                                | Riferimento                                                            |
| ---- | ---------------------------------------------------- | ------------------------------------ | ----------------------------------------------------- | ---------------------------------------------------------------------- |
| HT.1 | **Piano Transizione 5.0**                             | Energy/industriale (EN.6)            | HOT 2024-2026 (scadenze GSE feb 2026)                  | DM 24/7/2024                                                           |
| HT.2 | **DORA gap assessment**                               | Cyber/finance (CY.4)                 | In vigore 17/01/2025                                   | Reg. UE 2022/2554                                                      |
| HT.3 | **CRA Cyber Resilience Act**                          | Cyber/produttori IoT (CY.5)          | Reporting 11/9/2026, full 11/12/2027                   | Reg. UE 2024/2847                                                      |
| HT.4 | **CBAM declarant trimestrale**                        | Management/import (MG.6)             | Full 1/1/2026                                          | Reg. UE 2023/956                                                       |
| HT.5 | **DNSH PNRR (Tassonomia)**                            | Management/PA (MG.5)                 | Evergreen PNRR fino 2026                               | Reg. UE 2020/852 + Circ. MEF 33/2022                                   |
| HT.6 | **CSRD ESRS E1 Climate**                              | Management/sostenibilita' (MG.4)     | Applicaz. progressiva 2024-2028                        | D.Lgs 125/2024 + Reg. 2023/2772                                        |
| HT.7 | **AI Act** classificazione + documentazione Annex IV  | Software/AI                          | Full 2/8/2027 (high-risk)                              | Reg. UE 2024/1689 - gia' skill in repo: [`ai-act-compliance`](../skills/ai-act-compliance/) |

## Skill scartate (consolidato)

### Civile

- **APE**: workflow su SIERT, skill aggiunge poco.
- **Calcoli strutturali FEM completi** (modello edificio, push-over, time-history): dominio software dedicati. **Non escluso**: calcoli normativi tabellari + pre-dim (vedi sezione "Calcoli ingegneristici code-driven" in Parte 1).
- **Urbanistica comunale**: troppo frammentata.
- **Acustica edilizia UNI 11367/11444**: norma a pagamento.
- **BIM Capitolato Informativo UNI 11337**: norma a pagamento (alternativa: DM 312/2021).
- **Collaudo statico DPR 380 art. 67**: nicchia, rimandata.

### Settori troppo verticali / pubblico ridotto

- **Navale** (RINA, SOLAS/MARPOL): mercato concentrato, ROI dubbio.
- **Aerospaziale** (EASA Part 21): settore concentrato (Leonardo, Avio). Alternativa accessibile: **Reg. UE 2019/947 droni/UAS** (volume superiore).
- **Ferroviario** (SMS D.Lgs 50/2019 ANSFISA): pochi soggetti (IF, GI).
- **DORA TLPT**: solo entita' significative + tester certificati.
- **Tassonomia minimum safeguards**: nicchia molto ristretta.

### Vincolo copyright (norme a pagamento come fonte primaria)

- **Gas civili UNI 7129/11528**: ripiegare su DM 37/2008 + DM 8/11/2019.
- **ISO 9001/14001/45001**: skill metodologica OK ma non literal compliance.
- **FMEA IEC 60812 / SAE J1739**: struttura dominio comune.
- **PMBOK / ISO 21502**: concetti base pubblico dominio.

### Timing prematuro

- **EPBD IV (Direttiva 2024/1275 Case Green)**: recepimento italiano in ritardo (deadline 29/5/2026).
- **ESPR / DPP (Reg. UE 2024/1781)**: atti delegati per categoria prodotto ancora in lavorazione.

---

# Parte 3 - Top integrato per priorita' complessiva

Re-ranking di TUTTA la lista (civile + multi-area) considerando: volume, doc ufficiale gratuita, pain, timing/HOT, rischio.

## Priorita' 1 - quick win (alto volume, doc completa)

1. **POS Allegato XV** - gia' skill in repo
2. **DVR generico (D.Lgs 81 art. 28-29)** - gia' skill in repo (`dvr-generico`), trasversale
3. **Modulistica edilizia unificata + Salva Casa DL 69/2024** (CT.3) - **VOLUME ALTISSIMO** trasversale
4. **Piano Transizione 5.0** (EN.6) - **TIMING PERFETTO** scadenze GSE feb 2026
5. **PFTE D.Lgs 36/2023 + bandi-tipo ANAC + valutatore OEPV** (PR.1+PR.2+PR.3) - **VOLUME ALTISSIMO** PA
6. **Pregeo 10 + Docfa 4** (CT.1+CT.2) - **VOLUME ALTISSIMO** ogni edile/civile
7. **CAM DM 256/2022** - obbligatorio appalti PA
8. **Pratiche edilizie LR 65/2014 Toscana** - asset locale
9. **Spettro di risposta NTC §3.2 code-driven** (SC.1) - prerequisito ogni progetto sismico, output verificabile vs Excel CSLP

## Priorita' 2 - alto valore con specializzazione

10. **Documentazione previsionale impatto acustico L. 447/95** (AM.9) - alta ricorrenza, doc gratuita
11. **Configurazione CER + qualifica GSE** (EN.5) - **HOT TOPIC PNRR** boom 2024-2026
12. **Classificazione rischio sismico DM 58/2017 + PAM code-driven** (CV.1 + SC.2) - alto volume sismabonus, Allegato B strutturato, calcolo PAM con formule esplicite Allegato A
13. **Combinazioni di carico NTC §2.5.3 code-driven** (SC.3) - volume altissimo, errori frequenti su γ/ψ, output deterministico
14. **Pratica art. 87 CCE - autorizzazione SRB + valutazione CEM** (TC.1+TC.2) - settore telecom trascurato, post-5G
15. **Piano di lavoro amianto art. 256** (AM.8) - molto alto volume, doc puntuale
16. **DNSH PNRR (Tassonomia)** (MG.5) - obbligo per ogni progetto PNRR
17. **NIS2 self-assessment** (CY.1) - hot topic continuativo (gia' skill in repo)
18. **DM 37/2008 dichiarazione impianti** (EL.1) - volume altissimo

## Priorita' 3 - alto valore ma piu' complesse o di nicchia tecnica

19. **CBAM declarant trimestrale** (MG.6) - timing 1/1/2026, ricorrente trimestrale
20. **DORA gap assessment** (CY.4) - hot per banche/ICT, alta tariffa
21. **MUD ambientale** (AM.1) - annuale, scadenza fissa
22. **Verifica vulnerabilita' NTC cap. 8 + Denuncia opere strutturali** (CV NTC8 + L.1086/L.64)
23. **CRA documentazione tecnica + classificazione PDE** (CY.5) - 2026-2027 ramp-up
24. **AUA dossier** (CH.1) + **Audit sicurezza stradale RSIA** (TR.4) + **CSRD ESRS E1** (MG.4)
25. **Pacchetto NTC code-driven esteso**: carichi vento/neve §3.3-3.4 (SC.4+SC.5) + pre-dim sezione c.a. (SC.6) + trasmittanza U (SC.7) + periodo proprio T1 (SC.8) + capacita' portante fondazione (SC.9) + cedimenti edometrici (SC.10), completano la suite SC.1-SC.10 con validazione vs Excel/software

## Priorita' 4 - nicchie alto valore unitario / ROI dubbio

Seveso III notifica + RdS (CH.4), Mappatura acustica D.Lgs 194/2005 (AM.11), CTU (FR.1+FR.2), Verifiche ascensori DPR 162/1999, DPR 177/2011 ambienti confinati (SL.5), Diagnosi energetica (EN.1), MOG 231 (MG.2), MDR Classe I/IIa (BM.1), ADR (TR.1), Invarianza idraulica Toscana (locale).

---

# Indice rapido fonti ufficiali

- **Normativa nazionale**: [normattiva.it](https://www.normattiva.it/), [gazzettaufficiale.it](https://www.gazzettaufficiale.it/), [bosettiegatti.eu](https://www.bosettiegatti.eu/) (testi coordinati non ufficiali ma comodi)
- **UE**: [eur-lex.europa.eu](https://eur-lex.europa.eu/)
- **Edilizia/strutture/sismica**: [MIT](https://www.mit.gov.it/), [Protezione Civile](https://www.protezionecivile.gov.it/), [INGV reticolo sismico](http://zonesismiche.mi.ingv.it/), [Funzione Pubblica modulistica](https://www.funzionepubblica.gov.it/)
- **Ambiente**: [MASE](https://www.mase.gov.it/), [ISPRA](https://www.isprambiente.gov.it/), ARPA regionali, [va.mite.gov.it (VIA/VAS)](https://va.mite.gov.it/)
- **Energia/CER/Transizione 5.0**: [GSE](https://www.gse.it/), ENEA, MIMIT
- **Sicurezza lavoro**: [INAIL](https://www.inail.it/), [Min. Lavoro](https://www.lavoro.gov.it/)
- **Antincendio**: [vigilfuoco.it](https://www.vigilfuoco.it/)
- **Telecomunicazioni**: AGCOM, MIMIT, ARPA
- **Trasporti**: [MIT](https://www.mit.gov.it/), [aci.gov.it](https://www.aci.gov.it/), ANSFISA
- **Catasto**: [Agenzia Entrate](https://www.agenziaentrate.gov.it/)
- **Appalti/PA**: [ANAC](https://www.anticorruzione.it/), AgID
- **CSRD/ESG/PNRR**: EFRAG, MEF (RGS), Commissione UE
- **Finanza/cyber**: [Banca d'Italia](https://www.bancaditalia.it/), IVASS, CONSOB, ENISA
- **Giustizia/CTU**: [Min. Giustizia](https://www.giustizia.it/)
