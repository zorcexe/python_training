"""
Hauptmodul (Einstiegsprogramm)
String-Projekt: Verarbeiten einer Liste von Strings.
"""

import processor
from models import Customer
import django

# from processor import string_processor

# jedes Modul hat einen Namen
# die Datei, die direkt aufgerufen wird mit python app.py
# heisst __main__
print("Modulname von app.py", __name__)

transactions = [
    "TX1010, 670.00, KND007",
    "TX1001, 249.99, KND001",
    "TX1002, 19.50, KND002",
    "TX1003, 999.00, KND003",
    "TX1004, 5.75, KND004",
    "TX1005, 120.00, KND001",
    "TX1006, 450.30, KND005",
    "TX1007, 78.20, KND002",
    "TX1008, 310.10, KND006",
    "TX1009, 15.99, KND003",
]


def create_customer_list(transaction_result: dict) -> list[Customer]:
    """Erstelle Customerliste auf Basis der Transaktion-Dictionaries."""
    customer_list: list[Customer] = []

    for key, value in transaction_result.items():
        kunde = Customer(number=key, total_value=value)
        customer_list.append(kunde)

    return customer_list


def main():
    """Einstiegsprogramm, häufig main.py genannt"""
    result: dict = processor.string_processor(transactions)
    customer_list = create_customer_list(result)
    # print(result)
    # # result = string_processor(transactions)
    # # Aufgabe: a) Customerklasse importieren, b) eine
    # # beliebige Instanz der Customerkasse bilden (mit einem Wert
    # # aus result)
    # kdn = "KND003"
    # kunde_3 = Customer(
    #     number=kdn,
    #     total_value=result[kdn],
    # )


if __name__ == "__main__":
    # Wenn
    main()
