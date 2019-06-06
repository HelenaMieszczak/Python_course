#  W kodzie BMI ufamy, że użytkownik podaje wartość w kilogramach lub w metrach i rzutujemy do float.
#  Co jeśli użytkownik poda wartość 60 kg ? Zmodyfikuj kod z ostatnich zajęć tak, aby wykluczyć powyższy przypadek.

import bmi5


def get_user_input():
    try:
        wh = float(input("Podaj wagę (kg): "))
        ht = float(input("Podaj wzrost (m): "))
        print("Twoje dane to:", wh, ht)
        return True, (wh, ht)
    except(TypeError, ValueError, ZeroDivisionError):
        if TypeError:
            print("Podaj wartość liczbowa")
        elif ZeroDivisionError:
            print("Żadna z wartości nie może być zerem")
        elif ValueError:
            print("Podaj wartość liczbową.")
        else:
            print("NIezany bład")

        return False, ()


def bmi_cal(wh, ht):
    BMI = bmi5.count_bmi(wh, ht)
    print("Twoje BMI wynosi: ", BMI)
    return BMI


def advice(BMI):
    with open("bmi_adv5.txt", "r", encoding='utf-8') as fp:
        cont = fp.readlines()
        if bmi5.niedowaga(BMI):
            info = cont[0]
            print(info)
        elif bmi5.waga_w_normie(BMI):
            info1 = cont[1]
            print(info1)
        elif bmi5.nadwaga(BMI):
            info2 = cont[2]
            print(info2)
        else:
            info3 = cont[3]
            print(info3)


def main():
    status = False
    user_data = ()
    while not status:
        status, user_data = get_user_input()

    BMI = bmi_cal(*user_data)
    advice(BMI)


if __name__ == "__main__":
    main()