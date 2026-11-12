# 06_nachweis – Verwendungsnachweis und Frist

Eine Aufgabe: nach der Installation die Unterlagen für den Nachweis bei der KfW zusammenstellen und die 36-Monats-Frist ab Zusage im Blick halten.

Pfade sind relativ zur Wurzel des Arbeitsbereichs.

## Eingaben

- Arbeit (dieser Vorgang): `kunden/{vorgang}/05_antrag/zusage.md` (Zusagedatum)
- Arbeit (dieser Vorgang): `kunden/{vorgang}/06_nachweis/` (Rechnung, Fachunternehmererklärung, Inbetriebnahmeprotokoll, sobald sie vorliegen)
- Referenz (jeder Vorgang): `_shared/foerderregeln.md` (nur Abschnitt „Reihenfolge“, Punkt 3)

Nicht laden: Angebot, Vertrag, Förder-Check, andere Kundenordner.

## Ablauf

1. Prüfen, dass `05_antrag/check.md` mit `pass` beginnt und die Installation abgeschlossen ist. Dann `status:` auf `nachweis` setzen.
2. `frist.md` schreiben: Zusagedatum, Fristende (Zusagedatum + 36 Monate), Erinnerungen 6 und 3 Monate vor Fristende.
3. `nachweis-checkliste.md` schreiben: jede benötigte Unterlage mit Status `liegt vor` / `fehlt`.
4. Fehlt etwas: Entwurf einer Nachricht an Kunde oder Monteur, nicht versenden.
5. Liegt alles vor: Projektleitung prüft. Der Kunde reicht den Nachweis in „Meine KfW“ ein.

## Ergebnis

- `kunden/{vorgang}/06_nachweis/frist.md`
- `kunden/{vorgang}/06_nachweis/nachweis-checkliste.md`
- `kunden/{vorgang}/06_nachweis/check.md`

## Prüfung

Mensch, Projektleitung: jede Zeile der Checkliste steht auf `liegt vor`, das Fristende ist nicht überschritten. Schreibt `check.md` mit `pruefer: Projektleitung`. Bei `pass`: `status:` auf `abgeschlossen`.
