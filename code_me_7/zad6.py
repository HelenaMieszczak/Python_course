# Rozpoznawanie kart.Utwórz plik zawierający numery kart kredytowych. Sprawdź, podziel kart do plików wg typów
# np. visa.txt, mastercard.txt, americanexpress.txt.


def is_visa(number):
    if len_of_number not in [13, 16]:
        return False
    else:
        if number[0] == "4":
            return True
        else:
            return False


def is_mastercard(number):
    if len_of_number != 16:
        return False
    else:
        if int(number[:2]) >= 51 and int(number[:2]) <= 55:
            return True
        elif int(number[:4]) >= 2221 and int(number[:4]) <= 2720:
            return True
        else:
            return False


def is_american_express(number):
    if len_of_number != 15:
        return False
    else:
        if number[:2] == "34" or number[:2] == "37":
            return True
        else:
            return False


def save_to_file(card_type, number):
    save_file = card_type + "txt"
    with open(save_file, "a") as sf:
        sf.write(number + "\n")


def check_card_type(number):
    if is_visa(number):
        print("To visa.")
        save_to_file("visa", number)
    elif is_mastercard(number):
        print("To mastercard.")
        save_to_file("mastercard", number)
    elif is_american_express(number):
        print("To americanexpress.")
        save_to_file("americanexpress", number)
    else:
        print("Nie znam Twojej karty.")


# number = input("Podaj numer karty: ")
filename = "card_num.txt"

with open(filename, 'r') as fopen:
    num_list = fopen.readlines()

print(num_list)

len_of_number = 0
for num in num_list:
    num = num.replace("\n", "")
    len_of_number = len(num)
    if len_of_number not in [13, 15, 16]:
        print("Błędny numer.", num)
        continue
    check_card_type(num)


