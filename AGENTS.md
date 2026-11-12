# hansetherm Förderantrag-Ablauf

Dieser Arbeitsbereich führt jeden Kundenvorgang von der Anfrage (Online-Planungstool oder Partner toom) bis zur KfW-Zusage und zum Verwendungsnachweis. Ein KI-Agent arbeitet die nummerierten Stufen ab; nach jeder Stufe prüft ein Mensch oder ein Skript, bevor es weitergeht. Diese Datei leitet nur weiter, Inhalte stehen in den verlinkten Dateien.

## Wo was liegt

| Ordner | Inhalt |
|---|---|
| `01_eingang/` … `06_nachweis/` | die Stufen in Reihenfolge; je ein `CONTEXT.md` mit Eingaben, Ablauf, Ergebnis, Prüfung |
| `kunden/` | ein Ordner pro Kundenvorgang; dort liegen die Ergebnisse jeder Stufe und ihr `check.md` |
| `_shared/` | gleich für jeden Vorgang: Förderregeln, Produkte, Vorlagen |
| `_templates/kunde/` | Stempel: ein neuer Vorgang ist eine Kopie davon |
| `_tools/` | Skripte, Katalog in [_tools/CONTEXT.md](_tools/CONTEXT.md) |
| `docs/` | Anbindung an n8n / Make / Zapier und Datenschutz |

## Wohin bei welcher Aufgabe

| Wenn | Dann | Halt bei |
|---|---|---|
| neue Anfrage eingegangen | Ordner aus `_templates/kunde/` stempeln, dann [01_eingang](01_eingang/CONTEXT.md) | `check.md` der Stufe |
| eine Stufe hat `pass` | nächste nummerierte Stufe | deren `check.md` |
| eine Stufe hat `fail` | nichts weiter; Grund steht in der ersten Zeile | Mensch entscheidet |
| Förderregeln ändern sich | nur [_shared/foerderregeln.md](_shared/foerderregeln.md) | neues „gültig ab“ |
| Frage nach Status | `kunden/_index.md` (neu erzeugen: `python -I _tools/index.py kunden`) | Bericht |
| Frage nach Kennzahlen | `python -I _tools/kennzahlen.py` | Bericht |
| Ablauf im Überblick | [CONTEXT.md](CONTEXT.md) | – |

## Regeln

- Keine Stufe beginnt, bevor die vorige ein `check.md` mit erster Zeile `pass` hat.
- Der Agent liest pro Stufe nur die Dateien, die deren `CONTEXT.md` unter „Eingaben“ nennt.
- Der Agent versendet, unterschreibt oder beantragt nie selbst. Er schreibt Entwürfe; Menschen senden.
- Förderregeln stehen nur in `_shared/foerderregeln.md`. Erzeugte Dateien nicht von Hand ändern: Eingabe ändern und neu erzeugen.
- Alle Kundendaten in dieser Demo sind fiktiv.
