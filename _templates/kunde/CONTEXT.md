---
title: {vorgang}
description: {Name}, {Ort} – {Paket}, Quelle {planungstool|toom}
status: eingang
---
# Kundenvorgang {vorgang}

Ein Kundenvorgang von der Anfrage bis zum Nachweis. Die Zeile `status:` oben ist die einzige Stelle, an der der Stand steht. Jede Stufe legt ihre Ergebnisse und ihr `check.md` in den gleichnamigen Unterordner.

| Stufe | Ordner | Regeln der Stufe |
|---|---|---|
| Eingang | `01_eingang/` | [01_eingang/CONTEXT.md](../../01_eingang/CONTEXT.md) |
| Förder-Check | `02_foerdercheck/` | [02_foerdercheck/CONTEXT.md](../../02_foerdercheck/CONTEXT.md) |
| Angebot | `03_angebot/` | [03_angebot/CONTEXT.md](../../03_angebot/CONTEXT.md) |
| Vertrag | `04_vertrag/` | [04_vertrag/CONTEXT.md](../../04_vertrag/CONTEXT.md) |
| Antrag | `05_antrag/` | [05_antrag/CONTEXT.md](../../05_antrag/CONTEXT.md) |
| Nachweis | `06_nachweis/` | [06_nachweis/CONTEXT.md](../../06_nachweis/CONTEXT.md) |
