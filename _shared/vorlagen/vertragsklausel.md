---
description: Pflichtklausel für jeden Vertrag – die Förderbedingung, ohne die die Förderung verloren geht.
---
# Vorlage: Vertragsklausel Förderbedingung

Jeder Vertrag in `kunden/{vorgang}/04_vertrag/vertrag.md` enthält eine der beiden Varianten wörtlich als eigenen Abschnitt `## Förderbedingung`. `_tools/vertrag_check.py` lässt die Stufe scheitern, wenn sie fehlt. Grund: ein unbedingter Vertrag gilt als Vorhabenbeginn, und dann ist die KfW-Förderung verloren (siehe `../foerderregeln.md`, Reihenfolge).

Juristischer Wortlaut: Demo-Fassung. `TODO: vor echtem Einsatz rechtlich prüfen lassen.`

## Variante A: aufschiebende Bedingung (Standard)

> Dieser Vertrag steht unter der aufschiebenden Bedingung, dass dem Auftraggeber eine Förderzusage der KfW im Programm 458 erteilt wird. Bis zum Eintritt der Bedingung entstehen keine Leistungs- oder Zahlungspflichten. Tritt die Bedingung nicht binnen {frist_monate} Monaten ein, gilt der Vertrag als nicht geschlossen.

## Variante B: auflösende Bedingung

> Dieser Vertrag steht unter der auflösenden Bedingung, dass die KfW den Antrag des Auftraggebers im Programm 458 ablehnt. Mit Zugang der Ablehnung endet der Vertrag; bereits geleistete Zahlungen werden erstattet. Mit Arbeiten vor Ort wird erst nach Zugang der Förderzusage begonnen.
