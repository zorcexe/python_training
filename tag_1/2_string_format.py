"""
f-String (String formatieren)
"""

value = 3
print("Das Ergebnis der Berechnung ist", value, "Einheiten")
result = "Das Ergebnis der Berechnung ist " + str(value) + "Einheiten"

# Als Format-String formatiert
print(f"Das Ergebnis der Berechnung ist {value} Einheiten")
result = f"Das Ergebnis der Berechnung ist {value} Einheiten"

# mit der format-Methode
template = "Ein String mit zwei Werten: {} {}"
print(template.format(42, 44))
