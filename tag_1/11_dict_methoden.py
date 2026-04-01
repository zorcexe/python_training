"""
Dict Methoden
"""

populations = {
    "Berlin": 3748148,
    "Hamburg": 1822445,
    "München": 1471508,
    "Cologne": 1085664,
    "Frankfurt": 753056,
}

# Einwohnerzahl von Berlin
print(f"Einwohnerzahl von Berlin: {populations["Berlin"]}")
print(f"Einwohnerzahl von Berlin: {populations.get("Berlin")}")


# Iteration über ein Dict
for p in populations:
    print(p)

print("*" * 40)

# Iteration über Key-Value

for city, population in populations.items():
    print(f"{city} hat {population} Einwohner")


# dict.items() liefert eine Liste von Tupeln (Key, Value), die dann ad-hoc entpackt werden
# print(populations.items())
# values = [
#     ("Berlin", 3748148),
#     ("Hamburg", 1822445),
#     ("München", 1471508),
#     ("Cologne", 1085664),
#     ("Frankfurt", 753056),
# ]
