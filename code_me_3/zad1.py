# 1. Sprawdź czy liczba podana przez użytkownika jest podzielna przez 3 bez reszty.

num = int(input("Podaj liczbę: "))

b = num % 3
if b == 0:
    print("Liczba podana przez Ciebie jest podzielna przez 3.")
else:
    print("Liczba przez Ciebie podana NIE jest podzielna przez 3.")
