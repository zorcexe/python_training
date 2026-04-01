"""
Datentyp String
"""

string = "Spam"  # doppelte Anführugzeichen sind Standard, einfache aber möglich

print("letztes Element:", string[-1])  # m

# User-Eingabe (input()) => liefert immer einen String!
# size = input("Bitte gebe deine Größe in cm an: ")  # input liefert immer String
# print("Größe in cm:", int(size), size)


#         Gewicht (kg)
# BMI = ---------------
#        Größe (m) * Größe (m)

weight = int(input("Bitte Gewicht in kg:"))
size = float(input("Körpergröße in m (1.43)"))

bmi = weight / size**2
print("Der BMI ist:", round(bmi, 2))

# Länge eines Strings (allg. einer Sequenz)
print("Länge eines Strings", len("Bob"))
