# Utworz tabliczkę mnożenia jako zagnieżdżoną listę o rozmiarze 10 x 10, wypełnioną wynikami mnożenia wiersz × kolumna.

#
# for i in range(1, 11):
#     line = str(i)
#     for n in range(1, 11):
#         line += "\t " + str(i * n)
#     print(line)

# sign = (input("Wpisz jakikowliek znak:"))
# tab = [[sign] * 3] * 3
# for i in tab:
#     print(" ".join(i))

# tab = [[i] * x] * y
#
# for i in range(1,11):
#     line = i
#     line += 1
#         for


row = 4
col = 5
tab_1 = [['*'] * col] * row
print(tab_1)

tab_2 = []

for r in range(row):
    current_row = []
    for c in range(col):
        current_row.append('*')
    tab_2.append(current_row)

print(tab_2)

print(tab_1 == tab_2)
