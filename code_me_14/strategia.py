from jednostki.rycerz import Rycerz
from jednostki.lucznik import Lucznik


def main():
    ryc = Rycerz()
    print(ryc)
    ryc.maszeruj(10)
    print(ryc)
    ryc.atakuj()
    print(ryc)

    luc = Lucznik()
    print(luc)
    luc.atakuj()
    print(luc)

if __name__ == '__main__':
    main()