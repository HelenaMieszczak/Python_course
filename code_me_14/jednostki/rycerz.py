from wojownik import Wojownik


class Rycerz(Wojownik):
    def __init__(self):
        super().__init__()
        self.zycie = 60

    def atakuj(self):
        self.doswiadczenie += 0.3
        print("Machnąłem mieczem")