#  Napisz grę - kamień (k) / papier (p) / nożyce (n).
# Użytkownik podaje jedną z 3 figur.
# Komputer losuje jedną z 3 figur.
# Sprawdź kto wygrał tę rundę.
# Zmień kod tak, by użytkownik mógł podac liczbę rund.
# Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.
# Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’

import random

counter = 0
comp_wins = 0
user_wins = 0
rounds = int(input("Enter the number of rounds: "))


while counter != rounds:
    list1 = ["paper", "scissors", "rock"]
    comp_choice = list1[random.randint(0, 2)]
    print("\n")
    users_choice = input("Scissors, rock or paper?: ")
    print(comp_choice)
    if comp_choice == users_choice:
        print("Draw!")
        comp_wins += 1
        user_wins += 1
        counter += 1
    elif users_choice == "scissors":
        if comp_choice == "paper":
            print("You win", users_choice, "cuts", comp_choice, "!")
            user_wins += 1
        elif comp_choice == "rock":
            print("You lose :(", comp_choice, "smashes", users_choice)
            comp_wins += 1
        counter += 1
    elif users_choice == "paper":
        if comp_choice == "rock":
            print("You win", users_choice, "covers", comp_choice, "!")
            user_wins += 1
        elif comp_choice == "scissors":
            print("You lose :(", comp_choice, "cuts", users_choice)
            comp_wins += 1
        counter += 1
    elif users_choice == "rock":
        if comp_choice == "scissors":
            print("You win", users_choice, "smashes", comp_choice, "!")
            user_wins += 1
        elif comp_choice == "paper":
            print("You lose :(", comp_choice, "covers", users_choice)
            comp_wins += 1
        counter += 1
    else:
        print("Choose your type again")


    print("Computer score: ", comp_wins)
    print("Your score: ", user_wins)

print("\n",)
print("--------------")
if user_wins > comp_wins:
    print("***Congrats!***")
elif user_wins < comp_wins:
    print("***Computer wins!***")
else:
    print("***Draw!***")









