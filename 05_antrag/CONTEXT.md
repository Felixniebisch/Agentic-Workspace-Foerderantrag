# 05_antrag – KfW-Antrag vorbereiten

Eine Aufgabe: alles vorbereiten, damit der Kunde seinen Antrag in „Meine KfW“ selbst stellen kann, bevor die Arbeiten beginnen. hansetherm stellt die „Bestätigung zum Antrag“ (BzA) aus; den Antrag stellt nur der Kunde.

Pfade sind relativ zur Wurzel des Arbeitsbereichs.

## Eingaben

- Arbeit (dieser Vorgang): `kunden/{vorgang}/04_vertrag/check.md` (muss mit `pass` beginnen)
- Arbeit (dieser Vorgang): `kunden/{vorgang}/02_foerdercheck/zuschuss.md` (förderfähige Kosten, Fördersatz)
- Arbeit (dieser Vorgang): `kunden/{vorgang}/01_eingang/daten.md` (nur `name`, Anschrift, `selbstgenutzt`, `heizung_aktuell`, `kinder_unter_18`, `einkommen_zve_bis_eur`)
- Referenz (jeder Vorgang): `_shared/foerderregeln.md` (nur Abschnitt „Reihenfolge“)

Nicht laden: `vertrag.md` im Volltext, `angebot.md`, andere Kundenordner.

## Ablauf

1. Prüfen, dass `04_vertrag/check.md` mit `pass` beginnt. Sonst anhalten.
2. `bza.md` schreiben: die Angaben, die hansetherm für die BzA bestätigt (Vorhaben, Paket, förderfähige Kosten, Standort). hansetherm stellt die BzA im KfW-Portal aus; die BzA-ID wird hier eingetragen, sobald sie vorliegt.
3. `checkliste.md` schreiben: die Schritte für den Kunden, persönlich (welche Boni für ihn in Frage kommen, welche Nachweise er bereithalten muss, z. B. Einkommensteuerbescheid, wenn der Einkommensbonus offen ist).
4. `meine-kfw-werte.md` schreiben: Feld für Feld die Werte, die der Kunde in „Meine KfW“ einträgt, jede Zahl mit Herkunft (`zuschuss.md` oder `daten.md`).
5. Kunde stellt den Antrag. Der Agent stellt nichts, sendet nichts. Vertrieb übergibt die Unterlagen.
6. Kommt die Zusage: als `zusage.md` ablegen (Datum, Zusagenummer, Betrag), `check.md` schreiben, `status:` auf `bewilligt` setzen.

## Ergebnis

- `kunden/{vorgang}/05_antrag/bza.md`
- `kunden/{vorgang}/05_antrag/checkliste.md`
- `kunden/{vorgang}/05_antrag/meine-kfw-werte.md`
- `kunden/{vorgang}/05_antrag/zusage.md` (wenn die KfW zugesagt hat)
- `kunden/{vorgang}/05_antrag/check.md`

## Prüfung

Die KfW-Zusage liegt als `zusage.md` im Ordner und nennt Datum, Zusagenummer und Betrag → `pass`, `pruefer: Vertrieb`. Ohne Zusage bleibt die Stufe offen; bei Ablehnung `fail: KfW-Ablehnung <Grund>`.
