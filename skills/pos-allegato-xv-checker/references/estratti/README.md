# Estratti normativi

Questa cartella contiene estratti testuali delle fonti normative pubbliche citate dalla skill.

## Regole

- Solo testi di dominio pubblico o riproducibili secondo normativa italiana (L. 633/1941 art. 5 - atti ufficiali dello Stato riproducibili liberamente)
- Nessun testo a licenza proprietaria (UNI, CEI) in questa cartella
- Ogni estratto cita articolo/comma/punto con precisione
- Data di consultazione e hash della fonte sorgente riportati in `sources.yaml`

## File previsti (da preparare in sessione dedicata)

- [ ] `dlgs-81-2008-art-96.md` - obblighi datori di lavoro imprese esecutrici
- [ ] `dlgs-81-2008-art-100.md` - PSC, per confronto con POS
- [ ] `allegato-xv-testo.md` - testo integrale Allegato XV pertinente (punti 3 e 4)

## Formato atteso degli estratti

Ogni file inizia con:

```markdown
# Estratto: <titolo della fonte e articoli>

Fonte: [id in sources.yaml]
URL consultato: [url]
Data consultazione: YYYY-MM-DD
Hash SHA256 del binario: [hash]
Licenza: public-domain (riproducibile art. 5 L. 633/1941)

---

## Art. X - Titolo
[testo integrale]

## Art. Y - Titolo
[testo integrale]
```
