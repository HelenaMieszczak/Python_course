# Utwórz klasę dla storczyków. Storczyki z zasady mają różne kolory, pory kwitnienia, gatunki.
# Utwórz dowolne atrybuty i metody. Dodaj atrybut wspólny dla wszystkich storczyków - królestwo roślin.
# Utwórz kilka storczyków z różnymi parametrami.

class Orchids:

    kingdom = "Plants"

    def __init__(self, species, colour, blooming):
        self.species = species
        self.colour = colour
        self.blooming = blooming

    def show_orchid(self):
        print(self.species)

    def bloomig_time(self):
        month = input("Enter month of blooming:")
        month.capitalize()
        if month in self.blooming:
            print(self.species)



def main():
    orchid1 = Orchids("Orchis pallens L.", ["yellow", "pale yellow"], ["April", "May", "June"])
    orchid2 = Orchids("Neotinea ustulata (L.)", ["dark red", "dark brown"], ["March", "April", "May", "June"])
    orchid3 = Orchids("Orchis purpurea Huds", ["purple", "brown-red", "white"], ["April", "May"])

    colour = input("Enter the colour of orchid: ")
    if colour in orchid1.colour:
        orchid1.show_orchid()
    elif colour in orchid2.colour:
        orchid2.show_orchid()
    elif colour in orchid3.colour:
        orchid3.show_orchid()
    else:
        print("We don't have the orchid you looking for.")


    # months = input("Months of blooming:")
    # months = months.capitalize()
    # # while months in Orchids:
    # if months in orchid1:
    #     orchid1.bloomig_time()
    # elif months in orchid2.blooming:
    #     orchid2.show_orchid()
    # elif months in orchid3.blooming:
    #     orchid3.show_orchid()
    # else:
    #     print("We don't have the orchid you looking for.")



    # orchid1.bloomig_time()
    # orchid2.bloomig_time()
    # orchid3.bloomig_time()


if __name__ == "__main__":
    main()