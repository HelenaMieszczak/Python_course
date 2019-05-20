# Utwórz dowolną tablicę n x n zawierającą dowolny znak, a\
# następnie wyświetl jej elementy w formie tabeli n x n. Elementy powinny być oddzielone spacją

# tab = [
#     ['-', '-', '-']
#   ['-', '-', '-'],
#   ['-', '-', '-']
# ]
# n = 3
#
# for i in range(3):


sign = (input("Wpisz jakikowliek znak:"))
tab = [[sign] * 3] * 3
for i in tab:
    print(" ".join(i))
