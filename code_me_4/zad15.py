# Słowniki dla 10 krajów Europy utwórz listy 10 najpopularniejszych imion żeńskich. \
# Za każdym razem zapisz imiona w wersji anglojęzycznej. Dodaj wszystki listy razem. Nowa lista powinna zawierać 100 elementów.
# Wyświetl tylko te imiona, które wystąpiły conajmniej w 3 krajach.

england = ["Olivia", "Amelie", "Isla", "Ava", "Emily", "Isabella", "Mia", "Poppy", "Ella", "Lily"]
france = ["Louise", "Alice", "Chloe", "Emma", "Ines", "Sarah", "Jeanne", "Anna", "Adele", "Juliette"]
germany = ["Mia", "Emma", "Sophie", "Hannah", "Emilia", "Anna", "Marie", "Lena", "Amelie", "Lily"]
poland = ["Julia", "Susan", "Sophie", "Lena", "Maya", "Hannah", "Amelie", "Alice", "Mary", "Alexandra"]
spain = ["Lucia", "Mary", "Paula", "Daniela", "Martina", "Sarah", "Sophie", "Carla", "Alba", "Julia"]
portugal = ["Mary", "Leonor", "Matilde", "Beatrice", "Caroline", "Marina", "Anna", "Sophie", "Ines", "Margarida"]
italy = ["Sophie", "Juilia", "Aurora", "Martina", "Emma", "Greta", "Chiara", "Sarah", "Alice", "Anna"]
greece = ["Mary", "Cathrine", "Anastacia", "Anna", "Christine", "Mary", "Georgia", "Helen", "Alexandra", "Irene"]
denmark = ["Emma", "Sophie", "Ida", "Freja", "Clara", "Laura", "Anna", "Ella", "Isabella", "Karla"]
austria = ["Anna", "Sarah", "Lena", "Hannah", "Leonie", "Julia", "Sophie", "Laura", "Mary", "Lea"]

all_names = england + france + germany + poland + spain + portugal + italy + greece + denmark + austria
# print(all_names)
a_new = {}
for i in all_names:
    if i in a_new:
        a_new[i] += 1
    else:
        a_new[i] = 1

for k, v in a_new.items():
    if v > 3:
        print(k, ":", v)

