movie = input("Tytuł flimu: ")
grade = int(input("Ogólna cena filmu w skali 1-10: "))
characterization = int(input("Ocena charakteryzacji w skali 1-10: "))
music = int(input("Ocena muzyki w skali 1-10: "))

average = round((grade + characterization + music) / 3, 2)

print("Średnia Twoich ocen dla tego filmu wynosi: ", average)
