# Dla podanej przez użytkownika liście liczb całkowitych sprawdź czy pierwszy i ostatni element są takie same.

numbers = []

for num in range(5):
    n = int(input("Podaj dowolną liczbę: "))
    numbers.append(n)

if numbers[0] == numbers[-1]:
    print("Perwsza i ostatnia podana liczba są takie same.")
else:
    print("Pierwsza i ostania podana liczba NIE są takie same.")