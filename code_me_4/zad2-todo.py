#Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.


numbers = []


for num in range(10):
    n = int(input("Podaj dowolną liczbę: "))
    if n in numbers:
        n % 2 == 0
        numbers.append(n)
        print(numbers)


