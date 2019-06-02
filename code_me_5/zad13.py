# Stwórz grę wisielec “bez wisielca”.
# Komputer losuje wyraz z dostępnej w programie listy wyrazów.
# Wyświetla zamaskowany wyraz z widoczną liczbą znaków (np. ‘- - - - - - -‘)
# Użykownik podaje literę.
# Sprawdź, czy litera istnieje w wyrazie. Jeśli tak, wyświetl mu komunikat:
# “Trafione!” oraz napis ze znanymi literami.
# W przeciwnym wpadku pokaż komunikat:
# “Nie trafione, spróbuj jeszcze raz!”.
# Możesz ograniczyć liczbę prób do np. 10.

import random


def get_word():
    hidden_words = ["abrakadabra", "flowers", "kettle", "morning", "chair"]
    return random.choice(hidden_words).upper()


def check_the_letters(word, guesses, guess):
    guess = guess.upper()
    status = ""
    matches = 0
    for letter in word:
        if letter in guesses:
            status += letter
        else:
            status += "?"

        if letter == guess:
            matches += 1

    if matches >= 1:
        print(f"Yes! The word contains the letter {guess}")
    else:
        print(f"Sorry. The word does not contain the letter {guess}")

    return status


def main():
    word = get_word()
    guesses = []
    guessed = False
    print(f"The word contains {len(word)} letters")
    while not guessed:
        guess = input("Please enter the letter: ")
        guess = guess.upper()
        if guess in guesses:
            print("You already guessed this one.")
        elif len(guess) == 1:
            guesses.append(guess)
            result = check_the_letters(word, guesses, guess)
            if result == word:
                guessed = True
            else:
                print(result)
        elif len(guess) == len(word):
            guesses.append(guess)
            if guess == word:
                guessed = True
            else:
                print("Sorry, that is incorrect")
        else:
            print("Type again")

    print(f"Yes, you guessed the hidden word! You got it in {len(guesses)} tries.")


main()
