# 03_angebot – Festpreisangebot abzüglich Zuschuss

Eine Aufgabe: aus Paket, Festpreis und freigegebenem Zuschuss das Angebot schreiben. Der Agent übernimmt Zahlen nur aus den Eingaben, er rechnet nur die Differenz Festpreis minus sicherer Zuschuss.

Pfade sind relativ zur Wurzel des Arbeitsbereichs.

## Eingaben

- Arbeit (dieser Vorgang): `kunden/{vorgang}/02_foerdercheck/zuschuss.md` (nur wenn `02_foerdercheck/check.md` mit `pass` beginnt)
- Arbeit (dieser Vorgang): `kunden/{vorgang}/01_eingang/daten.md` (nur `name`, `strasse`, `plz`, `ort`, `produkt`)
- Referenz (jeder Vorgang): `_shared/vorlagen/angebot.md`
- Referenz (jeder Vorgang): `_shared/produkte.md`

Nicht laden: `_shared/foerderregeln.md` (der Zuschuss ist bereits gerechnet und freigegeben), andere Kundenordner.

## Ablauf

1. Prüfen, dass `02_foerdercheck/check.md` mit `pass` beginnt. Sonst anhalten.
2. Vorlage `_shared/vorlagen/angebot.md` füllen. Eigenanteil = `festpreis_eur` − `zuschuss_sicher_eur` aus `zuschuss.md`. Gültig bis: Angebotsdatum + 4 Wochen.
3. Steht in `zuschuss.md` `einkommensbonus: offen`, den Hinweissatz der Vorlage übernehmen; den Bonus nicht einrechnen.
4. Vertrieb um Freigabe bitten. Der Agent schickt das Angebot nicht an den Kunden.
5. Nach Freigabe: `status:` auf `vertrag` setzen.

## Ergebnis

- `kunden/{vorgang}/03_angebot/angebot.md`
- `kunden/{vorgang}/03_angebot/check.md` (von Vertrieb)

## Prüfung

Mensch, Vertrieb: Paket passt zur Wohnfläche laut `produkte.md`, Beträge stimmen mit `zuschuss.md` überein, kein Platzhalter `{…}` übrig. Schreibt `check.md` mit `pruefer: Vertrieb`. Vertrieb versendet das Angebot.
