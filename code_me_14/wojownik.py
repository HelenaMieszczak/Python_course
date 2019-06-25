class Wojownik:
    def __init__(self):
        self.doswiadczenie = 0

    def __repr__(self):
        nazwa = self.__class__.__name__
        return f"\n{nazwa}: \nHP =  {self.zycie} \nEXP =  {self.doswiadczenie}"

    def maszeruj(self, dystans):
        nazwa = self.__class__.__name__
        print(f"{nazwa}: przeszedłem {dystans} m")
        self.doswiadczenie += dystans * 0.2

