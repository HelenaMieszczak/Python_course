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