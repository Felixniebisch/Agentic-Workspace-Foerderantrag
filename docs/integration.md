# Anbindung und Datenschutz

Wie der Ablauf im Alltag ausgelöst wird, wo die Ordner liegen können und welche Daten der Agent sieht. Die Stufen selbst stehen in [CONTEXT.md](../CONTEXT.md).

## Auslöser (n8n, Make oder Zapier)

Jedes der drei Werkzeuge reicht; die Abläufe sind gleich.

| Ereignis | Automatisierung | Ergebnis im Arbeitsbereich |
|---|---|---|
| Formular im Online-Planungstool abgeschickt, oder E-Mail von toom eingegangen | Webhook / E-Mail-Trigger kopiert `_templates/kunde/` nach `kunden/JJJJ-MM-nachname-ort/` und legt den Formularinhalt als `01_eingang/rohanfrage.md` ab | neuer Kundenordner, `status: eingang` |
| neuer Kundenordner | ruft den Agenten mit „Stufe 01 für `<vorgang>`“ | `daten.md`, ggf. Rückfrage-Entwurf, `check.md` |
| `check.md` einer Stufe beginnt mit `pass` | Datei-Trigger ruft den Agenten für die nächste Stufe | nächste Stufe läuft bis zu ihrer Prüfung |
| Stufe wartet auf Menschen (02 Finanzen, 03 Vertrieb) | Nachricht in Slack oder per E-Mail mit Link auf das Ergebnis und zwei Knöpfen „Freigeben“ / „Ablehnen (Grund)“ | Antwort wird als `check.md` geschrieben: `pass` oder `fail: <Grund>`, mit `pruefer` und `datum` |
| `check.md` beginnt mit `fail` | Nachricht an die zuständige Person | nichts läuft weiter, bis ein Mensch korrigiert |
| Rückfrage-Entwurf liegt vor | Entwurf erscheint im Postfach des Vertriebs | Mensch prüft und sendet; Antwort des Kunden wird an `rohanfrage.md` angehängt, Stufe 01 läuft neu |
| wöchentlich | ruft `python -I _tools/kennzahlen.py` und `python -I _tools/index.py kunden` | Kennzahlen im Team-Kanal, aktuelle Übersicht |

Der Agent wird immer mit genau einer Stufe und einem Vorgang gerufen. Er liest das `CONTEXT.md` der Stufe und nur die dort genannten Dateien.

## Ablageort

Die Ordner sind gewöhnliche Dateien und Markdown-Texte. Sie können in Google Drive oder SharePoint liegen; die Automatisierung liest und schreibt dort über deren Schnittstelle. Jeder im Team kann den Stand eines Vorgangs ohne zusätzliches Werkzeug öffnen: Ordner aufmachen, `check.md` lesen. Zugriffsrechte werden pro Ordner `kunden/` vergeben.

## Datenschutz

- **Modell in der EU:** der Agent nutzt ein Sprachmodell, das in der EU gehostet und verarbeitet wird, mit Auftragsverarbeitungsvertrag.
- **Kein Training auf Kundendaten:** vertraglich ausgeschlossen; Kundendaten werden nur für die jeweilige Anfrage verarbeitet.
- **Nur die nötigen Felder:** jede Stufe nennt unter „Eingaben“, welche Dateien und Felder sie liest. Der Agent lädt nichts darüber hinaus, keine anderen Kundenordner. Das Angebot sieht z. B. kein Einkommen.
- **Der Agent handelt nie nach außen:** er versendet keine E-Mails, unterschreibt keine Verträge und stellt keine Anträge. Er schreibt Entwürfe; Menschen senden, unterschreiben und beantragen.
- **Nachvollziehbar:** jede Entscheidung liegt als Datei mit Datum und Prüfer vor; jede Förderzahl nennt die Regelzeile, aus der sie stammt.
- **Löschfristen:** `TODO: Aufbewahrungs- und Löschfristen mit Datenschutz festlegen (KfW-Nachweispflichten beachten).`
