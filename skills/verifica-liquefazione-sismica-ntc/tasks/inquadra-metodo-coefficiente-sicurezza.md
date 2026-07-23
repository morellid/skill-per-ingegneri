# Task: inquadra-metodo-coefficiente-sicurezza

Inquadra i **metodi di analisi** della verifica a liquefazione e il **coefficiente di sicurezza** secondo le
**NTC 2018 par. 7.11.3.4.3**, quando nessuna condizione di esclusione è soddisfatta. Supporto documentale:
**non** esegue il calcolo.

## Quando usarla

Il tecnico ha stabilito (con `valuta-esclusione-verifica-liquefazione`) che **nessuna** condizione di
esclusione ricorre e il terreno comprende strati/lenti di sabbie sciolte sotto falda, quindi la verifica è
necessaria e va impostata.

## Passi

1. **Campo di applicazione** (§7.11.3.4.3): si valuta il **coefficiente di sicurezza alla liquefazione** alle
   **profondità** in cui sono presenti i **terreni potenzialmente liquefacibili**, quando **nessuna** delle
   condizioni del §7.11.3.4.2 è soddisfatta e il terreno comprende **strati estesi o lenti spesse di sabbie
   sciolte sotto falda**.

2. **Metodo** (§7.11.3.4.3): salvo procedure di **analisi avanzate**, la verifica può essere effettuata con
   **metodologie di tipo storico-empirico** in cui il **coefficiente di sicurezza** è definito dal:

   **coefficiente di sicurezza = resistenza disponibile alla liquefazione / sollecitazione indotta dal
   terremoto di progetto**

3. **Resistenza alla liquefazione** (§7.11.3.4.3): valutata sulla base dei risultati di **prove in sito**
   (es. penetrometriche) o di **prove cicliche di laboratorio**.

4. **Sollecitazione indotta** (§7.11.3.4.3): stimata attraverso la conoscenza dell'**accelerazione massima
   attesa alla profondità di interesse** (l'azione sismica di riferimento si determina secondo il §3.2.3;
   categorie di sottosuolo al §3.2.2).

5. **Giudizio** (§7.11.3.4.3): l'**adeguatezza del margine di sicurezza** nei confronti della liquefazione
   deve essere **valutata e motivata dal progettista**.

6. **Conseguenze** (§7.11.3.4.1): se il terreno risulta suscettibile e con effetti rilevanti → **interventi di
   consolidamento** e/o **trasferimento del carico** a strati non suscettibili; con **fondazioni profonde** →
   valutare **riduzione della capacità portante** e **incrementi nei pali**.

Usa la checklist in `../references/estratti/verifica-liquefazione-checklist.md` (sezioni 1 e 3).

## Output atteso

Un inquadramento del metodo di verifica (coefficiente di sicurezza = resistenza/sollecitazione, metodi
storico-empirici, resistenza da prove, sollecitazione da a_max, margine motivato dal progettista) e delle
conseguenze, con **rinvio ai paragrafi** NTC. Nessun calcolo numerico del coefficiente di sicurezza.

## Cosa NON fare

- Non **calcolare** il coefficiente di sicurezza né derivare i rapporti **CRR/CSR** o le correlazioni con
  **(N₁)₆₀ / q_c1N** e la magnitudo: sono metodi di **letteratura/prove**, non nelle NTC.
- Non **progettare** gli interventi di consolidamento né valutare numericamente la riduzione di capacità
  portante o gli incrementi nei pali.
