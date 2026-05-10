# Task: Mappatura rischi tipici per mansione

Per una specifica mansione lavorativa, identifica i rischi tipici attesi (con riferimento ai Titoli D.Lgs. 81/2008) e le misure preventive/protettive standard. Strumento di supporto al `draft-dvr.md` o per pre-analisi rapide.

## Obiettivo

Tabella rischi-misure-DPI per la mansione richiesta, con riferimenti normativi.

## Input richiesti

- Mansione (es. operaio metalmeccanico, impiegato amministrativo, autista trasporti, infermiere, addetto cucina)
- Settore aziendale (per contestualizzare)
- Eventuali specificita' (turni notturni, esposizioni particolari)

## Fonti

Leggere prima: `references/estratti/dlgs-81-art-17-28-29.md` (tassonomia generale).

Per Titoli specifici, consultare il testo vigente su normattiva.it (URL in `references/sources.yaml`); estratti specifici per Titoli particolari da integrare in iterazioni successive.

## Procedura

### Passo 1 - Identificare il "profilo di rischio base" della mansione

Mappare la mansione ad uno o piu' "profili di rischio base":

| Profilo | Mansioni tipiche | Rischi principali attesi |
|---------|------------------|---------------------------|
| Ufficio / VDT | Impiegato amministrativo, programmatore, designer, contabile | VDT, postura, illuminazione, stress, microclima, elettrocuzione |
| Magazzino / logistica | Magazziniere, mulettista, picker, addetto spedizione | MMC, schiacciamento mezzi, urti, caduta materiale, rumore parziale |
| Produzione meccanica | Operaio CNC, saldatore, addetto presse, manutentore | Rumore, vibrazioni, taglio/abrasione, schiacciamento, CEM (saldatura), polveri metalliche, fumi saldatura |
| Edilizia / cantieri | Muratore, carpentiere, gruista, lattoniere | Rinvio POS - cantieri |
| Sanita' | Infermiere, OSS, medico, tecnico lab | Biologico (sangue, contatto), chimico (disinfettanti, citostatici), MMC pazienti, stress, aggressioni |
| Servizi alla persona | Parrucchiere, estetista, fisioterapista | Chimico (tinture, smacchianti), MMC posturale, biologico (sangue/cute) |
| Ristorazione | Cuoco, lavapiatti, cameriere | Microclima caldo, taglio, ustione, scivolamento, MMC, biologico (alimenti) |
| Trasporti | Autista, fattorino, corriere | MMC, postura, stress, alcoldroghe, vibrazioni corpo intero, sicurezza stradale |
| Pulizie | Addetto pulizie | Chimico (detergenti), MMC, biologico (rifiuti), elettrocuzione (apparecchi), scivolamento |
| Insegnamento | Docente, ricercatore | Voce, stress, microclima aula, chimico (laboratori) |
| Commercio | Cassiere, addetto vendita | Postura statica, MMC scaffali, aggressioni (rapine), microclima, stress da contatto pubblico |
| Sicurezza / vigilanza | Guardia giurata | Aggressioni, stress, turni notturni, mezzi |

Identificare il/i profilo/i applicabili.

### Passo 2 - Generare tabella rischi-misure per la mansione

Esempio per mansione "Impiegato amministrativo VDT" (profilo Ufficio):

```markdown
## Mansione: Impiegato amministrativo VDT

| Rischio | Riferimento | Misure preventive | Misure protettive | DPI | Note |
|---------|-------------|-------------------|-------------------|-----|------|
| **VDT - postura** | Titolo VII | Sedia ergonomica regolabile + scrivania regolabile altezza + posizione monitor a 50-70cm + supporto polsi | Pausa visiva 15min ogni 2h continuative VDT | N/A | Allegato XXXIV requisiti minimi |
| **VDT - illuminazione** | Titolo VII | Illuminazione 300-500 lux su scrivania + assenza riflessi monitor | Tende/veneziane regolabili | N/A | UNI EN 12464-1 |
| **VDT - eyestrain** | Titolo VII | Software di pausa visiva + monitor con anti-glare | Sorveglianza sanitaria oftalmica per VDT > 20h/sett | Eventuali occhiali specifici (a carico DdL) | Art. 176 |
| **Stress lavoro-correlato** | Art. 28 co. 1-bis | Carico lavoro proporzionato + chiarezza ruoli + pause + autonomia + comunicazione | Eventuali questionari fase 2 | N/A | Lettera circolare 18/11/2010 |
| **Microclima** | Titolo II | Climatizzazione 20-26 gradi C estate, 18-22 inverno | Adeguamento abbigliamento | N/A | UNI EN 7730 (comfort termico) |
| **Elettrocuzione** | Titolo III | Impianti a norma CEI 64-8 + multiprese conformi | Differenziali (DPI = N/A) | N/A | DPR 462/2001 verifiche periodiche |
| **Incendio** | Titolo II + DM 02/09/2021 | Vie esodo segnalate, estintori | Piano emergenza, addetti AI | Maschera anti-fumo (presente in cassetta emergenza) | DM antincendio 2021 |

Mansioni ergonomiche tipiche per la categoria:
- Postazione regolabile (sedia altezza + monitor altezza + tastiera staccata)
- Pause programmate
- Possibilita' di smart working (richiede DVR specifico per domicilio)

Sorveglianza sanitaria:
- Visita iniziale + biennale per VDT > 20h/sett (annuale per > 50 anni o limitazioni)
- Visita specialistica oftalmica
```

### Passo 3 - Per profili a maggior rischio, dettaglio specifico

#### Profilo Produzione meccanica - dettaglio operaio CNC

```markdown
| Rischio | Riferimento | Misure preventive | Misure protettive | DPI |
|---------|-------------|-------------------|-------------------|-----|
| Taglio / lacerazione | Art. 71-72 (attrezzature) | Protezioni interbloccate sulla macchina, formazione utilizzo | Procedura di emergenza | Guanti taglio EN 388 livello 5, scarpe S3 |
| Rumore | Titolo VIII Cap II | Macchine con riduttore rumore + insonorizzazione cabina | Rotazione personale | Cuffie SNR>30 dB se LEX,8h > 85 dB |
| Vibrazioni mano-braccio | Titolo VIII Cap III | Attrezzi a bassa vibrazione + manutenzione | Rotazione | Guanti antivibrazione EN ISO 10819 |
| Trucioli / schegge | Art. 71 | Schermo macchina, aspirazione | Procedura raccolta scarti | Occhiali EN 166 |
| Olio da taglio (chimico) | Titolo IX | Chiusura serbatoi, aspirazione nebbie | Lavaggio mani frequente | Guanti chimici EN 374, occhiali |
| Postura statica + MMC | Titolo VI | Pause regolari + alternanza | Esercizi ergonomici | N/A |
| Elettrocuzione | Titolo III | Impianti a norma | Manutenzione periodica | N/A diretto, scarpe S3 con isolamento |
```

#### Profilo Sanita' - dettaglio infermiere ospedale

```markdown
| Rischio | Riferimento | Misure | Procedure | DPI |
|---------|-------------|--------|-----------|-----|
| Biologico (HIV, HBV, HCV, ecc.) | Titolo X | Vaccinazioni + procedure punctura | Protocollo post-esposizione | Guanti latex/nitrile, mascherina, camice, occhiali se splash atteso |
| Chimico (disinfettanti) | Titolo IX | Areazione + diluizione corretta | SDS allegate | Guanti chimici, mascherina FFP2, occhiali |
| Citostatici (cancerogeno) | Titolo IX Cap II | Cappa di sicurezza + procedure preparazione | Sorveglianza sanitaria specifica | Guanti chemo, camice, mascherina, visiera |
| MMC pazienti (sollevamento, mobilizzazione) | Titolo VI | Solleva-pazienti, ausili | Formazione tecniche corrette | N/A |
| Aggressioni (PS, psichiatria) | Art. 28 | Sicurezza ambienti, allarme, addetti vigilanza | Procedura emergenza | N/A |
| Stress lavoro-correlato | Art. 28 co. 1-bis | Carico, turni gestiti, supporto psicologico | Valutazione fase 1+2 | N/A |
| Turni notturni | D.Lgs. 66/2003 | Limitazione successione notti | Visita annuale | N/A |
| Radiazioni ionizzanti (alcuni reparti) | D.Lgs. 101/2020 | Schermature, limitazione tempo | Sorveglianza dosimetrica | Camice piombato, visiera piombata |
```

#### Profilo Trasporti - dettaglio autista TIR

```markdown
| Rischio | Riferimento | Misure | DPI |
|---------|-------------|--------|-----|
| Sicurezza stradale | Reg. UE 165/2014 cronotachigrafo | Cronotachigrafo, pause obbligatorie | N/A diretto |
| Vibrazioni corpo intero | Titolo VIII Cap III | Sedile ammortizzato | N/A |
| MMC (carico/scarico) | Titolo VI | Mezzi meccanici (trans-pallet, sponda idraulica) | N/A |
| Postura prolungata | Art. 28 | Pause obbligatorie | N/A |
| Stress | Art. 28 co. 1-bis | Pianificazione turni, supporto | N/A |
| ADR (se merci pericolose) | Acc. ADR + D.Lgs. 40/2000 | Documentazione, formazione, equipaggiamento | DPI specifici per ADR (occhiali, guanti, scarpe S3) |
| Aggressioni / rapine | Art. 28 | Procedura, GPS tracking, comunicazione | N/A diretto |
| Sostanze psicoattive | D.Lgs. 81 art. 41 + Acc. Stato-Regioni | Sorveglianza obbligatoria | N/A |
```

### Passo 4 - Output

Per ogni mansione richiesta:

```markdown
# Mappa rischi - mansione [nome]

**Settore**: [...]
**Profilo di rischio base**: [...]
**Specificita' aziendali**: [...]

## Tabella rischi-misure-DPI

[tabella come sopra]

## Sorveglianza sanitaria
[indicazioni se applicabile]

## Formazione richiesta

- Formazione generale (4h) + specifica (X ore basate su rischio aziendale: 4 alto / 8 medio / 12 alto - Acc. Stato-Regioni)
- Formazione specifica:
  - Per VDT: informazione su rischi
  - Per uso DPI III categoria: addestramento documentato
  - Per attivita' a rischio specifico (lavori in quota, spazi confinati, ecc.): corsi abilitanti

## Limiti

- Mappa orientativa, va integrata e personalizzata sulla realta' aziendale
- I valori esatti (es. dB rumore, dosi chimico) richiedono misurazioni dirette
- Per mansioni ibride o nuove (es. operatore drone, IoT installer) puo' servire valutazione ad hoc

## Rinvio

**La mappa e' input al DVR. La valutazione effettiva richiede RSPP, eventuale medico competente, consultazione RLS, e l'applicazione di metodologie tecniche per i rischi specialistici (es. UNI EN ISO 11228 per MMC, UNI EN ISO 9612 per rumore, UNI EN ISO 5349 per vibrazioni mano-braccio, ecc.).**
```

## Casi limite

### Mansione ibrida (es. tecnico commerciale che fa anche manutenzione in cantieri)
Combinare due profili. Per mansione ibrida, la sorveglianza sanitaria si applica al profilo piu' rischioso.

### Nuove mansioni emergenti (es. operatore robotica collaborativa, addetto IoT manutenzione, data scientist)
Usare il profilo piu' simile come base + adattare per specificita' (es. data scientist = Ufficio + eventuali rischi etici/AI).

### Smart working / telelavoro
Profilo Ufficio si applica al domicilio del lavoratore. Il DVR deve includere sezione specifica (illuminazione, postazione, isolamento, emergenze a domicilio).

### Lavoratrici in stato di gravidanza
Per qualunque profilo, valutazione specifica D.Lgs. 151/2001: limitazioni di esposizione + cambio mansione se necessario.

## Limiti di questo task

- Mappa orientativa, basata su prassi e Titoli D.Lgs. 81 - non sostituisce valutazione tecnica del RSPP
- Mansioni molto specialistiche (es. saldatore subacqueo, addetto demolizione amianto) richiedono mappatura dedicata che la skill non copre completamente
