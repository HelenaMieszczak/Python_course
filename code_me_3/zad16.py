# Napisz prostą grę, w której użytkownik musi zgadnąć liczbę
# od 0 - 20 ukrytą w programie (np. secret_num = 5).
# Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie.

users_num =int(input("Zgadnij liczbę (1 - 20):"))
secret_num = 10


while users_num != secret_num:
    users_num =int(input("Zgadnij liczbę (1 - 20):"))
else:
    print("Brawo!")
