#Stwórz listę przedmiotów, które zabierzesz na bezludną wyspę.
#\Wyświetl nazwę właśnie spakowanego przedmiotu, dla po ostatnim przedmiocie pokaż informację: “Great, we are ready!”

amount = int(input("Podaj ilość przedmiotów, które zabierzesz na bezludnś wyspę: "))

i = 0
things = []

for i in range(amount):
    s = input("Napisz, co chcesz zabrać na bezludna wyspę: ")
    print(s)
print("Great, we are ready!")