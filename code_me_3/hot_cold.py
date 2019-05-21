# Stwórz grę ciepło zimno.
#Komputer losuje liczbę z zakresu od 1 do 100.
#Użytkownik podaje swój traf.
#Komuter odpowiada ciepło zimno, ale nie więcej niż 6 razy.
#Jeśli użytkownik zgadnie wygrywa gracz.
#Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer.

import random

comp_num = (random.randint(1,100))


users_num = int(input("Podaj swoją liczbę (1 - 100): "))
counter = 1
# jeśli podana liczba będzie za wysoko - program wyświetli napis "ciepło", jeśli za niska = "zimno".

while comp_num != users_num:
    if counter == 6:
        print("PRZEGRANA :(")
        break
    elif users_num > comp_num:
        print("ciepło")
    elif users_num < comp_num:
        print("zimno")
    users_num = int(input("Podaj swoją liczbę: "))
    counter += 1
else:
    print("GRATULACJE!!!")




