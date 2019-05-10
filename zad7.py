# coding=utf-8
# Zadanie 7
# Napisz konwerter walut.
# Program poprosi użytkownika o kwotę pieniędzy, jaką wezmą na wakacje
# a następnie przeliczy tę kwotę w euro oraz w dolarach.
# Zignoruj wszelkie centy, które mogą wyniknąć z konwersji.
# Wejście i wyjście powinny być zrozumiałe dla użytkownika.


EUR = 4.29
USD = 3.82

print("Jaką kwotę (PLN) planujesz zabrać ze sobą na wakacje?")
amount_of_money = int(input())

PLN_to_EUR = amount_of_money // EUR
PLN_to_USD = amount_of_money // USD

print("Podana przez Ciebie kwota w przeliczeniu na euro wynosi", PLN_to_EUR, "a na dolary", PLN_to_USD)