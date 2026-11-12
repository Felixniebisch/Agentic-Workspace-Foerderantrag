---
vorgang: 2026-09-hansen-hamburg
stichtag: 2026-09-15
festpreis_eur: 31900
foerderfaehige_kosten_eur: 28000
foerdersatz_sicher_prozent: 46
zuschuss_sicher_eur: 12880
hoechstsatz_prozent: 70
einkommensbonus: offen
erzeugt_von: _tools/foerdercheck.py
---
# Förder-Check 2026-09-hansen-hamburg

Erzeugt von `_tools/foerdercheck.py` aus `kunden/2026-09-hansen-hamburg/01_eingang/daten.md`. Nicht von Hand ändern: Eingang oder Regeln ändern und neu rechnen.

## Ergebnis

| Größe | Wert |
|---|---|
| Paket | HT-L09 Luft-Wasser-Wärmepumpe 9 kW, Komplettpaket |
| Festpreis | 31.900 € |
| förderfähige Kosten (max. 28.000 €) | 28.000 € |
| Fördersatz sicher | Summe 46 %, Deckel 70 % → **46 %** |
| **erwarteter Zuschuss (sicher)** | **12.880 €** |

Bestandteile: Grundförderung 30 %; Klima-Geschwindigkeitsbonus 16 %.

## Möglich mit Einkommensbonus (nur Information, nicht im Angebot)

| Stufe | Fördersatz (gedeckelt) | Zuschuss |
|---|---|---|
| +40 % | 70 % | 19.600 € |
| +30 % | 70 % | 19.600 € |
| +10 % | 56 % | 15.680 € |

## Offene Punkte für Finanzen

- Einkommensbonus: Stufengrenzen in foerderregeln.md R05 sind „zu prüfen“ (TODO Merkblatt 458). Im sicheren Zuschuss nicht enthalten.

## Verwendete Regelzeilen (wörtlich aus `_shared/foerderregeln.md`)

- R01 | grundfoerderung_prozent = 30 | gültig ab 21.07.2026 | alle Antragsteller | [1]
- R02 | speedbonus_prozent = 16 | gültig ab 21.07.2026 | nur selbstnutzende Eigentümer, die eine fossile Heizung ersetzen | [1]
- R03 | fossile_heizungen = oel, gas, fluessiggas, kohle | gültig ab 21.07.2026 | Heizarten, die als „fossil“ für R02 gelten; Liste zu prüfen gegen [2] | [1]
- R04 | einkommensbonus_stufen_prozent = 40, 30, 10 | gültig ab 21.07.2026 | nur selbstnutzende Eigentümer, gestaffelt nach zu versteuerndem Haushaltseinkommen | [1]
- R05 | einkommensbonus_schwellen_eur = zu prüfen | gültig ab 21.07.2026 | Einkommensgrenzen der Stufen 40 / 30 / 10 %; TODO gegen Merkblatt 458 prüfen, nicht schätzen | [2]
- R06 | hoechstsatz_prozent = 70 | gültig ab 21.07.2026 | Deckel der Summe aller Boni, in % der förderfähigen Kosten | [1]
- R08 | hoechstsatz_niedrig_grenze_eur = 30000 | gültig ab 21.07.2026 | Einkommensgrenze für R07 | [1]
- R09 | kind_zuschlag_grenze_eur = 10000 | gültig ab 21.07.2026 | erhöht die Grenze R08 einmalig, wenn mindestens ein Kind unter 18 im Haushalt lebt | [1]
- R10 | foerderfaehige_kosten_max_eur = 28000 | gültig ab 21.07.2026 | Höchstbetrag förderfähiger Kosten (erste Wohneinheit) | [1]
- R11 | effizienzbonus_kaeltemittel_prozent = 0 | gültig ab 21.07.2026 | kein Effizienzbonus mehr für natürliche Kältemittel | [1]
- R12 | absenkung_start = 2027-02-01 | gültig ab 01.02.2027 | ab diesem Tag sinken R10 und R02 je angefangenem Halbjahr | [1]

## Verwendete Produktzeile (aus `_shared/produkte.md`)

- HT-L09 | Luft-Wasser-Wärmepumpe 9 kW, Komplettpaket | festpreis_eur = 31900 | ca. 110–170 m² Wohnfläche
