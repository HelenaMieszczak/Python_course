# Korzystając z wikipedii utwórz klasy - Kot, Pies, Człowiek.Każda z nich powinna dziedziczyć z nadrzędnej klasy Ssaki.
# Klasa Ssaki powinna dziedziczyć z klasy Zwierzęta.Utwórz obiekty klas - kot, pies i człowiek, udowodnij,
# że rzeczywiście korzystają z klas rodziców.

class Animals:
    def __init__(self):
        print("Animals are multicellular eukaryotic organisms that form the biological kingdom Animalia.")

class Mammals(Animals):
    def __init__(self):
        print('''Mammals (from Latin mamma "breast") are vertebrate animals constituting the class Mammalia (/məˈmeɪliə/), 
            and characterized by the presence of mammary glands 
            which in females produce milk for feeding (nursing) their young, a neocortex (a region of the brain), 
            fur or hair, and three middle ear bones. ''')
        super().__init__()

class Cat(Mammals):
    def __init__(self):
        print("kot")
        super().__init__()

class Dog(Mammals):
    def __init__(self):
        print("pies")

class Human(Mammals):
    def __init__(self):
        print("człowiek")

cat = Cat()


