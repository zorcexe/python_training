"""
Bedingte Anweisungen (if else elif)

Python als falsch interpretiert:
0 => Ganzahl 0
0.0 => Float 0.0
"" => leerer String
[] => leere Liste
() => leerer Tupel
{} => leeres Dictionary
None
Folgende Werte, die an die Funktion bool() übergeben werden, werden von
False => der boolsche Wert False

Aufgabe:
Userinput: User gibt eine Zahl ein
wir prüfen, ob die Zahl in der folgenden Menge enthalten ist

entweder im Bereich 45 - 99 (A)
oder im Bereich 0 - 15 (B)
oder außerhalb (C)

if
elif (else if)
else
"""

# boolsche Datentyp
print("bool(false)", bool("False"))

city = ""
if city:
    print("City ist true")
else:
    print("City ist nicht true")


# Logisches und (&&)
x = 3
y = 2
z = 5
if x > y and z < 4:
    print("Die Aussage ist wahr")

# Logisches Oder (||)
if x > y or z < 4:
    print("links oder rechts ist wahr")

if not city:
    print("City ist ein leerer String")


Zahl = float(input("bitte gebe eine Zahl an: "))

if (Zahl > 44) and (Zahl < 100):
    print("A")
elif (Zahl >= 0) and (Zahl <= 15):
    print("B")
else:
    print("C")


city_name = "Snake-Case"


# Membership Operator
city = "hamburg"
if "burg" in city:
    print(f"burg ist in {city} enthalten")
