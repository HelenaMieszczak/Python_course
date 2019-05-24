# Napisz program, który na podstawie numeru karty odpowie czy ma doczynienia z Visą, MasterCard, a może AmericanExpress.
# Co wiemy o tych numerach tych kart?
# All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.
# MasterCard numbers either start with the numbers 51 through 55 or with the numbers 2221 through 2720. All have 16 digits.
# American Express card numbers start with 34 or 37 and have 15 digits.


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
        if number[:2] == "34" or number[:2] == 37:
            return True
        else:
            return False



number = input("Podaj numer karty: ")

len_of_number = len(number)

if len_of_number not in [13,15,16]:
    print("Błędny numer.")
if is_visa(number):
    print("To visa.")
elif is_mastercard(number):
    print("To mastercard.")
elif is_american_express(number):
    print("To americanexpres.")
else:
    print("Nie znam Twojej karty.")