# Utwórz zmienną przechowującą dowolny ciąg znaków. Sprawdź czy string jest dłuższy od 5 oraz czy zawiera literę a.\
# Jeśli zawiera, wszystkie litery a podmień na z.

word = input("Podaj dowolne słowo: ")

if len(word) <= 5 and "a" not in word:
    print("Podane słowo ma mniej niż 5 znaków oraz nie zawiera 'a'.")
elif len(word) <= 5 and "a" in word:
    print(word.replace("a","z"))
else:
    print("Podane słowo ma więcej niz 5 znaków.")
    print(word.replace("a", "z"))