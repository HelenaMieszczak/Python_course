# Utwórz plik na pulpicie zawierający listę ok. 20 cytatów. Każdy cytat powinen się znaleźć w nowej linii.
# Utwórz funkcję, która losuje i wyświetla w sposób ciekawy cytat na dziś.
# zmodyfikuj plik źródłowy, tak aby użytkownik mógł podać własną nazwę pliku z cytatami
# plik z cytatami powinen również zawierać informację o autorze, wyświetl cytat i pod spodem autora

import random


lines = "quotes.txt"


def show_quotes():
    with open("quotes.txt", "r") as fopen:
        quote = random.choice(fopen.readlines())
        quote = quote.replace(";", "\n")
        print("*" * (len(quote) + 30))
        print("Your quote for today is: ".center((len(quote) + 30)))
        print(quote.center((len(quote)+30)))
        print("*" * (len(quote) + 30))


show_quotes()


