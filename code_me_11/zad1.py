# Skorzystaj z wprowadzenia do OOP. Stwórz klasę Pies, która posiada wspomniane atrybuty oraz metodę.
# atrybuty: imię, kolor sierści, rasę
# metody: szczekaj, machaj ogonem
# Utwórz kilka obiektów klasy Pies z różnymi parametrami.

class Dog:
    def __init__(self, race, name, hair):
        self.race = race
        self.name = name
        self.hair = hair


    def szczekaj(self):
        print(f"{self.name}: hau hau")


def main():
    pies1 = Dog("Pudel", "Reksio", "brązowy")
    pies2 = Dog("Kundelek", "Burek", "niały w łaty")

    pies1.szczekaj()
    pies2.szczekaj()


if __name__ == "__main__":
    main()