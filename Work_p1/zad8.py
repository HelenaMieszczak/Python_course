# coding=utf-8
# Zadanie 8
#Ulepsz program z zadania 7, tak aby zwrócił ile banknotów
# 50, 20, 10 i 5 euro otrzyma użytkownik.

EUR = 4.29

print("Jaka kwotę (PLN) planujesz zabrać ze sobą na wakacje?")

amount_of_money = int(input())

PLN_to_EUR = amount_of_money // EUR

print(amount_of_money, "zł w przeliczeniu na euro wyniesie", PLN_to_EUR, "euro.")

value_50 = PLN_to_EUR // 50
value_20 = (PLN_to_EUR - value_50 * 50) // 20
value_10 = (PLN_to_EUR - (value_50 * 50 + value_20 * 20)) // 10
value_5 = (PLN_to_EUR - (value_50 * 50 + value_20 * 20 + value_10 * 10)) //5

print("Po wymianie otrzymasz", value_50, "banknotów(-ty) o nominale 50 euro,", value_20, "o nominale 20 euro,", \
      value_10, "o nominale 10 euro oraz", value_5, " o wartości 5 euro." )
