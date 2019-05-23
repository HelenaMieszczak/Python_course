# Nie korzystając z funkcji wbudowanej min(), napisz funkcję znajdującą minimalną wartość z 3 liczb. minimum_of(a, b, c).


def min_of_2(num1, num2):
    return num1 if num1 < num2 else num2


def minimum_of(x, y, z):
    return min_of_2(min_of_2(x, y), z)



a = int(input("Podaj 1. liczbę: "))
b = int(input("Podaj 2. liczbę: "))
c = int(input("Podaj 3. liczbę: "))

min_n = minimum_of(a, b, c)
print("Najmniejsza z podanych liczb to: ", min_n)