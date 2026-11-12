# Werkzeuge

Katalog der Skripte. Alle laufen mit Python 3 ohne Zusatzpakete, aus der Wurzel des Arbeitsbereichs. `-I` startet Python isoliert, damit nur diese Skripte geladen werden.

| Skript | Wofür | Befehl | Schreibt |
|---|---|---|---|
| `foerdercheck.py` | erwarteter KfW-458-Zuschuss (Stufe 02) | `python -I _tools/foerdercheck.py kunden/<vorgang> [--stichtag JJJJ-MM-TT]` | `kunden/<vorgang>/02_foerdercheck/zuschuss.md` |
| `vertrag_check.py` | Förderbedingung im Vertrag vorhanden? (Stufe 04) | `python -I _tools/vertrag_check.py kunden/<vorgang> [--datum JJJJ-MM-TT]` | `kunden/<vorgang>/04_vertrag/check.md`, Exit 1 bei fail |
| `kennzahlen.py` | Durchlaufzeit je Stufe, Rückfragen, Fehlerquote | `python -I _tools/kennzahlen.py` | nichts, nur Ausgabe |
| `index.py` | Übersicht aller Vorgänge mit Status | `python -I _tools/index.py kunden` | `kunden/_index.md` |
| `links.py` | prüft, dass jeder Link und jeder Eingabepfad existiert | `python -I _tools/links.py` | nichts, Exit 1 bei Fehlern |

Hinweise:
- `foerdercheck.py` liest die Regelzeilen unter „Regeln (maschinenlesbar)“ in `_shared/foerderregeln.md`. Neue Regel = neue Zeile dort, dann das Skript erweitern; nie einen Wert im Skript festschreiben.
- `links.py` erkennt Eingabelisten unter den Überschriften „Inputs“ und „Eingaben“; Zeilen mit „Referenz“ müssen schon existieren.
- `_index.md` wird nur erzeugt, nie von Hand geändert.
