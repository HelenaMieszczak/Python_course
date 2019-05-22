# Napisać funkcję, która oblicza pole koła na podstawie zadanego promienia.

def kolo():
    r = int(input("Podaj promnień: "))
    kolo = (3.14 * (r ** 2))
    print("Pole koła wynosi", kolo)

kolo()