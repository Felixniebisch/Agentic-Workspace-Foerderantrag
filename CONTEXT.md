# Ablauf eines Kundenvorgangs

Der ganze Weg auf einer Seite: welche Stufe was tut, wer prüft und welcher Status danach gilt. Die Einzelheiten jeder Stufe stehen in ihrem `CONTEXT.md`.

## Stufen

| # | Stufe | Der Agent erstellt | Prüfung | Status nach `pass` |
|---|---|---|---|---|
| 01 | [Eingang](01_eingang/CONTEXT.md) | vereinheitlichte Anfragedaten, ggf. Rückfrage-Entwurf | Vollständigkeit (Agent) | `foerdercheck` |
| 02 | [Förder-Check](02_foerdercheck/CONTEXT.md) | erwarteter KfW-Zuschuss per Skript | **Finanzen** gibt frei | `angebot` |
| 03 | [Angebot](03_angebot/CONTEXT.md) | Festpreis minus Zuschuss aus Vorlage | **Vertrieb** gibt frei | `vertrag` |
| 04 | [Vertrag](04_vertrag/CONTEXT.md) | Vertrag mit Förderbedingung | **Skript** `vertrag_check.py` | `antrag` |
| 05 | [Antrag](05_antrag/CONTEXT.md) | BzA, Checkliste und Werte für „Meine KfW“ | KfW-Zusage liegt im Ordner | `bewilligt` |
| 06 | [Nachweis](06_nachweis/CONTEXT.md) | Nachweisunterlagen, 36-Monats-Frist | **Projektleitung** bestätigt Vollständigkeit | `abgeschlossen` |

Statuskette (eine Zeile `status:` in `kunden/<vorgang>/CONTEXT.md`):
`eingang → foerdercheck → angebot → vertrag → antrag → bewilligt → nachweis → abgeschlossen`

`nachweis` gilt, sobald die Installation fertig ist und Stufe 06 beginnt.

## So sieht ein Kundenordner aus

```
kunden/2026-09-hansen-hamburg/
├─ CONTEXT.md          status: …  (die einzige Statuszeile)
├─ 01_eingang/         daten.md, rohanfrage.md, ggf. rueckfrage-entwurf.md, check.md
├─ 02_foerdercheck/    zuschuss.md, check.md
├─ 03_angebot/         angebot.md, check.md
├─ 04_vertrag/         vertrag.md, check.md
├─ 05_antrag/          bza.md, checkliste.md, meine-kfw-werte.md, zusage.md, check.md
└─ 06_nachweis/        nachweis-checkliste.md, frist.md, check.md
```

Ordnername: `JJJJ-MM-nachname-ort` (Monat des Eingangs, Kleinbuchstaben, Umlaute als ae/oe/ue/ss).

## Format jeder Prüfung (`check.md`)

```
pass                          oder   fail: <Grund in einem Satz>

datum: JJJJ-MM-TT
pruefer: Finanzen | Vertrieb | Agent | _tools/<skript>.py | Projektleitung
rueckfragen: <Anzahl>         nur in 01_eingang
```

Ein `fail` hält den Vorgang an dieser Stelle an. Freigaben aus Slack oder E-Mail werden als `check.md` abgelegt (siehe [docs/integration.md](docs/integration.md)).

## Die Reihenfolge, die die Förderung sichert

Vertrag mit Förderbedingung → KfW-Antrag vor Arbeitsbeginn → Abschluss in 36 Monaten. Quelle und Einzelheiten: [_shared/foerderregeln.md](_shared/foerderregeln.md).
