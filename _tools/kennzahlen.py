#!/usr/bin/env python3
"""Kennzahlen über alle Kundenvorgänge: Durchlaufzeit je Stufe, Rückfragen, Fehlerquote.

    python -I _tools/kennzahlen.py

Liest jede kunden/*/NN_*/check.md (erste Zeile `pass` oder `fail: <grund>`, Zeilen `datum:`
und optional `rueckfragen:`) und den Eingangstag `eingang_am` aus kunden/*/01_eingang/daten.md.
Durchlaufzeit einer Stufe = Datum ihres check.md minus Datum des check.md der Stufe davor
(Stufe 01: minus Eingangstag). Schreibt nichts, gibt nur aus. Nur Standardbibliothek.
"""
import datetime as dt
import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = Path(__file__).resolve().parent.parent
STUFEN = ["01_eingang", "02_foerdercheck", "03_angebot", "04_vertrag", "05_antrag", "06_nachweis"]


def feld(text, name):
    m = re.search(rf"^{name}:\s*(\S+)", text, re.M)
    return m.group(1) if m else None


def main():
    kunden = sorted(p for p in (ROOT / "kunden").iterdir() if p.is_dir() and not p.name.startswith("_"))
    dauer = {s: [] for s in STUFEN}
    checks = fails = rueckfragen = 0
    offen_fail = []
    for k in kunden:
        daten = k / "01_eingang" / "daten.md"
        vorher = feld(daten.read_text(encoding="utf-8"), "eingang_am") if daten.exists() else None
        for s in STUFEN:
            c = k / s / "check.md"
            if not c.exists():
                break
            text = c.read_text(encoding="utf-8")
            erste = text.splitlines()[0].strip() if text.strip() else ""
            checks += 1
            if erste.startswith("fail"):
                fails += 1
                offen_fail.append(f"{k.name}/{s}: {erste}")
            rueckfragen += int(feld(text, "rueckfragen") or 0)
            datum = feld(text, "datum")
            if datum and vorher:
                dauer[s].append((dt.date.fromisoformat(datum) - dt.date.fromisoformat(vorher)).days)
            vorher = datum
            if erste.startswith("fail"):
                break

    print(f"Kundenvorgänge: {len(kunden)}\n")
    print(f"{'Stufe':<17}{'Prüfungen':>10}{'Ø Tage':>9}{'max Tage':>10}")
    for s in STUFEN:
        d = dauer[s]
        avg = f"{sum(d) / len(d):.1f}" if d else "–"
        mx = str(max(d)) if d else "–"
        print(f"{s:<17}{len(d):>10}{avg:>9}{mx:>10}")
    quote = f"{100 * fails / checks:.0f} %" if checks else "–"
    print(f"\nRückfragen an Kunden gesamt: {rueckfragen}")
    print(f"Fehlerquote der Prüfungen:   {fails} von {checks} = {quote}")
    for f in offen_fail:
        print(f"  offen: {f}")


if __name__ == "__main__":
    main()
