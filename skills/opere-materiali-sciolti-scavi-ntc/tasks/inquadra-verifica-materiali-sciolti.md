# Task: inquadra-verifica-materiali-sciolti

Inquadra la **progettazione e la verifica di un manufatto di materiali sciolti** (rilevato, argine, terrapieno,
colmata, rinterro) secondo le **NTC 2018 par. 6.8** (par. 6.8.1-6.8.5). Supporto documentale: **non** calcola le
verifiche ne' dimensiona l'opera.

## Quando usarla

Il progettista geotecnico deve impostare criteri, verifiche SLU/SLE, aspetti costruttivi e monitoraggio di
un'opera in terra (par. 6.8.1-6.8.5). Per i **fronti di scavo** (par. 6.8.6) usa `inquadra-fronti-scavo`.

## Passi

1. **Verifica l'ambito** (par. 6.8): l'opera e' un manufatto di materiali sciolti (rilevati, argini di difesa,
   rinfianchi, rinterri, terrapieni, colmate) o un'opera con funzioni di drenaggio/filtro/transizione/
   fondazione/tenuta/protezione? Ricorda l'esclusione degli **sbarramenti di ritenuta idraulica** (dighe in
   terra: normativa specifica).
2. **Criteri generali** (par. 6.8.1): requisiti prestazionali e terreni di fondazione; scelta e qualificazione
   dei materiali (naturali o di provenienza diversa) e modalita' di posa; prescrizioni su spessore massimo degli
   strati, controlli, limiti di accettabilita', grado di compattazione e deformabilita'.
3. **Verifiche SLU** (par. 6.8.2): condizione [6.2.1] con i valori di progetto; **Combinazione 2 (A2+M2+R2)
   dell'Approccio 1**; coefficienti parziali Tab. 6.2.I (azioni), 6.2.II (parametri geotecnici) e **Tab. 6.8.I
   (gamma_R = 1,1, gruppo R2)**. Studia la **stabilita' globale** manufatto-terreno di fondazione nelle diverse
   fasi costruttive, a fine costruzione e in esercizio; estendi le **verifiche locali** agli elementi di
   rinforzo. Per manufatti su pendii valuta l'influenza sulla stabilita' del pendio; per opere di ritenuta
   idraulica verifica la stabilita' dei paramenti e affronta **sifonamento** ed **erosione** (par. 6.2.4.2).
4. **Verifiche SLE** (par. 6.8.3): valuta gli spostamenti del manufatto e del terreno circostante, compatibili
   con la funzionalita' dell'opera e con la sicurezza/funzionalita' dei manufatti adiacenti.
5. **Aspetti costruttivi** (par. 6.8.4): posa in strati; geosintetici e componenti artificiali certificati per
   norme europee armonizzate, con prove sperimentali.
6. **Controlli e monitoraggio** (par. 6.8.5): programma di prove di controllo in costruzione; monitoraggio di
   spostamenti e pressioni interstiziali compatibili con i requisiti di sicurezza e funzionalita'.

Usa la checklist in `../references/estratti/materiali-sciolti-scavi-checklist.md` (sezioni 1-6).

## Output atteso

Un inquadramento che indichi: ambito, combinazione e coefficienti da applicare (A2+M2+R2, Tab. 6.8.I gamma_R =
1,1), le verifiche richieste (stabilita' globale nelle varie fasi, SLE, elementi di rinforzo, eventuale ritenuta
idraulica) e i controlli/monitoraggio, con **rinvio ai paragrafi** NTC. Nessun calcolo o dimensionamento.

## Cosa NON fare

- Non calcolare le verifiche di stabilita' ne' dimensionare il manufatto o gli elementi di rinforzo.
- Non definire il modello geotecnico ne' scegliere i parametri al posto del progettista.
- Non trattare gli **sbarramenti di ritenuta idraulica** (dighe in terra), la **sicurezza dei lavoratori** negli
  scavi (D.Lgs 81/2008 Titolo IV) ne' la progettazione sismica (Cap. 7).
