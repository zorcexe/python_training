"""
Typehints: versuchen dsa Problem fehlender Typisierung zu beheben.

Sequence: String, Liste, Tuple
"""

from typing import Sequence


def summe(a: int, b: int) -> int:
    """Rückgabeewert int"""
    return a + b


def check_values(values: Sequence[str]) -> None:
    """Rückgabewert None"""
    for value in values:
        if "a" in value:
            print(value)


result = summe("3", "4")
print(result)

check_values(["a", "mias", "ad"])
check_values(("a", "mias", "ad"))
check_values("jaslfjsaf")
