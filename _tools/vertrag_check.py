#!/usr/bin/env python3
"""Vertrags-Check: lässt Stufe 04 scheitern, wenn die Förderbedingung im Vertrag fehlt.

    python -I _tools/vertrag_check.py kunden/<vorgang> [--datum JJJJ-MM-TT]

Liest  kunden/<vorgang>/04_vertrag/vertrag.md.
Schreibt kunden/<vorgang>/04_vertrag/check.md, erste Zeile `pass` oder `fail: <grund>`.
Exit-Code 1 bei fail. --datum setzt das Prüfdatum (Standard: heute). Grund für die harte Prüfung: ein Vertrag ohne aufschiebende oder
auflösende Bedingung gilt als Vorhabenbeginn, dann ist die KfW-Förderung verloren.
Nur Standardbibliothek.
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


def pruefen(text):
    """Gibt None zurück, wenn alles stimmt, sonst den Grund."""
    abschnitt = re.search(r"^## Förderbedingung\s*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    if not abschnitt:
        return "Abschnitt „## Förderbedingung“ fehlt (Vorlage _shared/vorlagen/vertragsklausel.md)"
    body = abschnitt.group(1).lower()
    if not re.search(r"(aufschiebende|auflösende)n?\s+bedingung", body):
        return "Förderbedingung nennt weder aufschiebende noch auflösende Bedingung"
    if "kfw" not in body or "458" not in body:
        return "Förderbedingung bezieht sich nicht auf die KfW-Förderung im Programm 458"
    if "{" in body:
        return "Förderbedingung enthält ungefüllte Platzhalter {…}"
    return None


def main(argv):
    if not argv:
        sys.exit(__doc__)
    datum = dt.date.today().isoformat()
    if "--datum" in argv:
        datum = dt.date.fromisoformat(argv[argv.index("--datum") + 1]).isoformat()
    vorgang = Path(argv[0])
    vorgang = vorgang if vorgang.is_absolute() else (ROOT / vorgang)
    vertrag = vorgang / "04_vertrag" / "vertrag.md"
    if not vertrag.exists():
        grund = "vertrag.md fehlt"
    else:
        grund = pruefen(vertrag.read_text(encoding="utf-8"))
    zeile = "pass" if grund is None else f"fail: {grund}"
    check = vorgang / "04_vertrag" / "check.md"
    check.parent.mkdir(parents=True, exist_ok=True)
    check.write_text(
        f"{zeile}\n\n"
        f"datum: {datum}\n"
        f"pruefer: _tools/vertrag_check.py\n",
        encoding="utf-8",
    )
    print(f"{vorgang.name}: {zeile}")
    sys.exit(0 if grund is None else 1)


if __name__ == "__main__":
    main(sys.argv[1:])
