# 01_eingang – Anfragedaten vereinheitlichen

Eine Aufgabe: die Anfrage eines Kunden in ein festes Datenformat bringen und prüfen, ob alles da ist. Fehlt etwas, entsteht ein Rückfrage-Entwurf und die Stufe bleibt offen. Diese Stufe rechnet keine Förderung und schreibt kein Angebot.

Pfade sind relativ zur Wurzel des Arbeitsbereichs. `{vorgang}` ist der Kundenordner, z. B. `2026-09-hansen-hamburg`.

## Eingaben

- Arbeit (dieser Vorgang): `kunden/{vorgang}/01_eingang/rohanfrage.md` (Formular-Export aus dem Planungstool oder Weiterleitung von toom, unverändert)
- Arbeit (dieser Vorgang): `kunden/{vorgang}/01_eingang/daten.md` (aus dem Stempel; hier wird eingetragen)
- Referenz (jeder Vorgang): `_shared/vorlagen/rueckfrage-email.md`
- Referenz (jeder Vorgang): `_shared/produkte.md` (nur die Paket-IDs, um `produkt` zu prüfen)

Nicht laden: `_shared/foerderregeln.md`, andere Kundenordner, spätere Stufen.

## Ablauf

1. Fehlt `rohanfrage.md` oder ist sie leer: anhalten und das melden.
2. Jedes Pflichtfeld aus der Rohanfrage in das Frontmatter von `daten.md` übertragen, in dieser Form:

| Feld | Form | Beispiel |
|---|---|---|
| `quelle` | `planungstool` oder `toom` | `planungstool` |
| `eingang_am` | JJJJ-MM-TT | `2026-09-01` |
| `name`, `strasse`, `plz`, `ort` | wie angegeben | `Jens Hansen` |
| `baujahr` | vierstellige Jahreszahl | `1978` |
| `heizung_aktuell` | `oel`, `gas`, `fluessiggas`, `kohle`, `nachtspeicher`, `waermepumpe`, `sonstige` | `gas` |
| `wohnflaeche_m2` | ganze Zahl | `145` |
| `selbstgenutzt` | `ja` / `nein` | `ja` |
| `haushalt_personen` | ganze Zahl | `4` |
| `einkommen_zve_bis_eur` | Obergrenze der angegebenen Einkommensklasse (zu versteuerndes Haushaltseinkommen), ganze Zahl | `60000` |
| `kinder_unter_18` | Anzahl, ganze Zahl | `2` |
| `produkt` | Paket-ID aus `_shared/produkte.md` | `HT-L09` |

3. Nur übertragen, was in der Rohanfrage steht. Nichts schätzen, nichts aus anderen Feldern ableiten. Unklares bleibt leer.
4. Ist ein Pflichtfeld leer oder unplausibel (Baujahr in der Zukunft, Paket-ID unbekannt): aus `_shared/vorlagen/rueckfrage-email.md` den Entwurf `rueckfrage-entwurf.md` schreiben, eine Frage pro Feld. Nicht versenden.
5. `check.md` schreiben (Format in [CONTEXT.md](../CONTEXT.md)). `rueckfragen:` zählt alle Fragen, die in diesem Vorgang je gestellt wurden, auch schon beantwortete.
6. Bei `pass`: in `kunden/{vorgang}/CONTEXT.md` die Zeile `status:` auf `foerdercheck` setzen.

## Ergebnis

- `kunden/{vorgang}/01_eingang/daten.md` (Frontmatter vollständig oder mit leeren Feldern)
- `kunden/{vorgang}/01_eingang/rueckfrage-entwurf.md` (nur wenn etwas fehlt)
- `kunden/{vorgang}/01_eingang/check.md`

## Prüfung

Agent: jedes Pflichtfeld aus Schritt 2 ist gefüllt und hat die genannte Form → `pass`. Sonst `fail: fehlt <felder>` und ein Rückfrage-Entwurf liegt daneben. Kommt die Antwort des Kunden, wird sie unten an `rohanfrage.md` angehängt und die Stufe neu ausgeführt.
