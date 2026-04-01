"""
Iteration über Listen.
"""

values = [1.23, 2.4, 32.4]

# Einfache Iteration
for value in values:
    print(value)


# Schüler und Noten ausgeben
grades = [1, 2, 4, 1, 3]
students = ["Bob", "Alice", "Grumpy", "Goofy", "Donald"]

# Best Practice
for index, student in enumerate(students):
    print(f"Der Schüler {student} hat die Note {grades[index]}")

# umständlicher Weg mit manuellem Counter
i = 0
for student in students:
    print(student, grades[i])
    i += 1  # i = i + 1


#########################
# Filtern
# Aufgabe: neue liste erstellen mit Werten >= 6
#########################
values = [1, 3, 6, 8, 9, 34]
filtered_values = []

for value in values:
    if value >= 6:
        filtered_values.append(value)


print(f"Gefilterte Werte: {filtered_values}")
