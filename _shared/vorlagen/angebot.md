---
description: Vorlage für das Festpreisangebot abzüglich erwartetem KfW-Zuschuss.
---
# Vorlage: Angebot

Der Agent füllt die Platzhalter aus `01_eingang/daten.md`, `02_foerdercheck/zuschuss.md` und `_shared/produkte.md` und legt das Ergebnis als `kunden/{vorgang}/03_angebot/angebot.md` ab. Er erfindet keine Beträge: jede Zahl kommt aus einer dieser drei Dateien.

---

**Angebot Nr. {vorgang}** · {datum}

{name}, {strasse}, {plz} {ort}

| Position | Betrag |
|---|---|
| {paket_id} {paket_bezeichnung} (Festpreis) | {festpreis_eur} € |
| abzüglich erwarteter KfW-Zuschuss (sicherer Betrag, {foerdersatz} % von {foerderfaehige_kosten_eur} €) | − {zuschuss_sicher_eur} € |
| **Ihr voraussichtlicher Eigenanteil** | **{eigenanteil_eur} €** |

{nur wenn Einkommensbonus offen: „Möglicherweise steht Ihnen zusätzlich ein einkommensabhängiger Bonus zu. Wir prüfen das mit Ihnen vor dem Antrag; im Angebot ist er nicht eingerechnet.“}

Hinweise:
- Der Zuschuss wird von der KfW an Sie ausgezahlt, nicht von hansetherm. Der Festpreis ist unabhängig davon verbindlich.
- Der Vertrag wird mit einer Förderbedingung geschlossen: ohne KfW-Zusage entstehen Ihnen keine Kosten.
- Angebot gültig bis {gueltig_bis}.
