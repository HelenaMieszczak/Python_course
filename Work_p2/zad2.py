# Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7 /
# i zwróć łańcuch złożony z trzech środkowych znaków danego ciągu.

txt = input("Podaj słowo (min. 7 liter, nieparzysta długość): ")
len(txt)
mid_index = len(txt) // 2

print(txt[mid_index - 1], txt[mid_index], txt[mid_index + 1])
