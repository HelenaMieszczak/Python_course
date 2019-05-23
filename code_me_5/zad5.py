# Skorzystaj ze swojego kodu bmi.py. Rozbij liczenie bmi na funkcję obliczającą bmi na podstawie danych użytkownika \
# oraz zwracającą odpowiednią wartość (niedowaga, waga normalna, nadwaga, otyłość) w zależności od otrzymanego parametru.

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

weight = float(input("Podaj wagę (kg): "))
height = float(input("Podaj wzrost (m): "))
BMI = round(weight/(height**2),2)
print("Twoje BMI wynosi: ", BMI)

if niedowaga(BMI):
    print("Niedowaga")
elif waga_w_normie(BMI):
    print("Waga w normie")
elif nadwaga(BMI):
    print("Nadwaga")
elif otylosc(BMI):
    print("Otylosc.")
