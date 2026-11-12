---
description: Die einzige Stelle, an der die Regeln der KfW-Heizungsförderung (Programm 458) stehen.
stand: 2026-07-21
---
# Förderregeln KfW 458 (Heizungsförderung für Privatpersonen)

Die einzige Stelle im Arbeitsbereich, an der Förderregeln stehen. Stufen und Skripte verweisen hierher und schreiben keine Regel ab. Ändert sich die Förderung, wird nur diese Datei geändert, mit neuem „gültig ab“-Datum und Quelle.

> **TODO (vor echtem Einsatz):** Alle Werte gegen das aktuelle KfW-Merkblatt 458 prüfen. Insbesondere die Einkommensgrenzen der Stufen 40 / 30 / 10 % (Regel R05) sind **zu prüfen** und hier bewusst nicht eingetragen.

## Quellen

- [1] ema-energiewelt.de, „Wärmepumpen-Förderung 2026: vor dem 21. Juli beantragen oder warten?“, https://ema-energiewelt.de/wissen/waermepumpen-foerderung-2026-vor-21-juli-beantragen-oder-warten
- [2] KfW-Merkblatt 458 (Heizungsförderung für Privatpersonen – Wohngebäude). `TODO: Fassung und Datum eintragen`

## Reihenfolge, die nie gebrochen werden darf

1. **Vertrag mit Förderbedingung**: Liefer- und Leistungsvertrag nur mit aufschiebender oder auflösender Bedingung (Förderzusage). Ein unbedingter Vertrag gilt als Vorhabenbeginn, dann entfällt die Förderung. [1]
2. **KfW-Antrag vor Beginn der Arbeiten**: der Kunde stellt den Antrag in „Meine KfW“, mit der „Bestätigung zum Antrag“ (BzA) des Fachunternehmens. [1]
3. **36 Monate ab Zusage**: in dieser Frist muss das Vorhaben abgeschlossen und nachgewiesen sein. [1]

## Regeln (maschinenlesbar)

Format: `- Regel-ID | schluessel = wert | gültig ab | Bedingung | Quelle`. `_tools/foerdercheck.py` liest genau diese Zeilen und schreibt die verwendeten Zeilen in sein Ergebnis.

- R01 | grundfoerderung_prozent = 30 | gültig ab 21.07.2026 | alle Antragsteller | [1]
- R02 | speedbonus_prozent = 16 | gültig ab 21.07.2026 | nur selbstnutzende Eigentümer, die eine fossile Heizung ersetzen | [1]
- R03 | fossile_heizungen = oel, gas, fluessiggas, kohle | gültig ab 21.07.2026 | Heizarten, die als „fossil“ für R02 gelten; Liste zu prüfen gegen [2] | [1]
- R04 | einkommensbonus_stufen_prozent = 40, 30, 10 | gültig ab 21.07.2026 | nur selbstnutzende Eigentümer, gestaffelt nach zu versteuerndem Haushaltseinkommen | [1]
- R05 | einkommensbonus_schwellen_eur = zu prüfen | gültig ab 21.07.2026 | Einkommensgrenzen der Stufen 40 / 30 / 10 %; TODO gegen Merkblatt 458 prüfen, nicht schätzen | [2]
- R06 | hoechstsatz_prozent = 70 | gültig ab 21.07.2026 | Deckel der Summe aller Boni, in % der förderfähigen Kosten | [1]
- R07 | hoechstsatz_niedrig_prozent = 80 | gültig ab 21.07.2026 | statt R06 bei zu versteuerndem Haushaltseinkommen bis zur Grenze R08 | [1]
- R08 | hoechstsatz_niedrig_grenze_eur = 30000 | gültig ab 21.07.2026 | Einkommensgrenze für R07 | [1]
- R09 | kind_zuschlag_grenze_eur = 10000 | gültig ab 21.07.2026 | erhöht die Grenze R08 einmalig, wenn mindestens ein Kind unter 18 im Haushalt lebt | [1]
- R10 | foerderfaehige_kosten_max_eur = 28000 | gültig ab 21.07.2026 | Höchstbetrag förderfähiger Kosten (erste Wohneinheit) | [1]
- R11 | effizienzbonus_kaeltemittel_prozent = 0 | gültig ab 21.07.2026 | kein Effizienzbonus mehr für natürliche Kältemittel | [1]
- R12 | absenkung_start = 2027-02-01 | gültig ab 01.02.2027 | ab diesem Tag sinken R10 und R02 je angefangenem Halbjahr | [1]
- R13 | absenkung_kosten_eur_je_halbjahr = 750 | gültig ab 01.02.2027 | Abzug von R10 je Halbjahr | [1]
- R14 | absenkung_speedbonus_punkte_je_halbjahr = 4 | gültig ab 01.02.2027 | Abzug von R02 je Halbjahr | [1]

## Rechenweg

1. Förderfähige Kosten = Festpreis laut Angebot, höchstens R10 (abzüglich R13 je Halbjahr ab R12).
2. Fördersatz = R01 + R02 (wenn Bedingung erfüllt, abzüglich R14 je Halbjahr ab R12) + Einkommensbonus R04 (wenn Bedingung erfüllt und Stufe bekannt).
3. Fördersatz höchstens R06, bzw. R07 bei Einkommen bis R08 (+ R09 mit Kind unter 18).
4. Erwarteter Zuschuss = förderfähige Kosten × Fördersatz.

Solange R05 „zu prüfen“ ist, rechnet das Angebot mit dem **sicheren Zuschuss ohne Einkommensbonus**. Die möglichen Beträge mit Einkommensbonus stehen nur zur Information im Förder-Check.
