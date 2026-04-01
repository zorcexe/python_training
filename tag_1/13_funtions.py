"""
Funktionen in Python
"""


def fn():
    """Ein Funktions-Docstring (<= 72 Zeichen sein).
    Default-Rückgabewert ist None
    """
    print("hallo, welt")


def average(values):
    """Durchschnitt der values berechnen und zurückgeben."""
    result = sum(values) / len(values)
    return result


x = fn()
print(x)

numbers = [1, 2, 3]
durchschnitt = average(numbers)
print(f"Der Durschnitt ist {durchschnitt}")
