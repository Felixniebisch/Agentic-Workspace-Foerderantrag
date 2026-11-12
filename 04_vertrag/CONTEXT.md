# 04_vertrag – Vertrag mit Förderbedingung

Eine Aufgabe: den Liefer- und Leistungsvertrag erstellen, immer mit Förderbedingung. Ein Vertrag ohne aufschiebende oder auflösende Bedingung gilt als Vorhabenbeginn, und die Förderung ist verloren. Deshalb prüft hier ein Skript und kein Mensch: der Fehler darf nie durchrutschen.

Pfade sind relativ zur Wurzel des Arbeitsbereichs.

## Eingaben

- Arbeit (dieser Vorgang): `kunden/{vorgang}/03_angebot/angebot.md` (nur wenn `03_angebot/check.md` mit `pass` beginnt und der Kunde angenommen hat)
- Arbeit (dieser Vorgang): `kunden/{vorgang}/01_eingang/daten.md` (nur `name`, `strasse`, `plz`, `ort`)
- Referenz (jeder Vorgang): `_shared/vorlagen/vertragsklausel.md`
- Werkzeug: `_tools/vertrag_check.py`

Nicht laden: `zuschuss.md`, `_shared/foerderregeln.md`, andere Kundenordner.

## Ablauf

1. Prüfen, dass `03_angebot/check.md` mit `pass` beginnt. Sonst anhalten.
2. `vertrag.md` schreiben: Parteien, Leistung und Festpreis aus `angebot.md`, dann den Abschnitt `## Förderbedingung` mit Variante A (Standard) oder B aus der Vorlage, wörtlich, Platzhalter gefüllt.
3. Ausführen: `python -I _tools/vertrag_check.py kunden/{vorgang}`. Das Skript schreibt `check.md`.
4. Bei `fail`: anhalten. Der Vertrag geht nicht zur Unterschrift. Klausel einsetzen und Schritt 3 wiederholen.
5. Bei `pass`: `status:` auf `antrag` setzen. Unterschrieben wird außerhalb dieses Arbeitsbereichs, von Menschen.

## Ergebnis

- `kunden/{vorgang}/04_vertrag/vertrag.md`
- `kunden/{vorgang}/04_vertrag/check.md` (vom Skript)

## Prüfung

Skript: `python -I _tools/vertrag_check.py kunden/{vorgang}` schreibt `pass` nur, wenn ein Abschnitt `## Förderbedingung` existiert, der eine aufschiebende oder auflösende Bedingung nennt, sich auf KfW 458 bezieht und keinen Platzhalter enthält. Sonst `fail: <Grund>`, Exit-Code 1.
