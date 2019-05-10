# Zadanie 5
# Napisz program, który pyta użytkownika o 2 liczby
# a następnie dzieli jedna przez drugą.
# Pokaż ile razy pierwsza liczba mieści się w drugiej
# oraz jaka jest reszta tego dzielenia. 

print("Podaj 2 liczby całkowite. Poniżej wynik dzielenia tych liczb.")

number1 = int(input("A = "))
number2 = int(input("B = "))

print("Wynik dzielenia liczby A przez B jest równy:", number1 / number2)
print("Liczba A mieści sie w B:", number1 // number2, "raz(y)")
print("Reszta z dzielenia liczby A przez B wynosi:", number1 % number2)