# Demo im Gespräch

1. Zuerst öffnen: [AGENTS.md](AGENTS.md) (Einstieg), dann [CONTEXT.md](CONTEXT.md) (sechs Stufen, wer prüft) und [kunden/_index.md](kunden/_index.md) (drei fiktive Vorgänge mit Status).
2. Übersicht neu erzeugen: `python -I _tools/index.py kunden`
3. Zuschuss für Kunde 1 rechnen, jede Zahl mit Regelzeile: `python -I _tools/foerdercheck.py kunden/2026-09-hansen-hamburg --stichtag 2026-09-15`, dann `02_foerdercheck/zuschuss.md` zeigen.
4. Vertrag ohne Förderbedingung wird gestoppt: `python -I _tools/vertrag_check.py kunden/2026-10-albers-pinneberg --datum 2026-10-20` (endet mit `fail`, Exit 1).
5. Kennzahlen über alle Vorgänge: `python -I _tools/kennzahlen.py` (Durchlaufzeit je Stufe, Rückfragen, Fehlerquote).
