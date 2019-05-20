# Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem \
# np.jako jeden string rozdzielonych przecinkiem lub białym znakiem). Następnie powitaj każdą osobę na liście.



names = input("Podaj imiona: ")
lista = names.split()
for i in lista:
    print("Hello,", i)