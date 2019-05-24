# Kolejnym warunkiem, aby dostać “żółte tablice”, jest to, aby samochód posiadał co najmniej 75% oryginalnych
# części.\ W naszym zadaniu zakładamy, że rzeczoznawca określił jego oryginalność w kategorii tak/nie. Poniżej
# stworzenia i wyświetlenia słownika w zadaniu powyżej: dopisz do słownika nowy klucz czy_oryginalny i ustaw jego
# wartość (typ: bool) wedle uznania. ponownie wyświetl zmieniony słownik Zmodyfikuj program tak, aby uwzględnił
# decyzję o możliwości zarejestrowania samochodu również od jego oryginalności. Dopisz odpowiednie komunikaty.

def create_car():
    car = {}
    car["marka"] = brand
    car["model"] = type
    car["rocznik"] = year
    car["czy_oryginalny"] = original

    return car


brand = input("Podaj markę auta: ")
type = input("Podaj model auta: ")
year = int(input("Podaj rocznik: "))
original = True

cars_dict = create_car()

print(cars_dict)


if (2019 - year > 25) and original:
    print("Gratulacje! Twój samochod", brand, "możę być zarejestrowany jako zabytek.")
else:
    print("Twoj samochód", brand, "jest jeszcze zbyt młody." )