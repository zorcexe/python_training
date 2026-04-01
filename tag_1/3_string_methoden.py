"""
wichtige String-Methoden und Slicing (Sub-Strings)
https://www.w3schools.com/python/python_strings_methods.asp
"""

city = "Nürnberg"
print(type(city))
# Prüfen ob String eine Zahl ist
print(city.isdigit())  # False

# Übungsaufgabe
# Ersetze alle alle a mit x
# String-Methode replace(ursprung, ersetzung)
string = "ababababa"
string = string.replace("a", "x")


if city.startswith("Nü"):
    print("City ist Nürnberg")


a = "aaa"
b = "aaa"
print(a == b)  # Strings vergleichen


# Strip (String von Steuerzeichen bereinigen)
eingabe = "  34 \r\n"
print(eingabe.strip())
