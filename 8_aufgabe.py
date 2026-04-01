# Aufgabe, es soll ermittelt werden, wieviele Städte ein "ü" im Namen haben
# for, in-Operator, Counter
# Ergebnis: es sind 3 Einträge mit ü enhalten

cities = [
    ["hamburg", 223],
    ["nürnberg", 23],
    ["münchen", 23],
    ["düsseldorf", 83],
]

zaehler = 0

for city in cities:
    if "ü" in city[0]:
        zaehler += 1

print(f"Anzahl der Städte mit Ü ist: {zaehler}")
