"""
Einführung in OOP

Klassen erben immer von einer Klasse object (Mutterklasse)
der Konstruktor in python ist in die Methoden
__new__() => Objekterzeuger und
__init__() => Objektinitialisierer

aufgeteilt. In der Regel nutzt man nur __init__
in __init__() werden die Parameter definiert, mit denen die Instanz initialisiert
werden soll.

Non-Public Methoden und Attribute werden mit _ gepräfixt.
"""

# Python Konvention: Konstanten groß schreiben (sind aber auch nur Variablen)
EXPORT_DIRECTORY = "/etc/home"


class Customer:
    def __init__(self, number: str, total_value: float) -> None:
        # print(f"id von {self=}")
        self.number = number
        self.total_value = total_value
        self._initialize_database()

    def send_transaction_data(self) -> None:
        print("Sending data ...")

    def _initialize_database(self) -> None:
        """Non-Public Methoden und Attribute werden mit _ gepräfixt."""
        print("Private Methode zum Initialisieren der DB")

    def __str__(self) -> str:
        """Benutzerfreundliche Darstellung eines Customer-Objekts."""
        return f"{self.number} / {self.total_value}"


kunde_1 = Customer(number="X343", total_value=202.2)
# print(f"id von {kunde_1}")
print(f"Typ von {type(kunde_1)=}")

# dir() zeigt alle Attribute und Methoden eines Objekts
# ZUm Debuggen dir() und vars() nutzen
print(f"Attribute und Methoden: {dir(kunde_1)}")  # list
print("kunde 1", kunde_1)
print("Eigenschaften von kunde_1:", vars(kunde_1))  # dict

# Zugriff auf Attribute und Methoden via Dot-Notation
print("Kundennummer:", kunde_1.number)
print("Total:", kunde_1.total_value)

# Aufruf einer öffentlichen methode
kunde_1.send_transaction_data()
kunde_1._initialize_database()

print("kunde:", kunde_1)
