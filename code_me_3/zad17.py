# Stwórz grę ciepło zimno.
#Komputer losuje liczbę z zakresu od 1 do 100.
#Użytkownik podaje swój traf.
#Komuter odpowiada ciepło zimno, ale nie więcej niż 6 razy.
#Jeśli użytkownik zgadnie wygrywa gracz.
#Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer.

import random

comp_num = (random.randint(1,100))
print(comp_num)

users_num = int(input("Podaj swoją liczbę: "))
counter = 1

while users_num != comp_num:
    counter += 1
    if users_num > comp_num
        print("zimno")
    elif use

    users_num = int(input("Podaj swoją liczbę: "))
else:
    print("You win")

