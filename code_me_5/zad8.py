#  Napisz funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika zakresie. Powinna zwrócić \
#  komunikat: “tak, liczba x znajduje się w zadanym zakresie”, “nie, liczba x jest z poza zakresu”.


def checking_num():
    if c in range(a,b):
        print("Tak, liczba", c,  "znajduje się w zadanym zakresie.")
    else:
        print("Nie, liczba", c, "jest z poza zakresu.")


a = int(input("Od: "))
b = int(input("Do: "))
c = int(input("Podaj liczbe, którą chcesz sprawdzić: "))

checking_num()

