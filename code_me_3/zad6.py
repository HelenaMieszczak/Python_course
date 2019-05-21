#Stwórz listę przedmiotów, które zabierzesz na bezludną wyspę.
#\Wyświetl nazwę właśnie spakowanego przedmiotu, dla po ostatnim przedmiocie pokaż informację: “Great, we are ready!”

amount = int(input("Podaj ilość przedmiotów, które zabierzesz w góry: "))

i = 0
things = []

for i in range(amount):
    s = input("Napisz, co chcesz zabrać góry: ")
    print(s)
print("Great, we are ready!")