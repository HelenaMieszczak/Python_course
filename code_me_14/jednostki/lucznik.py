from wojownik import Wojownik


class Lucznik(Wojownik):
    def __init__(self):
        super().__init__()
        self.zycie = 40
        # self.strz = 15

    # def atakuj(self, strzaly):
    #     self.doswiadczenie += strzaly * 0.4
    #     self.strz -= strzaly
    #     print("Rycerz: wypuscilem " + str(strzaly) + " strzał/" + "zostalo " + str(self.strz))
    #     strzelanie = True
    #     while strzelanie:
    #         if self.strz <= 0:
    #             print("Już nie postrzelasz :(")
    #             strzelanie = False

    def atakuj(self):
        print('Łucznik: Wypuściłem strzałę!')
        self.doswiadczenie += 0.4
        # strzaly = self.strz

        # strzelanie = True
        # while strzelanie:
        #     if self.strz <= 0:
        #         print("Już nie postrzelasz :(")
        #         strzelanie = False

