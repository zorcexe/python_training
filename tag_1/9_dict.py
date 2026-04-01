"""
Dictionary (ein key-value Speicher)
https://www.w3schools.com/python/python_dictionaries.asp
"""

d = {}  # leeres Dict
print(f"der Typ eines dicts {type(d)}")

# ein dict für Konfig (Schlüssel => Wert)
config = {
    "cpu": 4,
    "memory": 1024,
}

# ein Mapping von Tier auf Liste von englischen Tiernamen
de_en = {
    "katze": ["cat", "tom"],
    "vogel": ["bird", "xyz"],
}
de_en["hund"] = ["Dog", "Doggy"]

# Zugriff erfolt immer direkt via Schlüssel
print(f"config[cpu] {config["cpu"]}")

# Zugriff auf katze (de_en["katze"] ist eine Liste, also kann man iterieren)
for name in de_en["katze"]:
    print(name)


# get-Methode: liefert einen Wert aus einem Dict (via Key), falls Wert nicht vorhanden
# ist, gibt es einen Defaultwert
print("Zugriff auf Memory", config.get("memory", 2048))

# Usereingabe ist nicht im Dict vorhanden: Key-Error
user_input = "auto"
if user_input in de_en:
    print(f"Übersetzung von {user_input}: {de_en[user_input]}")
else:
    print(f"Das Wort {user_input} ist nicht im Wörterbuch")


# Ein Dict erstellen aus Element => Länge des Elements
values = ["asdfa", "fdb", "cd"]
d = {}
for value in values:
    # d[asdfa] = len(asdfa)
    d[value] = len(value)
