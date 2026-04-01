"""
Die Slice-Notation für Strings und alle anderen Sequenzen
string: TestString
# [<first element to include> : <first element to exclude> : <step> ]

a[start:stop]  # beginnt bei Start und endet bei Stop - 1
a[start:]      # beginnt bei Start und nimmt den Rest
a[:stop]       # beginnt bei 0 und endet bei Stop - 1
a[:]           # kopiert ganzen String

"""

string = "Test_xxxxstring"
print("string[0:3]:", string[0:3])
print("string[5:]", string[5:])

# Alles rausschneiden bis auf das letzte Zeichen
print("string[:]", string[:-1])
