#Stwórz zmienną password. Hasło powinno składać z liter i cyfr, \
# zwierać conajmniej 1 dużą literę i mieć długość conajmniej 8 znaków.

password = input("Podaj hasło (musi zawierać co najmniej 8 znaków - litery oraz cyfry i 1 dużą literę): ")

correct_len = len(password) > 7
alfa_num = password.isalnum()
not_all_letters = not password.isalpha()
not_all_digits = not password.isdigit()
correct_alnum = alfa_num and not_all_digits and not_all_letters
one_upper = not password.islower() and not password.isupper()

if correct_len and correct_alnum and one_upper:
    print("Hasło jest ok")
else:
    print("Podaj hasło ponownie")

