# Utwórz 2 krotki. Następnie utwórz listę będącą połączeniem elementów o \
# parzystym indeksie z pierwszej krotki, a oraz nieparzystych elementów z drugiej.

my_tuple1 = (1, 2, 3, 4, 5)
my_tuple2 = (11, 12, 13, 14, 15)

# tmp_list1 = list(my_list1)
# tmp_list2 = list(my_list2)
print(my_tuple1[::2])
print(my_tuple2[1::2])

new_tuple = my_tuple1[::2] + my_tuple2[1::2]
new_list = list(new_tuple)
print(new_list)


