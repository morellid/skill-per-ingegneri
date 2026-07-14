# Task: Classifica l'intervento e trova la soglia di zeta_E

## Obiettivo

Dato un intervento su una costruzione esistente, individuare in quale delle tre
categorie del par. 8.4 NTC 2018 ricade (riparazione/intervento locale,
miglioramento, adeguamento), stabilire se l'adeguamento e' obbligatorio e quale
soglia del rapporto zeta_E si applica.

## Input richiesti

- descrizione dell'intervento previsto (cosa si costruisce/modifica/rinforza);
- **classe d'uso** della costruzione (I, II, III, III uso scolastico, IV) e
  destinazione d'uso attuale e futura;
- se l'intervento comporta: sopraelevazione; ampliamento connesso; variazione di
  destinazione d'uso con incremento dei carichi verticali in fondazione (stima %
  se disponibile); trasformazione del sistema strutturale (nuovi elementi
  verticali portanti su cui gravi >= 50% dei carichi per piano); modifica di
  classe d'uso;
- (facoltativo) se l'intervento e' su bene di interesse culturale in zona a
  rischio sismico.

## Fonti da leggere

- `references/estratti/ntc2018-cap8-costruzioni-esistenti.md` sezioni 1, 2, 3
- se serve conferma testuale: `references/fonti/ntc2018-dm-17-01-2018.md`
  (par. 8.4, 8.4.1, 8.4.2, 8.4.3) e `references/fonti/circ-7-2019-mit.md`
  (C8.4.1/C8.4.2/C8.4.3)

## Procedura

### Passo 1 - Screening: adeguamento obbligatorio? (NTC 8.4.3)

Verifica se ricorre **almeno uno** dei casi a-e. Se si', l'intervento e' di
**adeguamento** e la soglia e':

| Caso (NTC 8.4.3) | Soglia zeta_E |
|---|---|
| a) sopraelevazione | zeta_E >= 1,0 |
| b) ampliamento strutturalmente connesso che altera significativamente la risposta | zeta_E >= 1,0 |
| c) variazione destinazione d'uso con incremento carichi verticali in fondazione > 10% | zeta_E >= 0,80 |
| d) insieme sistematico di opere -> sistema strutturale diverso (o nuovi elementi verticali con >= 50% carichi/piano) | zeta_E >= 1,0 |
| e) modifica di classe d'uso verso classe III scolastica o classe IV | zeta_E >= 0,80 |

Note da riportare:
- la verifica **locale** delle singole parti resta sempre obbligatoria, anche
  nei casi c) ed e);
- cordoli sommitali o variazioni di copertura **senza** incremento di superficie
  abitabile non sono "ampliamento" ex a): non obbligano l'adeguamento salvo
  ricorra una delle condizioni b), c), d), e) (NTC 8.4.3);
- l'adeguamento sismico deciso dal proprietario dopo una valutazione ex par. 8.3
  che riscontri inadeguatezza, se NON ricade in a)/b)/d), e' assimilato al caso
  c) con soglia 0,8 (Circolare C8.4.3).

### Passo 2 - Se NON e' adeguamento: locale o miglioramento?

- **Riparazione / intervento locale** (NTC 8.4.1) se: interessa singoli
  elementi, **non** cambia significativamente il comportamento globale e **non**
  riduce le condizioni di sicurezza preesistenti. Esempi dalla Circolare C8.4.1:
  ripristino/rinforzo/sostituzione di travi, architravi, coperture, impalcati,
  pilastri, pannelli murari; ripristino o nuovi collegamenti (catene/tiranti,
  chiodature); apertura di un vano con opportuni rinforzi purche' non modifichi
  significativamente rigidezza, resistenza alle azioni orizzontali e capacita' di
  deformazione. Per questa categoria non si richiede la valutazione della
  sicurezza globale, ma per il rafforzamento locale va valutato l'incremento del
  **livello di sicurezza locale** (C8.4.1). Non e' soggetto a collaudo statico.

- **Miglioramento** (NTC 8.4.2) se: aumenta la sicurezza preesistente senza
  necessariamente raggiungere i livelli del par. 8.4.3, e non ricade in nessun
  caso di adeguamento. La valutazione della sicurezza e' obbligatoria ed estesa
  all'intera struttura; e' soggetto a collaudo statico. Soglie di zeta_E dopo
  il miglioramento (in combinazione sismica zeta_E puo' essere < 1):

  | Classe d'uso | Soglia (NTC 8.4.2) |
  |---|---|
  | Classe III uso scolastico e classe IV | zeta_E >= 0,6 |
  | Restanti classe III e classe II | zeta_E incrementato di >= 0,1 rispetto allo stato di fatto |
  | (solo sistema di isolamento) | zeta_E >= 1,0 |

Nota: per beni culturali in zona a rischio sismico (art. 29 c. 4 D.Lgs. 42/2004)
e' sempre ammesso limitarsi al miglioramento (NTC 8.4).

## Output atteso

- **categoria dell'intervento** con la citazione del paragrafo (NTC 8.4.1/8.4.2/
  8.4.3) e la motivazione basata sugli input;
- **soglia di zeta_E applicabile** con il caso e il riferimento;
- se adeguamento: elenco dei casi a-e che ricorrono;
- indicazione se e' richiesto il **collaudo statico** e la **valutazione della
  sicurezza** (globale o solo locale);
- avvertenza finale: la skill classifica ma **non calcola** zeta_E ne' esegue la
  valutazione della sicurezza; il valore di zeta_E e la verifica sono
  responsabilita' del progettista (par. 8.3).
