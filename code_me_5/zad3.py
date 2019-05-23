# Napisać funkcję, która przyjmuje listę liczb i zwraca sumę wszystki elementów na liście.

def sumowanie(lista):
    return sum(lista)


list_num = input("Podaj dowolne liczby: ")
list_num = list_num.split()
print(list_num)


list_int = []
for i in list_num:
    list_int.append(int(i))

print(sumowanie(list_int))
