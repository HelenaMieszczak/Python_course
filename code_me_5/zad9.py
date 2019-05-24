# Napisz grę ciepło - zimno tak, aby korzystać z funkcji.

import random


def users_win():
    if users_num == comp_num:
        return True
    else:
        return False


def comp_win():
    if (counter == 6) and (comp_num != users_num):
        return True
    else:
        return False



comp_num = (random.randint(1,100))
users_num = int(input("Podaj swoją liczbę: "))
counter = 1

while comp_num != users_num:
    if users_num > comp_num:
        print("ciepło")
    elif users_num < comp_num:
         print("zimno")
    users_num = int(input("Podaj swoją liczbę: "))
    counter += 1



if comp_win():
    print("Przegrana :(")
else:
    print("Gratulacje")

