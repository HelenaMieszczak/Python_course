# Zadanie 6
# Zarówno lodówka, jak i winda mają wysokość, szerokość i głębokość. 
# Dowiedz się, ile miejsca pozostało w windzie, gdy lodówka jest w środku.
# Załóżmy, że wymiary lodówki zawsze będą mniejsze niż windy ( jest to prawdopodobne?)
# Wejście i wyjście powinny być zrozumiałe dla użytkownika.

print("Chcesz wwieźć lodówkę na 4 piętro. Podaj wymiary lodówki i windy, żeby sprawdzić czy się zmieści.")

print("Wymiary lodówki:")
height_of_refrigerator = float(input("Wysokośc lodówki (m):"))
width_of_refrigerator = float(input("Szerokość lodówki(m):"))
depth_of_refrigerator = float(input("Głębokośc lodówki (m):"))

print("Wymiary windy:")
height_of_elevator = float(input("Wysokośc windy (m):"))
width_of_elevator = float(input("Szerokość windy(m):"))
depth_of_elevator = float(input("Głębokośc windy (m):"))

free_space = (height_of_elevator * width_of_elevator * depth_of_elevator) - (height_of_refrigerator * width_of_refrigerator * depth_of_refrigerator)

print("W windzie pozostanie jeszcze", free_space, "m3 wolnego miejsca")