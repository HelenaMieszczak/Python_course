#  Napisać funkcję, która wypisze wszystkie parzyste z przekazanej listy elementów (wykorzystać funkcje z pkt 2)

def even_list(numbers):
    return even_numbers


numbers = input("Podaj dowolne liczby: ")
numbers = numbers.split()


even_numbers = []
for n in numbers:
    n = int(n)
    if n % 2 == 0:
        even_numbers.append(int(n))

print(even_list(even_numbers))

