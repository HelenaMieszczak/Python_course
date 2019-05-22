#  Utwórz “na sztywno” 2-wymiarową tablicę, tak, by kolejne wiersze \
#  zawierały dane osób, natomiast w kolumnach będzie znajdować się imię, nazwisko, zawód, np:
# Dorota, Wellman, dziennikarka
# Adam, Małysz, sportowiec
# Robert, Lewandowski, piłkarz
# Krystyna, Janda, aktorka
# Wyświetl w sposób przyjazny dla użytkownika

# names = [
#     ["Dorota", "Wellman", "dziennikarka"],
#     ["Adam", "Małysz", "sportowiec"],
#     ["Robert", "Lewandowski", "piłkarz"],
#     ["Krystyna", "Janda", "aktorka"],
# ]



people = []

for i in range(3):
    name = input("Podaj imię: ")
    surname = input("Podaj nazwisko: ")
    job = input("Podaj zawód: ")
    people.append([name, surname, job])

#print(people)


for n in people:
    print("\t".join(n))
