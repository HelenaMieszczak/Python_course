#Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.

#
# numbers = []
#
#
# for n in range(10):
#     n = int(input("Podaj dowolną liczbę: "))
#
#     if n % 2 == 1:
#         numbers.append(n)
#
# print(numbers)

#

liczby = input("Podaj 10 liczb: ")
liczby = liczby.split()

odd_numbers = []
for n in range(10):
    n = int(n)
    if n % 2 == 1:
        odd_numbers.append(int(n))

print(odd_numbers)
