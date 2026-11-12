# 02_foerdercheck – erwarteten KfW-Zuschuss berechnen

Eine Aufgabe: den erwarteten Zuschuss aus dem KfW-Programm 458 ausrechnen und Finanzen zur Freigabe vorlegen. Der Agent rechnet nicht selbst, das Skript rechnet, damit jede Zahl auf eine Regelzeile zurückgeht.

Pfade sind relativ zur Wurzel des Arbeitsbereichs.

## Eingaben

- Arbeit (dieser Vorgang): `kunden/{vorgang}/01_eingang/daten.md` (nur Frontmatter; nur wenn `01_eingang/check.md` mit `pass` beginnt)
- Referenz (jeder Vorgang): `_shared/foerderregeln.md`
- Referenz (jeder Vorgang): `_shared/produkte.md`
- Werkzeug: `_tools/foerdercheck.py`

Nicht laden: `rohanfrage.md`, Vorlagen, andere Kundenordner.

## Ablauf

1. Prüfen, dass `kunden/{vorgang}/01_eingang/check.md` mit `pass` beginnt. Sonst anhalten.
2. Ausführen: `python -I _tools/foerdercheck.py kunden/{vorgang} --stichtag <geplantes Antragsdatum>` (ohne `--stichtag`: heute).
3. `zuschuss.md` nicht von Hand ändern. Stimmt etwas nicht, Eingang oder Regeln korrigieren und neu rechnen.
4. Finanzen um Freigabe bitten (Nachricht mit Link auf `zuschuss.md`, siehe [docs/integration.md](../docs/integration.md)). Offene Punkte aus `zuschuss.md` in der Nachricht nennen.
5. Nach Freigabe: `status:` in `kunden/{vorgang}/CONTEXT.md` auf `angebot` setzen.

## Ergebnis

- `kunden/{vorgang}/02_foerdercheck/zuschuss.md` (sicherer Zuschuss, mögliche Beträge mit Einkommensbonus, wörtlich verwendete Regelzeilen)
- `kunden/{vorgang}/02_foerdercheck/check.md` (von Finanzen)

## Prüfung

Mensch, Finanzen: liest `zuschuss.md`, vergleicht Fördersatz und förderfähige Kosten mit den aufgeführten Regelzeilen und entscheidet über offene Punkte (z. B. Einkommensbonus). Schreibt `check.md`: `pass` oder `fail: <Grund>`, `pruefer: Finanzen`.
