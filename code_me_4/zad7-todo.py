# Napisz skrypt, który podaną listę podzieli na 3 równe listy i odwraca każdą z tych.
# input: [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
# output:
# [4, 3, 2, 1]
# [14, 13, 12, 11]
# [24, 23, 22, 21]
#
numbers = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
new_numbers = []

for i in range(0, len(numbers) +1):
    new_numbers.append(numbers[i : i + 4])
    print(new_numbers)
# tablica = ['1234567890']
# tablica2 =[]
# for x in range(len(tablica[0])/2):
#    tablica2.append(tablica[0][x*2:x*2+2])
# tablica = [1234567890]
# tablica_str = ' '.join(str(tablica[0])).split(' ')
# tablica_int = []
#
# for x in range(len(tablica_str) / 2):
#     tablica_int.append(int(''.join(tablica_str[x * 2:x * 2 + 2])))
#
# print
# tablica_int
# d = 11121314151617181910
# d = str(d)
# r = []
# for c in range (0, len (d) -1, 2):
# 	r.append (d[c:c+2])