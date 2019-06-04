import random


def get_word():
    choose = input("Choose your category: \n1 - fruits \n2 - animals \n3 - European capitals ")
    chosen = False
    while not chosen:
        with open('h_words', 'r') as f:
            lines = f.readlines()
            if choose == "1":
                words = lines[0]
                words = random.choice(words.split())
                words = words.upper()
                print(words)
                chosen = True
            elif choose == "2":
                words = lines[1]
                words = random.choice(words.split())
                words = words.upper()
                print(words)
                chosen = True
            elif choose == "3":
                words = lines[2]
                words = random.choice(words.split())
                words = words.upper()
                print(words)
                chosen = True
            else:
                print("Wrong input")
                choose = input("Choose your category 1, 2 or 3 ")

    return words


def check_the_letters(word, guesses, guess):
    guess = guess.upper()
    status = ""
    matches = 0
    for letter in word:
        if letter in guesses:
            status += letter
        else:
            status += ".?."

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

    print(f"Yes, you guessed the hidden word {word}! You got it in {len(guesses)} tries.")


main()
