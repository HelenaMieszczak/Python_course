# Stwórz moduł, który będzie przechowywał funkcję obliczającą bmi.py. Zaimportuj module do pliku fitmeter.py.
# Nowy plik będzie informował użytkownika o jego aktualnym BMI i na podstawie wyniku
# niedowaga, nadwaga, otyłość) sugerował zmiany w stylu życia pobierane z odpowiedniego pliku.

import bmi

wh = float(input("Podaj wagę (kg): "))
ht = float(input("Podaj wzrost (m): "))
BMI = bmi.count_bmi(wh, ht)
print("Twoje BMI wynosi: ", BMI)

with open("bmi_adv.txt", "r", encoding='utf-8') as fp:
    cont = fp.readlines()
    if bmi.niedowaga(BMI):
        info = cont[0]
        print(info)
    elif bmi.waga_w_normie(BMI):
        info1 = cont[1]
        print(info1)
    elif bmi.nadwaga(BMI):
        info2 = cont[2]
        print(info2)
    else:
        info3 = cont[3]
        print(info3)


