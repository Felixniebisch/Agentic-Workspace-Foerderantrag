---
description: Vorlage für die Rückfrage an den Kunden, wenn Angaben im Eingang fehlen.
---
# Vorlage: Rückfrage-E-Mail

Der Agent füllt die Platzhalter `{…}` und legt den Entwurf als `kunden/{vorgang}/01_eingang/rueckfrage-entwurf.md` ab. Er verschickt nichts: ein Mensch prüft und sendet. Eine Frage pro fehlendem Feld, in der Reihenfolge der Pflichtfelder.

---

**Betreff:** Ihre Wärmepumpen-Planung – uns fehlt noch {anzahl} Angabe(n)

Guten Tag {anrede} {nachname},

vielen Dank für Ihre Anfrage über {quelle}. Damit wir Ihre Förderung berechnen und Ihnen ein Festpreisangebot schicken können, brauchen wir noch:

{fragen: eine nummerierte Zeile pro fehlendem Feld, mit kurzer Erklärung, wofür wir es brauchen}

Antworten Sie einfach auf diese E-Mail. Sobald die Angaben da sind, melden wir uns innerhalb von zwei Werktagen mit Ihrem Förder-Check.

Viele Grüße
{bearbeiter}
