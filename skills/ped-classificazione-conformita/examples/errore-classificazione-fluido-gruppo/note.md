# Esempio - note di dominio (caso problematico)

## Errore da scoprire

L'utente classifica il propano come fluido di **gruppo 2** ("lo trattiamo
come gas comune in officina"). La classificazione corretta e' **gruppo 1**:
il propano e' classificato CLP come gas infiammabile categoria 1 (H220 "gas
estremamente infiammabile"), e "gas infiammabile" e' la prima delle 17
classi di pericolo enumerate all'art. 9 c. 1 lett. a del D.Lgs 26/2016.

## Perche' la skill deve rilevare l'errore

L'art. 9 c. 1 attribuisce i fluidi a gruppo 1 sulla base di una **lista
chiusa** di 17 classi di pericolo CLP. La logica e' a cascata:

1. Se il fluido cade in **una qualsiasi** di queste 17 classi, e' **gruppo 1**.
2. Solo se il fluido non cade in nessuna di queste 17 classi, e' **gruppo 2**
   (criterio residuale, art. 9 c. 1 lett. b).

La domanda "e' un gas comune in officina?" non e' un test ammesso dal
decreto. Il test ammesso e' "ricade in almeno una delle 17 classi CLP?".

## Conseguenze della correzione

La differenza fra gruppo 1 e gruppo 2 e' strutturale:

- **Tabella applicabile**: gruppo 2 -> tabella 2 (linee piu' permissive);
  gruppo 1 -> tabella 1 (linee piu' restrittive, perche' fluido piu'
  pericoloso).
- **Categoria attesa**: per PS = 18 bar e V = 5.000 L, sulla tabella 2 la
  fascia tipica e' II; sulla tabella 1 e' III o IV. La differenza e' ampia.
- **Moduli ammissibili (art. 10 c. 2)**:
  - Categoria II: A2, D1, E1.
  - Categoria III: B(progetto)+D, B(progetto)+F, B(produzione)+E,
    B(produzione)+C2, H.
  - Categoria IV: B(produzione)+D, B(produzione)+F, G, H1.
  - Il modulo **A2** non e' ammesso per cat. III. L'utente non puo'
    "scegliere" A2 se la categoria reale e' III.
- **Organismo notificato**: per cat. II il coinvolgimento e' parziale
  (prove a intervalli casuali in A2; sorveglianza qualita' in D1/E1).
  Per cat. III/IV e' sempre coinvolto a vario titolo. La richiesta
  dell'utente di "evitare l'organismo notificato" diventa impraticabile.
- **Cadenza visite (art. 10 c. 4)**: per cat. III su recipienti di art. 3
  c. 1 lett. a) punto 1) (recipienti destinati a gas infiammabili con PSxV
  significativo), i moduli di garanzia qualita' (D, E, H) prevedono visite
  senza preavviso, almeno due nel primo anno.

## Cosa la skill **non** fa in questo esempio

- Non legge graficamente la tabella 1 (la categoria III o IV e' un'attesa
  metodologica, da verificare sul PDF della GU).
- Non sceglie il modulo fra quelli ammissibili (e' decisione del fabbricante).
- Non identifica l'organismo notificato (rinvio alla banca dati NANDO).
- Non valuta gli aspetti ATEX o macchine se il serbatoio fa parte di un
  impianto piu' ampio: lo segnala come verifica a parte.

## Riferimenti normativi citati

- Reg. CE 1272/2008 (CLP), classe "gas infiammabili" categoria 1, H220.
- D.Lgs 26/2016 art. 9 c. 1 lett. a (17 classi -> gruppo 1) e lett. b (gruppo
  2 residuale).
- D.Lgs 26/2016 Allegato II (tabelle 1-9): tabella 1 (recipienti gas/vapori
  gruppo 1).
- D.Lgs 26/2016 art. 10 c. 2 lett. b/c/d (moduli per cat. II/III/IV).
- D.Lgs 26/2016 art. 10 c. 3 (opzione categoria superiore), c. 4 (visite),
  c. 5 (pezzo unico cat. III su attrezzature di art. 3 c. 1 lett. b).

## Insegnamento metodologico

Quando il fluido e' un gas, **non basta** verificare lo stato fisico o la
familiarita' d'uso. Bisogna sempre leggere la scheda di sicurezza del
produttore del fluido (Reg. CLP 1272/2008) e cercare se il fluido cade in
una delle 17 classi di pericolo elencate all'art. 9 c. 1 lett. a. La skill
chiede esplicitamente questa informazione nel task `classifica-fluido.md`.
