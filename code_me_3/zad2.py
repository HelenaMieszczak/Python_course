# Pobierz dwie wartości int od użytkownika i oblicz ich sumę. Jeśli suma jest większa niż 100, wyświetl ich sumę.

num1 = int(input("Podaj 1. liczbę: "))
num2 = int(input("Podaj 2. liczbę: "))
sum = num1 + num2

if sum > 100:
    print(sum)