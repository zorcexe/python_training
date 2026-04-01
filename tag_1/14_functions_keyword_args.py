"""
positionelle vs Keyword-Argumente
"""


def connect_to_database(user, password, encoding="utf-8"):
    """Verbindung zur Datenbank herstellen."""
    print(user, password, encoding)


def export_data(*, dir, file):
    """Directory und Datei müssen per keyword-argument übergeben werden.
    (alles rechts von dem Sternchen muss kw-arg sein)
    """


# Jede Funktion ist ein Objekt und kann wie jede anderer Datentyp behandelt werden,
# zb. Übergabe an Funktionen, Rückgabe von Funktionen
print(connect_to_database.__doc__)  # Dunder-Doc

# Funktion aufrufen mit und ohne encoding (per Position)
connect_to_database("bob", "secret123", "utf-16")
connect_to_database("alice", "secret123")

# Übergabe per Keyword-Argument
connect_to_database(password="geheim", user="grumpy")

# export_data(*, dir, file)
export_data(
    file="example.jpg",
    dir="/home",
)
