# Napisać funkcję, która sprawdza czy liczba jest parzysta.

def even_number():
    number = int(input("Podaj dowolną liczbę: "))
    if number % 2 == 0:
        print("Liczba jest parzysta.")
    else:
        print("Liczba nie jest parzysta.")


even_number()