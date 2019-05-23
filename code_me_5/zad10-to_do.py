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

marka = input("Podaj markę auta: ")
model = input("Podaj model auta:")
rocznik = int(input("Podaj rocznik: "))

def car_dict():
    car = {}
    car[marka] = marka
    car[model] = model
    car[rocznik] = rocznik
    return car

cars = car_dict()


