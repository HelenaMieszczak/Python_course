# Stwórz moduł, który będzie przechowywał funkcję obliczającą bmi.py. Zaimportuj module do pliku fitmeter.py.
# Nowy plik będzie informował użytkownika o jego aktualnym BMI i na podstawie wyniku
# niedowaga, nadwaga, otyłość) sugerował zmiany w stylu życia pobierane z odpowiedniego pliku.

def niedowaga(BMI):
    if BMI <= 18.4:
        return True
    else:
        return False


def waga_w_normie(BMI):
    if BMI > 18.4 and BMI <= 24.99:
        return True
    else:
        return False


def nadwaga(BMI):
    if BMI > 24.99 and BMI <= 30:
        return True
    else:
        return False


def otylosc(BMI):
    if BMI > 24.99 and BMI <= 30:
        return True
    else:
        return False


def count_bmi(weight, height):
    BMI = round(weight / (height ** 2), 2)
    return BMI


def main():
    weight = float(input("Podaj wagę (kg): "))
    height = float(input("Podaj wzrost (m): "))
    BMI = count_bmi(weight, height)
    print("Twoje BMI wynosi: ", BMI)



if __name__ == "__main__":
    main()
else:
    print('Plik zaimportowano jako moduł')

