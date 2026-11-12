#!/usr/bin/env python3
"""Förder-Check: erwarteter KfW-458-Zuschuss für einen Kundenvorgang.

    python -I _tools/foerdercheck.py kunden/<vorgang> [--stichtag JJJJ-MM-TT]

Liest  kunden/<vorgang>/01_eingang/daten.md  (Frontmatter),
       _shared/foerderregeln.md  (Zeilen unter „Regeln (maschinenlesbar)“),
       _shared/produkte.md  (Festpreis des Pakets).
Schreibt kunden/<vorgang>/02_foerdercheck/zuschuss.md  mit Ergebnis und den wörtlich
verwendeten Regelzeilen. Stichtag (geplantes Antragsdatum) ist standardmäßig heute.
Rechnet nichts, was nicht in foerderregeln.md steht: eine Regel „zu prüfen“ bleibt offen.
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
REGELN = ROOT / "_shared" / "foerderregeln.md"
PRODUKTE = ROOT / "_shared" / "produkte.md"
RULE = re.compile(r"^- (R\d{2}) \| (\w+) = ([^|]+?) \|")


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    data = {}
    for line in text[3:end].splitlines():
        if ":" in line and not line.lstrip().startswith("#"):
            k, v = line.split(":", 1)
            data[k.strip()] = re.split(r"\s+#", v.strip(), maxsplit=1)[0].strip()
    return data


def regeln():
    rules, lines = {}, {}
    for line in REGELN.read_text(encoding="utf-8").splitlines():
        m = RULE.match(line)
        if m:
            rid, key, val = m.groups()
            rules[key] = val.strip()
            lines[key] = line
    return rules, lines


def festpreis(paket):
    for line in PRODUKTE.read_text(encoding="utf-8").splitlines():
        if line.startswith(f"- {paket} |"):
            m = re.search(r"festpreis_eur = (\d+)", line)
            name = line.split("|")[1].strip()
            return int(m.group(1)), name, line
    sys.exit(f"Paket {paket!r} nicht in _shared/produkte.md")


def halbjahre_seit(start, stichtag):
    """Angefangene Halbjahre ab start (start selbst zählt als erstes)."""
    if stichtag < start:
        return 0
    monate = (stichtag.year - start.year) * 12 + stichtag.month - start.month
    if stichtag.day < start.day:
        monate -= 1
    return monate // 6 + 1


def eur(x):
    return f"{x:,.0f}".replace(",", ".")


def main(argv):
    if not argv or argv[0].startswith("-"):
        sys.exit(__doc__)
    vorgang = (ROOT / argv[0]).resolve() if not Path(argv[0]).is_absolute() else Path(argv[0])
    stichtag = dt.date.today()
    if "--stichtag" in argv:
        stichtag = dt.date.fromisoformat(argv[argv.index("--stichtag") + 1])

    daten_path = vorgang / "01_eingang" / "daten.md"
    if not daten_path.exists():
        sys.exit(f"fehlt: {daten_path.relative_to(ROOT)}")
    d = frontmatter(daten_path)
    pflicht = ["produkt", "heizung_aktuell", "selbstgenutzt", "einkommen_zve_bis_eur", "kinder_unter_18"]
    leer = [k for k in pflicht if not d.get(k)]
    if leer:
        sys.exit(f"Eingang unvollständig, Förder-Check nicht möglich: {', '.join(leer)}")

    r, rl = regeln()
    used = []

    def use(key):
        used.append(rl[key])
        return r[key]

    preis, paket_name, paket_zeile = festpreis(d["produkt"])

    # Absenkung ab Stichtag
    n = halbjahre_seit(dt.date.fromisoformat(use("absenkung_start")), stichtag)
    kosten_max = int(use("foerderfaehige_kosten_max_eur"))
    speed = int(use("speedbonus_prozent"))
    if n:
        kosten_max -= n * int(use("absenkung_kosten_eur_je_halbjahr"))
        speed = max(0, speed - n * int(use("absenkung_speedbonus_punkte_je_halbjahr")))
    kosten = min(preis, kosten_max)

    selbst = d["selbstgenutzt"].lower() in ("ja", "true", "yes")
    fossil = [h.strip() for h in use("fossile_heizungen").split(",")]
    satz = int(use("grundfoerderung_prozent"))
    posten = [f"Grundförderung {satz} %"]
    if selbst and d["heizung_aktuell"].lower() in fossil:
        satz += speed
        posten.append(f"Klima-Geschwindigkeitsbonus {speed} %")
    else:
        use("speedbonus_prozent")
        posten.append("Klima-Geschwindigkeitsbonus 0 % (nicht selbstgenutzt oder keine fossile Heizung)")
    use("effizienzbonus_kaeltemittel_prozent")

    einkommen = int(d["einkommen_zve_bis_eur"])
    kind = int(d["kinder_unter_18"]) > 0
    grenze = int(use("hoechstsatz_niedrig_grenze_eur"))
    if kind:
        grenze += int(use("kind_zuschlag_grenze_eur"))
    if einkommen <= grenze:
        deckel = int(use("hoechstsatz_niedrig_prozent"))
    else:
        deckel = int(use("hoechstsatz_prozent"))

    stufen = [int(s) for s in use("einkommensbonus_stufen_prozent").split(",")]
    schwellen = use("einkommensbonus_schwellen_eur")
    offen = []
    moeglich = []
    if not selbst:
        posten.append("Einkommensbonus 0 % (nur für selbstnutzende Eigentümer)")
    elif schwellen == "zu prüfen":
        offen.append("Einkommensbonus: Stufengrenzen in foerderregeln.md R05 sind „zu prüfen“ "
                     "(TODO Merkblatt 458). Im sicheren Zuschuss nicht enthalten.")
        for s in stufen:
            m_satz = min(satz + s, deckel)
            moeglich.append((s, m_satz, round(kosten * m_satz / 100)))
    else:
        offen.append("R05 ist eingetragen, aber dieses Skript ordnet Stufen noch nicht zu: bitte ergänzen.")

    satz_sicher = min(satz, deckel)
    zuschuss = round(kosten * satz_sicher / 100)

    rel = vorgang.relative_to(ROOT).as_posix()
    out = vorgang / "02_foerdercheck" / "zuschuss.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    text = [
        "---",
        f"vorgang: {vorgang.name}",
        f"stichtag: {stichtag.isoformat()}",
        f"festpreis_eur: {preis}",
        f"foerderfaehige_kosten_eur: {kosten}",
        f"foerdersatz_sicher_prozent: {satz_sicher}",
        f"zuschuss_sicher_eur: {zuschuss}",
        f"hoechstsatz_prozent: {deckel}",
        f"einkommensbonus: {'offen' if moeglich else 'entfällt'}",
        "erzeugt_von: _tools/foerdercheck.py",
        "---",
        f"# Förder-Check {vorgang.name}",
        "",
        f"Erzeugt von `_tools/foerdercheck.py` aus `{rel}/01_eingang/daten.md`. Nicht von Hand ändern: "
        "Eingang oder Regeln ändern und neu rechnen.",
        "",
        "## Ergebnis",
        "",
        "| Größe | Wert |",
        "|---|---|",
        f"| Paket | {d['produkt']} {paket_name} |",
        f"| Festpreis | {eur(preis)} € |",
        f"| förderfähige Kosten (max. {eur(kosten_max)} €) | {eur(kosten)} € |",
        f"| Fördersatz sicher | Summe {satz} %, Deckel {deckel} % → **{satz_sicher} %** |",
        f"| **erwarteter Zuschuss (sicher)** | **{eur(zuschuss)} €** |",
        "",
        "Bestandteile: " + "; ".join(posten) + ".",
        "",
    ]
    if moeglich:
        text += ["## Möglich mit Einkommensbonus (nur Information, nicht im Angebot)", "",
                 "| Stufe | Fördersatz (gedeckelt) | Zuschuss |", "|---|---|---|"]
        text += [f"| +{s} % | {ms} % | {eur(z)} € |" for s, ms, z in moeglich]
        text += [""]
    text += ["## Offene Punkte für Finanzen", ""]
    text += [f"- {o}" for o in offen] or ["- keine"]
    text += ["", "## Verwendete Regelzeilen (wörtlich aus `_shared/foerderregeln.md`)", ""]
    seen = []
    for line in used:
        if line not in seen:
            seen.append(line)
    text += sorted(seen) + ["", "## Verwendete Produktzeile (aus `_shared/produkte.md`)", "", paket_zeile, ""]
    out.write_text("\n".join(text), encoding="utf-8")
    print(f"{rel}: Zuschuss sicher {eur(zuschuss)} € ({satz_sicher} % von {eur(kosten)} €), "
          f"Einkommensbonus {'offen' if moeglich else 'entfällt'} -> {out.relative_to(ROOT).as_posix()}")


if __name__ == "__main__":
    main(sys.argv[1:])
