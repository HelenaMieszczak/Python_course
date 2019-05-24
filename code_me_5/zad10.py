# Napisz program, który będzie sprawdzał, czy nasz samochód kwalifikuje się do zarejestrowania jako zabytek.
# Program zacznie ze stworzonym słownikiem o trzech kluczach:
# marka (str)
# model (str)
# rocznik (int)
# Wypisze ten słownik na ekran (bez żadnego formatowania)
# Sprawdzi, czy samochód ma minimum 25 lat. Jeśli tak, wypisze komunikat:
# “Gratulacje! Twój samochód (tutaj_marka) może być zarejestrowany jako zabytek.”
# Jeśli nie spełnia powyższego warunku, wypisze komunikat:
# “Twój samochód (tutaj_marka) jest jeszcze zbyt młody.”
# Gdy program będzie poprawnie działał, pozmieniaj wartości słownika (ale nie klucze!), aby zobaczyć, czy progam również zmienia swoje zachowanie.


def create_car():
    car = {}
    car["marka"] = brand
    car["model"] = type
    car["rocznik"] = year
    return car


brand = input("Podaj markę auta: ")
type = input("Podaj model auta: ")
year = int(input("Podaj rocznik: "))

cars_dict = create_car()

print(cars_dict)

if 2019 - year > 25:
    print("Gratulacje! Twój samochod", brand, "możę być zarejestrowany jako zabytek.")
else:
    print("Twoj samochód", brand, "jest jeszcze zbyt młody." )