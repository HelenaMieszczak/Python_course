#Oblicz koszt wyprawy znając dystans, spalanie na 100km i cenę litra benzyny. \
# Załóżmy, że spalanie na 100km wynosi 6,4 l, trasa to 120km, litr benzyny kosztuje 5,04 zł.
#Zmodyfikuj skrypt tak, by przyjmował wartości od użytkownika.

distance = float(input("Podaj długość trasy wycieczki (km): "))
price_of_gas = float(input("Podaj cenę litra benzyny: "))
gas_per_100km = float(input("Podaj spalanie (l/100km): "))

cost = distance * gas_per_100km / 100 * price_of_gas

print("Koszt benzyny będzie wynosić: ", cost)