# Napisz grę ciepło - zimno tak, aby korzystać z funkcji.

import random

comp_num = (random.randint(1,100))
users_num = int(input("Podaj swoją liczbę: "))
counter = 1

def users_win():
    if users_num == comp_num:
        return True
    else:
        return False


def comp_win():
    counter == 6 and comp_num != users_num


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