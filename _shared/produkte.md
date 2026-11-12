---
description: Wärmepumpen-Pakete mit Festpreis, aus denen Förder-Check und Angebot rechnen.
---
# Produkte und Festpreise

Demo-Werte, fiktiv. Ein Paket umfasst Gerät, Montage, Demontage der Altanlage und hydraulischen Abgleich zum Festpreis (brutto). `_tools/foerdercheck.py` liest die Zeilen unter „Pakete“; das Angebot übernimmt Name und Preis.

## Pakete

Format: `- Paket-ID | Bezeichnung | festpreis_eur = Betrag | passend für`

- HT-L06 | Luft-Wasser-Wärmepumpe 6 kW, Komplettpaket | festpreis_eur = 27400 | bis ca. 110 m² Wohnfläche, gut gedämmt
- HT-L09 | Luft-Wasser-Wärmepumpe 9 kW, Komplettpaket | festpreis_eur = 31900 | ca. 110–170 m² Wohnfläche
- HT-L12 | Luft-Wasser-Wärmepumpe 12 kW, Komplettpaket | festpreis_eur = 36500 | ca. 170–240 m² oder unsanierter Altbau

Die Paketwahl kommt aus dem Online-Planungstool (Feld `produkt` in `01_eingang/daten.md`). Größere Häuser: Einzelplanung, nicht in dieser Demo.
