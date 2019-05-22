#  Nie korzystając z funkcji wbudowanej max(), napisz funkcję znajdującą maksymalną wartość z 3 liczb. maximum_of(a, b, c).

def max_of_2(x, y):
    # if x > y:
    #     return x
    # else:
    #     return y
    return x if x > y else y

def maximum_of(num1, num2, num3):
    return max_of_2(max_of_2(num1, num2), num3)

a = int(input("Podaj 1 l:"))
b = int(input("Podaj 1 l:"))
c = int(input("Podaj 1 l:"))

wieksza = maximum_of(a, b, c)
print("Największa podana liczba", wieksza)



