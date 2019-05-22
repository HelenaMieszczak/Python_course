# Pobierz od użytkownika parzystą listę elementów. Sprawdź czy 2 środkowe elementy są takie same

element = []

for i in range(6):
    e = input("Podaj dowolne słowa: ")
    element.append(e)

print(element)

mid_element = len(element) // 2

if element[mid_element] == element[mid_element - 1]:
    print("2 srodkowe elementy są takie same")
else:
    print("2 środkowe elementy nie są takie same")