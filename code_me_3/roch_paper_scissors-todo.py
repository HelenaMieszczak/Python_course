#  Napisz grę - kamień (k) / papier (p) / nożyce (n).
# Użytkownik podaje jedną z 3 figur.
# Komputer losuje jedną z 3 figur.
# Sprawdź kto wygrał tę rundę.
# Zmień kod tak, by użytkownik mógł podac liczbę rund.
# Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.
# Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’

import random

rounds = int(input("Podaj liczbę rund: "))
list1 = ["paper", "scissors", "rock"]
comp_choice = random.choices(list1, k=1)
users_choice = input("Scissors, rock or paper?")
print(comp_choice)

comp_wins = []
user_wins = []

if comp_choice == users_choice:
    print("Draw!")
elif ((comp_choice == "scissors" and users_choice == "paper") \
    or (comp_choice == "paper" and users_choice == "rock") \
    or (comp_choice == "rock" and users_choice == "scissors")):
    print("You lost")
else:
    print("You win")







