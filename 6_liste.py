"""
Datentyp liste, ein sequentieller, veränderlicher Datentyp
https://www.w3schools.com/python/python_lists.asp
"""

values = [1.23, 2.4, 32.4]

print(f"Das erste Element {values[0]}")

# Neues Element an die Liste anhängen (Liste wird verändert)
values.append(42.2)
values[0] = 99.3

# eine Liste sortieren (key-Funktion für komplexere Sortierungen (sort, key=...))
print(values)
values.sort()  # inplace Sortierung
print(values)

# Kopieren von Variablen (unverändlicher  Datentyp)
a = 42
b = a  # hier wird der Wert kopiert
a = 45
print(f"{a=}, {b=}")

# Kopieren von Variablen (verändlicher Datentyp)
values = [1, 2, 3]
values_copy = values  # hier wurde die Referenz (Pointer) kopiert
values.append(4)
print(f"{values=}, {values_copy=}")
print(f"{id(values), id(values_copy)}")
print("Identäts-Operator:", values is values_copy)

print("*" * 40)
# um wirklich zu kopieren (flache Kopie)
values = [1, 2, 3]
values_copy = values.copy()  # hier wurden die Werte kopiert, nicht die Referenz
values.append(4)
print(f"mit copy: {values=}, {values_copy=}")
print(f"mit copy: {id(values), id(values_copy)}")
print("mit copy: Identäts-Operator:", values is values_copy)
print("*" * 40)


# Problem: wenn eine Liste an eine Funktion übergeben wird, wird nur die Referenz (Pointer)
# übergeben.
def check_value(val):
    val.append(78)


values = [1, 2, 3]
check_value(values)
print(f"Neuer Values ist {values}")
