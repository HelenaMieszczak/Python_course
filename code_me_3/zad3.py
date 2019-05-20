#Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce. Oblicz średnią opinię o książce. W zależności \
# od wyniku dodaj komunikaty. Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry, ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi.

story = int(input("Podaj ocenę pod względem fabuły (1-10): "))
character = int(input("Jak oceniasz bohaterów (1-10): "))
style = int(input("Podaj ocenę języka książki (1-10): "))

average = round((story + character + style) / 3, 2)

if average >7:
    print("Bardzo dobra ksiązka", average)
elif average >= 4:
    print("Ksiązka jest przeciętna", average)
else:
    print("Ksiązka niewarta uwagi", average)
