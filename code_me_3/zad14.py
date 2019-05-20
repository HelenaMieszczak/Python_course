# Sortowanie. Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych. \
# Znajdź największą liczbę. Wyświetl liczby od największej do najmniejszej.

num1 = int(input("Podaj 1. liczbę: "))
num2 = int(input("Podaj 2. liczbę: "))
num3 = int(input("Podaj 3. liczbę: "))

list = []
list.append(num1)
list.append(num2)
list.append(num3)
list.sort()
print(list[::-1])
print("Największa podana przez Ciebie liczba to: ", max(list))

print(4.445 * 10 ** 8)
