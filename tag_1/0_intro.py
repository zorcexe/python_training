"""
Das ist ein Docstring und kein Kommentar (Modul-Docstring)
wer hat das entwickelt?

x + y   Summe von x und y
x - y   Differenz von x und y
x * y   Produkt von x und y
x / y   Quotient von x und y
x % y   Rest beim Teilen von x durch y*
+x  positives Vorzeichen
-x  negatives Vorzeichen
x ** y  x hoch y
x // y  abgerundeter Quotient von x und y*
Operatoren Precedence (Rangfolge)
https://docs.python.org/3/reference/expressions.html#operator-precedence

"""

name = "Bob"
print(name)

x = 2  # alles in Objekt
print("Typ von x:", type(x))  # Objekt der Klasse Integer

# Division erzeugt immer Float
y = 2
result = x / y
print("x/y:", result)

# Abrundungs-Division
print("Floor-Division:", 13 // 4)  # Abrundungs-Division

# Float nach Int umwandeln
value = 2.3  # float
print(int(value))


# round ist eine eingebaute Funktion (siehe pyhton builtin functions)
# https://mimo.org/glossary/python/round-function
value = 2.34342334
print("gerundet", round(value, 2))
