# Estratto - Formulazione classica del cedimento edometrico

> Sintesi della formulazione classica della compressione monodimensionale (Terzaghi 1925, Skempton 1944), di dominio pubblico tecnico, ampiamente trattata nei testi standard di meccanica dei terreni e geotecnica (Lancellotta R. "Geotecnica", Cestari, Holtz & Kovacs). NTC 2018 par. 6.2.4 rinvia a metodi consolidati di letteratura senza riprodurre la formula chiusa.

## Curva edometrica e parametri

La curva edometrica e-log(sigma') di un campione coesivo indisturbato sottoposto a prova edometrica presenta tipicamente:
- un **ramo di ricompressione** (OC, over-consolidated) a basse tensioni, con pendenza piccola Cr (indice di ricompressione)
- una **transizione** alla tensione di preconsolidazione sigma_p' (determinata graficamente con metodo Casagrande o Janbu)
- un **ramo vergine** (NC, normally consolidated) a tensioni elevate, con pendenza maggiore Cc (indice di compressione)

Tipicamente per argille naturali Cr / Cc e' nel range 1/5 - 1/10, ma puo' variare.

## Formula a tratti

Per uno strato di spessore iniziale h0 con indice dei vuoti iniziale e0, sottoposto a un incremento uniforme di tensione efficace verticale Delta sigma' = sigma_f' - sigma_0', il cedimento Delta h per compressione monodimensionale (deformazione laterale impedita) e':

### caso OC: sigma_f' <= sigma_p'

Tutto il carico mantiene il terreno nel ramo di ricompressione:

```
Delta h = h0 / (1 + e0) * Cr * log10(sigma_f' / sigma_0')
```

### caso NC: sigma_0' >= sigma_p'

Il terreno e' gia' normalmente consolidato (OCR = 1, sigma_p' = sigma_0'), tutto il carico avviene nel ramo vergine:

```
Delta h = h0 / (1 + e0) * Cc * log10(sigma_f' / sigma_0')
```

### caso transizione: sigma_0' < sigma_p' < sigma_f'

Il carico attraversa la tensione di preconsolidazione: prima ramo OC fino a sigma_p', poi ramo NC fino a sigma_f':

```
Delta h = h0 / (1 + e0) * [Cr * log10(sigma_p' / sigma_0')
                           + Cc * log10(sigma_f' / sigma_p')]
```

Il primo addendo e' il contributo OC, il secondo e' il contributo NC.

## Continuita' a sigma_f' = sigma_p'

A sigma_f' = sigma_p' la formula del caso OC e quella del caso transizione (con il solo termine Cr) coincidono. Per sigma_f' appena oltre sigma_p' si attiva il termine NC, che cresce continuamente da zero. Le tre formule formano un'unica funzione continua di Delta h(sigma_f').

## Deformazione media

```
epsilon = Delta h / h0
```

Per epsilon > 10% il metodo edometrico, basato su moduli costanti per ramo, e' approssimato: serve formulazione incrementale (Cv variabile, modulo edometrico tangente locale) o software dedicato.

## Limiti di validita'

- **Compressione monodimensionale**: valido per strati orizzontali estesi sotto area di carico larga rispetto a h0. Per fondazioni di area piccola rispetto alla profondita' dello strato, la deformazione laterale non e' trascurabile e si ricorre a correttivi (Skempton & Bjerrum) o FEM.
- **Singolo strato omogeneo**: per stratigrafie multilayer si somma il contributo di ciascuno strato (con Delta sigma' a profondita' calcolato separatamente, es. Boussinesq).
- **Carico in compressione**: per scarichi (rebound) la formula con Cr puo' essere usata con segno opposto, ma con cautela; la skill non lo copre per evitare ambiguita'.
- **Cedimento primario**: il cedimento immediato (elastico, non drenato) e quello secondario (creep, Calpha) sono fuori scope della formula edometrica classica.
- **Terreno non strutturato**: per argille strutturate (sensitive) la curva edometrica presenta un crollo a sigma_y' diverso da sigma_p' classico; la formula a due rami non e' adeguata.

## Riferimenti

- Terzaghi K. (1925), "Erdbaumechanik auf bodenphysikalischer Grundlage"
- Skempton A.W. (1944), "Notes on the compressibility of clays"
- Lancellotta R., "Geotecnica" (testo didattico standard, Zanichelli)
- Holtz R.D., Kovacs W.D., "An Introduction to Geotechnical Engineering"

## Note sull'uso da parte della skill

La formulazione e' implementata in `tasks/lib/cedimenti.py`. La skill applica esattamente la formula a tratti sopra, con dispatch automatico OC / NC / transizione in funzione di sigma_0', sigma_p', sigma_f'. Validazione input: Cr <= Cc, sigma_p' >= sigma_0' (OCR >= 1), Delta sigma' >= 0. La skill produce avvertenza per epsilon > 10% e per Delta sigma' = 0.
