# Estratto operativo - Marcatura CE dei prodotti elettrici (LVD / EMC / RED)

> Guida a: quale direttiva si applica, quale procedura di conformita' (moduli),
> quale documentazione e dichiarazione. Ogni voce rinvia alle fonti in
> `references/fonti/`. Non individua le norme armonizzate applicabili (a
> pagamento) ne' esegue le prove.

## 1. Quale direttiva si applica?

| Direttiva | Ambito | Rif. |
|---|---|---|
| **LVD 2014/35/UE** | materiale elettrico con tensione nominale **50-1000 V ca** o **75-1500 V cc** (esclusioni all. II) | art. 1 |
| **EMC 2014/30/UE** | apparecchi che possono generare/subire **perturbazioni elettromagnetiche**; impianti fissi | all. I |
| **RED 2014/53/UE** | **apparecchiature radio** (che emettono/ricevono onde radio) | art. 3 |

- Un prodotto puo' ricadere **contemporaneamente** in piu' direttive (es. un
  alimentatore: LVD + EMC).
- Un'**apparecchiatura radio** applica la **RED**, che **incorpora** gli obiettivi
  di sicurezza LVD (senza limiti minimi di tensione, art. 3.1.a) e i requisiti EMC
  (art. 3.1.b): in tal caso non si applicano separatamente LVD ed EMC.

## 2. Procedura di valutazione della conformita' (moduli)

| Direttiva | Moduli ammessi | Organismo notificato |
|---|---|---|
| **LVD** | **Modulo A** - controllo interno della produzione (all. III) | **No** (solo autovalutazione) |
| **EMC** | **Modulo A** (all. II) **oppure** esame UE del tipo **B** + conformita' al tipo **C** (all. III) | solo se si sceglie B+C |
| **RED** | **Modulo A** (all. II), **B+C** (all. III) o **H** (all. IV) | **Si'** se per l'art. 3.1 non si applicano le norme armonizzate (allora niente solo A) |

**Regola RED (art. 17)**: per i requisiti dell'**art. 3.1** (sicurezza + EMC), il
solo **Modulo A** e' ammesso **solo** se si applicano le **norme armonizzate**
pertinenti; in caso contrario servono **B+C** o **H** (organismo notificato). Per
i requisiti dell'art. 3.2 e 3.3, applicando norme armonizzate si puo' usare A, B+C
o H.

## 3. Requisiti essenziali / obiettivi

- **LVD** (all. I): marcature informative, assemblaggio/collegamento sicuro,
  protezione dai pericoli elettrici e da influenze esterne.
- **EMC** (all. I): emissione contenuta + immunita' adeguata; **impianti fissi**
  secondo buone prassi di ingegneria.
- **RED** (art. 3): 3.1 salute/sicurezza (obiettivi LVD) + EMC; 3.2 uso efficiente
  dello **spettro radio**; 3.3 interoperabilita'/privacy per **categorie
  determinate** (es. caricabatterie standardizzati, protezione dati).

## 4. Documentazione e dichiarazione

- **Documentazione tecnica**: LVD/EMC (nel modulo), **RED allegato V**.
- **Dichiarazione UE di conformita'**: LVD all. IV, EMC (art. dedicato), **RED
  all. VI**; RED prevede anche la **dichiarazione UE semplificata** (all. VII).
- **Marcatura CE**: apposta dal fabbricante prima dell'immissione sul mercato;
  quando interviene un **organismo notificato** in fase di produzione (moduli con
  sorveglianza), la marcatura CE e' **seguita dal numero dell'organismo**.

## Confini della skill (cosa NON copre)

- Non individua le **norme armonizzate** applicabili (EN a pagamento) ne' esegue o
  interpreta le **prove** (EMC, sicurezza elettrica, spettro).
- Non redige materialmente la documentazione tecnica ne' la dichiarazione: ne
  fornisce struttura e requisiti.
- Non copre altre direttive eventualmente applicabili (es. macchine 2023/1230,
  ATEX 2014/34, ErP, RoHS) se non nella misura del rinvio.
