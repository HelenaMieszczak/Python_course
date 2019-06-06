# Stwórz moduł, który przechowuje wzór na deltę. Skorzystaj z wbudowanego modułu math. W nowym pliku wykorzystaj moduł.

import delta

a = int(input("Podaj wartość a: "))
b = int(input("Podaj wartość b:"))
c = int(input("Podaj wartość c: "))


def main():
    outcome = delta.count_delta(a, b, c)
    if delta.check_delta(outcome):
        print(outcome)
    else:
        print("ujemna delta!!!!!!!!!")


if __name__ == "__main__":
    main()