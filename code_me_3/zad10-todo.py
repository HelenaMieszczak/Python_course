#W podanym przez użytkownika ciągu wejściowym policz wszystkie małe litery, wielkie litery, cyfry i znaki specjalne.

sentence = input("Podaj dowolne wyrażenie: ")

# sentence.islower()
# sentence.isupper()
# sentence.isdigit()
# not sentence.isalnum()

little_letters = []
big_letters = []
digits = []
other_signs = []

for i in sentence:
    if i == sentence.islower():
        little_letters.append()
    elif i == sentence.isupper():
        big_letters.append()
    elif i == sentence.isdigit():
        digits.append()
    elif i != sentence.isalnum():
         other_signs.append()
    else:
        print(sentence)

print(little_letters)
print(big_letters)
print(digits)
print(other_signs)

#
# for k, v in little_letters.items():
#     print(k, ":", v)

