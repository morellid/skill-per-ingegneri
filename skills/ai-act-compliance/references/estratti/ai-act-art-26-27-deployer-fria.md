# Estratto: AI Act Art. 26-27 - Obblighi deployer + FRIA

**Fonte**: `sources.yaml` id `ai-act-it-eurlex`
**Data consultazione**: 2026-04-25
**Hash SHA256**: a61b61706aee6676e3988ab696162d71d759c3debd48b2ecccac3555207f2b0c

---

## Articolo 26 - Obblighi dei deployer di sistemi di IA ad alto rischio

Il "**deployer**" (utilizzatore) e' la persona fisica o giuridica che usa un sistema di IA sotto la propria autorita', salvo uso personale non professionale (art. 3 par. 4).

### Par. 1 - Obblighi generali

I deployer di sistemi high-risk:
- Adottano misure tecniche e organizzative adeguate per garantire l'**uso conforme alle istruzioni d'uso**
- Garantiscono che i sistemi siano usati per le **finalita' previste**

### Par. 2 - Sorveglianza umana

I deployer **affidano la sorveglianza umana** a persone fisiche dotate della **competenza, formazione e autorita' necessarie** + risorse di supporto.

### Par. 3 - Dati di input

Quando i deployer **controllano i dati di input**, ne garantiscono la **rilevanza e rappresentativita'** rispetto alla finalita' prevista.

### Par. 4 - Monitoraggio funzionamento

I deployer monitorano il funzionamento del sistema in base alle istruzioni d'uso e, se necessario, **informano il fornitore** in conformita' all'art. 72.

Quando ritengono che l'uso possa comportare un **rischio per salute, sicurezza, diritti fondamentali**, sospendono l'uso e informano fornitore + autorita' di vigilanza.

### Par. 5 - Conservazione log

I deployer conservano i **log automaticamente generati** dal sistema per un periodo adeguato alla finalita' prevista, **almeno 6 mesi** (salvo applicabilita' di altre norme UE/nazionale).

### Par. 6 - Lavoratori

Prima di mettere in servizio o usare un sistema high-risk **nel luogo di lavoro**, i deployer **datori di lavoro** informano i rappresentanti dei lavoratori e i lavoratori interessati.

### Par. 7 - Informazione interessati persone fisiche

I deployer di sistemi high-risk che decidono o assistono a decisioni su persone fisiche **informano** tali persone che sono soggette all'uso del sistema high-risk. Per sistemi high-risk usati per attivita' di contrasto: si applica l'art. 13 della direttiva (UE) 2016/680 (LED).

### Par. 8 - Cooperazione con autorita'

I deployer cooperano con le autorita' competenti su qualsiasi azione intrapresa in relazione ai sistemi high-risk.

### Par. 9 - DPIA

Quando applicabile, i deployer usano le informazioni fornite ai sensi dell'art. 13 per condurre la **DPIA** ai sensi del GDPR art. 35 o LED art. 27.

### Par. 10 - Identificazione biometrica remota post-evento (per attivita' di contrasto)

Disciplina specifica.

### Par. 11 - Deployer pubblici e simili - registrazione art. 49

I deployer che siano autorita' pubbliche, agenzie/organismi UE, o privati che forniscono servizi pubblici (lett. b) e par. 12), prima di mettere in servizio sistemi high-risk Allegato III (escluso punto 2 infrastrutture critiche), si registrano nella **banca dati UE**.

### Par. 12 - FRIA: rinvio art. 27

Per i deployer di cui al par. 11 di cui al primo comma di tale paragrafo, **prima di mettere in servizio** un sistema high-risk Allegato III (esclusi quelli per attivita' di contrasto, migrazione, asilo, frontiere) - **eseguono il FRIA** ai sensi dell'art. 27.

---

## Articolo 27 - Valutazione d'impatto sui diritti fondamentali (FRIA)

### Par. 1 - Quando e' obbligatorio

Prima di mettere in servizio un sistema high-risk dell'**Allegato III** (esclusi punto 2 infrastrutture critiche), il deployer effettua una **FRIA** quando e':
- **Organismo di diritto pubblico**, oppure
- **Ente privato che fornisce servizi pubblici**, oppure
- Deployer di sistemi che effettuano attivita' di cui all'**Allegato III, punti 5 lett. b) e c)** (credit scoring + insurance pricing).

### Par. 1 - Contenuti del FRIA

La FRIA contiene:

- **a)** Descrizione dei **processi del deployer** in cui il sistema sara' usato
- **b)** Periodo e frequenza d'uso
- **c)** Categorie di **persone fisiche e gruppi** che potrebbero essere interessati
- **d)** **Rischi specifici di danno** che potrebbero impattare le categorie identificate, considerando le informazioni del fornitore (art. 13)
- **e)** Descrizione dell'attuazione delle **misure di sorveglianza umana**
- **f)** Misure da adottare in caso di **materializzazione dei rischi**, inclusi accordi per governance interna e meccanismi di reclamo

### Par. 2 - Aggiornamenti

L'obbligo si applica al primo uso. Per usi successivi simili, il deployer puo' fare riferimento a una FRIA precedentemente effettuata o **aggiornarla**.

### Par. 3 - Notifica autorita' di vigilanza

Il deployer notifica i risultati della FRIA all'autorita' di vigilanza tramite il **modello standardizzato** che l'AI Office sviluppera' (art. 27 par. 5).

### Par. 4 - Sinergia con DPIA

Se uno qualsiasi degli obblighi di FRIA e' gia' soddisfatto da una **DPIA condotta ai sensi del GDPR art. 35 o LED art. 27**, la FRIA **integra** tale DPIA.

---

## Note operative

### Chi DEVE fare il FRIA

- **Sempre**: organismi pubblici e privati che forniscono servizi pubblici essenziali, prima di usare sistemi high-risk Allegato III (esclusi infrastrutture, contrasto, migrazione)
- **Sempre**: deployer privati di sistemi credit scoring (Allegato III par. 5 lett. b) e insurance pricing (par. 5 lett. c)

### Chi NON deve (necessariamente) fare il FRIA

- Deployer privati di sistemi HR/educazione/biometria che non rientrano nei casi sopra
- Provider del sistema (loro fanno gestione rischi art. 9, non FRIA)

### Sinergia FRIA-DPIA

Se il sistema tratta dati personali (quasi sempre per Allegato III), il deployer deve fare entrambe ma puo' integrarle. In pratica si scrive **un unico documento** che soddisfa GDPR art. 35 + AI Act art. 27, con sezioni dedicate per gli aspetti specifici (rischi diritti fondamentali oltre privacy).

### Differenza con il sistema gestione rischi del provider (art. 9)

- **Provider art. 9**: gestione rischi interna al sistema, su tutto il ciclo di vita
- **Deployer art. 27 (FRIA)**: valutazione contestuale al **proprio uso del sistema**, prima di metterlo in servizio

Sono complementari. Il provider ha gia' fornito al deployer (tramite art. 13 - istruzioni d'uso) le informazioni che il deployer usa per il proprio FRIA.
