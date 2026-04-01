"""
Recap der wichtigsten Datentypen

- Zahlen (int, float)
- String (Sequenz, iterieren, Zugriff per Index, Slicing)
- List (Sequenz, iterieren, Zugriff per Index, Slicing)
- Dict (Key-Value-Speicher, Zugriff per Schlüssel)
- Boolean (True, False)
- None (häufig als Rückgabewert von Funktionen)
"""

# String
city = "Nürnberg"
for char in city:
    print(char)

# Slicing auf Strings
print(city[2:])  # rnberg

# Slicing auf Listen
cities = [
    "Berlin",
    "Nürnberg",
    "Dortmund",
    "Fürth",
]
print(cities[2:])  # ['Dortmund', 'Fürth']

# Dict
persons = {
    "bob": 43,
    "alice": 41,
}
for name, age in persons.items():
    print(f"{name} ist {age} Jahre alt")

# da None nur einmal im System vorkommt, wird mit dem is-opertor geprüft,
# ob ein Wert none ist.
v = None
if v is None:
    print("v ist None")
