
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


def calulate_bmi():
    weight = float(input("Podaj wagę (kg): "))
    height = float(input("Podaj wzrost (m): "))
    BMI = count_bmi(weight, height)
    print("Twoje BMI wynosi: ", BMI)




