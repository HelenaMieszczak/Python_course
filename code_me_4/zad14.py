# Usuń duplikat z podanej list i utwórz na jej bazie krotkę. Znajdź minimalną i maksymalną liczbę w krotce.
#
# >>>  example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 9]


example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 9]

new_list = []

for i in example_list:
    if i not in new_list:
        new_list.append(i)

print(new_list)

new_tuple = tuple(new_list)
print(new_tuple)
print(max(new_tuple))
print(min(new_tuple))