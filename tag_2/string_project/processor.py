"""
Modul processor: Stellt Funktionen zum Verarbeiten
von Transkationen zur Verfügung.
"""

print("Modulname von processor.py", __name__)


def string_processor(transactions: list[str]) -> dict[str, float]:
    """
    Verarbeite kommaseparierte Transkationsliste.

    Format der einzelnen Transaktionen:
    Tranksationsnummer, Wert, Kundennummer

    Return:
        die nach Kundennummer summierten Werte {kunde1: 399, kunde2: 343},
    """
    result = {}
    for t in transactions:
        line = t.split(",")[1:]
        value = float(line[0].strip())  # 34.3
        customer_id = line[1].strip()  # Leerzeichen
        # für jede Tranksation, einen Key im Dict anlegen
        if customer_id in result:
            result[customer_id] = result[customer_id] + value
        else:
            result[customer_id] = value

    return result


if __name__ == "__main__":
    # wenn ich processor.py direkt aufrufe (zb. zum Entwickeln)
    # dann wird der folgende Code ausgeführt:

    # die folgenden Zeilen sind zum Entwickeln und Testen meines stringprocessord
    # und nicht für den produktiven Einsatz gedacht
    transactions_tests = [
        "TX1010, 670.00, KND007",
        "TX1001, 249.99, KND001",
    ]

    customer_values = string_processor(transactions=transactions_tests)
    print(customer_values)
